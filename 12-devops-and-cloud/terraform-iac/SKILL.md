---
name: terraform-iac
description: "Write and review Terraform/OpenTofu infrastructure as code with modules, remote state, and safe applies. Use when defining cloud resources, reading a terraform plan, or structuring an IaC repo."
---

# Terraform Iac

Write and review Terraform/OpenTofu infrastructure as code with modules, remote state, and safe applies.

## Process

1. Identify provider and resources
2. split into reusable modules with variables and outputs
3. configure remote state with locking
4. run fmt, validate and plan before apply
5. review the plan for destroys

## Output format

Terraform files, module layout, and a plan-review checklist.

## Rules

- Never apply a plan containing unexpected destroys without explicit confirmation.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
