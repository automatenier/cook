# Command: /sync-writing-production

**Objective:** Synchronize the '# Production' lane from the Writing Kanban to the Content System Kanban.

**Workflow:**

1.  **Receive Directive:** Triggered by `/sync-writing-production`.
2.  **Execute Tool:** Run the `AI_Tools/content_kanban_production_sync.py` script.
    ```bash
    py -3 AI_Tools/content_kanban_production_sync.py
    ```
3.  **Process Output:** The script will move tasks from the 'Production' lane in `VLT_Content/__VLT_OBSVAULT/_  AReadme/New/Writing.md` to the 'Production' lane in `VLT_Content/01 HMN_Command/CONTENT SYSTEM.md`.
4.  **Confirm Completion:** Notify the user of how many tasks were transferred.

**Manual Verification:**
1. Check `VLT_Content/__VLT_OBSVAULT/_  AReadme/New/Writing.md` to ensure 'Production' lane is cleared of transferred tasks.
2. Check `VLT_Content/01 HMN_Command/CONTENT SYSTEM.md` to ensure tasks appear in the 'Production' lane.
