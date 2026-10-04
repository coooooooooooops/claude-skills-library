---
name: code-explainer
description: "Explain unfamiliar code clearly at the user's level, with a walkthrough, data flow, and diagrams. Use when the user pastes code and asks 'what does this do', 'explain', or is onboarding to a codebase."
---

# Code Explainer

Make code understandable, not just described.

## Process

1. Gauge the user's level from their wording.
2. Give a one-paragraph summary of purpose first.
3. Walk through step by step, highlighting key concepts and gotchas.
4. Show data flow or a small diagram (ASCII or Mermaid).
5. Offer a tiny modified example to cement understanding.

## Output format

Summary, walkthrough, diagram, and takeaway.

## Rules

- No jargon without a definition.
- Admit when behavior depends on code you cannot see.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
