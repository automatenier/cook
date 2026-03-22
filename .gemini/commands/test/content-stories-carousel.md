> **Model: Haiku** — story sequence and carousel props (mechanical template work)

# Workflow: Render Stories Carousel

When user asks to render a carousel for `[ClientName]`:

1. **Read approved script**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`
2. **Update `defaultProps`** in `VLT_Content/40_ENGINE/remotion/src/Root.tsx` under `StoriesCarousel` -- fill in `slides[]`, `client`, `accentColor`.
3. **Render** (see sections below).
4. **Move output** to `VLT_Content/04_HMN_OUTPUTS/[ClientName]/`.

## Slide Structure

```ts
slides: [
  { type: "hook",    headline: "...", subtext: "..." },
  { type: "content", headline: "...", subtext: "..." },
  { type: "cta",     headline: "...", subtext: "..." },
]
```

Timing: 5s/slide at 30fps. Duration formula: `(n_slides x 150) - ((n_slides - 1) x 20)` frames

## Design Tokens -- theme.ts

File: `VLT_Content/40_ENGINE/remotion/src/theme.ts`

**Option A -- Edit manually**: Update `colors.brand`, `fonts.heading` etc. directly.
**Option B -- Sync from Figma** (requires `FIGMA_TOKEN` + `FIGMA_FILE_ID` in `.env`):
```bash
py -3 AI_Tools/figma_tokens.py
```

## Local Render

```bash
cd VLT_Content/40_ENGINE/remotion
npx remotion studio                                              # Preview
npx remotion render StoriesCarousel out/carousel-[client].mp4   # MP4
npx remotion still StoriesCarousel --frame=75 out/slide-01.png  # PNG frame
```

Frame midpoints (5-slide): slide1=75, 2=205, 3=335, 4=465, 5=595

## Troubleshooting

| Issue | Fix |
|---|---|
| Figma finds 0 styles | Confirm styles are local in Figma (not library) |
| Text overflows | Shorten headline to <8 words. Reduce `theme.fontSizes.hook` |
| Duration mismatch | Recalculate and update `durationInFrames` in `Root.tsx` |
