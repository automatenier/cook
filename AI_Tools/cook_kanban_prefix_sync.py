"""
cook_kanban_prefix_sync.py
--------------------------
Automatically updates task prefixes and lane headers in Command.md, Human.md, and AI.md.
Ensures consistency between lane icons and task icons.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
BOARDS = [
    ROOT / "01 HMN__Command/Command.md",
    ROOT / "01 HMN__Command/Human.md",
    ROOT / "01 HMN__Command/AI.md"
]

LANE_RE = re.compile(r"^##\s+#?\s*(.+)")
# Match task lines and capture: 1. Checked status, 2. The rest of the line
TASK_RE = re.compile(r"^- \[([ x])\]\s*(.*)")

# Mapping from lane keywords to descriptive tags with icons
# Using concise 2-3 letter tags as requested
PREFIX_MAP = {
    "Meetings": "🤙 [MTG]",
    "Deepwork": "🧠 [DWK]",
    "Claude":   "🟧 [CLD]",
    "Gem_Cook": ":LiTerminalSquare: [G-CK]",
    "Gem_Content": ":LiTerminalSquare: [G-CT]",
    "Gem_OBS":   ":LiTerminalSquare: [G-OB]",
    "AI_Cook":  ":LiTerminalSquare: [G-CK]",
    "AI_Content": ":LiTerminalSquare: [G-CT]",
    "AI_OBS":   ":LiTerminalSquare: [G-OB]",
    "Gem":      ":LiTerminalSquare: [G]",
    "HMN_Cook": "🧠 [CK]",
    "HMN_Content": "🧑‍🤝‍🧑 [CT]",
    "HMN_OBS":  "🧑‍🤝‍🧑 [OB]",
    ":LiTerminalSquare: AI_":    ":LiTerminalSquare: [G]",
    ":LiTerminalSquare:AI_":    ":LiTerminalSquare: [G]",
    "🟧 Claude Task": "🟧 [CLD]"
}

# Mapping to rename Lane Headers (Clean up Lucide icons to Emojis or vice-versa)
# Improved to prevent duplication
LANE_RENAME_MAP = {
    "🤖": ":LiTerminalSquare:",
    "LiTerminalSquare:": ":LiTerminalSquare:",
    ":LiBrain:": "🧠"
}

def get_prefix(lane_name):
    sorted_keys = sorted(PREFIX_MAP.keys(), key=len, reverse=True)
    for key in sorted_keys:
        if key in lane_name:
            return PREFIX_MAP[key]
    return None

def clean_title(raw_title):
    """
    Strips existing prefixes, headers, emojis, and formatting to get the raw task title.
    Handles multiple levels of nested prefixes.
    """
    current = raw_title.strip()
    
    while True:
        prev = current
        # Remove leading markdown headers (###)
        current = re.sub(r"^#+\s*", "", current)
        # Remove Lucide icons (both correct and incorrect versions)
        current = re.sub(r"^:?LiTerminalSquare:\s*", "", current)
        # Remove emojis (common ones used in this repo)
        current = re.sub(r"^[🤖🧠🟧🤙🧑‍🤝‍🧑✅🗓️⚙️👀]+", "", current).strip()
        # Remove bracketed prefixes (including new concise ones and old long ones)
        current = re.sub(r"^\[[^\]]+\]\s*", "", current).strip()
        # Remove bold markers from start/end
        current = re.sub(r"^\*\*", "", current)
        current = re.sub(r"\*\*\s*$", "", current)
        current = current.strip()
        
        if current == prev:
            break
            
    return current

def sync_prefixes(board_path):
    if not board_path.exists():
        print(f"Skipping: {board_path.name} (not found)")
        return

    content = board_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    new_lines = []
    current_lane = None
    current_prefix = None
    
    in_settings = False
    updated_count = 0
    lane_updated_count = 0
    
    for line in lines:
        if "%% kanban:settings" in line:
            in_settings = True
        
        if in_settings:
            new_lines.append(line)
            continue
            
        lane_match = LANE_RE.match(line)
        if lane_match:
            original_lane = lane_match.group(1).strip()
            # Special fix for double colon issue before mapping
            clean_lane = original_lane.replace("::", ":")
            new_lane = clean_lane
            
            # 1. Rename Lane Header if needed
            for old_icon, new_icon in LANE_RENAME_MAP.items():
                if old_icon in new_lane and old_icon != new_icon:
                     new_lane = new_lane.replace(old_icon, new_icon).strip()
            
            # Ensure no double colons after mapping
            new_lane = new_lane.replace("::", ":")
            
            if new_lane != original_lane:
                line = f"## # {new_lane}"
                print(f"[{board_path.name}] Renamed Lane: {original_lane} -> {new_lane}")
                lane_updated_count += 1
            
            current_lane = new_lane
            current_prefix = get_prefix(current_lane)
            new_lines.append(line)
            continue
            
        task_match = TASK_RE.match(line)
        if task_match and current_prefix:
            checked = task_match.group(1)
            raw_title = task_match.group(2)
            
            title = clean_title(raw_title)
            
            # Canonical format: - [ ] ### PREFIX **Title**
            new_line = f"- [{checked}] ### {current_prefix} **{title}**"
            
            if line.strip() != new_line:
                print(f"[{board_path.name}] Updated Task: '{title[:30]}...'")
                new_lines.append(new_line)
                updated_count += 1
                continue
        
        new_lines.append(line)

    if updated_count > 0 or lane_updated_count > 0:
        board_path.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"Synced {board_path.name}: {updated_count} tasks, {lane_updated_count} lanes.")
    else:
        print(f"No updates needed for {board_path.name}")

if __name__ == "__main__":
    for board in BOARDS:
        sync_prefixes(board)
