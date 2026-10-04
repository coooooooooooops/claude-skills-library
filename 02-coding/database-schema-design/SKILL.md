---
name: database-schema-design
description: "Design relational and document schemas with proper normalization, keys, constraints, indexes, and migrations. Use when modeling data for an app, game save system, inventory, or analytics."
---

# Database Schema Design

Model data so it is correct, flexible, and fast.

## Process

1. List entities, relationships, and access patterns.
2. Normalize to 3NF, then denormalize deliberately for read performance.
3. Define primary/foreign keys, unique constraints, checks, and types.
4. Plan indexes from queries.
5. Write migrations that are reversible.

## Output format

ERD (Mermaid), DDL, and example queries.

## Rules

- Design from queries, not just nouns.
- Plan for schema evolution.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
