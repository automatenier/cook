---
description: Plans and scripts a single course module for JO Ed.
tags:
  - workflow
---

# Workflow: Course PDCT_MODULES

When user asks to `/course-module [CourseName] [PDCT_MODULESNumber]`:

1. **Read Course Brief**: Open `11_JO_Ed/courses/[CourseName]/brief.md`. Understand the course promise, avatar, and module outline.

2. **Locate PDCT_MODULES Slot**: Find PDCT_MODULES [PDCT_MODULESNumber] in the outline. Confirm:
   - PDCT_MODULES title
   - Key learning objective (what can they DO after this module?)
   - Where it sits in the transformation arc

3. **Script the PDCT_MODULES** using this structure:

---
## PDCT_MODULES [N] — [Title]

### Learning Objective
By the end of this module, the student will be able to: [specific action]

### Hook (0:00–0:30)
[Open with a pain point, bold claim, or surprising fact that makes them need to watch]

### Core Content
**Section 1: [Sub-topic]**
[Key points — keep each to 1-2 sentences, no fluff]

**Section 2: [Sub-topic]**
[Key points]

**Section 3: [Sub-topic]**
[Key points]

### The Framework / System
[Name the method. Give it a memorable structure (3 steps, acronym, etc.)]

### Real Example
[One concrete case study or demo that proves the framework works]

### Summary
[3 bullet takeaways max]

### Action Step
[One specific thing they do before the next module]

### Teaser for Next PDCT_MODULES
[1 sentence that makes them want to continue]
---

4. **Save PDCT_MODULES**: Write to `11_JO_Ed/courses/[CourseName]/modules/[N]_[title].md`.

5. **Update Brief**: Mark PDCT_MODULES [N] status as "Scripted" in `11_JO_Ed/courses/[CourseName]/brief.md`.

## Tool Invocation Examples

```bash
# Trigger this workflow
/course-module ai-automation 3

# Output location
# 11_JO_Ed/courses/ai-automation/modules/3_title.md

# Run sequentially for all modules
/course-module ai-automation 1
/course-module ai-automation 2
/course-module ai-automation 3
```
