---
name: notebooklm
description: Access Google NotebookLM features programmatically. Research sources, generate podcasts, PPTX, and more.
---

# NotebookLM

This skill provides an interface to the `notebooklm-py` library.

## Workflow

1. **Login**: First-time users must authenticate.
   ```bash
   py -3 -m notebooklm login
   ```
2. **Research**: Use the CLI to query or import.
   ```bash
   py -3 -m notebooklm ask --notebook <ID> "Your question"
   ```

## Key Commands

- `notebooklm list`: List your notebooks.
- `notebooklm create <name>`: Create a new notebook.
- `notebooklm import <notebook_id> <url_or_file>`: Add sources.
- `notebooklm generate <notebook_id> audio`: Create a podcast.
- `notebooklm generate <notebook_id> slides`: Create a PPTX.
