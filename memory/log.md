# Memory Log (append-only journal)

> Running record of important decisions, facts learned, and session summaries.
> Newest entries at the top. I read this before substantive work and append after
> meaningful changes, so continuity survives across chats and context compaction.

---

## 2026-06-30 — System setup
- Built Career OS skeleton: `01-profile`..`06-job-descriptions`, `04-resume`, `05-applications`.
- Added memory system: `.kiro/steering/_system.md` (map + retrieval protocol + firm rules),
  `memory/facts.md` (stable snapshot), `memory/log.md` (this journal).
- Decision: keep always-on steering small; bulk data lives in folders and is retrieved on demand.
- Next: intake `01-profile` (name, contact, links, education, skills, targets).

## 2026-06-30 — Profile intake (batch 1, from LinkedIn)
- Captured identity, contact, LinkedIn, education (ITM University, B.Tech CSE 2023–2027).
- Skills logged: full-stack (Django/React), Java/C++/Python/TS/JS, Flutter/RN/Kotlin/Android,
  SQL/PostgreSQL, MongoDB, AWS, DevOps, Gen/Agentic AI, MCP & agents, data analytics.
- Experience logged: Gwalior DAO (Technical Lead), ITM University (Full Stack intern, paid),
  Solvitude Solutions (Sr SME, Brainly.com), AdRyter (WordPress, unpaid), Banao (B2C).
- Certs: GDG Solution Challenge, MongoDB Basics, Postman API Student Expert, Own Your Identity.
- Leadership: President @ IDC; Technical Lead @ Gwalior DAO.
- Projects named (need detail): ROSE, University ERP, NETWORKED, Gmail Generator, Avalanche clone.
- Flagged: gray-area items (gmail generator, cert bypass) — keep out of formal ATS resumes.
- Still pending: GitHub/portfolio/LeetCode links, CGPA, target roles/companies, relocation,
  per-project details, quantified impact for each role.

## 2026-06-30 — Full LinkedIn intake (batch 2)
- Corrected experience durations from LinkedIn Experience section:
  ITM Full Stack (May 2025–Mar 2026, ~11mo, ERP/IQAC, on-site); Gwalior DAO Technical Lead
  (Dec 2025–Jan 2026, ~2mo, hybrid, Web3); Solvitude SME (Jan–Dec 2024, remote, Brainly.com);
  AdRyter WordPress (Jul–Aug 2024, part-time); Banao B2C (May–Jul 2024, freelance).
- Open to work: Gurugram (+2), on-site/hybrid/remote. 1,684 followers, 500+ connections.
- New skills/tools: KMP, OpenClaw, CrewAI, Hermes, RedHat/cybersecurity, Vite, Tailwind,
  shadcn/ui, Framer Motion, TanStack Query, DRF, Gunicorn/Nginx, CI/CD.
- Created project files: networked, better-than-claude-skills, inspect-helper, barterly,
  rose, curriculum-manager-erp. KMP app still to create.
- Certs (7): Full Stack Bootcamp, Postman Student Expert, MongoDB Basics, IQAC Internship
  Completion (ITMU/IQAC/2025/17), Own Your Identity, GDG Solution Challenge, Hacksagon Finalist.
- Hackathon: Hacksagon 2025 (IEEE ABV-IIITM) — Top Performer, Open Innovation category.
- Open questions: real GitHub username + repo URLs, CGPA, exact target roles/companies,
  ERP vs Curriculum Manager (same or separate?), project metrics, KMP app details.

## 2026-06-30 — GitHub access + full repo inventory (batch 3)
- gh CLI already authenticated as Shivam990q (no login needed). Token in keyring, not exposed.
- 97 repos total: 25 public, 72 private, 7 forks. Mostly TypeScript (61).
- Saved raw data: `03-projects/_github-raw.json`; generator: `_gen_inventory.ps1`.
- Full table: `03-projects/github-inventory.md`. Curated by category: `03-projects/_CURATED.md`.
- Flagship candidates: open-figma-mcp, better-than-claude-skills, Networked (client),
  University-Management-System-DBMS-LIVE-PROJECT, AGENTIC-ERP/Prabandh-Nexus, SmartRahagir,
  inspect-helper, Barterly-Redesigned, kiro-autonomy.
- Many repos are iterations (Prabandh*, RAVEN*, code-vault*, bold-core*) — pick best per family.
- Next: confirm which projects to feature, then deep-read those READMEs and write full project files + master resume.

## 2026-06-30 — Resume content intake (batch 4)
- Added professional summary (AI-focused full-stack dev: AI automation, agentic, Android, React/Python/Django).
- New skills: C, Bash/Shell, AI Prompt Engineering (JSON), Node.js, N8N, Docker, Kubernetes,
  Render/Railway/Heroku.
- New certs: Udemy (Django Full Stack; Advanced Python for IoT & ML), LinkedIn Learning
  (Career Essentials in GenAI), Google Cloud (ML & AI), Adryter 45-day internship.
- New/clarified projects: ITMU Parakh Portal MIS (React+Vite+Django; = Prabandh-Nexus family),
  CivicTrack (React+Django civic platform), Networked repo link (private), Google-Major-Security-Flaw.
- ITM role: ERP modernization (academic/finance/admin, automation+AI). Created itmu-parakh-portal-mis.md, civictrack.md.
- DISCREPANCIES to confirm:
  * Solvitude end date: resume Aug 2024 vs LinkedIn Dec 2024.
  * ITM end: resume "Present" vs LinkedIn "Mar 2026".
  * NETWORKED positioning: "consultancy platform" vs "professional networking platform".
- Resume omits Banao & Gwalior DAO (focused version) — full set still kept in experience file.

## 2026-07-01 — First application: JOSH Technology Group (FED)
- Campus drive via TAP Cell. Role chosen: Front End Developer (₹13.47 LPA > SQA ₹6.36 LPA).
- Deadline: 01 Jul 2026 10:00 AM (URGENT). Form: https://forms.gle/YnzYg1h9MRBwxNWr6
- Saved JD + research: 06-job-descriptions/josh-technology-frontend-2027.md
- Application tracker: 05-applications/josh-technology-frontend.md (+ tracker.md row)
- Tailored resume (LaTeX/Overleaf): 04-resume/tailored/josh-tech-frontend-2027.tex
- Research: ~9 elimination rounds; R1 70 MCQ (negative marking); CSS grilled hard; FE assignment.
- STILL NEED from Shivam (for form + resume): Roll Number, DOB, Gender(confirm Male), CGPA,
  current backlogs (#), history of backlogs (Y/N), 10th %, 12th %, Graduation % — add these to
  01-profile/education.md so they're reusable for every future form.

## 2026-07-01 — Academic data + branch correction (batch 5)
- IMPORTANT: Branch is AIML (B.Tech CSE with AI & ML specialization), NOT plain CSE.
  Corrected in education.md, about-me.md, facts.md, resume .tex.
- CGPA 7.47 (cumulative per portal; = Sem5 SGPA; simple avg of 5 sems ~7.11 → VERIFY official).
- SGPAs: S1 7.13, S2 6.50, S3 6.43, S4 8.04, S5 7.47. 0 backlogs, no history.
- 10th 88.67%, 12th 81.40%. Gender Male.
- Filled JOSH form values (education.md + application file). Resume CGPA set to 7.47.
- STILL NEED: Roll Number, DOB. Graduation % use official CGPA→% (≈74.7% via ×10 placeholder).
- JOSH eligibility is CS/IT/ECE; AIML generally counts as CS — confirm with TAP cell if strict.


## 2026-07-01 — Resume finalized + LaTeX toolchain installed
- Installed via scoop: tectonic (LaTeX engine) + poppler (pdftoppm/pdfinfo) for local compile/verify.
- Compile command: `tectonic 04-resume/tailored/josh-tech-frontend-2027.tex` → produces PDF.
- josh-tech-frontend-2027 resume: verified SINGLE PAGE, clean alignment, improved line spacing
  (linespread 1.02), certifications now as bullet points (5). Branch CSE (AI & ML), CGPA 7.47.
- Workflow note: can now locally compile + render (pdftoppm) + screenshot via temp http.server
  to visually verify any future resume before the user exports on Overleaf.


## 2026-07-01 — Resume polish round 2 (JOSH FED)
- Technical Skills: left-aligned flush (leftmargin=0pt), content refreshed/reorganized.
- Branch corrected to PLAIN CSE per Shivam (was AIML on portal). Updated resume, education.md,
  about-me.md, facts.md with a discrepancy note (match official transcript on forms).
- Project rename: "open-figma-mcp" -> "Open Figma MCP" (Title Case, consistent).
- Split combined project into two: Barterly (skill-trading) + CivicTrack (civic issues).
- Achievements reordered most-recent-first; ADDED "3rd Position - Full Stack Bootcamp (Dec 2025)".
- Headings all UPPERCASE; uniform section spacing; verified SINGLE PAGE via local tectonic+poppler.


## 2026-07-01 — Permanent automation tooling (Python)
- Added `data/profile.json` = machine-readable single source for form-fill (personal/education/links).
- Added `tools/` (all run from repo root, tested working):
  * sync_github.py — regenerates github-inventory.md + reports NEW/REMOVED/UPDATED repos
    (state in 03-projects/_github-state.json). Baseline saved (97 repos).
  * build_resume.py — tectonic compile + verifies page count (exit 2 if wrong) + --preview PNG.
  * new_application.py — scaffolds JD + application(tracker form values from profile.json) + resume copy.
  * check_health.py — lists pending/placeholder items + structure check (38 pending markers currently).
  * README.md — usage docs.
- Added `04-resume/_base-resume.tex` = reusable single-page template (copied per job, then tailored).
- Removed old PowerShell `_gen_inventory.ps1` and `_github-raw.json` (superseded by Python).
- Updated steering `_system.md` with Tools section + profile.json in memory map + sync rule.
- Workflow for any new job now: new_application.py -> paste JD -> tailor .tex -> build_resume.py --preview.


## 2026-07-01 — Policy: keep everything (no deletes)
- User wants NO file deletion; keep all for future reference.
- Restored _analyze.ps1, _gen_inventory.ps1, _github-raw.json in 03-projects/ (legacy PS tools,
  marked legacy; Python tools/ are the maintained versions).
- Added firm rule in _system.md: do not delete files (archive/mark legacy instead);
  only temp build artifacts (preview PNGs/.log) may be removed.


## 2026-07-01 — Edits: portfolio link, ITM dates/modules
- Real portfolio: https://shivam-portfolio-a1s4.onrender.com (updated resume header, base template,
  profile.json, personal.md, about-me.md). Previously header wrongly used networkedconsultancy.com.
- ITM role dates: changed "Present" -> "Feb 2026" (user said Feb 2025 but role starts May 2025 =
  impossible; assumed Feb 2026, flagged to confirm). Updated resume, base, work-and-internships.md.
- ITM modules: "academic, finance, admin" -> "admin, examination, and quiz modules".
- Resume re-verified 1 page.


## 2026-07-01 — Resume projects reordered (JOSH FED)
- Removed Open Figma MCP from resume (kept documented in index/curated).
- Added IDC Website (https://idcwebsite.onrender.com, repo IDC-WEBSITE) and
  Techrythm 2.0 TechFest site (https://techfest.itmuniversity.ac.in, repo TechFest2.0).
- Created 03-projects/idc-website.md and techrythm.md; updated projects README index.
- Resume Projects order: IDC, NETWORKED, Parakh, Techrythm, Barterly (CivicTrack dropped to fit 1 page).
- Verified single page.


## 2026-07-01 — Added Odoo achievement; projects spacing
- Added achievement: "8th Rank (Solo) - Odoo Online Hackathon" (resume + achievements.md).
- Trimmed summary to 2 lines to make room. Projects kept 5 with slight explanations.
- Resume page is now FULL; projects use default itemsep (more spacing overflows to 2 pages).
  If more air needed, drop one project/cert. Verified single page.


## 2026-07-01 — Header icons (FontAwesome) + projects next-line format
- Added icon contact header on ONE line (map-marker, phone, envelope, LinkedIn, GitHub, globe).
- Projects: title on line 1, description on next line (`\\` after title), concise 1-line descriptions.
- IMPORTANT (LaTeX/tooling): tectonic (local, XeTeX) can't load fontawesome5 fonts on this Windows
  setup (fontconfig error). Fix used: `\usepackage{iftex}\ifpdf ... fontawesome5 ... \else textbullet
  fallback \fi`. So on Overleaf (pdfLaTeX) real icons render; locally I verify layout with bullet
  fallbacks. Applied to both josh resume and 04-resume/_base-resume.tex.
- Both verified single page locally.


## 2026-07-01 — Fix: icons not showing (engine guard removed)
- Root cause: `\ifpdf` guard only loaded fontawesome5 under pdfLaTeX; if Overleaf uses
  XeLaTeX/LuaLaTeX, icons fell back to bullets. Fix: ALWAYS `\usepackage{fontawesome5}`
  (works on all Overleaf engines). Applied to josh resume + _base-resume.tex.
- build_resume.py upgraded: if a real compile fails and fontawesome5 is present, it auto-compiles
  a stubbed copy for local layout/page verification and prints "[icons stubbed locally...]".
  So icon-resumes stay locally verifiable while real icons render on Overleaf.


## 2026-07-01 — 2nd application: Stackmentalist (Python Full Stack Developer)
- Copied josh resume -> stackmentalist-python-fullstack-2027.tex; retailored for Python Full Stack.
- Changes: role subtitle, Python-first summary, skills (Python/Django/DRF/FastAPI/React/Next.js +
  Cloud/DevOps + AI/LangChain line), projects reordered to full-stack/Python (NETWORKED, Parakh,
  Better Than Claude Skills, CivicTrack, Barterly; dropped IDC & Techrythm as frontend-only).
- Added parakh live link earlier (https://parakh.itmuniversity.ac.in).
- JD: 06-job-descriptions/stackmentalist-python-fullstack-2027.md; app + form values:
  05-applications/stackmentalist-python-fullstack.md; tracker updated.
- Deadline 01 Jul 2026 10 AM, Pune, intern paid 8-15k / trainee unpaid, PPO. Form: forms.gle/btVzkDGQGv7Pj3ZH6
- HONESTY FLAG: FastAPI, Next.js, LangChain added to match JD — confirm Shivam can defend each.
- Verified single page.


## 2026-07-01 — Completeness audit
- Ran check_health; fixed what was known: GitHub username/URL (Shivam990q), product links
  (Parakh, IDC, Techrythm, Better-Than-Claude, Open Figma MCP, Inspect Helper, Barterly),
  target roles/sectors (from applications), project GitHub URLs (BTC skills, inspect-helper, barterly).
- Pending markers 37 -> 30. Remaining need Shivam's input (see below) OR are optional/trivial.
- STILL NEEDS USER INPUT: quantified impact/metrics for experience & projects; Solvitude/Banao
  "what I did" details; LeetCode/other social links; 10th/12th coursework & academic achievements;
  ROSE repo/tech; Curriculum Manager vs Parakh (same?); Own Your Identity cert date; Odoo hackathon date;
  Stackmentalist FastAPI/Next.js/LangChain confirm.


## 2026-07-01 — Deep research: JOSH Technology Group
- Saved 06-job-descriptions/josh-technology-DEEP-RESEARCH.md (company, model, tech, culture,
  comp, 8-9 round FED hiring process, prep plan).
- Key facts: JTG E-Business Software Pvt Ltd; founded 2009; bootstrapped; Gurgaon HQ; 210+ team;
  CEO Rishu Gupta; product Pod.AI; Glassdoor ~3.5/5; FED CTC 13.47L, bond 1L.
- FED interview: 8-9 elimination rounds; MCQ (neg marking, C/C++ + HTML/CSS/JS); CSS grilled;
  take-home static page (1wk) + timed screen-shared machine coding (<2h); technical PIs + HR.
- Clarified: NOT josh.ai / Josh Talks (different companies).


## 2026-07-01 — JTG FED prep: full resource hub added
- Expanded 05-applications/josh-technology-frontend-PREP.md with: detailed round-by-round + a
  COMPLETE RESOURCE HUB (YouTube channels by purpose, docs, question banks/platforms, JTG PYQ
  sources, must-master JS/CSS topics, machine-coding checklist, CN list, 7-day sprint, daily routine).
- Key channels: Namaste JS (Akshay Saini), RoadsideCoder, Kevin Powell (CSS), Codevolution (React),
  Gate Smashers (CN). Platforms: BFE.dev, GreatFrontEnd, Frontend Mentor, LeetCode. PYQ: GfG "Josh
  Technology" experiences + GitHub JOSH-TECHNOLOGY-GROUP-Assignment.


## 2026-07-01 — JTG FED direct resource LINKS file
- Created 05-applications/josh-technology-frontend-LINKS.md with clickable links: 10 GfG JTG
  interview-experience PYQ URLs, sample assignment repo, MCQ/output practice (BFE.dev, GfG),
  machine-coding (GreatFrontEnd, FrontendGeek), CSS games, docs, YouTube channels, DSA/CN.


## 2026-07-01 — Consolidated links into PREP
- Per Shivam: merged all resource links into josh-technology-frontend-PREP.md (single file);
  removed the duplicate josh-technology-frontend-LINKS.md (content moved, not lost).


## 2026-07-01 — JTG PREP made fully comprehensive
- Added to josh-technology-frontend-PREP.md: Question Bank WITH ANSWERS (15 JS output, JS concept
  Q&A, CSS concept Q&A, C/C++ MCQ samples, machine-coding approach + template, take-home rubric);
  Behavioral/HR scripts tailored to Shivam (self-intro, "Why JTG", HR Q&A, questions to ask);
  Logistics (day-before, MCQ strategy, common mistakes); and a Progress Tracker + mistakes log.
- PREP file now covers: rounds, checklists, resources, direct links, Q&A bank, HR scripts, tracker.


## 2026-07-01 — Clickable TOC for PREP + reusable tool
- Added tools/add_toc.py: inserts explicit `<a id="sec-N">` anchors before every heading + a
  Table of Contents (between <!-- TOC START/END -->) after the title. Idempotent, numeric anchors
  (work in GitHub/VS Code/Kiro). Skips fenced code blocks.
- Ran on josh-technology-frontend-PREP.md (78 TOC entries). Reuse on any md: `python tools/add_toc.py <file>`.
