---
name: model-evaluation
description: "Evaluate models with proper splits, metrics, calibration, and error analysis. Use when judging whether a model is good or debugging bad predictions."
---

# Model Evaluation

Evaluate models with proper splits, metrics, calibration, and error analysis.

## Process

1. Choose metrics for the business cost
2. use holdout or cross-validation
3. inspect confusion and error slices
4. check calibration
5. compare to baseline

## Output format

Evaluation report with error analysis.

## Rules

- Never evaluate on training data.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
