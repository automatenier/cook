---
description: Granular approval and moving of scripts from review to approved.
tags:
  - workflow
---

# Workflow: Approve Scripts

When user asks to `/approve [client]` or `/approve [filename]`:

1. **Identify Source**: Scan `VLT_Content/02_WORKSPACE/` for the specified client or file.
   - If `[client]` is provided: Find all `.md` files in `VLT_Content/02_WORKSPACE/[client]/projects/[YYYY-MM]/scripts/`.
   - If `[filename]` is provided: Search for that specific file across all client script folders.

2. **Validate Readiness (Optional)**: 
   - Check if a corresponding review exists in `VLT_Content/03_REVIEW/scripts_reviewed/`.
   - If no review exists, ask: "This script hasn't been AI-reviewed. Run `/review [filename]` first?"

3. **Execute Move**:
   - Move approved scripts from the `/scripts/` folder to the `/approved/` folder in the same project directory.
   - Update the filename prefix to `APPROVED_[YYYY-MM-DD]_` for clarity if requested.

4. **Log Action**: Use `cook_logger.py` to record the approval.

## Tool Invocation Examples

```bash
# Approve all pending scripts for a client
/approve fadli

# Approve a specific script
/approve 20260228_Cikarang_Tokyo.md
```
