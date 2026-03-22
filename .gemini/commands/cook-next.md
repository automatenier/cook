# Command: /next

**Objective:** Tell Jordan the single next action for a client.

**Arguments:** $ARGUMENTS (client name)

**Workflow:**

1.  **Read Checklist:**
    Read `VLT_OBSVAULT/01 HMN__Command/_clients Checklists/[nama]_checklist.md`.
    Scan for the first unchecked item `[ ]` that is assigned to `@Jordan`.

2.  **Output Format:**
    Output exactly:
    - The single next thing Jordan needs to do.
    - Estimated time.
    - Exactly how to do it (one sentence or one command).
    - What happens after (automation).

3.  **Example Output:**
    ---
    **Next for [NAMA]:** [Action Name]
    **Time:** [X] min
    **How:** [Exact step]
    **After:** [Next automated step]
    ---

4.  **Special Cases:**
    - If no Jordan tasks remain: "[NAMA] is all yours on Claude/n8n right now. Next Jordan action is [X] in Phase [Y]."
    - If a blocked item exists: Surface it first with unblocking context.
