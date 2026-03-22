> **Model: Sonnet** -- complex sprint orchestration with gate logic

# Consult-Execute-Client Workflow

**Trigger:** "Execute [Client] workflow" or "Continue [Client] sprint"

## Inputs

| Input | Source |
|-------|--------|
| Client worksheet | `PDCT_JO_Consult/2_Product_Pipeline/Client_Worksheets/[client]_Worksheet.md` |
| Delivery architecture | `AI_MEMORY/delivery-system.md` |
| Client context | `AI_MEMORY/JOConsult/` |

## Execution Steps

### Step 1 -- Load Current State
1. Read the client's worksheet, find `## CURRENT STATE` table
2. Note: Day, Phase, Last Completed, Paused -- Waiting For
3. If Paused -> Step 2. If nothing blocking -> Step 3.

### Step 2 -- Unblock a COLLECT
1. Tell user exactly what is needed
2. When received: save it, update CURRENT STATE, check gate condition
3. If gate satisfied -> Step 3. If more COLLECTs pending -> surface next one.

### Step 3 -- Execute AUTO Blocks
1. Find all AUTO blocks not yet marked done for the current day
2. Execute in sequence -- one block at a time, confirm save location after each
3. Mark done in worksheet session log

**Do not batch all AUTO blocks into one response. Complete one, confirm, then continue.**

### Step 4 -- Hit Next COLLECT or PLATFORM Block
1. Surface the next COLLECT or PLATFORM block
2. State: what to do, where to paste, what it unlocks
3. Update CURRENT STATE

### Step 5 -- Day Complete Check
1. Increment Day, update Phase
2. List each gate condition + status
3. Confirm before advancing if all gates met

## Edge Cases
| Situation | Action |
|-----------|--------|
| User provides COLLECT mid-session | Accept, update worksheet, continue |
| AUTO block tool fails | Read error, fix or flag -- do not retry paid API calls without confirming |
| Client requests revision | Re-generate only that output |
| Filming not done | Note as ONSITE pending -- continue parallel AUTO blocks |

## Tool Invocation
```bash
py -3 AI_Tools/cook_offer_agent.py --from-file "PDCT_JO_Consult/2_Product_Pipeline/Onboarding/fadli_onboarding.json" --client-name "Fadli"
py -3 AI_Tools/vault_youtube_note.py https://youtu.be/EXAMPLE_ID
py -3 AI_Tools/content_repurpose.py "VLT_Content/02_HMN_HUMANFLOW/jocons/fadli/projects/2026-03/approved/reel_01.md"
```

## Notes
- Never skip a gate condition
- All file saves must be confirmed before marking a block done
- Filming (Day 4) and consultation (Day 14) are physical -- flag as calendar items for Jordan
