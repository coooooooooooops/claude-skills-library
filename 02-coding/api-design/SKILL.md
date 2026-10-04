---
name: api-design
description: "Design clean REST, GraphQL, or RPC APIs with consistent naming, versioning, pagination, errors, auth, and idempotency. Use when the user is designing endpoints, schemas, SDK surfaces, or reviewing an API."
---

# Api Design

Design APIs that are predictable, evolvable, and hard to misuse.

## Process

1. Clarify consumers, use cases, and scale.
2. Model resources and relationships; choose nouns and verbs consistently.
3. Define request/response shapes, status codes, and a uniform error format.
4. Decide pagination, filtering, sorting, rate limits, and idempotency keys.
5. Plan auth, versioning, and deprecation.
6. Produce an OpenAPI or schema sketch with examples.

## Output format

Endpoint table, example payloads, error model, and OpenAPI snippet.

## Rules

- Optimize for the consumer's mental model.
- Never break existing clients without versioning.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
