---
description: Read all vault notes from today's date, compile a daily digest, execute any action todos found, and log what was changed. Usage: /vault-daily
tags:
  - claude-config
---

You are running the **vault-daily** command. Today's date is available via the `currentDate` in system context.

## Step 1 — Find today's notes in the vault

Run these two searches in parallel:

1. **Filename match** — files named `YYYY-MM-DD.md` (today's date) anywhere inside `VLT_OBSVAULT/`:
   ```bash
   find "c:/Workspace/Cook/VLT_OBSVAULT/" -name "<TODAY>.md" -not -path "*/.obsidian/*" 2>/dev/null
   ```
   Replace `<TODAY>` with today's actual date string (e.g., `2026-02-26`).

2. **Content match** — files that mention today's date inside their body:
   ```bash
   grep -rl "<TODAY>" "c:/Workspace/Cook/VLT_OBSVAULT/" --include="*.md" --exclude-dir=".obsidian" 2>/dev/null
   ```

Deduplicate the two lists. If no files are found, write the digest note with a "No vault entries found for today" section and skip to Step 4.

## Step 2 — Read each matched file

Read every file found in Step 1. For each file, extract:
- Full content
- Any checkboxes: `- [ ] …` or `- [x] …`
- Any lines containing keywords: `TODO`, `todo`, `action:`, `edit`, `update`, `fix`, `create`, `build`, `add`, `remove`, `change`

Categorise each item as:
- **Pending action** — unchecked `- [ ]` or a TODO/action keyword
- **Done** — checked `- [x]`
- **Note** — everything else (context, thoughts, references)

## Step 3 — Execute pending actions

For each **pending action** found:

1. Determine what file or system it targets. Use the action text as your guide.
   - If it says "edit system", check relevant files in `AI_BRAIN/`, `CLAUDE.md`, or `.agents/workflows/`
   - If it says "update workflow", locate the relevant workflow in `.agents/workflows/`
   - If it says "add client", update `PDCT_JO_Consult/clients/` or `20_Data/JO_Consult_CRM.xlsx` per existing patterns
   - If unclear, log it as "Needs clarification" and skip execution

2. Before editing any file, read it first.

3. Make the change. Keep edits minimal and targeted — don't refactor beyond what the action says.

4. Log the action in a running list: `[action text] → [file edited] → [what changed in 1 line]`

**Hard limits:**
- Never touch `VLT_OBSVAULT/` — it is READ-ONLY
- Never modify `20_Data/` without a backup to `.tmp/backup/` first
- If an action is ambiguous or risky, log it as "Skipped — needs clarification" instead of guessing

## Step 4 — Write the daily digest note

Write to: `c:/Workspace/Cook/HMN_A INPUTS/daily_brief/<TODAY>-vault-digest.md`

Use this exact structure:

```markdown
# Vault Digest — <TODAY>

## Notes from Today
<!-- One bullet per vault file read, with a 1–2 line summary of its content -->
- **[filename]:** [summary]

## Extracted Actions
<!-- All action items found, with status -->
| Action | Source File | Status |
|--------|------------|--------|
| [action text] | [filename] | Done / Skipped — needs clarification |

## What Was Edited
<!-- One entry per change made in Step 3 -->
- **[file path]:** [what changed — 1 sentence]

## Pending (Needs Your Input)
<!-- Actions skipped due to ambiguity -->
- [action text] — from [filename]
```

If no actions were found, write "No actions found in today's vault entries." in the Actions section.

## Step 5 — Confirm

After writing the digest:
1. Show the user the file path of the digest note
2. Print the **What Was Edited** and **Pending** sections so they can review immediately
3. If nothing was found in the vault for today, say so plainly and suggest they check if daily notes are being created
