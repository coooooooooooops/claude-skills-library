---
name: data-warehouse-modeling
description: "Model warehouses with star schemas, dimensions, facts, and slowly changing dimensions. Use when designing analytics databases or dbt projects."
---

# Data Warehouse Modeling

Model warehouses with star schemas, dimensions, facts, and slowly changing dimensions.

## Process

1. List business processes
2. define grain
3. design facts and dimensions
4. handle SCD types
5. layer staging, intermediate and marts

## Output format

Schema diagram and dbt layout.

## Rules

- Declare the grain before designing columns.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
