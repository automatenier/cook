Onboard a new client. Arguments: $ARGUMENTS
Format: [client_name] [tier]
Example: fadli bedah-digital

---

Parse arguments:
- client_name = first word, lowercased, spaces → hyphens (slug)
- tier = remaining words (e.g. "AI & Scale" or "Bedah Digital")

Execute these steps in order. Do not ask for confirmation between steps.

---

**STEP 1 — Create folders**

Run these mkdir commands:

```
mkdir -p "PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/[client_name]"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/0_Brand_Guidelines"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/1_Footage"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/2_Viral_Formats"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/3_LUTs_Filters"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/4_Audio_Voices"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/projects/2026-03/scripts"
mkdir -p "VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/projects/2026-03/approved"
```

**STEP 2 — Initialize Client Brief**

Create `VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/client_brief.md`.
Use the template from `VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/client_brief.md` as a base, replacing values with [client_name], [tier], and today's date.

**STEP 3 — Report to Jordan**

Output exactly this (fill in the blanks):

```
✅ Onboarding complete — [client_name]

Folders created:
- PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/[client_name]/
- VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/

Client Brief created: VLT_Content/02_HMN_HUMANFLOW/jocons/[client_name]/client_brief.md
(Note: Checklist and Board updates are currently handled manually in the Obsidian Vault)

Next action (Jordan, 5 min):
→ Confirm n8n sent the welcome email.
→ Book the onboarding call.
```
