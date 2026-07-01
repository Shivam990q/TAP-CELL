# Tools — Career OS automation

Python scripts that keep everything organized as data changes (GitHub repos, new jobs,
per-job resumes). Run all from the repo root. Requires: Python 3, `gh` (authenticated),
`tectonic`, `poppler` (pdftoppm/pdfinfo).

## Single source of truth
`data/profile.json` holds stable form-fill data (personal, education, links). Scripts read
it. Update this file when academic/contact details change.

## Scripts

### 1. Sync GitHub repos
```
python tools/sync_github.py
```
Fetches all repos via `gh`, regenerates `03-projects/github-inventory.md`, and reports
NEW / REMOVED / UPDATED repos since the last run (state in `03-projects/_github-state.json`).
Run it whenever you push new repos so the inventory never goes stale.

### 2. Build & verify a resume
```
python tools/build_resume.py 04-resume/tailored/<file>.tex --preview
```
Compiles with Tectonic, checks it fits one page (use `--pages N` to change), and with
`--preview` renders `preview-*.png` next to the PDF. Exit code: 0 = OK, 2 = wrong page count.

### 3. Scaffold a new job application
```
python tools/new_application.py --company "Acme Corp" --role "Frontend Engineer"
```
Creates, with a consistent structure every time:
- `06-job-descriptions/<slug>.md` (paste the JD)
- `05-applications/<slug>.md` (tracker + form values prefilled from profile.json)
- `04-resume/tailored/<slug>.tex` (copy of `04-resume/_base-resume.tex` to tailor)
- a row in `05-applications/tracker.md`

### 4. Health check
```
python tools/check_health.py
```
Verifies the folder structure and lists every pending/placeholder item across the knowledge
base, so nothing silently stays incomplete.

## Typical flow for a new job
1. `python tools/new_application.py -c "Company" -r "Role"`
2. Paste the JD into the generated `06-job-descriptions/<slug>.md`.
3. Tailor `04-resume/tailored/<slug>.tex` (role subtitle, skills order, projects).
4. `python tools/build_resume.py 04-resume/tailored/<slug>.tex --preview`
5. Fill the company form using the prefilled values; submit the PDF.
