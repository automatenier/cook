import pandas as pd
import gspread
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", ".pass/service_account.json")
SHEET_ID = os.getenv("GSHEET_ID", "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8")
EXCEL_PATH = r"___Data\A JOCONS\Product\JO_Onboard.xlsx"

def migrate_onboarding():
    try:
        # 1. Read Excel
        print(f"Reading Excel: {EXCEL_PATH}...")
        df = pd.read_excel(EXCEL_PATH, sheet_name="Sprint SOP")
        
        # Clean data for JSON/GSheet compatibility
        df = df.fillna('')
        data_to_upload = [df.columns.values.tolist()] + df.values.tolist()

        # 2. Connect to GSheets
        print(f"Connecting to Google Sheets ID: {SHEET_ID}...")
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        sh = gc.open_by_key(SHEET_ID)

        # 3. Create or Update "Sprint" tab
        try:
            ws = sh.worksheet("Sprint")
            print("Found existing 'Sprint' tab. Clearing...")
            ws.clear()
        except gspread.exceptions.WorksheetNotFound:
            print("Creating new 'Sprint' tab...")
            ws = sh.add_worksheet(title="Sprint", rows="100", cols="20")

        ws.update("A1", data_to_upload)
        print(f"Successfully migrated {len(df)} rows to 'Sprint' tab.")

    except Exception as e:
        print(f"Migration failed: {e}")

if __name__ == "__main__":
    migrate_onboarding()
