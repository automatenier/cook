# /create-captions

Generate "frame-perfect" captions for any audio file using Whisper transcription and Remotion rendering.

## Usage
`/create-captions "path/to/audio.mp3"`

## Workflow
1. **Transcribe:** Uses Whisper `base` model with word-level timestamps.
2. **Convert:** Groups words into 1-3 word high-retention phrases.
3. **Render (Transparent WebM):** Renders a `.webm` with a real alpha channel.

## ⚠️ Transparency — All 3 requirements must be met or the background stays black

| # | What | Why |
|---|------|-----|
| 1 | `props["transparent"] = True` in props.json | Tells the React component to render `backgroundColor: transparent` instead of `#111`. Missing this = black background regardless of codec. |
| 2 | `--codec vp8` (not h265, not mp4) | Only VP8/VP9 support alpha channels. h265 does not. Output must be `.webm`. |
| 3 | `--image-format png` + `--pixel-format yuva420p` | PNG preserves alpha per frame; `yuva420p` adds the alpha plane to the encoded video. |

## Script
Executed via `py -3 AI_Tools/create_captions.py "{{path}}"`
