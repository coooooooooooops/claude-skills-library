---
name: mcp-server-planner
description: "Plan and scaffold MCP servers: tools, resources, schemas, auth, and testing. Use when the user wants to connect Claude to a service or build a connector."
---

# Mcp Server Planner

Expose capabilities cleanly to models.

## Process

1. List the capabilities to expose and the data involved.
2. Define tool names, descriptions, and input schemas.
3. Plan auth and permissions with least privilege.
4. Scaffold with an official SDK.
5. Test with an inspector and real prompts.

## Output format

Tool spec and starter code outline.

## Rules

- Make tools narrow and well-described.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
