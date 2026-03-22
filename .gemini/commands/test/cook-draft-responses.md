> **Model: Sonnet** -- DM and email drafting requires tone judgment

# Workflow: Draft Responses

When user asks to `/draft-responses [context]`:

1. **Receive Input**: Platform, who it's from, what they're asking, desired outcome.
2. **Determine Tone**:
   | Relationship | Tone |
   |---|---|
   | Warm prospect | Confident, helpful, low-pressure |
   | Active client | Direct, supportive, professional |
   | Cold lead | Brief, curiosity-driven, no pitch |
   | Internal | Casual, clear |
3. **Draft 2 Versions**: Short (1-3 sentences) + full version. Label clearly.
4. **Flag Actions**: If message implies follow-up, state: "Action: [what to do after sending]."
5. **Output**: Print directly in chat. No file saved unless requested.

## Real Estate Context
- Property inquiries: confirm availability before committing
- Pricing: give range, not exact -- "typically between X and Y"
- Urgent leads: flag as "HOT -- respond within 2 hours"

```bash
/draft-responses Ahmad is asking about pricing for Bedah Digital
/draft-responses   # Agent asks for thread context
```
