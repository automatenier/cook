#!/usr/bin/env python3
import gspread
from pathlib import Path

def test_conn():
    try:
        print("Authenticating with gspread.oauth()...")
        gc = gspread.oauth()
        print("Creating a test sheet...")
        sh = gc.create("GEMINI_TEST_SHEET")
        print(f"SUCCESS! Created sheet: {sh.url}")
        # Delete it to clean up
        # gc.del_spreadsheet(sh.id)
        return True
    except Exception as e:
        print(f"FAILED: {e}")
        return False

if __name__ == "__main__":
    test_conn()
