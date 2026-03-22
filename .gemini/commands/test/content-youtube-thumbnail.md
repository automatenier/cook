> **Model: Haiku** -- structured thumbnail brief + Gemini Imagen for generation

# Workflow: YouTube Thumbnail Creator

**Trigger:** `/thumbnail [VideoTitle]`

## Inputs

| Input | Description |
|-------|-------------|
| VideoTitle | The confirmed YouTube video title |
| VideoTopic | 1-2 sentence summary |
| TargetEmotion | curiosity / shock / aspiration / FOMO |

## Steps

1. **Validate Inputs** -- confirm all 3. Ask if missing.
2. **Generate 3 Thumbnail Concepts** -- for each:
   - **Text overlay:** [max 5 words]
   - **Visual:** [face expression, background, composition]
   - **Emotion:** [viewer's first feeling]
   - **Why it works:** [1 sentence CTR logic]
   - **Imagen prompt:** [detailed prompt for Gemini Imagen]
3. **Recommend Strongest Concept** -- state which + why.
4. **Save**: `VLT_Content/04_HMN_OUTPUTS/Jordan/thumbnails/[YYYY-MM-DD]_[slug]_thumbnails.md`

## Notes
- Fill in Nanobanana brand context before first real use
- Confirm Gemini CLI has Imagen access before image generation
