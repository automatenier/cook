---
description: Build all Phase 2 deliverables for a client.
tags:
  - claude-config
---
> **Model: Sonnet** -- deliverable generation requires strategic copywriting

Build all deliverables for a client. Arguments: $ARGUMENTS (client name).

Phase 2 -- everything Claude generates before the offer review call.
Do not ask for confirmation between steps.

---

**STEP 1 -- Read onboarding data**

Check `PDCT_JO_Consult/clients/[nama]/onboarding.json`.
If missing, check `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/client_brief.md`.
If no data: "Missing onboarding data. Need: [list specific fields]."

**STEP 2 -- Run offer agent**

```bash
py -3 AI_Tools/cook_offer_agent.py --from-file "PDCT_JO_Consult/clients/[nama]/onboarding.json" --client-name "[nama]"
# Output: PDCT_JO_Consult/deliverables/[nama]/offer_sheet.md
# If tool fails: generate offer sheet inline and save to same path
```

**STEP 3 -- Build client brief**

Check `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/client_brief.md`.
If not exists, create from onboarding data: niche, ICP, offer, tone, brand voice, top objections.

**STEP 4 -- Generate VSL script**

Write to `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/projects/[YYYY-MM]/vsl_script.md`.
Structure: Hook -> Problem -> Agitation -> Solution -> Proof -> Offer -> CTA.

**STEP 5 -- Generate reactivation scripts**

Create `PDCT_JO_Consult/deliverables/[nama]/reactivation/` and write:
- `hot_leads.md` (< 30 days), `warm_leads.md` (30-90 days), `cold_leads.md` (90+ days)

**STEP 6 -- Generate shot list**

Write to `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/projects/[YYYY-MM]/shot_list.md`.

**STEP 7 -- Report to Jordan**

```
Build complete -- [nama]

- Offer sheet: PDCT_JO_Consult/deliverables/[nama]/offer_sheet.md
- VSL script: VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/projects/[YYYY-MM]/vsl_script.md
- Shot list: VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/projects/[YYYY-MM]/shot_list.md
- Reactivation: PDCT_JO_Consult/deliverables/[nama]/reactivation/

Before offer review call:
-> Review offer sheet (10 min) -- approve or edit 1 item
-> Review VSL script -- flag any line that doesn't sound like you
-> ElevenLabs voice clone still needs Jordan (10 min, do before filming day)
```
