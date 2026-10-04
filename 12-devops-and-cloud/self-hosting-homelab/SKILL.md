---
name: self-hosting-homelab
description: "Plan self-hosted services and homelabs with Docker, reverse proxies, DNS, VPN, and backups. Use when running your own apps at home or on a VPS."
---

# Self Hosting Homelab

Plan self-hosted services and homelabs with Docker, reverse proxies, DNS, VPN, and backups.

## Process

1. List services wanted and hardware
2. organize with docker compose
3. add reverse proxy and TLS
4. secure access with VPN or auth
5. automate backups and updates

## Output format

Stack plan with compose files.

## Rules

- Do not expose admin interfaces directly to the internet.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
