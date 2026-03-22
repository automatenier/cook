> **Model: Sonnet** -- course scripting requires pedagogical structure

# Workflow: Course Module

When user asks to `/course-module [CourseName] [ModuleNumber]`:

1. **Read Course Brief**: `VLT_OBSVAULT/PDCT_JO_ED/courses/[CourseName]/brief.md`
2. **Locate Module Slot**: Find Module [N] -- confirm title, objective, arc position.
3. **Script the Module**:

---
## Module [N] -- [Title]

### Learning Objective
By the end of this module, the student will be able to: [specific action]

### Hook (0:00-0:30)
[Pain point, bold claim, or surprising fact]

### Core Content
**Section 1:** [Key points - 1-2 sentences]
**Section 2:** [Key points]
**Section 3:** [Key points]

### The Framework / System
[Name the method -- 3 steps, acronym, etc.]

### Real Example
[One concrete case study that proves the framework works]

### Summary
[3 bullet takeaways max]

### Action Step
[One specific thing they do before the next module]
---

4. **Save**: `VLT_OBSVAULT/PDCT_JO_ED/courses/[CourseName]/modules/[N]_[title].md`
5. **Update Brief**: Mark Module [N] as "Scripted" in `brief.md`.

```bash
/course-module ai-automation 3
# Output: VLT_OBSVAULT/PDCT_JO_ED/courses/ai-automation/modules/3_title.md
```
