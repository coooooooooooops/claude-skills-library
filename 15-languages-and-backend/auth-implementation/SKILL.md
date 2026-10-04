---
name: auth-implementation
description: "Implement authentication and authorization: sessions, JWT, OAuth/OIDC, passwords, and roles. Use when adding login or access control."
---

# Auth Implementation

Implement authentication and authorization: sessions, JWT, OAuth/OIDC, passwords, and roles.

## Process

1. Prefer a proven library or provider
2. hash passwords with argon2 or bcrypt
3. use secure cookies
4. add RBAC checks server-side
5. add rate limiting and MFA options

## Output format

Auth design and code.

## Rules

- Never roll your own crypto.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
