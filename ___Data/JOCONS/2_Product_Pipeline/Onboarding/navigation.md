---
tags:
  - navigation
  - workflow
---
# Navigation Flow — How The VLT Connects

> A visualization of how you navigate between your creative vault (Obsidian) and your content factory (VS Code).

---

## The Two Workspaces

```
┌─────────────────────────────────┐     ┌──────────────────────────────────┐
│      @VLT_Content/__VLT_OBSVAULT (Creative)   │     │      @VLT_Content (Execution)    │
│                                 │     │                                  │
│  You write, you think, you      │     │  The AI Agent executes, builds,  │
│  strategize in flow state.      │     │  and deploys content.            │
│                                 │     │                                  │
│  - Strategy Brainstorming       │     │  - Script Generation             │
│  - Long-form Writing            │     │  - Project Brief Creation        │
│  - Client Notes & Insights      │     │  - Content Repurposing           │
│  - Reference Material           │     │  - Automated Rendering           │
│  - Creative Direction           │     │  - File Organization             │
│                                 │     │  - Automation Triggers           │
│                                 │     │                                  │
│  📂 VLT_Content/__VLT_OBSVAULT/               │     │  📂 VLT_Content/                 │
│  (READ-ONLY for agent)          │     │  (Full agent access)             │
└─────────────────────────────────┘     └──────────────────────────────────┘
```

---

## Primary Workflow: [New Project/Content Title]

> Replace this with your most common, end-to-end workflow.

```
[STARTING_TRIGGER]
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: [ACTION IN VS CODE / TERMINAL]                          │
│                                                                 │
│ Command: "Do the first thing for @[project_name]"               │
│   → Creates: path/to/new/folders/                               │
│   → Triggers: [Automation tool, e.g., n8n] workflow             │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: [MANUAL OR VA ACTION]                                   │
│                                                                 │
│   → Action: Collects assets, data, or materials.                │
│   → Delivers to: path/to/project/assets/                        │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: [AI AGENT ACTION IN VS CODE]                            │
│                                                                 │
│ Command: python tools/script_name.py --input [source_file]      │
│   → Reads: project briefs, assets, templates                    │
│   → Outputs: path/to/generated_deliverable.md                   │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: [YOUR CREATIVE WORK IN OBSIDIAN]                        │
│                                                                 │
│ You open [Creative Tool, e.g., CapCut] with the generated brief │
│ You perform the creative tasks that AI cannot replicate.        │
│ You direct the final "feel" and polish the output.              │
│                                                                 │
│ Export → path/to/final/export/                                  │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: [AUTOMATION OR DISTRIBUTION]                            │
│                                                                 │
│ → [Automation Tool] handles publishing, notifications, etc.     │
│ → Final deliverables are archived.                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## File Navigation Map

> IMPORTANT: Replace the placeholder structure below with your actual file tree.

### When you open VS CODE (@VLT_Content/):

```
VLT_Content/
├── workflows/          ← READ FIRST: How to do anything
│   ├── navigation.md   ← THIS FILE
│   └── [your_sop_1].md
│
├── projects/           ← ACTIVE WORK & PRODUCTION HUB
│   ├── [project_name_1]/
│   └── [project_name_2]/
│
├── library/            ← Reusable assets, templates, swipes
│   ├── hooks/
│   └── templates/
│
├── tools/              ← PYTHON SCRIPTS (AI Agent executes)
│   ├── [script_1].py
│   └── [script_2].py
│
├── n8n/                ← AUTOMATION WORKFLOWS
│   └── [workflow_1].json
│
└── deliverables/       ← Final, client-ready outputs
    └── [project_name_1]/
```

### When you open OBSIDIAN (@VLT_Content/__VLT_OBSVAULT/):

```
VLT_Content/__VLT_OBSVAULT/           ← YOUR CREATIVE & STRATEGIC SPACE
├── 10_Areas/           ← High-level life/business areas
├── 20_Projects/        ← Active project thinking space
├── 30_Resources/       ← Notes, articles, research
├── 40_Archives/        ← Completed projects and old notes
└── 99_Meta/            ← Templates, dashboards, SOPs
```

---

## The Hybrid Model: Who Does What

```
┌────────────────────────────────────────────────────────────────┐
│                    [YOUR NAME] (Strategist)                    │
│                                                                │
│  Creative Direction │  Strategy      │  Final Review           │
│  [Your Tool #1]     │  [Your Tool #2]│  Client Relationships   │
│                                                                │
│  WORKS IN: Obsidian + [Your Creative Software]                 │
└────────────────────────────────────────────────────────────────┘
                           │
                           │ Instructs
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                 [AI AGENT] (Executor)                          │
│                                                                │
│  Drafting            │  File Org      │  Repurposing          │
│  Brief Creation      │  Data Proc     │  Initial Assembly       │
│                                                                │
│  WORKS IN: VS Code / VLT_Content (tools/ + workflows/)         │
└────────────────────────────────────────────────────────────────┘
                           │
                           │ Triggers
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                    [AUTOMATION TOOL] (Automator)               │
│                                                                │
│  Notifications       │  Publishing    │  Data Entry           │
│  Reminders           │  Invoicing     │  Report Generation    │
│                                                                │
│  RUNS: Always-on background service                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Quick Commands & Actions

| Want to... | Do this |
|------------|---------|
| Start a new project | `[Your Command Here]` |
| Generate a script | `python tools/[script_name].py --input [source]` |
| Repurpose content | `[Your Command Here]` |
| Check a workflow | Read `workflows/[name].md` |
| Find a template | Look in `library/templates/` |