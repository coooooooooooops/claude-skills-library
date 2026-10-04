---
name: nginx-config
description: "Write and debug nginx configs: reverse proxy, TLS, caching, rate limits, and static hosting. Use when setting up a web server, fixing 502/504 errors, or redirecting traffic."
---

# Nginx Config

Write and debug nginx configs: reverse proxy, TLS, caching, rate limits, and static hosting.

## Process

1. Define sites and upstreams
2. configure server blocks with TLS
3. add proxy headers, gzip and caching
4. test with nginx -t
5. reload gracefully

## Output format

Config snippets and test commands.

## Rules

- Always test config before reload.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
