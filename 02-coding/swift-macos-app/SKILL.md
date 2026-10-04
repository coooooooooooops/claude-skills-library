---
name: swift-macos-app
description: "Build native macOS apps in Swift/SwiftUI/AppKit: menu bar apps, windows, drag-and-drop, notch UI, sandboxing, and distribution. Use when the user wants a Mac app, menu bar utility, or notch shelf-style tool."
---

# Swift Macos App

Create polished native macOS apps.

## Process

1. Choose SwiftUI with AppKit bridging where needed (NSPanel, NSStatusItem, NSWindow levels).
2. Define state with @Observable or ObservableObject; persist with SwiftData or files.
3. Implement drag-and-drop with onDrop/NSItemProvider and file promises.
4. For notch-area UI, use a borderless NSPanel positioned from screen safeAreaInsets.
5. Handle App Sandbox entitlements, signing, notarization, and distribution (App Store or direct DMG).

## Output format

Project layout, key Swift files, entitlements, and distribution steps.

## Rules

- Respect sandbox and privacy permissions.
- Test on multiple displays and macOS versions.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
