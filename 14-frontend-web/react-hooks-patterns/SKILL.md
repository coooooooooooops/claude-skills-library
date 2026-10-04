---
name: react-hooks-patterns
description: "Use React hooks correctly: useEffect pitfalls, custom hooks, memoization, and data fetching. Use when debugging re-renders, stale closures, or infinite loops."
---

# React Hooks Patterns

Use React hooks correctly: useEffect pitfalls, custom hooks, memoization, and data fetching.

## Process

1. Reproduce the issue
2. check dependency arrays
3. replace effects with derived state or event handlers
4. extract custom hooks
5. measure before memoizing

## Output format

Fixed code and explanation.

## Rules

- Avoid useEffect for things that are not synchronization.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
