---
name: linux-sysadmin
description: "Administer Linux servers: users, permissions, systemd, networking, disk, logs, and hardening basics. Use when troubleshooting a server, writing systemd units, or setting up a VPS."
---

# Linux Sysadmin

Administer Linux servers: users, permissions, systemd, networking, disk, logs, and hardening basics.

## Process

1. Gather distro and symptoms
2. inspect logs with journalctl
3. check disk, memory, CPU and network
4. fix configuration with minimal change
5. document the change

## Output format

Diagnostic commands with explanations and the fix.

## Rules

- Warn before destructive commands and suggest backups first.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
