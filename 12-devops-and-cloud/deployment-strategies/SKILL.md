---
name: deployment-strategies
description: "Choose and implement deployment strategies: rolling, blue/green, canary, and feature flags. Use when planning releases with minimal downtime and easy rollback."
---

# Deployment Strategies

Choose and implement deployment strategies: rolling, blue/green, canary, and feature flags.

## Process

1. Assess risk and traffic
2. select strategy
3. define health checks and success metrics
4. automate rollback triggers
5. plan database migration compatibility

## Output format

Rollout plan with rollback steps.

## Rules

- Make schema changes backward compatible across versions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
