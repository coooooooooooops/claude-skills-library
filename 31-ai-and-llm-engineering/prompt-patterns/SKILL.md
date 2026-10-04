---
name: prompt-patterns
description: "Apply prompting patterns: few-shot, chain of thought, structured output, and role setup. Use when improving model reliability."
---

# Prompt Patterns

Apply prompting patterns: few-shot, chain of thought, structured output, and role setup.

## Process

1. Define the task
2. add examples
3. request structured output
4. add constraints
5. test edge cases

## Output format

Prompt templates.

## Rules

- Examples beat long instructions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
