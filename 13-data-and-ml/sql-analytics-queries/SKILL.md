---
name: sql-analytics-queries
description: "Write analytics SQL: window functions, cohorts, funnels, retention, and rolling metrics. Use when the user needs business metrics from a database."
---

# Sql Analytics Queries

Write analytics SQL: window functions, cohorts, funnels, retention, and rolling metrics.

## Process

1. Confirm tables and grain
2. write CTEs step by step
3. use window functions for ranking and running totals
4. validate against a manual sample

## Output format

Commented SQL and expected output shape.

## Rules

- Define the grain of every table before joining.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
