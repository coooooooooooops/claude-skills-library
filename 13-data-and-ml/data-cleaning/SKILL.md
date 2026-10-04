---
name: data-cleaning
description: "Detect and fix data quality problems: duplicates, outliers, missing values, inconsistent formats. Use when data looks wrong or before any analysis."
---

# Data Cleaning

Detect and fix data quality problems: duplicates, outliers, missing values, inconsistent formats.

## Process

1. Profile each column
2. define rules for validity
3. handle missing values explicitly
4. dedupe and standardize
5. log every change

## Output format

Cleaning script and a change log.

## Rules

- Never silently drop data; document every removal.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
