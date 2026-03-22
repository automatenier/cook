---
description: Organizes and prioritizes features for a JO Ventures product roadmap.
tags:
  - workflow
---

# Workflow: Feature Roadmap

When user asks to `/feature-roadmap [ProductName]`:

1. **Locate Product Folder**: Check `12_JO_Ventures/features/` for existing feature files for [ProductName]. Check `12_JO_Ventures/roadmaps/[ProductName].md` if it exists.

2. **Collect Features**: Ask user to list or confirm all known features. For each, capture:
   - Feature name
   - What problem it solves
   - Who needs it (user type)
   - Effort estimate (Low / Medium / High)
   - Impact estimate (Low / Medium / High)

3. **Score & Prioritize** using ICE scoring (Impact × Confidence ÷ Effort):

   | Feature | Impact | Confidence | Effort | ICE Score | Priority |
   |---|---|---|---|---|---|
   | [Feature 1] | | | | | |
   | [Feature 2] | | | | | |

4. **Build Roadmap** in 3 horizons:

---
## [ProductName] — Roadmap

### Now (This Month)
- [Feature A] — [why it's first]
- [Feature B]

### Next (Next 2-3 Months)
- [Feature C]
- [Feature D]

### Later (Backlog)
- [Feature E]
- [Feature F]

### Won't Do (Decided Against)
- [Feature X] — reason: [why]
---

5. **Save Roadmap**: Write to `12_JO_Ventures/roadmaps/[ProductName]_roadmap_[Date].md`.

6. **Save Individual Feature Specs**: For each "Now" priority feature, create a spec file at `12_JO_Ventures/features/[ProductName]_[FeatureName].md` with: problem, solution, acceptance criteria, and open questions.

## Tool Invocation Examples

```bash
# Trigger this workflow
/feature-roadmap cook-tools

# Output locations
# 12_JO_Ventures/roadmaps/cook-tools_roadmap_2026-02-27.md
# 12_JO_Ventures/features/cook-tools_ToolRegistry.md
# 12_JO_Ventures/features/cook-tools_PipelineComposer.md
```
