---
description: Processes a call transcript into structured action items and client notes.
tags:
  - workflow
---

# Workflow: Meeting Intelligence

When user asks to `/meeting-intelligence [filename or ClientName]`:

1. **Locate Transcript**: Find the file in `HMN_A INPUTS/meetings/[filename].md` or ask user to paste the transcript.

2. **Extract Structure**: Parse the transcript and extract:
   - **Meeting Type**: Discovery / Check-in / Sales call / Internal / Real estate viewing
   - **Date & Participants**
   - **Key Decisions Made**
   - **Pain Points Mentioned** (direct quotes preferred)
   - **Action Items** — with owner and deadline if stated
   - **Follow-up Required**: Yes/No + what

3. **Route Output** based on meeting type:

   | Meeting Type | Output Location |
   |---|---|
   | JO Consult client | `PDCT_JO_Consult/clients/[ClientName]/meeting_[Date].md` |
   | Sales / discovery call | `PDCT_JO_Consult/pipeline/[ProspectName]_[Date].md` |
   | Real estate prospect | `PDCT_Real_Estate/prospects/[Name]_[Date].md` |
   | Real estate property tour | `PDCT_Real_Estate/properties/[Property]_notes.md` |
   | Internal / personal | `HMN_A INPUTS/ideas/[Date]_meeting_notes.md` |

4. **Update CRM** (remind user): "Add action items to `PDCT_JO_Consult/1_Sales_Pipeline/JO_Consult_CRM.xlsx` or `PDCT_Real_Estate/1_Sales_Pipeline/tracker.xlsx` manually."

5. **Archive Transcript**: Move original from `HMN_A INPUTS/meetings/` to `VLT_Content/05_ARCHIVE/meetings/[filename].md`.

## Tool Invocation Examples

```bash
# Trigger with a specific filename
/meeting-intelligence Fadli_2026-02-21

# Trigger with client name (agent searches HMN_A INPUTS/meetings/)
/meeting-intelligence Fadli

# Output locations by meeting type:
# JO Consult client   → PDCT_JO_Consult/clients/Fadli/meeting_2026-02-21.md
# Discovery call      → PDCT_JO_Consult/pipeline/Fadli_2026-02-21.md
# Real estate         → PDCT_Real_Estate/prospects/Ahmad_2026-02-21.md
# Internal            → HMN_A INPUTS/ideas/2026-02-21_meeting_notes.md
```
