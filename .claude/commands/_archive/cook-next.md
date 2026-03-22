---
tags:
  - claude-config
---
Tell Jordan the single next action for a client. Arguments: $ARGUMENTS (client name).

Read `A Human Workflow/A Manager/_clients/[nama]_checklist.md`.
Scan for the first unchecked item `[ ]` that is assigned to `@Jordan`.

Output ONLY:
1. The single next thing Jordan needs to do
2. How long it takes (in minutes)
3. Exactly how to do it (one sentence or one command to type)
4. What happens after (what Claude or n8n handles next automatically)

Keep it under 5 lines total. No preamble. No context unless Jordan asks.

Example output:
---
**Next for [NAMA]:** Confirm ElevenLabs voice clone approved by client
**Time:** 5 min
**How:** Open ElevenLabs → [client] voice → send 10-second test clip to client on WhatsApp
**After:** Claude generates voiceover batch automatically once approved
---

If there are no Jordan tasks remaining in the current phase, say:
"[NAMA] is all yours on Claude/n8n right now. Next Jordan action is [X] in Phase [Y], estimated [date]."

If there's a blocked item, surface that first with the context needed to unblock it.
