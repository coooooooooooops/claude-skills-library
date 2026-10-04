---
name: ci-cd-pipeline
description: "Design CI/CD pipelines (GitHub Actions, GitLab CI) with lint, test, build, cache, release, and deploy stages. Use when the user wants automation on push, automated releases, or deployment."
---

# Ci Cd Pipeline

Automate the path from commit to production.

## Process

1. Define stages: lint, type-check, test, build, security scan, release, deploy.
2. Use caching and matrix builds for speed.
3. Protect secrets; use environments and approvals for production.
4. Add semantic versioning and changelog automation if wanted.
5. Provide the workflow file.

## Output format

A working workflow YAML plus notes on required secrets.

## Rules

- Fail fast; keep pipelines under ~10 minutes.
- Never echo secrets.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
