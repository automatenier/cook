---
description: Generates titles, descriptions, hashtags, and thumbnail brief for a content piece.
tags:
  - workflow
---

# Workflow: Generate Metadata

When user asks to `/generate-metadata [ClientName] [ScriptRef]`:

1. **Read Approved Script**: Open `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef].md`.

2. **Read Client Context**: Check `VLT_Content/02_WORKSPACE/[ClientName]/client_brief.md` for niche, avatar, and platform targets.

3. **Generate Metadata Package**:

---
## Metadata Package — [ClientName] — [ScriptRef]

### Hook Variants (for A/B testing)
1. [Title option 1 — curiosity-driven]
2. [Title option 2 — result-driven]
3. [Title option 3 — controversy/pattern interrupt]

### Caption (Instagram / TikTok)
[Hook line]

[2-3 lines of body — expand on the hook, don't reveal everything]

[CTA — follow, comment, save, DM]

### Hashtags
**Niche:** #[x5]
**Broad:** #[x5]
**Location (if relevant):** #[x3]

### YouTube Description (if applicable)
[2-3 sentence description with keywords]

### Thumbnail Brief
- **Text overlay:** [exact words on thumbnail]
- **Visual concept:** [what should be shown]
- **Emotion to convey:** [curiosity / shock / aspiration]

### End Screen / Cards (YouTube)
- Suggest video: [topic that naturally follows]
---

4. **Save**: Write to `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/approved/[ScriptRef]_metadata.md`.

## Tool Invocation Examples

```bash
# Trigger this workflow
/generate-metadata fadli reel_01

# Output location
# VLT_Content/02_WORKSPACE/fadli/projects/2026-02/approved/reel_01_metadata.md

# Common follow-up: repurpose the approved script across platforms
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_WORKSPACE/fadli/projects/2026-02/approved/reel_01.md"
```
