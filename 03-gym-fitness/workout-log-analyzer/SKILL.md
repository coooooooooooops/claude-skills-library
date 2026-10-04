---
name: workout-log-analyzer
description: "Analyze workout history for volume, frequency, balance, and trends, and suggest adjustments. Use when the user pastes a log, CSV, or notes from past training."
---

# Workout Log Analyzer

Turn raw logs into insights.

## Process

1. Parse the log into date, exercise, sets, reps, load.
2. Compute weekly volume per muscle group and sessions per week.
3. Spot imbalances and missed muscle groups.
4. Highlight best lifts and plateaus.
5. Recommend 3 specific changes.

## Output format

Summary stats, balance chart description, and 3 recommendations.

## Rules

- Say when the data is too sparse to conclude anything.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
