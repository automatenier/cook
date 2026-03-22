"""
cook_gcal_reverse_sync.py
-------------------------
Pull events from Google Calendar (today/future) and add them to the 
Obsidian Kanban (Command.md) if they are not already there.

Logic:
  1. Fetch GCal events from today onwards.
  2. Filter for those that DON'T have the [kanban-sync] tag (to avoid loops).
  3. For each event:
     - Check if it already exists in Command.md or Calendar.md by title/date.
     - If not, append it to the '🤙 Meetings' lane in Command.md.
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo

# ── Import GCal Auth (Reuse) ──────────────────────────────────────────────────
# Import get_service from the existing sync tool
sys.path.append(str(Path(__file__).parent))
from cook_kanban_gcal_sync import get_service, ROOT, KANBAN_PATH, CALENDAR_PATH, TZ, CALENDAR_ID

# ── Config ───────────────────────────────────────────────────────────────────

# RegEx for existing tasks
TASK_TITLE_RE = re.compile(r"### (?:\[PLAN\]|\[MEET\])?\s*\*\*(.+?)\*\*", re.IGNORECASE)
DUE_DATE_RE   = re.compile(r"Due:\s*(\d{4}-\d{2}-\d{2})")

def is_task_in_file(title, target_date_str, file_text):
    """Search file text for a task with given title and date."""
    # Escape special regex chars in title
    escaped_title = re.escape(title)
    # Match title and then look for the due date in the next few lines
    # This is a bit rough but works for Obsidian Kanban cards
    pattern = rf"### (?:\[PLAN\]|\[MEET\])?\s*\*\*{escaped_title}\*\*.*?Due:\s*{target_date_str}"
    return re.search(pattern, file_text, re.DOTALL | re.IGNORECASE) is not None

def add_to_command_meetings(title, start_dt, location=None):
    """Append a new meeting task to the '🤙 Meetings' lane in Command.md."""
    if not KANBAN_PATH.exists(): return
    
    text = KANBAN_PATH.read_text(encoding="utf-8")
    date_str = start_dt.strftime("%Y-%m-%d")
    time_str = start_dt.strftime("%H:%M")
    
    # Format the new task
    new_task = f"- [ ] ### [MEET] **{title}**\n"
    new_task += f"      > ##### Due: {date_str} | ⏰ {time_str}\n"
    if location:
        new_task += f"      🕒 60m | 📍 {location}\n"
    else:
        new_task += f"      🕒 60m\n"
    
    # Find the '🤙 Meetings' lane
    lane_header = "## # 🤙 Meetings"
    if lane_header in text:
        # Split and insert after the header
        parts = text.split(lane_header, 1)
        # Find where the next lane starts or where settings start
        next_part = parts[1]
        
        # Append it right after the header
        updated_text = parts[0] + lane_header + "\n\n" + new_task + parts[1]
        KANBAN_PATH.write_text(updated_text, encoding="utf-8")
        return True
    return False

def reverse_sync(dry_run=False):
    service = get_service()
    now = datetime.now(TZ).isoformat()
    
    print(f"Fetching events from Google Calendar since {now}...")
    
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=now,
        singleEvents=True,
        orderBy='startTime',
        maxResults=20
    ).execute()
    
    events = events_result.get('items', [])
    
    if not events:
        print("No future events found in Google Calendar.")
        return

    command_text = KANBAN_PATH.read_text(encoding="utf-8") if KANBAN_PATH.exists() else ""
    calendar_text = CALENDAR_PATH.read_text(encoding="utf-8") if CALENDAR_PATH.exists() else ""
    
    added_count = 0
    
    for event in events:
        summary = event.get('summary', '(No Title)')
        description = event.get('description', '')
        
        # Skip spammy birthday events
        if "birthday" in summary.lower():
            continue
            
        # Skip events that WE synced from Kanban to GCal
        if "[kanban-sync]" in description:
            continue
            
        start = event['start'].get('dateTime', event['start'].get('date'))
        # start is either ISO timestamp or YYYY-MM-DD
        if 'T' in start:
            # Handle Zulu time or offset
            if start.endswith('Z'):
                start = start.replace('Z', '+00:00')
            start_dt = datetime.fromisoformat(start).astimezone(TZ)
            date_str = start_dt.strftime("%Y-%m-%d")
        else:
            # All-day event
            start_dt = datetime.strptime(start, "%Y-%m-%d").replace(tzinfo=TZ)
            date_str = start
            
        # Check if already in Command.md or Calendar.md
        if is_task_in_file(summary, date_str, command_text) or is_task_in_file(summary, date_str, calendar_text):
            continue
            
        print(f"  [NEW] {summary} on {date_str}")
        
        if not dry_run:
            location = event.get('location')
            if add_to_command_meetings(summary, start_dt, location):
                added_count += 1
                # Refresh command_text for next iteration to avoid duplicate inserts
                command_text = KANBAN_PATH.read_text(encoding="utf-8")
    
    if dry_run:
        print("\nDry run complete. No files modified.")
    else:
        print(f"\nDone! Added {added_count} events to Command.md '🤙 Meetings' lane.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reverse sync GCal events → Kanban")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()
    
    reverse_sync(dry_run=args.dry_run)
