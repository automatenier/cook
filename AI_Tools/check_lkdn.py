import gspread
import os
import json
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = ".pass/service_account.json"
SHEET_ID = "1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8"

def check_lkdn_cols():
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open_by_key(SHEET_ID)
    ws = sh.worksheet("LKDN")
    headers = ws.row_values(1)
    print(f"Headers for LKDN: {headers}")
    
    first_row = ws.get_all_records()
    if first_row:
        print(f"First record sample: {first_row[0]}")

if __name__ == "__main__":
    check_lkdn_cols()
