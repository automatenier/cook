> **Model: Haiku** — tool runner, mechanical execution

# Figma Sync Workflow (/figma-pull)

This workflow uses the Figma API to pull data from a Figma design file and saves it locally as a JSON document in your `.tmp/` folder.

## Prerequisites
- Requires `FIGMA_PAT` stored in `.env`

## Step 1: Execute Python Sync Tool

```bash
# Pull the entire file
py -3 AI_Tools/content_figma_manager.py --url "https://www.figma.com/design/FILE_ID/Name"

# Pull a specific node ID (e.g. 1:2)
py -3 AI_Tools/content_figma_manager.py --url "https://www.figma.com/design/FILE_ID/Name" --node-id "1:2"
```

## Step 2: Read Output
The tool outputs the node tree data to `.tmp/figma_output.json`. Read this file to parse style tokens, text content, and layout structure.

## Step 3: Sync Design Tokens to Remotion (optional)

If pulling tokens for a client carousel:
```bash
py -3 AI_Tools/figma_tokens.py
```
This reads all local color styles and text styles from your Figma file and overwrites `VLT_Content/40_ENGINE/remotion/src/theme.ts`.
Run every time you update the Figma style guide.
