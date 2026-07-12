# Career OS

A single source of truth about me, used to power resume tailoring, ATS optimization,
application tracking, and job-targeted content during campus placements (and beyond).

## How it works
- I fill these files in over time. The AI assistant (Kiro) reads them to help me.
- Auto-loaded every chat (kept small): `.kiro/steering/about-me.md` (who I am) and
  `.kiro/steering/_system.md` (memory map + retrieval rules + firm rules).
- Everything else is loaded on demand via search/read, so the system scales to unlimited
  data without hitting context limits.

## Memory model (why I don't "forget")
- Context window = short-term, finite, resets each chat. Not used to store data.
- Steering = small always-on layer: a map of what exists and rules for how to retrieve it.
- Folders = unlimited long-term knowledge, pulled only when relevant.
- `memory/log.md` (journal) + `memory/facts.md` (stable snapshot) preserve continuity
  across sessions and context compaction.
- Markdown throughout, so this folder also opens directly in Obsidian for a graph/second-brain view.

## Structure
| Folder | Purpose |
| --- | --- |
| `01-profile/` | Personal info, education, skills, all platform links |
| `02-experience/` | Work, internships, achievements, certifications |
| `03-projects/` | One file per project (use `_TEMPLATE.md`); `_`-prefixed = GitHub inventory tooling/data |
| `04-resume/` | Base resume template, ATS guide, `tailored/` per-job versions |
| `05-applications/` | `tracker.md` (all apps) + **per-company subfolder** `05-applications/<company>/` (prep, solutions, application record) |
| `06-job-descriptions/` | **Per-company subfolder** `06-job-descriptions/<company>/` (JD + deep research) |
| `data/` | `profile.json` — machine-readable single source for form-fill |
| `memory/` | `log.md` (journal) + `facts.md` (stable snapshot) |
| `tools/` | Python automation (new_application, sync_github, build_resume, check_health) |

> Company subfolders (e.g. `infosys/`, `josh-technology/`, `stackmentalist/`) keep all files for one
> drive together in both `05-applications/` and `06-job-descriptions/`. New drives: run
> `python tools/new_application.py -c "Company" -r "Role"` — it scaffolds the company folder automatically.

## Workflow
1. Fill folders in order, starting with `01-profile/`.
2. Add a file per project in `03-projects/`.
3. Keep the base resume (`04-resume/_base-resume.tex`) as the reusable single-page template.
4. For each opening: `python tools/new_application.py -c "Company" -r "Role"` scaffolds the
   company subfolder (JD + application record + tailored resume copy) → paste JD → tailor `.tex`
   → `python tools/build_resume.py <tex> --preview`.

## Status checklist
- [ ] 01-profile filled in
- [ ] 02-experience filled in
- [ ] 03-projects added
- [ ] 04-resume master built
- [ ] Steering summary up to date
