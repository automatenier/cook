---
name: source-analyst
description: Analyze multiple sources (PPTX, MD, PDF) to generate summaries, briefs, and insights. Inspired by NotebookLM. Use to "ingest" project files before creating new content.
---

# Source Analyst

Analyze project files to extract key information and synthesize it into actionable insights.

## Workflow

1.  **Ingest**: Read text from files (e.g., `read_pptx.py` for presentations).
2.  **Analyze**: Look for patterns, key data points, and themes.
3.  **Synthesize**: Create a "Brief" or "Source Note" to guide content creation.

## Tools

### Read PPTX Content

```bash
py -3 skills/source-analyst/scripts/read_pptx.py <path_to_pptx>
```
