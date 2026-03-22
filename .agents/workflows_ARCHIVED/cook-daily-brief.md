---
description: Compiles a structured daily brief from all active verticals.
tags:
  - workflow
---

# Workflow: Daily Brief

When user asks to `/daily-brief`:

1. **Check Inbox**: List unprocessed files in `HMN_A INPUTS/ideas/`, `HMN_A INPUTS/meetings/`. Count items.

2. **Check Content Pipeline**: Scan `VLT_Content/02_WORKSPACE/` for each active client:
   - Any scripts in `/scripts/` awaiting review?
   - Any approved scripts in `/approved/` ready to render?
   - Any outputs in `VLT_Content/04_OUTPUTS/` ready to schedule?

3. **Check JO Consult Pipeline**: Run `py -3 AI_Tools/get_crm_summary.py --limit 5` to get latest status.
   - Active clients with check-in due today
   - Prospects with follow-up overdue

4. **Check Real Estate**: The `get_crm_summary.py` tool also pulls from `PDCT_Real_Estate/1_Sales_Pipeline/tracker.xlsx`.
   - Leads requiring follow-up today
   - Scheduled property viewings

5. **Output Brief** in this format:

---
## Daily Brief — [Date]

### Inbox
- [X] items to triage → run `/inbox-triage`

### Content
- [ClientName]: [status of scripts/renders/outputs]

### JO Consult
- [Client/Prospect]: [action needed]

### Real Estate
- [Lead/Property]: [action needed]

### Today's Priority
1. [Most important action]
2. [Second priority]
3. [Third priority]
---

6. **Save Brief**: Write output to `HMN_A INPUTS/daily_brief/[YYYY-MM-DD]_brief.md`.

## Tool Invocation Examples

```bash
# Trigger this workflow
/daily-brief

# Output location
# HMN_A INPUTS/daily_brief/2026-02-27_brief.md

# Common follow-ups flagged by the brief:
/inbox-triage
/meeting-intelligence [filename]
```
