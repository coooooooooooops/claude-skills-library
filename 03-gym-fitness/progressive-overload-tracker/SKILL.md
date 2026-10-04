---
name: progressive-overload-tracker
description: "Track lifts and recommend when and how much to increase weight, reps, or sets based on logged performance. Use when the user shares workout logs, stalls on a lift, or asks how to progress."
---

# Progressive Overload Tracker

Turn logs into the next session's targets.

## Process

1. Collect recent sessions: weight, reps, sets, RPE.
2. Compute estimated 1RM trends and volume per muscle group per week.
3. Apply progression rules: hit top of rep range at target RIR, then add smallest load jump.
4. Diagnose stalls: sleep, calories, volume, technique, variation needed.
5. Write next session's targets.

## Output format

Table of lifts with trend and next targets, plus a stall diagnosis if needed.

## Rules

- Do not push load increases when form is breaking down.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
