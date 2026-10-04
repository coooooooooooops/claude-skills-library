---
name: kubernetes-manifests
description: "Write and debug Kubernetes manifests: Deployments, Services, Ingress, ConfigMaps, probes, and resource limits. Use when deploying to k8s or troubleshooting CrashLoopBackOff, pending pods, or networking."
---

# Kubernetes Manifests

Write and debug Kubernetes manifests: Deployments, Services, Ingress, ConfigMaps, probes, and resource limits.

## Process

1. Define workload and scaling needs
2. write Deployment with probes and requests/limits
3. add Service and Ingress
4. externalize config and secrets
5. debug with describe, logs and events

## Output format

YAML manifests plus kubectl commands to apply and verify.

## Rules

- Always set resource requests and readiness probes.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
