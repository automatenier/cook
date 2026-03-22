import gspread
import os
import json
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = ".pass/service_account.json"
SHEET_ID = "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8"

def list_tabs():
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open_by_key(SHEET_ID)
    print("Available tabs:")
    for ws in sh.worksheets():
        print(f"- '{ws.title}' (ID: {ws.id})")

if __name__ == "__main__":
    list_tabs()
