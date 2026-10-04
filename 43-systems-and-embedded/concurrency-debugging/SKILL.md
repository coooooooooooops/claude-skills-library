---
name: concurrency-debugging
description: "Find and fix race conditions, deadlocks, and thread-safety bugs. Use when behavior is non-deterministic."
---

# Concurrency Debugging

Find and fix race conditions, deadlocks, and thread-safety bugs.

## Process

1. Identify shared state
2. reproduce with stress
3. use thread sanitizers
4. apply locks or immutability
5. add tests

## Output format

Root cause and fix.

## Rules

- Prefer eliminating shared mutable state.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
