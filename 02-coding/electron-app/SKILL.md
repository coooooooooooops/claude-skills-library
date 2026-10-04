---
name: electron-app
description: "Build desktop apps with Electron: main/renderer architecture, IPC, security, packaging, auto-update. Use when the user wants a cross-platform desktop app or wrapper around web tech."
---

# Electron App

Ship secure, packaged Electron apps.

## Process

1. Set up main, preload, and renderer with contextIsolation on and nodeIntegration off.
2. Expose a minimal API via contextBridge; validate IPC messages.
3. Persist data in app.getPath('userData').
4. Package with electron-builder or Forge for each OS; set up code signing and notarization notes.
5. Add auto-update and crash handling.

## Output format

Project structure, key files, and build commands.

## Rules

- Never load remote content with Node access.
- Keep the preload surface tiny.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
