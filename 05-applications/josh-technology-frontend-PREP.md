# JOSH Technology Group — Front End Developer: Prep Roadmap

> Goal: clear an 8–9 round elimination process. Screening is HEAVY on CSS + core JavaScript,
> starts with a negative-marked MCQ, and includes a take-home page + a timed screen-shared
> machine-coding assignment, then technical PIs + HR.
> See company/process details in `06-job-descriptions/josh-technology-DEEP-RESEARCH.md`.

## Strategy per round (what to expect → how to clear)
1. **MCQ (50–70 Qs, 1 hr, negative marking):** ~10 C/C++ + ~40 HTML/CSS/JS; output-prediction,
   syntax, pseudo-code. → Prioritize ACCURACY; skip unsure ones (negative marking). Practice
   output-guessing daily.
2. **JS-focused round:** promises, async/await, closures, `this`, event loop. → Deep JS core.
3. **Take-home static page (~1 week):** pure HTML/CSS/JS, pixel-perfect + responsive. → Ship clean,
   semantic, responsive, no framework.
4. **Timed machine coding (<2 hr, screen-shared, checked every ~20 min):** build a UI component
   fast. → Practice rebuilding components from scratch under time.
5. **Technical PIs:** CSS (grilled), JS, HTML, Computer Networks, dry-run code. → Explain reasoning aloud.
6. **HR/managerial:** culture fit, ownership, communication, "why JTG". → STAR stories ready.

## Topic checklists

### CSS (MOST IMPORTANT — they grill this)
- Box model, margin collapse, `box-sizing`
- Positioning: static/relative/absolute/fixed/sticky; stacking context & z-index
- **Flexbox** (main/cross axis, grow/shrink/basis, alignment) — master fully
- **CSS Grid** (template, areas, auto-fit/fill, minmax)
- Centering (all methods), responsive design, media queries, mobile-first
- Specificity & the cascade, inheritance, units (px/em/rem/%/vh/vw)
- Selectors (child, sibling, attribute, pseudo-classes/elements)
- Transitions, transforms, animations (keyframes); SASS/LESS basics
- display types, overflow, `position: sticky`, common layout bugs

### JavaScript (core — heavily tested)
- Data types, coercion, `==` vs `===`, hoisting, scope, TDZ
- Closures, `this` binding (call/apply/bind), arrow vs regular
- **Promises, async/await, microtask vs macrotask, event loop** (very common)
- Callbacks, `setTimeout`/`setInterval`, debounce & throttle
- Array/object methods (map/filter/reduce/find/spread/destructuring)
- Prototypes & inheritance, ES6+ features, modules
- DOM manipulation, event delegation, bubbling/capturing
- Output-prediction snippets (for MCQ)

### HTML
- Semantic tags, forms & validation, accessibility (a11y) basics
- meta/SEO tags, `data-*`, media, tables

### React (they use React JS & Native)
- Components, props, state, hooks (useState/useEffect/useRef/useMemo/useCallback)
- Lists & keys, controlled inputs, lifting state, conditional rendering
- Basic performance (memo), component design; (context/router basics)

### CS fundamentals (light)
- Computer Networks: HTTP/HTTPS, status codes, DNS, TCP vs UDP, request/response, CORS basics
- C/C++: output/pointer MCQs, operators, loops, OOP basics (for the MCQ round)

## Machine-coding practice (build from scratch, timed, vanilla JS + a few React)
- Accordion, Tabs, Modal/Dialog, Carousel/Slider
- Star rating, Toast notifications, Todo list (add/edit/delete/filter)
- Autocomplete/typeahead (with debounce), Pagination, Infinite scroll
- Accordion tree, Tic-tac-toe, Stopwatch/Timer, OTP input
- Responsive navbar (hamburger), Image gallery/lightbox
> Do each in < 40 min, clean code, then redo in React.

## Day-wise plan

### 2-week plan (if you have ~14 days)
- **D1–2:** CSS deep dive (flexbox, grid, positioning, specificity) + 3 layout clones.
- **D3–4:** JS core (closures, this, promises, async, event loop) + 30 output MCQs/day.
- **D5:** HTML semantics/forms/a11y + responsive page (take-home style practice).
- **D6–7:** Machine coding — 2 components/day (vanilla), timed.
- **D8:** React fundamentals + rebuild 2 components in React.
- **D9:** Computer Networks + C/C++ output MCQs (for MCQ round).
- **D10:** Full mock MCQ (timed, negative marking) + review mistakes.
- **D11–12:** More machine coding (harder: autocomplete, carousel) + one polished take-home page.
- **D13:** Behavioral/HR prep (STAR stories, why JTG) + resume walkthrough.
- **D14:** Light revision + mock technical interview (explain out loud) + rest.

### Crash 3–4 day plan (if assessment is very soon)
- **Day 1:** CSS flexbox/grid/specificity + centering; JS promises/async/closures.
- **Day 2:** 60 output-prediction MCQs (JS + a few C/C++); 2 machine-coding components.
- **Day 3:** Responsive page build + React basics; Computer Networks quick pass.
- **Day 4:** Mock MCQ (negative-marking discipline) + 2 timed components + HR answers.

## Assessment-day tips
- Labs with **webcam + mic ON** — dress/setup accordingly, stable environment.
- MCQ: read carefully, **skip risky ones** (negative marking); manage the 1-hour clock.
- Machine coding: talk through your plan first, commit small working steps, handle edge cases.
- Interviews: think aloud, ask clarifying questions, dry-run with sample inputs.

## Behavioral / HR (STAR stories to prepare)
- **Leadership:** President, ITM Developers Club — leading team, organizing events.
- **Impact/build:** NETWORKED (client platform, end-to-end delivery, CI/CD).
- **Competition:** Hacksagon 2025 Top Performer; Odoo Hackathon 8th (solo).
- **Ownership/learning:** modernizing the university ERP (React + Django).
- **"Why JTG?":** product-builder/CTO-office model, direct mentorship from founders, flat
  hierarchy, latest tech across domains, own products like Pod.AI.

## Resources
- MDN (CSS/JS reference), javascript.info (JS deep), Flexbox Froggy / Grid Garden (CSS games),
  GreatFrontEnd / Frontend practice for machine coding, GeeksforGeeks "Josh Technology"
  interview experiences for pattern.


---

# ROUND-BY-ROUND (very detailed, with resources)

> Consolidated from multiple GeeksforGeeks JTG Front End Developer experiences (2024–2025).
> Format varies slightly by year: typically **9 rounds = ~4 online (home/college) + ~5 at the
> Gurugram office**, every round is an ELIMINATION round. Content rephrased for compliance.

## Round 1 — Online MCQ (elimination, ~1 hour, NEGATIVE marking)
- **What:** ~50 MCQs (some years ~70). Split roughly **~10 C/C++** + **~40 HTML/CSS/JS**.
  Question types: output-prediction, language syntax, pseudo-code, single-line integer output.
- **How to clear:** Accuracy over attempts (negative marking). Solve fast on sure ones, skip risky.
  JS output snippets (hoisting, closures, `this`, coercion) show up a lot.
- **Study:** JS/HTML/CSS output-prediction; C/C++ output & pointer basics; operators/loops.
- **Resources:**
  - javascript.info (Fundamentals + "Advanced working with functions")
  - MDN CSS + JS reference
  - GeeksforGeeks: "Josh Technology Interview" MCQ articles; JS output-prediction question sets
  - InterviewBit / GfG C output-question quizzes (for the C/C++ part)

## Round 2 — Online MCQ / Aptitude (elimination)
- **What:** Second objective round in some years — more HTML/CSS/JS, sometimes light aptitude
  and logical reasoning. Still negative marking in most reports.
- **Study:** Deeper CSS (specificity, box model, flex/grid), core JS; quick aptitude (ratios,
  percentages, series) if included.
- **Resources:** IndiaBix/GfG aptitude (quick), css-tricks "Complete Guide to Flexbox/Grid".

## Round 3 — Online Technical / Subjective (elimination)
- **What:** Conceptual HTML/CSS/JS — "easy but fundamental" per experiences. May ask to write
  short code/explain output. In SDE variants you write full programs WITH comments (comments help scoring).
- **Study:** Explain concepts crisply (event loop, promises, box model, positioning, specificity).
- **Resources:** javascript.info (Promises/async), "What the heck is the event loop" (Philip Roberts talk).

## Round 4 — Take-home Technical Assessment (build a static page, ~1 week)
- **What:** Build a **static web page using ONLY HTML, CSS, JavaScript** (no framework).
  Judged on pixel-perfection, responsiveness, clean/semantic code, and JS interactivity.
- **How to shine:** Mobile-first responsive, semantic HTML, organized CSS (BEM/variables),
  small clean JS, cross-browser, no console errors. Add subtle polish (transitions, a11y).
- **Resources:**
  - Frontend Mentor challenges (frontendmentor.io) — practice pixel-perfect responsive pages
  - Reference (public): a real JTG assignment sample repo exists on GitHub
    (search "JOSH-TECHNOLOGY-GROUP-Assignment") — study structure, don't copy
  - MDN "Responsive design", css-tricks media queries

## Round 5 — On-site Machine Coding (timed <2 hr, SCREEN-SHARED, checked every ~20 min)
- **What:** Build a working UI component/feature live while the interviewer watches and asks for
  updates every ~20 minutes. Tests speed + clean code + edge cases.
- **How to shine:** State the plan first → break into requirements/state/interactions → build in
  small working increments → handle edge cases → keep code readable. Talk while you build.
- **Practice components:** Accordion, Tabs, Modal, Carousel, Star-rating, Todo (CRUD+filter),
  Autocomplete (debounced), Pagination, Infinite scroll, Responsive navbar, OTP input, Stopwatch.
- **Resources:**
  - GreatFrontEnd — "Machine Coding Round" guide + practice questions
  - FrontendGeek — "20+ Frontend Machine Coding Round Questions"
  - Medium: "React JS Machine Coding: 25+ Must-Do Questions with Solutions" (sanchit0496)
  - GitHub: "frontend-interview-preparation-kit" (ghoshsuman845)

## Round 6 — Technical Personal Interview 1 (CSS-heavy)
- **What:** Introduction → deep questions on **CSS (they grill this hardest)**, JavaScript, HTML,
  and **Computer Networks** basics. Expect follow-ups and dry-running code.
- **Study:** CSS (flex/grid/positioning/specificity/centering, why layouts break), JS core,
  CN (HTTP/HTTPS, status codes, DNS, TCP vs UDP, CORS, how a URL loads a page).
- **Resources:** css-tricks, javascript.info, GfG Computer Networks basics.

## Round 7 — Technical Personal Interview 2 (deeper)
- **What:** Deeper problem-solving — more machine coding / DOM tasks, project deep-dive
  (they'll probe NETWORKED, Parakh, etc.), and reasoning. Sometimes light DSA/logic.
- **Study:** Be able to explain YOUR projects' architecture, tradeoffs, what you'd improve.
  Revisit basic DSA (arrays, strings, hashmaps) and DOM manipulation.
- **Resources:** Your own repos (know them cold), GfG DSA basics.

## Round 8 — HR / Managerial (culture fit, final)
- **What:** Communication, ownership, teamwork, "Why JTG?", strengths/weaknesses, relocation to
  Gurugram, bond acknowledgement, salary/joining.
- **How to shine:** STAR stories; genuine "why JTG" (product-builder/CTO-office model, founder
  mentorship, flat hierarchy, Pod.AI, latest tech). Be honest and confident.
- **Resources:** Prepare 5–6 STAR stories (see below) + 6–8 common HR questions.

## Notes that repeat across experiences
- Every round is an **elimination** round — no coasting.
- **CSS is the single most-tested area** for FED; JavaScript async/promises close second.
- Online tests are from **campus labs with webcam + mic ON**.
- Writing **comments** in subjective/coding rounds improves scoring.
- Communication is genuinely evaluated (JTG values blogs/presentations/teamwork).

## STAR stories to lock (reuse across PI + HR)
1. Leadership — President, ITM Developers Club (led team, ran events/talks).
2. End-to-end build — NETWORKED client platform (concept → production, CI/CD).
3. Competition — Hacksagon 2025 Top Performer; Odoo Hackathon 8th (solo).
4. Ownership/learning — modernizing university ERP (React + Django, real users).
5. Problem-solving — a tough bug/optimization you fixed (pick a concrete one).

## Consolidated resource list
- **CSS:** css-tricks (Flexbox & Grid complete guides), Flexbox Froggy, Grid Garden, MDN CSS.
- **JavaScript:** javascript.info, MDN JS, "What the heck is the event loop?" (Philip Roberts).
- **Machine coding:** GreatFrontEnd, FrontendGeek, Medium (25 React machine coding), BFE.dev.
- **Take-home:** Frontend Mentor.
- **CN:** GeeksforGeeks Computer Networks (HTTP, DNS, TCP/UDP, CORS).
- **Patterns:** GeeksforGeeks "Josh Technology" interview experiences (read 4–5 to see the pattern).


---

# COMPLETE RESOURCE HUB (question banks, PYQs, YouTube, courses) — GOAL: get selected

> Everything mapped to JTG's screening (CSS + core JS heavy, MCQ negative marking, take-home
> page, timed machine coding, technical PIs + HR). Prioritize the ⭐ items.

## A. YouTube channels (by purpose)

### Core JavaScript (for MCQ + JS + PI rounds)
- ⭐ **Akshay Saini — "Namaste JavaScript"**: closures, hoisting, event loop, callbacks,
  promises, async/await. THE series for JS internals (exactly what JTG's output MCQs test).
- ⭐ **RoadsideCoder (Piyush Agarwal)**: JS interview questions + output-based + polyfills
  (map/filter/reduce, debounce, throttle, promise.all) — perfect for JTG.
- **Chai aur Code (Hitesh Choudhary)**: JS + React, practical.
- **Web Dev Simplified (Kyle Cook)**: crisp JS/CSS/React concept videos.
- **Fireship**: quick "100 seconds" refreshers before the test.

### CSS (their MOST-tested area — do NOT skip)
- ⭐ **Kevin Powell**: best CSS channel — flexbox, grid, positioning, responsive, centering.
- **Web Dev Simplified**: CSS crash + flexbox/grid.
- Practice games: **Flexbox Froggy**, **Grid Garden**, **CSS Diner** (selectors), **CSS Battle**.

### Machine coding (timed component building — the on-site round)
- ⭐ **RoadsideCoder — "Frontend Machine Coding" / "React Interview Questions" playlists**:
  builds accordion, tabs, autocomplete, star rating, pagination, OTP, etc. with explanations.
- **GreatFrontEnd (YouTube + site)**: machine coding approach & solutions.
- **Codevolution**: deep React (hooks, patterns) for React-based machine coding.

### React (they use React JS & Native)
- ⭐ **Codevolution — React + React Hooks** playlists.
- **Chai aur Code / Web Dev Simplified**: React fundamentals & hooks.

### DSA / C++ basics (for the C/C++ MCQs + PI logic)
- **take U forward (Striver)**: DSA sheet + videos.
- **CodeHelp — Love Babbar**: C++/DSA.
- **Gate Smashers**: Computer Networks + OS (for CN questions in PI).

### Long free courses
- **freeCodeCamp**, **Traversy Media** (Modern JS, project builds), **Apna College** (web dev).

## B. Written resources / docs (deep + reference)
- ⭐ **javascript.info** — free book; do Fundamentals + "Advanced functions" + "Promises/async".
- ⭐ **MDN Web Docs** — CSS & JS reference (authoritative).
- **CSS-Tricks** — "A Complete Guide to Flexbox" & "…to Grid" (bookmark both).
- **"You Don't Know JS" (Kyle Simpson)** — free on GitHub; deep JS (scope/closures, this).
- **web.dev (Google)** — Learn CSS, Learn Responsive Design.

## C. Question banks & practice platforms
- ⭐ **BFE.dev (BigFrontEnd)** — JS quiz (output-based) + coding + system design. Gold for MCQ practice.
- ⭐ **GreatFrontEnd** — front-end interview platform: quizzes, machine coding, JS utils, system design.
- **JSchallenger** — JS exercises by difficulty.
- **Frontend Mentor** — real responsive page challenges (for the take-home round).
- **LeetCode** — "Top Interview 150" + JavaScript problems (for logic/DSA-lite in PIs).
- **InterviewBit** — front-end + C output questions.
- **30 seconds of code** — snippet patterns (debounce, deep clone, etc.).
- **CodePen** — build/host your take-home & practice components.

## D. JTG-specific PYQ / patterns (READ THESE FIRST)
- ⭐ **GeeksforGeeks → search "Josh Technology"**: read 5–6 Front End Developer interview
  experiences (2024–2025) to internalize the exact MCQ style, round order, and assignment type.
- **GeeksforGeeks "Josh Technology Interview MCQ Online Questions"** — sample MCQ patterns.
- **GitHub → "JOSH-TECHNOLOGY-GROUP-Assignment"** — a real submitted FE assignment (study the
  structure/quality expected; build your own, don't copy).
- **AmbitionBox / Glassdoor → Josh Technology "Interviews"** tab — more Q reports.

## E. Must-master JavaScript output/concept topics (MCQ + PI)
- Hoisting (var/let/const, TDZ), scope chain, closures
- `this` binding (implicit/explicit/new/arrow), call/apply/bind
- Event loop: call stack, microtask (promises) vs macrotask (setTimeout) ordering
- Promises: chaining, `Promise.all/race/allSettled`, error handling; async/await
- Coercion & `==` vs `===`, truthy/falsy, `typeof`, `NaN`
- Array/object methods, spread/rest, destructuring, optional chaining
- Prototypes & inheritance; `map` vs `forEach`; pass-by-value vs reference
- Polyfills to be able to write: `map`, `filter`, `reduce`, `bind`, debounce, throttle, `Promise.all`
- Practice output sets: dev.to "tricky promise output", Medium "JavaScript output-based questions",
  BFE.dev quiz.

## F. Must-master CSS topics (their hardest area)
- Box model + `box-sizing`, margin collapse
- Flexbox (grow/shrink/basis, align/justify) & Grid (template, areas, auto-fit/fill, minmax)
- Positioning (relative/absolute/fixed/sticky), stacking context, z-index
- Specificity & cascade, inheritance, units (px/em/rem/%/vh/vw/ch)
- Centering (5+ ways), responsive (mobile-first, media queries, clamp())
- Selectors (combinators, attribute, pseudo-class/element), transitions/transforms/animation
- Common interview asks: "center a div", "difference between flex & grid", "how does z-index work",
  "position sticky vs fixed", "specificity calc".

## G. Machine-coding component checklist (build each < 40 min, vanilla + React)
Accordion · Tabs · Modal · Carousel/Slider · Star rating · Todo (CRUD + filter) ·
Autocomplete/typeahead (debounced) · Pagination · Infinite scroll · Responsive navbar (hamburger) ·
OTP input · Stopwatch/Timer · Toast notifications · Nested comments · Image gallery/lightbox ·
Progress bar · Tic-tac-toe · Traffic light · Data table (sort/filter).
> Source playlists: RoadsideCoder, GreatFrontEnd, FrontendGeek "20+ machine coding".

## H. Computer Networks (for PI) — quick list
HTTP/HTTPS, methods, status codes (2xx/3xx/4xx/5xx), request/response headers, cookies vs
localStorage vs sessionStorage, DNS resolution, TCP vs UDP, what happens when you type a URL,
CORS, HTTP caching, HTTP/1.1 vs 2. → Gate Smashers CN + GfG CN.

## I. 7-day resource-mapped sprint (if time is short)
- **D1 CSS:** Kevin Powell flexbox+grid → Flexbox Froggy + Grid Garden → build 2 responsive layouts.
- **D2 JS core:** Namaste JS (closures, hoisting, event loop) → 20 BFE.dev output quizzes.
- **D3 JS async:** Namaste JS promises/async → write polyfills (Promise.all, debounce, throttle).
- **D4 Machine coding:** RoadsideCoder → build Accordion, Tabs, Star-rating (vanilla).
- **D5 Machine coding + React:** Autocomplete (debounce), Todo, Pagination in React.
- **D6 Take-home:** Frontend Mentor challenge — one polished responsive page.
- **D7 Mock + CN + HR:** timed BFE MCQ mock, CN quick pass, STAR stories + "why JTG".

## J. Daily routine (until the drive)
- 1 hr JS (concept + 15 output questions)
- 1 hr CSS (concept + one layout)
- 1 hr machine coding (1 component, timed)
- 30 min DSA-lite / CN / MCQ mock
- 15 min revise notes + track mistakes in a "mistakes log"

## K. Golden rules to actually get selected
- Master **CSS + JS async** cold — that's where JTG cuts people.
- Do **mock MCQs with negative marking** so you learn to skip smartly.
- Build components **without googling** and **while talking** (mimic screen-share).
- Know **your own projects** deeply (NETWORKED, Parakh) — they WILL probe them.
- Keep a **mistakes log**; revisit it every 2 days.
- Sleep before the online test; stable webcam/mic setup.


---

# DIRECT RESOURCE LINKS (clickable)

> JTG PYQ = GeeksforGeeks interview experiences (read these FIRST — they reveal the exact MCQ
> style, rounds, and assignment). Treat external content as reference.

## 1. JTG PYQ / Interview Experiences (READ FIRST)
- FED 2024 on-campus (9 rounds; R1 = 50 MCQ: 10 C/C++ + 40 HTML/CSS/JS):
  https://www.geeksforgeeks.org/interview-experiences/josh-technology-group-interview-experience-for-frontend-developer-2024-on-campus-opportunity/
- FED 2025 (9-round breakdown):
  https://www.geeksforgeeks.org/josh-technology-group-interview-experience-frond-end-developer-2025/
- FED (70 MCQ, negative marking, output/syntax):
  https://www.geeksforgeeks.org/josh-technology-group-interview-experience-for-front-end-developer/
- FED / SDE-intern campus drive (closures, promises, event loop + dry runs):
  https://www.geeksforgeeks.org/interview-experiences/josh-technology-group-frontend-developer-sde-intern-interview-experience-campus-drive/
- FED on-campus (JS output snippets, build HTML/CSS from a webpage, JS form validation):
  https://www.geeksforgeeks.org/interview-experiences/josh-technology-interview-experience-for-frontend-developer-on-campus/
- FDE at JTG (HTML/CSS/JS, strong JS promises/async emphasis):
  https://www.geeksforgeeks.org/interview-experiences/frontend-developer-interview-experience-at-jtg/
- Josh "MCQ Online Questions" (sample MCQ patterns):
  https://www.geeksforgeeks.org/interview-experiences/josh-technology-interview-experience-mcq-online-questions/
- SDE off-campus (50 MCQ on C, output-based):
  https://www.geeksforgeeks.org/interview-experiences/josh-technology-interview-experience-for-sde-off-campus/
- SDE role batch 2025 (8 elimination levels):
  https://www.geeksforgeeks.org/josh-technology-group-interview-experience-sde-role-batch-2025/
- Pool drive (logic → code on paper → dry run):
  https://www.geeksforgeeks.org/josh-interview-experience-pool-drive/
- More anytime → Google: `Josh Technology interview experience site:geeksforgeeks.org`
- Also check the "Interviews" tab on AmbitionBox & Glassdoor for Josh Technology Group.

## 2. Real assignment references (take-home round)
- Sample submitted FE assignment repo (study structure/quality — build your own, don't copy):
  https://github.com/yadavg123/JOSH-TECHNOLOGY-GROUP-Assignment
- Frontend interview prep kit (curated):
  https://github.com/ghoshsuman845/frontend-interview-preparation-kit

## 3. MCQ / output-question practice (Round 1)
- JavaScript Output-Based Interview Questions (GfG):
  https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/
- JavaScript Quiz Set-1 (GfG, many sets linked):
  https://www.geeksforgeeks.org/javascript/javascript-quiz-set-1/
- HTML Interview Questions (GfG):
  https://www.geeksforgeeks.org/html/html-interview-questions/
- BigFrontEnd (BFE.dev) — JS output quiz + coding (BEST for MCQ practice):
  https://bigfrontend.dev/
- Tricky Promise output questions (dev.to):
  https://dev.to/hitheshkumar/master-javascript-promises-10-tricky-output-questions-every-developer-must-know-part-1-1l43

## 4. Machine-coding practice (on-site timed round)
- GreatFrontEnd (machine coding + JS utils + quizzes): https://www.greatfrontend.com/
- GreatFrontEnd — Machine Coding Round guide: https://www.greatfrontend.com/blog/machine-coding-round
- FrontendGeek — 20+ Machine Coding questions:
  https://www.frontendgeek.com/blogs/20-frontend-machine-coding-round-interview-questions
- React 25+ Machine Coding (Medium, sanchit0496):
  https://medium.com/@sanchit0496/react-js-machine-coding-25-must-do-questions-with-solutions-344f47dee15d
- BFE.dev coding challenges: https://bigfrontend.dev/coding

## 5. Take-home page practice (pixel-perfect responsive)
- Frontend Mentor (real responsive challenges): https://www.frontendmentor.io/
- JSchallenger (JS exercises): https://www.jschallenger.com/

## 6. CSS practice (their MOST-tested area)
- Flexbox Froggy: https://flexboxfroggy.com/
- Grid Garden: https://cssgridgarden.com/
- CSS Diner (selectors): https://flukeout.github.io/
- CSS Battle: https://cssbattle.dev/
- CSS-Tricks — Complete Guide to Flexbox: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- CSS-Tricks — Complete Guide to Grid: https://css-tricks.com/snippets/css/complete-guide-grid/
- web.dev — Learn CSS: https://web.dev/learn/css/

## 7. Core docs / free books
- javascript.info (free JS book): https://javascript.info/
- MDN Web Docs: https://developer.mozilla.org/
- You Don't Know JS (free, GitHub): https://github.com/getify/You-Dont-Know-JS

## 8. YouTube channels (direct)
- Namaste JavaScript — Akshay Saini (JS internals): https://www.youtube.com/@AkshaySaini
- RoadsideCoder (frontend interview + machine coding): https://www.youtube.com/@RoadsideCoder
- Kevin Powell (CSS master): https://www.youtube.com/@KevinPowell
- Web Dev Simplified: https://www.youtube.com/@WebDevSimplified
- Codevolution (React deep): https://www.youtube.com/@Codevolution
- Chai aur Code (Hitesh Choudhary): https://www.youtube.com/@chaiaurcode
- Fireship (quick concepts): https://www.youtube.com/@Fireship
- Gate Smashers (Computer Networks/OS): https://www.youtube.com/@GateSmashers
- take U forward — Striver (DSA): https://www.youtube.com/@takeUforward
> If a handle doesn't open, search the channel name on YouTube.

## 9. DSA-lite / logic (for PIs & C MCQs)
- LeetCode — Top Interview 150: https://leetcode.com/studyplan/top-interview-150/
- GeeksforGeeks DSA: https://www.geeksforgeeks.org/dsa/
- Computer Networks (GfG): https://www.geeksforgeeks.org/computer-network-tutorials/

## How to use (fast path)
1. Read 4–5 JTG PYQ links (Section 1) → note exact MCQ style + round order.
2. Grind BFE.dev + GfG output questions (Section 3) with a timer + negative-marking mindset.
3. Kevin Powell + Flexbox Froggy/Grid Garden (Section 6) → build 2 responsive pages (Frontend Mentor).
4. RoadsideCoder + GreatFrontEnd (Section 4) → build 8–10 components under time.
5. Namaste JavaScript (Section 8) for closures/event loop/promises → re-do output quizzes.


---

# QUESTION BANK WITH ANSWERS (practice like the real rounds)

> Cover these cold. Answers are concise; type them out / run them to internalize.

## JavaScript — output prediction (Round 1 style, learn the trap)
1. `console.log(1 + "2" + 3)` → **"123"** ; `console.log(1 + 2 + "3")` → **"33"** (left-to-right; string concat).
2. `console.log(a); var a = 5;` → **undefined** (var hoisted, not init).
3. `console.log(b); let b = 5;` → **ReferenceError** (TDZ for let/const).
4. `for(var i=0;i<3;i++) setTimeout(()=>console.log(i),0)` → **3 3 3** ; with `let` → **0 1 2**.
5. Event loop: `console.log('A'); setTimeout(()=>console.log('B')); Promise.resolve().then(()=>console.log('C')); console.log('D')` → **A D C B** (sync → microtask → macrotask).
6. `typeof null` → **"object"** ; `typeof NaN` → **"number"** ; `NaN === NaN` → **false**.
7. `[] == ![]` → **true** ; `null == undefined` → **true** ; `null === undefined` → **false**.
8. `async function f(){console.log(1); await null; console.log(2)} console.log(0); f(); console.log(3)` → **0 1 3 2**.
9. `let i=1; console.log(i++ + ++i)` → **4** (1 + 3).
10. `console.log("5"-2, "5"+2)` → **3 "52"**.
11. `let x={a:1}; let y=x; y.a=2; console.log(x.a)` → **2** (objects by reference).
12. `[1,2,3].map(x=>x*2).filter(x=>x>2)` → **[4,6]**.
13. `const o={x:1,get(){return ()=>this.x}}; o.get()()` → **1** (arrow keeps lexical `this`).
14. `Promise.resolve(1).then(x=>{console.log(x);return 2}).then(console.log)` → **1** then **2**.
15. `console.log(0.1 + 0.2 === 0.3)` → **false** (floating point).

## JavaScript — concept Q&A
- **Closure:** function + its lexical scope; inner fn remembers outer variables even after outer returns.
- **Hoisting:** declarations moved to top of scope; `var`=undefined, `let/const`=TDZ, functions fully hoisted.
- **`this`:** implicit (obj.method), explicit (call/apply/bind), `new`, arrow = lexical (no own `this`).
- **Event loop:** call stack → microtasks (Promises) drain fully → one macrotask (setTimeout) → repeat.
- **Debounce vs Throttle:** debounce = run after quiet gap; throttle = run at most once per interval.
- **`==` vs `===`:** `==` allows coercion, `===` strict (type + value). Prefer `===`.
- **null vs undefined:** undefined = not assigned; null = intentional empty.
- **map vs forEach:** map returns new array; forEach returns undefined (side-effects).
- **Event delegation:** attach one listener on parent, use `event.target` (bubbling) — fewer listeners.
- **Promise vs callback:** promises avoid callback hell, chainable, better error handling.

## CSS — concept Q&A (their hardest area)
- **Center a div:** `display:flex; justify-content:center; align-items:center;` (or grid `place-items:center`).
- **Flex vs Grid:** flex = 1D (row OR column); grid = 2D (rows AND columns).
- **Specificity:** inline(1000) > id(100) > class/attr/pseudo-class(10) > element/pseudo-element(1); `!important` overrides.
- **box-sizing:** `border-box` includes padding+border in width (predictable sizing).
- **position sticky vs fixed:** sticky = relative until scroll threshold then sticks (within parent); fixed = always relative to viewport.
- **z-index/stacking context:** works only on positioned elements; new context created by position+z-index, opacity<1, transform, etc.
- **em vs rem:** em = relative to parent font-size; rem = relative to root (html) font-size.
- **Responsive:** mobile-first, media queries, relative units, `clamp()`, flexible images.
- **Margin collapse:** vertical margins of adjacent blocks collapse to the larger one.

## C / C++ — output MCQ samples (for the ~10 C/C++ MCQs)
- `int a=10,b=3; printf("%d", a%b);` → **1**
- `int arr[]={1,2,3}; printf("%d", *(arr+1));` → **2**
- `char c='A'; printf("%d", c);` → **65** (ASCII)
- `int x=5; printf("%d", x>3?x:0);` → **5**
- `int i=1; printf("%d", i<<2);` → **4** (bit shift)
> Revise: operators, precedence, loops, arrays/pointers basics, ternary, bitwise, `sizeof`.

## Machine-coding — how to approach (say this out loud)
1. **Clarify** requirements & edge cases (30–60s).
2. **Plan** structure: HTML skeleton → state → events → render.
3. **Build incrementally** — get a minimal working version first, then features.
4. **Handle edge cases** (empty, loading, invalid input) & clean up listeners.
5. **Talk while coding**; keep functions small & named.

### Mini template — Counter/Accordion pattern (vanilla)
```js
// state -> render -> events
let state = { open: null };
function render() { /* update DOM from state */ }
container.addEventListener('click', (e) => {
  const item = e.target.closest('[data-idx]'); // event delegation
  if (!item) return;
  const idx = Number(item.dataset.idx);
  state.open = state.open === idx ? null : idx;
  render();
});
render();
```

## Take-home assignment — quality rubric (score yourself)
- [ ] Pixel-perfect vs the given design; responsive (mobile→desktop)
- [ ] Semantic HTML; accessible (labels, alt, keyboard)
- [ ] Clean, organized CSS (variables/BEM); no inline styles hacks
- [ ] Working JS interactivity; no console errors
- [ ] Cross-browser; fast (optimized images, minimal reflows)
- [ ] README with setup + a short note on approach


---

# BEHAVIORAL / HR — SCRIPTS (tailored to Shivam)

## Self-introduction (60–90 sec, memorize the flow, not word-for-word)
"I'm Shivam Gupta, a final-year B.Tech CSE student at ITM University, Gwalior (2027 batch).
I'm a front-end-focused full-stack developer — my strongest stack is React with JavaScript/TypeScript
on the front end and Django REST on the back end. Over the last year I've been a Full Stack Engineer
intern at ITM University, where I helped modernize the university ERP (Parakh Portal) — building
reusable, responsive React components for admin, examination, and quiz modules. Alongside, I ship
real products: NETWORKED, a live client platform, and open-source work like a Figma-to-code MCP tool.
I also lead as President of the ITM Developers Club and was a Top Performer at the IEEE Hacksagon
hackathon. I love building clean, performant UIs, and JTG's product-builder culture is exactly where
I want to grow."

## "Why JTG?" (be specific — they'll notice)
"Three reasons: First, the product-builder / CTO-office model means I'd own products end-to-end and
see real business impact early. Second, the flat hierarchy and direct mentorship from senior directors
and founders is rare — I learn fastest with strong mentors. Third, JTG works across many domains
(healthcare, fintech, edutech) and the latest tech (React, Node, Go, cloud), plus your own product
Pod.AI — that breadth matches how I like to learn and build."

## Common HR questions → how Shivam should answer (STAR / honest)
- **Strengths:** fast learner, ownership, ship real products, comfortable across FE+BE.
- **Weakness:** pick a real, improving one (e.g., "I used to over-polish; now I timebox and ship, then iterate").
- **Biggest project:** NETWORKED — problem, your role end-to-end, tech, outcome; or Parakh ERP (real users).
- **Handling failure/tight deadline:** a hackathon or client deadline story (STAR).
- **Teamwork/conflict:** IDC — leading a team, resolving a disagreement, delivering an event.
- **Relocation to Gurugram?** Yes (you're open to it — already targeting Gurugram/Pune).
- **Bond (₹1L)?** Acknowledge you understand the 12-month internship + bond terms.
- **Where in 5 years?** Senior full-stack/front-end engineer owning products; strong system-design depth.
- **Why should we hire you?** Proven shipping (live products), leadership, strong FE fundamentals, fast learner.

## Smart questions to ASK the interviewer (shows interest)
- "What does the first 3–6 months look like for a front-end intern here?"
- "Which product/domain would I most likely start on?"
- "How does JTG approach front-end code quality and testing?"
- "What growth/mentorship looks like given the flat hierarchy?"
- "What separates interns who convert to strong full-time engineers here?"

---

# LOGISTICS & MINDSET

## Day-before checklist
- [ ] Test webcam + mic + internet (online rounds need both ON)
- [ ] Quiet, well-lit room; ID ready; charger/backup connection
- [ ] Revise: JS output notes, CSS specificity/flex/grid, event loop, your projects
- [ ] Skim 2–3 JTG PYQ links again; sleep well

## During the MCQ (negative marking) — strategy
- Two passes: Pass 1 = answer only the sure ones; Pass 2 = attempt likely ones; SKIP pure guesses.
- Track time (≈1 min/Q for 50 in 60 min). Don't get stuck.

## During machine coding / assignment
- Restate the task; agree on scope; build minimal working first; talk through decisions;
  handle edge cases; keep it clean; leave 5 min to test.

## Common mistakes to avoid
- Guessing in negative-marked MCQ.
- Weak CSS (their #1 filter) — don't wing flexbox/positioning/specificity.
- Silent coding in machine round — narrate your thinking.
- Not knowing YOUR OWN projects deeply (they will probe NETWORKED/Parakh).
- Over-engineering the take-home; instead ship clean + responsive + working.

---

# PROGRESS TRACKER (tick as you go)

## Concepts
- [ ] CSS: flexbox, grid, positioning, specificity, centering, responsive
- [ ] JS: closures, hoisting/TDZ, `this`, event loop, promises/async
- [ ] JS: polyfills (map/filter/reduce, bind, debounce, throttle, Promise.all)
- [ ] React: hooks, state, lists/keys, controlled inputs
- [ ] CN: HTTP, status codes, DNS, TCP/UDP, CORS
- [ ] C/C++: output/pointer/operator MCQs

## Practice done
- [ ] 100+ JS output MCQs (BFE.dev + GfG)
- [ ] 2 responsive pages (Frontend Mentor)
- [ ] 10 machine-coding components (vanilla) + 5 in React
- [ ] 1 timed mock MCQ (negative marking)
- [ ] 1 mock technical interview (spoken aloud)

## Ready-to-go
- [ ] Self-intro rehearsed
- [ ] "Why JTG" rehearsed
- [ ] 5 STAR stories written
- [ ] Projects deep-dive notes (NETWORKED, Parakh) ready
- [ ] Resume PDF final + uploaded

## Mistakes log (fill as you practice)
| Date | Topic | Mistake | Fix/Note |
| --- | --- | --- | --- |
| | | | |
