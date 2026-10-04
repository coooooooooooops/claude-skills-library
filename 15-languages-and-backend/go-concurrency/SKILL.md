---
name: go-concurrency
description: "Write Go with goroutines, channels, contexts, and worker pools safely. Use when handling concurrency or fixing races in Go."
---

# Go Concurrency

Write Go with goroutines, channels, contexts, and worker pools safely.

## Process

1. Define the concurrent workflow
2. use context for cancellation
3. prefer channels for ownership transfer
4. guard shared state
5. run the race detector

## Output format

Go code with race-safe design.

## Rules

- Always run with -race during development.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
