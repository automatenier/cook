---
description: Routes everything in HMN_A INPUTS to the correct vertical folder.
tags:
  - workflow
---

# Workflow: Inbox Triage

When user asks to `/inbox-triage`:

1. **Scan Inbox**: List all files in `HMN_A INPUTS/ideas/`, `HMN_A INPUTS/meetings/`, and `HMN_A INPUTS/daily_brief/`.

2. **Classify Each Item** using this routing logic:

   | Item Type | Route To |
   |---|---|
   | Call transcript / meeting notes | `HMN_A INPUTS/meetings/` → process with `/meeting-intelligence` |
   | Content idea (reel, post, hook) | `VLT_Content/HMN_A INPUTS/Jordan/` |
   | Consulting lead / prospect note | `PDCT_JO_Consult/pipeline/` |
   | Real estate prospect / property note | `PDCT_Real_Estate/prospects/` or `PDCT_Real_Estate/properties/` |
   | Course / education idea | `11_JO_Ed/courses/` |
   | Product / feature idea | `12_JO_Ventures/features/` |
   | Unclassifiable | Leave in place, flag for user |

3. **Move Files**: Relocate each file to its destination folder with a date prefix (`YYYY-MM-DD_filename.md`).

4. **Flag Meetings**: For any transcript in `HMN_A INPUTS/meetings/`, prompt user: "Run `/meeting-intelligence [filename]` to extract action items."

5. **Summary Report**: Output a short list of what was moved where. Keep it under 10 lines.

## Tool Invocation Examples

```bash
# Trigger this workflow
/inbox-triage

# Common follow-ups (agent will prompt these):
/meeting-intelligence 2026-02-27_call_Ahmad
py -3 AI_Tools/content_capture_idea.py "Idea from inbox item"
```
