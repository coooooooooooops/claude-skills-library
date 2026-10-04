---
name: inventory-forecasting
description: "Forecast stock needs from sales velocity, lead times, and seasonality. Use when deciding reorder quantities."
---

# Inventory Forecasting

Forecast stock needs from sales velocity, lead times, and seasonality.

## Process

1. Collect sales history
2. compute velocity
3. add lead time and safety stock
4. adjust for seasonality
5. set reorder points

## Output format

Reorder table.

## Rules

- Flag slow movers instead of reordering them.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
