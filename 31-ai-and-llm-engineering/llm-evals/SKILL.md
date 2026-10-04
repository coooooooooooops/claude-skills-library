---
name: llm-evals
description: "Build evaluation suites for LLM apps: test sets, graders, regressions, and metrics. Use when measuring prompt or model changes."
---

# Llm Evals

Build evaluation suites for LLM apps: test sets, graders, regressions, and metrics.

## Process

1. Collect real examples
2. define success criteria
3. write graders
4. run on every change
5. track regressions

## Output format

Eval harness.

## Rules

- No eval, no shipping prompt changes.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
