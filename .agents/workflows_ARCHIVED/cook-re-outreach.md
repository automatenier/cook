---
tags:
  - workflow
  - real-estate
---
# RE Outreach Workflow

**Trigger:** User says `"Run RE outreach"` or `"RE setter session"`
**Purpose:** Execute a daily/weekly RE prospecting and follow-up session. Move deals through the pipeline from Prospect → Viewing → Offer → Close.

---

## Inputs Required

| Input | Source |
|-------|--------|
| RE pipeline tracker | `PDCT_Real_Estate/1_Sales_Pipeline/tracker.xlsx` |
| RE prospect notes | `PDCT_Real_Estate/prospects/` |
| Scripts + objection handlers | `PDCT_Real_Estate/scripts/` |
| Market context | `PDCT_Real_Estate/market/` |

---

## Execution Steps

### Step 1 — Load Pipeline State

1. Read `PDCT_Real_Estate/1_Sales_Pipeline/tracker.xlsx` (or ask user to paste current deal summary)
2. Identify:
   - HOT prospects (viewing scheduled, offer pending)
   - WARM prospects (responded, need follow-up)
   - COLD prospects (no response in 3+ days)
   - New leads to contact today

---

### Step 2 — Prioritize Daily Actions

Run actions in this order:

| Priority | Action | Who |
|----------|--------|-----|
| 1 | Follow up HOT leads (offer pending / viewing done) | Jordan |
| 2 | Send viewing confirmations (24h before) | Jordan |
| 3 | Follow up WARM leads (no response 2-3 days) | Jordan |
| 4 | Send 20+ new DMs to cold prospects | Jordan (use script bank) |
| 5 | Add 5-10 new prospects to pipeline | Jordan |

---

### Step 3 — Generate Outreach Messages

For each prospect category, pull the appropriate script:

**New prospect (cold DM):**
- Source: `PDCT_Real_Estate/scripts/cold_dm_scripts.md`
- Personalize: use their name + property interest if known
- Platform: WhatsApp or Instagram DM

**Follow-up (no response 3 days):**
- Source: `PDCT_Real_Estate/scripts/follow_up_scripts.md`
- Rule: max 3 follow-ups per prospect before marking Lost

**Post-viewing follow-up:**
- Send within 2 hours of viewing
- Source: `PDCT_Real_Estate/scripts/post_viewing_scripts.md`
- Include: thank you + answer any questions raised during viewing + soft close

**Objection handling:**
- Source: `PDCT_Real_Estate/properties/[property]/objections.md`
- Match the specific objection raised to the handler

---

### Step 4 — Update Pipeline

After each outreach session:

1. Update `tracker.xlsx`:
   - Stage progression (e.g., Prospect → Initial Contact)
   - Last contact date
   - Notes from conversation
   - Next action + due date

2. Log new leads:
   ```
   py -3 AI_Tools/log_lead.py --name "[Name]" --source "IG Organic" --vertical re --status new
   ```

3. Log completed deals:
   ```
   py -3 AI_Tools/log_revenue.py --client "[Name]" --amount [IDR] --vertical re --type commission
   ```

---

### Step 5 — Weekly Pipeline Review (every Monday)

1. Count by stage: how many at each pipeline stage
2. Identify stalled deals (no movement in 5+ days)
3. Decision: push harder, adjust price/terms, or mark Lost
4. Set weekly targets: viewings booked, offers made
5. Update `PDCT_Real_Estate/prospects/` notes for any new intel

---

## Key Metrics to Track

| Metric | Daily Target | Weekly Target |
|--------|-------------|---------------|
| New DMs sent | 20 | 100 |
| Responses received | 5 | 25 |
| Viewings booked | 1 | 3-5 |
| Offers made | — | 1-2 |
| Deals closed | — | 1/month |

---

## Edge Cases

**Prospect asks price before viewing:**
- Do not send price via DM — book the viewing first
- Script: "Harga tergantung kondisi dan unit. Lebih baik kita lihat langsung — kapan bisa?"

**Prospect ghosts after viewing:**
- Wait 48h → send post-viewing follow-up
- If no response after 3 follow-ups → mark as Cold, reduce outreach to weekly touch

**Multiple prospects for same property:**
- Log all separately in tracker
- Note competition — creates urgency for serious buyers

**Lead from content (IG/TikTok):**
- Log source as "Content" in tracker
- Fast-track to viewing — content-sourced leads are warmer than cold outreach

---

## Output Files

| File | What to update |
|------|---------------|
| `PDCT_Real_Estate/1_Sales_Pipeline/tracker.xlsx` | Stage, last contact, next action |
| `PDCT_JO_Consult/pipeline/lead_attribution.csv` | via `log_lead.py` |
| `PDCT_Real_Estate/prospects/[name].md` | Notes from conversation |
