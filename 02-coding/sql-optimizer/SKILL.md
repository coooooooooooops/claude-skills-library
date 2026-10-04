---
name: sql-optimizer
description: "Write, explain, and optimize SQL queries and schemas: indexes, joins, EXPLAIN plans, N+1 problems. Use whenever the user shares SQL, a slow query, a schema, or asks about database performance."
---

# Sql Optimizer

Make queries correct first, then fast.

## Process

1. Confirm the dialect (Postgres, MySQL, SQLite, SQL Server) and table sizes.
2. Verify correctness: joins, null handling, duplicates, time zones.
3. Ask for or reason about the EXPLAIN plan; find scans, sorts, and bad estimates.
4. Propose indexes (composite order matters) and query rewrites (CTEs, window functions, EXISTS).
5. Warn about write overhead and index bloat; suggest measuring before and after.

## Output format

Optimized query, recommended indexes (DDL), and expected effect.

## Rules

- Never apply schema changes to production without a migration plan.
- Measure, don't assume.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
