---
name: logging-observability
description: "Add structured logging, metrics, tracing, and alerts so systems are debuggable in production. Use when the user asks how to monitor or troubleshoot a deployed system."
---

# Logging Observability

Make systems explain themselves.

## Process

1. Define key user journeys and SLIs/SLOs.
2. Use structured logs with request IDs and levels.
3. Add metrics (rate, errors, duration) and traces across services.
4. Create actionable alerts with runbooks; avoid alert fatigue.
5. Redact sensitive data.

## Output format

Instrumentation snippets, dashboard outline, and alert list.

## Rules

- Alert on symptoms, not causes.
- No PII in logs.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
