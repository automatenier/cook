---
tags:
  - consulting
---
# Navigation Flow — How Everything Connects

> Visualisasi bagaimana kamu navigate antara Obsidian (creative), VS Code/Cook (agent), dan automations (n8n) saat fulfilled satu client.

---

## The Two Workspaces

```
┌─────────────────────────────────┐     ┌──────────────────────────────────┐
│        OBSIDIAN (Creative)      │     │      VS CODE / COOK (Agent)      │
│                                 │     │                                  │
│  You write, you think, you      │     │  Claude executes, generates,     │
│  create in flow state.          │     │  repurposes, deploys.            │
│                                 │     │                                  │
│  - Content writing              │     │  - Script generation             │
│  - VSL scripting                │     │  - Offer agent                   │
│  - Strategy brainstorming       │     │  - Content repurposing           │
│  - Client notes                 │     │  - Remotion rendering            │
│  - Reference reading            │     │  - File organization             │
│  - Creative direction           │     │  - n8n workflow triggers          │
│                                 │     │                                  │
│  📂 SecondBrainObsidian/        │     │  📂 Cook/                        │
│  (READ-ONLY for agent)          │     │  (Full agent access)             │
└─────────────────────────────────┘     └──────────────────────────────────┘
```

---

## New Client: Full Flow (Day 0 → Day 14)

```
CLIENT SIGNS
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ VS CODE: Create folders + send welcome                         │
│                                                                 │
│ Claude: "Create folders for @busyfit"                           │
│   → content/clients/busyfit/ (brief, checklist, a_roll, etc.)  │
│   → Fulfillment/_CLIENT_DELIVERABLES/busyfit/                  │
│                                                                 │
│ n8n: Auto-send welcome email + Telegram channel setup           │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ VA: Collect onboarding data + materials                         │
│   → Upload to GDrive → Organize to Cook folders                 │
│   → Notify Jordan: "Data complete"                              │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ VS CODE: Generate offer sheet                                   │
│                                                                 │
│ Claude: python tools/offer_agent.py --from-file onboarding.json │
│   → Fulfillment/_OFFER_BLUEPRINT/offer_sheets/busyfit/          │
│   → Client reviews + approves                                   │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ REAL WORLD: Filming session (2 hours)                           │
│   → VA organizes footage to:                                    │
│     content/clients/busyfit/a_roll/                              │
│     content/clients/busyfit/footage/                             │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ VS CODE: Content production sprint                              │
│                                                                 │
│ Step 1: Find viral ref → Gemini analyzes → swipe_file JSON     │
│                                                                 │
│ Step 2: Claude: "Create reel for @busyfit using swipe #3"       │
│   Reads: swipe_file → client_brief → footage_checklist          │
│   Outputs: projects/260217_hook-busy-mom/brief.md               │
│                                                                 │
│ Step 3: Remotion renders draft → CapCut polishes                │
│                                                                 │
│ Step 4: Claude: "Repurpose brief at .../brief.md"               │
│   Outputs: repurposed.json (Threads, newsletter, YT, stories)  │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ OBSIDIAN: Your creative work                                    │
│                                                                 │
│ You open CapCut with the brief as shot list                     │
│ You edit in creative flow — music, transitions, grading         │
│ You write personal touches that AI can't replicate              │
│ You direct the "feel" of the content                            │
│                                                                 │
│ Export → content/clients/busyfit/projects/[slug]/export/         │
└─────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ n8n: Automation handles distribution                            │
│                                                                 │
│ → Schedule posts (IG, TikTok, Threads)                          │
│ → Trigger WA reminders                                          │
│ → Update Telegram progress channel                              │
│ → Monitor keyword CTA triggers                                  │
│ → Daily setter report collection                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Content Creation Cycle (Ongoing)

```
                  ┌──────────────────┐
                  │  FIND VIRAL REF  │
                  │  (Scroll + Save) │
                  └────────┬─────────┘
                           │
                  ┌────────▼─────────┐
                  │  GEMINI ANALYZE  │
                  │  Structure → JSON│
                  └────────┬─────────┘
                           │
              ┌────────────▼────────────┐
              │  VS CODE: CLAUDE WRITES │
              │  Brief with filenames   │
              │  using swipe + client   │
              │  brief + footage list   │
              └────────────┬────────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
     ┌────────▼────────┐    ┌──────────▼──────────┐
     │  REMOTION DRAFT  │    │  CAPCUT (YOU)       │
     │  Auto-render     │    │  Creative editing   │
     │  from brief      │    │  in Obsidian flow   │
     └────────┬─────────┘    └──────────┬──────────┘
              │                         │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  VS CODE: REPURPOSE     │
              │  1 reel → 7 pieces      │
              │  Threads, Newsletter,   │
              │  YT, TikTok, Stories    │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  PUBLISH (n8n + manual) │
              └─────────────────────────┘
```

---

## File Navigation Map

### When you open VS CODE (Cook/):

```
Cook/
├── workflows/          ← READ FIRST: How to do anything
│   ├── content_creation.md
│   ├── setter_dm_outreach.md
│   └── client_fulfillment.md
│
├── content/            ← CONTENT PRODUCTION HUB
│   ├── swipe_file/     ← Viral structure library (Gemini JSONs)
│   ├── clients/        ← Per-client: brief, footage, assets, projects
│   ├── library/        ← Hooks, CTAs, script templates
│   └── strategy/       ← Viral checklist, idea gen, bio setup
│
├── Fulfillment/        ← CLIENT DELIVERABLES
│   ├── _ONBOARDING/    ← All SOPs, roadmaps, templates
│   │   ├── client_14day_roadmap.md      ← Client sees this
│   │   ├── team_roadmap_va.md           ← VA follows this
│   │   ├── team_roadmap_setter.md       ← Setter follows this
│   │   ├── team_roadmap_editor.md       ← Editor follows this
│   │   ├── setter_scripts_master.md     ← All 8 setter scripts
│   │   ├── va_setup_sop.md              ← VA toolstack + setup
│   │   ├── client_self_execution_map.md ← What clients do
│   │   ├── vsl_presentation_template.md ← Client fills VSL structure
│   │   ├── new_client_folder_generator.md ← Folder creation guide
│   │   └── navigation_flow.md           ← THIS FILE
│   ├── _OFFER_BLUEPRINT/   ← Offer sheets, close reports
│   ├── _CONTENT_AUDIT/     ← Audit templates + reports
│   ├── _LEAD_ACTIVATION/   ← Reactivation scripts
│   └── _CLIENT_DELIVERABLES/ ← Per-client output folders
│
├── tools/              ← PYTHON SCRIPTS (Claude executes)
│   ├── offer_agent.py
│   ├── analyze_viral_reel.py
│   ├── repurpose_content.py
│   └── create_excel_crm.py
│
├── n8n/                ← AUTOMATION WORKFLOWS
│   ├── _JORDAN/        ← Personal systems
│   ├── _HTS_AGENCY/    ← Agency automations
│   ├── _JO_CONSULT/    ← JO Consult forms, invoicing
│   └── _CLIENT_SYSTEMS/ ← Delivered to clients
│
└── remotion/           ← VIDEO TEMPLATES
    └── src/
        ├── ValueCTAReel.tsx
        └── AuthenticityReel.tsx
```

### When you open OBSIDIAN (SecondBrainObsidian/):

```
SecondBrainObsidian/          ← YOUR CREATIVE SPACE (read-only for agent)
├── A Master Prompts/         ← Prompt templates (brand sheet, offer, audit)
├── A Result/                 ← Generated outputs
├── B Other Resour/           ← Supporting resources
├── Operations/               ← Dashboard, project tracking, SOPs
├── Brainstorms/              ← Ideation and strategy
└── Trainerize Recreate/      ← Platform notes
```

---

## The Hybrid Model: Who Does What

```
┌────────────────────────────────────────────────────────────────┐
│                    JORDAN (You)                                │
│                                                                │
│  Creative Direction  │  Strategy  │  Client Relationships     │
│  CapCut editing      │  Filming   │  Consultation calls       │
│  Voice/tone review   │  Approvals │  New offer design          │
│                                                                │
│  WORKS IN: Obsidian + CapCut + Google Meet                    │
└────────────────────────────────────────────────────────────────┘
                           │
                           │ Instructs
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                 CLAUDE (Agent)                                  │
│                                                                │
│  Script generation   │  Offer sheets  │  Content repurposing  │
│  Brief creation      │  Audit reports │  File organization     │
│  Remotion props      │  Email drafts  │  Strategy docs         │
│                                                                │
│  WORKS IN: VS Code / Cook (tools/ + workflows/)               │
└────────────────────────────────────────────────────────────────┘
                           │
                           │ Triggers
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                    n8n (Automation)                             │
│                                                                │
│  Welcome emails      │  WA reminders    │  Telegram channels  │
│  Form collection     │  Invoicing       │  EOD report bots    │
│  Calendar booking    │  Keyword CTA     │  Error alerts        │
│  Post scheduling     │  Lead scoring    │  Dashboard updates   │
│                                                                │
│  RUNS: Always-on background (self.n8n.cloud)                  │
└────────────────────────────────────────────────────────────────┘
                           │
                           │ Supports
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                      TEAM                                      │
│                                                                │
│  VA: Organize, coordinate, follow up, setup                   │
│  Setter: DM outreach, qualify, book calls                     │
│  Editor: CapCut polish, final exports                         │
│                                                                │
│  USES: GDrive, Telegram, Google Sheets, Instagram              │
└────────────────────────────────────────────────────────────────┘
```

---

## Typical Session: "I just got a new client, what do I do?"

1. **Open VS Code** → Run folder generator for new client
2. **Claude** → Creates folders, copies templates
3. **VA** → Sends welcome email, collects onboarding data
4. **Claude** → Generates offer sheet from onboarding data
5. **You** → Review offer sheet, schedule filming
6. **Real World** → Film A-roll + VSL (2 hours)
7. **VA** → Organizes footage to proper folders
8. **Claude** → Generates 30 reel scripts + content calendar
9. **You in Obsidian** → Open CapCut, edit reels in flow state
10. **Claude** → Repurpose each piece into 7 formats
11. **n8n** → Schedule posts, trigger reminders, track keywords
12. **Setter** → Start DM outreach using scripts
13. **Day 14** → Consultation call, launch lead magnet, handoff

---

## Quick Launch Commands

| Want to... | Do this |
|------------|---------|
| Create client folders | `Claude: "Create folders for @[client]"` |
| Generate offer sheet | `python tools/offer_agent.py --from-file [onboarding.json]` |
| Write a reel script | `Claude: "Create reel for @[client] using swipe #[X]"` |
| Repurpose content | `python tools/repurpose_content.py [brief.md] --type reel-value` |
| Analyze viral reel | `python tools/analyze_viral_reel.py [notes.md]` |
| Check workflows | Read `workflows/[name].md` |
| Onboard setter | Share `Fulfillment/_ONBOARDING/setter_scripts_master.md` |
| Onboard VA | Share `Fulfillment/_ONBOARDING/va_setup_sop.md` |
| Give client roadmap | Share `Fulfillment/_ONBOARDING/client_14day_roadmap.md` |
