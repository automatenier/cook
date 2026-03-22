> **Model: Sonnet** -- discovery call prep requires strategic reasoning

# Workflow: Discovery Call Prep

When user asks to `/disco-prep [ProspectName]`:

1. **Locate Prospect Data**: `PDCT_JO_Consult/pipeline/` for existing notes. Ask user to paste CRM row if needed.
2. **Read Offer Context**: `AI_BRAIN/context/` for JO Consult tiers and positioning.
3. **Build the Brief**:

---
## Discovery Call Brief -- [ProspectName] -- [Date]

### Who They Are
- Business/niche: | Current situation: | Where they found you:

### Pain Points to Probe (3-5)
### Dream Outcome to Surface
### Offer Match
- Recommended tier: [Bedah Digital / AI & Scale]
- Why this tier fits: | Price anchor:

### Key Questions to Ask
1.  2.  3.  4.  5.

### Objections to Prepare For
| Too expensive | Need to think | Not the right time |

### Call Goal
[ ] Qualify -> book follow-up  [ ] Close on the call
---

4. **Save**: `PDCT_JO_Consult/pipeline/[ProspectName]_disco_[Date].md`
5. **Prompt User**: "Brief saved. After the call, run `/meeting-intelligence [ProspectName]`."

```bash
/disco-prep Ahmad
/meeting-intelligence Ahmad_2026-03-03
/proposal-gen Ahmad
```
