---
description: Generates YouTube thumbnail concepts and image prompts for Jordan's personal channel using the Nanobanana brand voice.
tags:
  - workflow
  - youtube
---

# Workflow: YouTube Thumbnail Creator

**Agent:** Gemini CLI
**Trigger:** `/thumbnail [VideoTitle]`

---

## Inputs Required

| Input | Description |
|-------|-------------|
| `VideoTitle` | The confirmed YouTube video title |
| `VideoTopic` | 1-2 sentence summary of what the video covers |
| `TargetEmotion` | What should the viewer feel when they see the thumbnail? (curiosity / shock / aspiration / fear of missing out) |

---

## Nanobanana Brand Context

<!-- TODO: Fill in Jordan's personal brand voice, visual style, colors, and face/character style used in thumbnails -->

**Brand persona:** [FILL IN — who is Jordan on YouTube? Energy, tone, aesthetic]
**Visual style:** [FILL IN — e.g., bold text, dark background, face-forward, meme format, etc.]
**Color palette:** [FILL IN — primary and accent colors]
**Font style:** [FILL IN — e.g., chunky sans-serif, handwritten, etc.]
**Nanobanana Gem prompt:** [FILL IN — paste the Nanobanana system prompt / Gem instructions here]

---

## Steps

### 1. Validate Inputs
Confirm you have `VideoTitle`, `VideoTopic`, and `TargetEmotion` before proceeding.
If missing, ask the user for them before continuing.

### 2. Load Brand Context
Read the Nanobanana brand context above.
<!-- TODO: If Nanobanana Gem has a separate file, load it here -->

### 3. Generate 3 Thumbnail Concepts

For each concept, output the following structure:

---
**Concept [N]**
- **Text overlay:** [Exact words — max 5 words. Should create a click on its own.]
- **Visual:** [What is shown in the image — face expression, background, object, composition]
- **Emotion:** [What the viewer feels at first glance]
- **Why it works:** [1 sentence — hook logic]
- **Imagen prompt:** [Detailed prompt to generate this image with Gemini Imagen]
---

### 4. Recommend the Strongest Concept
State which concept to use and why (CTR logic — which headline + visual combination is most likely to stop a scroll).

### 5. Save Output

Write the full output to:
```
HMN_A Human/youtube/thumbnails/[YYYY-MM-DD]_[VideoTitle-slug]_thumbnails.md
```

<!-- TODO: Confirm the correct output folder for Jordan's YouTube content once structure is finalized -->

---

## Example Invocation

```
/thumbnail "I Tried Building a Business in 30 Days"
Topic: Jordan documents his 30-day sprint to close his first paying client.
Emotion: curiosity + aspiration
```

---

## Notes / Learnings

<!-- Add any edge cases, Gemini Imagen quirks, or brand refinements here as you use this workflow -->

- [ ] Confirm Gemini CLI has Imagen access before running image generation step
- [ ] Fill in Nanobanana brand context before first real use
- [ ] Decide if thumbnails go in `HMN_A Human/youtube/` or a client-style workspace folder
