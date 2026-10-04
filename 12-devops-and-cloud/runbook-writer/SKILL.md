---
name: runbook-writer
description: "Create operational runbooks with symptoms, diagnosis steps, commands, and escalation paths. Use when documenting how to operate or recover a service."
---

# Runbook Writer

Create operational runbooks with symptoms, diagnosis steps, commands, and escalation paths.

## Process

1. Define the alert or scenario
2. list quick checks
3. write step-by-step fixes with commands
4. add escalation contacts and rollback
5. test the runbook

## Output format

A runbook ready for on-call use.

## Rules

- Every step must be executable by someone unfamiliar with the system.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
