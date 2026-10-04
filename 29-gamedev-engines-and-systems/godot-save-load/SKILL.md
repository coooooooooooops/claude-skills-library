---
name: godot-save-load
description: "Implement Godot save and load systems with JSON, resources, versioning, and autosave. Use for persistence."
---

# Godot Save Load

Implement Godot save and load systems with JSON, resources, versioning, and autosave.

## Process

1. Define save data schema
2. serialize with Dictionary or Resource
3. add version field and migration
4. write atomically
5. add slots and autosave

## Output format

Save manager script.

## Rules

- Always version your save format.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
