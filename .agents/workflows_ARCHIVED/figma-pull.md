---
description: How to execute a pull from Figma to grab design node JSON data
---

# 🎨 Figma Sync Workflow (/figma-pull)

This workflow uses the Figma API to pull data from a Figma design file and saves it locally as a JSON document in your `.tmp/` folder. This is useful when you want to feed design context into another agent process or inspect nodes.

## Prerequisites
- Requires `FIGMA_PAT` stored in `C:\Workspace\Cook\.env` (This was set up automatically during integration).

## 🛠️ Step 1: Execute Python Sync Tool

You can pull an entire file or a specific node by running the python tool with the URL or Figma File ID.

```bash
# To pull the entire file
py -3 AI_Tools/figma_sync.py --url "https://www.figma.com/design/FILE_ID/Name"

# To pull a specific node ID (e.g. 1:2)
py -3 AI_Tools/figma_sync.py --url "https://www.figma.com/design/FILE_ID/Name" --node-id "1:2"
```

## 📂 Step 2: Read Output
The tool will output the node tree data to `C:\Workspace\Cook\.tmp\figma_output.json`. You can then read this file to parse style tokens, text content, and layout structure.
