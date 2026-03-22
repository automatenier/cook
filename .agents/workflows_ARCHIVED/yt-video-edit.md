---
description: Edits a raw talking-head video — silence removal (Silero VAD), mistake cuts (Whisper), audio enhancement, color grading, and optional intro prepend.
tags:
  - workflow
  - youtube
  - video-editing
---

# Workflow: AI Video Editor

**Tool:** `VLT_VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py`
**Trigger:** `/yt-video-edit`

---

## Inputs Required

| Input | Flag | Default |
|-------|------|---------|
| Raw video file | `--input` | required |
| Output path | `--output` | required |
| Intro clip (swivel teaser) | `--intro` | optional |
| Trigger words | `--trigger-words` | `"ugh,no wait,um actually,start over,let me redo,cut that,forget it"` |
| Min silence gap | `--min-silence-ms` | `500` |
| Whisper model | `--whisper-model` | `base` |

---

## What It Does

1. **Extracts audio** — 16kHz mono WAV for VAD + Whisper
2. **Silero VAD** — finds all speech regions, drops silence gaps longer than `--min-silence-ms`
3. **Whisper transcription** — word-level timestamps detect trigger words; the entire VAD segment containing the trigger is cut (the failed take). If the trigger fires at the very start of a segment and the previous segment ends within 1s, both are removed (handles "no wait, that was wrong about the last thing" pattern).
4. **Audio enhancement** — noise reduction (afftdn), high-pass 80Hz, low-pass 14kHz, EBU R128 loudness normalisation
5. **Color grading** — +5% contrast, +10% saturation, slight warm tone curve
6. **Intro prepend** — if `--intro` is provided, the swivel teaser is concatenated before the body
7. **Hardware-accelerated export** — auto-detects NVENC (NVIDIA) → VideoToolbox (Apple) → libx264 (CPU)

---

## Prerequisites

```bash
# 1. FFmpeg (system binary)
winget install FFmpeg          # Windows
brew install ffmpeg            # Mac

# 2. Python packages
pip install -r VLT_VLT_Content/AI_ENGINE/yt_tools/requirements_yt.txt
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

First run downloads Silero VAD model (~2MB) and the chosen Whisper model (base ~145MB).

---

## Example Invocations

**Basic (silence removal only):**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input "01_HMN_INPUTS/raw/my_video.mp4" \
  --output ".tmp/edited.mp4" \
  --skip-whisper
```

**Full pipeline with intro:**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input "01_HMN_INPUTS/raw/my_video.mp4" \
  --output "04_HMN_OUTPUTS/Jordan/my_video_edited.mp4" \
  --intro "VLT_VLT_Content/03_ASSET/Jordan/swivel_teaser.mp4" \
  --trigger-words "ugh,no wait,start over,let me try again"
```

**Higher accuracy (slower):**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input raw.mp4 --output edited.mp4 \
  --whisper-model small
```

---

## Outputs

| File | Location |
|------|----------|
| Edited video | `--output` path |

---

## Common Errors

| Error | Fix |
|-------|-----|
| `FFmpeg not found in PATH` | Install FFmpeg and restart terminal |
| `torch not installed` | `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu` |
| `openai-whisper not installed` | `pip install openai-whisper` |
| No segments remain after processing | Loosen `--trigger-words` or use `--skip-whisper` |
| Output is too short | Increase `--min-silence-ms` (e.g. `800`) |

---

## Notes

- Run from the **Cook/ root directory** so `.env` and output paths resolve correctly.
- Whisper `base` model is fast and accurate enough for clean audio. Use `small` for heavy accents or low-quality recording.
- The first Silero VAD run downloads a model from torch hub — needs internet once.
- If Silero VAD gives too many false positives, increase `--min-silence-ms` to `700`.
