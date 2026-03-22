# Command: /status

**Objective:** Give a complete status briefing for a client or all active clients.

**Workflow:**

1.  **Identify Input:** The user can provide a client name as an argument. If no argument is provided, the tool will show status for all active clients.
2.  **Execute Tool:** Run the `AI_Tools/cook_client_status.py` script.
    ```bash
    py -3 AI_Tools/cook_client_status.py [--client "<client_name>"]
    ```
3.  **Process Output:** The script will return a summary of today's agenda and sprint status.
4.  **Confirm Completion:** Present the formatted output to the user.

**Manual Fallback (if tool fails or detailed brief needed):**
Read these files:
1. `VLT_OBSVAULT/01 HMN__Command/_clients Checklists/[nama]_checklist.md`
2. `VLT_OBSVAULT/01 HMN__Command/client_board.md` — find their row
3. Any recent files in `VLT_Content/02_HMN_HUMANFLOW/[nama]/projects/`
4. `PDCT_JO_Consult/2_Product_Pipeline/Fulfillment/_CLIENT_DELIVERABLES/[nama]/` — check what exists
