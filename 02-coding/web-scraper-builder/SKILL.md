---
name: web-scraper-builder
description: "Design ethical, resilient web scrapers and data collectors: HTTP vs. headless browser, parsing, rate limiting, caching, and storage. Use when the user wants to collect public data or build a price tracker."
---

# Web Scraper Builder

Collect data reliably and respectfully.

## Process

1. Check for an official API or feed first.
2. Review robots.txt and terms of service; respect rate limits.
3. Choose requests+parser for static pages, Playwright for dynamic ones.
4. Add retries, backoff, caching, and structured output (CSV/SQLite/JSON).
5. Monitor for layout changes with schema checks.

## Output format

Scraper code, storage schema, and a maintenance plan.

## Rules

- Do not bypass authentication, paywalls, or anti-bot protections.
- Do not collect personal data without a lawful basis.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
