import gspread
from supabase import create_client
import os
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

# --- CONFIG ---
SHEET_IDS = [
    "1TsCCRHzPSLAuyZRB3h7F4zyugFbqbYxN4L4uXHEa0G8", # Agency-BIZ
    "1BCfwdILicqu6dC824Vvdbnqzwc18-FWGc2Y37sUdRVE", # Scrape
    "18_zwGJOdQ0_dthFW_zgf0Jz7h7ZWAk-33TENlX6N1Qc", # Talent EOD
    "1yQlVoPhL1qP1_py7_2uoSVaKgICfERmwlcyTTQgW2jc", # AI EOD
    "1ryyHlW8m_7pla68VLp8wXkpnPmj6uX8DxyICjN4cqGQ", # Content Asset
    "1JLiEJkV3-FbMkOS9-DOUOD1_N3vBcY08Rrgl41QMM14", # Client Sheet
    "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8"  # CRM
]

SERVICE_ACCOUNT_FILE = ".pass/service_account.json"
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xmfkewjxjsrffvmlcsid.supabase.co")
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtZmtld2p4anNyZmZ2bWxjc2lkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MzkxNTI2MSwiZXhwIjoyMDg5NDkxMjYxfQ.Ra00Q2VbWhp-303XVjn4-94D1QUjFv-2rb9-sarrk98"

def get_records_safe(ws):
    """Fetch all records safely even if headers are duplicates or empty."""
    data = ws.get_all_values()
    if not data: return []
    
    raw_headers = data[0]
    headers = []
    seen = {}
    
    for i, h in enumerate(raw_headers):
        h = h.strip()
        if not h:
            h = f"EmptyCol_{i}"
        if h in seen:
            seen[h] += 1
            h = f"{h}_{seen[h]}"
        else:
            seen[h] = 0
        headers.append(h)
        
    records = []
    for row in data[1:]:
        record = {}
        for i, h in enumerate(headers):
            val = row[i] if i < len(row) else ""
            record[h] = val
        records.append(record)
    return records

def sync_gsheets_to_supabase():
    try:
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        all_final_payloads = []

        for sid in SHEET_IDS:
            print(f"\n--- Syncing Spreadsheet: {sid} ---")
            try:
                sh = gc.open_by_key(sid)
                sheet_title = sh.title
                
                for ws in sh.worksheets():
                    try:
                        tab_name = ws.title
                        records = get_records_safe(ws)
                        if not records: continue
                        
                        print(f"  [{sheet_title}] {tab_name}: {len(records)} rows.")

                        for idx, r in enumerate(records):
                            unique_id = f"{sid}_{tab_name}_{idx}"
                            display_name = str(r.get('3-Username') or r.get('Name') or r.get('Customer Name') or r.get('Task Name') or unique_id).strip()
                            
                            payload = {
                                "name": unique_id,
                                "phone": display_name[:250], # Ensure it fits
                                "status": tab_name[:250],
                                "context": json.dumps({
                                    "sheet_id": sid,
                                    "sheet_title": sheet_title,
                                    "tab_name": tab_name,
                                    "row_data": r
                                }),
                                "updated_at": datetime.now(timezone.utc).isoformat()
                            }
                            all_final_payloads.append(payload)

                    except Exception as e:
                        print(f"    Error in tab {ws.title}: {e}")
            except Exception as e:
                print(f"  Error opening spreadsheet {sid}: {e}")

        if all_final_payloads:
            batch_size = 1000
            supabase.table("leads").delete().neq("name", "TEMP_DUMMY").execute()
            print(f"\nCleared Supabase. Syncing {len(all_final_payloads)} rows...")

            for i in range(0, len(all_final_payloads), batch_size):
                batch = all_final_payloads[i:i + batch_size]
                supabase.table("leads").upsert(batch, on_conflict="name").execute()
                print(f"  Synced batch {i//batch_size + 1}")
            
            print("Successfully synced all sheets.")
        else:
            print("No data found.")

    except Exception as e:
        print(f"Global Sync failed: {e}")

if __name__ == "__main__":
    sync_gsheets_to_supabase()
