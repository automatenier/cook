---
category: learning
status: evergreen
rating: 6
tags: [ai, claude, systems, tools]
created: 2026-02-21
source: direct experience
---

# Claude Code Outperforms Inline AI for Deterministic Tasks

## What this means
When a task has a correct/incorrect outcome (data transformation, file operations, API calls, CRM updates), running it through a Python tool returns a deterministic result. Asking Claude to reason through it inline introduces variability and inflates context cost.

## Why it matters for my work
Every repurposing session, CRM update, or content batch that runs inline costs ~100K tokens and degrades in quality by step 5. The same task through `repurpose_content.py` runs once, returns clean output, and costs near-zero reasoning tokens.

## The rule I use now
> If the output is mechanical and testable → route to a Python tool.
> If it requires judgement and creativity → use Claude inline.

## Evidence
- Repurposing 30 posts inline: ~3 hours, inconsistent quality
- Same via `tools/repurpose_content.py`: ~4 minutes, consistent schema

## Connects to
- [[WAT Framework Makes Agency Work Scalable]]
- [[Content]]
- [[Content System]]
