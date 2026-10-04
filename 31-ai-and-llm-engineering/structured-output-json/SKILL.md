---
name: structured-output-json
description: "Get reliable JSON from LLMs with schemas, validation, and repair loops. Use when parsing model output."
---

# Structured Output Json

Get reliable JSON from LLMs with schemas, validation, and repair loops.

## Process

1. Define a JSON schema
2. instruct and give examples
3. validate output
4. retry with error feedback
5. handle refusals

## Output format

Prompt and validator code.

## Rules

- Always validate model output.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
