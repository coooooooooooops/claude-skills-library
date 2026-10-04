---
name: api-security-review
description: "Review APIs for authentication, authorization, rate limits, and data exposure. Use when securing endpoints."
---

# Api Security Review

Review APIs for authentication, authorization, rate limits, and data exposure.

## Process

1. Check auth on every route
2. test object-level authorization
3. add rate limits
4. limit returned fields
5. log and monitor

## Output format

API security findings.

## Rules

- Broken object-level authorization is the top risk.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
