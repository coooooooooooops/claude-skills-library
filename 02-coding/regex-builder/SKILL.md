---
name: regex-builder
description: "Build, explain, and test regular expressions with examples and edge cases. Use whenever the user needs a regex, wants to parse or validate text patterns, or asks what a regex does."
---

# Regex Builder

Write regexes that are correct, readable, and tested.

## Process

1. Collect positive and negative example strings.
2. Choose the flavor (PCRE, JavaScript, Python, Go RE2).
3. Build incrementally with named groups and comments (verbose mode where available).
4. Test against all examples and list edge cases; warn about catastrophic backtracking.
5. Offer a non-regex alternative if parsing is better done another way.

## Output format

Final regex, token-by-token explanation, and a test table.

## Rules

- Do not parse HTML or nested structures with regex.
- Prefer anchored, specific patterns.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
