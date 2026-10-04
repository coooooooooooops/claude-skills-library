---
name: skill-builder
description: "Design and write new Claude skills: purpose, trigger description, instructions, resources, and tests. Use when the user wants to create or improve a skill."
---

# Skill Builder

Create skills that trigger reliably and work well.

## Process

1. Clarify what the skill does and when it should trigger.
2. Write a pushy, specific description listing contexts.
3. Write concise step-by-step instructions with output format and rules.
4. Add references or scripts only when needed.
5. Create 3 test prompts and iterate.

## Output format

A complete skill folder with SKILL.md.

## Rules

- Keep SKILL.md under about 500 lines.
- Put trigger info in the description.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
