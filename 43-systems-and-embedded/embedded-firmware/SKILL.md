---
name: embedded-firmware
description: "Design embedded firmware: interrupts, timers, state machines, low power, and drivers. Use for microcontroller projects."
---

# Embedded Firmware

Design embedded firmware: interrupts, timers, state machines, low power, and drivers.

## Process

1. Define hardware and timing needs
2. structure with a main loop or RTOS
3. keep ISRs short
4. add watchdog and logging
5. test on hardware

## Output format

Firmware architecture and code.

## Rules

- Keep interrupt handlers minimal.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
