# Command: /calendar

**Objective:** Pull events from Google Calendar into the Kanban '🤙 Meetings' lane in Command.md.

**Workflow:**

1.  **Execute Tool:** Run the reverse sync script.
    ```bash
    py -3 AI_Tools/cook_gcal_reverse_sync.py
    ```
2.  **Process Output:** The script identifies future events in Google Calendar that are not already on the board and appends them to the meetings lane in `01 HMN__Command/Command.md`.
3.  **Confirm Completion:** Inform the user how many events were added.

**Note:** The script automatically ignores events that were previously synced from the Kanban to Google Calendar (marked with `[kanban-sync]`) and any events containing "birthday" in the title.
