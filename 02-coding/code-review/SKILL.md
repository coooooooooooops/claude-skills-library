---
name: code-review
description: "Perform a structured, prioritized code review covering correctness, security, performance, readability, and tests. Use whenever the user pastes code, a diff, or a PR and asks for review, feedback, 'is this good', or 'what's wrong with this'."
---

# Code Review

Review code like a senior engineer: find real problems first, style last.

## Process

1. Understand intent: what is the code supposed to do? Ask if unclear.
2. Check correctness and edge cases (null, empty, large, concurrent, error paths).
3. Check security (input validation, injection, secrets, authz) and resource handling.
4. Check performance hot spots and complexity only where it matters.
5. Check readability, naming, structure, and test coverage.
6. Group findings by severity and propose concrete fixes with code.

## Output format

Sections: Blockers, Should-fix, Nits, Praise. Each item has location, problem, and suggested fix.

## Rules

- Lead with the most impactful issues.
- Praise what is good; it calibrates the review.
- Do not rewrite everything; respect the author's style.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
