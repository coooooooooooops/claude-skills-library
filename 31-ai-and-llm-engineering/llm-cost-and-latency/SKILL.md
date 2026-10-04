---
name: llm-cost-and-latency
description: "Reduce LLM cost and latency with caching, smaller models, batching, and prompt trimming. Use when bills or response times are too high."
---

# Llm Cost And Latency

Reduce LLM cost and latency with caching, smaller models, batching, and prompt trimming.

## Process

1. Measure tokens and latency
2. route easy tasks to small models
3. cache repeats
4. trim prompts
5. stream responses

## Output format

Optimization plan.

## Rules

- Measure quality after each cost cut.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
