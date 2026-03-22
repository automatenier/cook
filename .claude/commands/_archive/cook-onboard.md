---
description: Onboard a new client into JO Consult.
tags:
  - claude-config
---
> **Model: Sonnet** -- multi-step onboarding with folder setup and brief generation

Onboard a new client. Arguments: $ARGUMENTS
Format: [client_name] [tier]   Example: fadli bedah-digital

Parse arguments:
- client_name = first word, lowercased, spaces -> hyphens
- tier = remaining words (e.g. "AI & Scale" or "Bedah Digital")

Execute in order. Do not ask for confirmation between steps.

---

**STEP 1 -- Create folders**

```bash
mkdir -p "PDCT_JO_Consult/clients/[client_name]"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/0_Brand_Guidelines"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/1_Footage"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/2_Viral_Formats"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/3_LUTs_Filters"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/4_Audio_Voices"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/projects/[YYYY-MM]/scripts"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/projects/[YYYY-MM]/approved"
mkdir -p "PDCT_JO_Consult/deliverables/[client_name]"
```

**STEP 2 -- Initialize Client Brief**

Create `VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/client_brief.md`.
Use `VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/client_brief.md` as base template.
Replace: [client_name], [tier], today's date.

**STEP 3 -- Report to Jordan**

```
Onboarding complete -- [client_name]

Folders created:
- PDCT_JO_Consult/clients/[client_name]/
- VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/
- PDCT_JO_Consult/deliverables/[client_name]/

Client Brief: VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/client_brief.md

Next action (Jordan, 5 min):
-> Confirm n8n sent the welcome email.
-> Book the onboarding call.
-> Update CRM in 01 HMN__Command/00_COOK/ with new client row.
```
