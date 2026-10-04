---
name: docker-setup
description: "Create Dockerfiles, docker-compose setups, and dev containers with small images, caching, healthchecks, and security. Use when containerizing an app or debugging Docker problems."
---

# Docker Setup

Containerize reproducibly and securely.

## Process

1. Identify runtime, dependencies, ports, volumes, and env vars.
2. Use multi-stage builds, pinned base images, non-root users, and .dockerignore.
3. Order layers for cache efficiency.
4. Add compose services, healthchecks, and named volumes for data.
5. Document build and run commands.

## Output format

Dockerfile, docker-compose.yml, .dockerignore, and run instructions.

## Rules

- Never bake secrets into images.
- Pin versions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
