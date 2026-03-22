---
description: Drafts responses for WhatsApp, email, or DM conversations.
tags:
  - workflow
---

# Workflow: Draft Responses

When user asks to `/draft-responses [context]`:

1. **Receive Input**: User pastes the conversation thread or summarizes the context. Identify:
   - Platform (WhatsApp, email, Instagram DM, Telegram)
   - Who it's from (prospect, client, colleague, RE lead)
   - What they're asking or saying
   - Desired outcome of your reply

2. **Determine Tone** based on relationship:

   | Relationship | Tone |
   |---|---|
   | Warm prospect (consulting/RE) | Confident, helpful, low-pressure |
   | Active client | Direct, supportive, professional |
   | Cold lead | Brief, curiosity-driven, no pitch |
   | Internal / team | Casual, clear |

3. **Draft 2 Versions**: Short version (1-3 sentences) and full version (if needed). Label clearly.

4. **Flag if Action Needed**: If the message implies a follow-up task (schedule a call, send a doc, update CRM), state it explicitly at the bottom: "Action: [what to do after sending]."

5. **Output**: Print drafts directly in chat for user to copy-paste. Do not save to file unless user asks.

## Real Estate Context Rules
- For property inquiries: always confirm availability before committing
- For pricing questions: give range, not exact figure — "typically between X and Y, let's discuss your needs"
- For urgent leads: flag as "HOT — respond within 2 hours"

## Tool Invocation Examples

```bash
# Trigger with inline context
/draft-responses Ahmad is asking about pricing for Bedah Digital — wants to know if there's a payment plan

# Trigger with no context (agent will ask for the thread)
/draft-responses

# Output: printed directly in chat — no file saved unless requested
```
