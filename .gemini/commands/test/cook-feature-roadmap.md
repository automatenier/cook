> **Model: Sonnet** -- strategy and ICE prioritization

# Workflow: Feature Roadmap

When user asks to `/feature-roadmap [ProductName]`:

1. **Collect Features**: For each, capture name, problem it solves, user type, Effort (L/M/H), Impact (L/M/H).
2. **Score & Prioritize** (ICE: Impact x Confidence / Effort):
   | Feature | Impact | Confidence | Effort | ICE Score |
   |---|---|---|---|---|
3. **Build Roadmap**:

---
## [ProductName] -- Roadmap

### Now (This Month)
### Next (2-3 Months)
### Later (Backlog)
### Won't Do
---

4. **Save**: `AI_BRAIN/roadmaps/[ProductName]_roadmap_[Date].md`
5. **Feature Specs**: For each "Now" feature: `.tmp/features/[ProductName]_[Feature].md` (problem, solution, acceptance criteria, open questions)

```bash
/feature-roadmap cook-tools
```
