import os
import re
from pathlib import Path

# Define the root path (Cook/)
ROOT = Path(__file__).parent.parent

# Define the path mapping (Old Path Regex/String -> New Path)
# We use regex to be flexible with slashes and quotes
MAPPING = {
    # Ghost Workspace -> Actual HumanFlow
    r"VLT_Content/02_WORKSPACE": "VLT_Content/02_HMN_HUMANFLOW",
    r"VLT_Content/02_WORKSPACE/jocons": "VLT_Content/02_HMN_HUMANFLOW/jocons",
    
    # Ghost Engine -> AI Engine
    r"VLT_Content/40_ENGINE": "VLT_Content/AI_ENGINE",
    
    # Ghost System -> AI Brain (or specific subfolder)
    r"VLT_Content/00_SYSTEM/A Human Instruction": "VLT_Content/AI_BRAIN/HMN_Guide",
    r"VLT_Content/00_SYSTEM": "VLT_Content/AI_BRAIN",
    
    # Ghost Inputs -> New Inputs
    r"VLT_Content/HMN_A INPUTS": "VLT_Content/01_HMN_INPUTS",
    
    # Missing Review/Output Prefixes
    r"VLT_Content/03_REVIEW": "VLT_Content/03_HMN_REVIEW",
    r"VLT_Content/04_OUTPUTS": "VLT_Content/04_HMN_OUTPUTS",
    
    # Root Folder Redundancy Correction (where files moved)
    r"VLT_Content/02_HMN_HUMANFLOW/Authority_Proof_Planner": "01 HMN__Command/00_CONTENT/Authority_Proof_Planner",
}

def migrate_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    changes = 0
    
    for old, new in MAPPING.items():
        # Replace occurrences, trying to preserve the quote style if possible
        if old in new_content:
            new_content = new_content.replace(old, new)
            changes += 1
            
    if changes > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {changes} paths in {file_path.name}")
    return changes

def run_migration():
    tools_dir = ROOT / "AI_Tools"
    total_files = 0
    total_changes = 0
    
    for file in tools_dir.glob("*.py"):
        if file.name == "migrate_tool_paths.py":
            continue
        changes = migrate_file(file)
        if changes > 0:
            total_files += 1
            total_changes += changes
            
    print(f"\nMigration complete! Updated {total_changes} paths across {total_files} files.")

if __name__ == "__main__":
    run_migration()
