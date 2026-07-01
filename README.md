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
| `03-projects/` | One file per project (use `_TEMPLATE.md`) |
| `04-resume/` | Master resume, ATS guide, tailored versions |
| `05-applications/` | Application tracker (use `_TEMPLATE.md`) |
| `06-job-descriptions/` | Saved JDs I'm targeting |

## Workflow
1. Fill folders in order, starting with `01-profile/`.
2. Add a file per project in `03-projects/`.
3. Keep `04-resume/master-resume.md` as the complete "kitchen-sink" resume.
4. For each opening: save the JD in `06-job-descriptions/`, then generate a tailored,
   ATS-tuned resume from the master data.

## Status checklist
- [ ] 01-profile filled in
- [ ] 02-experience filled in
- [ ] 03-projects added
- [ ] 04-resume master built
- [ ] Steering summary up to date
