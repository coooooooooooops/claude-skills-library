---
name: security-audit
description: "Audit code and architecture for common vulnerabilities (OWASP Top 10, secrets, authz, injection, SSRF, unsafe deserialization, dependency risk) and recommend defensive fixes. Use when reviewing code for security, hardening an app, or handling user input, auth, or payments."
---

# Security Audit

Find and fix vulnerabilities defensively.

## Process

1. Map trust boundaries and sensitive data flows.
2. Check input validation, output encoding, auth/authz, session handling, and secrets storage.
3. Check dependencies, configuration, headers, and logging of sensitive data.
4. Rank findings by exploitability and impact.
5. Provide minimal, safe fixes and tests that guard against regression.

## Output format

Findings table (severity, location, risk, fix) and a hardening checklist.

## Rules

- Defensive guidance only; do not write exploit code or malware.
- Never include real secrets in output.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
