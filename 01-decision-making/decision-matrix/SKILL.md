---
name: decision-matrix
description: "Build a weighted decision matrix to compare options against criteria. Use whenever the user is choosing between 2+ options (tools, jobs, purchases, designs, vendors, plans), says 'which should I pick', 'help me decide', 'compare these', or is stuck between choices, even if they never say 'matrix'."
---

# Decision Matrix

Turn a vague choice into a scored, transparent comparison the user can challenge and adjust.

## Process

1. Restate the decision in one sentence and list every option, including 'do nothing' when relevant.
2. Elicit 4-8 criteria. Ask what matters most; separate must-haves (pass/fail) from nice-to-haves (scored).
3. Assign weights that sum to 100. Show the weights and ask for a quick sanity check.
4. Score each option 1-5 per criterion with a one-line justification. Mark guesses as guesses.
5. Compute weighted totals, then run a sensitivity check: which weight change flips the winner?
6. Give a recommendation plus the single biggest uncertainty that could change it.

## Output format

A markdown table (criteria, weight, scores), totals row, sensitivity note, and a 3-line recommendation.

## Rules

- Never hide the weights; the user must be able to edit them.
- If the winner is within ~5%, call it a tie and decide on a tiebreaker criterion.
- Gut feeling counts: ask 'does the result feel wrong?' and investigate why.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
