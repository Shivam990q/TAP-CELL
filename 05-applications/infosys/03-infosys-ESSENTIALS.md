# Infosys Test — ESSENTIALS (zero gaps: har chhoti detail jo test me chahiye)

> 🔖 **PROVENANCE:** Ye file ~90% **[AI-EXPLANATION]** — standard CS/DSA knowledge (data structures,
> patterns, complexity, Python) jo AI ne apne words + real-life analogy me samjhaya. Concepts universal
> hain (kisi ek source ke nahi). Legend: `README.md` → PROVENANCE INDEX.

> Iska maqsad: tere "data" me koi hole na rahe. Patterns + solutions alag files me hain.
> Ye file wo **plumbing + trigger + trap** cover karti hai jo pehli baar coding karne wale ko
> pata hi nahi hoti — aur wahi test me marwa deti hai. Ek baar padh le, phir kuch "naya" nahi lagega.
>
> Language: **Python 3** (test me sabse kam likhna padta, sabse kam bugs). **Java tera strong hai aur
> test me allowed hai → neeche file ke END me "APPENDIX: JAVA CHEAT-SHEET" add kar diya** (fast I/O +
> collections + comparator + pattern templates + Java-specific gotchas). Ek language chuno, dono me confuse mat ho.
>
> 🎓 **Agar DSA ka Z bhi nahi pata → SEEDHA neeche "DSA FROM ZERO" section (Part A/B/C) padho pehle.**
> Wahan har data-structure aur pattern real-life analogy se zero se samjhaya hai. Uske baad ye upar
> waala plumbing + `06-SOLUTIONS.md` sab samajh aayega.

---
# 0. SABSE PEHLE — test kaise chalta hai (mechanics)
- Online judge me tujhe **stdin se input** milta hai, **stdout pe output** dena hota hai (ya ek function complete karna hota hai — dono format aate hain).
- **Partial scoring:** har question ke peeche hidden test cases hote hain. Jitne pass, utne marks. Poora solve na ho to bhi jitne cases pass = marks.
- **Time Limit (TLE):** har case ka time limit hota hai (~1-2 sec). Slow algo = TLE = 0 us case pe. Isiliye complexity matter karti hai.
- **Compile/Runtime error = us submission pe 0** us case pe. Isliye edge cases handle karo.
- Strategy: pehle **brute force** likho (kuch cases pass honge = marks), phir optimize.

---
# 1. PYTHON — poora cheat sheet (jo bhi chahiye test me)

## 1.1 Input padhna (ye 90% log yahin atakte hain)
```python
import sys
input = sys.stdin.readline           # fast input (bade input ke liye zaroori)

n = int(input())                     # ek integer
a, b = map(int, input().split())     # ek line me do integer
arr = list(map(int, input().split()))# ek line me poora array
s = input().strip()                  # string (newline hatane ko strip)

# multiple lines / n lines padhna:
grid = [list(map(int, input().split())) for _ in range(n)]

# saara input ek saath (jab lines ka count pata na ho):
data = sys.stdin.read().split()
```
> ★ Trap: normal `input()` bade inputs pe SLOW hai → TLE. Upar wala `sys.stdin.readline` use karo.

## 1.2 Output dena
```python
print(ans)                           # normal
print(*arr)                          # array space-separated: 1 2 3
print('\n'.join(map(str, arr)))      # har element nayi line pe
sys.stdout.write(str(ans) + '\n')    # fast output (bahut output ho to)
```

## 1.3 Data structures (Python me ready-made)
```python
# List (dynamic array)
a = []; a.append(x); a.pop(); a[-1]; a.sort(); a.sort(reverse=True)

# Dict (HashMap)
d = {}; d[key] = val; d.get(key, 0); key in d
from collections import defaultdict, Counter
d = defaultdict(int)                 # missing key = 0 (frequency ke liye best)
freq = Counter(arr)                  # {element: count} ek line me

# Set (unique + O(1) lookup)
s = set(); s.add(x); x in s; s.discard(x)

# Stack = list (append/pop)
# Queue / Deque
from collections import deque
q = deque(); q.append(x); q.popleft(); q.appendleft(x); q.pop()

# Heap (min-heap by default)
import heapq
h = []; heapq.heappush(h, x); heapq.heappop(h); h[0]  # top (smallest)
# Max-heap: values ko negative karke daalo → -heapq.heappop(h)
```

## 1.4 Sorting + custom comparator
```python
arr.sort()                           # ascending
arr.sort(reverse=True)               # descending
arr.sort(key=lambda x: x[1])         # tuple ke 2nd element pe
pairs.sort(key=lambda p: (p[0], -p[1]))   # multi-key: p0 asc, p1 desc
# Full custom (jaise Largest Number):
from functools import cmp_to_key
arr.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
```

## 1.5 String ops
```python
s[::-1]                # reverse
s.isalnum(); s.lower(); s.upper()
''.join(list_of_chars) # list ko string banao
s.split(','); s.replace('a','b'); s.count('a')
ord('a'); chr(97)      # char <-> int (ASCII)
# frequency: Counter(s)
```

## 1.6 Math essentials
```python
import math
math.gcd(a, b)         # GCD
a // b                 # integer division (★ / float deta hai, // int)
a % b                  # modulo (negative pe dhyan)
pow(a, b)              # a^b   |   pow(a, b, m) = a^b mod m (fast, bade numbers)
float('inf'); float('-inf')   # infinity (min/max init ke liye)
math.isqrt(n)          # integer square root
```

---
# 2. CONSTRAINTS → KONSA ALGO (ye table test me algo chun-ne me help karega)
> Problem me "N ≤ ..." dekho, phir ye table se decide karo kaunsa approach chalega (warna TLE).

| N (input size) | Allowed complexity | Kaunse algo |
| --- | --- | --- |
| N ≤ 10-12 | O(2^N), O(N!) | Backtracking, permutations, brute subsets |
| N ≤ 100 | O(N^3) | 3 nested loops, some DP |
| N ≤ 1000-2000 | O(N^2) | 2D DP (LCS/Edit), nested loops |
| N ≤ 10^5 | O(N log N) | Sorting, heap, binary search, most greedy |
| N ≤ 10^6-10^7 | O(N) ya O(N log N) | Single pass, sliding window, prefix, hashing |
| N ≥ 10^9 (value) | O(log N) ya O(1) | Binary search on answer, math formula |
> ★ Rule: **N bada = O(N²) mat likho.** Constraint dekh ke algo chuno, phir code.

---
# 3. UNIVERSAL PROBLEM-SOLVING TEMPLATE (har question pe ye 6 steps)
1. **Padho + example dry-run:** input/output samajh, ek example haath se karo.
2. **Constraints dekho:** N kitna? → Section 2 se target complexity nikaalo.
3. **Pattern pehchano:** Section 4 ke triggers se — "ye keyword = ye pattern."
4. **Brute force sochо:** pehle simplest (kuch cases pass = marks). 
5. **Optimize:** pattern lagao (HashMap/two-pointer/DP/etc.).
6. **Edge cases test karo:** Section 5 checklist. Phir submit.

---
# 4. PATTERN TRIGGERS (problem me YE dikhe → YE pattern use karo)
> Ye sabse important table hai — pattern pehchan-na hi asli skill hai.

| Problem me ye dikhe / poochhe | Pattern |
| --- | --- |
| "two numbers sum to target", "seen before?", "count pairs" | **HashMap** |
| "sorted array", "pair from both ends", "in-place rearrange" | **Two Pointers** |
| "longest/shortest substring/subarray with condition" | **Sliding Window** |
| "sorted + find/position", "minimize the maximum", "N ≥ 10^9" | **Binary Search** |
| "maximum subarray sum (contiguous)" | **Kadane** |
| "max/min with choices at each step", "intervals", "schedule" | **Greedy** |
| "in how many ways", "min/max cost to reach", "choose/skip" | **DP** |
| "subsequence", "two strings compare" | **2D DP (LCS-type)** |
| "coins/items to make target", "subset sum" | **Knapsack DP** |
| "grid connected cells", "islands", "shortest steps to spread" | **DFS/BFS** |
| "dependencies/order/prerequisite", "cycle?" | **Topological sort** |
| "next greater/smaller element" | **Monotonic Stack** |
| "top K", "K-th largest/smallest", "merge K" | **Heap** |
| "matching brackets/nesting", "undo/last" | **Stack** |
| "weighted shortest path" | **Dijkstra** |
| "XOR", "unique among pairs", "bits" | **Bit manipulation** |
| "generate all combinations/permutations/subsets" | **Backtracking** |

---
# 5. EDGE CASES — universal checklist (ye miss = test cases fail)
Har problem submit se pehle ye soch:
- [ ] **Empty input** (n=0, empty array/string) — code crash to nahi karega?
- [ ] **Single element** (n=1)
- [ ] **All same elements** / all zero / all negative
- [ ] **Already sorted / reverse sorted**
- [ ] **Duplicates** present
- [ ] **Maximum size** (N max) — TLE to nahi? overflow to nahi?
- [ ] **Negative numbers** (modulo, sum, comparison me dhyan)
- [ ] **Integer overflow** — Python me overflow nahi hota (bada +ve), par logic me dhyan; Java/C++ me `long` use karo
- [ ] **First/last element** boundary (loop range sahi hai?)

---
# 6. COMMON BUGS / TRAPS (jo pehli baar wale karte hain)
- **Off-by-one:** loop `range(n)` vs `range(1, n)`, `<=` vs `<` in binary search. Dry-run se pakdo.
- **Integer division:** Python me `/` float deta hai (5/2 = 2.5), `//` int (5//2 = 2). Index me `//` use karo.
- **Mutable default / shared reference:** `[[0]*n]*m` galat hai (saari rows same object). Sahi: `[[0]*n for _ in range(m)]`.
- **Modifying list while iterating:** loop ke andar list se remove mat karo — naya list banao.
- **Recursion depth:** Python default ~1000. Bada recursion → `import sys; sys.setrecursionlimit(10**6)`.
- **Global vs local:** nested function me bahar ki variable change karni ho → `nonlocal`.
- **Comparison chain:** `a == b == c` Python me chalta hai par confuse mat ho.
- **String immutability:** string ko index se change nahi kar sakte; list banao (`list(s)`), change karo, `''.join`.

---
# 7. COMPLEXITY (Big-O) — 30-second refresher
- O(1) constant · O(log n) binary search · O(n) single loop · O(n log n) sorting ·
  O(n²) nested loops · O(2^n) subsets · O(n!) permutations.
- **Space bhi count hoti hai** — extra array/hashmap = O(n) space.
- Interview me hamesha bolo: "Ye O(...) time, O(...) space hai." Ye impress karta hai.

---
# 8. TEST-DAY MICRO-CHECKLIST (code likhne ka order)
1. Input padhne ka code sahi likho (Section 1.1) — yahin log time waste karte hain.
2. Q1 (easy) pehle FULL — saare cases pass karo, 20 marks bank.
3. Q2/Q3 pe brute force → jitne cases nikle. Phir optimize.
4. Har submit se pehle edge cases (Section 5) mann me chala lo.
5. TLE aaye → Section 2 dekho, better complexity waala algo lagao.
6. **Tab switch mat karna** (auto violation). Sab kuch judge ke andar hi.

---
> Bhai, ab tere "data" me poori plumbing aa gayi: input/output, STL, algo-selection, pattern-triggers,
> edge cases, traps. Ye + SOLUTIONS file ke 12 patterns = **test me kuch bhi "pehli baar" nahi lagega.**
> Tera kaam: samajh (tere liye ek pass kaafi), aur khel jaa. 🔥


---
---
# 🎓 DSA FROM ZERO — bilkul shuru se (agar DSA ka Z bhi nahi pata, ye padh)
> Ye section maan ke chalta hai ki tune kabhi DSA nahi kiya. Har cheez **real-life analogy** se
> samjhayi hai — ek baar padh, samajh aa jayega. Iske baad `06-SOLUTIONS.md` ka har solution samajh aayega.

## 🧠 Part A — Time Complexity (Big-O) zero se
**Kya hai:** "jaise-jaise input (N) bada hota hai, code kitna DHEELA hota hai" — uska naap. Seconds nahi,
**operations count** ki growth. Test me isse decide hota hai code TLE (time-limit-exceed) hoga ya nahi.

**Analogy:** ek kitaab me naam dhoondna —
- **O(1)** = index pata hai, seedha khol liya. (data bade to bhi time same). Fastest.
- **O(log N)** = dictionary/phonebook me aadha-aadha karke dhoondna (binary search). Bahut fast.
- **O(N)** = har page ek-ek karke dekhna (ek loop). Theek.
- **O(N log N)** = sort karna. Acceptable for N up to 10^5-10^6.
- **O(N²)** = har naam ke liye poori kitaab dobara dekhna (loop andar loop). **N bada to SLOW/TLE.**
- **O(2^N) / O(N!)** = saari possibilities try karna. Sirf chhote N (≤ 20) pe.

**Rule (yaad rakh):** N ≤ 10^5 dikhe → O(N) ya O(N log N) chahiye. N² mat likhna. (Table Section 2 me.)

---
## 📦 Part B — Data Structures zero se (kya + analogy + kab + Python)

**1. Array / List** — *cheezein ek line me, index se.*
- Analogy: lockers ki ek row (locker 0,1,2...). Index se seedha kholo = O(1).
- Kab: jab order matter kare, ya index se access chahiye.
- Python: `a = [10,20,30]; a[0]; a.append(40); a.sort()`

**2. HashMap / Dictionary (dict)** — *naam → value, instant.*
- Analogy: phonebook — naam do, number turant milta (poori list nahi dhoondni). Lookup = O(1).
- Kab: "kitni baar aaya" (frequency), "pehle dekha kya", "value → index". **Sabse zyada use hota.**
- Python: `d = {}; d["a"] = 5; d.get("a",0); "a" in d` · frequency: `Counter(arr)`

**3. Set** — *sirf "hai ya nahi", duplicates nahi.*
- Analogy: guest list — naam hai ya nahi, bas. Duplicate nahi rakhta. Check = O(1).
- Kab: unique elements, "already seen?", duplicates hatana.
- Python: `s = set(); s.add(3); 3 in s`

**4. Stack** — *plates ki dher — LIFO (Last In First Out).*
- Analogy: plate dher — jo AAKHRI rakhi wahi PEHLE niklegi.
- Kab: brackets matching, "pichhla/undo", next-greater-element.
- Python: list se — `st = []; st.append(x); st.pop(); st[-1]` (top).

**5. Queue** — *line/katar — FIFO (First In First Out).*
- Analogy: ticket line — jo PEHLE aaya wahi PEHLE nikla.
- Kab: BFS (level-by-level), "shortest steps".
- Python: `from collections import deque; q = deque(); q.append(x); q.popleft()`

**6. Heap (Priority Queue)** — *hamesha sabse chhota/bada top pe.*
- Analogy: hospital emergency — jiski priority sabse zyada wo pehle, chahe baad me aaya ho.
- Kab: "top-K", "K-th largest/smallest", "min/max baar-baar chahiye".
- Python: `import heapq; h=[]; heapq.heappush(h,x); heapq.heappop(h)` (min top). Max ke liye `-x` daalo.

**7. Tree (Binary Tree)** — *ulta ped — ek root, har node ke 2 bachche.*
- Analogy: family tree / company org-chart — ek boss (root), neeche branches.
- Kab: hierarchy, BST (sorted structure), traversals.
- Node: `class Node: def __init__(self,v): self.val=v; self.left=None; self.right=None`

**8. Graph** — *cities + roads / friend-network.*
- Analogy: sheher aur unhe jodne wali sadkein (nodes + edges).
- Kab: "connected?", "shortest path", "islands", "dependencies".
- Python: `graph = defaultdict(list); graph[u].append(v)` (adjacency list).

**9. Linked List** — *treasure hunt — har node me agle ka pata.*
- Analogy: ek parchi me agli parchi ka address. Index se nahi, chal ke jaana padta.
- Kab: insert/delete fast chahiye, ya interview me explicitly.
- Node: `class Node: def __init__(self,v): self.val=v; self.next=None`

> 💡 90% Q1/Q2 problems sirf **Array + HashMap + Set + Two-pointer** se ho jaate. Ye 4 sabse pehle pakdo.


---
## 🧩 Part C — 15 PATTERNS zero se (kya + analogy + kab + kaise + mini example)
> Har pattern = ek "sochne ka tarika". Problem me trigger dikhe → ye pattern lagao. Ek baar samajh
> gaye to us pattern ke SAARE problems ek jaise lagenge. Full code `06-SOLUTIONS.md` me.

**P1. HashMap Lookup** — *"pehle dekha hua yaad rakho".*
- Kab: "do cheezein jodo = target", "kitni baar", "duplicate?".
- Kaise: ek dict me chalte-chalte store karo; har naye pe check karo pehle aaya kya.
- Mini: Two Sum — har num pe dekho `target-num` dict me hai? → O(N). (`06` #1)

**P2. Two Pointers** — *"dono sire se andar chalo".*
- Kab: **sorted** array, palindrome, "in-place rearrange", pair-from-ends.
- Kaise: ek pointer left(0), ek right(end); condition ke hisaab se andar lao.
- Mini: Palindrome — left/right char compare, andar badho. (`06` #6)

**P3. Sliding Window** — *"ek khidki jo aage khiskti hai".*
- Kab: "longest/shortest **substring/subarray** with kuch condition".
- Kaise: right se window badhao; condition toote to left se chhota karo; best track karo.
- Mini: bina-repeat longest substring — window me duplicate aaya to left khisakao. (`06` #12)

**P4. Binary Search** — *"aadha-aadha kaat ke dhoondo".*
- Kab: **sorted** data me find; ya "minimize the maximum / maximize the minimum"; ya N ≥ 10^9.
- Kaise: lo, hi; mid dekho; aadha phenk do har step. O(log N).
- Mini: sorted array me target ka index. (`06` #10). Advanced: "answer pe" binary search (Painter's, `06` R2).

**P5. Kadane** — *"negative ho to reset".*
- Kab: "maximum sum wala **contiguous** subarray".
- Kaise: running sum jodo; agar sum negative ho gaya to 0 se restart; max track.
- Mini: Max Subarray. (`06` #3)

**P6. Greedy** — *"abhi ka best choice, aage ka mat socho".*
- Kab: "max/min", "intervals/schedule", "sort karke choose".
- Kaise: usually SORT karo (kisi cheez pe), phir har step locally-best pick.
- Mini: activity selection — jaldi khatam hone wala pehle. (`06` #22). Interval → end pe sort.

**P7. 1D DP (choose / skip)** — *"har step 2 choice, best yaad rakho".*
- Kab: "kitne tareeke", "min/max to reach", "adjacent nahi le sakte".
- Kaise: dp[i] = pichhle results se banao (dp[i-1], dp[i-2]...). Ek array me answers store.
- Mini: House Robber — dp[i] = max(chhodo dp[i-1], lo arr[i]+dp[i-2]). (`06` #16)

**P8. Knapsack DP** — *"target banane ke liye items choose".*
- Kab: "coins/items se sum/amount banao", "subset with sum".
- Kaise: dp[amount] = items try karke fill. 0/1 (ek baar) vs unbounded (baar-baar).
- Mini: Coin Change — dp[amt] = min(dp[amt], dp[amt-coin]+1). (`06` #17)

**P9. 2D Grid DP** — *"table bharke answer".*
- Kab: "do strings compare (subsequence/edit)", "grid me paths/min-cost".
- Kaise: dp[i][j] = neighbours (upar/left/diagonal) se banao. Match → diagonal+1.
- Mini: LCS — match `dp[i-1][j-1]+1`, warna `max(left,up)`. (`06` #26)

**P10. DFS / BFS (Graph/Grid)** — *"connected cheezein explore karo".*
- Kab: "grid islands", "connected?", "shortest steps to spread/reach".
- Kaise: DFS = recursion (gehrai me); BFS = queue (level-by-level, shortest ke liye). Visited mark karo.
- Mini: Number of Islands — '1' mila to DFS se poora island '0' kar do, count++. (`06` #30)

**P11. Topological Sort** — *"pehle wala kaam pehle".*
- Kab: "dependencies/prerequisites", "order banao", "cycle hai kya?".
- Kaise: indegree 0 wale process karo (BFS/Kahn), unke padosi ka indegree ghatao.
- Mini: Course Schedule — prerequisites graph, cycle ho to impossible. (`06` #32)

**P12. Monotonic Stack** — *"stack jo increasing/decreasing rakhta".*
- Kab: "**next greater / smaller** element", "histogram".
- Kaise: stack me indices rakho; naya bada aaye to pichhle chhote resolve karo.
- Mini: Next Greater Element. (`06` #34)

**P13. Heap / Top-K** — *"priority se nikaalo".*
- Kab: "top-K", "K-th largest/smallest", "merge K lists".
- Kaise: size-K heap rakho (K-th largest ke liye MIN-heap). Bada aaye to top nikaal do.
- Mini: Kth Largest — size-k min-heap ka top. (`06` #36)

**P14. Backtracking** — *"try karo → nahi bana to undo → dusra try".*
- Kab: "saare combinations/permutations/subsets banao".
- Kaise: choose → recurse → **un-choose (undo)**. Recursion tree.
- Mini: Subsets — har element lo/chhodo, recurse. (`06` #41)

**P15. Bit Manipulation** — *"0/1 bits ke tricks".*
- Kab: "XOR", "unique among pairs", "set/count bits", "subsets via bitmask".
- Kaise: XOR (x^x=0, x^0=x) → duplicates cancel; `&`,`|`,`<<` bit ops.
- Mini: Single Number — sabko XOR karo, akela bacha. (`06` #40)

---
## 🗺️ Part D — Zero-DSA roadmap (kis order me seekhna)
1. **Complexity** (Part A) — bas itna ki N dekh ke algo chun sako.
2. **Array + HashMap + Set + Two-pointer** (P1, P2) — Q1 ka 80% yahi.
3. **Sliding Window + Binary Search + Kadane** (P3, P4, P5).
4. **Greedy** (P6) — Q2 ke liye.
5. **DP** (P7, P8, P9) — Q3 ke liye (Aditya Verma playlist + `06` dekhо).
6. **Graph/Stack/Heap/Backtracking/Bit** (P10-P15) — SP edge + interview.
> Har pattern: ye analogy padho → `06-SOLUTIONS.md` me us pattern ke 2-3 problems samajh → `09-MOCK` me timed try.
> Zero se yahan tak: **Part A→B→C** ek baar dhyan se = tu problems samajhne layak ho jayega. Phir practice.


---
---
# ☕ APPENDIX: JAVA CHEAT-SHEET (agar Java me dena hai — tera strong language)
> Python vs Java: **Python** = kam likhna, kam bugs (recommended agar dono barabar aate). **Java** = tez
> execution, tera comfort. Jo choose karo, **usi ek me** poora test do. Neeche Java ka poora "plumbing"
> hai — fast I/O + collections + comparator + templates + gotchas. Ye Section 1 (Python) ka Java mirror hai.

## J1. Fast I/O (★ Scanner SLOW hai — BufferedReader use karo, warna bade input pe TLE)
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();               // output buffer (fast)

        int n = Integer.parseInt(br.readLine().trim());       // ek int
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());             // ek line me do int
        int b = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];                               // poora array ek line se
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());

        long ans = 0; // ... compute ...
        sb.append(ans).append('\n');
        System.out.print(sb);                                 // ★ ek hi baar print (loop me print = slow)
    }
}
```
> ★ Trap: `Scanner` chhote input pe theek, bade pe SLOW → `BufferedReader + StringTokenizer` use karo.
> Output loop me `System.out.println` mat karo — `StringBuilder` me jodo, ant me ek baar print.

## J2. Data structures (Java collections — Python STL ka mirror)
```java
List<Integer> list = new ArrayList<>();   list.add(x); list.get(i); list.size(); Collections.sort(list);
Map<Integer,Integer> map = new HashMap<>(); map.put(k,v); map.getOrDefault(k,0); map.containsKey(k);
map.merge(k, 1, Integer::sum);                          // frequency count (defaultdict jaisa)
Set<Integer> set = new HashSet<>();       set.add(x); set.contains(x); set.remove(x);
Deque<Integer> stack = new ArrayDeque<>(); stack.push(x); stack.pop();  stack.peek();   // STACK (LIFO)
Deque<Integer> queue = new ArrayDeque<>(); queue.offer(x); queue.poll(); queue.peek();  // QUEUE (FIFO)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();                       // min-heap (default)
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // max-heap
TreeMap<Integer,Integer> tm = new TreeMap<>();          // sorted map (floorKey/ceilingKey — ordered ops)
```
> `ArrayDeque` = stack aur queue dono (Stack class purana/slow, mat use karo). `PriorityQueue` = heap.

## J3. Sorting + custom comparator
```java
Arrays.sort(arr);                                       // int[] ascending
Arrays.sort(arr2D, (x, y) -> x[0] - y[0]);              // 2D array, first col pe (overflow safe: Integer.compare)
list.sort((x, y) -> Integer.compare(y, x));             // descending (list)
list.sort(Comparator.comparingInt(p -> p[1]));          // key = 2nd element
// Largest Number (concat comparator):
String[] s = ...; Arrays.sort(s, (x, y) -> (y + x).compareTo(x + y));
```
> ★ Comparator me `a - b` overflow kar sakta (bade ints) → `Integer.compare(a, b)` safe hai.

## J4. String / char / math
```java
StringBuilder sb = new StringBuilder(); sb.append(c); sb.reverse(); sb.toString();  // string build (immutable trap se bacho)
char[] ch = s.toCharArray();  String t = new String(ch);
int d = c - '0';           // char digit -> int      |    int idx = c - 'a';   // letter -> 0..25
s.charAt(i); s.length(); s.substring(i, j); s.equals(t);   // ★ .equals, == NAHI (strings)
long g = java.math.BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).longValue(); // ya khud Euclid gcd
long INF = Long.MAX_VALUE / 4;   int II = Integer.MAX_VALUE;   // init for min-finding
```

## J5. ★ JAVA-SPECIFIC GOTCHAS (yahin log marte hain — Python me ye nahi hote)
- **Integer overflow (#1 bug):** `int` max ≈ 2.1×10^9. Sum/product overflow ho jaata → **`long` use karo**
  (jaise prefix-sum, `a*b`). Python me overflow nahi hota; **Java me hota** — bade constraints pe dhyan.
- **`Arrays.sort(int[])` worst-case O(n²)** (dual-pivot quicksort ko adversarial input TLE kara sakta) →
  agar anti-test ka risk ho to **`Integer[]` box karke** sort (mergesort, guaranteed O(n log n)).
- **`==` vs `.equals()`:** objects (String, Integer) value-compare = `.equals()`. `==` reference dekhta.
  Integer cache (−128..127) me `==` "chalta dikhta" par bade numbers pe fail — hamesha `.equals()`.
- **2D array:** `int[][] dp = new int[m][n];` — rows independent (Python ka `[[0]*n]*m` shared-row trap Java me NAHI).
- **Array default values:** `int[]`=0, `boolean[]`=false, `long[]`=0. Custom init: `Arrays.fill(dp, -1);`.
- **Recursion depth:** Java stack ~10^4–10^5 frames; deep recursion → `StackOverflowError`. Bada ho to iterative karo.
- **Integer division:** `5/2 = 2` (int), `5.0/2 = 2.5`. Mid overflow-safe: `lo + (hi - lo) / 2`.

## J6. Pattern templates (Java — Section 4 ke patterns ka mirror)
```java
// Two pointers (sorted array)
int i = 0, j = n - 1;
while (i < j) { /* condition dekho, i++ ya j-- */ }

// Sliding window (variable size)
int left = 0, best = 0;
for (int right = 0; right < n; right++) {
    // window me arr[right] add karo
    while (/* window invalid */) { /* arr[left] remove; */ left++; }
    best = Math.max(best, right - left + 1);
}

// Binary search
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;              // overflow-safe
    if (a[mid] == target) return mid;
    else if (a[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}

// 1D DP (choose/skip — House Robber style)
long[] dp = new long[n + 1];
for (int i = 1; i <= n; i++)
    dp[i] = Math.max(dp[i - 1], (i >= 2 ? dp[i - 2] : 0) + arr[i - 1]);

// Graph BFS (queue)
Deque<Integer> q = new ArrayDeque<>(); q.offer(src);
boolean[] vis = new boolean[n]; vis[src] = true;
while (!q.isEmpty()) {
    int node = q.poll();
    for (int nb : adj.get(node)) if (!vis[nb]) { vis[nb] = true; q.offer(nb); }
}
```

> ☕ Java me poora test dena ho to: **BufferedReader I/O + `long` for sums + ArrayDeque/PriorityQueue +
> Integer.compare comparator** — bas itna yaad rahe to koi language-bug nahi aayega. Baaki logic
> (`06-SOLUTIONS.md` ke 55 solutions) same hai — sirf syntax Python→Java translate karna hai.
