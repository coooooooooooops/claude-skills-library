---
name: refactor-safely
description: "Refactor code in small, behavior-preserving steps with tests as a safety net. Use when the user wants to clean up, restructure, simplify, deduplicate, or modernize existing code."
---

# Refactor Safely

Improve structure without changing behavior.

## Process

1. Identify the smell and the goal (readability, testability, performance, extensibility).
2. Confirm or create characterization tests that pin current behavior.
3. Plan a sequence of tiny refactors (rename, extract, inline, move, replace conditional).
4. Apply one step at a time and re-run tests after each.
5. Summarize what changed and what is now easier.

## Output format

Step list with before/after snippets and the final cleaned code.

## Rules

- No feature changes mixed into refactors.
- If there are no tests, write them first or flag the risk clearly.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
