---
name: shell-scripting
description: "Write safe, portable bash/zsh scripts and one-liners with error handling and clear usage. Use when the user wants automation, a CLI tool, a cron job, file processing, or help with terminal commands."
---

# Shell Scripting

Write scripts that fail safely and are easy to maintain.

## Process

1. Clarify OS, shell, inputs, and outputs.
2. Start with `set -euo pipefail`, quote variables, and use functions.
3. Add usage/help, argument parsing, and dry-run mode for destructive actions.
4. Use shellcheck-friendly constructs; avoid parsing ls.
5. Provide an example invocation.

## Output format

A complete script with comments and usage.

## Rules

- Warn before destructive commands (rm, dd, mv over existing).
- Prefer simple, portable constructs.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
