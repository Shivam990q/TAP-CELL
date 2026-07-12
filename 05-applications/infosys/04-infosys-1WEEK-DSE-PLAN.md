# Infosys — 1-Week DSE "Anyhow Clear" Plan (Shivam)

> 🔖 **PROVENANCE:** ~80% **[AI-GENERATED]** — ye study-plan/schedule AI ne banaya (standard placement-prep
> wisdom pe based). Resource links [SRC]. Problem references `05`/`06` se. Legend: `README.md` → PROVENANCE INDEX.

> Goal: **DSE pakka nikaalna** (₹6.25 LPA floor), aur agar ho jaaye toh SP L1 tak push.
> Reality (deep-research se): DSE ke liye **~1 se 1.5 question worth test cases** pass karne hote hain.
> Matlab: **Q1 (easy) 100% full solve + Q2/Q3 me partial test cases**. Bas yahi 1 hafte me lock karna hai.
>
> Companion files: `05-infosys-QUESTION-BANK.md` (question-wise list), `02-infosys-DEEP-RESEARCH-2026.md`
> (strategy), `07-infosys-specialist-programmer-PREP.md` (full roadmap).

---

## 📁 SAARI FILES ORDER ME — konsi kiske liye (pehle ye padho)
> Ab sab Infosys files ek folder me hain: `05-applications/infosys/` (ye) aur JD
> `06-job-descriptions/infosys/`. Neeche bare filenames = isi `infosys/` folder me hain.

| File (numbered = explorer order) | Kiske liye / kab kholo |
| --- | --- |
| `README.md` | **Master index** — sabse pehle yahi kholo (category/order guide). |
| `01-infosys-specialist-programmer.md` | Application record + form values + **test-day checklist**. Test se 1 din pehle padho. |
| `02-infosys-DEEP-RESEARCH-2026.md` | **Strategy** — kaise select hona hai, marks split, integrity rules. Aaj padho. |
| `03-infosys-ESSENTIALS.md` | **★ DSA me SABSE PEHLE** — Python I/O, STL, algo-selection, pattern-triggers, edge cases, traps. |
| **`04-infosys-1WEEK-DSE-PLAN.md`** (ye file) | **Roz kholo** — 7-din ka day-by-day plan + checkboxes. |
| `05-infosys-QUESTION-BANK.md` | **Roz kholo** — topic-wise exact problems + GOLDMINE 40-list. |
| `06-infosys-SOLUTIONS.md` | **Har goldmine question ka FULL solution** (approach+code+pattern). |
| `07-infosys-specialist-programmer-PREP.md` | Deep reference — resources, 2-week plan, agar time bache. |
| `08-infosys-INTERVIEW-CS.md` | **Interview CS fundamentals FULL answers** (OOP/DBMS/OS/CN/GenAI). |
| `09-infosys-MOCK-PAPERS.md` | **★ Mock papers** — real Infosys-style 3Q/180min sets + REAL PYQ (test se pehle timed karo). |
| `../../06-job-descriptions/infosys/infosys-specialist-programmer-2027.md` | JD — role, eligibility, package, process. |

---

## 🎯 DSE Guarantee Formula (dimag me rakho)
1. **Q1 easy = full solve** (20 marks) → ye tera guaranteed base hai. Isko miss mat karna.
2. **Q2 greedy = brute force + jitne test cases nikle** → 10-20 marks partial.
3. **Q3 DP = brute/recursive solution likho** → 10-20 marks partial.
4. Total ~40-50/100 with good partials = **DSE zone**. 2 full solve = **SP zone**.
> Partial test cases COUNT. Freeze mat hona — aage badho, test cases pass karo.

> 📜 **REAL PYQ:** har din ke topic ke saath, `06-infosys-SOLUTIONS.md` ke **TIER 5 (real Infosys PYQ)**
> ke related problems bhi solve karo. Full real-PYQ list: `05-infosys-QUESTION-BANK.md` (REAL PYQ INDEX).

---

## 🗓️ 7-DIN KA PLAN (roz ~4-5 hrs)

### DAY 0 — FOUNDATION (agar DSA zero hai — ye pehle, warna skip)
> Ek problem solve karne se pehle concepts samajh. Ye din practice nahi, SAMAJHNE ka hai.
- [ ] `03-infosys-ESSENTIALS.md` → **"DSA FROM ZERO" Part A** (complexity/Big-O — N dekh ke algo chunna)
- [ ] Part B (data structures — Array/HashMap/Set/Stack/Queue/Heap/Tree/Graph, analogy se)
- [ ] Part C (15 patterns — kaunsa kab lagta, analogy + mini example)
- [ ] Part 1 (Python cheat-sheet — input/output, dict, list, sort) — syntax comfortable karo
- [ ] Ho gaya? → ab har problem "samajh" aayega. Day 1 se practice shuru.

### DAY 1 — Arrays + Strings + Hashing (Q1 ka bread & butter)
> 80% easy questions yahin se aate hain. Ye din sabse zaroori.
- [ ] Concepts: array traversal, frequency map (HashMap), string basics
- [ ] Problems (LeetCode/GfG):
  - [ ] Two Sum
  - [ ] Best Time to Buy and Sell Stock
  - [ ] Reverse a String / Reverse Integer
  - [ ] Valid Anagram
  - [ ] Valid Palindrome
  - [ ] Group Anagrams
  - [ ] Majority Element (Moore's voting)
  - [ ] Move Zeroes
- [ ] Target: 8 problems solve

### DAY 2 — Two Pointers + Sliding Window + Prefix Sum + Kadane
- [ ] Concepts: two-pointer, sliding window (fixed + variable), prefix sum, Kadane's
- [ ] Problems:
  - [ ] Maximum Subarray (Kadane)
  - [ ] Container With Most Water
  - [ ] Longest Substring Without Repeating Characters
  - [ ] Subarray Sum Equals K (prefix + hashmap)
  - [ ] Remove Duplicates from Sorted Array
  - [ ] Maximum Average Subarray I (fixed window)
  - [ ] Merge Sorted Array
- [ ] Target: 7 problems

### DAY 3 — Searching, Sorting, Binary Search + Recursion basics
- [ ] Concepts: binary search + variations, sort-based tricks, basic recursion
- [ ] Problems:
  - [ ] Binary Search
  - [ ] Search Insert Position
  - [ ] First and Last Position in Sorted Array
  - [ ] Find Minimum in Rotated Sorted Array
  - [ ] Factorial / Fibonacci (recursion)
  - [ ] Power(x, n) (fast power)
  - [ ] Sqrt(x) (binary search)
- [ ] Target: 7 problems

### DAY 4 — GREEDY (Q2 target — 30 marks)
> Ye din Q2 ke liye. Greedy me pattern pehchano: "har step pe locally best choice."
- [ ] Concepts: sorting + greedy choice, intervals, activity selection
- [ ] Problems:
  - [ ] Jump Game
  - [ ] Jump Game II
  - [ ] Assign Cookies
  - [ ] Merge Intervals
  - [ ] Non-overlapping Intervals
  - [ ] Minimum Number of Arrows / Meeting Rooms
  - [ ] Largest Number (array of strings concat)
  - [ ] ★ REAL PYQ: Job Sequencing with Deadlines · Khaled at-most-N/2 (`06` TIER5 R4, R8)
- [ ] Target: 6-8 problems

### DAY 5 — DYNAMIC PROGRAMMING basics (Q3 partials — 50 marks)
> Full nahi karna, bas recursive + basic DP samajh lo taaki partial test cases nikal sake.
> BEST resource: Aditya Verma DP playlist (YouTube).
- [ ] Concepts: recursion → memoization → tabulation. 1D DP + knapsack intro.
  - [ ] Climbing Stairs (intro DP)
  - [ ] House Robber
  - [ ] Coin Change (min coins)
  - [ ] 0/1 Knapsack (GfG)
  - [ ] Longest Common Subsequence (LCS)
  - [ ] Longest Increasing Subsequence (LIS)
  - [ ] ★ REAL PYQ: Subset Sum · Split-array-into-K-segments · Coin Change (`06` TIER5 R7, R1, #17)
- [ ] Target: 6-8 problems (samajh ke, ratke nahi)

### DAY 6 — Stacks/Queues + Graphs (BFS/DFS) + Trees + Bit/Math
> Breadth ke liye — thoda-thoda har topic taaki test me kuch bhi aaye toh attempt kar sako.
- [ ] Problems:
  - [ ] Valid Parentheses (stack)
  - [ ] Next Greater Element (monotonic stack)
  - [ ] Number of Islands (BFS/DFS)
  - [ ] Rotting Oranges (BFS)
  - [ ] Binary Tree Level Order Traversal
  - [ ] Maximum Depth of Binary Tree
  - [ ] Single Number (XOR)
  - [ ] Count Set Bits / Power of Two
  - [ ] ★ REAL PYQ (binary-search-on-answer): Painter's Partition · Aggressive Cows (`06` TIER5 R2, R3)
  - [ ] ★ REAL PYQ: Prime pairs (Sieve) · Distinct-in-window (`06` TIER5 R5, R6)
- [ ] Target: 8-10 problems

### DAY 7 — FULL MOCK + CS Fundamentals + SQL revision
- [ ] **Timed mock: 3 problems / 180 min** — use `09-infosys-MOCK-PAPERS.md` (MOCK SET 1 ya SET 2 — real Infosys-style). Timer lagao, no breaks, no googling. Phir solutions dekho.
- [ ] CS fundamentals quick revise — **FULL answers `08-infosys-INTERVIEW-CS.md` me** (OOP 4 pillars, DBMS normalization/joins, OS process-thread/deadlock, CN OSI/TCP-UDP, ML/GenAI).
- [ ] SQL: 2nd highest salary, find duplicates, GROUP BY + HAVING
- [ ] Apna self-intro + 1 project (NETWORKED/Parakh) bolke practice karo

---

## ✅ Din ka fixed routine
- Subah 2.5 hrs: din ka DSA topic + problems (upar checklist)
- Dopahar 1 hr: kal ke problems dubara (jo galat hue) + "mistakes log"
- Shaam 1 hr: 1 easy problem timed (10-15 min me) — speed banane ke liye

## 🔑 Golden rules (roz yaad rakho)
- **Q1 full karna hai — no matter what.** Wahi DSE ka base hai.
- Stuck? Brute force likho, test cases pass karo, aage badho. Freeze = zero.
- Language: **Java ya Python** (jo comfortable). Fast I/O + STL/collections yaad rakho.
- **Tab/window switch mat karna** test me — auto violation hai (2026 integrity rules).
- Neend puri lo test se pehle. System Check pehle se kar lena.

## 📌 Extra (agar time bache)
- [ ] InfyTQ free certification (SP shortlist boost): https://www.infytq.onwingspan.com/
- [ ] Previous year Infosys questions dekho (repeat hote hain) — QUESTION-BANK file me links

---
> Yaad rakh: DSE ke liye genius banne ki zarurat nahi. **Q1 solid + Q2/Q3 partial = ho gaya.**
> Ye 7 din sincerely kar liya toh DSE anyhow, aur SP ka bhi real chance.
