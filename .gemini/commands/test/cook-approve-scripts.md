> **Model: Sonnet** -- reviewing script quality before production

# Workflow: Approve Scripts

When user asks to `/approve [client]` or `/approve [filename]`:

1. **Identify Source**: `VLT_Content/02_HMN_HUMANFLOW/jocons/[client]/projects/[YYYY-MM]/scripts/`
2. **Validate Readiness**: Check if AI review exists. If not: "Run the review tool first?"
3. **Execute Move**: Move from `/scripts/` to `/approved/` in the same project directory.
4. **Log Action**: `py -3 AI_Tools/cook_logger.py`

```bash
/approve fadli
/approve 2026-03-01_value-cta_diet-consistency.md
```
