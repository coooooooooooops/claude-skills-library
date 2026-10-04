---
name: godot-dialogue-quests
description: "Build dialogue and quest systems in Godot with resources, state tracking, and UI. Use for RPGs and story games."
---

# Godot Dialogue Quests

Build dialogue and quest systems in Godot with resources, state tracking, and UI.

## Process

1. Model dialogue as data
2. track flags and quest state
3. drive UI from state
4. persist in saves
5. test branches

## Output format

Dialogue and quest framework.

## Rules

- Keep story data out of scripts.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
