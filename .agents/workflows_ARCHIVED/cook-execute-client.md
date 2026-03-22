---
tags:
  - workflow
---
# Consult-Execute-Client Workflow

**Trigger:** User says `"Execute [Client Name] workflow"` or `"Continue [Client Name] sprint"`
**Purpose:** Drive the 14-day client sprint from current state — execute AUTO blocks, surface COLLECT requests, enforce gating rules.

---

## Inputs Required

| Input | Source |
|-------|--------|
| Client name | From user trigger |
| Client worksheet | `PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_X_Worksheet.md` |
| Delivery architecture | `AI_MEMORY/delivery-system.md` |
| Client context | `AI_MEMORY/JOConsults.md` |

---

## Execution Steps

### Step 1 — Load Current State

1. Read the client's worksheet
2. Find the `## 📍 CURRENT STATE` table
3. Note: `Day`, `Phase`, `Last Completed`, `Paused — Waiting For`
4. If `Paused — Waiting For` is not empty → go to **Step 2 (Unblock)**
5. If nothing blocking → go to **Step 3 (Execute)**

---

### Step 2 — Unblock a COLLECT

When the current state shows a pending COLLECT:

1. Tell the user exactly what is needed (copy the COLLECT block from the worksheet)
2. Wait for input
3. When received:
   - Save/confirm the collected item
   - Update the worksheet CURRENT STATE (`Last Completed` + clear `Paused — Waiting For`)
   - Check the gate condition for the next day (see `delivery-system.md`)
   - If gate is satisfied → proceed to Step 3
   - If other COLLECT items still pending → surface the next one

---

### Step 3 — Execute AUTO Blocks

For the current day's AUTO blocks:

1. Read the day section from the worksheet
2. Identify all `🤖 AUTO` blocks not yet marked ✅
3. Execute them in sequence:
   - If a tool is required → run it (see tool commands in `JOConsults.md`)
   - If inline generation → generate and save to the correct output path (see `delivery-system.md`)
   - Confirm save location after each output
4. After each AUTO block → mark it ✅ in the worksheet session log

**Do not batch all AUTO blocks into one response.** Complete one, confirm, then continue.

---

### Step 4 — Hit Next COLLECT or PLATFORM Block

After AUTO blocks for the day are done:

1. Surface the next `📥 COLLECT` or `⚙️ PLATFORM` block
2. State clearly: what the user needs to do, where to paste the result, and what it unlocks
3. Update `## 📍 CURRENT STATE`:
   - `Last Completed`: last finished block
   - `Paused — Waiting For`: the current COLLECT/PLATFORM item

---

### Step 5 — Day Complete Check

When all blocks for the current day are ✅:

1. Update `CURRENT STATE` → increment `Day`, set `Phase` to next phase
2. State: "Day [X] complete. Gate check for Day [X+1]:"
3. List each gate condition and its status (✅ met / ⏳ pending)
4. If all gate conditions met → ask user to confirm before advancing
5. If gate conditions not met → list what's still needed

---

## Edge Cases

| Situation | Action |
|-----------|--------|
| User provides COLLECT input mid-session | Accept it, update worksheet, continue immediately |
| AUTO block requires tool that fails | Read error, fix or flag, do not retry paid API calls without confirming |
| Client requests a revision to an approved output | Re-generate only that specific output, re-save, ask for re-approval |
| Day 4 filming not done yet | Note it as `🎬 ONSITE pending` — continue with parallel AUTO blocks that don't depend on footage |
| Monthly cycle (post Day 14) | Switch to Monday–Friday weekly cadence defined in `delivery-system.md` |

---

## Output

After each session block, update `## 📋 SESSION LOG` in the worksheet:

```
| [#] | [Date] | [What was completed] | [Paused at] | [Next session starts at] |
```

---

## Notes

- Never skip a gate condition — blocked outputs depend on prior COLLECT data
- All file saves must be confirmed before marking a block ✅
- If the worksheet doesn't exist yet for the client, create it from `_TEMPLATE_Worksheet.md` first
- Filming (Day 4) and consultation (Day 14) are physical — flag these as calendar items for Jordan

## Tool Invocation Examples

```bash
# Trigger this workflow
Execute Fadli workflow
# or
Continue Fadli sprint

# Tool commands used during AUTO blocks:

# Generate offer sheet from onboarding form
py -3 AI_Tools/cook_offer_agent.py --from-file "PDCT_JO_Consult/clients/Fadli/onboarding.json" --client-name "Fadli"

# Interactive offer generation (no JSON file yet)
py -3 AI_Tools/cook_offer_agent.py --interactive --client-name "Fadli"

# Capture a YouTube swipe reference for the client
py -3 AI_Tools/vault_youtube_note.py https://youtu.be/EXAMPLE_ID

# Repurpose approved content
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_WORKSPACE/fadli/projects/2026-02/approved/reel_01.md"

# Output worksheet location
# PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_2_Worksheet.md
```
