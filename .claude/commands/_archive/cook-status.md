---
description: Give a complete status briefing for a client.
tags:
  - claude-config
---
> **Model: Sonnet** -- synthesizing status across multiple sources requires judgment

Give a complete status briefing for a client. Arguments: $ARGUMENTS (client name).

Read these files:
1. `PDCT_JO_Consult/clients/[nama]/worksheet.md` -- find CURRENT STATE table
2. `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/projects/` -- check latest month scripts/approved
3. `PDCT_JO_Consult/deliverables/[nama]/` -- check what deliverables exist
4. `01 HMN__Command/00_COOK/agent_log.csv` -- check recent agent actions for this client

Output:

---
## Status: [NAMA] -- [today's date]

**Phase:** [current phase]
**Day in sprint:** [X/14]
**On track / Behind / Blocked:** [assessment]

### Completed
[bullet list, grouped by phase]

### In Progress
[what's actively being worked on]

### Next 3 Actions
1. [Most urgent -- who does it]
2. [Second]
3. [Third]

### Blocked / Needs Jordan
[anything requiring Jordan's input or physical action]

### Content Pipeline
- Scripts: [X in review / Y approved / Z rendered]
- Last published: [date]
---
