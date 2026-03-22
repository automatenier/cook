---
description: Agent workflow to generate simple visuals using the Remotion/Stitcher engine.
---

# Workflow: Render Simple Reel

When user asks to `/render-simple-reel [ClientName] [ScriptRef]`:

1. **Read Script**: Locate the approved script at `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`.
2. **Place Assets** (REQUIRED — render will produce blank output without these):
   - Copy client footage → `VLT_Content/40_ENGINE/remotion/public/user-video.mp4`
   - Copy music track → `VLT_Content/40_ENGINE/remotion/public/music.mp3`
   - If either file is missing, stop and ask Jordan before proceeding.
   - Music volume defaults to 0.25 (25%) — adjust in component if needed.
   - Dark overlay is 45% opacity — adjust `rgba(0,0,0,X)` in component if text is hard to read.
3. **Update Engine**: Update `defaultProps` in `VLT_Content/40_ENGINE/remotion/src/Root.tsx` to match the script's hook, value, and CTA text.
4. **Execute Build**:
    ```bash
    cd VLT_Content/40_ENGINE/remotion
    npm run build
    # or for stitcher:
    node VLT_Content/40_ENGINE/stitcher.js
    ```
5. **Move to Outputs**: After rendering, move the `.mp4` or `.png` output to `VLT_Content/04_OUTPUTS/[ClientName]/`.
6. **Notify User**: Inform the user the deliverable is ready at `VLT_Content/04_OUTPUTS/[ClientName]/`.

## Render Decision — Local vs Modal

| Scenario | Use |
|---|---|
| **Batch render (2+ scripts)** | Modal — zero local CPU |
| Single test render | Local (`npm run build`) |
| Jordan's machine is off / lagging | Modal always |

**Rule: Default to Modal for any batch. Local is for one-off tests only.**

## Modal Batch Render (Preferred)

```bash
# Render all pending scripts for Fadli (skips already-done files)
py -3 AI_Tools/render_batch_modal.py --client fadli

# Preview what will render without actually running (dry run)
py -3 AI_Tools/render_batch_modal.py --client fadli --dry-run

# Render a specific month only
py -3 AI_Tools/render_batch_modal.py --client fadli --month 2026-03

# Render all clients at once
py -3 AI_Tools/render_batch_modal.py --all

# Re-render already-done files (force)
py -3 AI_Tools/render_batch_modal.py --client fadli --force
```

Outputs land in `VLT_Content/04_OUTPUTS/[client]/[script-stem].mp4`.
All renders fire **in parallel** on Modal — laptop stays free.

First time or after code changes: redeploy Modal before running:
```bash
PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/cook_modal_app.py
```

## Local Render (Single Scripts Only)

```bash
# Optional: analyze a reference reel markdown file first (outputs Remotion-ready JSON)
py -3 AI_Tools/content_analyze_viral_reel.py .tmp/reel_reference_notes.md

# Build the Remotion render (from project root)
cd VLT_Content/40_ENGINE/remotion && npm run build

# Or use the stitcher for simple text-over-video
node VLT_Content/40_ENGINE/stitcher.js

# Output location
# VLT_Content/04_OUTPUTS/fadli/reel_01.mp4
```
