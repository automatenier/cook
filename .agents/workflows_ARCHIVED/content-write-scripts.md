---
description: Agent workflow to draft scripts based on a client brief and latest swipe files.
---

# Workflow: Write Scripts

When user asks to `/write-scripts [ClientName]`:

1. **Read Client Context**: Open `VLT_Content/02_WORKSPACE/jocons/[ClientName]/client_brief.md`. Understand their niche, offer, avatar, and tone of voice.
2. **Read Swipe Structures**: Read recent files in `HMN_A INPUTS/Swipe Files/` or `VLT_Content/02_WORKSPACE/jocons/[ClientName]/2_Viral_Formats/`.
3. **Read Writing SOPs**: Read rules from `VLT_Content/00_SYSTEM/A Human Instruction/Content 1.md` (Viral Scripting) and `Content 2.md` (Idea Generation). Check `VLT_Content/00_SYSTEM/Agent Instructions/` for specific prompt structures.
4. **Generate Scripts**: Draft 3 distinct hooks + scripts resolving the client's audience pain points using the naming convention `YYYY-MM-DD_[type]_[slug].md`.
5. **Output to Review**: Save scripts to `VLT_Content/02_WORKSPACE/jocons/[ClientName]/projects/[YYYY-MM]/scripts/`.
6. **Automated Review**: Run the review tool for each generated script:
   ```bash
   py -3 AI_Tools/content_review_scripts.py "VLT_Content/02_WORKSPACE/jocons/[ClientName]/projects/[YYYY-MM]/scripts/[Filename].md"
   ```
7. **Prompt User**: Notify the user that the scripts and their AI reviews are ready for review in the client's project folder.

## Tool Invocation Examples

```bash
# Trigger this workflow
/write-scripts fadli

# Output location example
# VLT_Content/02_WORKSPACE/jocons/fadli/projects/2026-03/scripts/2026-03-01_value-cta_diet-consistency.md

# After scripts are approved, repurpose a finished script
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_WORKSPACE/jocons/fadli/projects/2026-03/approved/2026-03-01_value-cta_diet-consistency.md"
```
