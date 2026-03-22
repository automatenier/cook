---
description: Activate all systems for a client -- n8n flows, GDrive, funnel.
tags:
  - claude-config
---
> **Model: Sonnet** -- systems activation requires cross-checking multiple dependencies

Activate all systems for a client. Arguments: $ARGUMENTS (client name).
Do not ask for confirmation between steps.

---

**STEP 1 -- Check prerequisites**

Check `PDCT_JO_Consult/clients/[nama]/worksheet.md` for Phase 2 (Konten Setup) and Phase 1 (Filming) status.
If not complete, stop: "Cannot activate systems. Missing: [list exact incomplete items]."

**STEP 2 -- n8n activation checklist**

```
n8n Flows to Activate -- [NAMA]

[ ] Keyword CTA (IG + TikTok)
    -> Jordan: Set keyword in n8n flow + connect Meta Biz Suite for [nama]

[ ] Post-booking WA reminder
    -> Jordan: Connect [nama]'s WA Business API

[ ] CEO Dashboard auto-update
    -> Jordan: Paste [nama]'s Excel file link into n8n config

[ ] Telegram daily report
    -> Jordan: Confirm Telegram bot token is set for [nama]
```

**STEP 3 -- GDrive folder structure**

Write `PDCT_JO_Consult/deliverables/[nama]/gdrive_setup.md`:
```
[NAMA] -- Jo Consult/
A-Roll/ | B-Roll/ | Assets/ | Audio/ | Edited/ | Posted/
```
Include: share link with client, request 10 GB minimum space.

**STEP 4 -- Check funnel readiness**

Check `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/` for VSL + offer sheet.
Write `PDCT_JO_Consult/deliverables/[nama]/funnel_checklist.md` with status.

**STEP 5 -- Report to Jordan**

```
Systems checklist -- [NAMA]

1. n8n: [X/4 flows ready] -- see PDCT_JO_Consult/deliverables/[nama]/
2. GDrive: Template created -- share link with client
3. Funnel: [deploy-ready / missing: list]
4. Demo order: keyword CTA -> dashboard -> Telegram -> funnel

Jordan time to confirm all live: 5 minutes max.
```
