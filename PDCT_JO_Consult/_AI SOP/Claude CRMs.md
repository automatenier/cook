---
updated: 2026-02-22
tags:
  - system
---


Script is ready. Here's what happens when you run it:

```bash
python tools/migrate_to_sheets.py
```

**What it migrates (exact replica):**

|Tab|Rows|What's preserved|
|---|---|---|
|CRM|8|All 31 active columns, data values|
|EOD|50|All data + TARGETS row|
|SetterDash|40|All formulas (`=COUNTIFS(CRM!...)`) — calculate live|
|CashDash|35|All formulas (`=SUMPRODUCT(...)`) — calculate live|
|PaymentPlans|11|Data + `=F2-G2` formulas, totals|

**All preserved:** headers, frozen row 1, bold formatting, tab colors, cross-tab formulas.

**After it runs — 2 manual steps:**

1. Share the new Google Sheet with `n8nreader@festive-kayak-459112-e0.iam.gserviceaccount.com` as **Editor** (not just Viewer — n8n needs write access)
2. In n8n, upload the service account JSON key → it can then read/write the sheet by the ID saved to `.env`

Ready to run it? The browser sign-in will pop up once, then it's fully automated from there.