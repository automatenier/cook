**Phase 0 — Prompt 1 (Onboard):** Mostly right. The `/onboard` skill exists and takes the client name. But it does NOT automatically initiate ElevenLabs voice cloning — that's a manual step.

**Phase 0 — Prompt 2 (CRM):** Wrong executor. You say to **Claude**: `run create_excel_crm for Alex`. Claude runs the Python tool. Also: `create_excel_crm.py` saves to a **local `.tmp/` folder**, not GDrive. The Google Sheets migration we just built changes this.

**Phase 0 — Prompt 3 (Offer/Content consult):** Direction is right. Claude would reference `workflows/content_creation.md` and the offer agent tool. But it doesn't auto-write into a Notion "AI Swipe File" — it writes to `VLT_Content/clients/alex/`.

**Phase 1-2 — Prompt 4 (Content generation):** Wrong executor again. This is Claude + `content_creation.md` workflow + `repurpose_content.py`. Not Gemini. The output also goes to the client's content folder, not auto-scheduled.

**Phase 1-2 — Prompt 5 (Repurpose):** Right tool, wrong executor. Claude runs `repurpose_content.py`.

**Phase 1-2 — Prompt 6 (Handover):** Correct — `/handover Alex` is a real skill.

**Phase 3 — Prompt 7 (Monthly):** Correct — `/monthly Alex` is a real skill. But "pull up dashboard stats" requires n8n sync first (Claude can't read GSheets directly, as we covered).

---

## The Accurate Version

```
Phase 0:
  /onboard Alex                          ← Claude skill
  Claude: run create_excel_crm for Alex  ← Claude executes Python tool
  Claude: run offer_agent for Alex       ← Claude skill/tool

Phase 1-2:
  /content Alex                          ← Claude skill → workflows + tools
  Claude: run repurpose_content for Alex ← Claude executes Python tool
  /handover Alex                         ← Claude skill

Phase 3+:
  /monthly Alex                          ← Claude skill
  /status Alex                           ← Claude skill
  /next Alex                             ← Claude skill
```

---

## One Line Summary

Gemini described **your system accurately** but confused itself for Claude and invented a Gemini-as-operator role that doesn't exist. Everything you read there — run it through Claude Code, not Gemini.