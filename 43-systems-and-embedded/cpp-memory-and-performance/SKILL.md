---
name: cpp-memory-and-performance
description: "Debug and optimize C++ memory and performance: leaks, cache behavior, sanitizers, and profiling. Use when C++ crashes or runs slowly."
---

# Cpp Memory And Performance

Debug and optimize C++ memory and performance: leaks, cache behavior, sanitizers, and profiling.

## Process

1. Run AddressSanitizer and UBSan
2. fix ownership issues
3. profile with perf or VTune
4. improve data layout
5. re-measure

## Output format

Findings and fixes.

## Rules

- Measure before and after every change.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
