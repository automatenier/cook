> **Model: Claude / Sonnet** -- deep reasoning required. Run from Claude Code, not Gemini.

# Workflow: Long-Form Script -> Full Repurpose

**Trigger in Claude Code:** `/repurpose-longform [ScriptPath]`

This workflow requires identifying which moments in a 1000-3000 word script are worth extracting, classifying by content type, and deciding which platform fits each insight. That's strategy -- not template filling. Claude handles Phase 1. The tool handles Phase 2.

## Phase 1 -- Script Analysis & Clip Extraction

```bash
py -3 AI_Tools/content_extract_clips.py --input "[ScriptPath]" --pillar "[ContentPillar]"
# Outputs: .tmp/clips_manifest.json
```

If the tool doesn't exist yet: do Phase 1 inline -- read script, identify 3-6 repurposable moments.

## Phase 2 -- Repurpose Each Clip

```bash
py -3 AI_Tools/content_repurpose.py --input ".tmp/[clip_id]_excerpt.md" --type [reel_format]
```

Threads posts and carousels are generated inline by Claude.

## Phase 3 -- Save Outputs

```
[WorkspacePath]/projects/[YYYY-MM]/longform-repurpose/[YYYY-MM-DD]_[slug]/
  reel_scripts.md | threads.md | carousels.md | stories.md | email.md | yt_shorts_briefs.md
```

Run `/compact` after this workflow completes.
