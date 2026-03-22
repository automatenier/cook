"""
content_approve.py
------------------
Watches Content_Tracker.xlsx. When you change a row's Status from
"review" → "approved", this script:
  1. Moves the .md file from 03_HMN_REVIEW/[client]/ → 05_VLT_FINAL/[client]/[YYYY-MM]/
  2. Writes the Final_Path and Approved_Date back into the tracker.

Usage:
  py -3 AI_Tools/content_approve.py

Run this any time after you update statuses in the Excel file.
"""

import os
import shutil
from datetime import date
from pathlib import Path

import openpyxl

# ── Paths ────────────────────────────────────────────────────────────────────
CONTENT_ROOT  = Path(__file__).parent.parent / "Content"
TRACKER_PATH  = CONTENT_ROOT / "Content_Tracker.xlsx"
REVIEW_DIR    = CONTENT_ROOT / "03_HMN_REVIEW"
FINAL_DIR     = CONTENT_ROOT / "05_VLT_FINAL"

# ── Column map (1-indexed, matches the header row) ───────────────────────────
COL = {
    "id":            1,
    "client":        2,
    "month":         3,
    "post_date":     4,
    "slug":          5,
    "type":          6,
    "status":        7,
    "script_path":   8,
    "final_path":    9,
    "approved_date": 10,
    "notes":         11,
}

def move_to_final(client: str, month: str, filename: str) -> Path | None:
    """Move file from 03_HMN_REVIEW/[client]/ to 05_VLT_FINAL/[client]/[month]/."""
    src = REVIEW_DIR / client / filename
    if not src.exists():
        print(f"  ⚠  Not found in review: {src}")
        return None

    dest_dir = FINAL_DIR / client / month
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / filename

    shutil.move(str(src), str(dest))
    print(f"  ✓  Moved → {dest.relative_to(CONTENT_ROOT)}")
    return dest

def main():
    if not TRACKER_PATH.exists():
        print(f"Tracker not found: {TRACKER_PATH}")
        return

    wb = openpyxl.load_workbook(TRACKER_PATH)
    ws = wb.active

    today = date.today().isoformat()
    moved = 0

    for row in ws.iter_rows(min_row=2):  # skip header
        status     = row[COL["status"] - 1].value
        final_path = row[COL["final_path"] - 1].value

        if str(status).strip().lower() != "approved":
            continue
        if final_path:  # already processed
            continue

        client   = str(row[COL["client"] - 1].value or "").strip()
        month    = str(row[COL["month"] - 1].value or "").strip()
        slug     = str(row[COL["slug"] - 1].value or "").strip()
        filename = f"{slug}.md"

        print(f"Processing: {client} / {slug}")
        dest = move_to_final(client, month, filename)

        if dest:
            rel = str(dest.relative_to(CONTENT_ROOT))
            row[COL["final_path"] - 1].value    = rel
            row[COL["approved_date"] - 1].value = today
            moved += 1

    wb.save(TRACKER_PATH)
    print(f"\nDone — {moved} file(s) moved to 05_VLT_FINAL and tracker updated.")

if __name__ == "__main__":
    main()
