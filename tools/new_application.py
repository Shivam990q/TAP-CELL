"""Scaffold a new job application so every drive stays organized the same way.

Usage:
    python tools/new_application.py --company "JOSH Technology Group" --role "Front End Developer"
    python tools/new_application.py -c "Acme" -r "SDE Intern" --slug acme-sde

Creates:
    06-job-descriptions/<slug>.md   (paste the JD here)
    05-applications/<slug>.md       (tracker + Google-form values prefilled from profile.json)
    04-resume/tailored/<slug>.tex   (copy of 04-resume/_base-resume.tex to tailor)
Appends a row to 05-applications/tracker.md.
"""
from __future__ import annotations

import argparse
import datetime as dt

from _common import ROOT, load_profile, read_text, slugify, write_text

BASE_RESUME = ROOT / "04-resume" / "_base-resume.tex"


def jd_template(company: str, role: str) -> str:
    return f"""# {company} - {role}

- Source:
- Registration deadline:
- Batch / eligibility:
- Location / work mode:
- Stipend / package:
- Bond (if any):

## About the company
(paste / research)

## Role: {role} - Required skills (ATS keywords to mirror)
-

## Responsibilities
-

## Hiring process (research from interview experiences)
-

## Tailoring notes for resume
- Surface the JD's exact keywords; pick the most relevant projects; keep 1 page.
"""


def application_template(company: str, role: str, slug: str, p: dict) -> str:
    per = p["personal"]
    edu = p["education"]
    links = p["links"]
    today = dt.date.today().strftime("%d %b %Y")
    return f"""# Application: {company} - {role}

- Date: {today}
- Source:
- JD file: `06-job-descriptions/{slug}.md`
- Resume used: `04-resume/tailored/{slug}.tex`
- Registration link:
- Status: Registering
- Role chosen: {role}

## Form field values (prefilled from data/profile.json)
| Field | Value |
| --- | --- |
| Full Name | {per['full_name']} |
| Email | {per['email']} |
| Mobile | {per['phone']} |
| Gender | {per['gender']} |
| Date of Birth | {per['dob']} |
| Roll Number | {edu['roll_number']} |
| Current Degree | {edu['degree']} |
| Branch | {edu['branch']} |
| Year of Passing | {edu['passing_year']} |
| College | {edu['institution']} |
| Current CGPA | {edu['cgpa']} |
| Graduation % | {edu['graduation_percent_approx']} (use official conversion) |
| Backlogs (current) | {edu['backlogs']} |
| History of Backlogs | {edu['backlog_history']} |
| 10th % | {edu['tenth_percent']} |
| 12th % | {edu['twelfth_percent']} |
| Diploma | {edu['diploma']} |
| LinkedIn | {links['linkedin']} |
| GitHub | {links['github']} |
| Portfolio | {links['portfolio']} |
| CV / Resume | PDF from 04-resume/tailored/{slug}.tex |

> Branch note: {edu['branch_note']}

## Interview prep
-

## Next step
- Tailor resume, register before deadline, submit PDF.
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--company", required=True)
    ap.add_argument("-r", "--role", required=True)
    ap.add_argument("--slug", default=None)
    args = ap.parse_args()

    slug = args.slug or slugify(f"{args.company}-{args.role}")
    p = load_profile()

    jd = ROOT / "06-job-descriptions" / f"{slug}.md"
    app = ROOT / "05-applications" / f"{slug}.md"
    resume = ROOT / "04-resume" / "tailored" / f"{slug}.tex"
    tracker = ROOT / "05-applications" / "tracker.md"

    created = []
    for path, content in [
        (jd, jd_template(args.company, args.role)),
        (app, application_template(args.company, args.role, slug, p)),
    ]:
        if path.exists():
            print(f"SKIP (exists): {path.relative_to(ROOT)}")
        else:
            write_text(path, content)
            created.append(path)

    if resume.exists():
        print(f"SKIP (exists): {resume.relative_to(ROOT)}")
    else:
        write_text(resume, read_text(BASE_RESUME))
        created.append(resume)

    # Append tracker row
    if tracker.exists():
        row = (f"| {args.company} | {args.role} | "
               f"{dt.date.today():%d %b %Y} | Registering | Tailor resume + submit | `{slug}.md` |\n")
        with open(tracker, "a", encoding="utf-8", newline="\n") as f:
            f.write(row)

    print(f"\nScaffolded application '{slug}':")
    for c in created:
        print("  + " + str(c.relative_to(ROOT)))
    print("\nNext:")
    print(f"  1. Paste the JD into 06-job-descriptions/{slug}.md")
    print(f"  2. Tailor 04-resume/tailored/{slug}.tex (role subtitle + skills order + projects)")
    print(f"  3. python tools/build_resume.py 04-resume/tailored/{slug}.tex --preview")


if __name__ == "__main__":
    main()
