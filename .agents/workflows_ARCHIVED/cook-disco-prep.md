---
description: Prepares a structured discovery call brief for a JO Consult prospect.
tags:
  - workflow
---

# Workflow: Discovery Call Prep

When user asks to `/disco-prep [ProspectName]`:

1. **Locate Prospect Data**: Check `PDCT_JO_Consult/pipeline/` for any existing notes on [ProspectName]. Also check `PDCT_JO_Consult/1_Sales_Pipeline/JO_Consult_CRM.xlsx` for their row (ask user to paste if needed).

2. **Read Offer Context**: Read `AI_BRAIN/context/` for current JO Consult tiers and positioning. Reference `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_OFFER_BLUEPRINT/high_ticket_offer_framework.md` for offer details.

3. **Build the Brief** with these sections:

---
## Discovery Call Brief — [ProspectName] — [Date]

### Who They Are
- Business/niche:
- Current situation (what they told you):
- Where they found you:

### Pain Points to Probe
(Based on their niche — list 3-5 likely pain points to confirm on the call)

### Dream Outcome to Surface
(What result would make this call a 10/10 for them?)

### Offer Match
- Recommended tier: [Bedah Digital / AI & Scale]
- Why this tier fits:
- Price anchor to use:

### Key Questions to Ask
1.
2.
3.
4.
5.

### Objections to Prepare For
| Objection | Response |
|---|---|
| Too expensive | |
| Need to think about it | |
| Not the right time | |

### Call Goal
[ ] Qualify → book follow-up
[ ] Close on the call
---

4. **Save Brief**: Write to `PDCT_JO_Consult/pipeline/[ProspectName]_disco_[Date].md`.

5. **Prompt User**: "Brief saved. Open it before the call. After the call, run `/meeting-intelligence [ProspectName]` to log the outcome."

## Tool Invocation Examples

```bash
# Trigger this workflow
/disco-prep Ahmad

# Output location
# PDCT_JO_Consult/pipeline/Ahmad_disco_2026-02-27.md

# After the discovery call, log the outcome
/meeting-intelligence Ahmad_2026-02-27

# If they close on the call, next step
/proposal-gen Ahmad
```
