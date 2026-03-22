"""
Convert a reel analysis (markdown or manual notes) into structured JSON for Remotion.

Two modes:
  1. Manual: You write a .md file with your analysis, this converts it to JSON
  2. Gemini API: (optional) Upload video to Gemini for automatic analysis

The .md file can come from Telegram → n8n → OneDrive pipeline.

Usage:
    python tools/analyze_viral_reel.py notes.md
    python tools/analyze_viral_reel.py video.mp4 --gemini   (requires API key)
"""

import argparse
import json
import re
import sys
from pathlib import Path


TEMPLATE = """\
# Reel Analysis Template
# Fill this in manually (or paste from Gemini chat)
# Then run: python tools/analyze_viral_reel.py this_file.md

## Source
- video: (filename or link)
- duration: 15

## Hook (0-3s)
- technique: curiosity
- text: "Most fitness coaches waste 3 hours on content"
- visual: talking head, close up

## Segments
### Segment 1 (3-7s)
- purpose: value
- text: "Here's what I do instead"
- visual: talking head with text overlay
- camera: talking-head

### Segment 2 (7-12s)
- purpose: proof
- text: "This system got me 10 clients"
- visual: screen recording of dashboard
- camera: screen-recording

## CTA (12-15s)
- type: comment-keyword
- text: "Comment SYSTEM for the free template"
- visual: text on screen with arrow pointing to comments

## Pacing
- cuts: 6
- energy: high
- music: upbeat

## Style
- format: talking-head
- text_style: bold-captions
- color_mood: warm

## Why It Works
Hook creates curiosity gap, value section delivers quickly, CTA is specific and low friction.

## Replication Notes
Film talking head with bold text overlays. Keep each segment under 4 seconds. End with keyword CTA.
"""


def parse_markdown(md_text: str) -> dict:
    """Parse a manual analysis markdown file into structured JSON."""
    result = {
        "total_duration_seconds": 15,
        "hook": {"start": 0, "end": 3},
        "segments": [],
        "cta": {},
        "pacing": {},
        "style": {},
    }

    lines = md_text.strip().split("\n")
    current_section = None
    current_segment = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") and "Template" in line:
            continue

        # Section headers
        if line.startswith("## Hook"):
            current_section = "hook"
            times = re.findall(r"(\d+)-(\d+)s", line)
            if times:
                result["hook"]["start"] = int(times[0][0])
                result["hook"]["end"] = int(times[0][1])
            continue
        elif line.startswith("### Segment"):
            current_section = "segment"
            current_segment = {}
            times = re.findall(r"(\d+)-(\d+)s", line)
            if times:
                current_segment["start"] = int(times[0][0])
                current_segment["end"] = int(times[0][1])
            result["segments"].append(current_segment)
            continue
        elif line.startswith("## CTA"):
            current_section = "cta"
            times = re.findall(r"(\d+)-(\d+)s", line)
            if times:
                result["cta"]["start"] = int(times[0][0])
                result["cta"]["end"] = int(times[0][1])
            continue
        elif line.startswith("## Pacing"):
            current_section = "pacing"
            continue
        elif line.startswith("## Style"):
            current_section = "style"
            continue
        elif line.startswith("## Source"):
            current_section = "source"
            continue
        elif line.startswith("## Segments"):
            current_section = "segments_header"
            continue
        elif line.startswith("## Why It Works"):
            current_section = "why"
            continue
        elif line.startswith("## Replication"):
            current_section = "replication"
            continue

        # Parse key-value pairs
        if line.startswith("- "):
            kv = line[2:]
            if ":" in kv:
                key, _, value = kv.partition(":")
                key = key.strip().lower()
                value = value.strip().strip('"\'')

                if current_section == "source":
                    if key == "duration":
                        result["total_duration_seconds"] = int(value)
                elif current_section == "hook":
                    if key == "technique":
                        result["hook"]["technique"] = value
                    elif key == "text":
                        result["hook"]["text_on_screen"] = value
                    elif key == "visual":
                        result["hook"]["description"] = value
                elif current_section == "segment" and current_segment is not None:
                    if key == "purpose":
                        current_segment["purpose"] = value
                    elif key == "text":
                        current_segment["text_on_screen"] = value
                    elif key == "visual":
                        current_segment["description"] = value
                    elif key == "camera":
                        current_segment["camera"] = value
                elif current_section == "cta":
                    if key == "type":
                        result["cta"]["type"] = value
                    elif key == "text":
                        result["cta"]["text_on_screen"] = value
                    elif key == "visual":
                        result["cta"]["description"] = value
                elif current_section == "pacing":
                    if key == "cuts":
                        result["pacing"]["total_cuts"] = int(value)
                    elif key == "energy":
                        result["pacing"]["energy"] = value
                    elif key == "music":
                        result["pacing"]["music_mood"] = value
                elif current_section == "style":
                    if key == "format":
                        result["style"]["format"] = value
                    elif key in ("text_style", "text style"):
                        result["style"]["text_style"] = value
                    elif key in ("color_mood", "color mood", "color"):
                        result["style"]["color_mood"] = value
        elif current_section == "why" and line:
            result["why_it_works"] = line
        elif current_section == "replication" and line:
            result["replication_notes"] = line

    return result


def analyze_with_gemini(video_path: str) -> dict:
    """Optional: analyze video with Gemini API."""
    import os
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")

    try:
        from google import genai
    except ImportError:
        print("Error: google-genai not installed. Run: pip install google-genai")
        sys.exit(1)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    import time
    video_file = Path(video_path)
    print(f"Uploading {video_file.name} to Gemini...")
    client = genai.Client(api_key=api_key)
    uploaded = client.files.upload(file=video_file)

    # Wait for file to become ACTIVE
    print("Waiting for file to be ready...")
    while uploaded.state.name != "ACTIVE":
        time.sleep(3)
        uploaded = client.files.get(name=uploaded.name)
        print(f"  File state: {uploaded.state.name}")

    print(f"Processing with Gemini...")

    prompt = """Analyze this video and return a JSON object with: total_duration_seconds, hook (start/end/technique/text_on_screen/description), segments (array of start/end/purpose/text_on_screen/description/camera), cta (start/end/type/text_on_screen/description), pacing (total_cuts/energy/music_mood), style (format/text_style/color_mood), why_it_works, replication_notes. Return ONLY valid JSON."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[uploaded, prompt],
    )

    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw[:-3]
    return json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description="Convert reel analysis to Remotion JSON")
    parser.add_argument("input", help="Path to .md analysis file OR video file (with --gemini)")
    parser.add_argument("--gemini", action="store_true", help="Use Gemini API (requires API key)")
    parser.add_argument("--output", "-o", help="Output JSON path")
    parser.add_argument("--template", action="store_true", help="Print blank template and exit")
    args = parser.parse_args()

    if args.template:
        print(TEMPLATE)
        return

    input_file = Path(args.input)
    if not input_file.exists():
        print(f"Error: File not found: {args.input}")
        sys.exit(1)

    if args.gemini:
        analysis = analyze_with_gemini(args.input)
    else:
        md_text = input_file.read_text(encoding="utf-8")
        analysis = parse_markdown(md_text)

    if args.output:
        out = Path(args.output)
    else:
        out = Path(__file__).parent.parent / ".tmp" / f"{input_file.stem}_analysis.json"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Analysis saved to: {out}")

    print("\n--- Summary ---")
    print(f"Duration: {analysis.get('total_duration_seconds', '?')}s")
    print(f"Hook: {analysis.get('hook', {}).get('technique', '?')}")
    print(f"Segments: {len(analysis.get('segments', []))}")
    print(f"CTA: {analysis.get('cta', {}).get('type', '?')}")


if __name__ == "__main__":
    main()
