---
name: rtos-and-concurrency
description: "Use FreeRTOS or Zephyr: tasks, queues, mutexes, and priority pitfalls. Use when firmware needs multiple tasks."
---

# Rtos And Concurrency

Use FreeRTOS or Zephyr: tasks, queues, mutexes, and priority pitfalls.

## Process

1. Split work into tasks
2. choose priorities
3. communicate with queues
4. avoid priority inversion
5. size stacks

## Output format

Task design.

## Rules

- Prefer message passing to shared state.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
