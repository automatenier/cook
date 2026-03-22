# Command: /systems

**Objective:** Activate all systems for a client.

**Arguments:** $ARGUMENTS (client name)

**Workflow:**

1.  **Check Prerequisites:**
    Read `VLT_OBSVAULT/01 HMN__Command/_clients Checklists/[nama]_checklist.md`.
    Verify Phase 2 (Konten Setup) and Fase 1 (Filming) are complete.
    If not complete, stop and output: "Cannot activate systems. Missing: [list exact incomplete items]."

2.  **n8n Activation Checklist:**
    Output the checklist for Jordan to activate n8n flows (Keyword CTA, Post-booking WA, CEO Dashboard, Telegram report).

3.  **GDrive Folder Structure:**
    Write `PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/[nama]/gdrive_setup.md` with the recommended structure.

4.  **Check Funnel Status:**
    Verify VSL and offer sheet files exist in `VLT_Content/02_HMN_HUMANFLOW/jocons/[nama]/`.
    Write `PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/[nama]/funnel_checklist.md` with status.

5.  **Update Checklist:**
    In `VLT_OBSVAULT/01 HMN__Command/_clients Checklists/[nama]_checklist.md`, mark `[x]` for GDrive setup and Netlify funnel ready. (Note: Since VLT_OBSVAULT is read-only, request the user to confirm this update in their vault).

6.  **Report to Jordan:**
    Output a final summary of the system activation status.
