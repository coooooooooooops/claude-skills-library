---
name: graphql-server
description: "Design and build GraphQL servers: schema, resolvers, dataloaders, auth, and pagination. Use when building or optimizing a GraphQL API."
---

# Graphql Server

Design and build GraphQL servers: schema, resolvers, dataloaders, auth, and pagination.

## Process

1. Design schema from client needs
2. write resolvers
3. batch with dataloader to prevent N+1
4. add auth and depth limits
5. use cursor pagination

## Output format

Schema and resolver code.

## Rules

- Limit query depth and complexity.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
