<a id="sec-1"></a>
# Infosys — Specialist Programmer / DSE: Prep Roadmap

<!-- TOC START -->
## Table of Contents

  - [Company snapshot — Infosys Ltd](#sec-2)
  - [Hiring process (deep research — GeeksforGeeks/Medium/Great Learning)](#sec-3)
  - [Test strategy (180 min, 3 questions)](#sec-4)
  - [DSA topic-wise plan (the core — master these)](#sec-5)
- [QUESTION BANK / MUST-DO PROBLEMS](#sec-6)
  - [High-frequency Infosys SP/DSE problems (practice on LeetCode/GfG)](#sec-7)
  - [CS Fundamentals — interview Q&A (be crisp)](#sec-8)
    - [DBMS / SQL](#sec-9)
    - [OOP](#sec-10)
    - [Operating Systems](#sec-11)
    - [Computer Networks](#sec-12)
  - [Behavioral / HR (tailored to Shivam)](#sec-13)
- [MEGA RESOURCE VAULT (DSA sheets, platforms, PYQ, courses)](#sec-14)
  - [DSA sheets (pick ONE and finish it)](#sec-15)
  - [Practice platforms](#sec-16)
  - [Infosys-specific PYQ / guides](#sec-17)
  - [YouTube](#sec-18)
  - [CS fundamentals resources](#sec-19)
  - [Community compilations (use with caution)](#sec-20)
- [STUDY PLAN & TRACKER](#sec-21)
  - [2-week DSA sprint (test-focused)](#sec-22)
  - [Daily routine](#sec-23)
  - [Progress tracker](#sec-24)
  - [Golden rules](#sec-25)
- [MEGA RESOURCE VAULT v2 (Infosys PYQ repos, DP/DSA patterns, more)](#sec-26)
  - [Infosys / HackWithInfy PYQ — GitHub & pages (GOLD — practice exact style)](#sec-27)
  - [Dynamic Programming (HIGHEST priority for this test)](#sec-28)
  - [DSA patterns (recognize-the-pattern approach)](#sec-29)
  - [Solution manuals / compiled PYQ (verify, use as practice)](#sec-30)
  - [Online judges for timed practice (simulate 3Q/180 min)](#sec-31)
  - [Language-specific (pick ONE for the test — C++/Java/Python)](#sec-32)
  - [CS fundamentals (interview round)](#sec-33)
- [DEEP RESEARCH v2 — Selection intel, cutoffs & real interview questions](#sec-34)
  - [★ EXACT selection cutoffs (from 2025–2026 SP/DSE experiences)](#sec-35)
  - [★ Boost your shortlist: InfyTQ certification (FREE)](#sec-36)
  - [Test recap (our drive)](#sec-37)
  - [★ Technical Interview — REAL questions asked (prepare crisp answers + code)](#sec-38)
    - [OOP (asked in almost every interview — give REAL examples, not just definitions)](#sec-39)
    - [DBMS / SQL (standard)](#sec-40)
    - [Operating Systems](#sec-41)
    - [Computer Networks](#sec-42)
    - [Java (if you choose Java in the interview)](#sec-43)
    - [DSA in interview](#sec-44)
    - [Projects & HR](#sec-45)
  - [★ SP/DSE frequently-asked coding problems (drill these specifically)](#sec-46)
  - [Extra Infosys-specific resources (links)](#sec-47)
  - [Winning game-plan (to actually convert)](#sec-48)
- [ULTIMATE RESOURCE INDEX (everything — every source type)](#sec-49)
  - [1. Official Infosys / HackWithInfy](#sec-50)
  - [2. Coding practice platforms (DSA)](#sec-51)
  - [3. Competitive programming (for the hard test questions)](#sec-52)
  - [4. Structured DSA sheets/roadmaps (pick ONE, finish it)](#sec-53)
  - [5. YouTube — DSA & DP](#sec-54)
  - [6. YouTube — CS fundamentals (technical interview)](#sec-55)
  - [7. CS fundamentals notes/references (technical round)](#sec-56)
  - [8. GitHub — interview question banks & sheets](#sec-57)
  - [9. Cheatsheets](#sec-58)
  - [10. PYQ / Interview experiences (READ these — pattern signal)](#sec-59)
  - [11. LinkedIn (real experiences + networking)](#sec-60)
  - [12. Telegram channels (UNOFFICIAL — use for job alerts/PYQ, verify before trusting)](#sec-61)
  - [13. Google Drive / Scribd compilations (UNOFFICIAL — reference only)](#sec-62)
  - [14. Mock interviews & soft skills (HR round)](#sec-63)
  - [15. Aptitude (only if a section appears; our SP/DSE test is pure coding)](#sec-64)
  - [How to actually use this (don't drown)](#sec-65)
- [BONUS: NICHE / HIDDEN GEMS (things most people miss)](#sec-66)
  - [Pattern-based prep (learn patterns, not just problems)](#sec-67)
  - [Algorithm visualizers & CP learning (hidden but gold)](#sec-68)
  - [YouTube — high-signal (DSA/DP/graphs) that most miss](#sec-69)
  - [GitHub — high-value repos most miss](#sec-70)
  - [Company-tagged practice (find Infosys-tagged problems free)](#sec-71)
  - [Communities (ask doubts, get real intel)](#sec-72)
  - [HR / behavioral (extra)](#sec-73)
  - [Aptitude/verbal (only if a future Infosys SE track applies — NOT this coding test)](#sec-74)
  - [Reality check (honest)](#sec-75)

<!-- TOC END -->










> Goal: crack the online coding test (3 DSA problems / 180 min) → clear the 60-min technical
> interview. This role is **DSA-heavy** — the test tier decides your package (DSE ₹6.25L →
> SP L1 ₹10L → L2 ₹16L → L3 ₹21L). Aim high: strong DSA = higher tier.
> JD & logistics: `06-job-descriptions/infosys-specialist-programmer-2027.md`.

<a id="sec-2"></a>
## Company snapshot — Infosys Ltd
- Global IT services & consulting giant (HQ Bengaluru); 300k+ employees; clients worldwide.
- **SP/DSE** are Infosys's **premium fresher tech roles** (via HackWithInfy-style coding tests),
  targeting strong problem-solvers — much higher pay than the standard Systems Engineer role.
- Work: modernizing enterprise systems, cloud-native microservices, GenAI pipelines, data — across
  any technology (you must be flexible). PAN-India posting.

<a id="sec-3"></a>
## Hiring process (deep research — GeeksforGeeks/Medium/Great Learning)
1. **Online Programming Test** — **3 coding questions, 180 minutes**, DSA medium→hard.
   - Topics seen: **Dynamic Programming (very common), Greedy, Graphs, Arrays/Strings, Bit
     Manipulation, Recursion/Backtracking, Math/Number theory, Hashing, Heaps, Multisets**.
   - Question switching allowed; **partial scoring** by test cases (passing 50–60% of 2–3 Qs often
     earns an interview call). Constraints are high → brute force won't pass; optimize.
   - Proctored via **Infosys Wingspan** (detects external apps). Compilers are good; multiple langs.
2. **In-depth Technical Interview (~60 min)** for those who clear:
   - Deep DSA (explain approach → code → time/space complexity; sometimes on paper).
   - **CS fundamentals: DBMS/SQL, OOP, Operating Systems, Computer Networks.**
   - **Project discussion** (they probe your resume — NETWORKED, Parakh, etc.).
   - Sometimes puzzles/aptitude; behavioral ("why Infosys", relocation, learn any tech).

<a id="sec-4"></a>
## Test strategy (180 min, 3 questions)
- First 10 min: read ALL 3, gauge difficulty, start with the one you can fully solve.
- Aim: 1 full + strong partials on the other 2 (partial test cases count).
- Write a brute force first if stuck, then optimize; handle edge cases & constraints (int overflow,
  large N → need O(n log n) / O(n)).
- Test with sample + edge inputs before moving on. Manage time (~55–60 min/question max).

<a id="sec-5"></a>
## DSA topic-wise plan (the core — master these)
- **Arrays & Strings:** two pointers, sliding window, prefix sums, sorting, Kadane's.
- **Hashing:** frequency maps, two-sum patterns, grouping.
- **Recursion & Backtracking:** subsets, permutations, N-Queens, combination sum.
- **Dynamic Programming (HIGH priority):** 0/1 knapsack, LCS/LIS, coin change, edit distance,
  matrix DP, DP on subsequences, DP on strings.
- **Greedy:** interval scheduling, activity selection, Huffman-ish, jump game.
- **Graphs:** BFS/DFS, connected components, topological sort, Dijkstra, Union-Find (DSU).
- **Trees:** traversals, BST ops, LCA, height/diameter.
- **Stacks/Queues:** next greater element, monotonic stack, sliding-window max.
- **Heaps/Priority Queue:** top-K, merge K lists, median.
- **Bit Manipulation:** XOR tricks, set/clear bits, subsets via bitmask.
- **Math/Number theory:** GCD/LCM, sieve, modular arithmetic, fast power.
- **Complexity:** always state Big-O; know log/linear/quadratic tradeoffs.

---

<a id="sec-6"></a>
# QUESTION BANK / MUST-DO PROBLEMS

<a id="sec-7"></a>
## High-frequency Infosys SP/DSE problems (practice on LeetCode/GfG)
- Best Time to Buy & Sell Stock (I/II) · Kadane's Maximum Subarray
- Longest Common Subsequence (LCS) · Longest Increasing Subsequence (LIS)
- 0/1 Knapsack · Coin Change · Edit Distance · Matrix path DP (min/max path sum, unique paths)
- Rotten Oranges (BFS) · Number of Islands · Course Schedule (topo sort) · Dijkstra shortest path
- Next Smallest Palindrome · Swap two numbers without temp · Build a heap from array
- Subsets/Permutations (backtracking) · Combination Sum · N-Queens
- Next Greater Element (monotonic stack) · Sliding Window Maximum
- Top-K frequent elements · Merge K sorted lists · Kth largest
- Trapping Rain Water · Two Sum / 3Sum · Group Anagrams
- Detect cycle (linked list / graph) · LCA in BST/Binary Tree · Diameter of tree
- Bit tricks: single number (XOR), count set bits, power of two
> Do the **Striver SDE Sheet / NeetCode 150 / GfG Infosys SDE Sheet** systematically.

<a id="sec-8"></a>
## CS Fundamentals — interview Q&A (be crisp)
<a id="sec-9"></a>
### DBMS / SQL
- Normalization (1NF–3NF, BCNF); why normalize (reduce redundancy/anomalies).
- Keys: primary, foreign, candidate, composite. Indexes (speed reads, slow writes).
- ACID; transactions; isolation levels (dirty/phantom reads).
- JOINs (inner/left/right/full); GROUP BY vs WHERE vs HAVING; subqueries.
- DELETE vs TRUNCATE vs DROP. Write: 2nd highest salary, Nth highest, duplicates.

<a id="sec-10"></a>
### OOP
- 4 pillars: Encapsulation, Abstraction, Inheritance, Polymorphism (overloading vs overriding).
- Abstract class vs interface; composition vs inheritance; SOLID basics.

<a id="sec-11"></a>
### Operating Systems
- Process vs thread; context switching; scheduling (FCFS/SJF/RR/priority).
- Deadlock (4 conditions + prevention/avoidance/Banker's); semaphore/mutex; race condition.
- Paging vs segmentation; virtual memory; thrashing.

<a id="sec-12"></a>
### Computer Networks
- OSI/TCP-IP layers; TCP vs UDP; 3-way handshake; HTTP/HTTPS; DNS; how a URL loads.
- IP/subnetting basics; status codes; public vs private IP.

<a id="sec-13"></a>
## Behavioral / HR (tailored to Shivam)
- **Self-intro:** final-year CSE @ ITM (2027); strong in DSA + full-stack (React/Django); shipped
  live products (NETWORKED, Parakh ERP), President of IDC, Hacksagon Top Performer; love solving
  hard problems — a great fit for Infosys SP/DSE.
- **Why Infosys?** premium tech role, exposure to enterprise-scale systems + latest tech (cloud,
  GenAI), strong learning/mentorship, PAN-India opportunities, and a role that rewards coding skill.
- **Relocate anywhere?** Yes. **Work in any technology?** Yes — I pick up stacks fast.
- **Project deep-dive:** be ready to explain NETWORKED & Parakh architecture, your role, tradeoffs.
- Puzzles: practice a few classic ones (bulbs, egg drop, weighing balls).

---

<a id="sec-14"></a>
# MEGA RESOURCE VAULT (DSA sheets, platforms, PYQ, courses)

<a id="sec-15"></a>
## DSA sheets (pick ONE and finish it)
- ⭐ **Striver A2Z DSA Course** (best structured): https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/
- ⭐ **Striver SDE Sheet** (191 Qs, interview-focused): https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/
- ⭐ **NeetCode 150 / Blind 75**: https://neetcode.io/practice
- **Love Babbar 450 DSA**: https://github.com/itz-scarecrow/Love-Babbar-450
- **GfG Infosys SDE Sheet**: https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/
- Repos: abhiXsliet/DSA-SHEETS: https://github.com/abhiXsliet/DSA-SHEETS ·
  shubhanshurav/Interview-Preparation-Notes (PDFs): https://github.com/shubhanshurav/Interview-Preparation-Notes

<a id="sec-16"></a>
## Practice platforms
- ⭐ **LeetCode** (Top Interview 150 + patterns): https://leetcode.com/studyplan/top-interview-150/
- ⭐ **GeeksforGeeks Practice** (Infosys-tagged): https://www.geeksforgeeks.org/explore
- **Codeforces** (for hard/constraint-heavy, like SP test): https://codeforces.com/
- **CodeChef** (DSA + contests): https://www.codechef.com/
- **HackerRank** (Infosys often uses similar UI): https://www.hackerrank.com/
- **CodingNinjas / Naukri Code360**: https://www.naukri.com/code360/

<a id="sec-17"></a>
## Infosys-specific PYQ / guides
- GeeksforGeeks — Infosys SP/DSE interview experiences:
  https://www.geeksforgeeks.org/  (search "Infosys Specialist Programmer" / "Infosys DSE")
- Great Learning — Crack Infosys SP & DSE 2026: https://www.mygreatlearning.com/blog/infosys-sp-dse-interview-guide-2026/
- Educative — Infosys coding interview questions: https://www.educative.io/blog/infosys-coding-interview-questions
- CCBP — Infosys coding questions: https://www.ccbp.in/blog/articles/infosys-coding-questions
- PrepInsta — Infosys SP/DSE (test pattern + PYQ): https://prepinsta.com/
- HackWithInfy 2026 material (Scribd): search "HackWithInfy 2026 Complete Material"

<a id="sec-18"></a>
## YouTube
- ⭐ **take U forward (Striver)** — A2Z DSA, DP playlist: https://www.youtube.com/@takeUforward
- **Aditya Verma** — DP & recursion (best for DP): https://www.youtube.com/@AdityaVermaTheProgrammingLord
- **CodeHelp - Love Babbar** — DSA (Hindi): https://www.youtube.com/@CodeHelp
- **Abdul Bari** — algorithms (deep): https://www.youtube.com/@abdul_bari
- **Gate Smashers** — DBMS/OS/CN (interview theory): https://www.youtube.com/@GateSmashers

<a id="sec-19"></a>
## CS fundamentals resources
- DBMS/OS/CN: Gate Smashers + GfG (https://www.geeksforgeeks.org/)
- SQL practice: LeetCode SQL 50 (https://leetcode.com/studyplan/top-sql-50/), DataLemur (https://datalemur.com/)
- OOP: GfG OOP + Java/C++ oops interview Qs
- System design (basics): https://github.com/donnemartin/system-design-primer

<a id="sec-20"></a>
## Community compilations (use with caution)
- HackWithInfy / Infosys prep **Google Drive & Telegram** compilations exist — search
  `Infosys Specialist Programmer PYQ drive` / `HackWithInfy material`. Unofficial; verify. Prefer
  the sheets/platforms above (Striver/NeetCode/GfG) which are trusted and complete.

---

<a id="sec-21"></a>
# STUDY PLAN & TRACKER

<a id="sec-22"></a>
## 2-week DSA sprint (test-focused)
- **D1–2:** Arrays/Strings (two-pointer, sliding window, prefix), Hashing — 8–10 problems/day.
- **D3:** Recursion & Backtracking (subsets/permutations/combination sum).
- **D4–6:** **Dynamic Programming** (Aditya Verma playlist) — knapsack, LCS/LIS, coin change,
  edit distance, matrix DP — highest ROI for Infosys.
- **D7:** Greedy + intervals.
- **D8–9:** Graphs (BFS/DFS, topo sort, Dijkstra, DSU) + Trees.
- **D10:** Stacks/queues (monotonic), Heaps (top-K), Bit manipulation, Math.
- **D11:** Timed mock (3 problems / 180 min) on LeetCode/Code360 — simulate the real test.
- **D12:** CS fundamentals (DBMS + OS) revision.
- **D13:** CS fundamentals (CN + OOP) + SQL queries + puzzles.
- **D14:** Project deep-dive notes + HR answers + 1 more timed mock.

<a id="sec-23"></a>
## Daily routine
- 2 hrs DSA (topic + 6–8 problems) · 45 min CS fundamentals · 30 min SQL/puzzles ·
  15 min revise a "mistakes/patterns" log.

<a id="sec-24"></a>
## Progress tracker
- [ ] Arrays/Strings/Hashing · [ ] Recursion/Backtracking · [ ] **DP** · [ ] Greedy
- [ ] Graphs · [ ] Trees · [ ] Stacks/Queues/Heaps · [ ] Bit/Math
- [ ] Finished a full sheet (Striver SDE / NeetCode 150)
- [ ] 3 timed 3-question mocks (180 min each)
- [ ] DBMS · [ ] OS · [ ] CN · [ ] OOP · [ ] SQL queries
- [ ] Project deep-dive notes (NETWORKED, Parakh) · [ ] "Why Infosys" + HR
- [ ] System Check done + resume PDF uploaded

<a id="sec-25"></a>
## Golden rules
- **DP is the highest-frequency topic** — over-invest there (Aditya Verma playlist).
- Practice **timed 3-question mocks** — stamina + time management win the 180-min test.
- Always optimize past brute force (high constraints) and state complexity.
- In the interview: think aloud, write clean code, know your projects cold.

---

<a id="sec-26"></a>
# MEGA RESOURCE VAULT v2 (Infosys PYQ repos, DP/DSA patterns, more)

<a id="sec-27"></a>
## Infosys / HackWithInfy PYQ — GitHub & pages (GOLD — practice exact style)
- ⭐ **karthikreddy-7/Infosys-SP-Coding-Questions** (SP coding Qs):
  https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions
- ⭐ **itsmeheisenberg/HackWithInfy** (sample coding Qs + Java solutions):
  https://github.com/itsmeheisenberg/HackWithInfy
- **shubhammore9/InfyTQ_Coding** (Python & Java coding Qs + solutions):
  https://github.com/shubhammore9/InfyTQ_Coding
- **SUDARSHANTADAGE/InfyTQ-Answers** (InfyTQ assignments/quiz):
  https://github.com/SUDARSHANTADAGE/InfyTQ-Answers
- **PrepInsta — Infosys SP coding Qs**: https://prepinsta.com/infosys-sp-and-dse/specialist-programmer/coding-questions/
- **PrepInsta — HackWithInfy coding**: https://prepinsta.com/hackwithinfy/coding/
- **Codeforces — Infosys OA/contest problems** (community): https://codeforces.com/blog/entry/90569
- Great Learning SP/DSE guide (PYQ + pattern): https://www.mygreatlearning.com/blog/infosys-sp-dse-interview-guide-2026/
- CCBP Infosys coding Qs (C/C++/Java/Python solutions): https://www.ccbp.in/blog/articles/infosys-coding-questions

<a id="sec-28"></a>
## Dynamic Programming (HIGHEST priority for this test)
- ⭐ **Aditya Verma — DP playlist** (best intuition, Hindi): https://www.youtube.com/@AdityaVermaTheProgrammingLord
- ⭐ **Striver — DP playlist (A2Z / DP series)**: https://takeuforward.org/ (DP section) + YouTube @takeUforward
- **Grokking DP Patterns (notes mirror)**: https://github.com/asutosh97/educative-io-contents/blob/master/Grokking%20Dynamic%20Programming%20Patterns%20for%20Coding%20Interviews.md
- **aatalyk/Dynamic-Programming-Patterns**: https://github.com/aatalyk/Dynamic-Programming-Patterns
- **claytonjwong/The-ART-of-Dynamic-Programming**: https://github.com/claytonjwong/The-ART-of-Dynamic-Programming
- 7 DP patterns (linear, 2D grid, subsequence, knapsack, interval, tree, bitmask) — learn to
  recognize the pattern in the first 2 minutes.

<a id="sec-29"></a>
## DSA patterns (recognize-the-pattern approach)
- ⭐ **Chanda-Abdul/Several-Coding-Patterns** (Grokking coding patterns):
  https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews
- **PranabNandy/Leetcode-Patterns**: https://github.com/PranabNandy/Leetcode-Patterns
- **Dummy-Bug/Data-Structures-and-Algorithms** (most-asked Qs from LC/GfG/IB/sheets):
  https://github.com/Dummy-Bug/Data-Structures-and-Algorithms
- **14 patterns gist**: https://gist.github.com/mathcodes/cc2990f03dcfc16523c433328c4499d3
- **NeetCode Roadmap** (visual pattern map): https://neetcode.io/roadmap

<a id="sec-30"></a>
## Solution manuals / compiled PYQ (verify, use as practice)
- Scribd — "Infosys SP/DSE Coding Problems Solution Manual" (13 PYQ 2021–2025, C++/Java/Python).
- Scribd — "HackWithInfy 2026 Complete Material" (DSA + CS + PPI).
- (Community Google Drive/Telegram HackWithInfy dumps exist — search
  `HackWithInfy previous year questions drive`; unofficial, verify before trusting.)

<a id="sec-31"></a>
## Online judges for timed practice (simulate 3Q/180 min)
- LeetCode contests + patterns: https://leetcode.com/
- Codeforces (Div 3/Div 4 for speed): https://codeforces.com/
- CodeChef (Starters contests): https://www.codechef.com/
- AtCoder (Beginner Contests — great for constraint-heavy): https://atcoder.jp/
- GeeksforGeeks Practice (company-tagged Infosys): https://www.geeksforgeeks.org/explore

<a id="sec-32"></a>
## Language-specific (pick ONE for the test — C++/Java/Python)
- C++ STL for CP: https://www.geeksforgeeks.org/the-c-standard-template-library-stl/
- Java collections for DSA: https://www.geeksforgeeks.org/collections-in-java-2/
- Python for CP (fast I/O, collections/heapq/bisect): https://realpython.com/

<a id="sec-33"></a>
## CS fundamentals (interview round)
- Gate Smashers (DBMS/OS/CN): https://www.youtube.com/@GateSmashers
- Love Babbar OS/DBMS/CN one-shots: https://www.youtube.com/@CodeHelp
- SQL: LeetCode SQL 50 https://leetcode.com/studyplan/top-sql-50/ · DataLemur https://datalemur.com/
- OOP + System design basics: https://github.com/donnemartin/system-design-primer

---

<a id="sec-34"></a>
# DEEP RESEARCH v2 — Selection intel, cutoffs & real interview questions

<a id="sec-35"></a>
## ★ EXACT selection cutoffs (from 2025–2026 SP/DSE experiences)
- Solve **~1 to 1.5 questions** (majority of test cases) → **Digital Specialist Engineer (DSE)** shortlist.
- Solve **2 questions fully** → **Specialist Programmer (SP)** interview call.
- Solve **all 3** → top tier (Power Programmer / higher SP level, up to **L3 ₹21 LPA**).
- Partial test cases COUNT; question switching allowed.
> **Target: 2 full solves minimum** for SP. Every extra fully-solved question bumps your tier/package.

<a id="sec-36"></a>
## ★ Boost your shortlist: InfyTQ certification (FREE)
- **InfyTQ** is Infosys's free learning + certification platform. Clearing the InfyTQ certification
  improves shortlisting for the SP track and looks great pre-drive. Do it if time permits.
- Portal: https://www.infytq.onwingspan.com/

<a id="sec-37"></a>
## Test recap (our drive)
- 3 coding questions, **180 minutes**, DSA medium→hard. Languages: C/C++/Java/Python — use your
  strongest (**Java or Python** for you). This SP/DSE coding test has **no aptitude/verbal MCQ**
  section (that's Infosys's separate "Systems Engineer" track). Pure coding here.

<a id="sec-38"></a>
## ★ Technical Interview — REAL questions asked (prepare crisp answers + code)
<a id="sec-39"></a>
### OOP (asked in almost every interview — give REAL examples, not just definitions)
- Explain the 4 pillars (Encapsulation, Abstraction, Inheritance, Polymorphism) with real examples.
- Method overriding vs overloading — write code. Runtime vs compile-time polymorphism.
- Does Java support multiple inheritance? (No for classes; yes via interfaces — why.)
- Abstract class vs interface; `super`/`this`; constructor overloading.

<a id="sec-40"></a>
### DBMS / SQL (standard)
- Normalization 1NF → 2NF → 3NF → BCNF (with an example table).
- DDL / DML / DCL / TCL commands (+ examples). Give examples for DDL commands.
- Write SQL to UPDATE a column based on a given email id. Practice UPDATE/SELECT queries.
- All JOIN types; primary vs foreign key; triggers; indexing; ACID; DELETE vs TRUNCATE.
- Classic: 2nd/Nth highest salary; find duplicates; group-by + having.

<a id="sec-41"></a>
### Operating Systems
- Process vs thread; context switching; scheduling (FCFS/SJF/RR/Priority).
- Deadlock (4 conditions + prevention/avoidance); semaphore vs mutex; race condition.
- Paging vs segmentation; virtual memory; thrashing.

<a id="sec-42"></a>
### Computer Networks
- OSI vs TCP/IP layers; TCP vs UDP; 3-way handshake; HTTP/HTTPS; DNS; what happens when you type a URL.

<a id="sec-43"></a>
### Java (if you choose Java in the interview)
- JDK vs JRE vs JVM; `==` vs `.equals()`; String immutability & String pool.
- Collections: ArrayList vs LinkedList, HashMap internals; `final` vs `finally` vs `finalize`.
- Exception handling (checked vs unchecked); interfaces vs abstract classes.

<a id="sec-44"></a>
### DSA in interview
- They pick a problem → you explain **approach → code (sometimes on paper) → time/space complexity**,
  then optimize. Think aloud; dry-run with an example.

<a id="sec-45"></a>
### Projects & HR
- Deep-dive on YOUR projects (NETWORKED, Parakh): architecture, DB schema, challenges, what you'd improve.
- HR: tell me about yourself; **why Infosys**; willing to relocate PAN-India? work in any tech? strengths/weaknesses.

<a id="sec-46"></a>
## ★ SP/DSE frequently-asked coding problems (drill these specifically)
- Rotten Oranges (BFS) — very frequent · Longest Common Subsequence (LCS) · LIS
- Next Smallest Palindrome · Swap two numbers without a temp variable · Build a heap from an array
- Coin Change · Edit Distance · Matrix path DP · 0/1 Knapsack
- Dijkstra / shortest path · Topological sort · Number of Islands
- Best Time to Buy & Sell Stock · Two Sum · Remove duplicates from sorted array · Sentence palindrome
- Trapping Rain Water · Next Greater Element (monotonic stack) · Single Number (XOR)

<a id="sec-47"></a>
## Extra Infosys-specific resources (links)
- ⭐ InfyTQ (free cert + practice): https://www.infytq.onwingspan.com/
- Great Learning — Crack Infosys SP & DSE 2026: https://www.mygreatlearning.com/blog/infosys-sp-dse-interview-guide-2026/
- faceprep — Infosys technical interview questions: https://faceprep.in/article/infosys-technical-interview-questions/
- faceprep — Infosys recruitment pattern: https://faceprep.in/article/infosys-recruitment-pattern-important-topics-and-about-the-company/
- techprep.app — Infosys interview process: https://www.techprep.app/blog/infosys-interview-process
- interviewquery — Infosys SE guide: https://www.interviewquery.com/interview-guides/infosys-software-engineer
- Sumit Raghuwanshi — Infosys SP prep (Medium): https://sumitraghuwanshi.medium.com/infosys-specialist-programmer-sp-interview-preparation-guide-2024-906809148f4e
- GfG — Infosys SDE Sheet: https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/
- mindmajix — Top Infosys interview Qs: https://mindmajix.com/infosys-interview-questions
- PrepInsta — Infosys SP/DSE test pattern + PYQ: https://prepinsta.com/infosys/

<a id="sec-48"></a>
## Winning game-plan (to actually convert)
1. **Test:** aim for **2–3 full solves** → grind DP + graphs + arrays/strings; do timed 3Q/180-min mocks.
2. **InfyTQ cert** done (bonus shortlist points).
3. **Interview:** OOP (with examples) + DBMS/SQL + OS + CN + Java basics + **your projects cold**.
4. **HR:** confident "why Infosys", yes to relocation + any tech.
5. Keep a **mistakes log**; revise every 2 days; sleep before the test; System Check done.

---

<a id="sec-49"></a>
# ULTIMATE RESOURCE INDEX (everything — every source type)

> Exhaustive. Prioritize ⭐. External community sources (Telegram/Drive/Scribd) are UNOFFICIAL —
> use for reference only, verify before trusting; prefer the official/curated ones.

<a id="sec-50"></a>
## 1. Official Infosys / HackWithInfy
- HackWithInfy official: https://www.infosys.com/careers/hackwithinfy.html
- InfyTQ (free certification + practice — boosts SP shortlisting): https://www.infytq.onwingspan.com/
- Infosys careers: https://www.infosys.com/careers/
- HackWithInfy details (Unstop): https://unstop.com/blog/hackwithinfy-2025-key-details

<a id="sec-51"></a>
## 2. Coding practice platforms (DSA)
- ⭐ LeetCode: https://leetcode.com/  (Top Interview 150, patterns, contests)
- ⭐ GeeksforGeeks Practice: https://www.geeksforgeeks.org/explore  (Infosys-tagged problems)
- ⭐ Coding Ninjas / Naukri Code360: https://www.naukri.com/code360/
- HackerRank: https://www.hackerrank.com/  (Infosys often uses similar test UI)
- InterviewBit: https://www.interviewbit.com/
- Codolio (track progress + curated sheets): https://codolio.com/
- Scaler Topics (free DSA): https://www.scaler.com/topics/

<a id="sec-52"></a>
## 3. Competitive programming (for the hard test questions)
- ⭐ Codeforces: https://codeforces.com/  (Div 2/3 problems — closest to SP test difficulty)
- CSES Problem Set (must-do for CP fundamentals): https://cses.fi/problemset/
- AtCoder (Beginner Contests): https://atcoder.jp/
- ⭐ cp-algorithms (algorithm reference): https://cp-algorithms.com/
- CodeChef (practice + contests): https://www.codechef.com/

<a id="sec-53"></a>
## 4. Structured DSA sheets/roadmaps (pick ONE, finish it)
- ⭐ Striver A2Z DSA: https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/
- ⭐ Striver SDE Sheet: https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/
- ⭐ NeetCode 150 / Blind 75 / Roadmap: https://neetcode.io/practice  ·  https://neetcode.io/roadmap
- Grind 75: https://www.techinterviewhandbook.org/grind75/
- Love Babbar 450: https://github.com/itz-scarecrow/Love-Babbar-450
- GfG Infosys SDE Sheet: https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/
- roadmap.sh DSA: https://roadmap.sh/datastructures-and-algorithms

<a id="sec-54"></a>
## 5. YouTube — DSA & DP
- ⭐ take U forward (Striver) — A2Z + SDE + graphs/DP: https://www.youtube.com/@takeUforward
- ⭐ Aditya Verma — DP & recursion (BEST for DP): https://www.youtube.com/@AdityaVermaTheProgrammingLord
- CodeHelp - Love Babbar (DSA, Hindi): https://www.youtube.com/@CodeHelp
- Abdul Bari — algorithms (deep intuition): https://www.youtube.com/@abdul_bari
- NeetCode (LeetCode patterns): https://www.youtube.com/@NeetCode
- Errichto / William Lin (competitive programming): https://www.youtube.com/@Errichto
- Pepcoding, Programming Pathshala — placement DSA
> For Infosys-specific solutions: search **"HackWithInfy solutions <year>"** and
> **"Infosys Specialist Programmer coding questions solved"** on YouTube.

<a id="sec-55"></a>
## 6. YouTube — CS fundamentals (technical interview)
- ⭐ Gate Smashers — DBMS/OS/CN/DSA theory: https://www.youtube.com/@GateSmashers
- Knowledge Gate (Sanchit Jain) — OS/DBMS/CN: https://www.youtube.com/@KnowledgeGate
- Jenny's Lectures — DBMS/DS: https://www.youtube.com/@JennyslecturesCSIT
- Telusko / CodeWithHarry — Java/Python OOP: https://www.youtube.com/@Telusko

<a id="sec-56"></a>
## 7. CS fundamentals notes/references (technical round)
- GfG DBMS: https://www.geeksforgeeks.org/dbms/  · OS: https://www.geeksforgeeks.org/operating-systems/
  · CN: https://www.geeksforgeeks.org/computer-network-tutorials/  · OOP: https://www.geeksforgeeks.org/oops-concept-in-java/
- SQL practice: LeetCode SQL 50 (https://leetcode.com/studyplan/top-sql-50/) · DataLemur (https://datalemur.com/) · SQLBolt (https://sqlbolt.com/)
- last-minute notes (LMN) GfG: https://www.geeksforgeeks.org/last-minute-notes/

<a id="sec-57"></a>
## 8. GitHub — interview question banks & sheets
- yangshun/tech-interview-handbook: https://github.com/yangshun/tech-interview-handbook
- jwasham/coding-interview-university: https://github.com/jwasham/coding-interview-university
- donnemartin/system-design-primer: https://github.com/donnemartin/system-design-primer
- TheAlgorithms (Python/Java/C++): https://github.com/TheAlgorithms
- abhiXsliet/DSA-SHEETS (Striver+Babbar): https://github.com/abhiXsliet/DSA-SHEETS
- shubhanshurav/Interview-Preparation-Notes (PDF notes): https://github.com/shubhanshurav/Interview-Preparation-Notes
- sathvik-spartan/Neetcode-150-and-Blind-75 (+Anki): https://github.com/sathvik-spartan/Neetcode-150-and-Blind-75-DSA-Practice-
- Pradetto/DSA-Cheat-Sheets: https://github.com/Pradetto/DSA-Cheat-Sheets

<a id="sec-58"></a>
## 9. Cheatsheets
- Big-O cheat sheet: https://www.bigocheatsheet.com/
- DSA cheat sheets (repo above); cp-algorithms for templates
- SQL cheatsheet (sql-tutorial): https://mode.com/sql-tutorial/
- DevDocs (offline all-in-one): https://devdocs.io/
- Java/Python quick refs on GfG

<a id="sec-59"></a>
## 10. PYQ / Interview experiences (READ these — pattern signal)
- ⭐ GeeksforGeeks — search "Infosys Specialist Programmer" / "Infosys DSE" / "HackWithInfy":
  https://www.geeksforgeeks.org/  (Interview Experiences section)
- PrepInsta Infosys SP/DSE (test pattern + PYQ): https://prepinsta.com/infosys/
- faceprep Infosys guides: https://faceprep.in/  (technical Qs, pattern, HR)
- Glassdoor — Infosys "Interviews" tab: https://www.glassdoor.co.in/
- AmbitionBox — Infosys interviews: https://www.ambitionbox.com/
- Medium — Infosys SP prep (Sumit Raghuwanshi): https://sumitraghuwanshi.medium.com/infosys-specialist-programmer-sp-interview-preparation-guide-2024-906809148f4e
- Great Learning SP/DSE guide: https://www.mygreatlearning.com/blog/infosys-sp-dse-interview-guide-2026/

<a id="sec-60"></a>
## 11. LinkedIn (real experiences + networking)
- Search: **"Infosys Specialist Programmer interview experience"**, **"HackWithInfy"**, **"Infosys DSE"**
  in LinkedIn search + filter by "Posts".
- Follow hashtags: #HackWithInfy #InfosysSP #InfosysHiring #PlacementPreparation #DSA.
- Connect with ITM seniors placed at Infosys → ask for their test/interview experience directly.
- Post your prep journey (visibility) — Shivam already active (1,684 followers).

<a id="sec-61"></a>
## 12. Telegram channels (UNOFFICIAL — use for job alerts/PYQ, verify before trusting)
- Search on Telegram: **"HackWithInfy"**, **"Infosys placement"**, **"off campus jobs"**,
  **"coding placement material"**, **"DSA sheets"**.
- Commonly cited fresher-job/placement channels (verify current): "Off Campus Jobs 4u",
  "IT Freshers Jobs", "Coding Interview Prep", "Placement Material". (Names change — search, don't trust blindly.)
- Use them for **drive alerts + shared PDFs**, not as primary learning.

<a id="sec-62"></a>
## 13. Google Drive / Scribd compilations (UNOFFICIAL — reference only)
- Search: **"HackWithInfy 2026 complete material"**, **"Infosys DSE roadmap pdf"**,
  **"Infosys Specialist Programmer PYQ drive"**.
- Scribd examples: "INFOSYS HackWithInfy 2026 Complete Material", "Infosys DSE Roadmap".
- ⚠️ These are community-shared; may be outdated/inaccurate — cross-check with LeetCode/GfG.

<a id="sec-63"></a>
## 14. Mock interviews & soft skills (HR round)
- Pramp / Exponent (free peer mocks): https://www.pramp.com/
- interviewing.io (anonymous mocks): https://interviewing.io/
- HR question banks: GfG HR interview Qs, faceprep HR; prepare STAR stories (see HR section above).
- "Tell me about yourself", "Why Infosys", strengths/weaknesses, relocation — rehearse aloud.

<a id="sec-64"></a>
## 15. Aptitude (only if a section appears; our SP/DSE test is pure coding)
- IndiaBix: https://www.indiabix.com/  · PrepInsta aptitude: https://prepinsta.com/
- (Not needed for the 3-coding-question SP/DSE test, but useful if any future Infosys SE track.)

<a id="sec-65"></a>
## How to actually use this (don't drown)
1. ONE sheet (Striver A2Z or NeetCode 150) + LeetCode/Codeforces daily. Don't hop between 10 sheets.
2. Aditya Verma DP + Striver graphs = the two highest-ROI YouTube series for the test.
3. GfG interview experiences + PrepInsta = pattern; do 3 timed 3Q/180-min mocks.
4. Gate Smashers (DBMS/OS/CN) + OOP examples for the technical interview.
5. InfyTQ cert (bonus). Mocks (Pramp) for HR. Keep a mistakes log.

---

<a id="sec-66"></a>
# BONUS: NICHE / HIDDEN GEMS (things most people miss)

<a id="sec-67"></a>
## Pattern-based prep (learn patterns, not just problems)
- ⭐ Sean Prashad — LeetCode Patterns (grouped by pattern): https://seanprashad.com/leetcode-patterns/
- ⭐ AlgoMaster.io (Ashish Pratap Singh) — DSA patterns + newsletter: https://algomaster.io/
- Grokking the Coding Interview (DesignGurus patterns): https://www.designgurus.io/course/grokking-the-coding-interview
- AlgoMonster (pattern drills): https://algo.monster/
- Tech Interview Handbook — Grind75 + best-practice: https://www.techinterviewhandbook.org/

<a id="sec-68"></a>
## Algorithm visualizers & CP learning (hidden but gold)
- ⭐ VisuAlgo (visualize every DS/algo): https://visualgo.net/
- ⭐ Codeforces EDU (ITMO) — binary search, segment tree, two pointers: https://codeforces.com/edu/courses
- USACO Guide (structured CP, free): https://usaco.guide/
- cp-algorithms (reference): https://cp-algorithms.com/  · CSES set: https://cses.fi/problemset/
- Algorithms visualized: https://www.hackerearth.com/practice/ (also has company drives)

<a id="sec-69"></a>
## YouTube — high-signal (DSA/DP/graphs) that most miss
- ⭐ CodeStoryWithMIK (best recent DP/graphs explanations, Hindi): https://www.youtube.com/@codestorywithMIK
- Kunal Kushwaha — DSA bootcamp (free, structured): https://www.youtube.com/@KunalKushwaha
- Luv (competitive + DSA): https://www.youtube.com/@Luv-
- Fraz (interview DSA): https://www.youtube.com/@lets_code_together
- Pepcoding (Sumeet Malik) — DSA foundation: https://www.youtube.com/@Pepcoding

<a id="sec-70"></a>
## GitHub — high-value repos most miss
- kdn251/interviews (algorithms + company prep): https://github.com/kdn251/interviews
- SeanPrashad/leetcode-patterns: https://github.com/seanprashad/leetcode-patterns
- Devinterview-io (topic-wise Q&A): https://github.com/Devinterview-io
- kunal-kushwaha/DSA-Bootcamp-Java: https://github.com/kunal-kushwaha/DSA-Bootcamp-Java
- krishnadey30/LeetCode-Questions-CompanyWise (company-tagged): search on GitHub

<a id="sec-71"></a>
## Company-tagged practice (find Infosys-tagged problems free)
- GeeksforGeeks company tag (Infosys): https://www.geeksforgeeks.org/explore?company=Infosys
- LeetCode Discuss — search "Infosys" (free company lists shared by users): https://leetcode.com/discuss/
- HackerEarth practice + Infosys drives: https://www.hackerearth.com/

<a id="sec-72"></a>
## Communities (ask doubts, get real intel)
- Reddit: r/leetcode, r/developersIndia, r/cscareerquestions, r/csMajors
- Discord: takeUforward, Kunal Kushwaha "Community Classroom", Codeforces
- Peer group: form a 3–4 person prep group; do daily problems + weekend mocks.

<a id="sec-73"></a>
## HR / behavioral (extra)
- Google "Interview Warmup" (free AI practice): https://grow.google/certificates/interview-warmup/
- AmbitionBox HR questions (company-wise): https://www.ambitionbox.com/
- Big Interview / STAR method guides; rehearse out loud + record yourself.

<a id="sec-74"></a>
## Aptitude/verbal (only if a future Infosys SE track applies — NOT this coding test)
- IndiaBix: https://www.indiabix.com/  · PrepInsta: https://prepinsta.com/  · faceprep: https://faceprep.in/

---

<a id="sec-75"></a>
## Reality check (honest)
This prep file now covers essentially every credible source type: official (HackWithInfy/InfyTQ),
platforms (LeetCode/GfG/Codeforces/CSES/Code360/HackerRank), sheets/roadmaps (Striver/NeetCode/
Grind75), patterns (Sean Prashad/AlgoMaster), YouTube (DSA + DP + CS fundamentals), GitHub banks,
cheatsheets, PYQ (GfG/PrepInsta/faceprep/Glassdoor/AmbitionBox), LinkedIn/Telegram/Drive, mocks, HR.
**More links now = diminishing returns.** The lever from here is EXECUTION:
- Finish ONE sheet (Striver A2Z or NeetCode 150). Don't collect, DO.
- Aditya Verma DP + CodeStoryWithMIK/Striver graphs.
- 3 timed 3-question / 180-min mocks (this alone separates selected from not).
- Gate Smashers DBMS/OS/CN + OOP examples for the interview. InfyTQ cert. Projects cold.
