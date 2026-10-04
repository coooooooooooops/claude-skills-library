---
name: godot-testing-gut
description: "Test Godot code with GUT: unit tests, scene tests, and CI. Use when adding automated testing."
---

# Godot Testing Gut

Test Godot code with GUT: unit tests, scene tests, and CI.

## Process

1. Install GUT
2. test pure logic first
3. instance scenes for integration tests
4. run headless in CI
5. track regressions

## Output format

Test files and CI snippet.

## Rules

- Keep logic testable and separate from nodes.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
