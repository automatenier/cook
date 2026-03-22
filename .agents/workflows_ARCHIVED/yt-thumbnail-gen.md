---
description: Analyses a target YouTube thumbnail's face pose (yaw, pitch, roll) using MediaPipe, finds the best-matching reference photo of your face via Euclidean distance, and outputs a NanaBanana Pro face-swap prompt.
tags:
  - workflow
  - youtube
  - thumbnail
  - design
---

# Workflow: AI Thumbnail Matcher

**Tool:** `VLT_VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py`
**Trigger:** `/yt-thumbnail-match`

---

## Inputs Required

| Input | Flag | Default |
|-------|------|---------|
| Target thumbnail | `--thumbnail` | required (URL or local path) |
| Reference face folder | `--references` | required |
| Output folder | `--output-dir` | `.tmp/thumbnail_matches` |
| Top matches to show | `--top` | `3` |
| Extra prompt notes | `--extra` | optional |

---

## How It Works

1. **Download / load** — saves target thumbnail to `--output-dir/source_thumbnail.jpg`
2. **MediaPipe FaceMesh** — 468-point facial landmark detection on the source thumbnail → extracts yaw (left/right), pitch (up/down), roll (tilt) in degrees
3. **Reference scan** — runs MediaPipe on every image in `--references`, builds a pose vector `[yaw, pitch, roll]` for each
4. **Euclidean distance** — sorts references by `‖pose_source − pose_ref‖` (lower = better match)
5. **Outputs** — best match copy, full ranked JSON, NanaBanana prompt

### Why pose distance matters
A face-swap tool struggles when the reference photo faces a different direction than the thumbnail. By matching pose first, the swap looks natural instead of uncanny.

---

## Prerequisites

```bash
pip install -r VLT_VLT_Content/AI_ENGINE/yt_tools/requirements_yt.txt
# Installs: mediapipe, opencv-python, scipy, numpy
```

No API keys needed for the matching step.

---

## Reference Photo Tips

- **Quantity:** 15–30 photos gives good coverage of all angles
- **Angles to include:** dead-on front, 15° left, 15° right, 30° left, 30° right, slight up, slight down
- **Quality:** clear face, good lighting, no obstruction
- **Storage:** `VLT_VLT_Content/VLT_ASSETS/Jordan/reference_faces/` (recommended)
- **Format:** JPG, PNG, or WEBP all work

---

## Example Invocations

**From thumbnail URL:**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail "https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg" \
  --references "VLT_VLT_Content/VLT_ASSETS/Jordan/reference_faces/" \
  --top 3
```

**From local thumbnail file:**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail ".tmp/inspo_thumbnail.jpg" \
  --references "VLT_VLT_Content/VLT_ASSETS/Jordan/reference_faces/" \
  --output-dir ".tmp/thumbnail_matches/march_batch/"
```

**With extra NanaBanana instructions:**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail "https://..." \
  --references "VLT_VLT_Content/VLT_ASSETS/Jordan/reference_faces/" \
  --extra "Make the expression slightly more intense. Use warm skin tone."
```

---

## Outputs

| File | Description |
|------|-------------|
| `source_thumbnail.jpg` | Downloaded target thumbnail |
| `best_match_[name].jpg` | Your reference photo with closest pose |
| `ranked_matches.json` | All references ranked by pose distance |
| `nanobanana_prompt.txt` | Step-by-step face swap prompt for NanaBanana Pro |

---

## After Running

1. Open `nanobanana_prompt.txt` — it contains exact instructions for NanaBanana Pro
2. Upload `source_thumbnail.jpg` as the base image
3. Upload `best_match_*.jpg` as the reference face
4. Paste the prompt, set variations = 3
5. Pick the best output

If you don't have NanaBanana Pro yet, the matched reference photo + prompt work with:
- **Replicate** — `lucataco/faceswap` or `yan-ops/face-swap`
- **Stable Diffusion** + IP-Adapter FaceID
- **InsightFace** (open source, local)

---

## Common Errors

| Error | Fix |
|-------|-----|
| `No face detected in source thumbnail` | Use a cleaner thumbnail with a clearly visible face. Text-heavy or low-res thumbnails can fail. |
| `No faces detected in references folder` | Check photos have clear, well-lit faces. Remove group photos. |
| `mediapipe not installed` | `pip install mediapipe opencv-python` |
| `requests.exceptions.HTTPError` | Thumbnail URL may be private or require different headers — download manually and use `--thumbnail path/to/file.jpg` |

---

## Notes

- Run from the **Cook/ root directory**.
- Pose estimation is approximate (±5–10°) — it's good enough for matching, not surgery-precise.
- Distance < 10° = excellent match. 10–25° = good. > 30° = consider shooting a reference photo at that angle.
- The tool does NOT perform the face swap — it selects the optimal input for the swap tool.
