---
description: Audit Instagram funnel for a high-ticket consulting client -- identify bottlenecks across content, DMs, and sales.
tags:
  - claude-config
---
> **Model: Sonnet** -- pattern recognition across multi-source data requires judgment

Audit the Instagram sales funnel for a high-ticket consulting client. Arguments: $ARGUMENTS (client name + any pasted data).

## How to use
Run as: `/cook-audit [Client] [paste data inline or reference file path]`

Accepted inputs (paste any combination):
- Instagram Insights numbers (reach, profile visits, story views, reel plays, follower growth)
- DM sequence copy (the messages you send after someone engages)
- Sample DM conversation threads (anonymized ok)
- Sales call notes or close rate data (even ballpark numbers)
- Offer name + price point

If data is in a file, read it. If pasted inline, use as-is. If missing, ask only for what's needed to diagnose the most likely bottleneck -- don't ask for everything upfront.

## Analysis Steps

**Step 1 -- Build the funnel map**
Extract or estimate these numbers from the data provided:
```
Content Reach → Profile Visits → DM Initiated → Qualified → Call Booked → Closed
      ?      →       ?        →      ?        →     ?     →      ?      →    ?
```
Calculate conversion % at each stage. Flag any stage below benchmark:
- Reach → Profile Visit: <3% is weak
- Profile Visit → DM: <5% is weak
- DM Initiated → Qualified: <30% is weak
- Qualified → Call Booked: <50% is weak
- Call Booked → Closed: <20% is weak (high ticket)

**Step 2 -- Content audit (top of funnel)**
Look at content metrics and DM sequence triggers. Identify:
- Is reach growing or flat? What content type drives the most profile visits?
- Are reels/carousels attracting the right ICP or vanity audience?
- Does the content CTA match the DM sequence entry point?

**Step 3 -- DM sequence audit (mid funnel)**
Read the DM sequence copy. Identify:
- Which message in the sequence has the highest drop-off?
- Is the opener too salesy, too vague, or not qualifying fast enough?
- Is there a clear transition from rapport → qualification → call invite?
- Are objections (price, time, "I'll think about it") handled in the sequence?

**Step 4 -- Sales conversion audit (bottom funnel)**
From call notes or close rate data. Identify:
- Is the low close rate from price objections, trust gaps, or offer clarity?
- Are no-shows high? (booking → show rate below 60% = follow-up problem)
- Is the offer positioned as a transformation or a service?

**Step 5 -- Root cause ranking**
Rank bottlenecks by revenue leverage (biggest leak first):
1. [Highest leverage fix]
2. [Second]
3. [Third]

## Output Format

---
## Funnel Audit: [Client] -- [today's date]

### Funnel Map
| Stage | # or % | Benchmark | Status |
|-------|---------|-----------|--------|
| Reach → Profile Visit | | 3%+ | |
| Profile Visit → DM | | 5%+ | |
| DM → Qualified | | 30%+ | |
| Qualified → Call | | 50%+ | |
| Call → Closed | | 20%+ | |

### Top Bottleneck
**Where the biggest leak is:** [stage]
**Root cause:** [1-2 sentences, specific]

### Diagnosis by Layer

**Content (Top of Funnel)**
[What's working / what's not / specific fix]

**DM Sequence (Mid Funnel)**
[Drop-off point / rewrite recommendation for that specific message]

**Sales Conversion (Bottom Funnel)**
[Close rate issue + specific reframe or fix]

### Priority Fixes (ranked by revenue impact)
1. **[Fix 1]** -- [what to change, how to change it]
2. **[Fix 2]** -- [what to change, how to change it]
3. **[Fix 3]** -- [what to change, how to change it]

### Rewrites (if applicable)
[If DM copy was provided, include a rewritten version of the drop-off message here]

---

After output: "Paste the next data layer (DMs, call notes, content metrics) and I'll go deeper on whichever bottleneck is highest priority."
