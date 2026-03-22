"""
cook_kanban_sync_engine.py
--------------------------
Links 00_KANBAN_COMMAND.md (Role-based) and Calendar.md (Date-based).
"""

import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
COMMAND_PATH = ROOT / "01 HMN__Command/00_KANBAN_COMMAND.md"
CALENDAR_PATH = ROOT / "01 HMN__Command/Calendar.md"

LANE_RE = re.compile(r"^##\s+#?\s*(.+)")
TASK_HEAD_RE = re.compile(r"^- \[([ x])\] ### (\[(?:PLAN|MEET)\])?\s*\*\*([^*]+)\*\*")
DUE_RE = re.compile(r"Due:\s*(\d{4}-\d{2}-\d{2})")
CAL_DATE_RE = re.compile(r"(\d{2})/(\d{2})/(\d{2})")

def parse_kanban(path: Path):
    if not path.exists(): return None, []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    lanes = []
    current_lane = None
    
    for i, line in enumerate(lines):
        if line.startswith("%% kanban:settings"): break
        lane_match = LANE_RE.match(line)
        if lane_match:
            current_lane = {"name": lane_match.group(1).strip(), "tasks": []}
            lanes.append(current_lane)
            continue
        if not current_lane: continue
        
        task_match = TASK_HEAD_RE.match(line)
        if task_match:
            checked = task_match.group(1) == "x"
            tag = task_match.group(2) or "[PLAN]"
            title = task_match.group(3).strip()
            
            metadata = []
            due_date = None
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].strip() == ""):
                if lines[j].strip() != "":
                    metadata.append(lines[j])
                    due_match = DUE_RE.search(lines[j])
                    if due_match: due_date = due_match.group(1)
                j += 1
            
            current_lane["tasks"].append({
                "checked": checked, "tag": tag, "title": title, 
                "due": due_date, "metadata": metadata
            })
    return text, lanes

def format_task(task):
    status = "x" if task["checked"] else " "
    header = f"- [{status}] ### {task['tag']} **{task['title']}**"
    return "\n".join([header] + task["metadata"])

def sync_boards():
    cmd_text, cmd_lanes = parse_kanban(COMMAND_PATH)
    cal_text, cal_lanes = parse_kanban(CALENDAR_PATH)
    
    if not cmd_lanes or not cal_lanes: return

    # Index tasks and Route them
    cmd_tasks = {}
    cal_tasks = {t["title"]: t for l in cal_lanes for t in l["tasks"]}
    routed_lanes = {l["name"]: l for l in cmd_lanes}
    
    for lane in cmd_lanes:
        # We'll collect tasks to move
        tasks_to_keep = []
        for task in lane["tasks"]:
            # Check for /terminal X routing
            route_match = re.search(r"/terminal\s*(\d+)", task["title"] + " ".join(task["metadata"]))
            if route_match:
                t_num = route_match.group(1)
                target_lane_name = next((name for name in routed_lanes.keys() if f"Terminal {t_num}" in name), None)
                
                if target_lane_name and target_lane_name != lane["name"]:
                    routed_lanes[target_lane_name]["tasks"].append(task)
                    print(f"Rerouting '{task['title']}' to {target_lane_name}")
                    continue # Don't keep in current lane
            
            tasks_to_keep.append(task)
            cmd_tasks[task["title"]] = task
        
        lane["tasks"] = tasks_to_keep

    # 1. Sync Completion Status (Mutual)
    for title, cmd_t in cmd_tasks.items():
        if title in cal_tasks:
            # If one is checked, check both
            if cmd_t["checked"] or cal_tasks[title]["checked"]:
                cmd_t["checked"] = cal_tasks[title]["checked"] = True

    # 2. Add missing CMD tasks to CAL (if they have a Due date)
    for title, cmd_t in cmd_tasks.items():
        if cmd_t["due"] and title not in cal_tasks:
            # Target date lane in Calendar
            d = cmd_t["due"] # YYYY-MM-DD
            target_lane_name = f"{d[8:10]}/{d[5:7]}/{d[2:4]}" # DD/MM/YY
            
            found_lane = False
            for lane in cal_lanes:
                if target_lane_name in lane["name"]:
                    lane["tasks"].append(cmd_t)
                    found_lane = True
                    break
            
            if not found_lane:
                cal_lanes.insert(0, {"name": f"0 {target_lane_name}", "tasks": [cmd_t]})

    # Rebuild Files
    def rebuild(lanes, original_text):
        new_lines = []
        # Keep YAML frontmatter and header
        header_part = original_text.split("## ")[0]
        new_lines.append(header_part.strip())
        
        for lane in lanes:
            new_lines.append(f"\n\n## # {lane['name']}\n")
            for task in lane["tasks"]:
                new_lines.append(format_task(task) + "\n")
        
        # Keep settings
        settings_part = original_text.split("%% kanban:settings")[1]
        return "\n".join(new_lines) + "\n\n%% kanban:settings" + settings_part

    COMMAND_PATH.write_text(rebuild(cmd_lanes, cmd_text), encoding="utf-8")
    CALENDAR_PATH.write_text(rebuild(cal_lanes, cal_text), encoding="utf-8")
    print("Boards Synced Successfully.")

if __name__ == "__main__":
    sync_boards()
