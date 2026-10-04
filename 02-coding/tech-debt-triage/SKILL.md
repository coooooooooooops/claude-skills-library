---
name: tech-debt-triage
description: "Inventory and prioritize technical debt by impact, effort, and risk, and turn it into an actionable plan. Use when a codebase feels messy, slow to change, or the user asks what to fix first."
---

# Tech Debt Triage

Pay down the debt that actually hurts.

## Process

1. Collect pain points: slow areas, flaky tests, scary files, repeated bugs.
2. Score each by impact, frequency, effort, and risk.
3. Plot quick wins vs. big bets.
4. Create a sequenced plan with owners and timeboxes.
5. Define how to prevent new debt (lint rules, templates, reviews).

## Output format

Prioritized debt table and a 30/60/90-day plan.

## Rules

- Tie debt to business or velocity impact.
- Do not propose rewrites lightly.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
