# CRM Inbox Integration Plan — Real Estate Vertical

## Objective
Automate the extraction of lead data from Instagram/WhatsApp DMs and sync them directly into the Real Estate CRM (`RE_CRM.xlsx` or Google Sheets). This ensures no lead is dropped and the "Last Contact" date is always fresh.

## Key Files & Context
- **CRM Tracker:** `01 HMN__Command/11_Real_Estate/Dash/RE_CRM.xlsx`
- **Sales SOP:** `PDCT_Real_Estate\_AI SOP\A Setter Playbook\Cold-Database.md`
- **Automation Tool:** `AI_Tools/re_crm_manager.py` (To be created/extended)

---

## Workflow: DM to CRM

### 1. Capture & Extract
When a DM snippet is pasted (e.g., "Pak Ray" example), the AI will extract:
- **Name:** Lead's name (e.g., Ray).
- **IG Handle:** (If available).
- **Project Interest:** (e.g., Savasa / Yamabuki).
- **Qualification:** 
    - 2/3 Bedrooms? (LB 61 / LT 60).
    - Status: WARM (Inquiry received, responded).
- **Source:** Instagram DM.

### 2. CRM Sync Logic
The extracted data will be mapped to the `Pipeline` sheet in `RE_CRM.xlsx`:
| Column | Value |
| --- | --- |
| **Name** | Pak Ray |
| **Source** | IG Organic |
| **Status** | response |
| **Temp** | WARM |
| **Property Type** | Landed (Savasa) |
| **Last Contact** | 2026-03-12 |
| **Next Action** | Send KPR simulation / Visit Unit |
| **Notes** | Minat unit 2/3 kamar. Tipe Yamabuki LB 61/LT 60. |

### 3. Automated Drafting
The system will generate a response based on the **Setter Playbook**:
- **Goal:** Move from DM to WhatsApp or Site Visit.
- **Draft:** *"Halo Pak, untuk tipe Yamabuki (LB 61) ini favorit untuk 2 kamar. Boleh saya kirimkan simulasi cicilan KPR-nya lewat WhatsApp agar lebih jelas, Pak?"*

---

## Technical Implementation Steps

### Phase 1: Context Processor (Manual Prompting)
- Create a system prompt for the agent to "Analyze DM" and output a JSON format compatible with the CRM.

### Phase 2: CRM Update Tool (`re_crm_manager.py`)
- Extend `re_crm_setup.py` or create a new script to **append/update** rows in `RE_CRM.xlsx`.
- Command: `py -3 AI_Tools/re_crm_manager.py --add-lead data.json`

### Phase 3: Google Sheets Sync (Optional)
- Use `cook_add_n8n_sheet.py` logic to push the same data to the Google Sheet CRM if real-time team access is needed.

---

## Verification & Testing
- **Test Case:** Paste the "Pak Ray" DM.
- **Success Criteria:**
    1. AI correctly identifies "Pak Ray" as the prospect.
    2. AI identifies "Savasa Yamabuki" as the interest.
    3. AI generates a JSON blob for the Excel file.
    4. AI drafts a response that doesn't mention price immediately (per SOP).

---

*Plan drafted on 2026-03-19 for Jordan Mathew (Savasa Inhouse).*
