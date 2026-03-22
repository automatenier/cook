"""
cook_kanban_gcal_sync.py
------------------------
Sync Obsidian Kanban files to Google Calendar.

TWO SOURCES:

  --source kanban  (default)  Reads Command.md
    Meetings → individual timed events
    Claude   → individual events stacked from 12:00 per day
    Gem (1,2,3) → combined deep work block per due date (min 4hr)

  --source calendar           Reads Calendar.md (date-as-lane: ## # DD/MM/YY)
    [MEET] tasks → individual events at ⏰ time, 🕒 duration
    [PLAN] tasks → stacked from 12:00 (1-2 tasks) or one deep work block (3+)
    Lane date overrides any Due: field in the task

Auth (first run only):
  1. Download credentials.json from Google Cloud Console
     (APIs & Services → Credentials → OAuth 2.0 Client IDs → Desktop type)
  2. Place credentials.json in the project root (Cook/)
  3. Run the script — browser will open for one-time auth
  4. Token is saved to .tmp/gcal_token.json for future runs

Usage:
    py -3 AI_Tools/cook_kanban_gcal_sync.py
    py -3 AI_Tools/cook_kanban_gcal_sync.py --source calendar
    py -3 AI_Tools/cook_kanban_gcal_sync.py --dry-run
    py -3 AI_Tools/cook_kanban_gcal_sync.py --clear
"""

import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

# ── Config ───────────────────────────────────────────────────────────────────

ROOT          = Path(__file__).parent.parent
KANBAN_PATH   = ROOT / "01 HMN__Command/Command.md"
CALENDAR_PATH = ROOT / "01 HMN__Command/Calendar.md"
TOKEN_PATH    = ROOT / ".tmp/gcal_token.json"
CREDS_PATH    = ROOT / "credentials.json"
CALENDAR_ID = "jordanmathew811@gmail.com"
SYNC_TAG    = "[kanban-sync]"
TZ          = ZoneInfo("Asia/Jakarta")
SCOPES      = ["https://www.googleapis.com/auth/calendar"]

DEEPWORK_LANES   = {"Gem", "Deepwork"}
INDIVIDUAL_LANES = {"Claude"}
MEETING_LANES    = {"Meetings"}

load_dotenv(ROOT / ".env")


# ── Auth ─────────────────────────────────────────────────────────────────────

def get_service():
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build

    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDS_PATH.exists():
                print("ERROR: credentials.json not found.")
                print("  1. Go to console.cloud.google.com → APIs & Services → Credentials")
                print("  2. Create OAuth 2.0 Client ID (Desktop type)")
                print("  3. Download and save as credentials.json in Cook/")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)

        TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json())

    return build("calendar", "v3", credentials=creds)


# ── Parser ────────────────────────────────────────────────────────────────────

TASK_RE = re.compile(r"-\s+\[[ x]\]\s+###\s+\[(?:PLAN|MEET)\]\s+\*\*(.+?)\*\*", re.IGNORECASE)
DUE_RE  = re.compile(r"Due:\s*(\d{4}-\d{2}-\d{2})")
TIME_RE = re.compile(r"⏰\s*(\d{1,2}:\d{2})")
DUR_RE  = re.compile(r"🕒\s*(\d+)m")
LOC_RE  = re.compile(r"📍\s*(\S+)")


def parse_kanban(path: Path) -> dict:
    """Return dict of lane_key → list of task dicts."""
    text = path.read_text(encoding="utf-8")
    lanes: dict[str, list] = {}
    current_lane = None

    for line in text.splitlines():
        # Stop at kanban settings block
        if line.strip().startswith("%% kanban:settings"):
            break

        lane_match = re.match(r"^##\s+#?\s*(.+)", line)
        if lane_match:
            raw = lane_match.group(1).strip()
            # Normalize: strip emoji, whitespace → e.g. "HMN_Meetings"
            current_lane = re.sub(r"[^\w_]", "", raw.replace(" ", "_"))
            lanes[current_lane] = []
            continue

        if current_lane is None:
            continue

        title_match = TASK_RE.match(line.strip())
        if title_match:
            lanes[current_lane].append({
                "title":      title_match.group(1).strip(),
                "due":        None,
                "time":       None,
                "duration_m": None,
                "location":   None,
            })
            continue

        if lanes.get(current_lane):
            task = lanes[current_lane][-1]
            if m := DUE_RE.search(line):
                task["due"] = m.group(1)
            if m := TIME_RE.search(line):
                task["time"] = m.group(1)
            if m := DUR_RE.search(line):
                task["duration_m"] = int(m.group(1))
            if m := LOC_RE.search(line):
                task["location"] = m.group(1)

    return lanes


# ── Calendar.md parser ───────────────────────────────────────────────────────

LANE_DATE_RE = re.compile(r"(\d{2})/(\d{2})/(\d{2})")   # DD/MM/YY


def parse_calendar_md(path: Path) -> list:
    """
    Parse Calendar.md where lanes = dates (## # DD/MM/YY).
    Returns list of dicts: {date, tasks: [{title, time, duration_m, location, tag}]}
    """
    text = path.read_text(encoding="utf-8")
    days = []
    current_day = None

    for line in text.splitlines():
        if line.strip().startswith("%% kanban:settings"):
            break

        lane_match = re.match(r"^##\s+#?\s*(.+)", line)
        if lane_match:
            raw = lane_match.group(1).strip()
            m = LANE_DATE_RE.search(raw)
            if m:
                dd, mo, yy = m.groups()
                date_str = f"20{yy}-{mo}-{dd}"
                current_day = {"date": date_str, "tasks": []}
                days.append(current_day)
            else:
                current_day = None
            continue

        if current_day is None:
            continue

        title_match = TASK_RE.match(line.strip())
        if title_match:
            tag = "MEET" if re.search(r"\[MEET\]", line, re.IGNORECASE) else "PLAN"
            current_day["tasks"].append({
                "title":      title_match.group(1).strip(),
                "time":       None,
                "duration_m": None,
                "location":   None,
                "tag":        tag,
            })
            continue

        if current_day["tasks"]:
            task = current_day["tasks"][-1]
            if m := TIME_RE.search(line):
                task["time"] = m.group(1)
            if m := DUR_RE.search(line):
                task["duration_m"] = int(m.group(1))
            if m := LOC_RE.search(line):
                task["location"] = m.group(1)

    return days


def collect_events_from_calendar(days: list) -> list:
    """Build GCal events from Calendar.md day-list."""
    events = []

    for day in days:
        date_str = day["date"]
        tasks    = day["tasks"]
        if not tasks:
            continue

        meets = [t for t in tasks if t["tag"] == "MEET"]
        plans = [t for t in tasks if t["tag"] == "PLAN"]

        # Meetings → individual events at their ⏰ time
        for t in meets:
            start = _dt(date_str, t["time"] or "12:00")
            end   = start + timedelta(minutes=t["duration_m"] or 60)
            ev = {
                "summary":     t["title"],
                "start":       {"dateTime": start.isoformat(), "timeZone": "Asia/Jakarta"},
                "end":         {"dateTime": end.isoformat(),   "timeZone": "Asia/Jakarta"},
                "description": f"{SYNC_TAG} Calendar/MEET",
            }
            if t["location"]:
                ev["location"] = t["location"]
            events.append(ev)

        if not plans:
            continue

        # Find start time — after last meeting on that day, or 12:00
        meet_ends = []
        for t in meets:
            s = _dt(date_str, t["time"] or "12:00")
            meet_ends.append(s + timedelta(minutes=t["duration_m"] or 60))
        cursor = max(meet_ends) if meet_ends else _dt(date_str, "12:00")

        if len(plans) <= 2:
            # Stack individually
            for t in plans:
                dur = t["duration_m"] or 30
                end = cursor + timedelta(minutes=dur)
                events.append({
                    "summary":     t["title"],
                    "start":       {"dateTime": cursor.isoformat(), "timeZone": "Asia/Jakarta"},
                    "end":         {"dateTime": end.isoformat(),    "timeZone": "Asia/Jakarta"},
                    "description": f"{SYNC_TAG} Calendar/PLAN",
                })
                cursor = end
        else:
            # Deep work block
            total_m = sum(t["duration_m"] or 30 for t in plans)
            total_m = max(total_m, 240)
            end = cursor + timedelta(minutes=total_m)
            task_lines = "\n".join(f"  • {t['title']} ({t['duration_m'] or 30}m)" for t in plans)
            events.append({
                "summary":     "🔴 Deep Work",
                "start":       {"dateTime": cursor.isoformat(), "timeZone": "Asia/Jakarta"},
                "end":         {"dateTime": end.isoformat(),    "timeZone": "Asia/Jakarta"},
                "description": f"{SYNC_TAG} Calendar/DW\n\n{task_lines}",
            })

    return events


# ── Event builders ─────────────────────────────────────────────────────────────

def _dt(date_str: str, time_str: str) -> datetime:
    h, m = map(int, time_str.split(":"))
    y, mo, d = map(int, date_str.split("-"))
    return datetime(y, mo, d, h, m, tzinfo=TZ)


def build_meeting_event(task: dict) -> dict | None:
    if not task["due"]:
        return None
    start = _dt(task["due"], task["time"] or "12:00")
    end   = start + timedelta(minutes=task["duration_m"] or 60)
    ev = {
        "summary":     task["title"],
        "start":       {"dateTime": start.isoformat(), "timeZone": "Asia/Jakarta"},
        "end":         {"dateTime": end.isoformat(),   "timeZone": "Asia/Jakarta"},
        "description": f"{SYNC_TAG} HMN_Meetings",
    }
    if task["location"]:
        ev["location"] = task["location"]
    return ev


def build_main_events(tasks: list) -> list:
    """Stack HMN_Main tasks sequentially per day starting at 12:00."""
    # Group by date
    by_date: dict[str, list] = {}
    for t in tasks:
        if t["due"]:
            by_date.setdefault(t["due"], []).append(t)

    events = []
    for due_date, day_tasks in sorted(by_date.items()):
        cursor = _dt(due_date, "12:00")
        for task in day_tasks:
            dur = task["duration_m"] or 30
            end = cursor + timedelta(minutes=dur)
            events.append({
                "summary":     task["title"],
                "start":       {"dateTime": cursor.isoformat(), "timeZone": "Asia/Jakarta"},
                "end":         {"dateTime": end.isoformat(),   "timeZone": "Asia/Jakarta"},
                "description": f"{SYNC_TAG} HMN_Main",
            })
            cursor = end
    return events


def build_deepwork_blocks(tasks_by_lane: dict) -> list:
    """
    Combine HMN_Content + HMN_OBS tasks.
    Group by due date → one deep work block per day (min 4hr).
    """
    # Collect all tasks with their source lane
    by_date: dict[str, list] = {}
    for lane, tasks in tasks_by_lane.items():
        for t in tasks:
            if t["due"]:
                by_date.setdefault(t["due"], []).append((lane, t))

    events = []
    for due_date, lane_tasks in sorted(by_date.items()):
        total_m = sum(t["duration_m"] or 30 for _, t in lane_tasks)
        total_m = max(total_m, 240)  # floor 4hr

        start = _dt(due_date, "12:00")
        end   = start + timedelta(minutes=total_m)

        lanes_used = sorted({l.replace("HMN_", "") for l, _ in lane_tasks})
        label = " + ".join(lanes_used)

        task_lines = "\n".join(
            f"  • [{l.replace('HMN_', '')}] {t['title']} ({t['duration_m'] or 30}m)"
            for l, t in lane_tasks
        )
        events.append({
            "summary":     f"🔴 Deep Work — {label}",
            "start":       {"dateTime": start.isoformat(), "timeZone": "Asia/Jakarta"},
            "end":         {"dateTime": end.isoformat(),   "timeZone": "Asia/Jakarta"},
            "description": f"{SYNC_TAG} Deep Work\n\n{task_lines}",
        })
    return events


# ── Sync ──────────────────────────────────────────────────────────────────────

def collect_events(lanes: dict) -> list:
    events = []
    deepwork_input: dict[str, list] = {}

    for lane_key, tasks in lanes.items():
        if not tasks:
            continue

        if any(k in lane_key for k in MEETING_LANES):
            for t in tasks:
                ev = build_meeting_event(t)
                if ev:
                    events.append(ev)

        elif any(k in lane_key for k in INDIVIDUAL_LANES):
            events.extend(build_main_events(tasks))

        elif any(k in lane_key for k in DEEPWORK_LANES):
            deepwork_input[lane_key] = tasks

    if deepwork_input:
        events.extend(build_deepwork_blocks(deepwork_input))

    return events


def get_existing_synced(service) -> set:
    """Return set of (summary, date_str) for events already synced."""
    existing = set()
    page_token = None
    while True:
        result = service.events().list(
            calendarId=CALENDAR_ID,
            q=SYNC_TAG,
            maxResults=250,
            pageToken=page_token,
        ).execute()
        for ev in result.get("items", []):
            if SYNC_TAG in ev.get("description", ""):
                start = ev["start"].get("dateTime", ev["start"].get("date", ""))
                existing.add((ev.get("summary", ""), start[:10]))
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    return existing


def clear_synced(service):
    """Delete all future kanban-synced events."""
    page_token = None
    deleted = 0
    while True:
        result = service.events().list(
            calendarId=CALENDAR_ID,
            q=SYNC_TAG,
            maxResults=250,
            pageToken=page_token,
        ).execute()
        for ev in result.get("items", []):
            if SYNC_TAG in ev.get("description", ""):
                service.events().delete(calendarId=CALENDAR_ID, eventId=ev["id"]).execute()
                print(f"  [DEL] {ev.get('summary')} on {ev['start'].get('dateTime','')[:10]}")
                deleted += 1
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    print(f"\n{deleted} events deleted.")


def sync(dry_run=False, source="kanban"):
    if source == "calendar":
        days   = parse_calendar_md(CALENDAR_PATH)
        events = collect_events_from_calendar(days)
    else:
        lanes  = parse_kanban(KANBAN_PATH)
        events = collect_events(lanes)

    if not events:
        print("No events to sync.")
        return

    print(f"Parsed {len(events)} event(s):\n")
    for ev in events:
        s = ev["start"]["dateTime"]
        e = ev["end"]["dateTime"]
        print(f"  {'[DRY] ' if dry_run else ''}{ev['summary']}")
        print(f"         {s[:10]} {s[11:16]} → {e[11:16]} WIB\n")

    if dry_run:
        return

    service  = get_service()
    existing = get_existing_synced(service)
    created = skipped = 0

    for ev in events:
        date_str = ev["start"]["dateTime"][:10]
        key = (ev["summary"], date_str)
        if key in existing:
            print(f"  [SKIP] Already exists: {ev['summary']} on {date_str}")
            skipped += 1
            continue
        service.events().insert(calendarId=CALENDAR_ID, body=ev).execute()
        print(f"  [OK]   {ev['summary']} → {date_str} @ {ev['start']['dateTime'][11:16]}")
        created += 1

    print(f"\nDone — {created} created, {skipped} skipped.")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync Obsidian Kanban → Google Calendar")
    parser.add_argument("--source",  choices=["kanban", "calendar"], default="kanban",
                        help="kanban = 00_KANBAN_COMMAND.md (default) | calendar = Calendar.md")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no API calls")
    parser.add_argument("--clear",   action="store_true", help="Delete all synced events")
    args = parser.parse_args()

    if args.clear:
        sync_service = get_service()
        clear_synced(sync_service)
    else:
        sync(dry_run=args.dry_run, source=args.source)
