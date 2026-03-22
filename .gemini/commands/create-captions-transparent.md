# /create-captions-transparent

Generate "real" transparent captions (WebM) for any audio file.

## Usage
`/create-captions-transparent "path/to/audio.mp3"`

## Workflow
1. **Transcribe:** Whisper `base` model.
2. **Convert:** Groups into high-retention phrases.
3. **Render (Transparent WebM):**

## ⚠️ Transparency — All 3 requirements must be met or the background stays black

| # | What | Why |
|---|------|-----|
| 1 | `props["transparent"] = True` in props.json | Tells the React component to render `backgroundColor: transparent` instead of `#111`. Missing this = black background regardless of codec. |
| 2 | `--codec vp8` (not h265, not mp4) | Only VP8/VP9 support alpha channels. h265 does not. Output must be `.webm`. |
| 3 | `--image-format png` + `--pixel-format yuva420p` | PNG preserves alpha per frame; `yuva420p` adds the alpha plane to the encoded video. |

## Script
Executed via `py -3 AI_Tools/create_captions_transparent.py "{{path}}"`
