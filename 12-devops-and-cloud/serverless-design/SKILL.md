---
name: serverless-design
description: "Design serverless apps with Lambda or Cloud Functions, queues, and managed services. Use when building event-driven or low-ops backends."
---

# Serverless Design

Design serverless apps with Lambda or Cloud Functions, queues, and managed services.

## Process

1. Map events and triggers
2. keep functions small and idempotent
3. handle cold starts and timeouts
4. use queues for retries
5. set concurrency and cost limits

## Output format

Architecture and function skeletons.

## Rules

- Design every handler to be safely retried.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
