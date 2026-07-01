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
