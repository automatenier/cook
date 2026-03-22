---
tags:
  - memory
---
# MEMORY — Cook Project

## Project Structure (verified 2026-03-02)

- WAT framework: `AI_Tools/`, `.env` for API keys
- Client content: `VLT_Content/02_HMN_HUMANFLOW/[client_name]/`
- Client acquisition: `PDCT_JO_Consult/` and `PDCT_Real_Estate/` (Vault: `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/`)
- Command Center: `01 HMN__Command/` (Logs, KPIs, Guides)
- Capture OS: `02 HMN_A INPUTS/` (Meetings, Ideas, Briefs)
- Obsidian vault: `VLT_Content/__VLT_OBSVAULT/` (READ-ONLY except `PDCT_JO_ED/`)
- Education vertical: `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/` (Courses, Modules)
- Commands: `.claude/commands/` and `.gemini/commands/`

---

## Active Clients (as of 2026-03-02)

- Fadli — Bedah Digital tier
- Mathew_Jordan
- Ruth
- Real Estate (vertical)
- SAVASA

---

## File Routing Rules

- **NEVER use `.tmp/` as a dumping ground.** It is for disposable, auto-generated files only.
- Always route new files to the correct folder:
  - Scripts/tools → `AI_Tools/`
  - Client deliverables → `PDCT_JO_Consult/` or `VLT_Content/02_HMN_HUMANFLOW/[client]/`
  - Course content → `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/`
  - Agent memory/notes → `AI_MEMORY/`
  - Raw input → `02 HMN_A INPUTS/`
  - Dashboards/spreadsheets → `01 HMN__Command/` (NEVER inside VLT_ folders)

---

## Key Files

| File | Purpose |
|---|---|
| `01 HMN__Command/00_COOK/Daily_KPI_Tracker.xlsx` | Jordan's deals/pipeline tracker — DO NOT OVERWRITE |
| `01 HMN__Command/00_COOK/agent_log.csv` | Agent execution log |
| `01 HMN__Command/00_CONTENT/Content_Performance_Tracker.xlsx` | Content performance tracking (synced from Kanban) |
| `AI_Tools/tools_index.md` | Tool lookup — grep this before searching manually |
| `AI_BRAIN/README.md` | Context OS README |
| `CLAUDE.md` | Claude agent instructions (auto-loaded, never re-read mid-session) |
| `gemini.md` | Gemini agent instructions |

---

## Obsidian Wikilink Syntax

Jordan's vault uses standard Obsidian linking. Always interpret these automatically:
- `[[Note Name]]` — internal link to a note called `Note Name.md` in the vault
- `[[Note Name|Alias]]` — same link but displayed as "Alias"
- `[[Note Name#Heading]]` — links to a specific heading inside a note
- `[[Note Name#^block-id]]` — links to a specific block/paragraph
- `![[file]]` — embeds a file (image, PDF, or note)

**How to resolve wikilinks:** Cannot auto-navigate them. When Jordan references `[[Note Name]]`, ask for the file path or paste content — unless path can be inferred from vault structure (`VLT_Content/__VLT_OBSVAULT/`).

---

## Critical Lessons

- **Never overwrite existing files without reading them first** — untracked in git ≠ empty
- `01 HMN__Command/00_COOK/Daily_KPI_Tracker.xlsx` has live pipeline data — DO NOT OVERWRITE
- When a task says "create a new X", always use a new filename — never assume an existing file is the right target
- `.env` is READ-ONLY — never touch it. Tell Jordan if a key is missing.
- `VLT_Content/__VLT_OBSVAULT/` is READ-ONLY except `PDCT_JO_ED/`
- Jordan wants clean directories — don't accumulate files in temp folders
