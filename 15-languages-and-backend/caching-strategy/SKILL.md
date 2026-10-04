---
name: caching-strategy
description: "Design caching: browser, CDN, application, and database layers with invalidation. Use when speeding up reads or fixing stale data."
---

# Caching Strategy

Design caching: browser, CDN, application, and database layers with invalidation.

## Process

1. Identify read-heavy hot paths
2. choose cache layer and TTL
3. define invalidation
4. protect against stampedes
5. measure hit rate

## Output format

Caching plan.

## Rules

- Define how each cache gets invalidated before adding it.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
