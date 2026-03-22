#!/usr/bin/env python3
"""
Skill Evaluator & Optimization Logger
=======================================
Logs skill optimization runs and scores to a Google Sheet.
Uses service_account.json for authentication.

Usage: py -3 AI_Tools/skill_evaluator.py --skill source-analyst --score 9 --notes "Added P.A.R.T. and CoV"
"""

import argparse
import gspread
from pathlib import Path
from datetime import datetime
import os

# Paths
CREDENTIALS_FILE = Path(".pass/service_account.json")
SHEET_NAME = "Agent_Skill_Optimization_Log"

def get_args():
    parser = argparse.ArgumentParser(description="Log skill evaluation results.")
    parser.add_argument("--skill", required=True, help="Name of the skill being evaluated.")
    parser.add_argument("--score", type=int, default=0, help="Performance score (1-10).")
    parser.add_argument("--notes", default="", help="Optimization notes.")
    return parser.parse_args()

def log_to_sheet(skill, score, notes):
    try:
        if not CREDENTIALS_FILE.exists():
            print(f"ERROR: Credentials not found at {CREDENTIALS_FILE}")
            return False

        # Authenticate
        gc = gspread.service_account(filename=str(CREDENTIALS_FILE))
        
        # Open or Create Spreadsheet
        try:
            sh = gc.open(SHEET_NAME)
        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Creating new spreadsheet: {SHEET_NAME}")
            sh = gc.create(SHEET_NAME)
            # Share it with the human's email (jordanmathew1223@gmail.com)
            # You might need to change this depending on the user's setup
            # sh.share("jordanmathew1223@gmail.com", perm_type='user', role='writer')
            ws = sh.get_worksheet(0)
            ws.append_row(["Date", "Skill", "Score (1-10)", "Notes"])
            ws.update_cell(1, 1, "Date") # Ensure headers
        
        ws = sh.get_worksheet(0)
        
        # Log entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ws.append_row([timestamp, skill, score, notes])
        
        print(f"SUCCESS: Logged optimization for '{skill}' with score {score} to {sh.url}")
        return True
    except Exception as e:
        print(f"FAILED to log to Google Sheets: {e}")
        return False

if __name__ == "__main__":
    args = get_args()
    log_to_sheet(args.skill, args.score, args.notes)
