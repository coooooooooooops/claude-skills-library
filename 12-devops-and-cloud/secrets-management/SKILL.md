---
name: secrets-management
description: "Manage secrets safely with vaults, environment variables, rotation, and scanning. Use when handling API keys, passwords, or fixing a leaked secret."
---

# Secrets Management

Manage secrets safely with vaults, environment variables, rotation, and scanning.

## Process

1. Inventory secrets
2. move them to a manager such as Vault or cloud secrets
3. inject at runtime
4. rotate regularly
5. add pre-commit scanning
6. revoke anything leaked

## Output format

Secrets handling plan and leak-response steps.

## Rules

- Treat any committed secret as compromised and rotate it.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
