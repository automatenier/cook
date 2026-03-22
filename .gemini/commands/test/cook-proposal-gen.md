> **Model: Sonnet** -- proposal generation requires strategic positioning

# Workflow: Proposal Generation

When user asks to `/proposal-gen [ClientName]`:

1. **Gather Inputs**: Niche, avatar, core pain point, desired outcome, agreed tier, pricing, start date.
2. **Read Framework**: `PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/` for offer structure.
3. **Generate Proposal**:

---
## JO Consult -- Proposal for [ClientName]

### Power Statement
Saya membantu {Avatar} mendapatkan {Hasil} dalam {Timeframe} tanpa {Hal yang Mereka Benci}

### The Problem We're Solving
[1-paragraph: current situation + core pain]

### The Solution -- [Program Name]
**Phase 1:** [Name] -- [Goal] -- Weeks 1-X
**Phase 2:** [Name] -- [Goal] -- Weeks X-Y
**Phase 3:** [Name] -- [Goal] -- Weeks Y-Z

### What's Included
- [ ] Weekly check-ins
- [ ] [Deliverable 1]
- [ ] Direct support via WhatsApp/Telegram

### Investment
| Pay-in-Full | Rp [X] | One payment |
| Installment | Rp [X] | [N]x payments |

### Guarantee
Work Until You Win

### Next Steps
1. Sign agreement  2. Submit onboarding form  3. First session on [Date]
---

4. **Save**: `PDCT_JO_Consult/1_Sales_Pipeline/[ClientName]_proposal_[Date].md`
5. **Remind User**: "Update CRM -- move [ClientName] to 'Proposal Sent'."

```bash
/proposal-gen Fadli
py -3 AI_Tools/cook_offer_agent.py --from-file "PDCT_JO_Consult/2_Product_Pipeline/Onboarding/fadli_onboarding.json" --client-name "Fadli"
```
