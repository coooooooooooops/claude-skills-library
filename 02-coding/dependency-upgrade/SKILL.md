---
name: dependency-upgrade
description: "Plan and execute dependency and framework upgrades safely: changelog review, breaking changes, codemods, staged rollout. Use when upgrading packages, languages, or frameworks, or when audit warnings appear."
---

# Dependency Upgrade

Upgrade without breaking production.

## Process

1. Inventory current and target versions; read changelogs for breaking changes.
2. Upgrade in small batches, starting with low-risk patches and minors.
3. Run tests, linters, and type checks after each batch.
4. Apply codemods and fix deprecations.
5. Document the changes and a rollback plan.

## Output format

Upgrade plan, command list, breaking-change checklist, and rollback steps.

## Rules

- Pin versions and commit lockfiles.
- Never upgrade everything at once.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
