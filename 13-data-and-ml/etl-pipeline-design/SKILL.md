---
name: etl-pipeline-design
description: "Design reliable ETL/ELT pipelines with idempotency, schema checks, and orchestration. Use when moving or transforming data between systems."
---

# Etl Pipeline Design

Design reliable ETL/ELT pipelines with idempotency, schema checks, and orchestration.

## Process

1. Map sources and targets
2. define schemas and contracts
3. make loads idempotent
4. orchestrate with Airflow or similar
5. add data-quality checks and alerts

## Output format

Pipeline design and DAG sketch.

## Rules

- Every task must be safely re-runnable.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
