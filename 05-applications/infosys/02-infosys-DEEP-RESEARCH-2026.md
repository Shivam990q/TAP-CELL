# Infosys SP/DSE — Deep Research 2026 (how to actually get selected)

> 🔖 **PROVENANCE:** ~85% **[WEB-VERIFIED]** — test pattern, marks split, timeline, integrity crackdown,
> packages sab real 2026 web sources se (links inline diye). ~15% **[AI-EXPLANATION]** — AI ne organize +
> strategy notes. TAP-meeting confirmation user se. Legend: `README.md` → PROVENANCE INDEX.

> Compiled 11 Jul 2026 from current (2026) sources. Companion to
> `07-infosys-specialist-programmer-PREP.md` (the big roadmap) and
> `../../06-job-descriptions/infosys/infosys-specialist-programmer-2027.md` (JD).
> Everything here is paraphrased from public sources with links; content was rephrased
> for compliance with licensing restrictions. Verify test-day specifics against Infosys' own
> instructions email.

---

## 0. The one-line reality
Selection is **NOT** "solve all 3 perfectly." It's a **weighted score**: how many test cases you
pass × the difficulty of the question you attempted × how clean your approach is. **Strong partials
across all 3 beat one perfect solve.** Then a calm, clear interview decides SP vs DSE.
(Source: first-hand DSE experience, [Pravallika, Medium, Apr 2026](https://medium.com/@pravallikaseshasai/hackwithinfy-guide-rounds-questions-how-i-landed-the-dse-role-bc4f64db465d).)

---

## 1. The online test — exact structure (2026)
- **3 coding questions, 180 minutes**, no sectional time limit — switch between questions freely.
- Difficulty + marks split (PrepInsta 2026):
  - **Q1 — Easy (20 marks):** basic data structures / algorithms.
  - **Q2 — Medium (30 marks):** usually a **Greedy** problem.
  - **Q3 — Hard (50 marks):** usually **Dynamic Programming**.
- **Partial scoring by test cases** — you get marks for every test case passed, even without a full solve.
- Languages: **C, C++, Java, Python, JavaScript** — use your strongest (Java or Python for you).
- Proctored (Infosys Wingspan / HackerRank-style). Medium→Hard, LeetCode-grade.
- Sources: [PrepInsta SP/DSE coding](https://prepinsta.com/infosys-sp-and-dse/coding-questions/),
  [PrepInsta syllabus 2026](https://prepinsta.com/infosys-sp-and-dse/syllabus),
  [GeeksforGeeks Infosys SDE sheet](https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/).

### Score-maximizing test strategy (do this exact order)
1. **First 10 min:** read all 3. Grab the easy one (Q1) and fully solve + pass all its cases first — bank the 20.
2. Go to whichever of Q2/Q3 you can get the most test cases on. Write **brute force first**, get partial
   cases passing, then optimize. Partial > frozen.
3. Watch constraints: large N means brute force TLEs — you need O(n log n) / O(n). State/aim for the right complexity.
4. Test with sample + edge inputs (empty, 1 element, max N, overflow) before moving on.
5. Never burn 90 min on one question. Rotate. **Target: Q1 full + strong partials on Q2 & Q3.**

---

## 2. Real 2026 timeline (what to expect after the form)
From a candidate who converted last cycle (dates shift, pattern holds):
- Structured prep phase (orientation, navigator sessions, mock tests) rolls out **May–July**.
- **Qualifier test** ~mid-July (their year: **July 12**), online, 3 hrs.
- **Results ~10–12 days later** (~July 24) → candidates split into two tracks:
  - **Category 1 – immediate interviews** (offline, nearest Infosys office, within ~a week). Top
    coders here; strong coding + interview → **SP + hackathon** (~top ~100), decent → **DSE**.
  - **Category 2 – direct interview track** for SP/DSE (no hackathon).
- Interviews stretch across **Sep–Dec**; final results **Jan–Feb**. Both SP & DSE start as "Power Intern" training.
- Source: [Pravallika, Medium](https://medium.com/@pravallikaseshasai/hackwithinfy-guide-rounds-questions-how-i-landed-the-dse-role-bc4f64db465d).

---

## 3. The interview (this is where SP vs DSE is decided)
Format (offline, from 2026 experience): time slot (expect delays) → **live coding round ~45 min,
solve 1 of 2 problems in front of the interviewer** → technical + HR discussion. Carry **laptop,
hard-copy resume, and a 2-slide PPT (intro + career goals)**.

### What they actually ask (prepare all of these)
- **DSA (live):** trees, graphs, **DP**, recursion/backtracking, binary search, greedy, sliding window.
  Real reported problems: longest non-decreasing subsequence (variation), a graph problem, anagrams,
  valid parentheses, matrix rotation. They want **approach → code/pseudocode on paper → complexity**.
- **OOP:** 4 pillars with real examples, overloading vs overriding, abstract class vs interface,
  + basic **design patterns**.
- **DBMS/SQL:** DDL/DML/DCL/DQL, joins, normalization, **window functions**, and writing queries on
  paper (e.g., find/remove duplicate rows, Nth highest salary).
- **OS & CN basics:** process vs thread, deadlock, scheduling; TCP/IP, TCP vs UDP, 3-way handshake, DNS.
- **★ NEW for 2026 — basics of ML / GenAI.** HWI 2026 is explicitly **AI-themed** ("solutions powered
  by AI", generative AI). Be able to explain: what ML is, supervised vs unsupervised, what an LLM/GenAI
  is, what an AI agent/RAG is at a high level. **This is your edge** — you build agents (ROSE, MCP,
  CrewAI). Lead with it.
- **Projects & HR:** deep-dive on YOUR resume (NETWORKED, Parakh ERP) — architecture, DB schema,
  challenges, tradeoffs. Self-intro, internship discussion, "rate your skills honestly," why Infosys,
  relocate PAN-India? work in any tech? (Answer **yes** to both.)
- Sources: [Pravallika/Medium], [faceprep Infosys technical Qs 2026](https://faceprep.in/article/infosys-technical-interview-questions/),
  [Core Java @ Infosys 2026, Medium](https://medium.com/@sparsh187/core-java-interview-questions-asked-in-infosys-2026-complete-guide-a4f95e287be2).

### Interview edge (what converts)
- Solving/attempting well in the **harder** SP-track coding round + a confident interview → **SP**.
- Good interview but only partial coding → typically **DSE**. So: **prep the live-coding round hard**,
  and be genuinely fluent talking about your own projects — most questions branch from your self-intro.

---

## 4. ★ 2026 integrity crackdown — DO NOT get flagged
Infosys publicly flagged **proxy/identity-theft malpractice** (people getting others to sit their
assessments) and **paused tests to tighten verification**. Expect **stricter ID checks + heavier
proctoring** this cycle.
([theworkersrights, Apr 2026](https://www.theworkersrights.com/infosys-recruitment-update-hiring-test-delay-explained/)).

Wingspan/proctoring rules (treat as hard rules):
- **Switching tab / window / app = auto-logged violation.** Do not leave the test screen. Ever.
- No phone, smartwatch, headphones, second monitor. Close Teams/Skype/all background apps.
- Face visible, quiet room, stable net. Carry **govt photo ID + college ID**; the name must match
  your form exactly (Shivam Gupta).
- Do the **System Check** link the day before. Login within 15 min of your slot.
- Sources: [Infosys assessment guidelines](https://www.scribd.com/document/807976064/Important-Instructions-for-Students),
  proctoring behavior ([shadecoder 2026](https://www.shadecoder.com/blogs/does-hackerrank-detect-cheating-a-candidate-s-guide-in-2025)).

---

## 5. Packages (campus drive vs HWI — for context)
- Your ITM campus drive JD: **SP L3 ₹21L · SP L2 ₹16L · SP L1 ₹10L (+₹1L joining bonus) · DSE ₹6.25L
  (+₹75k bonus)**. Test performance decides the tier.
- HWI public figures run slightly different (SP ~₹9.5L, DSE ~₹6.5L, SE ~₹3.6L) — ballpark, cycle-dependent.
- Takeaway: **more test cases passed on harder questions = higher tier = more money.** Push for the SP band.

---

## 6. ★ Boost your shortlist before the test — InfyTQ certification (FREE)
Clearing the **InfyTQ** certification improves SP shortlisting and looks strong pre-drive. Do it if
time allows: https://www.infytq.onwingspan.com/ . (From PREP; still valid 2026.)

---

## 7. Focused question bank to drill (highest ROI, 2026-tagged)
Greedy (Q2 style) + DP (Q3 style) win the test. Drill these patterns:
- **DP (over-invest here):** 0/1 knapsack, coin change, LCS, **LIS / longest non-decreasing subsequence**,
  edit distance, matrix path DP, partition/subset-sum, DP on strings, split-array-into-k-segments-min-cost.
- **Greedy:** interval scheduling/activity selection, jump game, largest-number-from-array (concatenation),
  **XOR-sum maximization (bit greedy)**, minimize cost/partitions.
- **Graphs:** BFS/DFS, number of islands, rotten oranges, topological sort, Dijkstra, Union-Find.
- **Arrays/Strings:** two-pointer, sliding window (window max), prefix sums, Kadane, anagrams, valid parentheses, matrix rotation.
- **Recursion/backtracking:** subsets, permutations, combination sum, N-Queens.
- **Trees:** traversals, BST ops, LCA, height/diameter. **Heaps:** top-K, merge K lists. **Bit:** single number (XOR), count set bits.
- Practice sources: [PrepInsta SP coding Qs](https://prepinsta.com/infosys-sp-and-dse/specialist-programmer/coding-questions/),
  [karthikreddy-7/Infosys-SP-Coding-Questions](https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions),
  [CCBP Infosys coding](https://www.ccbp.in/blog/articles/infosys-coding-questions),
  [LeetCode Infosys OA discuss](https://leetcode.com/discuss/), Striver SDE Sheet, NeetCode 150.

---

## 8. "Get selected anyhow" — the honest game plan
1. **Test (biggest lever):** 2 weeks of timed practice. Bank Q1 fully, strong partials on Q2/Q3.
   Do **3 full timed mocks (3Q/180 min)** to build stamina — pressure, not difficulty, is what breaks people.
2. **Over-index on DP + Greedy** (that's Q2/Q3). Aditya Verma DP playlist + Striver.
3. **InfyTQ cert** done before the drive (bonus shortlist points).
4. **Interview:** rehearse a crisp self-intro; know NETWORKED & Parakh cold; prepare **GenAI/agent talk**
   (your differentiator); OOP-with-examples + SQL-on-paper + OS/CN basics.
5. **Zero integrity risk:** no tab switches, IDs ready, System Check done — one flag can end it.
6. **HR:** confident "why Infosys," yes to PAN-India relocation + any technology.

---

## 9. UPDATE (11 Jul 2026) — real PYQ patterns + a pattern change to watch
### Real SP/DSE PYQ problem-types (2021-2025, repeat hote hain)
Largest-number-from-array (greedy) · split-array-into-k-segments-min-cost (DP) · choose-at-most-N/2-
elements (DSE) · GET(l,r) range function (SP OA Dec 2024) · remove-duplicates-in-place · XOR-sum
maximization (bit-greedy) · Next Smallest Palindrome · Rotten Oranges / Number of Islands.
→ **Exact 40-problem goldmine + links are now in `05-infosys-QUESTION-BANK.md` (GOLDMINE section).**
Sources: [PrepInsta SP](https://prepinsta.com/infosys-sp-and-dse/specialist-programmer/coding-questions/),
[PrepInsta DSE](https://prepinsta.com/infosys-sp-and-dse/digital-specialist-engineer/coding-questions/),
[GfG SP OA Dec 2024](https://www.geeksforgeeks.org/interview-experiences/infosys-oa-experience-for-specialist-programmer/),
[Scribd 13-PYQ manual 2021-25](https://www.scribd.com/document/956288573/Infosys-SP-DSE-Coding-Problems-Solution-Manual),
GitHub: karthikreddy-7/Infosys-SP-Coding-Questions, itsmeheisenberg/HackWithInfy, Devang-25/HackWithInfy-2022-Solutions.

### ✅ Pattern CONFIRMED (via ITM TAP Cell meeting, Jul 2026) — pure coding
**Confirmed with the TAP Cell in a meeting: the test is 3 CODING questions / 180 min — pure coding,
NO aptitude / NO pseudo-code section for this SP/DSE campus drive.** (Some general 2026 Infosys SP
writeups mention an aptitude/pseudo-code gate for other tracks, but that does NOT apply here.)
→ Full focus on DSA: Arrays/Strings/Hashing (Q1) + Greedy (Q2) + DP (Q3). No time wasted on aptitude.

## Sources (all 2026 unless noted)
- Great Learning — Crack Infosys SP & DSE 2026: https://www.mygreatlearning.com/blog/infosys-sp-dse-interview-guide-2026/
- PrepInsta SP/DSE (pattern, syllabus, coding): https://prepinsta.com/infosys-sp-and-dse/
- First-hand DSE experience (timeline + interview): https://medium.com/@pravallikaseshasai/hackwithinfy-guide-rounds-questions-how-i-landed-the-dse-role-bc4f64db465d
- Infosys HackWithInfy 2026 (AI theme): https://www.infosys.com/careers/hackwithinfy.html
- faceprep Infosys technical questions 2026: https://faceprep.in/article/infosys-technical-interview-questions/
- Core Java @ Infosys 2026: https://medium.com/@sparsh187/core-java-interview-questions-asked-in-infosys-2026-complete-guide-a4f95e287be2
- GeeksforGeeks Infosys SDE sheet: https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/
- Integrity crackdown (2026): https://www.theworkersrights.com/infosys-recruitment-update-hiring-test-delay-explained/
- InfyTQ (free cert): https://www.infytq.onwingspan.com/
