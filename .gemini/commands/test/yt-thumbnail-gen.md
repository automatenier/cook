> **Model: Haiku + Imagen** — face pose matching tool runner, then Gemini Imagen for generation

# Workflow: AI Thumbnail Matcher

**Tool:** `VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py`
**Trigger:** `/yt-thumbnail-match`

## Inputs Required

| Input | Flag | Default |
|-------|------|---------|
| Target thumbnail | `--thumbnail` | required (URL or local path) |
| Reference face folder | `--references` | required |
| Output folder | `--output-dir` | `.tmp/thumbnail_matches` |
| Top matches to show | `--top` | `3` |
| Extra prompt notes | `--extra` | optional |

## How It Works

1. **Download / load** — saves target thumbnail to `--output-dir/source_thumbnail.jpg`
2. **MediaPipe FaceMesh** — 468-point facial landmark detection → extracts yaw, pitch, roll in degrees
3. **Reference scan** — runs MediaPipe on every image in `--references`, builds a pose vector for each
4. **Euclidean distance** — sorts references by pose distance (lower = better match)
5. **Outputs** — best match copy, full ranked JSON, NanaBanana prompt

## Prerequisites

```bash
pip install -r VLT_Content/AI_ENGINE/yt_tools/requirements_yt.txt
# Installs: mediapipe, opencv-python, scipy, numpy
```

## Reference Photo Tips
- **Quantity:** 15–30 photos gives good coverage of all angles
- **Angles to include:** dead-on front, 15° left, 15° right, 30° left, 30° right, slight up, slight down
- **Storage:** `VLT_Content/03_ASSET/Jordan/reference_faces/`

## Example Invocations

```bash
# From thumbnail URL
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail "https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg" \
  --references "VLT_Content/03_ASSET/Jordan/reference_faces/" \
  --top 3

# From local thumbnail file
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail ".tmp/inspo_thumbnail.jpg" \
  --references "VLT_Content/03_ASSET/Jordan/reference_faces/" \
  --output-dir ".tmp/thumbnail_matches/march_batch/"

# With extra NanaBanana instructions
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_thumbnail_matcher.py \
  --thumbnail "https://..." \
  --references "VLT_Content/03_ASSET/Jordan/reference_faces/" \
  --extra "Make the expression slightly more intense. Use warm skin tone."
```

## After Running

1. Open `nanobanana_prompt.txt` — contains exact instructions for NanaBanana Pro
2. Upload `source_thumbnail.jpg` as the base image
3. Upload `best_match_*.jpg` as the reference face
4. Paste the prompt, set variations = 3, pick best output

## Common Errors

| Error | Fix |
|-------|-----|
| `No face detected in source thumbnail` | Use a cleaner thumbnail with a clearly visible face |
| `No faces detected in references folder` | Check photos have clear, well-lit faces. Remove group photos. |
| `mediapipe not installed` | `pip install mediapipe opencv-python` |
| `requests.exceptions.HTTPError` | Download thumbnail manually and use `--thumbnail path/to/file.jpg` |

## Notes
- Run from the **Cook/ root directory**.
- Pose estimation is approximate (±5–10°). Distance < 10° = excellent match.
- The tool does NOT perform the face swap — it selects the optimal input for the swap tool.
