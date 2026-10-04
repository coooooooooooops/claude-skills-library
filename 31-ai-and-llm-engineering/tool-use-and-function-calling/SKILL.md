---
name: tool-use-and-function-calling
description: "Design tools for LLM function calling: schemas, descriptions, error handling, and safety. Use when giving models actions."
---

# Tool Use And Function Calling

Design tools for LLM function calling: schemas, descriptions, error handling, and safety.

## Process

1. Define narrow tools
2. write clear descriptions and schemas
3. return structured errors
4. limit permissions
5. log calls

## Output format

Tool definitions.

## Rules

- Keep humans in the loop for irreversible actions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
