> **Model: Sonnet** -- outreach scripting and pipeline prioritization require judgment

# RE Outreach Workflow

**Trigger:** "Run RE outreach" or "RE setter session"

## Inputs
- `PDCT_Real_Estate/pipeline/tracker.xlsx`
- `PDCT_Real_Estate/prospects/`
- `PDCT_Real_Estate/scripts/`

## Execution Steps

### Step 1 -- Load Pipeline State
Read tracker (or ask user to paste summary). Identify: HOT / WARM / COLD / New leads.

### Step 2 -- Prioritize Daily Actions
1. Follow up HOT leads  2. Send viewing confirmations (24h before)  3. Follow up WARM leads  4. Send 20+ new cold DMs  5. Add 5-10 new prospects

### Step 3 -- Generate Outreach Messages
- **Cold DM**: `PDCT_Real_Estate/scripts/cold_dm_scripts.md` -- personalize with name + property
- **Follow-up**: `PDCT_Real_Estate/scripts/follow_up_scripts.md` -- max 3 follow-ups before Lost
- **Post-viewing (within 2h)**: `PDCT_Real_Estate/scripts/post_viewing_scripts.md`
- **Objections**: `PDCT_Real_Estate/properties/[property]/objections.md`

### Step 4 -- Update Pipeline
Update `tracker.xlsx`: stage, last contact, notes, next action + due date.

### Step 5 -- Weekly Review (every Monday)
Count by stage, identify stalled deals (5+ days), set weekly targets.

## Key Metrics
| DMs sent: 20/day | Responses: 5/day | Viewings: 1/day | Deals: 1/month |

## Edge Cases
- Price before viewing -> don't send price, book viewing first
- Ghosts after viewing -> 48h wait -> post-viewing follow-up -> 3 follow-ups -> mark Cold
- Content leads -> fast-track to viewing (warmer)
