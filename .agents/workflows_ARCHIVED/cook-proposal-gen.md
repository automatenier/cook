---
description: Generates a proposal and SOW for a JO Consult client.
tags:
  - workflow
---

# Workflow: Proposal Generation

When user asks to `/proposal-gen [ClientName]`:

1. **Gather Inputs**: Ask user for (or locate from existing files):
   - Client's business niche and avatar
   - Core pain point they came to solve
   - Desired outcome / transformation
   - Agreed tier (Bedah Digital / AI & Scale) and pricing
   - Start date and duration

2. **Read Framework**: Reference `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_OFFER_BLUEPRINT/high_ticket_offer_framework.md` for power statement and mechanism structure.

3. **Generate Proposal** using this structure:

---
## JO Consult — Proposal for [ClientName]

### Power Statement
[Saya membantu {Avatar} mendapatkan {Hasil} dalam {Timeframe} tanpa {Hal yang Mereka Benci}]

### The Problem We're Solving
[1-paragraph summary of their current situation and core pain]

### The Solution — [Program Name]
**Phase 1:** [Name] — [Goal] — Weeks 1–X
**Phase 2:** [Name] — [Goal] — Weeks X–Y
**Phase 3:** [Name] — [Goal] — Weeks Y–Z

### What's Included
- [ ] Weekly check-ins
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] Direct support via WhatsApp/Telegram

### Investment
| Option | Price | Structure |
|---|---|---|
| Pay-in-Full | Rp [X] | One payment, save Rp [Y] |
| Installment | Rp [X] | [N]x payments |

### Guarantee
[Work Until You Win — or customize per client]

### Next Steps
1. Sign agreement
2. Submit onboarding form
3. First session on [Date]
---

4. **Save Proposal**: Write to `PDCT_JO_Consult/deliverables/[ClientName]/proposal_[Date].md`.

5. **Remind User**: "Update `PDCT_JO_Consult/1_Sales_Pipeline/JO_Consult_CRM.xlsx` — move [ClientName] to 'Proposal Sent' stage."

## Tool Invocation Examples

```bash
# Trigger this workflow
/proposal-gen Fadli

# Output location
# PDCT_JO_Consult/deliverables/Fadli/proposal_2026-02-27.md

# Common follow-up: generate offer sheet once client signs
py -3 AI_Tools/cook_offer_agent.py --from-file "PDCT_JO_Consult/clients/Fadli/onboarding.json" --client-name "Fadli"
```
