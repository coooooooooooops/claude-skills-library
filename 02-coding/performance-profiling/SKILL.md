---
name: performance-profiling
description: "Find and fix performance bottlenecks using measurement: profiling, benchmarks, algorithmic analysis, caching, and memory. Use when something is slow, laggy, uses too much memory, or the user asks to optimize."
---

# Performance Profiling

Optimize what is measured, not what is guessed.

## Process

1. Define the metric and target (latency p95, FPS, memory, throughput).
2. Establish a baseline with a reproducible benchmark.
3. Profile to find the top 1-3 hot spots.
4. Fix the biggest first: algorithm, I/O, allocation, caching, batching, parallelism.
5. Re-measure and stop when the target is met.

## Output format

Baseline, findings, changes, and before/after numbers.

## Rules

- No premature optimization.
- Keep optimizations readable and documented.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
