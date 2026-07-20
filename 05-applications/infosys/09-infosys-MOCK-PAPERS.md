# Infosys SP/DSE — MOCK PAPERS + REAL PYQ (actual test feel)

> 🔖 **PROVENANCE:** MOCK SET 1-5 ke problem-STORIES = **[AI-GENERATED]** (AI ne likhe) par real
> patterns/problems pe based — har problem ke saath "Mirrors: [SRC]" hai (jaise LC 312, Wipro, Accenture).
> "REAL PYQ BANK" section = **[REAL-PYQ]** (actually Infosys me reported, source ke saath). Solutions ka
> code = [AI-EXPLANATION]. Legend: `README.md` → PROVENANCE INDEX.

> Maqsad: test **ajeeb na lage**. Infosys ke questions **story-wrapped** hote hain (kahani + Input
> format + Constraints + Output + Sample cases). Ye file exactly wahi feel deti hai.
> Har mock set = **3 questions / 180 min** (Q1 easy 20 · Q2 greedy 30 · Q3 DP 50) — bilkul real jaisa.
>
> **Kaise use karo (real mock):** timer 180 min lagao, phone door, ek editor kholo (Python/Java),
> khud solve karo, PHIR solution dekho. Problem statements meri words me hain (real Infosys PYQ
> patterns pe based — sources: PrepInsta, GfG OA experiences, Scribd PYQ 2024-25).
> Patterns aur base solutions: `06-infosys-SOLUTIONS.md`. Plumbing: `03-infosys-ESSENTIALS.md`.

---
# 🧪 MOCK SET 1 (180 min — start timer)

## Q1 — "Popular Product" [Easy · 20 marks]
Ek online store ke paas **N** orders hain. Har order ek product ID hai. Store manager us product ko
"Popular Product" declare karta hai jo **strictly N/2 se zyada** baar order hua ho. Guaranteed hai ki
aisa ek product hamesha exist karta hai. Us product ka ID print karo.

**Input format:**
- Line 1: integer N (orders ki sankhya)
- Line 2: N space-separated integers (product IDs)

**Output:** Popular Product ka ID.

**Constraints:** 1 ≤ N ≤ 10^6 · 1 ≤ ID ≤ 10^9

**Sample Input:**
```
7
3 3 4 2 3 3 3
```
**Sample Output:**
```
3
```
**Explanation:** 3 aaya 5 baar (> 7/2 = 3.5). Isliye 3.

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Moore's Voting (O(n), O(1)). N up to 10^6 → hashmap bhi chalega par voting best.
```python
import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count, cand = 0, None
    for x in arr:
        if count == 0: cand = x
        count += 1 if x == cand else -1
    print(cand)
solve()
```
**Complexity:** O(n) time, O(1) space. (Detail: `06-SOLUTIONS.md` #4.)
</details>

---

## Q2 — "Festival Stalls" [Medium · 30 marks · Greedy]
Ek festival ground pe **N** stall-owners aana chahte hain. Har owner ka ek fixed time-slot hai
`[start, end)` jisme wo ground use karega. Ground pe **ek time pe ek hi stall** lag sakta hai.
Organizer maximum kitne stalls allow kar sakta hai bina kisi do slots ke overlap ke?

**Input format:**
- Line 1: N
- Agli N lines: do integers `start end` (ek stall ka slot)

**Output:** maximum non-overlapping stalls ki sankhya.

**Constraints:** 1 ≤ N ≤ 10^5 · 0 ≤ start < end ≤ 10^9

**Sample Input:**
```
4
1 3
3 5
2 4
5 7
```
**Sample Output:**
```
3
```
**Explanation:** End-time pe sort → `[1,3],[2,4],[3,5],[5,7]`. Greedy pick jiska end sabse jaldi:
`[1,3]` lo (end=3) → `[2,4]` skip (start 2 < 3, overlap) → `[3,5]` lo (start 3 ≥ 3) → `[5,7]` lo
(start 5 ≥ 5). Total = **3** non-overlapping stalls. (Slot `[start,end)` half-open hai, isliye end==start
touch overlap nahi.)

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Activity selection — **end time pe sort**, greedily pick jiska end sabse jaldi.
```python
import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    slots = [tuple(map(int, input().split())) for _ in range(n)]
    slots.sort(key=lambda x: x[1])      # end pe sort
    count, last_end = 0, -1
    for s, e in slots:
        if s >= last_end:               # overlap nahi
            count += 1
            last_end = e
    print(count)
solve()
```
**Complexity:** O(n log n). **Insight:** jaldi khatam hone wala pick karo → max fit.
(Related: `06-SOLUTIONS.md` #22 Non-overlapping Intervals.)
</details>

---

## Q3 — "Warehouse Partition" [Hard · 50 marks · DP]
Ek warehouse me **N** boxes ek line me hain, har box ka weight `a[i]`. Inhe **exactly K contiguous
groups** me baantna hai (har box exactly ek group me). Ek group ka **cost = us group ke weights ka
sum ka square**. Total cost = saare groups ke cost ka sum. Aisa partition dhoondo jisme **total cost
minimum** ho. Minimum total cost print karo.

**Input format:**
- Line 1: do integers N K
- Line 2: N space-separated integers a[i]

**Output:** minimum possible total cost.

**Constraints:** 1 ≤ K ≤ N ≤ 500 · 1 ≤ a[i] ≤ 10^4

**Sample Input:**
```
4 2
1 2 3 4
```
**Sample Output:**
```
52
```
**Explanation:** 2 groups ke possible splits: `[1][2,3,4]` → 1² + 9² = 82; `[1,2][3,4]` → 3² + 7² =
9+49 = 58; `[1,2,3][4]` → 6² + 4² = 36+16 = **52**. Minimum = **52**.

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Interval/partition DP. `dp[i][k]` = pehle i elements ko k groups me baantne ka min cost.
Transition: `dp[i][k] = min over j ( dp[j][k-1] + cost(j+1..i) )`, cost = (prefix[i]-prefix[j])².
```python
import sys
input = sys.stdin.readline
def solve():
    n, K = map(int, input().split())
    a = list(map(int, input().split()))
    pre = [0]*(n+1)
    for i in range(n): pre[i+1] = pre[i] + a[i]
    INF = float('inf')
    # dp[k][i] = min cost of first i elements in k groups
    dp = [[INF]*(n+1) for _ in range(K+1)]
    dp[0][0] = 0
    for k in range(1, K+1):
        for i in range(1, n+1):
            for j in range(k-1, i):          # last group = a[j..i-1]
                seg = pre[i] - pre[j]
                if dp[k-1][j] + seg*seg < dp[k][i]:
                    dp[k][i] = dp[k-1][j] + seg*seg
    print(dp[K][n])
solve()
```
**Complexity:** O(K·N²) — N≤500 so ~1.25e8 worst, borderline; DSE ke liye ye partial bhi chalega.
**Insight:** "array ko k parts me baanto, cost optimize" = **partition DP** (real Infosys SP PYQ).
</details>

> ⏱️ SET 1 khatam. Score: Q1 full + Q2/Q3 partial = DSE zone. Teeno = SP zone.


---
# 🧪 MOCK SET 2 (180 min — start timer)

## Q1 — "Secret Code Palindrome" [Easy · 20 marks]
Ek security system ka password valid tab hai jab wo **palindrome** ho — par sirf letters aur digits
count hote hain, baaki symbols/spaces ignore, aur case (upper/lower) ignore. Ek string di hai; print
`YES` agar valid palindrome hai, warna `NO`.

**Input format:** Line 1: string S (spaces/symbols ho sakte hain).
**Output:** `YES` / `NO`.
**Constraints:** 1 ≤ |S| ≤ 10^5.

**Sample Input:**
```
A man, a plan, a canal: Panama
```
**Sample Output:**
```
YES
```

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Two pointers (alphanumeric skip, case-insensitive).
```python
import sys
def solve():
    s = sys.stdin.readline().rstrip("\n")
    t = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(t)-1
    while i < j:
        if t[i] != t[j]: print("NO"); return
        i += 1; j -= 1
    print("YES")
solve()
```
**Complexity:** O(n). (Detail: `06-SOLUTIONS.md` #6.)
</details>

---

## Q2 — "Treasure Picker (Khaled)" [Medium · 30 marks · Greedy]
Khaled ke paas **N** treasures ki ek array A hai (N even). Wo **at most N/2** treasures utha sakta hai
(consecutive hona zaroori nahi). Har treasure ki value A[i] hai. Wo **maximum total value** chahta hai
jo utha sake. Wo maximum sum print karo.

**Input format:** Line 1: N (even) · Line 2: N integers A[i] (positive & negative ho sakte).
**Output:** max sum of at most N/2 chosen elements.
**Constraints:** 2 ≤ N ≤ 10^5 · -10^9 ≤ A[i] ≤ 10^9.

**Sample Input:**
```
6
5 -2 9 -8 3 1
```
**Sample Output:**
```
17
```
**Explanation:** N/2 = 3. Top-3 positive by value: 9,5,3 = 17. (Negatives skip; agar sab negative to
0 chuno / ya problem ke hisaab se — edge case dhyan.)

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Greedy — sort desc, top N/2 me se sirf positive lo.
```python
import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = 0
    for i in range(n//2):        # at most N/2
        if a[i] > 0: total += a[i]
        else: break              # aage sab chhote/negative
    print(total)
solve()
```
**Complexity:** O(n log n). **Insight:** "at most K elements, maximize" = sort + top-K greedy.
(Real Infosys DSE PYQ — "Khaled, at most N/2 elements".)
</details>

---

## Q3 — "Cashier Minimum Notes" [Hard · 50 marks · DP]
Ek cashier ke paas unlimited notes hain denominations `coins[]` me. Use **exactly amount X** dena hai
minimum notes me. Agar possible nahi to `-1`. Minimum notes ki sankhya print karo.

**Input format:** Line 1: M (denominations) · Line 2: M integers coins[] · Line 3: X (amount).
**Output:** min notes, ya -1.
**Constraints:** 1 ≤ M ≤ 100 · 1 ≤ coins[i] ≤ 10^4 · 1 ≤ X ≤ 10^5.

**Sample Input:**
```
3
1 2 5
11
```
**Sample Output:**
```
3
```
**Explanation:** 5+5+1 = 11 → 3 notes.

<details><summary>APPROACH + SOLUTION</summary>

**Pattern:** Unbounded knapsack DP (Coin Change).
```python
import sys
input = sys.stdin.readline
def solve():
    m = int(input()); coins = list(map(int, input().split())); X = int(input())
    INF = float('inf')
    dp = [0] + [INF]*X
    for amt in range(1, X+1):
        for c in coins:
            if c <= amt and dp[amt-c]+1 < dp[amt]:
                dp[amt] = dp[amt-c]+1
    print(dp[X] if dp[X] != INF else -1)
solve()
```
**Complexity:** O(X·M). (Detail: `06-SOLUTIONS.md` #17.)
</details>

> ⏱️ SET 2 khatam. Ab check: kitne test cases pass hote (edge: empty, all-negative, X impossible).

---
# 📜 REAL PYQ BANK — actual Infosys me poochhe gaye (statements + approach)
> Ye actually reported hain (sources: GfG OA experiences, PrepInsta, Scribd PYQ 2024-25). Statement
> meri words me; solve khud karo phir approach dekho.
> 👉 **In sabke FULL CODE solutions `06-infosys-SOLUTIONS.md` ke TIER 5 (R1-R13) me hain.**

### PYQ 1 — "Hungry Fish" (GfG, SP lateral) [Hard]
Ek injected fish size x kisi chhoti fish y (y<x) ko kha ke size x+y ho jaati hai. Aquarium me kai
fish hain. Scientist **normal fish add ya remove** kar sakta hai (2 moves). Objective: ant me sirf
**1 fish** bache. Minimum moves batao.
**Approach:** sort karo; injected fish se greedily chhoti fish khilao; jise nahi kha sakte use remove
karo ya ek chhoti add karke bridge banao. Greedy + sorting.

### PYQ 2 — "GET(l,r) Max Pairs" (GfG SP OA, Dec 2024) [Hard]
Array arr[n]. Function GET(l,r) defined (e.g. subarray XOR/sum/max). Un index pairs (l,r), 1≤l<r≤n,
ki **sankhya** batao jinke liye GET(l,r) **maximum** hai.
**Approach:** GET ka max nikaalo (prefix/sliding), phir count karo kitne pairs wahi max dete. Prefix + hashing.

### PYQ 3 — "Spiral Matrix" (HackWithInfy 2026, L3) [Medium]
M×N matrix ko **spiral order** me traverse karke elements print karo (top→right→bottom→left, andar aate jao).
**Approach:** 4 boundaries (top,bottom,left,right) maintain karo, shrink karte jao. Careful boundary handling.
```python
def spiralOrder(mat):
    res=[]; top,bot=0,len(mat)-1; left,right=0,len(mat[0])-1
    while top<=bot and left<=right:
        for j in range(left,right+1): res.append(mat[top][j])
        top+=1
        for i in range(top,bot+1): res.append(mat[i][right])
        right-=1
        if top<=bot:
            for j in range(right,left-1,-1): res.append(mat[bot][j])
            bot-=1
        if left<=right:
            for i in range(bot,top-1,-1): res.append(mat[i][left])
            left+=1
    return res
```

### PYQ 4 — "Largest Number" (karthikreddy repo) [Medium · Greedy]
Non-negative integers ki array (as strings) ko aise arrange karo ki concatenate karne pe **largest
number** bane. Print that number.
**Approach:** custom comparator — a+b vs b+a. (Full: `06-SOLUTIONS.md` #21.)

### PYQ 5 — "Subset Sum" (karthikreddy repo) [Medium · DP]
Non-negative integers ka set + value `sum`. Check karo koi subset hai jiska sum = given sum. `True/False`.
Example: set={3,34,4,12,5,2}, sum=9 → True (4+5).
**Approach:** boolean knapsack DP. (Full: `06-SOLUTIONS.md` #25 Partition — same skeleton.)

### PYQ 6 — "Drying Walls / Painter" (Scribd SP PYQ 2024) [Hard]
N walls, har wall ko paint karne me time; ek paid painter + ek free painter (free tab kaam kare jab
paid busy ho). Minimize cost. **Approach:** DP + greedy (paint-house / painter-partition style).

### PYQ 7 — "Count Distinct Subarray Values" (Scribd, SP 7-Jul-2024) [Medium]
Array A ke saare subarrays consider karo; kuch property (distinct count / max) pe based answer.
**Approach:** sliding window + hashing, ya contribution technique.

---
# 🎯 MOCK STRATEGY (test-day dohrao)
1. Pehle 10 min: teeno padho. Q1 (easy) pakka pehle → 20 marks bank.
2. Q2/Q3 me brute force → jitne test cases pass ho. Partial = marks.
3. Har solve se pehle edge cases (empty, 1 element, all-negative, max N) — `03-ESSENTIALS.md` checklist.
4. Story lambi ho to ghabrao mat — usme se **actual input/output + constraint** nikaalo, wahi asli problem hai.
5. **≥ 2 aise timed mocks** de do test se pehle → real test bilkul familiar lagega.


---
# 🧪 MOCK SET 3 (180 min — start timer)

## Q1 — "Sock Sorting" [Easy · 20 marks]
Ek laundry me **N** socks ek dher me hain, har sock ek color-code (integer) ka hai. Do same-color
socks ka ek **pair** banta hai. Maximum kitne complete pairs ban sakte hain?

**Input:** Line1: N · Line2: N integers (colors).
**Output:** number of pairs.
**Constraints:** 1 ≤ N ≤ 10^5 · 1 ≤ color ≤ 10^9.
**Sample Input:**
```
7
10 20 20 10 10 30 50
```
**Sample Output:**
```
2
```
**Explanation:** 10 → 3 socks → 1 pair; 20 → 2 → 1 pair; baaki single. Total 2.
**Edge:** N=0 → 0; sab distinct → 0; sab same (N socks) → N//2.

<details><summary>SOLUTION</summary>

**Pattern:** Frequency map. Har color ke count//2 jodo.
```python
import sys
from collections import Counter
def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); colors = data[1:1+n]
    freq = Counter(colors)
    print(sum(c//2 for c in freq.values()))
solve()
```
**Complexity:** O(N). **Mirrors:** Wipro "Sock Merchant" (HackerRank/Wipro OA real).
</details>

---

## Q2 — "Feeding the Rats" [Medium · 30 marks · Greedy]
Ek gali me **H** ghar line me hain; ghar i me `food[i]` units khana hai. **R** rats hain, har rat
**U** units khata hai. Ek rat lagatar (contiguous) gharon se kha sakta hai jab tak U pura na ho.
**Minimum kitne ghar** chahiye taaki saare R rats pet bhar sakein? (Agar possible nahi → -1.)

**Input:** Line1: H R U · Line2: H integers food[].
**Output:** min ghar (ya -1).
**Constraints:** 1 ≤ H ≤ 10^5 · 1 ≤ R,U ≤ 10^9 · 0 ≤ food[i] ≤ 10^4.
**Sample Input:**
```
5 2 4
1 3 2 4 2
```
**Sample Output:**
```
3
```
**Explanation:** Total chahiye R×U = 8. Ghar greedily lo (max food pehle): 4+3+2 = 9 ≥ 8 → 3 ghar.
**Edge:** total food < R×U → -1; U huge → -1.

<details><summary>SOLUTION</summary>

**Pattern:** Greedy — sabse zyada food wale ghar pehle lo jab tak need pura na ho.
```python
import sys
def solve():
    data = sys.stdin.read().split()
    h, r, u = int(data[0]), int(data[1]), int(data[2])
    food = list(map(int, data[3:3+h]))
    need = r * u
    food.sort(reverse=True)
    count = 0; got = 0
    for f in food:
        if got >= need: break
        got += f; count += 1
    print(count if got >= need else -1)
solve()
```
**Complexity:** O(H log H). **Mirrors:** Accenture "feed rats / min houses" (real OA).
</details>

---

## Q3 — "Balloon Coins" [Hard · 50 marks · Interval DP]
**N** balloons ek line me, balloon i pe number `a[i]`. Tum balloons ek-ek karke burst karte ho. Jab
balloon i burst karo to **coins = a[left] × a[i] × a[right]** milte (left/right = i ke abhi-bache
adjacent balloons; array ke bahar imaginary balloon = 1). Sab burst karke **max total coins** batao.

**Input:** Line1: N · Line2: N integers a[].
**Output:** max coins.
**Constraints:** 1 ≤ N ≤ 300 · 0 ≤ a[i] ≤ 100.
**Sample Input:**
```
4
3 1 5 8
```
**Sample Output:**
```
167
```
**Explanation:** best order → 1,5,3,8 burst; coins add up to 167 (classic).
**Edge:** N=1 → a[0]×1×1 = a[0]; a[i]=0 handled by formula.

<details><summary>SOLUTION</summary>

**Pattern:** Interval DP — "last balloon to burst in (l,r)". `dp[l][r]` = max coins bursting all strictly between l,r.
```python
import sys
def solve():
    data = sys.stdin.read().split()
    n = int(data[0]); a = list(map(int, data[1:1+n]))
    vals = [1] + a + [1]                      # padding
    m = len(vals)
    dp = [[0]*m for _ in range(m)]
    for length in range(2, m):                # gap between l and r
        for l in range(0, m-length):
            r = l + length
            for k in range(l+1, r):           # k = last burst in (l,r)
                dp[l][r] = max(dp[l][r],
                               dp[l][k] + vals[l]*vals[k]*vals[r] + dp[k][r])
    print(dp[0][m-1])
solve()
```
**Complexity:** O(N³). **Mirrors:** LeetCode 312 "Burst Balloons" (HWI-hard interval-DP style).
</details>

> ⏱️ SET 3 done. Interval DP (Q3) = SP-hard tier — samajh gaye to bada edge.

---
# 🧪 MOCK SET 4 (180 min — start timer)

## Q1 — "Reach the Number" [Easy-Medium · 20 marks]
Ek counter `X` pe start hai. Ek move me ya to counter **+1** karo ya **×2**. Minimum kitne moves me
`X` se `Y` (Y ≥ X) tak pahunchoge?

**Input:** Line1: X Y.
**Output:** min moves.
**Constraints:** 1 ≤ X ≤ Y ≤ 10^9.
**Sample Input:**
```
3 11
```
**Sample Output:**
```
4
```
**Explanation:** Forward: `3 →(+1) 4 →(+1) 5 →(×2) 10 →(+1) 11` = **4 moves**. (Code backward chalta:
`11→10→5→4→3` = 4 steps — jo tez hai.) 3 moves me 11 possible nahi (verify: max reach checks).
**Edge:** X==Y → 0.

<details><summary>SOLUTION</summary>

**Pattern:** Greedy **working backwards** (Y→X): Y even & Y>X → divide; else Y-1. (BFS bhi chalega par slow.)
```python
import sys
def solve():
    x, y = map(int, sys.stdin.readline().split())
    moves = 0
    while y > x:
        if y % 2 == 0 and y // 2 >= x:
            y //= 2
        else:
            y -= 1
        moves += 1
    print(moves + (x - y))                    # agar y x se neeche gir gaya
solve()
```
**Complexity:** O(log Y). **Mirrors:** "Unthinkable/Y→X division" OA (real, Sep 2025).
</details>

---

## Q2 — "Conference Rooms" [Medium · 30 marks · Greedy + Heap]
**N** meetings hain, har ek `[start, end)`. Ek room me ek time pe ek meeting. **Minimum kitne rooms**
chahiye taaki saari meetings ho sakein?

**Input:** Line1: N · agli N lines: start end.
**Output:** min rooms.
**Constraints:** 1 ≤ N ≤ 10^5 · 0 ≤ start < end ≤ 10^9.
**Sample Input:**
```
3
0 30
5 10
15 20
```
**Sample Output:**
```
2
```
**Explanation:** [0,30] overlaps dono se → 2 rooms.

<details><summary>SOLUTION</summary>

**Pattern:** Sort by start + **min-heap** of end-times (busy rooms). Heap size = rooms needed.
```python
import sys, heapq
def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    it = iter(data[1:])
    meets = [(int(s), int(e)) for s, e in zip(it, it)]
    meets.sort()
    heap = []                                  # end times
    for s, e in meets:
        if heap and heap[0] <= s:
            heapq.heappop(heap)                # ek room free ho gaya
        heapq.heappush(heap, e)
    print(len(heap))
solve()
```
**Complexity:** O(N log N). **Mirrors:** LeetCode 253 "Meeting Rooms II" (greedy+heap).
</details>

---

## Q3 — "Spell Corrector" [Hard · 50 marks · DP]
Ek user ne word `A` type kiya; dictionary word `B` hai. Ek operation = insert / delete / replace ek
character. `A` ko `B` banane ke **minimum operations** (edit distance) batao.

**Input:** Line1: A · Line2: B.
**Output:** min operations.
**Constraints:** 1 ≤ |A|,|B| ≤ 2000.
**Sample Input:**
```
sunday
saturday
```
**Sample Output:**
```
3
```
**Explanation:** sunday→saturday: insert 'a','t', replace 'n'→'r' → 3.

<details><summary>SOLUTION</summary>

**Pattern:** 2D DP (edit distance).
```python
import sys
def solve():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(dp[m][n])
solve()
```
**Complexity:** O(m·n). **Mirrors:** LeetCode 72 "Edit Distance" (`06` #28).
</details>

> ⏱️ SET 4 done.


---
# 🧪 MOCK SET 5 (180 min — start timer)

## Q1 — "Code Formatter" [Easy · 20 marks]
Ek code editor check karta hai ki brackets balanced hain ya nahi. String me sirf `(){}[]` hain.
Balanced tab jab har opening ka sahi order me matching closing ho. `YES`/`NO` print karo.

**Input:** Line1: string S.
**Output:** YES / NO.
**Constraints:** 1 ≤ |S| ≤ 10^5.
**Sample Input:**
```
{[()]}
```
**Sample Output:**
```
YES
```
**Edge:** empty → YES; sirf closing `)` → NO; odd length → NO.

<details><summary>SOLUTION</summary>

**Pattern:** Stack.
```python
import sys
def solve():
    s = sys.stdin.readline().strip()
    pairs = {')':'(', ']':'[', '}':'{'}
    st = []
    for c in s:
        if c in pairs:
            if not st or st.pop() != pairs[c]:
                print("NO"); return
        else:
            st.append(c)
    print("YES" if not st else "NO")
solve()
```
**Complexity:** O(n). **Mirrors:** LeetCode 20 (`06` #20).
</details>

---

## Q2 — "Warehouse Looter" [Medium · 30 marks · Greedy]
Ek chor ke paas bag capacity **W** hai. **N** items hain, item i ka weight w[i], value v[i]. Chor
item ka **fraction** bhi le sakta hai (item divisible hai). Max total value batao (2 decimal tak).

**Input:** Line1: N W · agli N lines: w v.
**Output:** max value (2 decimals).
**Constraints:** 1 ≤ N ≤ 10^5 · 1 ≤ W,w,v ≤ 10^9.
**Sample Input:**
```
3 50
10 60
20 100
30 120
```
**Sample Output:**
```
240.00
```
**Explanation:** ratio (v/w): 6,5,4. Le: pura 10(60)+pura 20(100)+ 20/30 of 30(80) = 240.

<details><summary>SOLUTION</summary>

**Pattern:** **Fractional knapsack** = Greedy by value/weight ratio (0/1 knapsack se ALAG — wo DP hota).
```python
import sys
def solve():
    data = sys.stdin.read().split()
    n, W = int(data[0]), int(data[1])
    items = []
    idx = 2
    for _ in range(n):
        w, v = int(data[idx]), int(data[idx+1]); idx += 2
        items.append((v/w, w, v))
    items.sort(reverse=True)                    # ratio desc
    total = 0.0
    for ratio, w, v in items:
        if W >= w:
            total += v; W -= w
        else:
            total += ratio * W; break           # fraction
    print(f"{total:.2f}")
solve()
```
**Complexity:** O(N log N). **Insight:** fraction allowed → greedy; fraction NOT allowed → 0/1 knapsack DP (`06` #24). **Ye difference interview me poochte hain!**
</details>

---

## Q3 — "Longest Palindrome Signal" [Hard · 50 marks · DP]
Ek signal string `S` hai. Usme se kuch characters hata ke sabse lambi **palindromic subsequence**
banao (order same rahe, characters delete kar sakte). Uski length batao.

**Input:** Line1: S.
**Output:** longest palindromic subsequence length.
**Constraints:** 1 ≤ |S| ≤ 2000.
**Sample Input:**
```
bbbab
```
**Sample Output:**
```
4
```
**Explanation:** "bbbb" palindrome subsequence → length 4.

<details><summary>SOLUTION</summary>

**Pattern:** 2D DP — `dp[i][j]` = LPS in S[i..j]. Ends match → +2, else max(skip left/right).
```python
import sys
def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    print(dp[0][n-1])
solve()
```
**Complexity:** O(n²). **Mirrors:** LeetCode 516 (LCS-family, `06` #26 ka cousin — LPS = LCS(S, reverse(S))).
</details>

> ⏱️ SET 5 done. Total ab 5 full mock sets.

---
# 🧬 PATTERN-MIXED PROBLEMS (2+ patterns ek saath — real OA layered style)
> Real test me single-pattern kam, **layered** problems zyada. Ye samajh gaye to koi bhi combo aaye, ready.

## MX1 — "Library Allocation" [Hard · Binary Search + Greedy]
**N** books line me, book i me pages[i]. **M** students me baantni hain — har student ko **contiguous**
books milengi, har book kisi ek ko. Aisa baanto ki **jise sabse zyada pages mile, wo minimum ho**. Wo value batao.
**Constraints:** 1 ≤ M ≤ N ≤ 10^5.
<details><summary>SOLUTION</summary>

**Mixed pattern:** *Binary search on the answer* (max-pages) + *greedy* feasibility check.
```python
import sys
def solve():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    pages = list(map(int, data[2:2+n]))
    def students_needed(limit):
        cnt, cur = 1, 0
        for p in pages:
            if p > limit: return float('inf')
            if cur + p > limit: cnt += 1; cur = p
            else: cur += p
        return cnt
    lo, hi = max(pages), sum(pages)
    while lo < hi:
        mid = (lo+hi)//2
        if students_needed(mid) <= m: hi = mid
        else: lo = mid+1
    print(lo)
solve()
```
**Kyun mixed:** answer pe binary search + har mid pe greedy check. O(N log(sum)). (Painter's/Book-allocation.)
</details>

## MX2 — "Server Task Scheduler" [Medium-Hard · Greedy + Math + Heap-thinking]
CPU pe **tasks** (letters) run karne hain. Same task ke do runs ke beech **kam se kam n idle/other
units** ka gap chahiye (cooldown). Minimum total time (task+idle) batao.
**Example:** tasks="AAABBB", n=2 → 8 (`A B _ A B _ A B`).
<details><summary>SOLUTION</summary>

**Mixed pattern:** *Greedy* (most-frequent task pehle schedule) + *math formula* (frequency counting).
```python
import sys
from collections import Counter
def solve():
    tasks = sys.stdin.readline().strip().split()[0]
    n = int(sys.stdin.readline())
    freq = Counter(tasks)
    max_f = max(freq.values())
    count_max = sum(1 for v in freq.values() if v == max_f)
    # formula: gaps banao most-frequent ke around
    ans = max(len(tasks), (max_f - 1) * (n + 1) + count_max)
    print(ans)
solve()
```
**Kyun mixed:** greedy intuition + combinatorial formula. O(T). (LeetCode 621 Task Scheduler.)
</details>

## MX3 — "Cheapest Flights (≤ K stops)" [Hard · Graph + DP]
**n** cities, flights list `[u, v, price]`. `src` se `dst` jaana hai **at most K stops** me. Minimum
cost batao (nahi to -1).
**Constraints:** 1 ≤ n ≤ 100 · 0 ≤ K < n.
<details><summary>SOLUTION</summary>

**Mixed pattern:** *Graph* + *DP over stops* (bounded Bellman-Ford — K+1 relaxations).
```python
import sys
def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    flights = []
    for _ in range(m):
        u,v,p = int(data[idx]),int(data[idx+1]),int(data[idx+2]); idx+=3
        flights.append((u,v,p))
    src, dst, K = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    INF = float('inf')
    dist = [INF]*n; dist[src] = 0
    for _ in range(K+1):                        # at most K stops = K+1 edges
        newd = dist[:]
        for u,v,p in flights:
            if dist[u] != INF and dist[u]+p < newd[v]:
                newd[v] = dist[u]+p
        dist = newd                             # ★ round ke END me update (K-stops bound sahi rahe)
    print(dist[dst] if dist[dst] != INF else -1)
solve()
```
**Kyun mixed:** graph shortest-path par "K stops" constraint → DP layer (edges count bound). O(K·E). (LeetCode 787.)
</details>

## MX4 — "Distinct Flavors Window" [Medium · Sliding Window + Hashing]
Ice-cream flavors ki array. **Kitne subarrays** hain jinme **at most K distinct** flavors hain?
<details><summary>SOLUTION</summary>

**Mixed pattern:** *Sliding window* + *hashmap* (count trick).
```python
import sys
from collections import defaultdict
def at_most_k(arr, k):
    freq = defaultdict(int); left = 0; total = 0
    for right in range(len(arr)):
        freq[arr[right]] += 1
        while len(freq) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0: del freq[arr[left]]
            left += 1
        total += right - left + 1               # naye subarrays ending at right
    return total
# exactly K = at_most_k(arr,K) - at_most_k(arr,K-1)
```
**Kyun mixed:** window shrink (sliding) + distinct-count (hash) + counting trick. O(N).
</details>

---
# ⏱️ REAL EXAM SIMULATOR — 180-min mock kaise doon (bilkul asli jaisa)
1. **Setup:** phone dusre kamre me. Laptop pe ek code editor (VS Code / online judge). Ek stopwatch
   180:00 pe. Paani + govt-ID paas (real jaisa habit).
2. **Rules (strict):** NO google, NO ChatGPT, NO copy-paste. Sirf language docs allowed (jaise real).
   Tab switch mat karna (real me violation hota).
3. **Attempt:** ek mock set (SET 1-5 me se) kholo — sirf problem statements dekho, solutions COLLAPSED rakho.
   - Pehle 10 min: teeno padho, Q1 (easy) se start.
   - Har Q: brute force → sample cases test → optimize → edge cases (empty, 1, max N, negative).
   - Time-box: ~55 min/question max. Stuck → partial likho, aage badho.
4. **Submit-simulation:** har Q ke apne 2-3 test cases khud banao aur run karo (hidden cases jaisa).
5. **Review (mock ke baad):** solutions kholo, apna approach compare karo, jo miss hua wo "mistakes
   log" me likho. 2 din baad wahi pattern dobara.
6. **Kitne mocks:** test se pehle **kam se kam 3-4 full mocks** (SET 1→5). Har mock ke baad familiar
   badhta jayega — real test din pe "arey ye to dekha hua hai" wali feeling aayegi.

> HONEST: ye exact same questions guarantee nahi (koi nahi de sakta). Par ye **real reported patterns +
> layered problems + timed sim** hain — isse test **familiar** lagega, ajeeb/surprise nahi. Yahi asli edge.
