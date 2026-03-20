import gspread
from supabase import create_client
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# --- CONFIG ---
# Use environment variable for the JSON content if available, otherwise fallback to local file
SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", ".pass/service_account.json")
SHEET_ID = os.getenv("GSHEET_ID", "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8")

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xmfkewjxjsrffvmlcsid.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtZmtld2p4anNyZmZ2bWxjc2lkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MzkxNTI2MSwiZXhwIjoyMDg5NDkxMjYxfQ.Ra00Q2VbWhp-303XVjn4-94D1QUjFv-2rb9-sarrk98")

def sync_gsheets_to_supabase():
    try:
        # 1. Fetch from Google Sheets
        if SERVICE_ACCOUNT_JSON:
            # For GitHub Actions: Use JSON string from secrets
            creds_dict = json.loads(SERVICE_ACCOUNT_JSON)
            gc = gspread.service_account_from_dict(creds_dict)
        else:
            # Local: Use file
            gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
            
        sh = gc.open_by_key(SHEET_ID)
        
        # Explicitly target ONLY the 'CRM' worksheet
        ws = sh.worksheet("CRM")
        records = ws.get_all_records()
        print(f"Fetched {len(records)} rows from worksheet 'CRM'.")

        all_payloads = []
        # Process & Sync
        for r in records:
                # Map columns accurately
                name = str(r.get('3-Username', '')).strip()
                if not name:
                    continue
                
                # Try multiple possible phone column names
                phone = str(r.get('Phone Number') or r.get('Column 17') or r.get('6-WA Number') or r.get('phone') or '-')
                # Clean up phone number (remove spaces, etc if needed, but keeping original format for now)
                if phone == '0' or phone == 'None':
                    phone = '-'
                    
                payload = {
                    "name": name,
                    "phone": phone,
                    "status": str(r.get('5-Status', '-')),
                    "booked": str(r.get('9--Booked', '')).upper() == 'TRUE',
                    "close_status": str(r.get('11-Close', '-')),
                    "context": f"{ws.title}: {str(r.get('13-Leadate', '-'))}",
                    "updated_at": datetime.utcnow().isoformat()
                }
                all_payloads.append(payload)

        # 3. Deduplicate by name (Python side) before upsert
        unique_payloads = {}
        for p in all_payloads:
            name = p['name']
            if name not in unique_payloads:
                unique_payloads[name] = p
            else:
                # Merge logic: If existing lead has no phone, but current one does, update it
                if (unique_payloads[name]['phone'] == '-' or not unique_payloads[name]['phone']) and p['phone'] != '-':
                    unique_payloads[name]['phone'] = p['phone']
                
                # Also keep the most descriptive context if possible
                if p['context'].startswith('WA:') and not unique_payloads[name]['context'].startswith('WA:'):
                     unique_payloads[name]['context'] = p['context']
        
        payload_list = list(unique_payloads.values())

        # 4. Connect to Supabase
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        # 5. Upsert (Bulk)
        # We use 'name' as the unique key for upserting
        if payload_list:
            result = supabase.table("leads").upsert(payload_list, on_conflict="name").execute()
            print(f"Successfully synced {len(payload_list)} total unique leads to Supabase cloud.")
        else:
            print("No leads found to sync.")

    except Exception as e:
        print(f"Sync failed: {e}")

if __name__ == "__main__":
    sync_gsheets_to_supabase()
