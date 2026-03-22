"""
Repurpose finished content into multiple platform formats using Claude.

Takes your completed script/storyboard/handoff and generates:
- Music recommendation (genre, BPM, track suggestions)
- Pacing beat map (matched to your duration)
- IG Reel caption + hashtags + cover text
- TikTok caption + hashtags + hook text
- Threads post (lead magnet angle)
- Story sequence (3 slides)
- Newsletter email (expanded value)
- YouTube script outline (long-form deep dive)

Claude does NOT rewrite your creative. It preserves your hook and voice, adapts format per platform.

Usage:
    python tools/repurpose_content.py <input_file> [--type reel-value|reel-auth]
    python tools/repurpose_content.py --text "your caption or transcript here"
    python tools/repurpose_content.py VLT_Content/clients/jordan/projects/250218_hook/brief.md
"""

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")


REPURPOSE_PROMPT = """You are a content repurposing engine for JO Consult, an Indonesian online business coaching brand.

Your job is to take FINISHED content (a reel script, storyboard, or transcript) and produce everything needed to publish it across all platforms. You do NOT rewrite the creative. You preserve the voice, hook, and message exactly — then adapt format per platform.

Content type: {content_type}

Original content:
---
{content}
---

Generate ALL of the following. Return as JSON with this exact structure:

{{
  "music": {{
    "vibe": "<1-2 words: e.g. 'calm confident' or 'hype energetic'>",
    "genre": "<e.g. lo-fi hip hop / trap / cinematic / acoustic pop>",
    "bpm": "<e.g. 90-100 BPM for calm, 120-140 for hype>",
    "track_suggestions": ["<track name or description 1>", "<track name or description 2>", "<track name or description 3>"],
    "platform_note": "<e.g. 'Use trending audio on TikTok if available — original audio on IG for brand recognition'>"
  }},
  "pacing": {{
    "total_duration": "<detected or recommended duration, e.g. '30s'>",
    "beat_map": ["<0-3s: hook line on screen>", "<3-8s: problem 1>", "<8-15s: problem 2-3>", "<15-25s: solution>", "<25-30s: CTA>"]
  }},
  "ig_reel": {{
    "caption": "<IG caption. Hook first line (no emojis on line 1). Value in body. CTA at end. 150-300 chars before 'more'>",
    "hashtags": ["<10-15 relevant hashtags>"],
    "cover_text": "<text overlay for reel cover/thumbnail, 3-5 words max>"
  }},
  "tiktok": {{
    "caption": "<TikTok caption, punchier. Max 150 chars>",
    "hashtags": ["<8-10 TikTok-specific hashtags>"],
    "hook_text": "<on-screen text for first 2s>"
  }},
  "threads_post": {{
    "text": "<Threads post, 300-500 chars. Lead magnet angle — give value then soft CTA. Line breaks for readability>",
    "cta": "<specific CTA, e.g. 'Comment GUIDE for the free template'>"
  }},
  "story_sequence": [
    {{
      "slide": 1,
      "text": "<hook/question>",
      "visual": "<what to show: talking head / text card / poll sticker>"
    }},
    {{
      "slide": 2,
      "text": "<slide 2 text>",
      "visual": "<description>"
    }},
    {{
      "slide": 3,
      "text": "<CTA slide>",
      "visual": "<link sticker / DM prompt / swipe up>"
    }}
  ],
  "newsletter_email": {{
    "subject_line": "<compelling subject, 5-8 words>",
    "preview_text": "<1 sentence preview>",
    "body": "<expanded version of the reel. 200-400 words. Conversational, personal. End with soft CTA to book a call or reply>"
  }},
  "youtube_outline": {{
    "title": "<SEO-friendly YouTube title>",
    "hook": "<first 30s script>",
    "sections": ["<section 1>", "<section 2>", "<section 3>"],
    "cta": "<end CTA>",
    "description": "<2-3 sentence YouTube description with keywords>"
  }}
}}

Rules:
- Preserve exact hook wording from original — don't rephrase it
- Indonesian market context (Bahasa or mixed Bahasa/English is fine)
- Online business coaching niche (NOT fitness — this is about helping coaches scale with AI/systems)
- Music suggestions should match the vibe of the script, not generic
- Beat map must match the actual duration if specified
- Return ONLY valid JSON"""


def repurpose(content: str, content_type: str = "reel-value", output_path: str | None = None) -> dict:
    """Repurpose content using Claude."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    prompt = REPURPOSE_PROMPT.format(content_type=content_type, content=content)

    print("Sending to Claude for repurposing...")
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = message.content[0].text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.split("\n", 1)[1]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]

    result = json.loads(raw_text)

    if output_path:
        out = Path(output_path)
    else:
        out = Path(__file__).parent.parent / ".tmp" / "repurposed_content.json"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Repurposed content saved to: {out}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Repurpose content with Claude")
    parser.add_argument("input_file", nargs="?", help="Path to text file with content")
    parser.add_argument("--text", "-t", help="Direct text input instead of file")
    parser.add_argument("--type", dest="content_type", default="reel-value",
                        choices=["reel-value", "reel-auth", "youtube", "story"],
                        help="Type of source content")
    parser.add_argument("--output", "-o", help="Output JSON path")
    args = parser.parse_args()

    if args.text:
        content = args.text
    elif args.input_file:
        content = Path(args.input_file).read_text(encoding="utf-8")
    else:
        print("Error: provide either a file path or --text")
        sys.exit(1)

    result = repurpose(content, args.content_type, args.output)

    print("\n--- Generated Formats ---")
    print(f"Threads: {result['threads_post']['text'][:80]}...")
    print(f"Email subject: {result['newsletter_email']['subject_line']}")
    print(f"YouTube title: {result['youtube_script_outline']['title']}")
    print(f"TikTok: {result['tiktok_caption']['text'][:80]}...")
    print(f"Stories: {len(result['story_sequence'])} slides")


if __name__ == "__main__":
    main()
