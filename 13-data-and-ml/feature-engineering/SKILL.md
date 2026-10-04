---
name: feature-engineering
description: "Create and select features that improve models: encoding, scaling, interactions, and time features. Use when improving model performance on tabular data."
---

# Feature Engineering

Create and select features that improve models: encoding, scaling, interactions, and time features.

## Process

1. Understand the domain
2. encode categoricals
3. create ratios, lags and aggregates
4. avoid leakage
5. test importance and prune

## Output format

Feature list with code.

## Rules

- Prevent target leakage; split before computing aggregates.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
