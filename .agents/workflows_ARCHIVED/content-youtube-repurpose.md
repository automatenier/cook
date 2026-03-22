---
description: Analyzes a long-form YouTube script and repurposes it into reels, threads, carousels, stories, and email across all supported platforms.
tags:
  - workflow
  - youtube
  - repurpose
---

# Workflow: Long-Form Script → Full Repurpose

**Agent:** Claude
**Trigger:** `/repurpose-longform [ScriptPath]`

---

## Why Claude, Not Gemini

This workflow requires deep reasoning: identifying which moments in a 1000–3000 word script are worth extracting, classifying each by content type, and deciding which platform fits each insight. That's strategy — not template filling. Claude handles Phase 1. The tool handles Phase 2.

---

## Inputs Required

| Input | Description |
|-------|-------------|
| `ScriptPath` | Path to the long-form YouTube script `.md` file |
| `Channel` | Whose channel — Jordan or client name (determines voice/persona) |
| `ContentPillar` | Social Media Marketing / AI / Workflow & Automations |

---

## Supported Output Formats

| Format | Variants | Tool |
|--------|----------|------|
| IG Reel script | Value / CTA / Authenticity | `repurpose_content.py` |
| TikTok clip | — | `repurpose_content.py` |
| Threads post | Hard Truth / Humble Brag / Contrarian / Vulnerable | Inline (Claude) |
| IG Carousel | Value / Proof | Inline (Claude) |
| IG Stories | 3-slide sequence | `repurpose_content.py` |
| Newsletter email | — | `repurpose_content.py` |
| YouTube Short brief | Hook + key moment | Inline (Claude) |

---

## Phase 1 — Script Analysis & Clip Extraction

### Step 1: Read the script
```
Read: [ScriptPath]
```

### Step 2: Extract repurposable segments

Run the extraction tool:
```bash
py -3 AI_Tools/content_extract_clips.py --input "[ScriptPath]" --pillar "[ContentPillar]"
```

This outputs a **clip manifest** JSON to `.tmp/clips_manifest.json` with this structure:
```json
[
  {
    "id": "clip_01",
    "title": "Short label for the insight",
    "excerpt": "The exact lines from the script",
    "type": "value | cta | story | proof",
    "best_platforms": ["reel", "threads", "carousel"],
    "threads_type": "hard_truth | humble_brag | contrarian | vulnerable",
    "reel_format": "value | cta | authenticity"
  }
]
```

> **If the tool doesn't exist yet:** Do Phase 1 inline. Read the script, identify 3–6 repurposable moments, and construct the manifest manually before proceeding to Phase 2.

---

## Phase 2 — Repurpose Each Clip

For each clip in the manifest, run based on `best_platforms`:

### Reels + TikTok + Stories + Email
```bash
py -3 AI_Tools/content_repurpose.py --input ".tmp/[clip_id]_excerpt.md" --type [reel_format]
```

### Threads Posts (4 types)
Generate inline using the persona in `VLT_Content/00_SYSTEM/Agent Instructions/Reels V2/Thread Prompt.md`.

For each clip flagged for Threads:
- Write 1 post in the assigned `threads_type`
- Indonesian version + English version
- Max 280 chars per post, line breaks for dramatic effect
- No emojis, no hashtags in body

### Carousels
For each clip flagged for Carousel:
- Slide 1: Bold hook (5 words max)
- Slides 2–6: One insight per slide, plain text
- Last slide: CTA (DM / follow / comment keyword)
- Write ID version + EN version

### YouTube Shorts Brief
For each clip flagged as a strong short:
- Hook (first 3s on screen)
- Talking point (15–30s)
- End screen CTA

---

## Phase 3 — Save Outputs

Write all outputs to:
```
[WorkspacePath]/projects/[YYYY-MM]/longform-repurpose/[YYYY-MM-DD]_[script-slug]/
  ├── manifest.json          ← clip manifest
  ├── reel_scripts.md        ← all reel scripts
  ├── threads.md             ← all threads posts (ID + EN)
  ├── carousels.md           ← all carousel copy
  ├── stories.md             ← all story sequences
  ├── email.md               ← newsletter email
  └── yt_shorts_briefs.md    ← YouTube Shorts briefs
```

**Workspace path:**
- Jordan's personal channel: `HMN_A Human/youtube/` ← [TODO: confirm this path]
- Client: `VLT_Content/02_WORKSPACE/[client]/projects/[YYYY-MM]/longform-repurpose/`

---

## Quality Rules

- **Never paraphrase the hook** — preserve the exact wording from the original script
- **Voice consistency** — Jordan's Threads voice: Anak Jaksel tone, raw, conversational, Bahasa/English mix
- **Platform fit first** — don't force a clip onto a platform where it doesn't land naturally. Drop it if it doesn't fit.
- **CTA variety** — don't repeat the same CTA across all clips. Rotate: comment keyword / DM / follow / book a call
- **Content pillar check** — every output must map to one of: Social Media Marketing / AI / Workflow & Automations

---

## Token Economy Note

Phase 1 inline analysis = ~1 Claude call. Each repurpose_content.py run = 1 API call. For a 6-clip manifest, expect 6–8 tool calls total. Run `/compact` after this workflow completes.

---

## Notes / Learnings

<!-- Document any edge cases, script length limits, or tone issues encountered here -->

- [ ] Build `AI_Tools/content_extract_clips.py` to automate Phase 1
- [ ] Confirm output path for Jordan's personal YouTube content (`HMN_A Human/youtube/` vs other)
- [ ] Test with a real script to validate clip extraction quality
