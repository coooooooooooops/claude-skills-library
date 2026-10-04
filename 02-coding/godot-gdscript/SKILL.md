---
name: godot-gdscript
description: "Build Godot 4 games with GDScript: scene architecture, signals, autoloads, resources, physics, input, multiplayer, and performance. Use whenever the user mentions Godot, GDScript, .tscn, or building a 2D/3D game in Godot."
---

# Godot Gdscript

Write idiomatic Godot 4 code with clean scene structure.

## Process

1. Identify the game type and the feature (player controller, inventory, AI, UI, networking).
2. Propose scene tree and node responsibilities; prefer composition and signals over tight coupling.
3. Use Godot 4 syntax: typed GDScript, @export, @onready, await, Callable-based signals, CharacterBody2D/3D.
4. Put shared data in Resources and global state in minimal autoloads.
5. For multiplayer use the high-level API: MultiplayerSpawner, MultiplayerSynchronizer, RPC annotations, server authority.
6. Provide complete scripts and the scene setup steps.

## Output format

Scene tree sketch, full typed scripts, and setup notes.

## Rules

- Use Godot 4 APIs only, not Godot 3 names.
- Keep logic out of _process when signals or timers work.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
