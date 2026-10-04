---
name: claude-md-writer
description: "Write CLAUDE.md or project instruction files so coding agents understand the repo: commands, architecture, conventions. Use when setting up a project for Claude Code or similar agents."
---

# Claude Md Writer

Give agents the context a new teammate needs.

## Process

1. Summarize what the project is.
2. List build, test, and run commands.
3. Describe architecture and key directories.
4. State conventions and pitfalls.
5. Keep it concise and current.

## Output format

A CLAUDE.md file.

## Rules

- Only include things that save time.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
