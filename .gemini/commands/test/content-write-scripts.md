> **Model: Sonnet** -- script writing requires strategic quality and voice matching

# Workflow: Write Scripts

When user asks to `/write-scripts [ClientName]`:

1. **Read Client Context**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/client_brief.md`
2. **Read Swipe Structures**: `VLT_Content/01_HMN_INPUTS/Swipe Files/` or `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/2_Viral_Formats/`
3. **Read Writing SOPs**: `VLT_Content/AI_BRAIN/Agent Instructions/`
4. **Generate Scripts**: Draft 3 distinct hooks + scripts. Filename: `YYYY-MM-DD_[type]_[slug].md`
5. **Output to Review**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/scripts/`
6. **Automated Review**:
   ```bash
   py -3 AI_Tools/content_review_scripts.py "VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/scripts/[Filename].md"
   ```
7. **Prompt User**: Notify scripts + AI reviews are ready.

```bash
/write-scripts fadli
# Output: VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/projects/2026-03/scripts/2026-03-01_value-cta_diet-consistency.md
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/projects/2026-03/approved/..."
```
