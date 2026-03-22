# NotebookLM Integration Demo (JO Consult)

This document demonstrates how to use the `notebooklm-py` library within the **JO Consult** workflow for automated research and content generation.

## 1. Quick Status Check
Verify your connection and active notebooks:
```bash
py -3 -m notebooklm list
```

## 2. Research & Analysis
Ask questions directly to your "AI" notebook (ID: `6ada...`):
```bash
py -3 -m notebooklm ask --notebook 6ada "Summarize the core offer in this notebook."
```

## 3. Automated Source Ingestion
Add new research materials (URLs, PDFs, or YouTube videos) to your notebook:
```bash
py -3 -m notebooklm source add 6ada "https://github.com/teng-lin/notebooklm-py"
```

## 4. Content Generation (Beyond the Web UI)
Generate advanced artifacts directly from your sources:

### Deep Research & Insights
```bash
py -3 -m notebooklm generate 6ada report
```

### Audio Overviews (Podcasts)
```bash
py -3 -m notebooklm generate 6ada audio
```

### Editable Slide Decks (PPTX)
Unlike the web UI (PDF only), this tool exports editable PowerPoint files:
```bash
py -3 -m notebooklm download 6ada slide-deck
```

### Knowledge Base Tools
```bash
py -3 -m notebooklm generate 6ada quiz
py -3 -m notebooklm generate 6ada flashcards
```

---
*Note: Ensure you are logged in via `py -3 -m notebooklm login` before running these commands.*
