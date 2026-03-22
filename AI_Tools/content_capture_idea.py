"""
capture_idea.py — Write a raw idea to VLT_Content/01_HMN_INPUTS as a timestamped Markdown note.

Usage:
    python capture_idea.py "Your idea text here"

Output:
    VLT_Content/01_HMN_INPUTS/YYYY-MM-DD_idea_<slug>.md
"""

import sys
import os
import re
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

INBOX_DIR = Path(__file__).parent.parent / "02 HMN_A INPUTS" / "ideas"


def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:max_len].rstrip("-")


def capture_idea(raw_text: str) -> Path:
    if not raw_text.strip():
        raise ValueError("Idea text cannot be empty.")

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    slug = slugify(raw_text)
    filename = f"{date_str}_idea_{slug}.md"

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    out_path = INBOX_DIR / filename

    # Avoid clobbering if slug collision on same day
    counter = 1
    while out_path.exists():
        out_path = INBOX_DIR / f"{date_str}_idea_{slug}_{counter}.md"
        counter += 1

    content = f"""---
date: {date_str}
time: {time_str}
tags: [idea]
status: raw
---

# {raw_text.strip()}

---

*Captured {date_str} at {time_str}*
"""

    out_path.write_text(content, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python capture_idea.py \"Your idea text\"")
        sys.exit(1)

    raw = " ".join(sys.argv[1:])
    try:
        path = capture_idea(raw)
        print(f"OK: {path}")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
