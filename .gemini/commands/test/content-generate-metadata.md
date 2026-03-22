> **Model: Haiku** — template-based caption and hashtag generation

# Workflow: Generate Metadata

When user asks to `/generate-metadata [ClientName] [ScriptRef]`:

1. **Read Approved Script**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`
2. **Read Client Context**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/client_brief.md`
3. **Generate Metadata Package**:

---
## Metadata Package -- [ClientName] -- [ScriptRef]

### Hook Variants (A/B testing)
1. [Title - curiosity-driven]
2. [Title - result-driven]
3. [Title - controversy/pattern interrupt]

### Caption (Instagram / TikTok)
[Hook line]
[2-3 lines of body]
[CTA - follow, comment, save, DM]

### Hashtags
**Niche:** #[x5] | **Broad:** #[x5] | **Location:** #[x3]

### YouTube Description
[2-3 sentence description with keywords]

### Thumbnail Brief
- **Text overlay:** [exact words]
- **Visual concept:** [what to show]
- **Emotion:** [curiosity / shock / aspiration]
---

4. **Save**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef]_metadata.md`

```bash
/generate-metadata fadli reel_01
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/projects/2026-03/approved/reel_01.md"
```
