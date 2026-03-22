# Agent SOP: Product Knowledge vs. Content Production

## 1. Strict Workspace Separation
To maintain a clean and scalable system, agents MUST adhere to this structural boundary:

*   **`VLT_Content/__VLT_OBSVAULT/` (The Brain):** This is the **Source of Truth** for all Product Knowledge, research, strategy, and evergreen notes. 
    *   *Rule:* If a file describes *what* we are selling or *how* it works (technical specs, market analysis, competitor deep-dives), it lives here.
*   **`VLT_Content/` (The Factory):** This is the **Production Workspace** for scripts, storyboards, and final outputs.
    *   *Rule:* If a file is a script, a filming plan, or a specific project deliverable, it lives here.

## 2. Agent Workflow for New Knowledge
When an agent discovers or receives new product-related information:
1.  **Extract** the core knowledge (specs, USP, benefits).
2.  **Save** to the appropriate sub-folder in `VLT_Content/__VLT_OBSVAULT/_Product Knowledge/`.
3.  **Reference** that knowledge when writing scripts in the `VLT_Content/` workspace using Obsidian's `[[link]]` syntax (if applicable) or by reading the file.

## 3. Why This Matters
*   **Readability:** The vault is optimized for reading and connecting ideas.
*   **Reusability:** Product knowledge can be reused for 50 different reels without cluttering the content production folders.
*   **Clarity:** Keeping "The Brain" separate from "The Factory" prevents agents from getting lost in production drafts when they need technical facts.

---
*Last updated: 2026-02-28*
