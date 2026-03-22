# /image-text-overlay

> **Model: Haiku** — Mechanical image processing, no deep reasoning needed.

## Usage
```
/image-text-overlay <image_path> | <title> | <item1>, <item2>, ...
```

**Example:**
```
/image-text-overlay C:\Users\natha\...\photo.JPG | Calon Menantu Idaman | Polisi, Tentara, Dokter, Pilot, Taruna
```

## What it does
Overlays centered white text with black outline onto a photo, using the standard Jordan text style:
- **Font:** Arial Regular (thin/light)
- **Title:** 68px, centered, white with 3px black stroke
- **List:** 60px, centered, white with 3px black stroke, auto-numbered
- **Spacing:** 80px gap between title and list, 16px between list items
- **Output:** Saves as `[original_name]_text.JPG` in the same folder as the source image (or specify output path)

## SOP

**Step 1 — Parse arguments**
Split `$ARGUMENTS` by ` | `:
- `[0]` = image path
- `[1]` = title text
- `[2]` = comma-separated list items (strip whitespace, auto-number them)

If no output path given, output to same folder as input with `_text` suffix.

**Step 2 — Run the overlay script inline**

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.open(IMAGE_PATH)
draw = ImageDraw.Draw(img)
w, h = img.size

font_path = r"C:\Windows\Fonts\arial.ttf"
title_font = ImageFont.truetype(font_path, 68)
list_font = ImageFont.truetype(font_path, 60)

def draw_outlined_text_center(draw, y, text, font, img_width, fill="white", outline="black", stroke_width=3):
    bbox = font.getbbox(text)
    text_w = bbox[2] - bbox[0]
    x = (img_width - text_w) // 2
    for dx in range(-stroke_width, stroke_width + 1):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline)
    draw.text((x, y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]

y = 25

# Title
th = draw_outlined_text_center(draw, y, TITLE, title_font, w, stroke_width=3)
y += th + 80  # Gap between title and list

# Numbered list
for i, item in enumerate(ITEMS, 1):
    lh = draw_outlined_text_center(draw, y, f"{i}. {item}", list_font, w, stroke_width=3)
    y += lh + 16

img.save(OUTPUT_PATH, quality=95)
```

**Step 3 — Confirm**
Show the output image to the user and confirm the save path.

## Style Reference
This is the "Jordan meme text" style — thin white centered text, light black outline. Used for viral hook images.
