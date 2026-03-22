import gspread
from pathlib import Path

def check_access():
    SERVICE_ACCOUNT_FILE = "service_account.json"
    try:
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        print("Service Account connected.")
        
        # List all files visible to the service account
        files = gc.list_spreadsheet_files()
        print(f"Visible spreadsheets: {len(files)}")
        for f in files:
            print(f" - {f['name']} (ID: {f['id']})")
            
        # Try to create a tiny test sheet to see if quota is still an issue
        try:
            sh = gc.create("QUOTA_TEST")
            print(f"Success! Created test sheet: {sh.url}")
            gc.del_spreadsheet(sh.id)
        except Exception as e:
            print(f"Quota test failed: {e}")

    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    check_access()
