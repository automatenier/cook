> **Model: Haiku** — Remotion props and render execution (mechanical)

# Workflow: Render Simple Reel

When user asks to `/render-simple-reel [ClientName] [ScriptRef]`:

1. **Read Script**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`
2. **Place Assets** (REQUIRED):
   - Client footage -> `VLT_Content/40_ENGINE/remotion/public/user-video.mp4`
   - Music track -> `VLT_Content/40_ENGINE/remotion/public/music.mp3`
   - If either is missing, stop and ask Jordan.
3. **Update Engine**: Update `defaultProps` in `VLT_Content/40_ENGINE/remotion/src/Root.tsx`.
4. **Execute Build**:
   ```
   cd VLT_Content/40_ENGINE/remotion && npm run build
   ```
5. **Move to Outputs**: `VLT_Content/04_HMN_OUTPUTS/[ClientName]/`

## Render Decision

| Scenario | Use |
|---|---|
| Batch (2+) | Modal -- zero local CPU |
| Single test | Local (npm run build) |
| Jordan's machine off | Modal always |

## Modal Batch Render (Preferred)

```bash
py -3 AI_Tools/render_batch_modal.py --client fadli
py -3 AI_Tools/render_batch_modal.py --client fadli --dry-run
py -3 AI_Tools/render_batch_modal.py --client fadli --month 2026-03
py -3 AI_Tools/render_batch_modal.py --all

# Redeploy after code changes:
PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/cook_modal_app.py
```

## Local Render (Single Only)

```bash
py -3 AI_Tools/content_analyze_viral_reel.py .tmp/reel_reference_notes.md
cd VLT_Content/40_ENGINE/remotion && npm run build
```
