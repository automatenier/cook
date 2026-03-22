---
description: Summarize session learnings into AI_MEMORY/sessions.md before clearing context
tags:
  - claude-config
---

Before the user runs /clear, capture what happened this session.

1. Write a concise session summary entry to `c:/Workspace/Cook/AI_MEMORY/sessions.md`. Append to the file — do NOT overwrite. Use this format exactly:

```
## YYYY-MM-DD — [1-line session title]
- **Client/scope:** [client name or "system work"]
- **Done:** [bullet list of what was completed]
- **Learned:** [any tool quirks, API limits, path issues, or new patterns discovered]
- **Next:** [what should happen next session, if known]
```

2. Use today's actual date.
3. After writing, confirm the entry was appended and tell the user: "Session logged — safe to run `/clear`."
