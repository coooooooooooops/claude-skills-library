---
name: git-commit-pr
description: "Write clean commit messages, branch strategy, and pull request descriptions, and fix common git messes. Use when the user mentions commit, PR, rebase, merge conflict, git history, or asks how to undo something in git."
---

# Git Commit Pr

Keep history readable and recover safely from git mistakes.

## Process

1. For commits: use imperative subject under 72 chars; body explains why, not what.
2. For PRs: summary, motivation, changes, testing, screenshots, risks, rollout.
3. For messes: first run `git status` and `git reflog` to see state; prefer non-destructive fixes (revert, new branch) before reset --hard.
4. Provide exact commands with explanation, and warn before anything destructive.
5. Suggest a small branching convention (main + short-lived feature branches).

## Output format

Ready-to-paste commit message or PR body, or a command sequence with warnings.

## Rules

- Never suggest force-push to shared branches without a warning.
- Recommend a backup branch before risky history edits.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
