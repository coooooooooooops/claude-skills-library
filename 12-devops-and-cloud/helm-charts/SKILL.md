---
name: helm-charts
description: "Create and maintain Helm charts with templated values, helpers, and environment overrides. Use when packaging apps for Kubernetes or fixing chart templating errors."
---

# Helm Charts

Create and maintain Helm charts with templated values, helpers, and environment overrides.

## Process

1. Scaffold chart
2. parameterize via values.yaml
3. add helpers and named templates
4. add per-environment value files
5. lint and template-render before install

## Output format

Chart structure, values files, and install commands.

## Rules

- Keep templates readable; avoid logic-heavy templating.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
