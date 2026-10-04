---
name: agent-workflow-designer
description: "Design multi-step AI agent workflows: tools, memory, guardrails, evals, and human checkpoints. Use when building automations or agents."
---

# Agent Workflow Designer

Build agents that are reliable.

## Process

1. Define the job and success metric.
2. Break into steps and decide which need an LLM.
3. Choose tools and define their schemas.
4. Add validation, retries, and human approval for risky actions.
5. Build evals and logs.

## Output format

Workflow diagram and spec.

## Rules

- Keep a human in the loop for irreversible actions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
