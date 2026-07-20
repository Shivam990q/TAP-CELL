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


## 2026-07-01 — Stackmentalist Python Full Stack PREP created
- Created 05-applications/stackmentalist-python-fullstack-PREP.md (mirrors JOSH structure):
  company snapshot, inferred 3-5 round process, topic checklists (Python/DSA, SQL, Django/DRF,
  FastAPI, React/Next, async/MQ, LangChain), Q&A bank with answers, resource links, HR scripts
  (tailored), 10-day plan, progress tracker. Added clickable TOC (40 entries) via add_toc.py.
- Note: Stackmentalist = small Pune startup, limited public interview data → plan built from JD skills.


## 2026-07-01 — Stackmentalist DEEP RESEARCH added
- Fetched rendered stackmentalist.com: full company profile (StackMentalist Ventures Pvt Ltd,
  Hinjewadi Pune + Dubai; services; full tech stack incl FastAPI + LangChain/ChromaDB/OpenAI;
  clients Vinkapp/Anujan/Procureasify; InnovateX hackathon). Added a "Company snapshot — Deep
  Research" section to stackmentalist-python-fullstack-PREP.md + refreshed TOC (45 entries).
  Also saved company facts to memory/facts.md.


## 2026-07-01 — MEGA RESOURCE VAULT added to both PREP files
- Researched & added curated GitHub repos + platforms to both prep files:
  * JOSH (frontend): yangshun/front-end-interview-handbook, lydiahallie/javascript-questions,
    sudheerj js+react questions, 33-js-concepts, suveshmoza FE-Interview-Preparation, tech-interview-handbook,
    system-design-primer, DSA-SHEETS, BFE.dev, GreatFrontEnd, JavaScript30, NeetCode, PrepInsta/InterviewBit/AmbitionBox.
  * Stackmentalist (backend/py): rohan-paul Awesome-Python-Django-Interview, rohanmistry231 FastAPI prep,
    Devinterview django/api-design, Tanu-N-Prabhu Python, TheAlgorithms/Python, full-stack-interview-qa,
    system-design-primer, DataLemur/SQLBolt/LeetCode SQL50, LangChain/LangGraph/Chroma docs.
- Noted community Google Drive/Notion/Telegram compilations exist but flagged as unofficial (prefer repos).
- Refreshed TOCs: JOSH 84 entries, Stackmentalist 53 entries.


## 2026-07-01 — Resources v2 added to both PREP files
- JOSH: roadmap.sh (frontend/js/react), GreatFrontEnd GFE75 + playbook + React-19 Qs, FrontendLead,
  mock interviews (Pramp, interviewing.io), Grind75/Blind75 repos, DSA cheat sheets, CSS/JS cheatsheets
  (malven flex/grid, css-tricks almanac, devdocs).
- Stackmentalist: roadmap.sh (backend/python/full-stack/system-design), Grind75/Blind75 (Python),
  Strivers SDE (Python), SQL practice (DataLemur/StrataScratch/SQLZoo/use-the-index-luke), mock
  interviews, python-cheatsheet (gto76), testdriven.io, system-design-primer + ByteByteGo, extra YouTube.
- Refreshed TOCs: JOSH 91, Stackmentalist 61. Audit: PREP files comprehensive; 37 pending markers
  are profile/experience metrics (need Shivam's real numbers), not prep/resume gaps.


## 2026-07-01 — 3rd application: Infosys (Specialist Programmer / DSE)
- Campus drive via TAP Cell; deadline 02 Jul 2026 10 AM. Form: forms.gle/QC928sKwwaMJf3L96.
- Roles: SP L1/L2/L3 (10/16/21 LPA) + DSE (6.25 LPA). Test tier decides package. PAN India.
- Process: online coding test (3 DSA Qs, 180 min, medium-hard, DP-heavy) → 60-min technical interview
  (DSA + DBMS/OS/CN/OOP + SQL + projects). Proctored via Wingspan. Eligibility: 60/65% + 6 CGPA,
  NO active backlogs (Shivam: 10th 88.67, 12th 81.40, CGPA 7.47, 0 backlogs -> eligible; simple-average note).
- Created: JD (infosys-specialist-programmer-2027.md), application + form values
  (infosys-specialist-programmer.md), resume (copied base -> tailored as Software Engineer, DSA/CS-fundamentals
  emphasis; 1 page verified), PREP (deep research + DSA topic plan + must-do problems + CS-fundamentals Q&A
  + HR + MEGA resource vault + 2-week sprint + tracker; TOC 24 entries). Tracker updated.
- Resources: Striver A2Z/SDE, NeetCode150, Aditya Verma DP, GfG Infosys SDE Sheet, LeetCode/Codeforces/Code360,
  Great Learning/Educative/PrepInsta guides, Gate Smashers (CS fundamentals).
- Key: DSA (esp DP) is the make-or-break; do timed 3Q/180min mocks.


## 2026-07-01 — Infosys resume rebuilt from JOSH format
- Per Shivam: copied josh-tech-frontend-2027.tex (preferred format) over infosys resume, then adapted:
  subtitle "Software Engineer"; summary = DSA + C++/Java/Python + full-stack; skills = Languages /
  CS Fundamentals (DSA/OOP/DBMS/OS/CN) / Full-stack / Tools&Cloud; projects = NETWORKED, Parakh,
  Better Than Claude Skills, CivicTrack, Barterly (dropped IDC & Techrythm). Verified single page.


## 2026-07-01 — Infosys PREP: MEGA RESOURCE VAULT v2 added
- Added Infosys/HackWithInfy PYQ repos (karthikreddy-7/Infosys-SP-Coding-Questions,
  itsmeheisenberg/HackWithInfy, shubhammore9/InfyTQ_Coding, SUDARSHANTADAGE/InfyTQ-Answers),
  PrepInsta SP/HackWithInfy coding pages, Codeforces Infosys OA blog, DP resources (Aditya Verma,
  Striver, Grokking DP, DP-pattern repos), DSA-pattern repos (Chanda-Abdul, PranabNandy, NeetCode
  roadmap, 14-patterns gist), online judges (LeetCode/CF/CC/AtCoder), lang-specific + CS fundamentals.
  Refreshed TOC (32 entries).


## 2026-07-02 — Infosys PREP deep research v2 + resume edits
- Resume edits (per Shivam): removed C++ (summary+skills); swapped Better Than Claude Skills -> Autonomy
  (Social Media Automation, Python); swapped CivicTrack -> NewsFlow (Astro news aggregator). 1 page verified.
- CGPA corrected everywhere earlier: 7.11 (simple avg of 5 SGPAs; 7.47 was only Sem-5 SGPA; portal cumulative N/A).
- Added DEEP RESEARCH v2 to infosys PREP: EXACT cutoffs (1-1.5Q->DSE, 2Q->SP, 3Q->top/L3), InfyTQ cert tip,
  real technical interview Q&A (OOP/DBMS/SQL/OS/CN/Java), SP frequently-asked coding problems, extra links
  (InfyTQ, faceprep, Great Learning, techprep, interviewquery, GfG SDE sheet, PrepInsta). TOC 47 entries.
- GitHub sync: 98 repos (new TAP-CELL — flagged it's PUBLIC & has personal data -> advise make private).


## 2026-07-02 — Infosys PREP: ULTIMATE RESOURCE INDEX added
- Added exhaustive 15-category resource index to infosys PREP: official (HackWithInfy/InfyTQ),
  coding platforms (LeetCode/GfG/Code360/HackerRank/InterviewBit/Codolio), CP (Codeforces/CSES/
  AtCoder/cp-algorithms/CodeChef), sheets/roadmaps (Striver A2Z+SDE/NeetCode/Grind75/Babbar450),
  YouTube DSA (Striver/Aditya Verma/Abdul Bari/NeetCode) + CS fundamentals (Gate Smashers/Knowledge
  Gate), GitHub banks, cheatsheets (bigO/DSA/SQL), PYQ (GfG/PrepInsta/faceprep/Glassdoor/AmbitionBox),
  LinkedIn strategy, Telegram (with caution), Google Drive/Scribd (with caution), mock interviews
  (Pramp/interviewing.io), HR, aptitude note. TOC now 64 entries. Flagged unofficial sources.


## 2026-07-02 — JOSH PREP: ULTIMATE RESOURCE INDEX added
- Added exhaustive 15-category frontend resource index to josh-technology-frontend-PREP.md
  (JTG PYQ, FE platforms GreatFrontEnd/BFE/FrontendLead, JS/CSS practice, machine coding, DSA-lite,
  YouTube JS/CSS/React + CN, GitHub repos, docs/books, cheatsheets malven/cssreference, roadmaps,
  technical-round theory, LinkedIn strategy, Telegram/Drive with caution, mock+HR). TOC 108 entries.
- (User's message said "Infosys" but pointed to josh PREP file — treated as JOSH frontend index.)


## 2026-07-02 — Stackmentalist PREP: ULTIMATE RESOURCE INDEX added
- Added exhaustive 16-category Python-full-stack resource index (Python/DSA/SQL, Django/DRF, FastAPI,
  React/Next, system design, LangChain, YouTube, GitHub banks, cheatsheets, roadmaps, PYQ, LinkedIn/
  Telegram/Drive with caution, mocks, HR) + reality-check (execution focus). TOC 79 entries.
- All 3 companies' PREP files now have full ULTIMATE RESOURCE INDEX + TOC. Advised execution > more links.


## 2026-07-02 — Saved marksheet + POD-form data
- 10th: MPBSE, 2020, 88.67% (266/300), English medium; 12th: MPBSE, 2022, 81.40% (407/500), PCM.
  School: Ganga Public Higher Secondary School, Duttapura, Morena. (education.md + profile.json)
- Academic gap: 12 months (12th 2022 -> B.Tech 2023); reason = IIT-JEE preparation.
- CGPA corrected to 7.11 (simple avg of 5 SGPAs; 7.47 was Sem-5 SGPA; portal cumulative N/A) everywhere.
- Added to profile.json: languages (English/Hindi), marital status Single, father Mukesh Gupta,
  mother Alpana Gupta, current address (Godamkoot, Mala Road, Gwalior 474001), permanent (Choti
  Bazaria, Jiwaji Ganj, Morena 476001) — flagged to verify exact spelling.
- JOSH POD portal: profile fully filled but final submit showed "Registration closed" (already
  registered via Google Form earlier). Drafted email to support@pod.ai + TAP cell to resolve.

## 2026-07-11 — Infosys official Application for Employment submitted
- Completed the 89-question Infosys "Application for Employment" form (the mandatory campus
  recruitment application emailed by Talent.Acquisition@infosys.com; deadline Sun 12 Jul 2026).
- Filled from `data/profile.json`. Key values used:
  - Personal: Shivam Gupta, MALE, DOB 31/07/2004, email guptashivam93660@gmail.com, mobile 8269699824.
  - Passport: NO (has other govt IDs but no passport). Citizenship: Indian.
  - Communication address: Gwalior (current) — pincode 474001; post office to verify.
  - Education (simple-average per form instruction): X 88.67% (MPBSE, 2020), XII 81.40% PCM (MPBSE,
    HSC, 2022), B.Tech CSE ITM University Gwalior 7.11 CGPA, passing 2027.
  - Backlogs: NO. Gaps: YES — 12 months, reason JEE/competitive-exam prep drop year.
  - Association with Infosys previously: NO. Director/Partner/Criminal declarations: all NO.
  - Uploads: passport photo (<512KB), resume PDF (<2MB), college/govt photo ID PDF (NOT Aadhaar).
  - Declaration: I Agree + captcha.
- User confirmed all uploads done and submitted.
- NOTE reaffirmed: use 7.11 simple-average CGPA (NOT 7.47 sem-5 SGPA) — Infosys declaration requires
  simple average of all subjects/semesters.
- Next: await shortlist; grind DSA (DP/graphs/arrays) for 3-question / 180-min coding test.

## 2026-07-11 — Infosys deep research (2026) compiled
- Created `05-applications/infosys-DEEP-RESEARCH-2026.md` from fresh 2026 web sources.
- Key new findings vs old PREP:
  - Test = 3Q/180min, no sectional limit; Q1 easy 20 marks (DS/algo), Q2 medium 30 (Greedy),
    Q3 hard 50 (DP). Partial scoring by test cases. Langs C/C++/Java/Python/JS.
  - Selection = test-cases-passed × difficulty × approach. Strong partials beat one perfect solve.
  - Real timeline (last cycle): qualifier ~July 12, results ~July 24, split Cat1 (immediate offline
    interviews, top→SP+hackathon ~100, decent→DSE) vs Cat2 (direct SP/DSE interviews). Interviews
    Sep–Dec, final results Jan–Feb. Both start as "Power Intern".
  - Interview: offline, live coding ~45 min solve 1 of 2 in front of interviewer; carry laptop +
    hardcopy resume + 2-slide PPT (intro + goals). Topics: trees/graphs/DP/recursion/binary
    search/greedy/sliding window; OOP+design patterns; DBMS joins/normalization/window functions +
    SQL on paper; OS/CN basics; ★ NEW basics of ML/GenAI (HWI 2026 is AI-themed) — Shivam's agent/
    GenAI work (ROSE, MCP, CrewAI) is a differentiator to lead with.
  - ★ 2026 integrity crackdown: Infosys flagged proxy/identity-theft, paused tests to tighten
    verification → expect stricter ID checks + heavy proctoring. Tab/window/app switch = auto violation.
  - InfyTQ free cert boosts SP shortlist.
- Game plan emphasis: over-index DP+Greedy, do 3 timed 3Q/180min mocks, InfyTQ cert, rehearse
  self-intro + projects + GenAI talk, zero integrity risk, yes to relocation/any-tech.

## 2026-07-11 — Infosys emails reviewed, both files updated with missing details
- Cross-checked the Infosys program email (09 Jul) + ITM TAP notice (01 Jul, reopened 03 Jul).
- Added to JD + application files:
  - Program name: "Infosys Campus Recruitment Program 2026-27"; Shivam nominated by ITM.
  - Official form deadline 12 Jul 2026; must use only the invited email; shortlist based on form.
  - ★ IMPORTANT DISCREPANCY: Infosys email says assessment + interview are **IN-PERSON** (phased);
    ITM notice called the test "internet-based." Flagged to confirm exact mode with TAP Cell.
  - Eligibility nuance: better of Class XII / Diploma considered; simple average incl. all subjects.
  - Full eligible specializations list; ITM TAP contact tap.cell@itmuniversity.ac.in (Sahil Chhabria, CRPO).
  - Queries only to talent.acquisition@infosys.com.

## 2026-07-11 — Infosys DSE-focused prep files created
- Created `05-applications/infosys-1WEEK-DSE-PLAN.md` — 7-day intensive plan to clear DSE anyhow
  (Q1 full + Q2/Q3 partials), day-by-day checkboxes, daily routine, golden rules, + a "saari files
  order me" index of all Infosys files and what each is for.
- Created `05-applications/infosys-QUESTION-BANK.md` — topic-wise must-do problems (priority map:
  Arrays/Strings/Hashing + Greedy + DP basics for DSE), CS fundamentals Q&A, ML/GenAI angle, HR.
- DSE target logic reaffirmed: ~1–1.5 questions worth of test cases clears DSE; 2 full solves → SP.

## 2026-07-11 — Infosys GOLDMINE research merged into existing files
- Ran market research on real SP/DSE PYQ. Merged (no new files):
  - `infosys-QUESTION-BANK.md`: added GOLDMINE section — real PYQ problem-types table w/ LeetCode
    equivalents, exact resources (Striver, Aditya Verma DP, Gate Smashers, NeetCode, InfyTQ),
    Infosys PYQ GitHub repos, a curated **40-problem list in 3 tiers** (Tier1=20 DSE-lock,
    Tier1+2=32 SP chance, all 40 = SP L2/L3), and project-connected interview answers (self-intro,
    NETWORKED/Parakh/ROSE/MCP/CrewAI hooks, CS fundamentals, HR).
  - `infosys-DEEP-RESEARCH-2026.md`: added real PYQ patterns + ⚠️ possible 2026 pattern change
    (aptitude + pseudo-code tracing common gate in some SP processes) — our campus JD says pure
    coding 3Q/180min; flagged pseudo-code as insurance + confirm with TAP Cell.
- Key intel: FacePrep/TechPrep report a common OA gate (aptitude/pseudo-code/coding) for SE/SP/PP in
  2026; PrepInsta says SP/DSE process differs from SE. Our JD = pure coding. Verify with TAP Cell.

## 2026-07-11 — Infosys pattern CONFIRMED + full solutions file created
- User confirmed via ITM TAP Cell MEETING: test = **3 coding questions / 180 min, PURE CODING**
  (no aptitude, no pseudo-code). Updated DEEP-RESEARCH + QUESTION-BANK to mark this RESOLVED
  (removed the pseudo-code "insurance" ambiguity).
- User wants FULL answers to every goldmine question (never done LeetCode/DP before but learns fast;
  will sit 1 week, understand logic + patterns from solutions).
- Created `05-applications/infosys-SOLUTIONS.md` — FULL solutions for all 40 goldmine problems in
  Python: each with Pattern → Samajh (approach) → Code → Complexity → Key insight. Organized in
  Tier 1 (20 DSE-lock), Tier 2 (12 SP push), Tier 3 (8 SP L2/L3), + a 12-pattern cheat-sheet at end.
- User preference noted: redundancy is FINE (don't consolidate); just wants all important questions
  + answers in one place. God-level learner, 90+ projects, 5+ yrs hardware/software; grasps concepts
  in one pass but has zero DSA practice — so solutions/patterns matter more than drilling.
- File order index updated (1WEEK plan) to include SOLUTIONS as #6.

## 2026-07-11 — Infosys ESSENTIALS (zero-gaps foundation) created
- User's ask: he grasps anything in one pass but can't handle what's NOT in his "data" (no unknown
  unknowns allowed). Wants every smallest detail covered.
- Created `05-applications/infosys-ESSENTIALS.md` — the plumbing a first-timer misses:
  test mechanics + partial scoring, full Python cheat sheet (fast stdin I/O, collections, heap,
  deque, sorting/comparator, string/math ops), constraints→algorithm table, universal 6-step
  problem template, PATTERN-TRIGGER table (keyword→pattern), universal edge-case checklist,
  common bugs/traps (off-by-one, int division, [[0]*n]*m pitfall, recursion limit), Big-O refresher,
  test-day micro-checklist.
- Language chosen: Python 3 (least boilerplate). Java version pending user confirmation.
- File index in 1WEEK plan updated: ESSENTIALS = read FIRST (#7 listed but marked "sabse pehle").

## 2026-07-11 — 05-applications & 06-job-descriptions reorganized company-wise
- Moved all files into per-company subfolders. Structure now:
  - `05-applications/infosys/` (7 files: 1WEEK-DSE-PLAN, DEEP-RESEARCH-2026, ESSENTIALS,
    QUESTION-BANK, SOLUTIONS, specialist-programmer-PREP, specialist-programmer)
  - `05-applications/josh-technology/` (frontend-PREP, frontend)
  - `05-applications/stackmentalist/` (python-fullstack-PREP, python-fullstack)
  - `05-applications/` root keeps: tracker.md, _TEMPLATE.md
  - `06-job-descriptions/infosys/`, `/josh-technology/`, `/stackmentalist/`; root keeps README.md
- Updated cross-references (relative paths) in moved files, tracker.md detail paths, 1WEEK index,
  06 README, and steering `.kiro/steering/_system.md` memory map (new company-wise paths).
- Intra-company links use bare filenames (same folder); cross-folder use ../../<folder>/<company>/.

## 2026-07-11 — Workspace consistency pass after company-wise reorg
- Full audit done. Updated automation to match new structure:
  - `tools/new_application.py`: now creates `06-job-descriptions/<company>/<slug>.md` and
    `05-applications/<company>/<slug>.md` (added --company-slug arg; default = slugify(company)).
    Templates + tracker row + JD path references updated to company-wise paths.
  - `tools/add_toc.py`: usage example path updated to subfolder.
  - `tools/check_health.py`: no change needed — uses rglob (recurses into subfolders).
- memory/log.md historical entries left as-is (they record past state; not broken links).
- Confirmed: all content files, cross-references, tracker, steering memory-map, and 06 README are
  consistent with the company-wise structure. Root folders intact (01–06, data, memory, tools).

## 2026-07-11 — Full workspace structure audit
- Reviewed all main folders. Verdict:
  - 01-profile (4 files), 02-experience (2), 04-resume, data, memory, tools = already clean &
    single-purpose; NOT restructured (over-structuring small folders adds nav overhead + would
    break tool/steering references). Left as-is intentionally.
  - 03-projects: 12 project docs + `_`-prefixed inventory tooling/data. sync_github.py HARDCODES
    `03-projects/github-inventory.md` + `_github-state.json`; .ps1 scripts use $PSScriptRoot to find
    `_github-raw.json`. So moving these = risk with low benefit → left as-is (already grouped by `_`).
  - Updated root `README.md` Structure + Workflow to document company-wise subfolders + tools flow.
- Cleanup candidate flagged (NOT done — needs user OK): `.playwright-mcp/` ~40 temp browser logs
  (.log) + screenshots (.png/.yml) = junk from earlier form automation. Firm rules allow deleting
  temp .log/PNG artifacts; awaiting user confirmation before removing.

## 2026-07-11 — 04-resume/tailored reorganized company-wise
- Moved tailored resumes into per-company subfolders:
  - `04-resume/tailored/infosys/` (infosys-specialist-programmer-2027.tex + .pdf)
  - `04-resume/tailored/josh-technology/` (josh-tech-frontend-2027.tex)
  - `04-resume/tailored/stackmentalist/` (stackmentalist-python-fullstack-2027.tex)
  - `.gitkeep` stays at tailored/ root.
- Updated all resume-path references: infosys/josh/stackmentalist application files, infosys JD
  tailoring note, `tools/new_application.py` (resume path now company-wise + template + prints),
  `tools/build_resume.py` usage, `tools/README.md`, `05-applications/_TEMPLATE.md`, steering _system.md.
- new_application.py diagnostics clean. Now consistent: 04/05/06 all company-wise.
- memory/log.md historical entries left as-is (past-state records).

## 2026-07-11 — Consistency/freshness audit (facts, steering, CGPA)
- Found + fixed staleness the earlier passes missed:
  - `.kiro/steering/about-me.md`: CGPA 7.47 → 7.11 (auto-loads every chat; was contradicting all
    other files). Added "Active applications" block + company-wise structure note + "use 7.11" rule.
    Replaced non-existent `04-resume/master-resume.md` reference with real `_base-resume.tex` + tailored.
  - `memory/facts.md`: was last-updated 2026-06-30 (missing all July activity). Added active
    applications (Infosys submitted, josh/stackmentalist), company-wise repo structure, Infosys prep
    set list; bumped date to 2026-07-11.
  - `.kiro/steering/_system.md`: fixed 3 `master-resume.md` pointers → `_base-resume.tex`/tailored.
  - CGPA form-values corrected 7.47 → 7.11 (simple avg) in josh + stackmentalist application files
    and Infosys JD "fit" line (were inconsistent with education.md/profile.json/Infosys decision).
- Verified remaining 7.47 mentions are all correct-context (explaining Sem-5 SGPA), not form values.
- Now consistent end-to-end: .kiro, 01-06, data, memory, tools all aligned on 7.11 + company-wise structure.

## 2026-07-11 — Infosys files organized via master INDEX (README)
- Created `05-applications/infosys/README.md` = master index organizing all 7 Infosys files
  category-wise + type-wise + reading-order (line-wise):
  - A Application (specialist-programmer.md) · B Strategy (DEEP-RESEARCH-2026) ·
    C Plan/Reference (1WEEK-DSE-PLAN, PREP) · D DSA Prep (ESSENTIALS→QUESTION-BANK→SOLUTIONS).
  - Includes reading-order flow, quick-start, category summaries.
- Decision: kept the 7 files FLAT in infosys/ (not split into subfolders) because they are tightly
  cross-linked; subfolders would break links + hurt navigation for only 7 files. README is the
  organized view. (Same judgment as 03-projects: avoid over-fragmentation.)

## 2026-07-11 — Infosys files numbered for explorer order
- Added numeric prefixes (kept original names) so files sort in reading order:
  README · 01-specialist-programmer · 02-DEEP-RESEARCH-2026 · 03-ESSENTIALS · 04-1WEEK-DSE-PLAN ·
  05-QUESTION-BANK · 06-SOLUTIONS · 07-PREP.
- Updated ALL references to new numbered names: README (rewritten), 04 file-index table + companion
  line, cross-refs in 01/02/05/06, tracker.md (01-...), 06 JD (02-DEEP-RESEARCH), facts.md prep-set list.
- Verified: no stale un-numbered inline refs remain (grep clean).

## 2026-07-11 — Coverage audit → filled gaps for BOTH roles (DSE + SP)
- Honest audit found 2 gaps:
  1. Interview CS-fundamentals were TOPIC-only (no actual answers) in PREP/QUESTION-BANK.
  2. DSA solutions missing trees, backtracking, linked-list (interview + SP-relevant).
- Fixed:
  - Appended TIER 4 to `06-infosys-SOLUTIONS.md` (11 new: subsets, permutations, combination sum,
    max-depth, diameter, LCA, validate BST, level-order, reverse-LL, detect-cycle, merge-LL).
    Now 51 solutions, 15 patterns (added backtracking, tree DFS/BFS, fast-slow pointer).
  - Created `08-infosys-INTERVIEW-CS.md` — FULL crisp answers: OOP (with code), DBMS/SQL (queries),
    OS, CN, ML/GenAI (ROSE/MCP/CrewAI hooks), Java/Python quick, HR.
  - Updated README (added Category E interview + ROLE COVERAGE table), 04 index table, facts.md.
- Verdict: both roles now covered end-to-end (test + interview). 8 numbered files + README.

## 2026-07-11 — Added real Infosys-style MOCK PAPERS (test-feel gap filled)
- User: solutions felt like renamed LeetCode; wanted ACTUAL Infosys-style problem statements so the
  onsite test feels familiar (mock-like).
- Researched real Infosys SP/DSE PYQ (PrepInsta, GfG OA experiences Dec 2024, Scribd 2024-25, HWI 2026).
- Created `09-infosys-MOCK-PAPERS.md`:
  - 2 full MOCK SETS (3Q/180min each, story-wrapped Infosys style with Input format/Constraints/
    Sample I/O/Explanation + collapsible approach+solution): Popular Product, Festival Stalls,
    Warehouse Partition (split-array-k-segments DP); Secret Code Palindrome, Treasure Picker (Khaled
    N/2 greedy), Cashier Min Notes (coin change).
  - REAL PYQ BANK with statements+approach: Hungry Fish, GET(l,r) max pairs, Spiral Matrix (HWI 2026),
    Largest Number, Subset Sum, Drying Walls/Painter, Count-distinct-subarray.
  - Test-day mock strategy.
- Updated README (file order, Category D row, reading step MOCK), 04 index + Day-7 mock line, facts.md.
- Infosys folder now: README + 01-09 (9 numbered files).

## 2026-07-11 — Made QUESTION-BANK + SOLUTIONS "real" (Tier 5 real PYQ)
- Appended TIER 5 to `06-infosys-SOLUTIONS.md` — 8 REAL Infosys PYQ with full story-statements +
  solutions: Split-array-K-segments (DP), Painter's Partition (BS-on-answer), Aggressive Cows
  (BS-on-answer), Job Sequencing (greedy), Prime pairs (Sieve), Distinct-in-window (sliding),
  Subset Sum (DP), Khaled N/2 (greedy) + 5 approach-only (Hungry Fish, GET(l,r), guest-serving,
  spiral, binary-string). Sources: PrepInsta, GfG OA 2024-25, Scribd PYQ, HWI 2026.
- Added "REAL INFOSYS PYQ INDEX" to `05-infosys-QUESTION-BANK.md` — categorized real-PYQ→solution map.
- Integrated real PYQ into `04-infosys-1WEEK-DSE-PLAN.md` (Days 4/5/6 + top callout; Day7 mock uses 09).
- Honesty framing kept: can't guarantee identical live questions; these are real reported problems +
  patterns → test will feel familiar. Not fabricated as "guaranteed exact".

## 2026-07-11 — Made files self-contained (removed all "approach-only/reference-only")
- User wanted everything IN the files (no "see link / figure it out / detail elsewhere").
- Audited via grep for deferral markers. Fixed:
  - `06-SOLUTIONS.md`: replaced the "REAL PYQ — approach only" block with **Tier 5 (contd.) R9-R13
    FULL solutions**: Hungry Fish (greedy, verified on example), GET(l,r) max pairs, Guest Serving
    (next-greater), Spiral Matrix (full code), Longest run + Max-consecutive-ones-with-K-flips.
    Now 64 full solutions total (Tier1-4 core + Tier5 R1-R13 real PYQ). No approach-only left.
  - `05-QUESTION-BANK.md` + `04-1WEEK`: CS-fundamentals pointers redirected from PREP (topics only)
    to `08-INTERVIEW-CS.md` (actual full answers).
  - `09-MOCK-PAPERS.md`: real-PYQ bank now notes full code is in 06 Tier 5.
  - README solution count updated to 64, marked self-contained.
- Remaining external links (YouTube/Striver/InfyTQ) are legit resource links, not missing content.

## 2026-07-11 — Executed "real-exam" prompt: full-statement mocks + pattern-mixed (existing files enriched)
- User gap: QB questions were 1-liners (unreal); wanted full story-wrapped real-exam problems, mixed
  companies, pattern-mixed (layered) problems, deep research. Enrich existing files only (no new files).
- Deep research: SP 2025 (LeetCode discuss) = offline, 2 problems, "solve 1 fully", topics greedy/
  knapsack/DP/trees/graphs/segment-fenwick; company OA problems (Wipro sock-pairs, Accenture feed-rats,
  Y→X working-backwards). Sources logged in files.
- `09-MOCK-PAPERS.md` (enriched): added MOCK SET 3,4,5 (9 more full story-wrapped Q with solutions:
  sock-pairs, feed-rats, burst-balloons interval-DP, reach-number, meeting-rooms-II heap, edit-distance,
  balanced-brackets, fractional-knapsack, longest-palindromic-subsequence). Now 5 sets = 15 problems.
  + PATTERN-MIXED section (MX1 book-allocation BS+greedy, MX2 task-scheduler greedy+math, MX3 cheapest-
  flights graph+DP, MX4 distinct-window sliding+hash). + REAL EXAM SIMULATOR 6-step guide.
- `05-QUESTION-BANK.md`: added intro clarifying 1-liners = topic-checklist; full real problems in 06 Tier5
  + 09 (routed). `06` unchanged (already 64 full). README + facts updated.
- Honesty kept: no "guaranteed exact Q" claim; framed as real patterns + layered + timed sim = familiar.

## 2026-07-11 — QUESTION-BANK Tier-1 converted to FULL statements (zero-DSA friendly)
- User (zero DSA) confused: QB Tier-1 problems were 1-liners ("Two Sum — hashmap") — useless for a
  beginner + not how Infosys actually asks. Confirmed: Infosys asks FULL story-wrapped problems, NOT 1-liners.
- Fixed `05-QUESTION-BANK.md`: replaced Tier-1 20 one-liners with 20 FULL real-Infosys-style statements
  (Hinglish story + Input/Output format + Constraints + Sample I/O + explanation), each → solution # in
  `06-SOLUTIONS.md`. Kept a name-only quick-checklist below for later revision.
- Tier 2-3 still name-checklist (they map to `06` #21-40 full solutions); can convert on request.

## 2026-07-11 — Filled zero-DSA gap: "DSA FROM ZERO" teaching added
- Read 03-ESSENTIALS; found it had plumbing/triggers but never TAUGHT the concepts (a zero-DSA person
  can't use "Sliding Window"/"HashMap" triggers without knowing what they are).
- Added to `03-infosys-ESSENTIALS.md` a big "DSA FROM ZERO" section:
  - Part A: Big-O/complexity via analogy (book-search) + N→algo rule.
  - Part B: 9 data structures zero se (Array/HashMap/Set/Stack/Queue/Heap/Tree/Graph/LinkedList) —
    each with real-life analogy + when + Python.
  - Part C: all 15 patterns zero se — kya + analogy + kab + kaise + mini example + link to 06 #.
  - Part D: zero-DSA learning roadmap (order to learn).
- Cross-linked: ESSENTIALS intro flags it; 06-SOLUTIONS intro points here for unknown concepts;
  04-PLAN got a "Day 0 FOUNDATION" (read DSA-from-zero before Day 1). facts.md updated.
- Now a true zero-DSA learner can understand in one read, then use QUESTION-BANK/SOLUTIONS/MOCKS.

## 2026-07-11 — Completeness verified: QUESTION-BANK + SOLUTIONS + MOCK all complete
- Found QB Tier-2/3 were still 1-liners → converted ALL to full statements.
  QUESTION-BANK now: Tier1 (20) + Tier2 (12) + Tier3 (8) = 40 FULL-statement problems (story+I/O+
  constraints+sample+solution#) + real-PYQ index + interview + HR. COMPLETE.
- SOLUTIONS verified via grep: #1-40 (Tier1-3) + #41-51 (Tier4 trees/backtracking/LL) + R1-R13
  (Tier5 real PYQ) — all with full code. COMPLETE.
- MOCK-PAPERS verified: MOCK SET 1-5 (15 full problems) + MX1-MX4 (pattern-mixed) + REAL EXAM
  SIMULATOR. COMPLETE.

## 2026-07-11 — Added complete SOURCE/REFERENCE MAP (every question traceable)
- User asked if every question has an exact reference/source. Honest: Tier 5 + mocks had per-problem
  sources, but Tier 1-4 standard problems didn't each carry an exact source line.
- Added "SOURCE / REFERENCE MAP" to `05-QUESTION-BANK.md`: every problem → exact origin
  (LeetCode number / GfG / Infosys PYQ source): Tier1 (LC 1,121,53,169,242,125,26,283,88,704,35,3,560,
  49,70,198,322,55,56,20), Tier2 (LC 179,435,134,GfG-knapsack,416,1143,300,72,64/62,200,994,207),
  Tier3 (LC 42,496,239,215,347,GfG-dijkstra/743,GfG-palindrome,136/421), Tier4 (LC 78,46,39,104,543,
  236,98,102,206,141,21), Tier5 R1-R13 (PrepInsta/GfG-OA/Scribd/karthikreddy/HWI origins), mocks +
  master resource links. Honest note: standard = LeetCode canonical (not exact-guaranteed); Tier5 = real reported.

## 2026-07-11 — Provenance labeling added (real vs AI, honest)
- User wanted every content piece labelled: real-sourced vs AI-generated/reworded/explained.
- Added master "PROVENANCE INDEX" + LEGEND to `README.md` (file-by-file real% vs AI%, honest bottom line).
- Added a top-of-file PROVENANCE banner to all 9 numbered files (01-09) classifying content:
  01 factual · 02 ~85% WEB-VERIFIED · 03 ~90% AI-EXPLANATION · 04 ~80% AI-GENERATED plan ·
  05 Tier1-4 AI-REWORDED of SRC-LC# + Tier5 REAL-PYQ · 06 problems SRC/PYQ + code AI-EXPLANATION ·
  07 ~70% SRC resources · 08 ~95% AI-EXPLANATION (standard CS) · 09 mock stories AI-GENERATED + PYQ bank REAL-PYQ.
- Tags: [SRC][WEB-VERIFIED][REAL-PYQ][AI-REWORDED][AI-GENERATED][AI-EXPLANATION][UNVERIFIED].
- Honest bottom line documented: real-reported Infosys content (02, Tier5, PYQ bank, WEB-VERIFIED) vs
  standard LeetCode-canonical (Tier1-4, AI-reworded) vs AI's own teaching/practice (03,04,08,09 stories,
  all code). No fake sources. Never claimed "exact same question guaranteed".

## 2026-07-19 — Infosys: added META file (DSA map + vocabulary + decision-engine + how-to-ask-AI)
- Trigger: user pasted a long Gemini voice-chat (Hinglish) where he kept circling ONE unmet need —
  he wanted the full DSA "tree", ALL the terminology with clear DIFFERENCES, the pattern-recognition
  decision-logic, and (his actual workflow) exactly WHAT/HOW to ask an AI to generate his `.md` notes.
  His pain: "mujhe hi nahi pata main kya poochun" (didn't know the vocabulary → couldn't ask). Gemini
  kept giving shallow/repetitive answers and over-loading advanced noise (amortized analysis, memory
  hierarchy, compiler design, concurrency, system design) irrelevant to a 10-day coding round.
- Read 03-ESSENTIALS first to match voice + avoid duplication. Existing files already have the CONTENT
  (Big-O basics, 9 DS, 15 patterns, constraints→algo table, keyword→pattern triggers, edge-cases, bugs,
  64 solutions, mocks). The gap was the META/orientation layer (map + language), not more problems.
- Created `05-applications/infosys/10-infosys-DSA-MAP-AND-VOCAB.md` (~95% AI-EXPLANATION, matches
  PROVENANCE convention). Structure:
  - PART 1 — full DSA taxonomy TREE (ASCII), branch one-liners, each tagged [TEST-CORE]/[INTERVIEW]/
    [EXTRA-skip]; + SCOPE callout explicitly telling him to IGNORE the advanced noise Gemini pushed.
  - PART 2 (the core) — terminology dictionary in 7 groups WITH DIFFERENCES + a "GALTI YAHAN HOTI HAI"
    note each: (1) levels: topic/pattern/algorithm/technique/DS/ADT/paradigm; (2) complexity: time/
    space/O/Θ/Ω/best-avg-worst/amortized; (3) problem-anatomy: constraint/edge/corner/test-case/
    invariant; (4) approach: brute/optimal/trade-off/optimal-substructure/overlapping-subproblems/
    greedy-choice; (5) recursion: iterative/recursive/base/recurrence/memoization/tabulation; (6) array-
    memory: in-place/stable/auxiliary/prefix-suffix/subarray-vs-subsequence-vs-subset; (7) structure:
    node/pointer/edge/degree/adjacency/traversal/DFS-vs-BFS/inorder-preorder-postorder.
  - PART 3 — 4-SIGNAL decision engine (constraints→output-type→signal-words→structure) + text
    flowchart = "how expert/AI internally decides the pattern" (his exact ask).
  - PART 4 — "AI se kaise puchho" prompt playbook: 7 copy-paste templates (T1 learn-topic, T2 get-
    decision-logic, T3 cheat-sheet, T4 debug+class-of-mistake, T5 stress-test-thinking, T6 compare-
    approaches, T7 quiz) + 8-point per-topic question checklist + RED FLAGS that his `.md` is shallow.
    This directly serves his "AI se .md banwaake ek-pass me seekhna" method.
  - PART 5 — Infosys focus-filter table (tree branch → importance → which file 03/05/06/09) + 10-day
    order + one-line selection reality (Q1 full + partials = DSE; 2 full = SP).
- Wired in: README (top 01→10, file-order line, Category-D read-first row, reading-order STEP 1.5,
  PROVENANCE INDEX row for 10 + bottom-line list; fixed stale "8 files" → "ye files"). facts.md prep-set
  line updated (added 10; also corrected 06 count 51→64) + date bumped to 2026-07-19.
- Honesty kept: no "guaranteed exact question" claim; file is universal DSA knowledge organized/
  explained + an AI-prompting framework, all labelled AI-EXPLANATION.
- Note (unrelated, same session earlier): user was fighting VS Code/Kiro to open MULTIPLE markdown
  previews as tabs — answer = "Markdown: Toggle Preview Locking" per preview (locked = [Preview] in
  brackets → next preview opens as a new tab instead of reusing); or the "Markdown Multi Tab Preview"
  extension. `workbench.editor.enablePreview` is unrelated.
