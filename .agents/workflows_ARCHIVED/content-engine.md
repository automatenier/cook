---
description: How to operate the JO Content Engine to generate social media assets.
tags:
  - workflow
---

# JO Content Engine Workflow

7 stages from viral swipe to a tracked, high-performing post.

## Phase 1: Ingestion & Ideation
**Where:** `VLT_Content/HMN_A INPUTS/`
**Who:** Agent
- Drop viral video links and transcripts into `VLT_Content/HMN_A INPUTS/` or `VLT_Content/HMN_A INPUTS/Swipe Files/`.
- The Agent analyzes structures against `VLT_Content/00_SYSTEM/A Human Instruction/viral_checklist.md`.

## Phase 2: AI Copywriting
**Where:** `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/scripts/`
**Who:** Agent
- Run `/write-scripts [ClientName]`
- Agent reads `client_brief.md`, connects swipe structure to client pain points, drafts hooks + scripts.

## Phase 3: Review
**Where:** `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/scripts/`
**Who:** User
- Open the script file, request tweaks or mark as APPROVED.
- Move approved scripts to `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/approved/`.

## Phase 4: Visual Production
**Where:** `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/`
**Who:** User (CapCut) & Agent (Remotion)
- **Complex Edits:** Edit in CapCut using approved scripts and raw footage from `VLT_Content/02_WORKSPACE/[ClientName]/1_Footage/`.
- **Simple Edits:** Run `/render-simple-reel [ClientName] [ScriptRef]` for Remotion text-over-video renders.

## Phase 5: Output & Scheduling
**Where:** `VLT_Content/04_OUTPUTS/[ClientName]/`
**Who:** User
- Final `.mp4` and `.png` deliverables go to `VLT_Content/04_OUTPUTS/[ClientName]/`.
- Schedule natively via Meta Business Suite / Instagram app.

## Phase 6: Archiving
**Where:** `VLT_Content/05_ARCHIVE/`
**Who:** Agent
- Periodically move posted content from `VLT_Content/04_OUTPUTS/` to `VLT_Content/05_ARCHIVE/` to keep the workspace clean.

## Phase 7: Tracking
**Where:** n8n → `PDCT_JO_Consult/1_Sales_Pipeline/content_tracker.xlsx`
**Who:** Automation (n8n)
- n8n fetches post metrics every few days via API.
- Logs Views, Saves, Engagement into `PDCT_JO_Consult/1_Sales_Pipeline/content_tracker.xlsx`.
- Review to decide which structures (Hooks, Topics) to repeat in Phase 1.

## Tool Invocation Examples

```bash
# Phase 1 — capture a viral reference to swipe files
py -3 AI_Tools/vault_youtube_note.py https://youtu.be/EXAMPLE_ID

# Phase 2 — write scripts for a client
/write-scripts fadli

# Phase 4 — render a simple text-over-video reel
/render-simple-reel fadli reel_01

# Phase 4 (alternative) — analyze a reference reel and render via Remotion
py -3 AI_Tools/content_analyze_viral_reel.py .tmp/reel_reference_notes.md

# Post-approval — repurpose to all platforms
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_WORKSPACE/fadli/projects/2026-02/approved/reel_01.md"

# Generate metadata (captions, hashtags, thumbnail brief)
/generate-metadata fadli reel_01
```
