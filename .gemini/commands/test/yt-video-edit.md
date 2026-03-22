> **Model: Haiku** — tool runner, mechanical execution

# Workflow: AI Video Editor

**Tool:** `VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py`
**Trigger:** `/yt-video-edit`

## Inputs Required

| Input | Flag | Default |
|-------|------|---------|
| Raw video file | `--input` | required |
| Output path | `--output` | required |
| Intro clip (swivel teaser) | `--intro` | optional |
| Trigger words | `--trigger-words` | `"ugh,no wait,um actually,start over,let me redo,cut that,forget it"` |
| Min silence gap | `--min-silence-ms` | `500` |
| Whisper model | `--whisper-model` | `base` |

## What It Does

1. **Extracts audio** — 16kHz mono WAV for VAD + Whisper
2. **Silero VAD** — finds all speech regions, drops silence gaps longer than `--min-silence-ms`
3. **Whisper transcription** — word-level timestamps detect trigger words; the entire VAD segment containing the trigger is cut
4. **Audio enhancement** — noise reduction, high-pass 80Hz, low-pass 14kHz, EBU R128 loudness normalisation
5. **Color grading** — +5% contrast, +10% saturation, slight warm tone curve
6. **Intro prepend** — if `--intro` is provided, swivel teaser is concatenated before the body
7. **Hardware-accelerated export** — auto-detects NVENC (NVIDIA) → VideoToolbox (Apple) → libx264 (CPU)

## Prerequisites

```bash
winget install FFmpeg          # Windows
pip install -r VLT_Content/AI_ENGINE/yt_tools/requirements_yt.txt
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Example Invocations

```bash
# Basic (silence removal only)
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input "02 HMN_A INPUTS/raw/my_video.mp4" \
  --output ".tmp/edited.mp4" \
  --skip-whisper

# Full pipeline with intro
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input "02 HMN_A INPUTS/raw/my_video.mp4" \
  --output "VLT_Content/04_HMN_OUTPUTS/Jordan/my_video_edited.mp4" \
  --intro "VLT_Content/03_ASSET/Jordan/swivel_teaser.mp4" \
  --trigger-words "ugh,no wait,start over,let me try again"

# Higher accuracy (slower)
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_video_editor.py \
  --input raw.mp4 --output edited.mp4 \
  --whisper-model small
```

## Common Errors

| Error | Fix |
|-------|-----|
| `FFmpeg not found in PATH` | Install FFmpeg and restart terminal |
| `torch not installed` | `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu` |
| `openai-whisper not installed` | `pip install openai-whisper` |
| No segments remain | Loosen `--trigger-words` or use `--skip-whisper` |
| Output is too short | Increase `--min-silence-ms` (e.g. `800`) |

## Notes
- Run from the **Cook/ root directory**.
- Whisper `base` model is fast and accurate enough for clean audio. Use `small` for heavy accents.
- First Silero VAD run downloads a model from torch hub — needs internet once.
