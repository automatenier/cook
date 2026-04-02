# H:\My Drive\Cook\___Data\B Real Estate\_serve_sheets.py
# Updated: multi-tab CRM + Content Calendar sheet
# Run: py -3 _serve_sheets.py

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json, datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

# ── Google Sheets auth ────────────────────────────────────────────────────────
import gspread
import google.oauth2.service_account as sac

SA_FILE = r"C:\Users\natha\Cook\_____AI_INFRA\.pass\Archive\service_account.json"
SCOPES  = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]
with open(SA_FILE) as f:
    creds = json.load(f)
credentials = sac.Credentials.from_service_account_info(creds, scopes=SCOPES)
gc = gspread.authorize(credentials)

SHEET_IDS = {
    "crm":     "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8",
    "content": "1ryyHlW8m_7pla68VLp8wXkpnPmj6uX8DxyICjN4cqGQ",
}

CRM_TABS = {"WA": "WhatsApp", "Meta": "Meta Ads", "Tiktok": "TikTok", "LKDN": "LinkedIn", "Email": "Email"}

# ── Fetch CRM (all 5 tabs) ───────────────────────────────────────────────────
def fetch_crm():
    wb = gc.open_by_key(SHEET_IDS["crm"])
    all_records = []

    def norm(headers, row, tab, rownum):
        rec = {"channel": CRM_TABS.get(tab, tab), "row": rownum}
        for h, v in zip(headers, row):
            h, v = h.strip(), v.strip()
            if not h or not v:
                continue
            if h == "3-Username":         rec["name"]          = v
            elif h == "Phone Number":    rec["phone"]         = v
            elif h == "Status":          rec["temperature"]    = v
            elif h == "5-Status":        rec["status"]         = v
            elif h == "4-leadType":      rec["lead_type"]      = v
            elif h == "Source":          rec["source"]         = v
            elif h == "FU Date":         rec["fu_date"]        = v
            elif h == "9--Booked":       rec["booked"]         = v.upper() == "TRUE"
            elif h == "10-Show":        rec["show_flag"]      = v.upper() == "TRUE"
            elif h == "11-Close":        rec["close_status"]   = v
            elif h == "12-Close Rate":  rec["close_rate"]     = v
            elif h == "14-Close Date":  rec["close_date"]     = v
            elif h == "15-Lead To Close":rec["lead_to_close"]  = v
            elif h == "16-Context DM":  rec["context"]        = v
            elif h == "24-CNV":         rec["booked"]         = v.upper() == "TRUE"
            elif h == "13-Leadate":     rec["lead_date"]      = v
            elif h == "2-24-Convo":     rec["convo"]          = v
        return rec if rec.get("name") or rec.get("phone") else None

    for ws in wb.worksheets():
        tab = ws.title
        if tab not in CRM_TABS:
            continue
        rows = ws.get_all_values()
        if not rows:
            continue
        headers = rows[0]
        for i, row in enumerate(rows[1:], start=2):
            if len(row) < 3 or all(v.strip() == "" for v in row):
                continue
            rec = norm(headers, row, tab, i)
            if rec:
                all_records.append(rec)

    all_records.sort(key=lambda r: -r["row"])
    return all_records

# ── Fetch Content Calendar ─────────────────────────────────────────────────────
def fetch_content_calendar():
    wb = gc.open_by_key(SHEET_IDS["content"])
    records = []
    for ws in wb.worksheets():
        tab = ws.title
        # Included new tabs and kept old ones for backward compatibility
        if tab not in ("Calendar March", "Stories March", "Footage", "Production Pipeline", "April Calendar"):
            continue
        rows = ws.get_all_values()
        if not rows or len(rows) < 2:
            continue
        headers = rows[0]
        for i, row in enumerate(rows[1:], start=2):
            if not any(row):
                continue
            rec = {"tab": tab, "row": i}
            for h, v in zip(headers, row):
                h, v = h.strip(), v.strip()
                if not h:
                    continue
                # Normalize key names
                key = h.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")[:40]
                rec[key] = v
            # Ensure we have at least some descriptive data
            if rec.get("title") or rec.get("id") or rec.get("date"):
                records.append(rec)
    
    # Sort by date if available, otherwise by row
    records.sort(key=lambda r: (r.get("date", ""), r.get("row", 0)))
    return records

_cache = {"crm": None, "content_calendar": None, "cache_time": None}
CACHE_TTL = 120

def get_cached(key, fetcher):
    now = datetime.datetime.now()
    if _cache[key] is None or _cache["cache_time"] is None \
       or (now - _cache["cache_time"]).total_seconds() > CACHE_TTL:
        print(f"[{now.strftime('%H:%M:%S')}] Fetching {key}...")
        _cache[key] = fetcher()
        _cache["cache_time"] = now
        print(f"  -> {len(_cache[key])} records")
    return _cache[key]

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/crm":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            data = get_cached("crm", fetch_crm)
            self.wfile.write(json.dumps(data).encode())
            return
        if self.path == "/api/content-calendar":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            data = get_cached("content_calendar", fetch_content_calendar)
            self.wfile.write(json.dumps(data).encode())
            return
        if self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "time": datetime.datetime.now().isoformat()}).encode())
            return
        # serve files from this dir
        path = self.path.split("?")[0]
        if path == "/":
            path = "/index.html"
        fpath = os.path.join(os.path.dirname(__file__), path.lstrip("/"))
        if os.path.isfile(fpath):
            self.path = fpath
        return SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, fmt, *args):
        print(f"[HTTP] {args[0]}")

if __name__ == "__main__":
    print("[START] Connecting to Google Sheets...")
    _cache["crm"] = fetch_crm()
    _cache["content_calendar"] = fetch_content_calendar()
    _cache["cache_time"] = datetime.datetime.now()
    print(f"[READY] CRM: {len(_cache['crm'])} records | Content Calendar: {len(_cache['content_calendar'])} records")
    PORT = 3456
    print(f"[SERV]  http://localhost:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
