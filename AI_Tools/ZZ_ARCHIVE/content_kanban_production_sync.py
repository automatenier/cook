"""
Synchronize '# Production' lanes between Writing Kanban and Content System Kanban.
Moves tasks from Writing.md's '# Production' lane to CONTENT SYSTEM.md's '# Production' lane.
"""

import re
from pathlib import Path

WRITING_KANBAN = Path("VLT_Content/__VLT_OBSVAULT/_  AReadme/New/Writing.md")
CONTENT_SYSTEM_KANBAN = Path("VLT_Content/01 HMN_Command/CONTENT SYSTEM.md")

def process_boards():
    if not WRITING_KANBAN.exists() or not CONTENT_SYSTEM_KANBAN.exists():
        print("Error: One or both Kanban files not found.")
        return

    # Process Writing Board (Source)
    writing_lines = WRITING_KANBAN.read_text(encoding="utf-8").splitlines()
    new_writing_lines = []
    extracted_tasks = []
    
    in_production_lane = False
    
    for line in writing_lines:
        if line.startswith("## # Production"):
            in_production_lane = True
            new_writing_lines.append(line)
            continue
            
        if in_production_lane:
            if line.startswith("## "):
                in_production_lane = False
                new_writing_lines.append(line)
            elif line.strip().startswith("- [ ]") or line.strip().startswith("- [x]"):
                extracted_tasks.append([line])
            elif extracted_tasks and (line.startswith("\t") or line.startswith("    ")):
                extracted_tasks[-1].append(line)
            elif line.strip() == "":
                # Skip empty lines in production lane to clear it out
                pass
            else:
                # Some other content in the lane? (not a task, not metadata)
                # If it's not a header, and we are in production lane, it might be text.
                # Let's keep it in the lane for now if it's not a task.
                new_writing_lines.append(line)
        else:
            new_writing_lines.append(line)

    if not extracted_tasks:
        print("No tasks found in Writing Production lane.")
        return

    print(f"Extracted {len(extracted_tasks)} tasks.")

    # Process Content System (Destination)
    system_lines = CONTENT_SYSTEM_KANBAN.read_text(encoding="utf-8").splitlines()
    new_system_lines = []
    
    in_production_lane = False
    tasks_injected = False
    
    for line in system_lines:
        if line.startswith("## # Production"):
            in_production_lane = True
            new_system_lines.append(line)
            # Inject tasks right after header
            for task_block in extracted_tasks:
                new_system_lines.extend(task_block)
            tasks_injected = True
            continue
            
        if in_production_lane:
            if line.startswith("## "):
                in_production_lane = False
                new_system_lines.append(line)
            else:
                # Keep existing items in Production
                new_system_lines.append(line)
        else:
            new_system_lines.append(line)

    # Save files
    WRITING_KANBAN.write_text("\n".join(new_writing_lines), encoding="utf-8")
    CONTENT_SYSTEM_KANBAN.write_text("\n".join(new_system_lines), encoding="utf-8")
    print("Sync complete.")

if __name__ == "__main__":
    process_boards()
