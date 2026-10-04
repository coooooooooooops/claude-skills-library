---
name: error-handling
description: "Design robust error handling, validation, retries, timeouts, and logging. Use when code crashes on bad input, lacks failure paths, or the user asks about exceptions, resilience, or graceful degradation."
---

# Error Handling

Fail loudly, recover where sensible, and never lose information.

## Process

1. Classify errors: user error, transient, bug, fatal.
2. Validate at boundaries and fail fast with actionable messages.
3. Add timeouts, retries with backoff and jitter for transient failures, and circuit breakers if needed.
4. Log with context but without secrets.
5. Test the failure paths.

## Output format

Revised code with error taxonomy and tests.

## Rules

- Never swallow exceptions silently.
- Retry only idempotent operations.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
