---
name: queues-and-workers
description: "Design background jobs with queues, retries, dead letters, and idempotency. Use when offloading slow or unreliable work."
---

# Queues And Workers

Design background jobs with queues, retries, dead letters, and idempotency.

## Process

1. Choose broker
2. define job payloads
3. make handlers idempotent
4. set retry with backoff
5. add dead-letter queue and monitoring

## Output format

Queue design and worker code.

## Rules

- Jobs must tolerate running twice.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
