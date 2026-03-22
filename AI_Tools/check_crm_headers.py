
import gspread
import os

def list_all_sheets():
    creds_path = '.pass/service_account.json'
    if not os.path.exists(creds_path):
        print(f"Error: {creds_path} not found")
        return

    client = gspread.service_account(filename=creds_path)
    spreadsheet_id = '1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8'
    sh = client.open_by_key(spreadsheet_id)
    
    for ws in sh.worksheets():
        headers = ws.row_values(1)
        print(f"Sheet: {ws.title} (ID: {ws.id})")
        print(f"Headers: {headers}\n")

if __name__ == "__main__":
    list_all_sheets()
