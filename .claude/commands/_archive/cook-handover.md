---
tags:
  - claude-config
---
Prepare the Day-14 handover call for a client. Arguments: $ARGUMENTS (client name).

Generates everything Jordan needs for a confident 80-minute handover call.

Do not ask for confirmation between steps.

---

**STEP 1 — Read client context**

Read:
- `A Human Workflow/A Manager/_clients/[nama]_checklist.md` — what's complete
- `VLT_Content/clients/[nama]/client_brief.md` — brand, niche, offer
- `Z Products/Fulfillment/_OFFER_BLUEPRINT/offer_sheets/[nama]/` — offer sheet
- `VLT_Content/clients/[nama]/projects/month_01/` — content batch status

**STEP 2 — What's live checklist**

List every deliverable ready with ✅ or 🔴:
- Offer sheet
- VSL funnel (Netlify)
- Content batch Month 1 (X reels)
- n8n automations (keyword CTA, booking WA, dashboard, Telegram)
- CEO Dashboard Excel
- Telegram bot
- Community/Discord

Flag 🔴 items — Jordan must know gaps before the call.

**STEP 3 — Generate call agenda**

Output time-boxed 80-minute agenda:
```
00:00–05:00  Quick win — show first metric already visible
05:00–15:00  Walk offer sheet (live doc)
15:00–25:00  Demo VSL funnel (Netlify, live)
25:00–40:00  Show content batch (top 5 reels in GDrive)
40:00–50:00  Demo keyword CTA live (comment → DM fires)
50:00–60:00  Walk CEO Dashboard Excel
60:00–65:00  Show Telegram daily report
65:00–75:00  Set Month 2–4 goals + KPIs together
75:00–80:00  Next steps + Chrome Sales HQ walkthrough
```

**STEP 4 — Talking points per section**

For each agenda section: 2–3 bullets Jordan can reference.
Customize to the client's niche, offer, and specific goals.

**STEP 5 — Month 2–4 goals**

Suggest based on client niche:
- Month 2: First organic close target, suggested ad spend
- Month 3: Scale content volume, retargeting campaign
- Month 4: Referral system, offer upsell

**STEP 6 — Post-call action list**

What Jordan does in 5 minutes after the call ends:
1. Update checklist — mark Fase 2 complete
2. Update `A Human Workflow/A Manager/client_board.md` → status 🟢 AKTIF
3. Update CRM → stage: Active
4. Confirm n8n sends Chrome Sales HQ instructions automatically

**STEP 7 — Save and report**

Save everything to `Z Products/Fulfillment/_CLIENT_DELIVERABLES/[nama]/handover_brief_[YYYY-MM-DD].md`

Output: "Handover brief ready. Open `Z Products/Fulfillment/_CLIENT_DELIVERABLES/[nama]/handover_brief_[date].md` — review 10 minutes before the call."
