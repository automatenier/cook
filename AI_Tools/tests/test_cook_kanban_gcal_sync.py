"""
Tests for cook_kanban_gcal_sync.py
Uses mock kanban content — no API calls.
"""

import sys
from pathlib import Path
from textwrap import dedent

sys.path.insert(0, str(Path(__file__).parent.parent))

from cook_kanban_gcal_sync import parse_kanban, collect_events

MOCK_KANBAN = dedent("""\
    ---
    kanban-plugin: board
    ---

    ## # 🧑‍🤝‍🧑HMN_Meetings

    - [ ] ### [MEET] **SAVASA: Discovery Call**
          > ##### Due: 2026-03-05 | ⏰ 14:00
          🕒 60m | 📍 Zoom | 📚 [[01_Manager]]

    ## # 🧑‍🤝‍🧑HMN_Main

    - [ ] ### [PLAN] **Fadli: Welcome Email**
          > ##### Due: 2026-03-03
          `/client-status` | 🕒 05m | 📚 [[02_VA]]
    - [ ] ### [PLAN] **Ruth: Onboarding Setup**
          > ##### Due: 2026-03-03
          `/onboard` | 🕒 15m | 📚 [[01_Manager]]

    ## # 🧑‍🤝‍🧑HMN_Content

    - [ ] ### [PLAN] **Strategy: Personal Brand Angle**
          > ##### Due: 2026-03-05
          `/content-strategy` | 🕒 30m | 📚 [[07_Writing]]

    ## # 🧑‍🤝‍🧑HMN_OBS

    - [ ] ### [PLAN] **Jordan: Cikarang Tokyo Scripts**
          > ##### Due: 2026-03-05
          `/content-write-scripts` | 🕒 45m | 📚 [[07_Writing]]
    - [ ] ### [PLAN] **Fadli: VSL Script**
          > ##### Due: 2026-03-06
          `/vsl-gen` | 🕒 40m | 📚 [[09_Product]]

    %% kanban:settings
    ```
    {}
    ```
    %%
""")


def _parse_mock():
    """Write mock to a tmp file and parse it."""
    import tempfile, os
    tmp = Path(tempfile.mktemp(suffix=".md"))
    tmp.write_text(MOCK_KANBAN, encoding="utf-8")
    lanes = parse_kanban(tmp)
    tmp.unlink()
    return lanes


def test_parse_lanes():
    lanes = _parse_mock()
    assert "HMN_Meetings" in lanes
    assert "HMN_Main" in lanes
    assert "HMN_Content" in lanes
    assert "HMN_OBS" in lanes


def test_parse_meeting_task():
    lanes = _parse_mock()
    task = lanes["HMN_Meetings"][0]
    assert task["title"] == "SAVASA: Discovery Call"
    assert task["due"] == "2026-03-05"
    assert task["time"] == "14:00"
    assert task["duration_m"] == 60
    assert task["location"] == "Zoom"


def test_parse_main_tasks():
    lanes = _parse_mock()
    tasks = lanes["HMN_Main"]
    assert len(tasks) == 2
    assert tasks[0]["due"] == "2026-03-03"
    assert tasks[0]["duration_m"] == 5
    assert tasks[1]["duration_m"] == 15


def test_meeting_event_time():
    lanes = _parse_mock()
    events = collect_events(lanes)
    meet_ev = next(e for e in events if "Discovery Call" in e["summary"])
    assert "14:00" in meet_ev["start"]["dateTime"]
    assert "15:00" in meet_ev["end"]["dateTime"]
    assert meet_ev["location"] == "Zoom"


def test_main_tasks_stacked():
    """Two HMN_Main tasks on same day should be sequential, not overlapping."""
    lanes = _parse_mock()
    events = collect_events(lanes)
    main_evs = sorted(
        [e for e in events if "[kanban-sync] HMN_Main" in e.get("description", "")],
        key=lambda e: e["start"]["dateTime"]
    )
    assert len(main_evs) == 2
    # First ends at 12:05, second starts at 12:05
    assert main_evs[0]["end"]["dateTime"] == main_evs[1]["start"]["dateTime"]


def test_deepwork_block_min_4hr():
    """Deep work block with < 4hr of tasks should still be 4hr."""
    lanes = _parse_mock()
    events = collect_events(lanes)
    dw = next(e for e in events if "Deep Work" in e["summary"] and "2026-03-05" in e["start"]["dateTime"])
    start = dw["start"]["dateTime"]
    end   = dw["end"]["dateTime"]
    from datetime import datetime
    from zoneinfo import ZoneInfo
    s = datetime.fromisoformat(start)
    e = datetime.fromisoformat(end)
    assert (e - s).seconds >= 4 * 3600


def test_deepwork_combines_content_and_obs():
    """Content + OBS tasks on same date → single combined block."""
    lanes = _parse_mock()
    events = collect_events(lanes)
    dw_0305 = [e for e in events if "Deep Work" in e["summary"] and "2026-03-05" in e["start"]["dateTime"]]
    assert len(dw_0305) == 1  # combined, not two separate blocks
    assert "Content" in dw_0305[0]["summary"] or "OBS" in dw_0305[0]["summary"]


def test_no_events_without_due_date():
    """Tasks with no Due: line should be skipped."""
    from cook_kanban_gcal_sync import build_meeting_event
    task = {"title": "Test", "due": None, "time": None, "duration_m": 30, "location": None}
    assert build_meeting_event(task) is None


# ── Calendar.md parser tests ──────────────────────────────────────────────────

from cook_kanban_gcal_sync import parse_calendar_md, collect_events_from_calendar

MOCK_CALENDAR = dedent("""\
    ---
    kanban-plugin: board
    ---

    ## # 05/03/26

    - [ ] ### [MEET] **SAVASA: Discovery Call**
          > ##### Due: 2026-03-05 | ⏰ 14:00
          🕒 60m | 📍 Zoom | 📚 [[01_Manager]]
    - [ ] ### [PLAN] **Jordan: Cikarang Tokyo Scripts**
          🕒 45m | 📚 [[07_Writing]]
    - [ ] ### [PLAN] **Fadli: VSL Script**
          🕒 40m | 📚 [[09_Product]]
    - [ ] ### [PLAN] **Ruth: March Sprint Scripts**
          🕒 30m | 📚 [[07_Writing]]

    ## # 06/03/26

    - [ ] ### [MEET] **Fadli: Onboarding Call**
          > ##### Due: 2026-03-06 | ⏰ 12:00
          🕒 30m | 📍 Google Meet | 📚 [[01_Manager]]

    %% kanban:settings
    ```
    {}
    ```
    %%
""")


def _parse_cal_mock():
    import tempfile
    tmp = Path(tempfile.mktemp(suffix=".md"))
    tmp.write_text(MOCK_CALENDAR, encoding="utf-8")
    days = parse_calendar_md(tmp)
    tmp.unlink()
    return days


def test_calendar_parse_dates():
    days = _parse_cal_mock()
    assert len(days) == 2
    assert days[0]["date"] == "2026-03-05"
    assert days[1]["date"] == "2026-03-06"


def test_calendar_parse_tasks():
    days = _parse_cal_mock()
    day = days[0]
    assert len(day["tasks"]) == 4  # 1 MEET + 3 PLAN
    assert day["tasks"][0]["tag"] == "MEET"
    assert day["tasks"][1]["tag"] == "PLAN"


def test_calendar_meeting_uses_exact_time():
    days = _parse_cal_mock()
    events = collect_events_from_calendar(days)
    meet = next(e for e in events if "Discovery Call" in e["summary"])
    assert "14:00" in meet["start"]["dateTime"]
    assert "15:00" in meet["end"]["dateTime"]


def test_calendar_plans_after_meetings():
    """PLAN deep work block should start after the meeting ends."""
    days = _parse_cal_mock()
    events = collect_events_from_calendar(days)
    dw = next(e for e in events if "Deep Work" in e["summary"])
    meet = next(e for e in events if "Discovery Call" in e["summary"])
    assert dw["start"]["dateTime"] >= meet["end"]["dateTime"]


def test_calendar_deepwork_for_3plus_plans():
    """3+ PLAN tasks on same day → single deep work block."""
    days = _parse_cal_mock()
    events = collect_events_from_calendar(days)
    dw_events = [e for e in events if "Deep Work" in e["summary"]]
    assert len(dw_events) == 1


def test_calendar_single_meeting_no_deepwork():
    """Day with only a MEET → no deep work block."""
    days = _parse_cal_mock()
    events = collect_events_from_calendar(days)
    mar6 = [e for e in events if "2026-03-06" in e["start"]["dateTime"]]
    assert len(mar6) == 1
    assert "Fadli: Onboarding Call" in mar6[0]["summary"]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
