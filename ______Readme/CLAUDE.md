# Agent Instructions

You're working inside the **WAT framework** (Workflows, Agents, Tools). This architecture separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution. That separation is what makes this system reliable.

## The WAT Architecture

**Layer 1: Workflows (The Instructions)**
- Markdown SOPs stored in `.claude/commands/` (Claude) and `.gemini/commands/` (Gemini)
- Each command file is self-contained: model routing hint + full SOP
- Written in plain language, the same way you'd brief someone on your team

**Layer 2: Agents (The Decision-Maker)**
- This is your role. You're responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- Example: If you need to pull data from a website, don't attempt it directly. Find the relevant command in `.claude/commands/`, follow the SOP, then execute the Python tool in `AI_Tools/`

**Layer 3: Tools (The Execution)**
- Python scripts in `AI_Tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast
- **Modal** (`AI_Tools/cook_modal_app.py`) — cloud execution layer for running tools 24/7 when Jordan is away. Deployed at: https://automatenier--cook-tools-frontend.modal.run. Redeploy with: `PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/cook_modal_app.py`

**Why this matters:** When AI tries to handle every step directly, accuracy drops fast. If each step is 90% accurate, you're down to 59% success after just five steps. By offloading execution to deterministic scripts, you stay focused on orchestration and decision-making where you excel.

## How to Operate

**1. Look for existing tools first**
Before building anything new, check `AI_Tools/` based on what your workflow requires. Only create new scripts when nothing exists for that task.
**To find the right tool instantly:** Grep `AI_Tools/tools_index.md` — one row per tool with purpose, invocation, and output.
Example: `grep -i "repurpose" AI_Tools/tools_index.md`

**2. Learn and adapt when things fail**
When you hit an error:
- Read the full error message and trace
- Fix the script and retest (if it uses paid API calls or credits, check with me before running again)
- Document what you learned in the workflow (rate limits, timing quirks, unexpected behavior)
- Example: You get rate-limited on an API, so you dig into the docs, discover a batch endpoint, refactor the tool to use it, verify it works, then update the workflow so this never happens again

**3. Keep workflows current**
Workflows should evolve as you learn. When you find better methods, discover constraints, or encounter recurring issues, update the workflow. That said, don't create or overwrite workflows without asking unless I explicitly tell you to. These are your instructions and need to be preserved and refined, not tossed after one use.

## The Self-Improvement Loop

Every failure is a chance to make the system stronger:
1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow with the new approach
5. Move on with a more robust system

This loop is how the framework improves over time.

## File Structure

**What goes where:**
- **Dashboards & spreadsheets**: `01 HMN__Command/` — ALL Excel/CSV files live here. `00_CONTENT/` for content trackers, `10_JO_Consult/Dash/` for consult CRM, `11_Real_Estate/Dash/` for RE. NEVER place .xlsx or .csv files inside `VLT_Content/` or `VLT_Content/__VLT_OBSVAULT/` — those vaults are markdown-only.
- **Human guides**: `VLT_Content/HMN_HUMAN/` — setup guides for tools (Chrome, VSCode, Obsidian, Claude Code, Gemini). READ reference only. No spreadsheets.
- **Context & priming**: `AI_BRAIN/` — stable SOPs, business model, agent instructions
- **Capture**: `02 HMN_A INPUTS/` — raw input (meetings, ideas, daily briefs) before routing
- **Client acquisition**: `PDCT_JO_Consult/` — consulting CRM, pipeline, outreach, proposals, SOWs. `PDCT_Real_Estate/` — RE pipeline, prospects, scripts (Vault: `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/`)
- **Content (all verticals)**: `VLT_Content/02_HMN_HUMANFLOW/jocons/` — JO Consult content. `VLT_Content/02_HMN_HUMANFLOW/real_estate/` — RE content. All script writing and production lives in `VLT_Content/` regardless of vertical.
- **Automation specs**: `AI_n8n/JOCONSULT/` — all JO Consult n8n workflows (including `_CLIENT_SYSTEMS/` + `_JO_CONSULT/`). `AI_n8n/REAL_ESTATE/` — RE-specific n8n workflows.
- **Content production**: `VLT_Content/` — full MS Content pipeline (inbox → workspace → review → outputs → archive)
- **Automation docs**: `AI_n8n/` — n8n workflow specs (actual workflows live in n8n cloud)
- **Python tools**: `AI_Tools/` — execution scripts
- **Obsidian vault**: `VLT_Content/__VLT_OBSVAULT/` — Jordan's personal knowledge base. Contains `PDCT_JO_ED/` (education vertical — courses, modules) and `PDCT_Real_Estate/` (real estate vertical). Agents may READ anywhere; may WRITE only inside `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/` and `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/`.
- **Temp files**: `.tmp/` — disposable, regenerated as needed

**Directory layout:**
```
Cook/
├── CLAUDE.md                  # This file — agent instructions
├── gemini.md                  # Gemini agent instructions
├── .env                       # API keys (NEVER store secrets anywhere else)
│
├── 01 HMN__Command/           # Command Center — Project trackers (COOK, CONTENT, OBSVAULT)
│   ├── 00_COOK/             # Agent logs, KPI trackers
│   ├── 00_CONTENT/
│   └── 00_OBSVAULT/
│
├── __Readme/                  # Workspace Guides — Prefix-by-prefix documentation
│
├── AI_BRAIN/                  # Context OS — agent priming & master SOPs
│   ├── context/               # Business model, avatar, brand voice, pricing
│   ├── SOPs/                  # Master SOPs (cross-vertical)
│   └── agent_instructions/    # Per-agent priming files
│
├── 02 HMN_A INPUTS/           # Capture OS — all raw input lands here
│   ├── meetings/              # Call transcripts, Plaud Note exports
│   ├── ideas/                 # Raw ideas before triage
│   └── daily_brief/           # Auto-generated daily briefs (n8n → here)
│
├── AI_MEMORY/           # Agent memory — persists across sessions
│
├── .tmp/                    # Temp files — regenerated as needed
│
├── PDCT_JO_Consult/             # Client acquisition OS — consulting CRM, pipeline, proposals
│   ├── clients/               # Per-client folders
│   ├── pipeline/              # Lead tracking & CRM
│   ├── deliverables/          # Proposals, SOWs, offer blueprints
│   └── A Sales Assets/        # Website copy, sales collateral
│   # NOTE: content → VLT_Content/02_HMN_HUMANFLOW/jocons/ | n8n workflows → AI_n8n/JOCONSULT/
│
├── PDCT_Real_Estate/            # Client acquisition OS — RE pipeline & outreach (Vault: VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/)
│   ├── pipeline/              # tracker.xlsx — leads & deal stages
│   ├── properties/            # Per-project specs + objections
│   ├── prospects/             # Individual prospect notes
│   ├── scripts/               # Sales call scripts, objection handling
│   └── A Sales Assets/        # Website copy, RE sales collateral
│   # NOTE: content → VLT_Content/02_HMN_HUMANFLOW/real_estate/ | n8n workflows → AI_n8n/REAL_ESTATE/
│
├── AI_n8n/                    # N8N automation docs — all vertical workflows
│   ├── JOCONSULT/             # JO Consult n8n specs
│   │   ├── _CLIENT_SYSTEMS/   # Client delivery bots, forms, notifications
│   │   ├── _JO_CONSULT/       # Consult forms, sales, onboarding
│   │   ├── Chatbot/
│   │   ├── Outreach/
│   │   ├── Sales/
│   │   └── Voice/
│   ├── REAL_ESTATE/           # RE-specific n8n specs
│   └── _JORDAN/               # Jordan's personal automations
│
├── AI_Tools/                  # Python execution layer
│   ├── modal_app.py           # Modal cloud deployment (repurpose + web UI)
│   ├── analyze_viral_reel.py
│   ├── repurpose_content.py
│   ├── offer_agent.py
│   ├── crm_manager.py
│   ├── render_manager.py
│   └── requirements.txt
│
├── VLT_Content/__VLT_OBSVAULT/         # Jordan's personal Obsidian knowledge base (READ-ONLY except PDCT_JO_ED/ and PDCT_Real_Estate/)
│   └── PDCT_JO_ED/            # Education vertical — agents may write here
│       ├── courses/
│       │   ├── _template/     # Copy to start a new course
│       │   └── [course_name]/
│       │       ├── brief.md
│       │       ├── modules/   # One .md per module
│       │       └── published/ # Final exports
│       └── workflows/
│
├── VLT_Content/                       # JO Content vertical — full production pipeline
│   ├── AI_BRAIN/              # Content SOPs, agent instructions, shared assets
│   │   ├── Agent Instructions/    # Reels V2, Long Form
│   │   └── Remotion_Formulas/     # hook_bank.md, cta_bank.md, script_templates/
│   ├── 01_HMN_INPUTS/            # Swipe files, content ideas
│   ├── 02_HMN_HUMANFLOW/         # Active client work (ALL verticals — jocons, real_estate, external clients)
│   │   └── [client_name]/     # e.g. jocons/, real_estate/, Mathew_Jordan/
│   │       ├── client_brief.md
│   │       ├── 0_Brand_Guidelines/
│   │       └── projects/
│   │           └── [YYYY-MM]/
│   │               ├── scripts/   # Agent script outputs (pre-review)
│   │               └── approved/  # Approved scripts ready to render
│   ├── 03_HMN_REVIEW/            # Scripts flagged for user review
│   ├── 04_HMN_OUTPUTS/           # Final deliverables per client
│   ├── 05_VLT_FINAL/             # Approved/Published content
│   ├── ZZ_ARCHIVE/            # Posted / completed content
│   └── AI_ENGINE/             # Remotion + stitcher render engine
│
└── .agents/
    └── workflows_ARCHIVED/    # Legacy SOPs — merged into .claude/commands/ + .gemini/commands/
```

**Agent workflow commands:**

SOPs live in `.claude/commands/` (Claude) and `.gemini/commands/` (Gemini). Each file is self-contained with model routing hint at the top.

| Command | Model | Agent | What it does |
|---|---|---|---|
| `/content-write-scripts [Client]` | Sonnet | Both | Draft 3 hooks + scripts from brief + swipe files |
| `/content-render-reel [Client] [Ref]` | Haiku | Both | Render text-over-video via Remotion |
| `/content-reel-rewrite-csv [Client]` | Haiku | Both | Batch rewrite reels from CSV |
| `/content-generate-metadata [Client] [Ref]` | Haiku | Both | Titles, captions, hashtags, thumbnail brief |
| `/content-stories-carousel [Client]` | Haiku | Both | Generate story sequence & carousel content |
| `/content-youtube-thumbnail [Client]` | Haiku | Both | Generate YouTube thumbnail brief |
| `/content-youtube-repurpose [Client]` | Sonnet | **Claude only** | Repurpose long-form YouTube to short content |
| `/cook-approve-scripts [Client]` | Sonnet | Both | Approve drafted scripts for rendering |
| `/cook-inbox-triage` | Haiku | Both | Route everything in HMN_A INPUTS to correct vertical |
| `/cook-meeting-intelligence [file]` | Sonnet | Both | Extract action items from call transcript |
| `/cook-daily-brief` | Haiku | Both | Compile morning brief across all verticals |
| `/cook-draft-responses [context]` | Sonnet | Both | Draft WhatsApp/email/DM replies |
| `/cook-disco-prep [Prospect]` | Sonnet | Both | Prepare discovery call brief |
| `/cook-proposal-gen [Client]` | Sonnet | Both | Generate proposal + SOW |
| `/cook-execute-client [Client]` | Sonnet | Both | Execute active client sprint |
| `/cook-course-module [Course] [N]` | Sonnet | Both | Plan + script a course module |
| `/cook-feature-roadmap [Product]` | Sonnet | Both | Prioritize features + build roadmap |
| `/cook-re-outreach [Prospect]` | Sonnet | Both | Generate real estate outreach messaging |
| `/figma-pull [URL]` | Haiku | Both | Extract images or tokens from Figma |
| `/yt-outlier-finder` | Haiku | Both | Find YouTube outliers for research |
| `/yt-thumbnail-gen` | Haiku + Imagen | Both | Generate YouTube thumbnails |
| `/yt-video-edit` | Haiku | Both | Execute YouTube video edits |
| `/content-ai-video-workflow` | Haiku | Both | AI Video production workflow |
| `/content-engine` | Sonnet | Both | Core content engine orchestration |

**Core principle:** `.tmp/` is disposable. `PDCT_JO_Consult/` + `PDCT_Real_Estate/` = client acquisition systems. `VLT_Content/__VLT_OBSVAULT/` = Jordan's knowledge base — READ-ONLY except `PDCT_JO_ED/` where agents may write course content. `AI_BRAIN/` = stable agent priming. `VLT_Content/` = production pipeline. `AI_Tools/` does the work, `.claude/commands/` + `.gemini/commands/` tell you how.

**Gemini CLI:** Slash commands are defined in `.gemini/commands/` — self-contained SOPs with model routing hints.
**Claude CLI:** Slash commands are defined in `.claude/commands/` — same structure, plus Claude-only workflows.

## Rules — VLT_Content/__VLT_OBSVAULT/

**`VLT_Content/__VLT_OBSVAULT/` is READ-ONLY — except `PDCT_JO_ED/` and `PDCT_Real_Estate/`.**

This is Jordan's personal Obsidian knowledge base. Outside of `PDCT_JO_ED/` and `PDCT_Real_Estate/`, you must NEVER:
- Create new files inside `VLT_Content/__VLT_OBSVAULT/`
- Edit, modify, or overwrite any file inside `VLT_Content/__VLT_OBSVAULT/`
- Delete or rename any file inside `VLT_Content/__VLT_OBSVAULT/`
- Move files into or out of `VLT_Content/__VLT_OBSVAULT/`

**Inside `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/` and `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/` you MAY:**
- Create and write course briefs, module scripts, and published outputs
- Follow the `_template/` folder structure for new courses
- Use Obsidian-compatible markdown (frontmatter, `[[wikilinks]]`, callouts)

**Everywhere in vault you MAY:**
- Read files when a workflow or task requires context
- Quote or reference content in your outputs

For all other vault-inspired output, write to the appropriate location (`PDCT_JO_Consult/`, `VLT_Content/`, etc.) — never into the vault outside `PDCT_JO_ED/`.

## Token Economy — Keep Costs Low

Every token costs money. LLMs are stateless — the entire conversation history is resent with every message, compounding costs fast. Apply these rules every session, every response.

### Session Initialization — Never Reload What's Already Loaded

- **CLAUDE.md is auto-injected at session start.** Never re-read it mid-session.
- Don't speculatively load client folders, workflow files, or swipe files "just in case"
- Read the swipe file once per session. If needed again, reference it by path — never re-read
- New session = zero context cost. Only loading files costs tokens. Start clean whenever possible.
- **One phase per session.** Complete a discrete deliverable block, then prompt `/clear`.

### Model Routing — Right Model for Each Task

Switch with `/model` before task blocks. Haiku costs ~20x less than Sonnet. Don't pay Sonnet prices for mechanical work.

| Task | Model |
|------|-------|
| Swipe file build, VSL script, offer sheet, email sequences, DM scripts | Sonnet |
| Strategy, complex reasoning, content audit, session planning | Sonnet |
| Discovery call prep, proposal generation | Sonnet |
| Captions (IG + TikTok), Remotion props, story sequences | Haiku |
| Threads posts (template rewrites), scheduling, shot lists | Haiku |
| Telegram messages (daily/weekly), reminder templates | Haiku |
| Daily brief compilation, inbox triage | Haiku |
| Repurposing (30 posts → 150+ pieces) | **Tool** (`AI_Tools/content_repurpose.py`) locally, or **Modal web UI** if Jordan is away — never inline |

**Rule:** If it's a template rewrite or output that doesn't require deep reasoning → Haiku. If quality and strategy matter → Sonnet.

### Agent Rules (Enforce These Automatically)

**Read only what you need**
- Use Grep/Glob to locate specific sections before reading whole files
- When reading large files, use `offset` and `limit` to pull only the relevant lines
- Never paste large file contents into your response — reference by path instead

**Keep responses tight**
- Answer the question, don't narrate your process
- Skip restating what the user just said
- No filler phrases ("Great question!", "Certainly!", "As you can see...")
- Bullet points over paragraphs for structured info

**Offload to tools, not context**
- Don't reason through data inline when a Python tool can handle it — tools return only the result
- Don't load a workflow file on every turn — read it once, act on it
- Repurposing 30+ content pieces must go through `AI_Tools/content_repurpose.py`, not inline
- If Jordan is away (machine off): use Modal — web UI at https://automatenier--cook-tools-frontend.modal.run or `modal run AI_Tools/cook_modal_app.py` from any machine
- **Multi-step chains:** Use `pipeline.py` when 2+ tools need to run in sequence — saves round-trips and keeps the agent out of intermediate babysitting
  Example: `py -3 AI_Tools/cook_pipeline.py .tmp/pipeline_examples/youtube_to_repurpose.yaml`

**Don't repeat context**
- If a file or fact was established this session, don't re-read or re-quote it
- Reference by filename/line number, not by content

**Targeted tool calls**
- Prefer Grep over Read when searching for a specific value
- Run parallel tool calls when tasks are independent to reduce round-trips

### User-Side Actions (Prompt These at the Right Moment)

| Trigger | What to say |
|---|---|
| Discrete deliverable complete (e.g., proposal done) | "Done — run `/clear` before starting the next deliverable." |
| Phase complete | "Phase done — `/clear` before next phase saves the most tokens." |
| 3+ large files read, or complex reasoning session | "Context is loading up — run `/compact` now before we generate." |
| Switching from strategy to mechanical tasks | "Switch to Haiku with `/model` — this next block is mechanical." |
| Repurposing or Telegram batch coming up | "This goes through the Python tool, not inline — saves ~100K tokens." |

### What to Avoid
- Loading entire client folders speculatively "just in case"
- Running repurpose / Telegram batches as inline Claude generation
- Generating long explanations for simple confirmations
- Re-reading CLAUDE.md mid-session (it's already loaded)
- Creating intermediary markdown summaries of files that can be referenced directly
- Using Sonnet for captions, Remotion props, scheduling, or story sequence rewrites

---

## Bottom Line

You sit between what I want (workflows) and what actually gets done (tools). Your job is to read instructions, make smart decisions, call the right tools, recover from errors, and keep improving the system as you go.

Stay pragmatic. Stay reliable. Keep learning.

---

## Memory & Skills Reference

Persistent knowledge lives in `AI_MEMORY/` inside this project:

| File | What it covers |
|------|---------------|
| `AI_MEMORY/MEMORY.md` | Vault structure, active clients, project layout |
| `AI_MEMORY/obsidian-tracker.md` | Full obsidian-tracker syntax, chart types, colors, working examples, troubleshooting |

**When to read memory files (on-demand only — do not auto-load):**
- User says "load memory" or task requires client/path context → read `AI_MEMORY/MEMORY.md`
- Tracker charts or dashboard task → read `AI_MEMORY/obsidian-tracker.md`
- After learning something new that should persist → write it to the relevant memory file

**Rules for updating memory:**
- Write new learnings immediately after solving a bug or discovering a pattern
- Keep `MEMORY.md` concise — detailed references go in topic files
- Never duplicate content already in CLAUDE.md

---

## Engineering Mode (Epics System)

Use this mode when asked to build or fix a tool, run an audit, or execute an epic brief.

### The Build Loop
1. Check `AI_Tools/` for anything reusable before writing from scratch
2. Write the tool to `AI_Tools/[tool_name].py`
3. Write a test to `AI_Tools/tests/test_[tool_name].py` using mock data
4. Run the test — verify it passes without errors
5. Update the relevant command in `.claude/commands/` (and `.gemini/commands/` if applicable) with any new learnings

### Rules (Non-Negotiable)
- **Never overwrite an existing file without confirming its contents first.** If a file already exists at the target path, check what's in it before writing. If it contains data that isn't yours to replace, write to a new file with a different name and tell Jordan. Untracked in git does NOT mean empty or disposable.
- **When a task says "create a new X", always use a new filename** — never assume an existing file with a similar name is the right target.
- **Backup before touching pipeline trackers** — copy to `.tmp/backup/` before any tracker modification
- **No tool ships without a test** — `AI_Tools/tests/test_[name].py` must exist and pass
- **API keys from `.env` only** — use `os.getenv()`, never hardcode
- **`.env` is READ-ONLY — NEVER touch it.** Do not create, edit, overwrite, delete, or append to `.env` under any circumstance. Only Jordan can modify this file. If a key is missing, tell Jordan — do not attempt to fix it yourself.
- **n8n scripts must output clean JSON to stdout** — so n8n can parse the response
- **Don't break existing workflows** — verify no existing SOPs depend on what you changed

### Scope Boundaries
| Directory | Access |
|-----------|--------|
| `AI_Tools/` | Read + Write — primary build workspace |
| `.claude/commands/` | Read + careful edit only |
| `.gemini/commands/` | Read + careful edit only |
| `.tmp/` | Read + Write — disposable |
| `PDCT_JO_Consult/` | Read + Write |
| `PDCT_Real_Estate/` | Read + Write |
| `VLT_Content/` | Read + Write |
| `AI_BRAIN/` | Read + Write |
| `AI_n8n/` | Read-only — do not modify unless strictly requested |
| `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/` | Read + Write — course content only |
| `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/` | Read + Write — real estate vault content |
| `VLT_Content/__VLT_OBSVAULT/` (rest) | READ-ONLY — never modify |
