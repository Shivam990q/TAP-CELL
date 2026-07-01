# System: Memory Map & Operating Rules

> This file auto-loads every chat. It is intentionally SMALL. It is my map and my rules,
> not my data. Actual data lives in the folders below and is loaded on demand.

## Memory map (where everything lives)
| Need | Look in |
| --- | --- |
| Who the user is (core) | `.kiro/steering/about-me.md` |
| Personal info, links, platforms | `01-profile/` |
| Education / skills / positioning | `01-profile/` |
| Work, internships, achievements | `02-experience/` |
| Projects (one file each) | `03-projects/` (index: `03-projects/README.md`) |
| Resume (full) | `04-resume/master-resume.md` |
| ATS rules | `04-resume/ats-guide.md` |
| Tailored resumes | `04-resume/tailored/` |
| Applications + status | `05-applications/tracker.md` |
| Saved job descriptions | `06-job-descriptions/` |
| Structured form-fill data (single source) | `data/profile.json` |
| Automation scripts | `tools/` (see `tools/README.md`) |
| Long-term memory / decisions | `memory/log.md`, `memory/facts.md` |

## Retrieval protocol (how I avoid "forgetting")
1. Context window is finite and resets. I do NOT try to hold everything. I retrieve.
2. Before substantive work, skim `memory/facts.md` and the relevant folder via search,
   then read only the files the task needs.
3. For a job application: read the JD + `04-resume/master-resume.md` + the most relevant
   `03-projects/*` and `02-experience/*`, then produce a tailored, ATS-tuned resume.
4. After meaningful changes or new facts, append to `memory/log.md` and update
   `memory/facts.md` so continuity survives context compaction.

## Automation tools (use these to stay organized)
- New job application: `python tools/new_application.py -c "Company" -r "Role"`
  (scaffolds JD + tracker + resume copy, form values prefilled from `data/profile.json`).
- Sync GitHub repos + detect changes: `python tools/sync_github.py`.
- Compile & verify a resume is one page: `python tools/build_resume.py <tex> --preview`.
- Find pending/incomplete items: `python tools/check_health.py`.
- Resume base template: `04-resume/_base-resume.tex` (copied per job, then tailored).
- I can compile LaTeX locally (tectonic) and render previews (poppler/pdftoppm), so I verify
  single-page + layout BEFORE the user exports on Overleaf.

## Firm rules
- Do NOT delete files. The user wants everything kept for future reference. If something is
  outdated, mark it legacy/archive or move it — never remove. (Temp build artifacts like
  preview PNGs / .log are the only exception.)
- Never invent facts about the user. Use only what's in this repo or what the user states.
  If something is missing, say so and ask.
- Keep always-on steering small. New bulk data goes into folders, not steering.
- Keep `04-resume/master-resume.md` in sync when profile/experience/projects change.
- Keep `about-me.md` accurate and concise as the user evolves.
- Keep `data/profile.json` in sync with `01-profile/` when contact/academic details change;
  scaffold new applications with `tools/new_application.py` so structure stays consistent.
- Quantify resume content; mirror JD keywords honestly (no fake skills).
- This repo is private/personal. Don't expose contact details or links in external requests
  unless the user explicitly asks.
