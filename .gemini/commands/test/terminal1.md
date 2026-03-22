# Command: /terminal1
# Role: Manager / Lead Agent

## Instruction:
1.  **Isolate Lane**: Use `grep_search` to find the line number of `## # :LiTerminalSquare: Terminal 1` in `01 HMN__Command\00_KANBAN_COMMAND.md`.
2.  **Targeted Read**: Use `read_file` starting from that line number until the next `## #` header or the end of the task list.
3.  **Strict Focus**: Propose an **Implementation Plan** ONLY for the tasks found within this specific lane. Ignore all other headers and lanes.
4.  **Wait for Acceptance**: Ask: *"Would you like me to proceed with this implementation plan for Terminal 1?"*
5.  **Update Board**: Upon approval, execute and update the checkboxes in the original file.
