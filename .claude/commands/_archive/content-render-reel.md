> **Model: Haiku** — Remotion props and render execution (mechanical)

# Workflow: Render Reel

---

## CRITICAL RULES — READ BEFORE DOING ANYTHING

1. **NEVER run `npm run build`** — it renders ALL compositions and wastes hours of CPU. Always target a specific composition.
2. **NEVER use `.mov` files directly in Remotion** — they are VFR and will jitter. Pre-process first.
3. **NEVER use the `loop` prop on `<Video />`** — it causes a 1-frame freeze at every loop seam. Pre-bake loops with FFmpeg instead.
4. **ALWAYS pre-process footage before touching `props.json` or `Root.tsx`.**

---

## Step-by-Step

### Step 1 — Identify the composition ID

Check `VLT_Content/AI_ENGINE/remotion/src/Root.tsx` for the `id=` of the composition to render.

Common IDs:
- `reproduction-video` — multi-clip video with voiceover
- `ValueCTAReel`, `AuthenticityReel`, `TierListReel`, etc.

### Step 2 — Check source footage

List `VLT_Content/AI_ENGINE/remotion/public/` and identify:
- Are source files `.mov` or non-standard FPS? → **MUST pre-process (Step 3)**
- Are source files already `_fixed.mp4`? → skip to Step 4

### Step 3 — Pre-process footage (MANDATORY for .mov or VFR sources)

Run FFmpeg in this exact order. Do NOT skip either sub-step.

**3a. Convert to CFR 30fps H264 MP4:**
```bash
# Run once per source file:
ffmpeg -y -i 1.mov -filter:v fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p -an 1_cfr.mp4
ffmpeg -y -i 2.mov -filter:v fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p -an 2_cfr.mp4
ffmpeg -y -i 3.mov -filter:v fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p -an 3_cfr.mp4
```

Flags explained:
- `-filter:v fps=30` — forces Constant Frame Rate at exactly 30.00 FPS (fixes jitter)
- `-crf 18` — near-lossless quality
- `-pix_fmt yuv420p` — browser-compatible
- `-an` — strip audio (audio is handled separately via the `videoSrc` Audio component)

**3b. Pre-bake loops + trim to segment duration:**

First, get each clip's duration:
```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 1_cfr.mp4
```

Then calculate how many loop repetitions are needed for each segment:
- `segments_needed = ceil(segment_duration_seconds / clip_duration_seconds)`
- Use `-stream_loop N` where N = segments_needed (N loops means N+1 total plays)
- Trim with `-t [segment_duration + 0.1]` as a buffer

Example (segment = 24s, clip = 9.6s → need 3 plays → `-stream_loop 2`):
```bash
ffmpeg -y -stream_loop 2 -i 1_cfr.mp4 -t 24.1 -c copy 1_fixed.mp4
ffmpeg -y -stream_loop 2 -i 2_cfr.mp4 -t 24.1 -c copy 2_fixed.mp4
ffmpeg -y -stream_loop 3 -i 3_cfr.mp4 -t 24.1 -c copy 3_fixed.mp4
```

Output naming: always `[N]_fixed.mp4`.

### Step 4 — Update props.json

In `VLT_Content/AI_ENGINE/remotion/src/props.json`, update `backgroundVideos` srcs:
```json
{ "src": "1_fixed.mp4", "start": 0, "end": 720 },
{ "src": "2_fixed.mp4", "start": 720, "end": 1440 },
{ "src": "3_fixed.mp4", "start": 1440, "end": 2144 }
```

Never reference `.mov` files in props.json.

### Step 5 — Check ReproductionReel.tsx has NO loop prop

In `VLT_Content/AI_ENGINE/remotion/src/ReproductionReel.tsx`, the `<Video />` component must NOT have a `loop` prop:
```tsx
// CORRECT:
<Video src={staticFile(bg.src)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} muted />

// WRONG — causes 1-frame freeze at seam:
<Video src={staticFile(bg.src)} ... muted loop />
```

If `loop` is present, remove it.

### Step 6 — Render ONE composition

Use the named npm script or target the composition directly:

```bash
# Named scripts (preferred):
cd VLT_Content/AI_ENGINE/remotion
npm run render-reproduction     # → out/reproduction_fixed.mp4
npm run render-value            # → out/value-reel.mp4
npm run render-auth             # → out/auth-reel.mp4

# Generic (for any composition ID):
npx remotion render src/index.ts [composition-id] --output out/[filename].mp4
```

**NEVER run `npm run build`** — it has no `--id` flag and renders every composition in Root.tsx.

### Step 7 — Move output

```bash
mv VLT_Content/AI_ENGINE/remotion/out/[filename].mp4 VLT_Content/04_HMN_OUTPUTS/[ClientName]/
```

---

## Why Jitter Happens — Quick Reference

| Root Cause | Symptom | Fix |
|---|---|---|
| `.mov` VFR source (~29.79 FPS) | Rhythmic hitch every ~1s | `ffmpeg -filter:v fps=30` |
| Non-CFR → browser can't predict frame position | Video jumps ±a few ms | Same CFR fix |
| `loop` prop on `<Video />` | 1-frame freeze at every loop seam | Pre-bake with `ffmpeg -stream_loop` |
| Audio embedded in video file | Drift between audio and video over time | `-an` flag on CFR step; audio via separate `<Audio src={videoSrc} />` |

---

## Render Decision

| Scenario | Command |
|---|---|
| Single composition, local | `npm run render-[name]` or `npx remotion render src/index.ts [id]` |
| Batch (2+ compositions) | Modal — zero local CPU |
| Jordan's machine off | Modal always |

## Modal Batch Render

```bash
py -3 AI_Tools/content_render_manager.py --client fadli
py -3 AI_Tools/content_render_manager.py --client fadli --dry-run
py -3 AI_Tools/content_render_manager.py --client fadli --month 2026-03

# Redeploy after code changes:
PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/cook_modal_app.py
```
