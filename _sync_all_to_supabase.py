# H:\My Drive\Cook\___Data\B Real Estate\_sync_all_to_supabase.py
# Syncs Google Sheets CRM + Content Asset to Supabase
# Run: py -3 _sync_all_to_supabase.py
# Note: Requires network access to Supabase (xmfkewjxjsrffvmlcsid.supabase.co)

import json, urllib.request, urllib.error
from datetime import datetime

# ── Google Sheets auth ────────────────────────────────────────────────────────
import gspread
import google.oauth2.service_account as sac

SA_FILE = r"H:\My Drive\Cook\_____AI_INFRA\.pass\Archive\service_account.json"
SCOPES   = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]

with open(SA_FILE) as f:
    creds = json.load(f)
credentials = sac.Credentials.from_service_account_info(creds, scopes=SCOPES)
gc = gspread.authorize(credentials)

# ── Supabase config ────────────────────────────────────────────────────────────
SB_URL  = "https://xmfkewjxjsrffvmlcsid.supabase.co"
SB_KEY  = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtZmtewjxanNyZmZ2bWxjc2lkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM5MTUyNjEsImV4cCI6MjA4OTQ5MTI2MX0.Ra00Q2VbWhp-303XVjn4-94D1QUjFv-2rb9-sarrk98"

def sb_headers():
    return {
        "apikey": SB_KEY,
        "Authorization": f"Bearer {SB_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

def upsert_records(table, records):
    """Upsert records to Supabase using REST API"""
    url = f"{SB_URL}/rest/v1/{table}"
    data = json.dumps(records).encode()
    req = urllib.request.Request(url, data=data, headers=sb_headers())
    req.add_header("Upsert", "id=eq.{id}")
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        return resp.status, resp.read().decode()[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:500]
    except Exception as e:
        return "NETWORK_ERROR", str(e)

# ── Sheet 1: CRM ──────────────────────────────────────────────────────────────
print("[1/2] Reading CRM sheet...")
CRM_SHEET_ID = "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8"

try:
    sheet = gc.open_by_key(CRM_SHEET_ID)
    rows  = sheet.sheet1.get_all_values()

    if not rows:
        print("  -> CRM sheet is empty!")
    else:
        headers = rows[0]
        records = []
        for i, row in enumerate(rows[1:], start=2):
            if len(row) < 3 or all(v.strip() == "" for v in row):
                continue
            rec = {}
            for h, v in zip(headers, row):
                clean_h = h.strip()
                if not clean_h or not v.strip():
                    continue
                if clean_h == "3-Username":
                    rec["name"] = v.strip()
                elif clean_h == "Phone Number":
                    rec["phone"] = v.strip()
                elif clean_h == "Status":
                    rec["temperature"] = v.strip()
                elif clean_h == "5-Status":
                    rec["status"] = v.strip()
                elif clean_h == "4-leadType":
                    rec["lead_type"] = v.strip()
                elif clean_h == "Source":
                    rec["source"] = v.strip()
                elif clean_h == "FU Date":
                    rec["fu_date"] = v.strip()
                elif clean_h == "9--Booked":
                    rec["booked"] = v.strip().upper() == "TRUE"
                elif clean_h == "10-Show":
                    rec["show_flag"] = v.strip().upper() == "TRUE"
                elif clean_h == "11-Close":
                    rec["close_status"] = v.strip()
                elif clean_h == "12-Close Rate":
                    try:
                        rec["close_rate"] = float(v.strip().replace("%",""))
                    except:
                        pass
                elif clean_h == "14-Close Date":
                    rec["close_date"] = v.strip()
                elif clean_h == "15-Lead To Close":
                    rec["lead_to_close_days"] = v.strip()
                elif clean_h == "16-Context DM":
                    rec["context"] = v.strip()
                elif clean_h == "24-CNV":
                    rec["booked"] = v.strip().upper() == "TRUE"
                elif clean_h == "13-Leadate":
                    rec["lead_date"] = v.strip()

            if rec.get("name") or rec.get("phone"):
                rec["id"] = rec.get("name", "")[:50] + "_" + str(i)
                rec["updated_at"] = datetime.utcnow().isoformat() + "Z"
                rec["context"] = rec.get("context", "") + f" | sheet_row:{i} | sheet_id:{CRM_SHEET_ID}"
                records.append(rec)

        print(f"  -> {len(records)} CRM records extracted")
        if records:
            status, msg = upsert_records("leads", records)
            print(f"  -> CRM upsert status: {status}")
            if status != 200 and status != 201 and status != 204:
                print(f"  -> Response: {msg}")
except Exception as e:
    print(f"  -> CRM error: {e}")

# ── Sheet 2: Content Asset ────────────────────────────────────────────────────
print("\n[2/2] Reading Content Asset sheet...")
CONTENT_SHEET_ID = "1ryyHlW8m_7pla68VLp8wXkpnPmj6uX8DxyICjN4cqGQ"

try:
    sheet = gc.open_by_key(CONTENT_SHEET_ID)
    rows  = sheet.sheet1.get_all_values()

    if not rows:
        print("  -> Content Asset sheet is empty!")
    else:
        headers = rows[0]
        records = []
        for i, row in enumerate(rows[1:], start=2):
            if len(row) < 2 or all(v.strip() == "" for v in row):
                continue
            rec = {}
            for h, v in zip(headers, row):
                clean_h = h.strip()
                if not clean_h or not v.strip():
                    continue
                if "title" in clean_h.lower() or "name" in clean_h.lower():
                    rec["title"] = v.strip()
                elif "status" in clean_h.lower() or "stage" in clean_h.lower():
                    rec["stage"] = v.strip()
                elif "platform" in clean_h.lower() or "channel" in clean_h.lower():
                    rec["platform"] = v.strip()
                elif "hook" in clean_h.lower():
                    rec["hook"] = v.strip()
                elif "script" in clean_h.lower():
                    rec["script"] = v.strip()
                elif "due" in clean_h.lower() or "date" in clean_h.lower():
                    rec["due_date"] = v.strip()
                elif "editor" in clean_h.lower():
                    rec["editor"] = v.strip()
                elif "type" in clean_h.lower():
                    rec["content_type"] = v.strip()
                else:
                    # capture any other field
                    key = clean_h.lower().replace(" ", "_")[:30]
                    rec[key] = v.strip()

            if rec.get("title"):
                rec["id"] = rec["title"][:50] + f"_{i}"
                rec["updated_at"] = datetime.utcnow().isoformat() + "Z"
                rec["context"] = f"sheet_row:{i} | sheet_id:{CONTENT_SHEET_ID}"
                records.append(rec)

        print(f"  -> {len(records)} Content Asset records extracted")
        if records:
            status, msg = upsert_records("content_assets", records)
            print(f"  -> Content Asset upsert status: {status}")
            if status != 200 and status != 201 and status != 204:
                print(f"  -> Response: {msg}")
except Exception as e:
    print(f"  -> Content Asset error: {e}")

print("\n[DONE] Sync complete.")
