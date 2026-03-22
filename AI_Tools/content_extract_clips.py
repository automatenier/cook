"""
Extract repurposable clips from a long-form YouTube script.

Analyzes a long script and returns a JSON manifest of 3–6 segments,
each classified by content type and best-fit platforms.

Usage:
    py -3 AI_Tools/extract_longform_clips.py --input "path/to/script.md" --pillar "AI"
    py -3 AI_Tools/extract_longform_clips.py --input "path/to/script.md" --pillar "Workflow & Automations"

Output:
    .tmp/clips_manifest.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

EXTRACT_PROMPT = """You are a content strategist analyzing a long-form YouTube script.

Your job: identify 3–6 moments in this script that are worth repurposing as short-form content.

Content pillars: {pillar}

For each clip, output:
- id: clip_01, clip_02, etc.
- title: short label (5 words max)
- excerpt: the exact lines from the script (verbatim, 50–150 words)
- type: one of — value | cta | story | proof
  - value: teaches something concrete
  - cta: drives an action (book a call, DM, follow)
  - story: personal experience or journey
  - proof: result, case study, number
- best_platforms: array — any of: reel, tiktok, threads, carousel, story, email, yt_short
- threads_type: one of — hard_truth | humble_brag | contrarian | vulnerable
- reel_format: one of — value | cta | authenticity

Script:
---
{script}
---

Rules:
- Only extract moments that can stand alone without the full video context
- Prioritize moments with a clear insight or hook
- Don't force a clip onto a platform where it won't land — be selective with best_platforms
- Return ONLY valid JSON array, no markdown wrapper"""


def extract_clips(script_path: str, pillar: str) -> list:
    """Extract repurposable clips from a long-form script."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    script = Path(script_path).read_text(encoding="utf-8")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = EXTRACT_PROMPT.format(pillar=pillar, script=script)

    print(f"Analyzing script: {script_path}")
    print(f"Content pillar: {pillar}")

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Haiku sufficient for extraction
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = message.content[0].text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.split("\n", 1)[1]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]

    clips = json.loads(raw_text)

    out_path = Path(__file__).parent.parent / ".tmp" / "clips_manifest.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(clips, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Manifest saved to: {out_path}")
    print(f"Extracted {len(clips)} clips:")
    for clip in clips:
        print(f"  [{clip['id']}] {clip['title']} — {clip['type']} → {', '.join(clip['best_platforms'])}")

    return clips


def main():
    parser = argparse.ArgumentParser(description="Extract repurposable clips from a long-form script")
    parser.add_argument("--input", "-i", required=True, help="Path to script .md file")
    parser.add_argument("--pillar", "-p", default="AI", help="Content pillar (AI / Social Media Marketing / Workflow & Automations)")
    args = parser.parse_args()

    extract_clips(args.input, args.pillar)


if __name__ == "__main__":
    main()
