<a id="sec-1"></a>
# Stackmentalist — Python Full Stack Developer: Prep Roadmap

<!-- TOC START -->
## Table of Contents

  - [Company snapshot](#sec-2)
  - [Likely hiring process (inferred — startups usually run 3–5 rounds)](#sec-3)
  - [Topic checklists](#sec-4)
    - [Python (core + DSA — foundation of this role)](#sec-5)
    - [SQL & database design (JD emphasizes this)](#sec-6)
    - [Backend — Django + Django REST Framework](#sec-7)
    - [Backend — FastAPI (JD lists "expertise")](#sec-8)
    - [Frontend — React + Next.js](#sec-9)
    - [Systems & practices (JD "good to have"/preferred)](#sec-10)
- [QUESTION BANK WITH ANSWERS](#sec-11)
  - [Python — output / concept (very common)](#sec-12)
  - [SQL — practice (write these)](#sec-13)
  - [Django / DRF — Q&A](#sec-14)
  - [FastAPI — Q&A](#sec-15)
  - [React / Next.js — Q&A](#sec-16)
  - [Async / systems — Q&A](#sec-17)
  - [Machine / practical round — how to approach](#sec-18)
- [RESOURCE LINKS (clickable)](#sec-19)
  - [Python + DSA](#sec-20)
  - [SQL](#sec-21)
  - [Django + DRF](#sec-22)
  - [FastAPI](#sec-23)
  - [React + Next.js](#sec-24)
  - [Full-stack interview question sets](#sec-25)
  - [LLMs / LangChain (differentiator)](#sec-26)
  - [Cloud / Docker / Git](#sec-27)
- [BEHAVIORAL / HR — SCRIPTS (tailored to Shivam)](#sec-28)
  - [Self-introduction (Python full-stack framing)](#sec-29)
  - ["Why Stackmentalist?"](#sec-30)
  - [HR questions → how to answer](#sec-31)
  - [Smart questions to ask](#sec-32)
- [STUDY PLAN](#sec-33)
  - [10-day plan](#sec-34)
  - [Daily routine](#sec-35)
  - [Common mistakes to avoid](#sec-36)
- [PROGRESS TRACKER](#sec-37)
  - [Concepts](#sec-38)
  - [Practice done](#sec-39)
  - [Ready-to-go](#sec-40)
  - [Mistakes log](#sec-41)

<!-- TOC END -->


> Goal: convert this internship/PPO drive (Pune). Role screens on **Python + DSA, SQL & DB design,
> Django + FastAPI (backend), React + Next.js (frontend)**, plus Agile/SDLC, Git/Docker, and
> (good-to-have) LLMs/LangChain. Interview decides intern (paid ₹8–15k) vs trainee (unpaid).
> JD source: `06-job-descriptions/stackmentalist-python-fullstack-2027.md`.

<a id="sec-2"></a>
## Company snapshot
- **Stackmentalist / StackMentalist Ventures** — a services/product tech company (site: stackmentalist.com;
  also listed on Clutch). Positions itself around building "intelligent, scalable solutions".
- **Location:** Pune. Smaller/younger company than a large MNC — expect a leaner, faster process.
- Public interview data is limited (small company), so this plan is built from the **JD's required
  skills + standard Python Full Stack interview patterns** for startups. Adjust as you learn more.

<a id="sec-3"></a>
## Likely hiring process (inferred — startups usually run 3–5 rounds)
1. **Registration / resume shortlist** (done via the Google Form).
2. **Online / coding assessment** — Python + DSA + SQL (MCQ and/or 1–2 coding problems).
3. **Technical interview 1** — Python depth, Django/FastAPI, REST APIs, SQL, your projects.
4. **Technical interview 2 / machine round** — build or extend a small feature (backend API +
   maybe a React screen), debugging, design a simple schema.
5. **HR / managerial** — culture fit, "why Stackmentalist", intern-vs-trainee decision, joining.
> Since interview decides intern vs trainee, aim to over-perform in the technical rounds.

<a id="sec-4"></a>
## Topic checklists

<a id="sec-5"></a>
### Python (core + DSA — foundation of this role)
- Data types, mutability, list/dict/set/tuple, comprehensions, slicing
- Functions, `*args/**kwargs`, closures, decorators, generators/iterators, lambda
- OOP: classes, inheritance, dunder methods, `@staticmethod/@classmethod`, MRO
- Exceptions, context managers (`with`), file I/O
- Modules, virtualenv/pip, `if __name__ == '__main__'`
- Memory model (references, mutable default args trap), GIL basics
- DSA: arrays/strings, hashmaps/sets, two-pointers, sliding window, recursion, sorting,
  stacks/queues, basic trees & graphs, time/space complexity (Big-O)

<a id="sec-6"></a>
### SQL & database design (JD emphasizes this)
- SELECT, WHERE, JOINs (inner/left/right/full), GROUP BY, HAVING, ORDER BY
- Aggregates, subqueries, `EXISTS`/`IN`, `CASE`, window functions (basic)
- Indexes, primary/foreign keys, normalization (1NF–3NF), transactions/ACID
- Schema design: one-to-many, many-to-many (junction tables), constraints
- Query optimization basics; N+1 problem (and how ORMs cause it)

<a id="sec-7"></a>
### Backend — Django + Django REST Framework
- Models, migrations, ORM queries (`filter/annotate/select_related/prefetch_related`)
- DRF: serializers, viewsets, routers, authentication/permissions, pagination
- Request/response cycle, middleware, settings, `.env`/secrets
- Auth: session vs token/JWT; CSRF; CORS

<a id="sec-8"></a>
### Backend — FastAPI (JD lists "expertise")
- Path/query/body params, Pydantic models & validation, response models
- Async endpoints (`async def`), dependency injection, routers
- Auto docs (OpenAPI/Swagger), status codes, error handling
- FastAPI vs Django/DRF: when to use which (lightweight/async APIs vs batteries-included)

<a id="sec-9"></a>
### Frontend — React + Next.js
- Components, props, state, hooks (useState/useEffect/useRef/useMemo/useCallback)
- Lists/keys, controlled forms, lifting state, conditional rendering, fetching data
- Next.js: pages/app router, SSR vs SSG vs CSR, API routes, file-based routing (high level)
- Responsive/UI-UX basics, calling REST APIs from the UI

<a id="sec-10"></a>
### Systems & practices (JD "good to have"/preferred)
- REST principles, microservices basics, API design
- **Async programming, message queues (e.g., Celery/RabbitMQ/Redis), event-driven** (know the "why")
- Git workflow, Docker basics, Postman; Agile/Scrum, SDLC, CI/CD
- Cloud basics (AWS/GCP/Azure — services you've touched)
- LLMs/LangChain (differentiator — you have agentic-AI background): chains, prompts, embeddings,
  RAG at a high level

---

<a id="sec-11"></a>
# QUESTION BANK WITH ANSWERS

<a id="sec-12"></a>
## Python — output / concept (very common)
1. `print(type([]) is list)` → **True**. `print([] == [])` → **True**; `print([] is [])` → **False**.
2. Mutable default arg trap: `def f(x, l=[]): l.append(x); return l` → repeated calls **accumulate**
   (`f(1)`→[1], `f(2)`→[1,2]). Fix: `l=None` then `l = l or []`.
3. `print(1 == True, 2 == True)` → **True False** (bool is int subclass; True==1).
4. `a=[1,2,3]; b=a; b.append(4); print(a)` → **[1,2,3,4]** (same reference).
5. `print(0.1 + 0.2 == 0.3)` → **False** (float precision).
6. List vs tuple: list mutable, tuple immutable (hashable → usable as dict key).
7. `is` vs `==`: `is` = identity (same object); `==` = value equality.
8. Shallow vs deep copy: `copy.copy` vs `copy.deepcopy` (nested objects).
9. Decorator: a function that wraps another to add behavior (logging, timing, auth).
10. Generator: uses `yield`, lazy, memory-efficient; `next()` pulls values.
11. `*args` (tuple of positional), `**kwargs` (dict of keyword) args.
12. GIL: only one thread executes Python bytecode at a time → use multiprocessing/async for concurrency.
13. `@staticmethod` (no self/cls), `@classmethod` (gets cls), instance method (gets self).
14. List comprehension: `[x*x for x in range(5) if x%2==0]` → `[0,4,16]`.
15. `dict.get(k, default)` avoids KeyError; `setdefault`, `defaultdict`, `Counter` are handy.

<a id="sec-13"></a>
## SQL — practice (write these)
- Second highest salary:
  `SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp);`
- Count per group: `SELECT dept, COUNT(*) FROM emp GROUP BY dept HAVING COUNT(*) > 5;`
- Join: `SELECT e.name, d.name FROM emp e JOIN dept d ON e.dept_id = d.id;`
- Duplicates: `SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;`
- **Concepts:** JOIN types, WHERE vs HAVING, GROUP BY, indexes (speed reads/slow writes),
  normalization (remove redundancy), transactions (ACID), primary vs foreign key,
  `DELETE` vs `TRUNCATE` vs `DROP`, N+1 query problem.

<a id="sec-14"></a>
## Django / DRF — Q&A
- **Django request lifecycle:** URL → middleware → view → model/ORM → template/serializer → response.
- **ORM optimize:** `select_related` (FK, SQL join) vs `prefetch_related` (M2M/reverse, extra query).
- **Serializer:** validates + converts model ↔ JSON in DRF.
- **Auth:** session (cookie) vs token/JWT (stateless); DRF permissions/authentication classes.
- **MVT** (Model-View-Template) vs MVC.
- **CSRF/CORS:** CSRF protects form posts; CORS controls cross-origin API access.

<a id="sec-15"></a>
## FastAPI — Q&A
- **What/why:** modern, fast, async Python API framework; auto validation (Pydantic) + auto Swagger docs.
- **Pydantic model:** declares request/response schema; validates types automatically.
- **async def:** enables concurrency for I/O-bound endpoints (DB/HTTP calls).
- **Dependency injection:** `Depends()` for auth, DB sessions, shared logic.
- **FastAPI vs Django:** FastAPI = lightweight async APIs/microservices; Django = full-batteries
  (ORM, admin, auth) monolith. Use FastAPI for high-performance APIs, Django for full apps.

<a id="sec-16"></a>
## React / Next.js — Q&A
- **Hooks:** useState (state), useEffect (side effects/lifecycle), useRef (mutable ref/no re-render),
  useMemo/useCallback (memoize value/fn).
- **Keys:** stable unique ids for list reconciliation (don't use index if list reorders).
- **Controlled vs uncontrolled inputs.**
- **Next.js rendering:** SSR (per request), SSG (build time), CSR (client) — pick per page needs.
- **Why Next.js:** routing, SSR/SEO, API routes, performance out of the box.

<a id="sec-17"></a>
## Async / systems — Q&A
- **Async vs threads vs multiprocessing:** async = single-thread cooperative (I/O-bound);
  threads limited by GIL; multiprocessing for CPU-bound.
- **Message queue (Celery + Redis/RabbitMQ):** offload slow tasks (emails, reports) to background
  workers → responsive APIs; decoupling & retries.
- **Event-driven:** components react to events/messages (pub-sub) → scalable, loosely coupled.
- **REST vs microservices:** REST = API style; microservices = many small independently-deployable services.

<a id="sec-18"></a>
## Machine / practical round — how to approach
1. Clarify requirements & data model. 2. Design the schema/endpoints. 3. Build a minimal working
   API (Django/DRF or FastAPI) + one React screen. 4. Handle validation/errors. 5. Talk through
   tradeoffs. Keep code clean, commit small steps.
- Practice: build a mini CRUD (e.g., Todo/Notes) — FastAPI or DRF backend + React frontend + SQL DB.

---

<a id="sec-19"></a>
# RESOURCE LINKS (clickable)

<a id="sec-20"></a>
## Python + DSA
- Python docs: https://docs.python.org/3/
- Real Python (deep tutorials): https://realpython.com/
- NeetCode (DSA patterns): https://neetcode.io/
- LeetCode Top Interview 150: https://leetcode.com/studyplan/top-interview-150/
- GeeksforGeeks Python: https://www.geeksforgeeks.org/python-programming-language/
- YouTube: **CodeWithHarry (Python)**, **take U forward (DSA)**, **Corey Schafer (Python/Django)**

<a id="sec-21"></a>
## SQL
- SQLBolt (interactive): https://sqlbolt.com/
- Mode SQL tutorial: https://mode.com/sql-tutorial/
- LeetCode SQL 50: https://leetcode.com/studyplan/top-sql-50/
- GfG SQL interview questions: https://www.geeksforgeeks.org/sql-interview-questions/

<a id="sec-22"></a>
## Django + DRF
- Django docs: https://docs.djangoproject.com/
- DRF docs: https://www.django-rest-framework.org/
- YouTube: **Corey Schafer Django**, **Dennis Ivy (Django/DRF)**

<a id="sec-23"></a>
## FastAPI
- FastAPI docs (excellent tutorial): https://fastapi.tiangolo.com/
- FastAPI interview questions: https://goodspace.ai/interview-questions/fastapi

<a id="sec-24"></a>
## React + Next.js
- React docs: https://react.dev/
- Next.js docs/learn: https://nextjs.org/learn
- YouTube: **Codevolution (React/Next)**, **Web Dev Simplified**

<a id="sec-25"></a>
## Full-stack interview question sets
- Python Full Stack Qs (CCBP): https://www.ccbp.in/blog/articles/python-full-stack-developer-interview-questions
- Full Stack Qs (GfG): https://www.geeksforgeeks.org/html/full-stack-developer-interview-questions-and-answers/
- Full-stack interview QA (GitHub): https://github.com/AhmedAbdelbasetAli/full-stack-interview-qa

<a id="sec-26"></a>
## LLMs / LangChain (differentiator)
- LangChain docs: https://python.langchain.com/
- LangGraph docs: https://langchain-ai.github.io/langgraph/

<a id="sec-27"></a>
## Cloud / Docker / Git
- Docker get started: https://docs.docker.com/get-started/
- Git handbook: https://guides.github.com/introduction/git-handbook/

---

<a id="sec-28"></a>
# BEHAVIORAL / HR — SCRIPTS (tailored to Shivam)

<a id="sec-29"></a>
## Self-introduction (Python full-stack framing)
"I'm Shivam Gupta, final-year B.Tech CSE at ITM University (2027). I'm a full-stack developer who
works across Python/Django REST on the backend and React/TypeScript on the frontend. As a Full
Stack Engineer intern at ITM University, I built and modernized the Parakh ERP (React + Django REST)
for admin, examination, and quiz modules. I've shipped live products like NETWORKED (Django REST +
React + custom CMS) and open-source AI tooling (an MCP server, 16+ LLM 'skills'). I also lead the
ITM Developers Club and enjoy building scalable APIs and clean UIs — which is exactly the Python
full-stack work this role involves."

<a id="sec-30"></a>
## "Why Stackmentalist?"
"I want to work in a fast-moving team where I can own features end-to-end across backend and
frontend. Stackmentalist builds intelligent, scalable solutions, and this role spans exactly my
stack — Python/Django/FastAPI + React/Next.js — plus room to use my AI/LangChain background. A
startup pace means faster learning and real ownership early, which suits how I work."

<a id="sec-31"></a>
## HR questions → how to answer
- **Intern vs trainee:** show you're technically strong (you want the paid intern slot) but are
  eager to learn regardless — focus on contribution.
- **Strengths:** ship end-to-end, fast learner, full-stack + AI edge.
- **Weakness:** real + improving (e.g., "timeboxing polish; I ship then iterate").
- **Relocate to Pune?** Yes.
- **Biggest project:** NETWORKED or Parakh — problem, your role, tech, outcome (STAR).
- **Why should we hire you:** proven shipping (live products), full-stack range, AI differentiator.

<a id="sec-32"></a>
## Smart questions to ask
- "What does an intern work on in the first 3 months here?"
- "Which stack/product would I start on — more backend (FastAPI/Django) or frontend (React/Next)?"
- "How is the intern → full-time (PPO) decision made?"
- "How does the team use AI/LLMs in your products?"

---

<a id="sec-33"></a>
# STUDY PLAN

<a id="sec-34"></a>
## 10-day plan
- **D1:** Python core (data model, OOP, decorators, generators) + 10 easy DSA.
- **D2:** DSA (arrays/strings/hashmaps, two-pointer, sliding window) + Big-O.
- **D3:** SQL (joins, group by, subqueries) → SQLBolt + LeetCode SQL 50.
- **D4:** Django + DRF (models, ORM, serializers, auth) — build a small CRUD API.
- **D5:** FastAPI (Pydantic, async, DI) — rebuild the CRUD API in FastAPI.
- **D6:** React + Next.js (hooks, forms, fetch) — build a UI for the CRUD.
- **D7:** Async/message queues/REST/microservices concepts + Docker/Git basics.
- **D8:** Full mini project: FastAPI/DRF + React + SQL (end-to-end CRUD) — this IS the practical round.
- **D9:** Mock: Python + SQL + DSA questions timed; revise LangChain basics.
- **D10:** Behavioral/HR + resume walkthrough + project deep-dive notes.

<a id="sec-35"></a>
## Daily routine
- 1 hr Python/DSA · 1 hr backend (Django/FastAPI) · 45 min SQL · 45 min React/Next · 30 min concepts/HR.

<a id="sec-36"></a>
## Common mistakes to avoid
- Weak SQL (JD stresses DB design) — practice joins/group-by/subqueries.
- Not being able to explain FastAPI vs Django (they'll ask).
- Listing FastAPI/Next.js/LangChain but unable to discuss them — be honest, prep the basics.
- Not knowing YOUR projects deeply (NETWORKED, Parakh) — expect a deep-dive.
- Silent coding in the practical round — narrate.

---

<a id="sec-37"></a>
# PROGRESS TRACKER

<a id="sec-38"></a>
## Concepts
- [ ] Python: OOP, decorators, generators, mutable-default trap, GIL
- [ ] DSA: arrays/strings/hashmaps, two-pointer, sliding window, Big-O
- [ ] SQL: joins, group by/having, subqueries, indexes, normalization
- [ ] Django/DRF: models, ORM (select/prefetch), serializers, auth
- [ ] FastAPI: Pydantic, async, DI, docs; vs Django
- [ ] React/Next: hooks, forms, fetch, SSR/SSG/CSR
- [ ] Async/MQ/REST/microservices; Docker/Git; cloud basics
- [ ] LangChain/LLM basics (differentiator)

<a id="sec-39"></a>
## Practice done
- [ ] 40+ Python questions + 30 DSA problems (NeetCode/LeetCode)
- [ ] LeetCode SQL 50 (or 25+)
- [ ] Built a CRUD API in DRF AND in FastAPI
- [ ] Built a React/Next UI calling that API (end-to-end mini project)
- [ ] 1 timed mock (Python + SQL + DSA)

<a id="sec-40"></a>
## Ready-to-go
- [ ] Self-intro + "Why Stackmentalist" rehearsed
- [ ] STAR stories (NETWORKED, Parakh, IDC, Hacksagon/Odoo)
- [ ] Project deep-dive notes ready
- [ ] Resume PDF final (stackmentalist-python-fullstack-2027) + uploaded

<a id="sec-41"></a>
## Mistakes log
| Date | Topic | Mistake | Fix/Note |
| --- | --- | --- | --- |
| | | | |
