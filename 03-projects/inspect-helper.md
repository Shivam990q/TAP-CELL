# Inspect Helper — Chrome Extension

- One-liner: Chrome extension that restores developer tools access on sites that block them.
- Status: Live / open-source (MIT)
- Links: Extension/repo: https://github.com/Shivam990q/inspect-helper
- Timeline: ~3 months ago (confirm)
- Role: Solo developer

## Problem
Some sites block right-click/Inspect, disable copy-paste, close tabs when DevTools open,
and use anti-debugging tricks — blocking legitimate learning/debugging.

## Tech stack
Chrome Extension (Manifest V3), JavaScript

## What I built (key features)
- Re-enables right-click → Inspect; restores copy/paste & text selection
- Stops tabs from closing when DevTools opens
- Neutralizes anti-debugging tricks (debugger traps, viewport detection, console probes)

## Impact / metrics
- 43+ reactions on launch post; positioned as a developer-friction tool. (Add install count.)

## Resume bullets (draft)
- Built a Manifest V3 Chrome extension that restores DevTools/right-click access by
  neutralizing common anti-debugging techniques (debugger traps, console probes).
