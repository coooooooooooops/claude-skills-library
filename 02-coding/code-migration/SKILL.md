---
name: code-migration
description: "Migrate code between languages, frameworks, or versions (JS to TS, Python 2 to 3, REST to GraphQL, Godot 3 to 4) with parity checks. Use when porting or rewriting."
---

# Code Migration

Port code with behavior parity and a safe cutover.

## Process

1. Inventory features and external dependencies.
2. Map concepts and APIs from source to target.
3. Migrate incrementally with both versions runnable; keep tests as the contract.
4. Run comparison tests on real inputs.
5. Plan cutover and rollback.

## Output format

Mapping table, migration steps, and converted code.

## Rules

- Do not rewrite and redesign simultaneously.
- Keep a parity checklist.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
