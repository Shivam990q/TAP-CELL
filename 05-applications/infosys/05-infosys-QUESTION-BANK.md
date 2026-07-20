# Infosys DSE/SP — Question Bank (topic-wise, question clarity)

> 🔖 **PROVENANCE:** Tier 1-4 problems = standard **LeetCode-canonical** ([SRC: LC#] SOURCE MAP me),
> statements AI ne Hinglish me **[AI-REWORDED]**. Tier 5 + REAL PYQ INDEX = **[REAL-PYQ]** (Infosys me
> actually reported, source ke saath). Sample I/O + samajh = [AI-EXPLANATION]. Legend: `README.md` → PROVENANCE INDEX.

> ⚠️ **Neeche ki list ek TOPIC-CHECKLIST hai** (quick reference — kaunse problems cover karne). Ye
> intentionally 1-line me hai taaki ek nazar me poora syllabus dikhe.
> **FULL real-exam problem statements (story + Input/Output + constraints + samples + full solution)
> yahan hain:**
> - `06-infosys-SOLUTIONS.md` → 64 full solutions incl. **TIER 5 (13 REAL Infosys PYQ, full statements)**.
> - `09-infosys-MOCK-PAPERS.md` → **5 full timed mock sets (15 problems) + PATTERN-MIXED section (4)** —
>   sab story-wrapped, real-exam style. **Total ~30+ full-statement real problems.**
> Toh: checklist yahan se, aur asli exam-feel practice `09` (timed) + `06` (solutions) se.
>
> `04-infosys-1WEEK-DSE-PLAN.md` follow karte waqt yahan se problems uthao.
> Practice: LeetCode (leetcode.com) + GeeksforGeeks (geeksforgeeks.org/explore, Infosys-tagged).
> Sources: PrepInsta, GfG Infosys SDE sheet, karthikreddy-7/Infosys-SP-Coding-Questions (GitHub).

---

## 🟢 PRIORITY MAP (kya pehle karna hai)
| Priority | Topic | Test me kahan | Time do |
| --- | --- | --- | --- |
| ⭐⭐⭐ | Arrays/Strings/Hashing | Q1 (easy, 20 marks) — **pakka full** | Most |
| ⭐⭐⭐ | Greedy | Q2 (medium, 30 marks) | High |
| ⭐⭐⭐ | DP (basics) | Q3 (hard, 50 marks) — partials | High |
| ⭐⭐ | Two-pointer/Sliding window/Binary search | Q1-Q2 mix | Medium |
| ⭐⭐ | Graphs (BFS/DFS) | Q2-Q3 | Medium |
| ⭐ | Trees/Stack/Heap/Bit/Math | koi bhi | Breadth ke liye |

---

## 1. Arrays & Strings & Hashing ⭐⭐⭐ (Q1 — YE PAKKA KARO)
**Pattern:** frequency map, sorting, single-pass, two-sum style.
- [ ] Two Sum — hashmap
- [ ] Best Time to Buy and Sell Stock — track min
- [ ] Maximum Subarray (Kadane) — running sum
- [ ] Majority Element — Moore's voting
- [ ] Valid Anagram / Group Anagrams — sort/count
- [ ] Valid Palindrome — two pointer
- [ ] Move Zeroes / Remove Duplicates from Sorted Array
- [ ] Merge Sorted Array
- [ ] Reverse String / Reverse Integer
- [ ] First Unique Character (frequency map)

## 2. Two Pointers + Sliding Window + Prefix Sum ⭐⭐
**Pattern:** window expand/shrink, do pointers, prefix[] for range sums.
- [ ] Longest Substring Without Repeating Characters
- [ ] Container With Most Water
- [ ] Subarray Sum Equals K — prefix + hashmap
- [ ] Maximum Average Subarray I — fixed window
- [ ] Minimum Size Subarray Sum — variable window
- [ ] Trapping Rain Water (SP-level, thoda hard)
- [ ] 3Sum

## 3. Binary Search + Searching/Sorting ⭐⭐
**Pattern:** sorted array → O(log n). "Search space" par binary search.
- [ ] Binary Search / Search Insert Position
- [ ] First and Last Position in Sorted Array
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search in Rotated Sorted Array
- [ ] Sqrt(x) / Koko Eating Bananas (binary search on answer)
- [ ] Power(x, n) — fast exponentiation

## 4. Greedy ⭐⭐⭐ (Q2 — 30 marks)
**Pattern:** sort karo → har step locally-best choice. Intervals bahut aate hain.
- [ ] Jump Game / Jump Game II
- [ ] Assign Cookies
- [ ] Merge Intervals
- [ ] Non-overlapping Intervals
- [ ] Minimum Number of Arrows to Burst Balloons
- [ ] Meeting Rooms / Meeting Rooms II
- [ ] Largest Number (concat strings for max number)
- [ ] Gas Station
- [ ] Candy (hard)
- [ ] XOR-Sum maximization (bit-greedy — Infosys me aaya hai)

## 5. Dynamic Programming ⭐⭐⭐ (Q3 — 50 marks; over-invest)
**Pattern:** recursion → memoize → tabulate. "Choose / don't choose."
**Resource: Aditya Verma DP playlist (YouTube) — sabse best.**
- [ ] Climbing Stairs (intro)
- [ ] House Robber / House Robber II
- [ ] Coin Change (min coins) + Coin Change II (ways)
- [ ] 0/1 Knapsack (GfG) ← core
- [ ] Subset Sum / Partition Equal Subset Sum
- [ ] Longest Common Subsequence (LCS) ← core
- [ ] Longest Increasing Subsequence (LIS) + non-decreasing variation (interview me aaya)
- [ ] Edit Distance
- [ ] Unique Paths / Minimum Path Sum (matrix DP)
- [ ] Split array into k segments, minimum cost (PrepInsta SP)

## 6. Graphs ⭐⭐ (Q2-Q3)
**Pattern:** BFS (shortest/level), DFS (connected), topo sort, DSU.
- [ ] Number of Islands (BFS/DFS)
- [ ] Rotting Oranges (BFS — Infosys favourite)
- [ ] Flood Fill
- [ ] Course Schedule (topological sort)
- [ ] Clone Graph
- [ ] Dijkstra shortest path (GfG)
- [ ] Number of Provinces / Union-Find (DSU)

## 7. Trees ⭐ (interview me zyada)
- [ ] Maximum Depth of Binary Tree
- [ ] Binary Tree Level Order Traversal (BFS)
- [ ] Inorder/Preorder/Postorder Traversal
- [ ] Diameter of Binary Tree
- [ ] Lowest Common Ancestor (LCA)
- [ ] Validate BST

## 8. Stacks & Queues ⭐
- [ ] Valid Parentheses
- [ ] Next Greater Element (monotonic stack)
- [ ] Min Stack
- [ ] Sliding Window Maximum (deque)
- [ ] Largest Rectangle in Histogram (hard)

## 9. Heaps / Priority Queue ⭐
- [ ] Kth Largest Element
- [ ] Top K Frequent Elements
- [ ] Merge K Sorted Lists

## 10. Bit Manipulation + Math ⭐
- [ ] Single Number (XOR)
- [ ] Number of 1 Bits / Counting Bits
- [ ] Power of Two
- [ ] GCD / LCM (Euclid)
- [ ] Sieve of Eratosthenes (primes)
- [ ] Next Smallest Palindrome (Infosys favourite)
- [ ] Swap two numbers without temp variable

---

## 🎤 INTERVIEW — CS Fundamentals (DSE interview me poochte hain)
> Ye topic-list hai. **FULL crisp ANSWERS `08-infosys-INTERVIEW-CS.md` me hain** (OOP code, SQL queries,
> OS/CN/GenAI sab likhe hue). Yahan sirf checklist ki kya-kya cover karna hai.

### OOP (har interview me)
- 4 pillars (Encapsulation, Abstraction, Inheritance, Polymorphism) — **real example** ke saath
- Overloading vs Overriding (code likho); compile-time vs runtime polymorphism
- Abstract class vs Interface; Java multiple inheritance (classes NO, interface YES)

### DBMS / SQL
- Normalization 1NF→2NF→3NF→BCNF (example table)
- Primary vs Foreign vs Candidate key; Index (read fast, write slow)
- JOINs (inner/left/right/full); GROUP BY vs WHERE vs HAVING
- ACID; DELETE vs TRUNCATE vs DROP
- **Likhne aate hain:** 2nd/Nth highest salary, duplicate rows, window functions

### OS
- Process vs Thread; context switching; scheduling (FCFS/SJF/RR)
- Deadlock (4 conditions + prevention); mutex vs semaphore; race condition
- Paging vs segmentation; virtual memory; thrashing

### Computer Networks
- OSI vs TCP/IP layers; TCP vs UDP; 3-way handshake
- HTTP/HTTPS; DNS; "URL type karne pe kya hota hai"; status codes

### ★ ML / GenAI basics (2026 NEW — tera differentiator)
- ML kya hai; supervised vs unsupervised
- LLM / Generative AI kya hai; AI agent / RAG high-level
- **Apne projects se connect karo:** ROSE (JARVIS-like), MCP, CrewAI, Better Than Claude Skills

---

## 🧠 HR / Behavioral (ready rakho)
- Self-intro (30-45 sec): CSE final-year @ ITM 2027, strong DSA + full-stack, shipped NETWORKED
  & Parakh ERP, President IDC, Hacksagon Top Performer, building ROSE (Gen-AI agent)
- "Why Infosys?" — premium tech role, enterprise-scale + latest tech (cloud, GenAI), learning + PAN-India
- Relocate anywhere? **YES.** Any technology? **YES.**
- Projects deep-dive: NETWORKED + Parakh (architecture, DB, challenges, tradeoffs) — cold yaad rakho

---
> Rule: ye list ratna nahi hai. Har problem **samajh ke** solve karo, pattern pehchano.
> DSE ke liye Topics 1-5 kaafi hain. SP ke liye 6-10 bhi add karo.


---
---

# 💰 GOLDMINE (market research, 11 Jul 2026) — "itna kar liya to round anyhow nikal jaayega"

> Ye section fresh 2026 web research se bana hai. Har item ke saath: source/link, kyun important,
> difficulty, expected time. Priority order me — pehle DSE-guaranteed, phir SP-extra.
> Rule: ratna nahi, samajhna hai. Testing/experiment ki zarurat nahi — ye list hi kaafi hai.

## ⚡ Sabse pehle padhne wali baat — actual Infosys SP/DSE PYQ patterns (real, repeat hote hain)
Ye exact problem-types Infosys SP/DSE tests (2021-2025) me baar-baar aaye hain (sources neeche):
| Problem-type | Topic | Kahan aaya | LeetCode/GfG equivalent (practice yahan) |
| --- | --- | --- | --- |
| Largest number from array of strings (concat for max) | Greedy | SP repeat | LeetCode 179 "Largest Number" |
| Split array into k consecutive segments, min cost | DP | SP (PrepInsta) | LeetCode 410 "Split Array Largest Sum" (variation) |
| Choose at most N/2 elements from array (max something) | Greedy/DP | DSE (PrepInsta) | Greedy + sort pattern |
| GET(l,r) range function on array | Prefix/segment | SP OA (GfG, Dec 2024) | Range-sum / prefix problems |
| Remove duplicates from sorted array in-place O(1) | Arrays | SP/DSE sheet | LeetCode 26 |
| XOR-Sum maximization (bit greedy) | Greedy + Bit | SP (Scribd manual) | LeetCode "Maximum XOR" patterns |
| Next Smallest Palindrome | Math/String | Infosys classic | GfG "Next Smallest Palindrome" |
| Rotten Oranges / Number of Islands | Graph BFS/DFS | very frequent | LeetCode 994 / 200 |
> Sources: [PrepInsta SP coding](https://prepinsta.com/infosys-sp-and-dse/specialist-programmer/coding-questions/),
> [PrepInsta DSE coding](https://prepinsta.com/infosys-sp-and-dse/digital-specialist-engineer/coding-questions/),
> [GfG Infosys SP OA experience (Dec 2024)](https://www.geeksforgeeks.org/interview-experiences/infosys-oa-experience-for-specialist-programmer/),
> [Scribd — Infosys SP/DSE Solution Manual (13 PYQ 2021-25)](https://www.scribd.com/document/956288573/Infosys-SP-DSE-Coding-Problems-Solution-Manual).

## ✅ PATTERN CONFIRMED (TAP Cell meeting) — PURE CODING
**TAP Cell meeting me confirm ho gaya: 3 CODING questions / 180 min — pure coding hai. NO aptitude,
NO pseudo-code.** Toh 100% focus DSA pe: Arrays/Strings/Hashing (Q1) + Greedy (Q2) + DP (Q3).
Aptitude/pseudo-code pe time WASTE nahi karna.

## 📚 EXACT RESOURCES (minimum set — sirf ye, aur kuch nahi chahiye)
| # | Resource | Kiske liye | Link |
| --- | --- | --- | --- |
| 1 | **Striver A2Z / SDE Sheet** (ek chuno, poora karo) | Complete DSA — DSE+SP dono | https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/ |
| 2 | **Aditya Verma — DP playlist** (YouTube) | Q3 (DP, 50 marks) — best intuition | https://www.youtube.com/@AdityaVermaTheProgrammingLord |
| 3 | **Gate Smashers** (YouTube) | Interview CS fundamentals (DBMS/OS/CN) | https://www.youtube.com/@GateSmashers |
| 4 | **NeetCode 150** (alt to Striver) | Pattern-based practice | https://neetcode.io/practice |
| 5 | **InfyTQ (FREE cert)** | SP shortlist boost — DO IT | https://www.infytq.onwingspan.com/ |

### 💎 Infosys-specific PYQ GOLDMINE repos (exact style practice)
- [ ] **karthikreddy-7/Infosys-SP-Coding-Questions** — https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions
- [ ] **itsmeheisenberg/HackWithInfy** (sample paper + Java solutions) — https://github.com/itsmeheisenberg/HackWithInfy
- [ ] **Devang-25/HackWithInfy-2022-Solutions** (+ LeetCode discuss Q-list) — https://github.com/Devang-25/HackWithInfy-2022-Solutions
- [ ] **Adit-Mugdha-das/LeetCode-Top-50-DP-Solutions** — https://github.com/Adit-Mugdha-das/LeetCode-Top-50-DP-Solutions
- [ ] **PrepInsta SP/DSE coding** — https://prepinsta.com/infosys-sp-and-dse/coding-questions/
- [ ] **GfG Infosys SDE Sheet** — https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/

## ✅ THE 40-PROBLEM GOLDMINE (yahi complete karo — DSE anyhow, SP strong chance)
> Har problem LeetCode pe naam se search karo. Difficulty (E/M/H) + time diya hai.

### TIER 1 — DSE guaranteed (Q1 full + partials). Ye 20 PAKKA karo:
> Neeche har problem **FULL real-Infosys-style statement** me hai (story + Input/Output + Constraints +
> Sample). Solution ka full code: `06-infosys-SOLUTIONS.md` me diye number pe. Checkbox tick karte ja.

**T1.1 — "Do Dost ka Budget" [Easy · 10 min] [ ]**
Ek shop me N items hain, prices `arr[]` me. Do alag items dhoondo jinki price ka sum bilkul `target`
ke barabar ho. Un dono items ke **index** (0-based) print karo. (Exactly ek answer exist karta.)
- Input: L1: `N target` · L2: N integers.
- Output: do indices (space-separated).
- Constraints: 2 ≤ N ≤ 10^5 · -10^9 ≤ arr[i], target ≤ 10^9.
- Sample In: `4 9` / `2 7 11 15` → Out: `0 1` (2+7=9). → **Solution: `06` #1**

**T1.2 — "Stock Se Profit" [Easy · 10 min] [ ]**
Ek stock ka N-din ka price `arr[]` hai. Ek din khareedo, baad ke kisi din becho. **Max profit** batao
(profit na ho to 0).
- Input: L1: N · L2: N prices. · Output: max profit.
- Constraints: 1 ≤ N ≤ 10^5.
- Sample In: `6` / `7 1 5 3 6 4` → Out: `5` (khareedo 1, becho 6). → **Solution: `06` #2**

**T1.3 — "Sabse Faydemand Streak" [Easy · 15 min] [ ]**
N integers (positive/negative) ki array. Aisa **contiguous subarray** dhoondo jiska sum **maximum** ho.
Wo max sum batao.
- Input: L1: N · L2: N integers. · Output: max subarray sum.
- Constraints: 1 ≤ N ≤ 10^5 · -10^4 ≤ arr[i] ≤ 10^4.
- Sample In: `9` / `-2 1 -3 4 -1 2 1 -5 4` → Out: `6` ([4,-1,2,1]). → **Solution: `06` #3 (Kadane)**

**T1.4 — "Popular Product" [Easy · 10 min] [ ]**
N orders (product IDs). Jo product **N/2 se zyada** baar aaya (guaranteed exist), uska ID batao.
- Input: L1: N · L2: N IDs. · Output: majority ID.
- Sample In: `7` / `3 3 4 2 3 3 3` → Out: `3`. → **Solution: `06` #4 (Moore's voting)**

**T1.5 — "Anagram Check" [Easy · 10 min] [ ]**
Do strings s, t. Kya t, s ke letters ka rearrangement (anagram) hai? `YES`/`NO`.
- Input: L1: s · L2: t. · Constraints: 1 ≤ len ≤ 10^5.
- Sample In: `listen` / `silent` → Out: `YES`. → **Solution: `06` #5**

**T1.6 — "Sentence Palindrome" [Easy · 10 min] [ ]**
Ek string; sirf letters/digits count (symbols/space/case ignore). Palindrome hai? `YES`/`NO`.
- Sample In: `A man, a plan, a canal: Panama` → Out: `YES`. → **Solution: `06` #6**

**T1.7 — "Duplicate Hatao" [Easy · 10 min] [ ]**
Ek **sorted** array me se duplicates in-place hatao; nayi length k batao (pehle k elements unique).
- Input: L1: N · L2: N sorted integers. · Output: k (unique count).
- Sample In: `5` / `1 1 2 2 3` → Out: `3`. → **Solution: `06` #7**

**T1.8 — "Zeroes Peeche" [Easy · 10 min] [ ]**
Array me saare 0 end me le jao, non-zero ka order same rahe (in-place).
- Sample In: `5` / `0 1 0 3 12` → Out: `1 3 12 0 0`. → **Solution: `06` #8**

**T1.9 — "Do Sorted List Merge" [Easy · 15 min] [ ]**
Do sorted arrays ko ek sorted array me merge karo.
- Input: L1: `m n` · L2: m integers · L3: n integers. · Output: merged sorted.
- Sample In: `3 3`/`1 2 3`/`2 5 6` → Out: `1 2 2 3 5 6`. → **Solution: `06` #9**

**T1.10 — "Number Dhoondo" [Easy · 10 min] [ ]**
Sorted array me `target` ka index batao (na mile → -1). O(log N) chahiye.
- Sample In: `5 9`/`1 3 5 7 9` → Out: `4`. → **Solution: `06` #10 (Binary Search)**

**T1.11 — "Insert Position" [Easy · 10 min] [ ]**
Sorted array me target mile to uska index; na mile to wo index jaha insert karna chahiye.
- Sample In: `4 5`/`1 3 5 6` → Out: `2`. → **Solution: `06` #11**

**T1.12 — "Bina Repeat Longest" [Medium · 25 min] [ ]**
String me sabse lambi substring jisme koi character repeat na ho — uski **length** batao.
- Sample In: `abcabcbb` → Out: `3` ("abc"). → **Solution: `06` #12 (Sliding Window)**

**T1.13 — "Sum = K Subarrays" [Medium · 25 min] [ ]**
Integer array + K. Kitne **contiguous subarrays** hain jinka sum exactly K hai?
- Sample In: `3 2`/`1 1 1` → Out: `2`. → **Solution: `06` #13 (Prefix+Hash)**

**T1.14 — "Anagram Groups" [Medium · 20 min] [ ]**
N words; anagram-wale words ko ek group me daalo. Kitne groups bane?
- Sample In: `6`/`eat tea tan ate nat bat` → Out: `3`. → **Solution: `06` #14**

**T1.15 — "Seedhiyan (Stairs)" [Easy · 10 min] [ ]**
N seedhiyan; ek baar me 1 ya 2 step. Top tak jaane ke **kitne distinct tareeke**?
- Sample In: `4` → Out: `5`. → **Solution: `06` #15 (DP intro)**

**T1.16 — "Chor aur Ghar (House Robber)" [Medium · 20 min] [ ]**
Ghar line me, har ghar me paisa `arr[]`. **Adjacent ghar loot nahi sakte** (alarm baj jaayega). Max kitna loot sakte?
- Sample In: `4`/`2 7 9 3` → Out: `11` (2+9). → **Solution: `06` #16 (DP)**

**T1.17 — "Cashier Min Coins" [Medium · 30 min] [ ]**
Coins denominations `coins[]` (unlimited). Amount X banane ke **minimum coins** (na bane → -1).
- Sample In: `3`/`1 2 5`/`11` → Out: `3` (5+5+1). → **Solution: `06` #17 (DP)**

**T1.18 — "Jump Ho Payega?" [Medium · 20 min] [ ]**
Array, arr[i] = us index se max kitne aage jump kar sakte. Index 0 se **last index** tak pahunch sakte? `true/false`.
- Sample In: `5`/`2 3 1 1 4` → Out: `true`. → **Solution: `06` #18 (Greedy)**

**T1.19 — "Overlapping Intervals Merge" [Medium · 20 min] [ ]**
N intervals `[start,end]`. Overlapping wale merge karke non-overlapping list do.
- Sample In: `4`/`1 3`/`2 6`/`8 10`/`15 18` → Out: `1 6 / 8 10 / 15 18`. → **Solution: `06` #19**

**T1.20 — "Brackets Balanced?" [Easy · 10 min] [ ]**
String of `(){}[]`. Balanced hai? `YES`/`NO`.
- Sample In: `{[()]}` → Out: `YES`. → **Solution: `06` #20 (Stack)**

> ⬆️ Ye 20 = **DSE lock**. Har ek ka full code `06-SOLUTIONS.md` me (# diya hai). Aur Tier 2-3 (neeche
> checklist) + real PYQ (`06` Tier5) + timed mocks (`09`) = SP zone.

### TIER 1 quick-checklist (naam se — jab yaad ho jaye):
- [ ] Two Sum · Best Time Buy/Sell · Max Subarray(Kadane) · Majority · Valid Anagram · Valid Palindrome
- [ ] Remove Duplicates · Move Zeroes · Merge Sorted · Binary Search · Search Insert
- [ ] Longest Substring No-Repeat · Subarray Sum=K · Group Anagrams · Climbing Stairs
- [ ] House Robber · Coin Change · Jump Game · Merge Intervals · Valid Parentheses

### TIER 2 — SP push (Q2 greedy + Q3 DP fully). Ye 12 (full statements):

**T2.1 — "Sabse Bada Number" [Medium · 25 min] ★ Infosys PYQ [ ]**
N non-negative integers. Inhe aise arrange karke jodo ki **sabse bada number** bane. Wo number (string) print karo.
- Input: L1: N · L2: N integers. · Sample In: `3`/`3 30 34` → Out: `34330`. → **Solution: `06` #21 (Greedy comparator)**

**T2.2 — "Max Non-Overlapping Meetings" [Medium · 25 min] [ ]**
N intervals `[start,end]`. Minimum kitne intervals **remove** karo taaki baaki koi overlap na karein?
- Input: L1: N · N lines: start end. · Sample In: `4`/`1 2`/`2 3`/`3 4`/`1 3` → Out: `1`. → **Solution: `06` #22 (Greedy, end pe sort)**

**T2.3 — "Petrol Pump Circle" [Medium · 25 min] [ ]**
Circular route me N petrol pumps; pump i pe `gas[i]` petrol, agle tak jaane me `cost[i]`. Kis pump se
start karo ki poora circle ghoom sako? Starting index (nahi to -1).
- Sample In: gas=`1 2 3 4 5`, cost=`3 4 5 1 2` → Out: `3`. → **Solution: `06` #23 (Greedy)**

**T2.4 — "Chor ka Bag (0/1 Knapsack)" [Medium · 30 min] ★ [ ]**
N items, har item weight `w[i]` value `v[i]`. Bag capacity W. Har item **poora lo ya chhodo** (fraction nahi).
Max total value?
- Input: L1: `N W` · N lines: w v. · Sample In: `3 4`/`1 1`/`3 4`/`4 5` → Out: `5`. → **Solution: `06` #24 (DP)**

**T2.5 — "Do Barabar Hisse" [Medium · 30 min] [ ]**
Array ko do subsets me baant sakte ho jinke sum barabar ho? `YES`/`NO`.
- Sample In: `4`/`1 5 11 5` → Out: `YES` (11 = 1+5+5). → **Solution: `06` #25 (Subset-sum DP)**

**T2.6 — "Common Subsequence" [Medium · 30 min] ★ [ ]**
Do strings. Sabse lambi **subsequence** (order same, beech ke chars skip ok) jo dono me common ho — length batao.
- Sample In: `abcde`/`ace` → Out: `3` ("ace"). → **Solution: `06` #26 (2D DP)**

**T2.7 — "Badhta Order (LIS)" [Medium · 30 min] ★ [ ]**
Array me sabse lambi **increasing subsequence** ki length (order same, beech skip ok).
- Sample In: `6`/`10 9 2 5 3 7 101 18` → Out: `4` ([2,3,7,101]). → **Solution: `06` #27 (DP)**

**T2.8 — "Word Correct karo (Edit Distance)" [Hard · 35 min] [ ]**
Word A ko word B banana hai — insert/delete/replace ek char = 1 op. Minimum ops?
- Sample In: `horse`/`ros` → Out: `3`. → **Solution: `06` #28 (2D DP)**

**T2.9 — "Grid me Min Cost Path" [Medium · 25 min] [ ]**
M×N grid, har cell me cost. Top-left se bottom-right tak jao (sirf right/down). Minimum total cost?
- Sample In: grid `[[1,3,1],[1,5,1],[4,2,1]]` → Out: `7`. → **Solution: `06` #29 (Matrix DP)**

**T2.10 — "Kitne Islands" [Medium · 25 min] ★ frequent [ ]**
Grid of '1'(land)/'0'(water). Kitne alag islands (connected land — up/down/left/right)?
- Sample In: `[[1,1,0],[0,1,0],[0,0,1]]` → Out: `2`. → **Solution: `06` #30 (DFS/BFS)**

**T2.11 — "Sade Oranges" [Medium · 25 min] ★ Infosys favourite [ ]**
Grid: 0 empty, 1 fresh orange, 2 rotten. Har minute rotten apne adjacent fresh ko rotten kar deta.
Kitne minute me saare rotten? (Nahi ho sakte → -1.)
- Sample In: `[[2,1,1],[1,1,0],[0,1,1]]` → Out: `4`. → **Solution: `06` #31 (BFS)**

**T2.12 — "Course Dependencies" [Medium · 30 min] [ ]**
N courses; kuch ke prerequisites hain (`[a,b]` = a ke liye b pehle). Saare courses complete ho sakte? `true/false`.
- Sample In: `2`/`[[1,0]]` → Out: `true`. → **Solution: `06` #32 (Topological sort)**

### TIER 3 — SP L2/L3 edge (hard). Time bache to ye 8 (full statements):

**T3.1 — "Baarish ka Paani" [Hard · 35 min] [ ]**
Buildings ki heights `arr[]` (bar chart). Baarish ke baad bars ke beech **kitna paani** ruk sakta hai?
- Sample In: `[0,1,0,2,1,0,1,3,2,1,2,1]` → Out: `6`. → **Solution: `06` #33 (Two-pointer)**

**T3.2 — "Agla Bada (Next Greater)" [Medium · 25 min] [ ]**
Array me har element ke liye **uske daaye pehla bada element** batao (nahi to -1).
- Sample In: `4`/`4 5 2 10` → Out: `5 10 10 -1`. → **Solution: `06` #34 (Monotonic Stack)**

**T3.3 — "Window ka Max" [Hard · 30 min] [ ]**
Array + window size K. Har K-size window ka **maximum** print karo.
- Sample In: `arr=[1,3,-1,-3,5,3,6,7], k=3` → Out: `3 3 5 5 6 7`. → **Solution: `06` #35 (Monotonic Deque)**

**T3.4 — "K-th Sabse Bada" [Medium · 20 min] [ ]**
Array me **K-th largest** element (sorted order me Kth bada). Sort kiye bina efficiently.
- Sample In: `arr=[3,2,1,5,6,4], k=2` → Out: `5`. → **Solution: `06` #36 (Min-Heap size K)**

**T3.5 — "Top K Frequent" [Medium · 25 min] [ ]**
Array me jo **K sabse zyada baar** aaye, wo elements batao.
- Sample In: `arr=[1,1,1,2,2,3], k=2` → Out: `1 2`. → **Solution: `06` #37 (Count + Heap)**

**T3.6 — "Sabse Sasta Rasta" [Hard · 35 min] [ ]**
Weighted graph (nodes + edges with cost). Ek source se har node tak **minimum cost** batao.
- Input: n, edges `[u,v,w]`, src. · Output: dist array. → **Solution: `06` #38 (Dijkstra, min-heap)**

**T3.7 — "Agla Chhota Palindrome" [Medium · 30 min] ★ Infosys classic [ ]**
Ek number (string). Usse **strictly bada** sabse chhota **palindrome** number batao.
- Sample In: `1234` → Out: `1331`. Edge: `999` → `1001`. → **Solution: `06` #39 (Mirror + carry)**

**T3.8 — "Akela Number + Max XOR" [Medium · 25 min] ★ Infosys bit-greedy [ ]**
(a) Array me har element 2 baar aaya sivaay ek ke — wo akela batao.
(b) Array me do elements ka **maximum XOR** batao.
- Sample In (a): `[4,1,2,1,2]` → `4`. (b): `[3,10,5,25,2,8]` → `28`. → **Solution: `06` #40 (XOR / bit-greedy)**

> **Bas yahi 40. Tier 1 (20) = DSE lock. Tier 1+2 (32) = SP real chance. Poora 40 = SP L2/L3 tak.**
> Ab **saare 40 FULL-statement** hain (story + I/O + sample). Full code `06-infosys-SOLUTIONS.md` me
> (# diya). + REAL PYQ (`06` Tier5, 13) + timed mocks (`09`, 5 sets + mixed) = complete.

---

# 🎤 INTERVIEW — project-connected REAL answers (tere projects se)
> Rat-ke nahi, apne experience se bolo. Ye ready-made hooks hain.

### Self-intro (30-45 sec, ye bolo)
"Main Shivam Gupta, final-year CSE @ ITM University Gwalior, 2027 batch. Strong in DSA aur full-stack
(React + Django). Maine live products ship kiye — NETWORKED (client consultancy platform) aur Parakh
ERP/IQAC system as a full-stack intern. President hoon ITM Developers Club ka, aur Hacksagon 2025 me
Top Performer raha. Abhi ROSE bana raha hoon — ek JARVIS-jaisa Gen-AI agent. Mujhe hard problems solve
karna aur naye stacks seekhna pasand hai."

### Project deep-dive hooks (poochhenge to ye connect karo)
- **NETWORKED** → full-stack architecture, REST APIs, DB schema, deployment (Nginx/Gunicorn), auth.
  Question aaye "biggest challenge?" → scaling/deployment ya auth flow bolo.
- **Parakh ERP (ITM internship)** → Django REST + React, real users, IQAC data — DB design,
  normalization real example yahan se do. "What would you improve?" → indexing/query optimization.
- **ROSE / MCP / CrewAI** → ★ 2026 GenAI angle. "AI agent kya hai?" → RAG, tools, MCP protocol,
  multi-agent orchestration (CrewAI). Ye tera differentiator hai — HWI 2026 AI-themed hai.
- **Better Than Claude Skills** → 16+ LLM skills, OSS — prompt engineering + system design baat.

### CS fundamentals — likely questions (FULL answers `08-infosys-INTERVIEW-CS.md` me)
- OOP: 4 pillars with example, overloading vs overriding (code), abstract class vs interface
- DBMS: normalization (Parakh ERP se example), joins, ACID, 2nd highest salary query, find duplicates
- OS: process vs thread, deadlock 4 conditions, scheduling, paging vs segmentation
- CN: OSI vs TCP/IP, TCP vs UDP, 3-way handshake, "URL type karne pe kya hota hai", DNS
- SQL on paper: `SELECT ... GROUP BY ... HAVING`, window functions, DDL/DML/DCL/DQL
- ML/GenAI basics: supervised vs unsupervised, what is LLM, RAG, AI agent — ROSE se connect

### HR (2-3 line answers)
- "Why Infosys?" → premium tech role, enterprise-scale + latest tech (cloud, GenAI), learning culture, PAN-India.
- Relocate anywhere? **YES.** Any technology? **YES.** Strengths → problem-solving, fast learner, shipping products.


---
---

# 📜 REAL INFOSYS PYQ INDEX (actual reported questions — categorized)
> Ye actually Infosys SP/DSE / HackWithInfy me aaye (PrepInsta, GfG OA 2024-25, Scribd PYQ, HWI 2026).
> Har ek ka **full statement + solution** `06-infosys-SOLUTIONS.md` **TIER 5** me hai, ya
> `09-infosys-MOCK-PAPERS.md` me. Ye list = "kya real me aata hai" ka proof + practice map.

## By topic (real PYQ → kahan solved)
| Real Infosys PYQ | Topic / pattern | Role | Solution |
| --- | --- | --- | --- |
| Split array into K segments, min cost | Partition DP | SP | `06` TIER5 R1 |
| Painter's Partition / Drying Walls | Binary search on answer | SP | `06` TIER5 R2 |
| Aggressive Cows (max-min distance) | Binary search on answer | SP | `06` TIER5 R3 |
| Job Sequencing with Deadlines | Greedy | SP/DSE | `06` TIER5 R4 |
| Prime pairs / count primes | Sieve (number theory) | DSE | `06` TIER5 R5 |
| Distinct elements in every window K | Sliding window + hash | DSE | `06` TIER5 R6 |
| Subset Sum (boolean) | Knapsack DP | SP/DSE | `06` TIER5 R7 |
| Khaled — at most N/2, max sum | Greedy (sort top-K) | DSE | `06` TIER5 R8 |
| Largest Number (concat strings) | Greedy comparator | SP | `06` #21 |
| Next Smallest Palindrome | Math/String | SP/DSE | `06` #39 |
| Max XOR of two numbers | Bit greedy | SP | `06` #40 |
| Spiral Matrix | Matrix traversal | SP (HWI'26) | `09` PYQ 3 |
| Rotten Oranges / Number of Islands | Graph BFS/DFS | SP/DSE | `06` #30,#31 |
| Coin Change (min notes) | Unbounded knapsack DP | SP/DSE | `06` #17 |
| Hungry Fish (min moves) | Greedy + sort | SP | `06` TIER5 approach |
| GET(l,r) max pairs | Prefix + hashing | SP | `06` TIER5 approach |
| Guest serving / next greater | Monotonic stack | SP | `06` #34 |
| Longest run / binary string flips | Single pass | DSE | `06` TIER5 approach |

## Full timed practice papers
- `09-infosys-MOCK-PAPERS.md` → **2 full mock sets (3Q/180min)** + real PYQ bank, Infosys story-style.

> Honest note: exact same question aana guarantee nahi (koi bhi guarantee nahi de sakta). Par ye
> **real reported problems + patterns** hain — inhe solve kiya to test **familiar** lagega, surprise nahi.
> Anyhow selection ka formula wahi: **Q1 full + Q2/Q3 partial = DSE lock; 2 full = SP.**


---
---
# 🔖 SOURCE / REFERENCE MAP — har question ka EXACT origin (verifiable)
> Har problem kahan se hai + kahan practice/verify karo. **LeetCode (LC) number** diya hai — leetcode.com
> pe wo number/naam search karo, wahi canonical problem milega. Infosys-specific PYQ ke original source
> bhi diye. Standard DSA problems ka "origin" = LeetCode (industry-standard canonical set).

## TIER 1 (DSE-lock 20) — practice link
| # | Problem | Exact source (search yahan) |
| --- | --- | --- |
| T1.1 | Two Sum | LeetCode 1 · GfG "Two Sum" |
| T1.2 | Best Time to Buy & Sell Stock | LeetCode 121 |
| T1.3 | Max Subarray (Kadane) | LeetCode 53 · GfG "Kadane's Algorithm" |
| T1.4 | Majority Element | LeetCode 169 · GfG "Majority Element" (Moore's) |
| T1.5 | Valid Anagram | LeetCode 242 |
| T1.6 | Valid Palindrome | LeetCode 125 |
| T1.7 | Remove Duplicates from Sorted Array | LeetCode 26 (★ Infosys SP/DSE sheet) |
| T1.8 | Move Zeroes | LeetCode 283 |
| T1.9 | Merge Sorted Array | LeetCode 88 |
| T1.10 | Binary Search | LeetCode 704 |
| T1.11 | Search Insert Position | LeetCode 35 |
| T1.12 | Longest Substring Without Repeating | LeetCode 3 |
| T1.13 | Subarray Sum Equals K | LeetCode 560 |
| T1.14 | Group Anagrams | LeetCode 49 |
| T1.15 | Climbing Stairs | LeetCode 70 |
| T1.16 | House Robber | LeetCode 198 |
| T1.17 | Coin Change | LeetCode 322 |
| T1.18 | Jump Game | LeetCode 55 |
| T1.19 | Merge Intervals | LeetCode 56 |
| T1.20 | Valid Parentheses | LeetCode 20 |

## TIER 2 (SP-push 12)
| # | Problem | Exact source |
| --- | --- | --- |
| T2.1 | Largest Number | LeetCode 179 (★ Infosys SP PYQ — karthikreddy repo) |
| T2.2 | Non-overlapping Intervals | LeetCode 435 |
| T2.3 | Gas Station | LeetCode 134 |
| T2.4 | 0/1 Knapsack | GfG "0-1 Knapsack Problem" (★ core) |
| T2.5 | Partition Equal Subset Sum | LeetCode 416 |
| T2.6 | Longest Common Subsequence | LeetCode 1143 |
| T2.7 | Longest Increasing Subsequence | LeetCode 300 |
| T2.8 | Edit Distance | LeetCode 72 |
| T2.9 | Min Path Sum / Unique Paths | LeetCode 64 / 62 |
| T2.10 | Number of Islands | LeetCode 200 (★ Infosys frequent) |
| T2.11 | Rotting Oranges | LeetCode 994 (★ Infosys favourite) |
| T2.12 | Course Schedule | LeetCode 207 |

## TIER 3 (SP L2/L3 edge 8)
| # | Problem | Exact source |
| --- | --- | --- |
| T3.1 | Trapping Rain Water | LeetCode 42 |
| T3.2 | Next Greater Element | LeetCode 496 · GfG "Next Greater Element" |
| T3.3 | Sliding Window Maximum | LeetCode 239 |
| T3.4 | Kth Largest Element | LeetCode 215 |
| T3.5 | Top K Frequent Elements | LeetCode 347 |
| T3.6 | Dijkstra Shortest Path | GfG "Dijkstra's Algorithm" · LeetCode 743 |
| T3.7 | Next Smallest Palindrome | GfG "Next Smallest Palindrome" (★ Infosys classic) |
| T3.8 | Single Number / Maximum XOR | LeetCode 136 / 421 (★ Infosys bit-greedy) |

## TIER 4 (interview DSA — in `06` #41-51)
| # | Problem | Source |
| --- | --- | --- |
| 41 | Subsets | LeetCode 78 |
| 42 | Permutations | LeetCode 46 |
| 43 | Combination Sum | LeetCode 39 |
| 44 | Max Depth of Binary Tree | LeetCode 104 |
| 45 | Diameter of Binary Tree | LeetCode 543 |
| 46 | Lowest Common Ancestor | LeetCode 236 |
| 47 | Validate BST | LeetCode 98 |
| 48 | Level Order Traversal | LeetCode 102 |
| 49 | Reverse Linked List | LeetCode 206 |
| 50 | Detect Cycle (Linked List) | LeetCode 141 |
| 51 | Merge Two Sorted Lists | LeetCode 21 |

## TIER 5 (REAL Infosys PYQ — in `06` R1-R13) — original sources
| # | Problem | Real source (reported) |
| --- | --- | --- |
| R1 | Split array into K segments (min cost) | PrepInsta Infosys SP coding · LC 410 (variant) |
| R2 | Painter's Partition / Drying Walls | Scribd Infosys SP PYQ · GfG "Painter's Partition" |
| R3 | Aggressive Cows (max-min dist) | GfG · SPOJ AGGRCOW (Infosys-style BS-on-answer) |
| R4 | Job Sequencing with Deadlines | GfG "Job Sequencing Problem" |
| R5 | Prime Pairs / Sieve | Scribd Infosys SP PYQ ("prime pairs") |
| R6 | Distinct in every window K | GfG "Count distinct elements in every window" |
| R7 | Subset Sum (boolean) | karthikreddy-7/Infosys-SP-Coding-Questions (GitHub) · GfG |
| R8 | Khaled — at most N/2 max sum | PrepInsta Infosys DSE coding questions |
| R9 | Hungry Fish (min moves) | GfG Infosys SP interview experience |
| R10 | GET(l,r) max pairs | GfG Infosys SP OA experience (Dec 2024) |
| R11 | Guest Serving / Next Greater | Scribd Infosys SP PYQ · LC 496 |
| R12 | Spiral Matrix | HackWithInfy 2026 (LeetCode discuss) · LC 54 |
| R13 | Longest run / Max consecutive ones (K flips) | LC 485 / 1004 (binary-string PYQ) |
| R14 | Task scheduling (profit − delay×step), maximize | **HackWithInfy 2026 Round 2** (LeetCode discuss, May 2026) — fresh PYQ |

## TIER 6 (audit-added high-frequency — full code in `06` #52-55)
| # | Problem | Exact source |
| --- | --- | --- |
| 52 | 3Sum | LeetCode 15 |
| 53 | Search in Rotated Sorted Array | LeetCode 33 |
| 54 | Largest Rectangle in Histogram | LeetCode 84 |
| 55 | Number of Provinces (Union-Find / DSU) | LeetCode 547 · GfG "Union-Find / Disjoint Set" |

## MOCK PAPERS (`09`) sources
- SET 1-5 problems: story-wrapped versions of real patterns; each problem me "Mirrors: [source]" note hai
  (Wipro sock-pairs, Accenture feed-rats, LC Burst Balloons 312, LC Meeting Rooms II 253, etc.).
- Pattern-mixed MX1-4: LC 410 (book/painter), LC 621 (task scheduler), LC 787 (cheapest flights), LC 340/992 (distinct window).

## Master resource links (jahan se research + practice)
- Infosys SP/DSE PYQ: [PrepInsta](https://prepinsta.com/infosys-sp-and-dse/) · [GfG Infosys SDE sheet](https://www.geeksforgeeks.org/dsa/infosys-sde-sheet-interview-questions-and-answers/) · GfG OA experiences (2024-25)
- HackWithInfy: [karthikreddy-7 repo](https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions) · [itsmeheisenberg/HackWithInfy](https://github.com/itsmeheisenberg/HackWithInfy) · [Devang-25 HWI 2022](https://github.com/Devang-25/HackWithInfy-2022-Solutions)
- Practice: [LeetCode](https://leetcode.com/) · [GfG Practice](https://www.geeksforgeeks.org/explore) · [NeetCode 150](https://neetcode.io/practice) · [Striver A2Z](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
- Learn: [Aditya Verma DP (YT)](https://www.youtube.com/@AdityaVermaTheProgrammingLord) · [Gate Smashers CS (YT)](https://www.youtube.com/@GateSmashers)

> ⚠️ HONEST: "standard problems" (Tier 1-4) LeetCode ke canonical problems hain — Infosys/har company
> inhi ki tarah ya inpe based questions poochte hain (exact same guarantee nahi). Tier 5 wale ACTUALLY
> Infosys me reported hue. Har problem ab traceable hai — LC number/GfG/source se verify kar sakta hai.
