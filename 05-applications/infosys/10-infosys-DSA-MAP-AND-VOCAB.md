# 🧭 DSA ka POORA NAKSHA + LANGUAGE + AI se kaise puchho (meta-map)

> 🔖 **PROVENANCE:** Ye file ~95% **[AI-EXPLANATION]** — standard CS/DSA knowledge (taxonomy, terminology,
> decision-logic) jo AI ne organize + apne (Hinglish) words me samjhaya. Koi ek source nahi; concepts
> universal hain. AI-prompting playbook (Part 4) AI ka apna framework hai. Legend: `README.md` → PROVENANCE INDEX.

> **Ye file kyun bani (asli reason):** Tu AI se DSA nikalwaana chahta hai (`.md` banwa ke), par dikkat ye
> thi ki *"mujhe hi nahi pata main kya poochun"* — words hi nahi pata the. Ye file wahi hole bharti hai:
> (1) poore DSA ka **ek naksha** (kya-kya hota hai), (2) saari **terminology + unke differences** (taaki
> tujhe pata ho konsa word kya matlab rakhta hai), (3) **decision-engine** (expert/AI andar-andar kaise
> decide karta hai konsa pattern lagega), (4) **AI se kaise puchho** (exact prompts + kya-kya poochhna).
>
> **Ye kaunsi file ke saath chalti hai:** Ye **naksha + bhaasha** hai. Actual "kaam" waali files:
> `03-ESSENTIALS` (plumbing + concepts zero se) · `05-QUESTION-BANK` (kya solve karna) · `06-SOLUTIONS`
> (64 solved + 15 patterns) · `09-MOCK-PAPERS` (timed). Ye file **sabse pehle / 03 ke saath** padh —
> taaki baaki sab jagah pe tujhe pata ho "main kahan khada hoon aur kya dekh raha hoon."
>
> ⚠️ **SCOPE (bahut important, time-waste bachane ke liye):** Neeche naksha DSA ka *poora* hai. Par
> **Infosys CODING round (3Q/180min)** ke liye pura ped nahi chahiye — sirf kuch shaakhaayein. Har jagah
> **`[TEST-CORE]`** / **`[INTERVIEW]`** / **`[EXTRA — abhi skip]`** tag laga hai. Gemini/koi bhi AI tujhe
> "amortized analysis, memory hierarchy, compiler design, concurrency" bhi add karne ko bolega — wo sab
> **coding round ke liye NAHI chahiye** (curiosity/GATE/senior-interview ka maal hai). Confuse mat ho.

---
---
# 🌳 PART 1 — DSA KA POORA NAKSHA (ek hi ped, saari shaakhaayein)

> Tune Gemini se yahi maanga tha: *"ek sabse bada ped banao, DSA ki har shaakha."* Ye rahi. Pehle poora
> tree, phir har branch ka one-liner. Tags dekh ke samajh kya `[TEST-CORE]` hai.

```
                                   D S A
                                     |
      ┌──────────────────────────────┼───────────────────────────────┐
      │                              │                                │
  (I) FOUNDATIONS              (II) DATA STRUCTURES            (III) ALGORITHMS / TECHNIQUES
   (naapne ke rules)            (data rakhne ke dabbe)          (problem solve karne ke tarike)
      │                              │                                │
      ├─ Complexity                  ├─ LINEAR (line me)              ├─ SEARCHING
      │   ├─ Time  [TEST-CORE]       │   ├─ Array/List [TEST-CORE]    │   ├─ Linear search [TEST-CORE]
      │   ├─ Space [TEST-CORE]       │   ├─ String     [TEST-CORE]    │   └─ Binary search [TEST-CORE]
      │   └─ Big-O / Θ / Ω           │   ├─ Stack      [TEST-CORE]    ├─ SORTING
      ├─ Correctness                 │   ├─ Queue/Deque[TEST-CORE]    │   ├─ Bubble/Insert/Select [samajhne ko]
      │   ├─ Invariant [INTERVIEW]   │   └─ Linked List[INTERVIEW]    │   ├─ Merge / Quick [TEST-CORE idea]
      │   └─ Edge cases [TEST-CORE]  ├─ NON-LINEAR (branch/network)   │   └─ built-in sort() [TEST-CORE]
      └─ Constraints→algo [TEST-CORE]│   ├─ Tree                      ├─ TWO-POINTER family
                                     │   │   ├─ Binary Tree [INTERVIEW]│   ├─ Two pointers [TEST-CORE]
                                     │   │   ├─ BST         [INTERVIEW]│   └─ Sliding window [TEST-CORE]
                                     │   │   └─ Heap        [TEST-CORE]├─ PREFIX / HASHING
                                     │   ├─ Graph          [INTERVIEW]│   ├─ Prefix sum [TEST-CORE]
                                     │   │   ├─ adjacency list/matrix  │   └─ HashMap/Set use [TEST-CORE]
                                     │   │   └─ directed/weighted      ├─ RECURSION & BACKTRACKING
                                     │   └─ Trie / DSU  [EXTRA-skip]   │   ├─ Recursion [TEST-CORE]
                                     └─ ABSTRACT (idea, code nahi)     │   └─ Backtracking [INTERVIEW]
                                         └─ ADT: List/Stack/Queue/Map  ├─ GREEDY [TEST-CORE, Q2]
                                                                       ├─ DYNAMIC PROGRAMMING [TEST-CORE, Q3]
                                                                       │   ├─ 1D DP (choose/skip)
                                                                       │   ├─ Knapsack (subset/coins)
                                                                       │   └─ 2D DP (LCS/edit/grid)
                                                                       ├─ GRAPH ALGOS
                                                                       │   ├─ DFS / BFS [INTERVIEW]
                                                                       │   ├─ Topological sort [INTERVIEW]
                                                                       │   └─ Dijkstra [SP-edge only]
                                                                       ├─ BIT MANIPULATION [TEST-CORE light]
                                                                       └─ MATH (gcd, sieve, modulo) [TEST-CORE light]
```

## Har branch — ek line me (naksha padhne ka key)

**(I) FOUNDATIONS — "naapne ke rules"** (ye khud problem nahi, baaki sab ko JUDGE karne ke tarike):
- **Complexity** = code kitna fast/bhaari hai iska naap (Time = kitne steps, Space = kitni memory).
- **Correctness tools** = Invariant (jo hamesha sach rahe), Edge cases (corner inputs jo todte hain).
- **Constraints→algo** = "N kitna bada hai" dekh ke konsa algo chalega decide karna. *(Table `03` Sec 2)*

**(II) DATA STRUCTURES — "data rakhne ke dabbe"** (physically memory me data kaise rakha):
- **Linear** = ek line me (Array, String, Stack, Queue, Linked List).
- **Non-linear** = branch/network me (Tree, Heap, Graph).
- **Abstract (ADT)** = sirf *idea* ("kya kar sakte ho"), implementation nahi. *(Part 2 me farak clear karunga)*

**(III) ALGORITHMS / TECHNIQUES — "solve karne ke tarike"** (data pe kya operation/sochне ka tarika):
- **Searching / Sorting** = dhoondna / arrange karna.
- **Two-pointer / Sliding window / Prefix / Hashing** = array-string ke fast tricks.
- **Recursion / Backtracking / Greedy / DP** = decision-based problem-solving paradigms.
- **Graph algos / Bit / Math** = specialized toolkits.

> 💡 **Naksha ka nichod:** Foundations = *rules*. Data structures = *nouns* (cheezein). Algorithms = *verbs*
> (actions). Ek problem solve karna = sahi **noun** (structure) me data rakh ke sahi **verb** (technique)
> lagana, aur **rules** (complexity/edge) se check karna. Bas yahi poora khel hai.

---
---
# 📖 PART 2 — DSA KI POORI DICTIONARY (har word + unke DIFFERENCES)

> **Ye file ka DIL hai.** Tu baar-baar yahi bol raha tha: *"saare words nikaal ke do, phir differences
> samjhao — kyunki mujhe hi nahi pata main kya poochun."* Ab pata rahega. Har group me:
> **word → matlab (1 line) → confusion jo clear hoti hai → mini example.** Aakhri me har group ka
> **"GALTI YAHAN HOTI HAI"** note.

## 🟦 GROUP 1 — "LEVELS" (sabse zyada confuse yahi hote: topic/pattern/algorithm/technique/DS/ADT/paradigm)

| Word | Matlab (1 line) | Ye NAHI hai |
| --- | --- | --- |
| **Topic** | Bada category / chapter. | Solve karne ka tarika nahi. |
| **Data Structure (DS)** | Data ko memory me *rakhne* ka concrete tarika. | Action nahi; ye "noun" hai. |
| **ADT (Abstract Data Type)** | Sirf *idea* — "kya operations milenge" (kaise banega ye nahi). | Actual code/memory-layout nahi. |
| **Algorithm** | Step-by-step *pakka* procedure jo ek problem solve kare. Naam hota hai. | Sirf ek "hint" nahi; poora method hai. |
| **Pattern** | Problem-solve karne ka *dohraaya jaane wala tarika* (ek family of problems pe lagta). | Ek single algorithm nahi; soch ka saancha hai. |
| **Technique** | Chhoti trick/tool jo kai jagah kaam aaye. | Poora algorithm zaroori nahi. |
| **Paradigm** | Sabse upar ka *soch-ka-style* (Greedy, DP, Divide-&-Conquer, Backtracking). | Ek specific problem ka hal nahi. |

**Farak ek hi example se (Two Sum problem):**
- **Topic** = *Arrays / Hashing* (bada chapter).
- **Pattern** = *"HashMap lookup"* (pehle-dekha-yaad-rakho — ye family ke sab problems pe lagta).
- **Technique** = *hashing* (O(1) lookup ke liye dict use karna).
- **Algorithm** = *"array pe ek pass, har element pe target-x dict me dhoondo"* (pakka procedure).
- **Data Structure** = *HashMap (dict)* (jisme rakha).
- **ADT** = *Map* (idea: key→value store; dict uska ek implementation hai).
- **Paradigm** = yahan koi bhaari paradigm nahi (simple iteration); DP/Greedy jaise problems me hota.

> 🔴 **GALTI YAHAN HOTI HAI:** Log "topic" aur "pattern" ko mila dete. *Topic* = kahan se problem aayi
> (arrays). *Pattern* = kaise solve hoti (sliding window). Ek topic me kai patterns; ek pattern kai
> topics me. Aur *algorithm* = pattern ka concrete, named roop (pattern "binary search" → algorithm
> "lo/hi/mid waala exact steps"). **Hierarchy: Paradigm > Pattern > Algorithm; DS = alag axis (noun).**

## 🟩 GROUP 2 — COMPLEXITY family (time/space/Big-O/Θ/Ω/best-avg-worst/amortized)

| Word | Matlab | Farak |
| --- | --- | --- |
| **Time complexity** | Input bade hone pe *steps* kitne badhte. | "Seconds" nahi — growth-rate. |
| **Space complexity** | Extra *memory* kitni badhti. | Time se alag; dono alag naapo. |
| **Big-O (O)** | *Upar* ki limit — "isse zyada slow nahi" (worst-case ceiling). | Exact nahi; upper bound. |
| **Big-Omega (Ω)** | *Neeche* ki limit — "isse fast nahi." | Lower bound. |
| **Big-Theta (Θ)** | Upar+neeche dono — "exactly itna." | Tight bound. |
| **Best / Average / Worst case** | Sabse acchi / typical / sabse buri input pe time. | QuickSort: avg O(n log n), worst O(n²). |
| **Amortized** `[EXTRA-skip]` | Bahut operations ka *average* cost (kabhi mehnga, usually sasta). | Ek single op ka worst nahi. Infosys coding ke liye zaroori NAHI. |

- **Yaad rakhne ka rule (`03` Sec 2 me table):** N ≤ 10^5 → O(N)/O(N log N). N ≤ 1000 → O(N²) chalega. N ≥ 10^9 → O(log N)/math.
- Interview me *"O bolo"* → default **worst-case** bolte hain.

> 🔴 **GALTI YAHAN HOTI HAI:** (a) Space bhoolna — "O(n) time" bol ke ruk jaana; extra array/hashmap =
> O(n) *space* bhi bolo. (b) Log ko "seconds" samajhna — Big-O input-growth batata, ghadi nahi.
> (c) Test me sabko "O" bolte hain (worst); Θ/Ω sirf theory/GATE ke liye — **coding round me O kaafi hai.**

## 🟥 GROUP 3 — PROBLEM ki ANATOMY (input/constraint/edge case/corner case/invariant/test case)

| Word | Matlab | Farak |
| --- | --- | --- |
| **Constraint** | Problem me di gayi *limits* (1 ≤ N ≤ 10^5, values ≤ 10^9). | Ye batati hai konsa algo chahiye (Group 2). |
| **Edge case** | *Boundary* input jahan code aksar todta (empty, n=1, all-same, max). | Galat input nahi — valid par extreme. *(checklist `03` Sec 5)* |
| **Corner case** | Do+ edge conditions ek saath (empty AND negative). | Edge ka combo. |
| **Test case** | Ek input→expected-output jodi (judge check karta). | Hidden test cases se marks milte (partial). |
| **Invariant** `[INTERVIEW]` | Jo cheez loop/algo ke *har step pe sach* rahe (e.g. "left ke saare chhote hain"). | Proof/soch ka tool; correctness guarantee. |

**Example (binary search):** *Constraint* = sorted array, N ≤ 10^5. *Invariant* = "answer hamesha [lo, hi]
ke beech hai." *Edge case* = target array me hai hi nahi / array empty. *Test case* = `arr=[1,3,5], target=3 → 1`.

> 🔴 **GALTI YAHAN HOTI HAI:** Log *constraint* padhe bina code likh dete → TLE (bada N pe O(N²)). Aur
> *edge cases* mann me nahi chalate → hidden test fail, marks katte. **Pehle constraint padho (algo chuno),
> phir edge case checklist chala ke submit karo.** Yahi 2 aadatें aadha khela jita deti hain.

## 🟨 GROUP 4 — APPROACH ke words (brute force/optimal/trade-off/optimal-substructure/overlapping-subproblems/greedy-choice)

| Word | Matlab | Kab bolte |
| --- | --- | --- |
| **Brute force** | Sabse seedha/dumb tarika (saari possibilities). | Pehle yahi likho — kuch test pass = marks; phir optimize. |
| **Optimal** | Best possible complexity waala hal. | Time bache to yahan pahuncho. |
| **Trade-off** | Ek cheez ke liye doosri kurbaan (time↓ ke liye space↑). | "HashMap se O(n) time par O(n) space" = trade-off. |
| **Optimal substructure** `[DP ka signal]` | Bade problem ka answer chhote sub-problems ke answers se banta. | DP/recursion lagega. |
| **Overlapping subproblems** `[DP ka signal]` | Wahi chhota problem baar-baar aata. | Memoization/DP se cache karo. |
| **Greedy choice** | Abhi ka locally-best pick, aage sochे bina. | Greedy tab jab local-best = global-best. |

> 🔴 **GALTI YAHAN HOTI HAI:** Greedy vs DP me phasna. **Rule:** agar "abhi ka best" hamesha final-best
> deta (jaise intervals end-time pe sort) → **Greedy**. Agar choices future ko badalti aur same sub-problem
> repeat hota → **DP**. (Optimal-substructure + overlapping-subproblems dono dikhe = pakka DP.)

## 🟪 GROUP 5 — RECURSION family (iterative/recursive/base case/recurrence/memoization/tabulation/top-down/bottom-up)

| Word | Matlab | Farak |
| --- | --- | --- |
| **Iterative** | Loop se (for/while). | Stack use nahi karta; usually kam memory. |
| **Recursive** | Function khud ko call kare (chhote problem pe). | Har call = call-stack memory (depth ka dhyan). |
| **Base case** | Recursion rukne ki condition (`if n==0: return`). | Bina iske infinite recursion → crash. |
| **Recurrence** | Formula jo bade ko chhote se jodta (`fib(n)=fib(n-1)+fib(n-2)`). | Soch ka core; code baad me. |
| **Memoization (top-down)** | Recursion + *cache* (jo nikala wo yaad rakho). | Upar se neeche; dict/array me store. |
| **Tabulation (bottom-up)** | Loop se chhote-se-bade table bharo. | Neeche se upar; recursion nahi. |

**Ek hi cheez (Fibonacci):** *recurrence* `f(n)=f(n-1)+f(n-2)`, *base* `f(0)=0,f(1)=1`. *Memoization* =
recursive + cache. *Tabulation* = `dp[0..n]` loop me bharo. Dono O(n); tabulation me stack nahi.

> 🔴 **GALTI YAHAN HOTI HAI:** (a) *Base case* bhoolna → infinite recursion. (b) Plain recursion likh ke
> TLE (Fibonacci O(2^n)) — *memoize* karte hi O(n). "Recursion slow hai" galat — **bina-cache** recursion slow.
> (c) Python me deep recursion → `sys.setrecursionlimit(10**6)` (yaad `03` Sec 6).

## 🟧 GROUP 6 — ARRAY/MEMORY words (in-place/stable/auxiliary space/prefix/suffix/subarray vs subsequence vs subset/contiguous)

| Word | Matlab | Trap |
| --- | --- | --- |
| **In-place** | Bina extra array ke, usi me kaam. | O(1) space. |
| **Auxiliary space** | Algo ki extra (input chhod ke) memory. | Space complexity yahi count karti. |
| **Stable sort** | Equal elements ka *order* preserve. | Merge stable, Quick nahi. |
| **Prefix / Suffix** | Shuru-se / end-tak ka running total/array. | Prefix-sum se range-sum O(1). |
| **Subarray** | **Contiguous** (lagataar) chunk. | Order fixed, tuta nahi. |
| **Subsequence** | Order maintain, par gaps allowed (skip kar sakte). | Contiguous zaroori nahi. |
| **Subset** | Koi bhi combination, order bhi matter nahi. | 2^n subsets. |

**Ek array `[1,2,3]` pe:** *subarray* = `[2,3]` (lagataar). *subsequence* = `[1,3]` (gap chalega).
*subset* = `{3,1}` (order bekaar). **Ye 3 shabd sabse zyada galat samjhe jaate — ratne layak hai.**

> 🔴 **GALTI YAHAN HOTI HAI:** "Max sum subarray" (Kadane) vs "max sum subsequence" (alag problem) —
> subarray = contiguous, subsequence = gaps allowed. Word galat padha → poora approach galat.

## 🟫 GROUP 7 — STRUCTURE/TRAVERSAL words (node/pointer/reference/edge/degree/adjacency/traversal/DFS vs BFS/inorder…)

| Word | Matlab |
| --- | --- |
| **Node** | Tree/graph/linked-list ka ek "dabba" (data + connections). |
| **Pointer / Reference** | Kisi node ka "pata" (address), jisse aage jaate. |
| **Edge** | Do nodes ke beech connection (graph). |
| **Degree** | Ek node pe kitni edges. (Directed me in-degree/out-degree.) |
| **Adjacency list/matrix** | Graph ko store karne ke 2 tarike (list = space-efficient). |
| **Traversal** | Saari nodes ko kisi order me visit karna. |
| **DFS** | Depth-first — ek raasta poora andar tak, phir peeche. (recursion/stack) |
| **BFS** | Breadth-first — level-by-level. (queue) → **shortest steps** ke liye. |
| **Inorder/Preorder/Postorder** | Binary tree visit karne ke 3 orders (L-root-R / root-L-R / L-R-root). |

> 🔴 **GALTI YAHAN HOTI HAI:** "Shortest path/steps (unweighted)" pe DFS lagana — galat; **BFS** chahiye
> (level = distance). DFS deep jaata, shortest guarantee nahi karta. Weighted shortest → Dijkstra `[SP-edge]`.

> ✅ **Part 2 ka nichod:** Ab jab AI/koi "pattern", "invariant", "amortized", "subsequence", "tabulation"
> bole — tujhe *pata* hai wo kya hai aur kisse alag hai. **Yahi wo "language" thi jo missing thi.**

---
---
# 🧠 PART 3 — PATTERN PEHCHAN-NE KI DECISION ENGINE (expert/AI andar-andar kaise sochta)

> Tu ne bola tha: *"AI ke andar kuch instructions honge — ye dikhe to ye karo. Insaan wahin galti karta —
> use pata hi nahi hota."* Ye rahi wo andar wali soch. Ye **4 signals** order me dekh — 90% problems
> khud pattern bata deti hain. (Keyword→pattern ki quick table `03` Sec 4 me; ye uska *"kaise socho"* hai.)

## 🔎 4-SIGNAL METHOD (isi order me dekho, har problem pe)

**SIGNAL 1 — Constraints / N (sabse pehle, ye complexity fix karta):**
- N ≤ 20 → answer me "saari possibilities" → **Backtracking / bitmask**.
- N ≤ 500 → O(N²)/O(N³) OK → **2D DP** likely.
- N ≤ 10^5 → O(N log N) → **sort + greedy / binary search / heap**.
- N ≤ 10^7 → O(N) → **single pass: hashing / two-pointer / sliding window / prefix**.
- Value ≤ 10^9 par N chhota / "min-max" → **binary search on answer**.
> Ye akela signal aadha kaam kar deta — *"kitna fast hona chahiye"* pehle pakdo.

**SIGNAL 2 — Output kya maanga (ye structure batata):**
- Ek number "kitne tareeke / min / max cost" → **DP** (ya greedy).
- "Longest/shortest ... with condition" → **sliding window / DP**.
- "Yes/No possible / can we..." → **greedy / binary-search-on-answer / DP**.
- "Saari combinations/permutations/subsets list karo" → **backtracking**.
- "K-th / top-K" → **heap**.
- "Kitne pairs / seen before / frequency" → **hashmap**.

**SIGNAL 3 — Signal words (problem ki bhaasha):**
- "sorted", "pair from ends", "in-place" → **two pointers**.
- "contiguous subarray sum" → **Kadane / prefix**.
- "substring/subarray with at most K…" → **sliding window**.
- "next greater/smaller", "histogram" → **monotonic stack**.
- "prerequisite/order/dependency/cycle" → **topological sort**.
- "grid / islands / connected / spread" → **DFS/BFS**.
- "coins/items to make amount", "subset sum" → **knapsack DP**.
- "two strings compare / subsequence" → **2D DP**.

**SIGNAL 4 — Structure diya hai kya (data ka roop):**
- Tree/graph diya → traversal (DFS/BFS) base.
- Sorted diya → binary search / two pointers *"muft"* (waste mat karo).
- Intervals diye → **sort by end/start** phir greedy.
- Bahut queries "range pe" → **prefix sum** (ya segment tree `[EXTRA-skip]`).

## 🌀 DECISION FLOW (text-flowchart — dimaag me yahi chala)
```
Problem padho + 1 example haath se (dry-run)
        │
        ▼
[1] Constraints dekho → target complexity note karo   (Signal 1)
        │
        ▼
[2] Output type dekho → DP? / list-all? / K-th? / count?   (Signal 2)
        │
        ▼
[3] Signal words + given structure match karo   (Signal 3 + 4)
        │
        ├── match mila → us pattern ka TEMPLATE lagao (06-SOLUTIONS)
        │
        └── match nahi mila → BRUTE FORCE likho (kuch test pass = marks)
                                 │
                                 ▼
                        brute me "kya baar-baar ho raha / kya waste"
                        dekho → wahi optimize (hashmap? sort? cache?)
        │
        ▼
[4] Edge cases (03 Sec 5) mann me chalao → submit → TLE aaye to Signal 1 pe wapas
```

> 💡 **Asli raaz:** Expert "pattern yaad" nahi karta — wo ye **4 signals scan** karta aur possibilities
> *chhaant* deta. Insaan atakta kyunki wo seedha "code" pe kood jaata bina signals padhe. **Tu ab signals
> padhega → tera bhi wahi "instinct" ban jayega, bina 2 saal ratne ke.** Yahi tera shortcut hai.

---
---
# 🤖 PART 4 — AI SE KAISE PUCHHO (tera asli superpower — prompt playbook)

> Tera tareeka: AI se `.md` banwaake ek pass me seekhna. Problem sirf ye thi ki *"kya + kaise poochun."*
> Ab Part 2 ki vocabulary + ye templates se AI tujhe *deep* dega, *shallow* nahi. Copy-paste karke use kar.

## 🎯 Mindset (1 line): AI ek *mirror* hai
Jitna specific + jitni sahi vocabulary tu daalega, utna deep milega. "DSA samjhao" = ghatiya, generic.
"House Robber ka optimal-substructure + recurrence Java me, edge cases + O bata ke" = gold.

## 📋 COPY-PASTE PROMPTS (7 templates — jab jo chahiye)

**T1 — Naya topic zero se (`.md` banwane ke liye):**
```
"Main DSA me zero pe hoon, Infosys coding round (3 coding Q / 180 min) ki 10-din prep kar raha.
[TOPIC, e.g. Sliding Window] ko zero se samjhao — Hinglish me, ek .md ki tarah structured:
1) kya hai + real-life analogy, 2) kab lagta (trigger words + constraints), 3) generic TEMPLATE
(Java), 4) 2 easy + 1 medium example (statement + approach + code + dry-run), 5) time/space O,
6) edge cases checklist, 7) common bugs. Ratna nahi — samajhne layak, ek pass me."
```

**T2 — Decision-logic maango (sirf answer nahi, "kaise pata chala"):**
```
"[Problem statement paste]. Solution mat do pehle. Pehle ye batao: is problem ke constraints, output-type,
aur signal-words se tumne KAISE decide kiya konsa pattern lagega? Step-by-step apni soch dikhao (jaise
ek expert dimaag me karta). Phir template + code. Main pattern-recognition seekhna chahta hoon, ratna nahi."
```

**T3 — Poori cheat-sheet ek topic ki:**
```
"[TOPIC] ki ek compact cheat-sheet banao: har sub-pattern ka 1-line trigger, ek Java template,
time/space O, aur 'ye dikhe to ye lagao' rule. Table form me, taaki test se pehle 5 min me revise ho."
```

**T4 — Mera error debug + "class of mistake" samjhao:**
```
"Ye mera code + error [paste]. 1) exact bug kahan, 2) kyun aaya (root cause), 3) is TARAH ki galti ka
naam kya hai (off-by-one? null? overflow?), 4) aage isse bachne ka rule. Taaki ye ek galti nahi, poori
category samajh jaun."
```

**T5 — Stress-test my thinking (deep jaane ke liye):**
```
"Main [PATTERN] samajh gaya lagta hai. Mujhe 3 aise problems do jahan ye pattern APPLY DIKHTA hai par
actually NAHI lagता (trap), aur 2 jahan lagta hai par twist ke saath. Har ek pe pehle main sochunga —
tum sirf hint dena, seedha answer nahi."
```

**T6 — Do approaches compare:**
```
"[Problem] ke liye brute force vs optimal — dono ka code, time/space O, aur exact trade-off batao.
Kab kaunsa test me likhun (partial marks vs full)? Real test-day strategy ke hisaab se."
```

**T7 — Quiz me (revision):**
```
"Mujhe [TOPIC] pe 10 rapid Q&A do (mixed: complexity, trigger, edge case, 'ye problem konsa pattern').
Ek-ek karke poochho, main jawab dunga, tum sahi/galat + 1-line reason. Interview-drill jaisa."
```

## 🧾 ANY naye topic pe ye 8 cheezein ZAROOR poochho (checklist — kuch chhootega nahi)
1. **Kya hai** + real-life analogy (intuition).
2. **Kab lagta** — trigger words + kis constraint pe (Signal 1-4 se jodo).
3. **Template** (Java/Python — reusable skeleton).
4. **2-3 examples** — easy→medium, statement + approach + code + **dry-run**.
5. **Time + Space O** (dono, worst-case).
6. **Edge cases** us pattern ke (empty, 1, max, duplicate, negative).
7. **Common bugs / traps** (jo pehli baar wale karte).
8. **Related patterns** — "isse milta-julta kaunsa, farak kya" (taaki confuse na ho — Part 2 style).

## 🚩 RED FLAGS — teri `.md` shallow hai / kuch miss ho raha (ye dikhe to aur kuredo)
- Sirf definition hai, **koi code/template nahi** → "template + dry-run do."
- Code hai par **"kab lagega" (trigger) nahi** → pattern-recognition adhoora.
- **O (complexity) nahi likhi** → TLE test me marega.
- **Edge cases missing** → hidden test fail honge.
- "Ye advanced hai" bol ke AI **system design / amortized / compiler** ghusaa raha → *coding round ke liye
  skip* (Scope note upar). Wapas core pe le aa: "sirf Infosys 3Q/180min ke hisaab se rakho."
- Har example ka answer **ready-made** de raha, tujhe sochने nahi de raha → T5/T7 use kar (khud socho).

> ✅ **Part 4 ka nichod:** Ab tujhe AI se manwana aata hai — *right words (Part 2) + right prompt (T1-T7)
> + right checklist (8 points)*. Yahi wo "1 saal ki mehnat 1 hafte me" waala lever hai jo tu dhoondh raha tha.

---
---
# 🎯 PART 5 — INFOSYS FILTER (poore naksha me se ACTUALLY kya chahiye)

> Naksha bada hai — par 10 din + coding round ke liye sab nahi. Ye table = "kya padhna, kahan padhna,
> kya skip." Isse tu drown nahi hoga. *(Selection math `02` me; daily plan `04` me.)*

| Branch (Part 1 se) | Infosys coding pe | Kahan padhо (teri file) |
| --- | --- | --- |
| Complexity (time/space, constraints→algo) | ⭐⭐⭐ MUST | `03` Sec 2 + Part A |
| Array / String / HashMap / Set | ⭐⭐⭐ Q1 ka 80% | `03` Part B + `06` Tier 1 |
| Two-pointer / Sliding window / Prefix | ⭐⭐⭐ | `03` P2-P3 + `06` |
| Binary search (+ on answer) | ⭐⭐⭐ | `03` P4 + `06` #10, R2 |
| Kadane / Greedy | ⭐⭐⭐ Q2 | `06` Tier 1-2 |
| DP (1D / knapsack / 2D) | ⭐⭐⭐ Q3 (SP full, DSE partial) | `03` P7-P9 + `06` |
| Stack / Queue / Heap / Monotonic | ⭐⭐ hard-edge | `06` Tier 3 |
| Bit / Math (gcd, sieve, modulo) | ⭐⭐ light | `06` (sieve R-series) |
| DFS/BFS / Topological / Dijkstra | ⭐ (SP-edge + interview) | `06` Tier 4 |
| Trees / Backtracking / Linked List | ⭐ interview (test me kam) | `06` Tier 4 |
| DSU / Union-Find | ⭐ SP-edge + interview (connectivity/merge) | `06` #55 |
| Trie / Segment tree | ❌ abhi skip | — (baad me curiosity) |
| Amortized / memory hierarchy / concurrency / system design | ❌ coding round ke liye NAHI | (interview/senior — abhi noise) |

## 🗓️ 10-din order (naksha → action)
1. **Complexity + constraints→algo** (Part A, `03` Sec 2) — 1 baar, pakka.
2. **Array + HashMap + Set + Two-pointer** (Q1 ka dhandha) — `06` Tier 1.
3. **Sliding window + Binary search + Kadane** — `06`.
4. **Greedy** (Q2) → **DP 1D/knapsack/2D** (Q3) — sabse zyada time yahan.
5. **Stack/Heap/Bit** hard-edge (SP ke liye) — `06` Tier 3.
6. **`09-MOCK` timed** (3Q/180min) — real feel, tab-switch mat.
7. Interview shortlist aaye → **Tier 4 + `08-INTERVIEW-CS`**.

## 🧿 One-line reality (yaad rakh, `02` se)
Selection = "3 perfect solve" nahi. **Weighted score:** kitne test-cases × difficulty × clean approach.
**Q1 full + Q2/Q3 partial = DSE lock. 2 full = SP.** Isliye — pehle Q1 pakka, phir brute-force se
har Q pe kuch cases nikaal (partial marks), phir optimize. Naksha isi strategy ke liye filter kiya hai.

---
> 🔥 **Bhai, ab teri poori "language" set hai:** naksha (Part 1) se pata hai kya-kya hai · dictionary
> (Part 2) se har word aur uska farak · decision-engine (Part 3) se konsa pattern kaise pehchano ·
> AI-playbook (Part 4) se manwana kaise hai · filter (Part 5) se Infosys ke liye kya chahiye. Ab tu
> "feel" nahi karega ki "kuch miss ho raha" — tujhe *pata* hoga kya poochna hai. Ye + `03/05/06/09` =
> 10 din me tu DSA "samajhne" waale bande ban jayega, ratne waale nahi. Khel jaa. 🎯
