"""
sync_jocons_calendar.py
-----------------------
Scans VLT_Content/02_HMN_HUMANFLOW/jocons/[client]/projects/[month]/scripts and approved/ for .md files,
matches them to rows in the content calendar by date,
and updates Script Real + Status columns.

Usage:
    py -3 AI_Tools/sync_jocons_calendar.py --client fadli --month 2026-03
    py -3 AI_Tools/sync_jocons_calendar.py --client fadli --month 2026-03 --dry-run
"""
import sys
import os
import re
import argparse
from pathlib import Path
from datetime import date

import openpyxl

# â”€â”€ Paths â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
ROOT         = Path(__file__).parent.parent    
CALENDAR     = ROOT / "PDCT_JO_Consult/4_Content_Calendar/JOCons_Content_Calendar.xlsx"

# Column positions (1-indexed)
COL_DATE        = 1   # Post Date
COL_STATUS      = 2   # Status
COL_LINK_OUT    = 3   # Link Outliers
COL_TYPE        = 4   # Type
COL_VISUAL_HOOK = 5   # Visual Hook
COL_SCRIPT_AI   = 6   # Script AI
COL_SCRIPT_REAL = 7   # Script Real
COL_FOOTAGE_AI  = 8   # Footage AI
COL_FOOTAGE     = 9   # Footage

# Status progression â€” only advance, never go back
STATUS_RANK = {
    "Not Started": 0,
    "In Progress": 1,
    "Script Done": 2,
    "Filmed":      3,
    "Edited":      4,
    "Posted":      5,
}

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")  


def parse_date(filename: str):
    """Extract date from filename like 2026-02-27_type_slug.md"""
    m = DATE_RE.match(filename)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))  
    except ValueError:
        return None


def collect_scripts(client, month):
    """Return dict: {date: (relative_path, target_status)}"""
    found = {}
    
    base_project_dir = ROOT / f"VLT_Content/02_HMN_HUMANFLOW/jocons/{client}/projects/{month}"
    scripts_dir = base_project_dir / "scripts"
    approved_dir = base_project_dir / "approved"

    for folder, target_status in [(scripts_dir, "Script Done"), (approved_dir, "Edited")]:    
        if not folder.exists():
            print(f"  [INFO] Folder not found: {folder}")
            continue
        for f in sorted(folder.glob("*.md")):  
            if f.name.startswith("_"):
                continue  # skip _README etc   
            d = parse_date(f.name)
            if not d:
                continue
            rel_path = str(f.relative_to(ROOT)).replace("\\", "/")
            # Approved takes priority over scripts for the same date
            if d not in found or target_status == "Edited":
                found[d] = (rel_path, target_status)

    return found


def set_status(current: str, new_status: str) -> str:
    """Only advance status, never go backwards."""
    current_rank = STATUS_RANK.get(current, 0) 
    new_rank     = STATUS_RANK.get(new_status, 0)
    return new_status if new_rank > current_rank else current


def sync(client, month, dry_run=False):
    if not CALENDAR.exists():
        print(f"ERROR: Calendar not found at {CALENDAR}")
        sys.exit(1)

    scripts = collect_scripts(client, month)
    if not scripts:
        print(f"No valid script files found for {client} in {month} â€” nothing to sync.")
        return

    wb = openpyxl.load_workbook(CALENDAR)      
    ws = wb.active

    updated = 0
    skipped = 0

    for row in ws.iter_rows(min_row=2):        
        date_cell = row[COL_DATE - 1]
        if not date_cell.value:
            continue

        # Normalise to date object
        cell_date = date_cell.value
        if hasattr(cell_date, "date"):
            cell_date = cell_date.date()       

        if cell_date not in scripts:
            skipped += 1
            continue

        rel_path, target_status = scripts[cell_date]
        current_status = row[COL_STATUS - 1].value or "Not Started"
        new_status     = set_status(current_status, target_status)

        if dry_run:
            print(f"  [DRY] {cell_date} | Status: {current_status} -> {new_status} | Script Real: {rel_path}")
        else:
            row[COL_SCRIPT_REAL - 1].value = rel_path
            row[COL_STATUS - 1].value      = new_status
            updated += 1
            print(f"  [OK] {cell_date} -> {new_status} | {rel_path}")

    if not dry_run:
        wb.save(CALENDAR)
        print(f"\nSync complete. {updated} rows updated, {skipped} dates skipped.")   
    else:
        print(f"\nDry run complete. {len(scripts)} scripts found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync scripts to the JO Consult calendar")
    parser.add_argument("--client", required=True, help="Client name (e.g., fadli)")
    parser.add_argument("--month", required=True, help="Month folder (e.g., 2026-03)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    print(f"Calendar : {CALENDAR}")
    print(f"Client   : {args.client}")
    print(f"Month    : {args.month}")
    print()
    sync(args.client, args.month, dry_run=args.dry_run)
