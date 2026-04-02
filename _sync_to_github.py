# C:\Users\natha\Cook\___Data\B Real Estate\_sync_to_github.py
import json, os, datetime
import gspread
import google.oauth2.service_account as sac

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SA_FILE = r"C:\Users\natha\Cook\_____AI_INFRA\.pass\Archive\service_account.json"

# Google Sheets Config
SHEET_IDS = {
    "crm":     "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8",
    "content": "1ryyHlW8m_7pla68VLp8wXkpnPmj6uX8DxyICjN4cqGQ",
}
CRM_TABS = {"WA": "WhatsApp", "Meta": "Meta Ads", "Tiktok": "TikTok", "LKDN": "LinkedIn", "Email": "Email"}

def fetch_crm(gc):
    print("Fetching CRM...")
    wb = gc.open_by_key(SHEET_IDS["crm"])
    all_records = []
    
    def norm(headers, row, tab, rownum):
        rec = {"channel": CRM_TABS.get(tab, tab), "row": rownum}
        for h, v in zip(headers, row):
            h, v = h.strip(), v.strip()
            if not h: continue
            if h == "3-Username":         rec["name"] = v
            elif h == "Phone Number":    rec["phone"] = v
            elif h == "5-Status":        rec["status"] = v
            elif h == "9--Booked":       rec["booked"] = v.upper() == "TRUE"
            elif h == "11-Close":        rec["close_status"] = v
            elif h == "16-Context DM":  rec["context"] = v
            elif h == "FU Date":         rec["fu_date"] = v
            elif h == "Source":          rec["source"] = v
        return rec if rec.get("name") or rec.get("phone") else None

    for ws in wb.worksheets():
        if ws.title in CRM_TABS:
            rows = ws.get_all_values()
            if not rows: continue
            headers = rows[0]
            for i, row in enumerate(rows[1:], start=2):
                rec = norm(headers, row, ws.title, i)
                if rec: all_records.append(rec)
    return all_records

def fetch_content(gc):
    print("Fetching Content Calendar...")
    wb = gc.open_by_key(SHEET_IDS["content"])
    records = []
    for ws in wb.worksheets():
        if ws.title in ("Calendar March", "April Calendar", "Footage"):
            rows = ws.get_all_values()
            if not rows or len(rows) < 2: continue
            headers = rows[0]
            for i, row in enumerate(rows[1:], start=2):
                if not any(row): continue
                rec = {"tab": ws.title, "row": i}
                for h, v in zip(headers, row):
                    key = h.lower().replace(" ", "_")[:30]
                    rec[key] = v
                records.append(rec)
    return records

if __name__ == "__main__":
    try:
        scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]
        credentials = sac.Credentials.from_service_account_info(json.load(open(SA_FILE)), scopes=scopes)
        gc = gspread.authorize(credentials)
        
        crm_data = fetch_crm(gc)
        content_data = fetch_content(gc)
        
        with open(os.path.join(BASE_DIR, "data_crm.json"), "w") as f:
            json.dump(crm_data, f, indent=2)
            
        with open(os.path.join(BASE_DIR, "data_content.json"), "w") as f:
            json.dump(content_data, f, indent=2)
            
        print(f"Success! {len(crm_data)} CRM records and {len(content_data)} Content records exported.")
    except Exception as e:
        print(f"Error: {e}")
