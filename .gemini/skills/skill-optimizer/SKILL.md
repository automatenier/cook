---
name: skill-optimizer
description: Self-improving automation for skills. Research best practices, update SKILL.md files, and run evaluations using Google Workspace tools.
---

# Skill Optimizer

Move beyond manual prompt engineering by letting the agent research, test, and optimize its own skills.

## Workflow

1.  **Identify Target**: Choose a skill to optimize (e.g., `source-analyst`, `pptx-generator`).
2.  **Autoresearch**:
    - Use `google_web_search` to find "best practices for [Task] AI prompts".
    - Use `web_fetch` to extract specific workflow steps from high-quality sources.
3.  **Update Skill**:
    - Read the existing `.gemini/skills/[Skill Name]/SKILL.md`.
    - Synthesize the research into an improved `Workflow` and `Instructions`.
    - Overwrite the skill file with the optimized version.
4.  **Evaluate (Evals)**:
    - Load test cases from the "Optimization Evals" Google Sheet.
    - Run the skill against those cases.
    - Grade the output using criteria and log the results back to the Sheet.

## Tools

### Run Autoresearch Loop

```bash
py -3 AI_Tools/skill_optimizer_loop.py --skill <skill_name> --eval_sheet <sheet_id>
```

### Grade Skill Output

```bash
py -3 AI_Tools/skill_grader.py --input <test_input> --output <skill_output> --criteria <criteria_text>
```
