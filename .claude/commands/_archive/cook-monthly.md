---
tags:
  - claude-config
---
Run the monthly cycle for an active client. Arguments: $ARGUMENTS (client name, optionally month number).

Do not ask for confirmation between steps.

---

**STEP 1 — Read last month's performance**

Check `Z Products/Fulfillment/_CONTENT_AUDIT/client_audits/[nama]/` for latest audit.
Check `VLT_Content/clients/[nama]/projects/` for last month's batch.
Check `A Human Workflow/A Manager/_clients/[nama]_checklist.md` log for Telegram report data.

**STEP 2 — Update swipe file**

Based on performance data:
- Top 3 performing formats/hooks → double down
- 2 underperforming formats → retire or modify
Write update log to `VLT_Content/clients/[nama]/swipe_file_update_[month].md`

**STEP 3 — Generate next month's content batch**

Apply lessons from Step 2. Run same pipeline as `/content [nama] [month]`:
30 reels, 30 stories, 30 threads, 4 YT scripts.
Save to `VLT_Content/clients/[nama]/projects/[new_month]/`

**STEP 4 — Generate consultation call brief**

Write to `Z Products/Fulfillment/_CLIENT_DELIVERABLES/[nama]/consult_brief_[month].md`:
- Performance summary (what worked, what didn't)
- 3 strategic recommendations for next month
- 3 questions to ask the client
- Goals vs actuals from last month
- Suggested goals for next month

**STEP 5 — Meta Ads copy (Month 2+ only)**

If client is Month 2 or later:
- Identify top 2 performing organic reels
- Write 3 ad copy variants per reel: hook + body + CTA
- Output to `Z Products/Fulfillment/_CLIENT_DELIVERABLES/[nama]/ads_[month].md`

**STEP 6 — Reset checklist**

In `A Human Workflow/A Manager/_clients/[nama]_checklist.md`, reset the SIKLUS BULANAN section: uncheck all tasks so they're fresh for this month.

**STEP 7 — Report to Jordan**

Output:
```
Monthly cycle for [NAMA] started.

New content batch: VLT_Content/clients/[nama]/projects/[month]/REVIEW_[month].md (10 min review)
Consultation brief: Z Products/Fulfillment/_CLIENT_DELIVERABLES/[nama]/consult_brief_[month].md

Next Jordan action:
→ Review content batch (10 min)
→ Lead the 1-1 call using the consult brief
```
