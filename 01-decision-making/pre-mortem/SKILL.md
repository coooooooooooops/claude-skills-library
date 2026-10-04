---
name: pre-mortem
description: "Run a pre-mortem: assume the plan already failed and work backwards to find why. Use before launching a project, committing to a plan, starting a build, or whenever the user says 'what could go wrong', 'stress test this', 'risks', or shares a plan to review."
---

# Pre Mortem

Surface hidden risks early by imagining failure has already happened.

## Process

1. Restate the plan and the success definition.
2. Declare: 'It is 6 months later and this failed badly.' Brainstorm 10+ distinct causes across people, tech, market, timing, money, and dependencies.
3. Cluster causes and rate each by likelihood (L/M/H) and impact (L/M/H).
4. For the top 5 risks, define an early-warning signal and a cheap mitigation.
5. Identify any 'kill criteria': conditions under which to stop or pivot.

## Output format

Risk table (risk, likelihood, impact, signal, mitigation) plus 3 kill criteria and the first action to take this week.

## Rules

- Include at least one uncomfortable risk the user probably did not want to hear.
- Prefer specific causes over generic ones ('API quota exhausted at 1k users' beats 'technical issues').
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
