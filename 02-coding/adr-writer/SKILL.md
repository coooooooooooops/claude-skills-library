---
name: adr-writer
description: "Write Architecture Decision Records capturing context, options, decision, and consequences. Use when making or documenting technical decisions like stack choice, database, framework, or architecture changes."
---

# Adr Writer

Preserve the reasoning behind technical choices.

## Process

1. Title the decision and set status (proposed, accepted, superseded).
2. Write the context and constraints.
3. List options with pros and cons.
4. State the decision and why.
5. List consequences, risks, and follow-ups.

## Output format

A numbered markdown ADR file (e.g. docs/adr/0007-use-sqlite.md).

## Rules

- Keep to one page.
- Record rejected options; future you will ask.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
