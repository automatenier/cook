---
description: Read Gemini video transcriptions from a CSV and rewrite them using brand tone for Remotion reels.
---

# Workflow: Reel Rewriting from CSV

When the user asks to `/reel-rewrite-csv [CSV Path] [ClientName]`:

1. **Read CSV**: Parse the CSV containing Gemini-web transcriptions. The CSV should have columns like `Video Reference`, `VLT_Content/Transcription`.
2. **Rewrite Script**: Read `VLT_Content/00_SYSTEM/agent_prompt.md` (or client specific brand voice guidelines) to apply the brand tone.
3. **Generate Assets**: For each rewritten script, generate a structured markdown file with hook, core message, and call-to-action to `VLT_Content/02_WORKSPACE/[ClientName]/projects/[YYYY-MM]/scripts/`.
4. **Update Canvas (Optional)**: If working with `VLT_Content/Canvas.canvas`, update the corresponding text nodes to reflect the new, repurposed script.
5. **Render (Optional)**: Trigger the `/render-simple-reel` workflow using the newly minted scripts.

## Tool Invocation Examples

```bash
# Trigger this workflow
/reel-rewrite-csv .tmp/transcriptions.csv fadli
```
