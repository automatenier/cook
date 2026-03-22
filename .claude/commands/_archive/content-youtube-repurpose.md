---
description: Repurpose a long-form YouTube script into short content. Claude-only -- requires deep reasoning.
tags:
  - claude-config
  - content
---
> **Model: Sonnet** -- deep reasoning required for clip selection and platform fit

# Workflow: Long-Form Script -> Full Repurpose

**Trigger:** `/repurpose-longform [ScriptPath]`

This workflow requires identifying which moments in a 1000-3000 word script are worth extracting, classifying by content type, and deciding which platform fits each insight. Claude handles Phase 1. The tool handles Phase 2.

## Inputs

| Input | Description |
|-------|-------------|
| ScriptPath | Path to long-form YouTube script .md |
| Channel | Jordan or client name (determines voice/persona) |
| ContentPillar | Social Media Marketing / AI / Workflow & Automations |

## Supported Output Formats

| Format | Variants | Method |
|--------|----------|--------|
| IG Reel script | Value / CTA / Authenticity | content_repurpose.py |
| TikTok clip | -- | content_repurpose.py |
| Threads post | Hard Truth / Humble Brag / Contrarian / Vulnerable | Inline (Claude) |
| IG Carousel | Value / Proof | Inline (Claude) |
| IG Stories | 3-slide sequence | content_repurpose.py |
| Newsletter email | -- | content_repurpose.py |
| YouTube Short brief | Hook + key moment | Inline (Claude) |

## Phase 1 -- Script Analysis & Clip Extraction

```bash
py -3 AI_Tools/content_extract_clips.py --input "[ScriptPath]" --pillar "[ContentPillar]"
# Outputs: .tmp/clips_manifest.json
```

Manifest structure:
```json
[{
  "id": "clip_01",
  "title": "Short label",
  "excerpt": "Exact lines from script",
  "type": "value | cta | story | proof",
  "best_platforms": ["reel", "threads", "carousel"],
  "threads_type": "hard_truth | humble_brag | contrarian | vulnerable",
  "reel_format": "value | cta | authenticity"
}]
```

If tool doesn't exist: do Phase 1 inline -- read script, identify 3-6 repurposable moments, construct manifest manually.

## Phase 2 -- Repurpose Each Clip

```bash
py -3 AI_Tools/content_repurpose.py --input ".tmp/[clip_id]_excerpt.md" --type [reel_format]
```

**Threads** -- inline, for each clip flagged for Threads:
- 1 post per threads_type, Indonesian + English version
- Max 280 chars, line breaks for dramatic effect. No emojis, no hashtags in body.

**Carousels** -- inline:
- Slide 1: Bold hook (5 words max). Slides 2-6: one insight each. Last: CTA.
- ID + EN version.

## Phase 3 -- Save Outputs

```
VLT_Content/02_HMN_HUMANFLOW/jocons/[client]/projects/[YYYY-MM]/longform-repurpose/[YYYY-MM-DD]_[slug]/
  manifest.json | reel_scripts.md | threads.md | carousels.md | stories.md | email.md | yt_shorts_briefs.md
```

## Quality Rules
- Never paraphrase the hook -- preserve exact wording from original script
- Jordan's Threads voice: Anak Jaksel tone, raw, conversational, Bahasa/English mix
- Platform fit first -- don't force a clip where it doesn't land
- CTA variety -- rotate: comment keyword / DM / follow / book a call

Run `/compact` after this workflow completes (~6-8 tool calls for a 6-clip manifest).
