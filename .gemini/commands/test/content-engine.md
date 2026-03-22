> **Model: Sonnet** -- orchestration across all 7 content pipeline stages

# JO Content Engine Workflow

7 stages from viral swipe to a tracked, high-performing post.

## Phase 1: Ingestion & Ideation
**Where:** `VLT_Content/01_HMN_INPUTS/Swipe Files/`
- Drop viral video links and transcripts here.
- Agent analyzes structures against viral checklist.

## Phase 2: AI Copywriting
**Where:** `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/scripts/`
- Run `/write-scripts [ClientName]`
- Agent reads `client_brief.md`, drafts hooks + scripts.

## Phase 3: Review (Human)
- Open script, request tweaks or mark APPROVED.
- Move approved scripts to `...approved/`.

## Phase 4: Visual Production
- Complex edits -> CapCut
- Simple edits -> `/render-simple-reel [ClientName] [ScriptRef]`

## Phase 5: Output & Scheduling
**Where:** `VLT_Content/04_HMN_OUTPUTS/[ClientName]/`
- Schedule via Meta Business Suite / Instagram app.

## Phase 6: Archiving
**Where:** `VLT_Content/ZZ_ARCHIVE/`
- Move posted content from `04_HMN_OUTPUTS/` to archive.

## Phase 7: Tracking
- n8n fetches post metrics, logs to `01 HMN__Command/00_CONTENT/`.

## Tool Invocation
```bash
py -3 AI_Tools/vault_youtube_note.py https://youtu.be/EXAMPLE_ID
/write-scripts fadli
/render-simple-reel fadli reel_01
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/projects/2026-03/approved/reel_01.md"
/generate-metadata fadli reel_01
```
