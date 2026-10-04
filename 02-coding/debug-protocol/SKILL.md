---
name: debug-protocol
description: "Systematic debugging: reproduce, isolate, hypothesize, test, fix, and prevent regressions. Use when the user reports a bug, error message, stack trace, crash, or says 'it doesn't work' or 'why is this happening'."
---

# Debug Protocol

Debug with the scientific method instead of random changes.

## Process

1. Collect the exact error, expected vs. actual behavior, environment, and recent changes.
2. Reproduce minimally; if impossible, add logging to capture state.
3. Form 3 ranked hypotheses from the evidence.
4. Design the cheapest test for each hypothesis (print, assert, bisect, rubber-duck).
5. Fix the root cause, not the symptom, and explain why it happened.
6. Add a regression test and note how to prevent the class of bug.

## Output format

Diagnosis (root cause), fix (code), and prevention (test or guard).

## Rules

- Change one thing at a time.
- Read the actual error message carefully before guessing.
- If you must guess, say so and give a way to verify.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
