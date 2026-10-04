---
name: test-writer
description: "Write thorough, maintainable tests (unit, integration, property-based) with good names, edge cases, and minimal mocking. Use when the user asks for tests, coverage, TDD, or wants to verify code works."
---

# Test Writer

Produce tests that catch real bugs and document behavior.

## Process

1. Identify the public behavior and the contracts to verify.
2. List cases: happy path, boundaries, invalid input, errors, concurrency, idempotency.
3. Pick the framework matching the project (pytest, jest, vitest, JUnit, Go testing, GUT for Godot).
4. Write Arrange-Act-Assert tests with descriptive names.
5. Mock only at boundaries (network, time, filesystem).
6. Suggest mutation or property tests for critical logic.

## Output format

Runnable test file plus a short list of cases intentionally not covered.

## Rules

- One behavior per test.
- Tests must fail when the code is wrong; sanity-check that.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
