import os
import time
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Configuration ---
ROOT = Path(__file__).resolve().parent.parent
WATCH_DIR = ROOT / "VLT_Content" / "01_HMN_INPUTS" / "Media_Swipe" / "Jordan"
KANBAN_FILE = ROOT / "VLT_Content" / "01 HMN_Command" / "00_IDEATION_KANBAN.md"
SECTION_HEADER = "## 🔍 Outlier Research (Viral Reels)"
ALLOWED_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi"}

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

class ReelWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        if file_path.suffix.lower() in ALLOWED_EXTENSIONS:
            log(f"New video detected: {file_path.name}")
            # Wait a moment to ensure file is fully copied
            time.sleep(2)
            self.update_kanban(file_path)

    def update_kanban(self, video_path):
        if not KANBAN_FILE.exists():
            log(f"Error: Kanban file not found at {KANBAN_FILE}")
            return

        filename = video_path.name
        # Relative link from Kanban's dir to video
        try:
            rel_path = os.path.relpath(video_path, KANBAN_FILE.parent).replace("\\", "/")
            obsidian_link = f"[[{rel_path}]]"
        except:
            obsidian_link = filename

        with open(KANBAN_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Check for duplicates
        if any(filename in line for line in lines):
            log(f"Skipping: {filename} already in Kanban.")
            return

        final_lines = []
        appended = False
        for line in lines:
            final_lines.append(line)
            if SECTION_HEADER in line and not appended:
                # Add the new task right after the header
                # Ensure there is a newline after the header if not already present
                task = f"\n- [ ] ### [AUTO]\n      New Reel Analysis: {filename}\n      Source: {obsidian_link}\n"
                final_lines.append(task)
                appended = True

        if not appended:
            log(f"Error: Could not find section '{SECTION_HEADER}' in {KANBAN_FILE}")
            return

        with open(KANBAN_FILE, "w", encoding="utf-8") as f:
            f.writelines(final_lines)
        
        log(f"Successfully added '{filename}' to Kanban.")

def main():
    if not WATCH_DIR.exists():
        log(f"Creating watch directory: {WATCH_DIR}")
        WATCH_DIR.mkdir(parents=True, exist_ok=True)

    event_handler = ReelWatcher()
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_DIR), recursive=False)
    
    log(f"Watching: {WATCH_DIR}")
    log(f"Updating: {KANBAN_FILE}")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
