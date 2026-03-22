---
description: Agent workflow to render Instagram story carousels using the Remotion engine with Figma-synced design tokens.
---

# Workflow: Render Stories Carousel

When user asks to render a carousel for `[ClientName]`:

1. **Read the approved script**: `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`
2. **Update `defaultProps`** in `VLT_Content/40_ENGINE/remotion/src/Root.tsx` under the `StoriesCarousel` composition — fill in `slides[]`, `client`, and `accentColor`.
3. **Render** (see sections below).
4. **Move output** to `VLT_Content/04_OUTPUTS/[ClientName]/`.
5. **Notify user**: deliverable ready at `VLT_Content/04_OUTPUTS/[ClientName]/`.

---

## Slide Structure

Each carousel takes a `slides` array. Max 7 slides recommended for story format.

```ts
slides: [
  {
    type: "hook",        // Big opening — one strong statement
    headline: "...",     // Required. Short, punchy.
    subtext: "...",      // Optional. One supporting line.
  },
  {
    type: "content",     // Point / tip / fact slides
    headline: "...",     // Required.
    subtext: "...",      // Optional. Elaboration or stat.
  },
  {
    type: "cta",         // Closing slide — always last
    headline: "...",     // The ask. e.g. "DM 'SISTEM' sekarang"
    subtext: "...",      // Optional. What they get.
  },
]
```

**Slide timing:** 5 seconds each at 30fps. Total duration auto-calculates based on slide count.

**Duration formula:** `(n_slides × 150) − ((n_slides − 1) × 20)` frames
e.g. 5 slides = 670 frames (~22 seconds)
Update `durationInFrames` in `Root.tsx` if you change slide count.

---

## Design Tokens — theme.ts

All colors, fonts, and sizes come from one file:
`VLT_Content/40_ENGINE/remotion/src/theme.ts`

### Option A — Edit manually (before Figma file exists)
Open `theme.ts` and update `colors.brand`, `fonts.heading`, etc. directly.

### Option B — Sync from Figma (once design file is ready)

**Prerequisites in `.env`:**
```
FIGMA_TOKEN=<personal access token from figma.com/settings>
FIGMA_FILE_ID=<key from Figma URL: figma.com/file/FILE_KEY/...>
```

**Run:**
```bash
py -3 AI_Tools/figma_tokens.py
```

This reads all local color styles and text styles from your Figma file and overwrites `theme.ts`. Remotion picks up changes on next render.

**What gets extracted automatically:**
- Local color styles → `theme.colors`
- Local text styles → `theme.fonts` + `theme.fontSizes`

**What to set manually in `theme.ts` after sync:**
- `theme.spacing` — Figma has no native spacing tokens
- `theme.radius` — same

**Run sync every time you update the Figma style guide.** No need to touch component code.

---

## Render Decision — Local vs Modal

| Scenario | Use |
|---|---|
| **Batch render (2+ carousels)** | Modal — zero local CPU |
| Single test / preview | Local (`npm run build`) |
| Jordan's machine is off / lagging | Modal always |

---

## Local Render (Single)

```bash
cd VLT_Content/40_ENGINE/remotion

# Preview in browser (hot reload)
npx remotion studio

# Render to MP4
npx remotion render StoriesCarousel out/carousel-[client].mp4

# Or via npm script
npm run build
```

Output: `VLT_Content/40_ENGINE/remotion/out/`
Move to: `VLT_Content/04_OUTPUTS/[ClientName]/`

---

## Render as PNG Frames (Static Carousel Export)

To export individual slide images instead of video:

```bash
cd VLT_Content/40_ENGINE/remotion

# Export frame at halfway point of each slide (e.g. slide 1 = frame 75)
npx remotion still StoriesCarousel --frame=75 out/slide-01.png
npx remotion still StoriesCarousel --frame=205 out/slide-02.png
# etc.
```

Frame midpoints per slide (5-slide default):
| Slide | Start frame | Mid frame |
|-------|-------------|-----------|
| 1     | 0           | 75        |
| 2     | 130         | 205       |
| 3     | 260         | 335       |
| 4     | 390         | 465       |
| 5     | 520         | 595       |

---

## Adding a New Client Carousel

1. Add a new `<Composition>` block in `Root.tsx` with a unique `id` (e.g. `StoriesCarousel-Fadli`)
2. Set `accentColor` to client's brand color
3. Fill in `slides[]` from the approved script
4. Render targeting that composition ID:
   ```bash
   npx remotion render StoriesCarousel-Fadli out/fadli-carousel.mp4
   ```

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Figma token extraction finds 0 styles | Confirm styles are **local** (not library). Check in Figma: Assets panel → Local styles |
| Text overflows slide | Shorten headline to <8 words. `theme.fontSizes.hook` can be reduced in `theme.ts` |
| CTA slide text hard to read | CTA slides use `color: #000` on brand background — ensure `accentColor` is light enough |
| Duration mismatch | Recalculate: `(n × 150) − ((n−1) × 20)` and update `durationInFrames` in `Root.tsx` |
