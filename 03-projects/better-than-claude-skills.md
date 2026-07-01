# Better Than Claude Skills — Open-source LLM skills

- One-liner: Open-source set of 16+ production-ready "skills" that turn any LLM into an
  autonomous, domain-expert agent.
- Status: Live / open-source (MIT)
- Links: GitHub: https://github.com/Shivam990q/better-than-claude-skills | License: MIT
- Timeline: ~2 months ago (confirm)
- Role: Solo creator

## Problem
General LLMs (Claude, Gemini, GPT) produce generic, half-broken output on complex tasks
(React architecture, MCP servers, production UI, Playwright tests, new skills).

## Approach — Progressive Disclosure Architecture (3 layers)
- Layer 1: metadata triggers (always loaded)
- Layer 2: workflow (loaded on activation)
- Layer 3: scripts & references (loaded on demand)
> Goal: give the model exactly what it needs, when it needs it — minimal context, fewer
> hallucinations. (Same principle this Career OS uses.)

## What it does (skills)
- Frontend Design (distinctive production UIs), Algorithmic Art (P5.js)
- Document Mastery (.docx/.xlsx/.pdf/.pptx — TOC, formulas, formatting)
- MCP Builder (build Model Context Protocol servers)
- Web App Builder (multi-component React/Next.js with state management)
- Skill Creator (AI writes, benchmarks, and optimizes new skills itself)

## Impact / metrics
- 16+ skills, MIT licensed, drag-and-drop usable. (Add GitHub stars/forks if available.)

## Resume bullets (draft)
- Designed a 3-layer "progressive disclosure" architecture for LLM agents, reducing prompt
  bloat and hallucination while enabling 16+ reusable, production-ready skills (open-source, MIT).
