# /video-text-overlay

> **Model: Haiku** — Mechanical video processing, no deep reasoning needed.

## Usage
```
/video-text-overlay <video_path> | <text>
```

**Example:**
```
/video-text-overlay C:\Users\natha\...\clip.mov | 6. Sales
```

## What it does
Burns centered white text with black outline onto a video, always placed in the exact center of the frame.

- **Font:** Arial Regular (thin/light)
- **Size:** 60px
- **Color:** White with 3px black stroke
- **Position:** Horizontally + vertically centered `(w-text_w)/2 : (h-text_h)/2`
- **Audio:** Preserved as-is
- **Output:** Saves as `[original_name]_text.mov` in the same folder as the source video

## SOP

**Step 1 — Parse arguments**
Split `$ARGUMENTS` by ` | `:
- `[0]` = video path
- `[1]` = text to overlay

Derive output path: same folder as input, filename + `_text` suffix, same extension.

**Step 2 — Run FFmpeg**

```bash
ffmpeg -i "INPUT_PATH" \
  -vf "drawtext=fontfile='C\\:/Windows/Fonts/arial.ttf':text='TEXT':fontsize=60:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=(h-text_h)/2" \
  -codec:a copy \
  "OUTPUT_PATH" -y
```

**Step 3 — Confirm**
Tell the user the output path. Done.

## Notes
- FFmpeg must be installed and on PATH (already confirmed working)
- If text contains special characters like `'`, escape them with `\'`
- For multi-line text, use `\n` in the text string and add `:line_spacing=10`
