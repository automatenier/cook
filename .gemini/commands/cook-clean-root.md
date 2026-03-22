# Command: /clean-root

**Objective:** Maintain a clean workspace by ensuring the root directory contains ONLY folders.

**Workflow:**

1.  **Scan Root:**
    List the root directory (`.`) and identify any files that are not folders or essential system dotfiles (`.gitignore`, `.geminiignore`, `.env`, `.git`).

2.  **Auto-Route Files:**
    Automatically move files to their relevant homes:
    - **Instructions/Docs:** Move to `______Readme/` (e.g., `gemini.md`, `CLAUDE.md`, `README.md`).
    - **CRM/Reports:** Move to `PDCT_JO_Consult/F. Data Reporting/` (e.g., `.html`, `.xlsx`, `.csv`).
    - **Media/Footage:** Move to `VLT_Content/__VLT_OBSVAULT/01_HMN_INPUTS/Reels/` (e.g., `.mov`, `.mp4`, `.png`, `.jpg`).
    - **Scripts/Code:** Move to `AI_Tools/` (e.g., `.py`, `.js`).

3.  **Confirm Execution:**
    Provide a list of moved files and their new locations.

4.  **Enforce Rule:**
    Remind the user (and any other agent) that "The root directory is for folders ONLY."

---

**Trigger:** Run this manually if the root gets crowded, or after complex migrations.
