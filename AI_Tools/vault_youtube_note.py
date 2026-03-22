"""
youtube_note.py — Fetch a YouTube transcript, summarize key insights with Claude Haiku,
and save a structured note to VLT_Content/01_HMN_INPUTS/Swipe Files/.

Usage:
    python youtube_note.py <YouTube URL>

Output:
    VLT_Content/01_HMN_INPUTS/Swipe Files/YYYY-MM-DD_<video-title-slug>.md

Requirements:
    youtube-transcript-api, anthropic, python-dotenv
"""

import sys
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import anthropic
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

SWIPE_DIR = Path(__file__).parent.parent / "Content" / "HMN_A INPUTS" / "Swipe Files"
CLAUDE_MODEL = "claude-haiku-4-5-20251001"


def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from various URL formats."""
    parsed = urlparse(url)
    if parsed.hostname in ("youtu.be",):
        return parsed.path.lstrip("/").split("?")[0]
    if parsed.hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
    raise ValueError(f"Cannot extract video ID from URL: {url}")


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript text, preferring English then falling back to any available language."""
    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(video_id, languages=["en", "en-US", "id"])
    except NoTranscriptFound:
        transcript_list = api.list(video_id)
        # Pick the first available transcript (manual or auto-generated)
        transcript = next(iter(transcript_list)).fetch()
    return " ".join(chunk.text for chunk in transcript)


def summarize_with_claude(transcript: str, url: str) -> dict:
    """Use Claude Haiku to extract structured insights from transcript."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""You are analyzing a YouTube video transcript to extract content strategy insights.
The transcript may be in Indonesian or English — respond in English regardless.

URL: {url}

Transcript (may be truncated):
{transcript[:12000]}

Extract the following and respond in this exact format:

TITLE: [infer a short title from the content]
HOOK_TYPE: [e.g. "Bold claim", "Question", "Story open", "Stat", "Controversy"]
STRUCTURE: [describe the content structure in 2-3 sentences]
KEY_INSIGHTS:
- [insight 1]
- [insight 2]
- [insight 3]
SWIPE_NOTES: [1-2 sentences on what makes this format worth stealing]
"""

    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text
    return parse_claude_response(raw, url)


def parse_claude_response(raw: str, url: str) -> dict:
    """Parse Claude's structured response into a dict."""
    def extract(label: str) -> str:
        pattern = rf"{label}:\s*(.+?)(?=\n[A-Z_]+:|$)"
        match = re.search(pattern, raw, re.DOTALL)
        return match.group(1).strip() if match else ""

    title = extract("TITLE") or "YouTube Note"
    hook_type = extract("HOOK_TYPE")
    structure = extract("STRUCTURE")
    swipe_notes = extract("SWIPE_NOTES")

    # Extract bullet list for KEY_INSIGHTS
    insights_block = extract("KEY_INSIGHTS")
    insights = [line.lstrip("- ").strip() for line in insights_block.splitlines() if line.strip().startswith("-")]

    return {
        "title": title,
        "hook_type": hook_type,
        "structure": structure,
        "insights": insights,
        "swipe_notes": swipe_notes,
    }


def slugify(text: str, max_len: int = 50) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:max_len].rstrip("-")


def write_note(data: dict, url: str) -> Path:
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    slug = slugify(data["title"])
    filename = f"{date_str}_{slug}.md"

    SWIPE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = SWIPE_DIR / filename

    counter = 1
    while out_path.exists():
        out_path = SWIPE_DIR / f"{date_str}_{slug}_{counter}.md"
        counter += 1

    insights_md = "\n".join(f"- {i}" for i in data["insights"])

    content = f"""---
date: {date_str}
source: youtube
url: {url}
hook_type: {data['hook_type']}
tags: [swipe, youtube]
status: raw
---

# {data['title']}

## Structure
{data['structure']}

## Key Insights
{insights_md}

## Swipe Notes
{data['swipe_notes']}

---
*Captured {date_str} via youtube_note.py*
"""

    out_path.write_text(content, encoding="utf-8")
    return out_path


def process(url: str) -> Path:
    video_id = extract_video_id(url)
    print(f"Fetching transcript for video ID: {video_id}")
    transcript = fetch_transcript(video_id)
    print(f"Transcript fetched ({len(transcript)} chars). Summarizing...")
    data = summarize_with_claude(transcript, url)
    path = write_note(data, url)
    return path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_note.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1].strip()
    try:
        path = process(url)
        print(f"OK: {path}")
    except (TranscriptsDisabled, NoTranscriptFound):
        print("ERROR: No transcript available for this video (disabled or not found).", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
