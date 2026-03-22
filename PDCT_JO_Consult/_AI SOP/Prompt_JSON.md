# Prompt 2: Blueprint to Remotion JSON (Technical Version)

**Task:** Act as a Senior Video Editor and Automation Engineer. Convert the following **Unified Content Blueprint** into a frame-accurate Remotion JSON that is compatible with the `ReproductionReel.tsx` component.

**Input Resources:**
1. **The Blueprint:** [Paste Blueprint.md here]
2. **Technical Reference:** Use the schema defined in `VLT_Content/AI_ENGINE/remotion/REMOTION_TECHNICAL_GUIDE.md`.

**JSON Generation Rules:**
1. **Word-by-Word (Type: text):** Break the script into chunks of 1-3 words. Use `type: "text"`.
2. **Transition Markers (Type: notification):** Every time the footage "shifts" (A-Roll to B-Roll), create a `type: "notification"` layer to act as a visual marker.
3. **Animations:** 
   - Use `animation: "slide-up"` for `text`.
   - Use `animation: "pop"` for `notification`.
4. **Progress Bar:** Always include a `type: "progress-bar"` from frame 0 to the end.

**Output Schema (Strict):**
```json
{
  "slug": "reproduction-video",
  "durationInSeconds": [total],
  "layers": [
    {
      "type": "text | progress-bar | notification",
      "content": "string",
      "startFrame": number,
      "endFrame": number,
      "props": {
        "color": "#FFFFFF",
        "position": "center | top | bottom",
        "animation": "slide-up | pop | fade-in"
      }
    }
  ]
}
```
