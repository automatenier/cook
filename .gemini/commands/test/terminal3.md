# Command: /terminal3
# Role: Systems / Tools Agent

## Instruction:
1.  **Isolate Lane**: Use `grep_search` to find the line number of `## # :LiTerminalSquare: Terminal 3` in `01 HMN__Command\00_KANBAN_COMMAND.md`.
2.  **Targeted Read**: Use `read_file` starting from that line number until the next `## #` header or the end of the task list.
3.  **Strict Focus**: Identify technical tasks like `/systems`, `/migrate`, or folder restructuring ONLY within this specific lane. Ignore all other headers and lanes.
4.  **Implementation Plan**: For each task in this section, provide an **Implementation Plan**:
    *   **Technical Goal**: What system needs updating or migrating.
    *   **Tool**: Which Python script to run.
5.  **Wait for Acceptance**: Ask: *"Would you like me to proceed with this implementation plan for Terminal 3?"*
6.  **Update Board**: Run tools and update the board checkboxes upon approval.
