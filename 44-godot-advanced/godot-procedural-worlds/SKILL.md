---
name: godot-procedural-worlds
description: "Generate Godot worlds with FastNoiseLite, chunking, tilemaps, and seeded determinism. Use for terrain and roguelike maps."
---

# Godot Procedural Worlds

Generate Godot worlds with FastNoiseLite, chunking, tilemaps, and seeded determinism.

## Process

1. Choose noise and seed
2. chunk and stream
3. place features with rules
4. validate connectivity
5. cache chunks

## Output format

Generation scripts.

## Rules

- Make generation deterministic from a seed.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
