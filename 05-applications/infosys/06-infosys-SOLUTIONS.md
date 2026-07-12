# Infosys Goldmine — FULL SOLUTIONS (har question ka answer + logic + pattern)

> 🔖 **PROVENANCE:** Problems ka origin = LeetCode-canonical / real-PYQ (`05` SOURCE MAP me har # ka
> exact source). **Har solution ka code + Hinglish "Samajh" = [AI-EXPLANATION]** (AI ne likha/samjhaya).
> Tier 5 (R1-R13) = [REAL-PYQ] (source inline). Tags legend: `README.md` → PROVENANCE INDEX.

> Ye file `05-infosys-QUESTION-BANK.md` ke 40-problem GOLDMINE ka **poora solution** hai.
> Language: **Python** (padhne/samajhne me sabse clean; logic Java/C++ me same rahega).
> Har problem ka format: **Pattern → Samajh (approach) → Code → Complexity → Key insight.**
>
> Kaise use karo: pehle "Samajh" padho, khud sochne ki koshish karo 2 min, phir code dekho.
> Ratna nahi — **pattern** pakdo. Ek pattern 10+ problems me kaam aata hai.
>
> 🎓 **Koi data-structure/pattern samajh na aaye (HashMap/Sliding Window/DP kya hai)? → pehle
> `03-infosys-ESSENTIALS.md` ka "DSA FROM ZERO" (Part A/B/C) padho — sab analogy se zero se samjhaya hai.**
>
> Pattern-count: Tier 1 me sirf ~6 core patterns hain (HashMap, Two-pointer, Sliding Window,
> Binary Search, 1D-DP, Greedy). Ye 6 samajh gaye = aadha kaam ho gaya.

---
# 🟢 TIER 1 — DSE LOCK (ye 20 pakka). Q1 full + Q2/Q3 partial.

## 1. Two Sum — Easy
**Pattern:** HashMap (complement lookup)
**Samajh:** Har number ke liye chahiye `target - num`. Ek dictionary me "kya-kya dekha" store karo;
har step pe check karo complement pehle aa chuka kya.
```python
def twoSum(nums, target):
    seen = {}                      # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
```
**Complexity:** O(n) time, O(n) space.
**Key insight:** "Pehle dekha hua yaad rakho" — HashMap se O(n²) → O(n).

## 2. Best Time to Buy and Sell Stock — Easy
**Pattern:** Single pass, track minimum
**Samajh:** Ab tak ka sabse sasta din yaad rakho; har din pe check karo "aaj bechu to kitna profit."
```python
def maxProfit(prices):
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)     # sabse sasta buy day
        best = max(best, p - min_price)   # aaj bechne ka profit
    return best
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** Buy low pehle aana chahiye sell se — isliye min ko continuously update karo.

## 3. Maximum Subarray (Kadane's) — Easy/Medium
**Pattern:** Kadane (running sum, reset on negative)
**Samajh:** Chalte-chalte sum jodo; agar running sum negative ho gaya to use phenk do (0 se restart),
kyunki negative aage ka sum ghatayega hi.
```python
def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)   # ya to naya start, ya jodo
        best = max(best, cur)
    return best
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** "cur + x vs x" — yahi Kadane ka dil hai.

## 4. Majority Element — Easy
**Pattern:** Moore's Voting
**Samajh:** Majority (>n/2) element baaki sabko "cancel" kar deta hai. Count badhao same pe, ghatao alag pe;
count 0 hua to naya candidate.
```python
def majorityElement(nums):
    count = 0
    candidate = None
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** Majority element cancellation survive karta hai — genius trick.

## 5. Valid Anagram — Easy
**Pattern:** Frequency count
**Samajh:** Anagram matlab dono me same letters same count me. Frequency compare karo.
```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    from collections import Counter
    return Counter(s) == Counter(t)
```
**Complexity:** O(n) time, O(1) space (26 letters).
**Key insight:** Counting = anagram/permutation problems ka default hathiyar.

## 6. Valid Palindrome — Easy
**Pattern:** Two pointers
**Samajh:** Do pointer — ek aage se, ek peeche se; non-alphanumeric skip karo, compare karo.
```python
def isPalindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1; j -= 1
    return True
```
**Complexity:** O(n) time, O(n) space (clean karne me).
**Key insight:** Palindrome/reverse = two-pointer (dono sire se andar).

## 7. Remove Duplicates from Sorted Array — Easy
**Pattern:** Two pointers (slow/fast), in-place
**Samajh:** Sorted hai to duplicate paas-paas honge. `slow` unique tak likhta hai, `fast` scan karta hai.
```python
def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1                 # nayi length
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** In-place = slow/fast pointer. (★ Infosys PYQ.)

## 8. Move Zeroes — Easy
**Pattern:** Two pointers (slow = insert position)
**Samajh:** Non-zero ko aage bhar do `slow` pe; baaki ko 0 se fill karo. Ya swap karo.
```python
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** "Achhe elements ko aage pack karo" — partition pattern.

## 9. Merge Sorted Array — Easy
**Pattern:** Two pointers from the END
**Samajh:** nums1 ke end me space hai. Peeche se bada element bharo (taaki overwrite na ho).
```python
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]; i -= 1
        else:
            nums1[k] = nums2[j]; j -= 1
        k -= 1
```
**Complexity:** O(m+n) time, O(1) space.
**Key insight:** Overwrite bachane ke liye peeche se bharo.

## 10. Binary Search — Easy
**Pattern:** Binary search (sorted → half karo)
**Samajh:** Sorted array me mid dekho; chhota hai to right jao, bada hai to left.
```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```
**Complexity:** O(log n) time, O(1) space.
**Key insight:** `lo <= hi` aur `mid±1` — off-by-one se bacho. Ye pattern 10+ problems me.

## 11. Search Insert Position — Easy
**Pattern:** Binary search (lower bound)
**Samajh:** Wahi binary search; na mile to `lo` hi insert position hoti hai.
```python
def searchInsert(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```
**Complexity:** O(log n) time, O(1) space.
**Key insight:** "lower bound" = pehli position jahan value >= target.

## 12. Longest Substring Without Repeating Characters — Medium
**Pattern:** Sliding window + set/map
**Samajh:** Window expand karo right se; duplicate aaya to left se shrink karo jab tak duplicate hat na jaaye.
```python
def lengthOfLongestSubstring(s):
    seen = {}                    # char -> last index
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1   # window ko duplicate ke aage le jao
        seen[c] = right
        best = max(best, right - left + 1)
    return best
```
**Complexity:** O(n) time, O(min(n,charset)) space.
**Key insight:** "Longest/shortest substring with condition" = sliding window. Bahut aata hai.

## 13. Subarray Sum Equals K — Medium
**Pattern:** Prefix sum + HashMap
**Samajh:** Running sum rakho. Agar `runningSum - k` pehle dikha hai, to beech me ek subarray = k tha.
```python
def subarraySum(nums, k):
    from collections import defaultdict
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1                  # empty prefix
    for x in nums:
        prefix += x
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
```
**Complexity:** O(n) time, O(n) space.
**Key insight:** "Subarray sum" + count = prefix sum ko HashMap me store karo.

## 14. Group Anagrams — Medium
**Pattern:** HashMap with sorted-string key
**Samajh:** Anagrams ka sorted form same hota hai. Sorted string ko key banao, list me daalo.
```python
def groupAnagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for w in strs:
        key = ''.join(sorted(w))     # ya tuple of 26-count
        groups[key].append(w)
    return list(groups.values())
```
**Complexity:** O(n·k log k) time (k = word length).
**Key insight:** "Group by property" = us property ko HashMap key banao.

## 15. Climbing Stairs — Easy (DP intro)
**Pattern:** 1D DP (Fibonacci)
**Samajh:** n-th step pe pahunchne ke tarike = (n-1) ke + (n-2) ke. Fibonacci hi hai.
```python
def climbStairs(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** DP ki entry — "current = pichhle do ka sum." Har DP yahin se shuru samjho.

## 16. House Robber — Medium (DP)
**Pattern:** 1D DP (choose / skip)
**Samajh:** Har ghar pe 2 choice: loot (to pichhla skip) ya skip. Max le lo.
```python
def rob(nums):
    prev, cur = 0, 0             # prev = i-2 tak best, cur = i-1 tak best
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** "Choose vs don't choose" = har DP/knapsack ka core. Yaad rakho.

## 17. Coin Change (min coins) — Medium (DP)
**Pattern:** Unbounded knapsack DP
**Samajh:** dp[amt] = kam se kam coins amt banane ke. Har coin try karo: dp[amt] = min(dp[amt], dp[amt-coin]+1).
```python
def coinChange(coins, amount):
    INF = float('inf')
    dp = [0] + [INF] * amount
    for amt in range(1, amount + 1):
        for c in coins:
            if c <= amt:
                dp[amt] = min(dp[amt], dp[amt - c] + 1)
    return dp[amount] if dp[amount] != INF else -1
```
**Complexity:** O(amount·coins) time, O(amount) space.
**Key insight:** "Minimum/ways to make a target" = coin/knapsack DP. Q3 me bahut aata hai.

## 18. Jump Game — Medium (Greedy)
**Pattern:** Greedy (farthest reach)
**Samajh:** Har index pe track karo "sabse door kahan tak pahunch sakte." Agar current index reach se bahar → false.
```python
def canJump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** Greedy = "abhi tak ka best reach" maintain karo. (Q2 style.)

## 19. Merge Intervals — Medium (Greedy/Sorting)
**Pattern:** Sort + merge
**Samajh:** Start se sort karo; agla interval pichhle se overlap kare to merge (end ko extend), warna naya.
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for s, e in intervals:
        if res and s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)   # overlap → merge
        else:
            res.append([s, e])
    return res
```
**Complexity:** O(n log n) time (sort), O(n) space.
**Key insight:** Interval problems = pehle SORT karo (start ya end pe). Q2 favourite.

## 20. Valid Parentheses — Easy
**Pattern:** Stack
**Samajh:** Opening bracket push karo; closing aaye to top se match karo. Ant me stack khali = valid.
```python
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return not stack
```
**Complexity:** O(n) time, O(n) space.
**Key insight:** "Matching / nesting / last-seen" = Stack. Bahut common.

---
> ✅ TIER 1 done. Yahan sirf ~6 patterns the: HashMap, Two-pointer, Sliding Window, Binary Search,
> 1D-DP (choose/skip), Greedy. Inko samajh gaye to DSE ka Q1 + partials pakke.
> Aage TIER 2 (SP push) aur TIER 3 (SP L2/L3) neeche.


---
# 🟡 TIER 2 — SP PUSH (ye 12 add karo). Q2 greedy + Q3 DP fully.

## 21. Largest Number — Medium (Greedy) ★ Infosys PYQ
**Pattern:** Custom comparator sort
**Samajh:** Do numbers a,b ka order decide karo isse: agar `a+b > b+a` (string jod ke) to a pehle.
Sabko is rule se sort karo, jod do.
```python
from functools import cmp_to_key
def largestNumber(nums):
    arr = list(map(str, nums))
    arr.sort(key=cmp_to_key(lambda a, b: (a+b < b+a) - (a+b > b+a)))
    res = ''.join(arr)
    return '0' if res[0] == '0' else res     # all-zero edge case
```
**Complexity:** O(n log n · k) time.
**Key insight:** "Order dhundo" = custom comparator. Yahan compare = concatenation.

## 22. Non-overlapping Intervals — Medium (Greedy)
**Pattern:** Sort by END + greedy keep
**Samajh:** Jaldi khatam hone wale interval ko rakho (max fit). Overlap aaye to remove count badhao.
```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])       # end pe sort
    end = float('-inf')
    remove = 0
    for s, e in intervals:
        if s >= end:
            end = e                          # keep
        else:
            remove += 1                      # overlap → remove
    return remove
```
**Complexity:** O(n log n) time.
**Key insight:** Activity selection = sort by end time. Classic greedy.

## 23. Gas Station — Medium (Greedy)
**Pattern:** Greedy (total + running tank)
**Samajh:** Agar total gas >= total cost to answer exist karta hai. Jahan tank negative ho, wahan se start reset karo.
```python
def canCompleteCircuit(gas, cost):
    total, tank, start = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1                    # yahan tak se nahi hoga
            tank = 0
    return start if total >= 0 else -1
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** "Negative hua to aage se restart" — greedy reset trick.

## 24. 0/1 Knapsack — Medium (DP) ★ core
**Pattern:** 2D → 1D DP (choose/skip with capacity)
**Samajh:** Har item: lo (value + baaki capacity) ya chhodo. Max. Capacity peeche se update (0/1 ke liye).
```python
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for cap in range(W, weights[i] - 1, -1):   # REVERSE = 0/1
            dp[cap] = max(dp[cap], dp[cap - weights[i]] + values[i])
    return dp[W]
```
**Complexity:** O(n·W) time, O(W) space.
**Key insight:** 0/1 knapsack me capacity loop REVERSE (har item ek baar). Unbounded me forward.

## 25. Partition Equal Subset Sum — Medium (DP)
**Pattern:** Subset-sum DP (knapsack variant)
**Samajh:** Total odd → impossible. Warna dekho subset sum = total/2 ban sakta hai kya (boolean knapsack).
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```
**Complexity:** O(n·target) time, O(target) space.
**Key insight:** "Subset with sum X?" = boolean knapsack. Same skeleton as #24.

## 26. Longest Common Subsequence — Medium (DP) ★ core
**Pattern:** 2D DP on two strings
**Samajh:** Char match → diagonal+1; na match → left/up ka max. Classic grid DP.
```python
def longestCommonSubsequence(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```
**Complexity:** O(m·n) time, O(m·n) space.
**Key insight:** Two-string DP = 2D grid, "match → diagonal, else max(left,up)". LCS/Edit Distance sab isi pe.

## 27. Longest Increasing Subsequence — Medium (DP) ★ (non-decreasing variation bhi asked)
**Pattern:** DP O(n²) ya binary-search O(n log n)
**Samajh (simple O(n²)):** dp[i] = i pe khatam hone wali LIS. Har j<i dekho, agar chhota to extend.
```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:            # non-decreasing ke liye <=
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```
**Complexity:** O(n²) time (O(n log n) with bisect), O(n) space.
**Key insight:** "Subsequence with order" = dp[i] ending-at-i. `<` ko `<=` karo to non-decreasing.

## 28. Edit Distance — Hard (DP)
**Pattern:** 2D DP (insert/delete/replace)
**Samajh:** Match → diagonal; warna 1 + min(insert, delete, replace). LCS jaisa grid.
```python
def minDistance(a, b):
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
    return dp[m][n]
```
**Complexity:** O(m·n) time & space.
**Key insight:** 3 operations = 3 neighbours ka min + 1. Grid DP ka strong example.

## 29. Unique Paths / Minimum Path Sum — Medium (Matrix DP)
**Pattern:** 2D grid DP
**Samajh (Min Path Sum):** Har cell tak min cost = cell + min(upar, left).
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: continue
            up   = grid[i-1][j] if i > 0 else float('inf')
            left = grid[i][j-1] if j > 0 else float('inf')
            grid[i][j] += min(up, left)
    return grid[m-1][n-1]
# Unique Paths (count): dp[i][j] = dp[i-1][j] + dp[i][j-1], first row/col = 1
```
**Complexity:** O(m·n) time.
**Key insight:** Grid me har cell = "upar/left se aaya" — matrix DP ka base.

## 30. Number of Islands — Medium (Graph DFS/BFS) ★ frequent
**Pattern:** Grid DFS/BFS (flood fill)
**Samajh:** '1' mila to island count++, aur us puri connected land ko DFS se '0' kar do (visited).
```python
def numIslands(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1)
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count
```
**Complexity:** O(m·n) time.
**Key insight:** "Connected regions in grid" = DFS/BFS flood fill. Visited ko mark karo.

## 31. Rotting Oranges — Medium (Graph BFS) ★ Infosys favourite
**Pattern:** Multi-source BFS (level = time)
**Samajh:** Saare rotten (=2) ko queue me daalo, BFS karo level-by-level; har level = 1 minute.
```python
from collections import deque
def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2: q.append((i, j))
            elif grid[i][j] == 1: fresh += 1
    minutes = 0
    while q and fresh:
        minutes += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    q.append((x, y))
    return minutes if fresh == 0 else -1
```
**Complexity:** O(m·n) time.
**Key insight:** "Shortest time/steps to spread" = BFS level count. Multi-source = saare start ek saath.

## 32. Course Schedule (topological sort) — Medium (Graph)
**Pattern:** Topo sort (Kahn's / BFS on indegree)
**Samajh:** Cycle ho to impossible. Indegree 0 wale process karo, unke padosi ka indegree ghatao.
```python
from collections import deque, defaultdict
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:      # b -> a
        graph[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(numCourses) if indeg[i] == 0])
    done = 0
    while q:
        node = q.popleft()
        done += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return done == numCourses
```
**Complexity:** O(V+E) time.
**Key insight:** "Ordering with dependencies / cycle detect" = topological sort (indegree BFS).

---
> ✅ TIER 2 done. Naye patterns: custom-comparator greedy, 2D grid DP (LCS/Edit/Path),
> knapsack (0/1 + subset), graph DFS/BFS/topo. Tier 1+2 = 32 problems = SP real chance.


---
# 🔴 TIER 3 — SP L2/L3 EDGE (ye 8, time bache to). Hard patterns.

## 33. Trapping Rain Water — Hard
**Pattern:** Two pointers (max-left / max-right)
**Samajh:** Har bar pe paani = min(leftMax, rightMax) - height. Do pointer se ek pass me.
```python
def trap(height):
    if not height: return 0
    l, r = 0, len(height) - 1
    lmax = rmax = 0
    water = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water += lmax - height[l]
            l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax - height[r]
            r -= 1
    return water
```
**Complexity:** O(n) time, O(1) space.
**Key insight:** Chhoti wall wali side hamesha bounded hai — wahi side move karo.

## 34. Next Greater Element (monotonic stack) — Medium
**Pattern:** Monotonic decreasing stack
**Samajh:** Stack me indices rakho jinka next-greater abhi nahi mila. Bada element aaya to unhe resolve karo.
```python
def nextGreaterElements(nums):
    res = [-1] * len(nums)
    stack = []                      # indices, decreasing values
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        stack.append(i)
    return res
```
**Complexity:** O(n) time, O(n) space.
**Key insight:** "Next greater/smaller" = monotonic stack. Ek baar samjho, 8+ problems.

## 35. Sliding Window Maximum — Hard
**Pattern:** Monotonic deque
**Samajh:** Deque me indices rakho decreasing order me; front hamesha window ka max. Purane/chhote hatao.
```python
from collections import deque
def maxSlidingWindow(nums, k):
    dq = deque()                    # indices, decreasing values
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:          # window se bahar
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```
**Complexity:** O(n) time, O(k) space.
**Key insight:** Window max/min = monotonic deque (front = answer).

## 36. Kth Largest Element — Medium
**Pattern:** Min-heap of size k
**Samajh:** Size-k min-heap rakho; heap ka top = k-th largest. Bada aaye to top nikaal do.
```python
import heapq
def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]
```
**Complexity:** O(n log k) time, O(k) space.
**Key insight:** "K-th largest / top-K" = size-k heap. Largest ke liye MIN-heap (ulta lagta hai par sahi).

## 37. Top K Frequent Elements — Medium
**Pattern:** Count + heap (ya bucket sort)
**Samajh:** Frequency count karo, phir top-K frequent nikaalo (heap ya bucket).
```python
from collections import Counter
import heapq
def topKFrequent(nums, k):
    freq = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda p: p[1])]
```
**Complexity:** O(n log k) time.
**Key insight:** Count phir top-K = Counter + heap. HashMap + heap combo.

## 38. Dijkstra Shortest Path — Hard (Graph)
**Pattern:** Min-heap greedy (weighted shortest path)
**Samajh:** Source se dist=0. Heap se sabse paas wala node lo, uske padosi ki dist update karo (relax).
```python
import heapq
def dijkstra(n, edges, src):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))     # undirected; directed ke liye hatao
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]                 # (distance, node)
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nb, w in graph[node]:
            if d + w < dist[nb]:
                dist[nb] = d + w
                heapq.heappush(pq, (dist[nb], nb))
    return dist
```
**Complexity:** O(E log V) time.
**Key insight:** Weighted shortest path = Dijkstra (min-heap + relax). BFS ka weighted version.

## 39. Next Smallest Palindrome — Medium (Math/String) ★ Infosys classic
**Pattern:** Mirror left half → right, carry if needed
**Samajh:** Left half ko right pe mirror karo. Agar mirror wala >= original nahi hua, to middle pe +1 karo (carry).
```python
def next_smallest_palindrome(num_str):
    n = len(num_str)
    digits = list(num_str)
    # left half ko right pe mirror
    for i in range(n // 2):
        digits[n - 1 - i] = digits[i]
    candidate = ''.join(digits)
    if candidate > num_str:
        return candidate
    # warna middle se +1 (carry propagate)
    i = (n - 1) // 2
    j = n // 2
    carry = 1
    dg = list(candidate)
    while i >= 0 and carry:
        d = int(dg[i]) + carry
        carry = d // 10
        dg[i] = dg[j] = str(d % 10)
        i -= 1; j += 1
    if carry:                        # jaise 99 -> 101
        return '1' + '0' * (n - 1) + '1'
    return ''.join(dg)
```
**Complexity:** O(n) time.
**Key insight:** Palindrome banao = ek half ko mirror; badhana ho to middle se carry. (Edge: all 9s.)

## 40. Single Number + Maximum XOR (bit) — Medium ★ Infosys bit-greedy
**Pattern:** XOR properties + bitwise greedy
**Samajh (Single Number):** x^x=0, x^0=x. Saare XOR karo → duplicates cancel, akela bacha.
```python
def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x                     # pairs cancel out
    return res
```
**Maximum XOR of two numbers (bit-greedy):** MSB se har bit pe try karo ki 1 ban sakta hai kya (prefix set + check).
```python
def findMaximumXOR(nums):
    ans = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {x & mask for x in nums}
        cand = ans | (1 << i)        # ye bit 1 kar sakte?
        if any((cand ^ p) in prefixes for p in prefixes):
            ans = cand
    return ans
```
**Complexity:** Single Number O(n); Max XOR O(32n).
**Key insight:** XOR = "pairs cancel" (single number) + "MSB se greedy bit banao" (max XOR).

---
# 🎯 PATTERN CHEAT-SHEET (ye 12 patterns = poora goldmine)
1. **HashMap** — Two Sum, Group Anagrams, Subarray Sum K, Top-K
2. **Two Pointers** — Palindrome, Remove Dup, Move Zeroes, Merge, Trapping Rain Water
3. **Sliding Window** — Longest Substring, Window Max, Min Size Subarray
4. **Binary Search** — Search, Insert Position, Rotated array, "search on answer"
5. **Kadane** — Maximum Subarray
6. **Greedy** — Jump Game, Gas Station, Intervals, Largest Number
7. **1D DP (choose/skip)** — Climbing Stairs, House Robber
8. **Knapsack DP** — Coin Change, 0/1 Knapsack, Partition Subset
9. **2D Grid DP** — LCS, Edit Distance, Path Sum, Unique Paths
10. **Graph DFS/BFS** — Number of Islands, Rotting Oranges, Course Schedule (topo)
11. **Stack / Monotonic Stack** — Valid Parentheses, Next Greater, Window Max (deque)
12. **Heap** — Kth Largest, Top-K, Dijkstra + **Bit/XOR** tricks

> Bhai, ye 12 patterns hi 90% Infosys test cover karte hain. Ek-ek pattern samajh (tere god-level
> mind ke liye 1-1 din bhi zyada hai), phir us pattern ke saare problems auto-solve lagenge.
> **Q1 (HashMap/Two-pointer/Kadane) = pakka. Greedy + DP samajh = SP zone. Chalo shuru!**


---
# 🟣 TIER 4 — INTERVIEW ESSENTIALS (Trees + Backtracking + Linked List)
> Ye test me kam, par **interview me pakka** (SP + DSE dono). PREP inhe list karta hai — yahan full solutions.
> Naye patterns: **Backtracking (13), Tree DFS/BFS (14), Fast-Slow pointer (15)**.

## 41. Subsets — Medium (Backtracking) — pattern 13
**Samajh:** har element pe 2 choice — lo ya chhodo. Recursion tree se saare combos.
```python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])              # har node ek valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)       # aage se
            path.pop()                   # undo (backtrack)
    backtrack(0, [])
    return res
```
**Complexity:** O(2^n · n). **Key insight:** choose → recurse → **undo** = backtracking ka core.

## 42. Permutations — Medium (Backtracking)
**Samajh:** har position pe har unused element try karo.
```python
def permute(nums):
    res = []
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True; path.append(nums[i])
            backtrack(path, used)
            path.pop(); used[i] = False  # undo
    backtrack([], [False]*len(nums))
    return res
```
**Complexity:** O(n! · n). **Key insight:** `used[]` se repeat avoid; undo dono (path + used).

## 43. Combination Sum — Medium (Backtracking) ★
**Samajh:** target tak pahunchne ke liye elements (reuse allowed) try karo.
```python
def combinationSum(candidates, target):
    res = []
    def backtrack(start, path, remain):
        if remain == 0:
            res.append(path[:]); return
        if remain < 0: return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remain - candidates[i])   # i (not i+1) = reuse
            path.pop()
    backtrack(0, [], target)
    return res
```
**Complexity:** exponential. **Key insight:** reuse allowed → `i`; no reuse → `i+1`.

## 44. Maximum Depth of Binary Tree — Easy (Tree DFS) — pattern 14
```python
def maxDepth(root):
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```
**Complexity:** O(n). **Key insight:** tree = recursion on left+right. Base case = None.

## 45. Diameter of Binary Tree — Easy/Medium (Tree DFS) ★
**Samajh:** har node pe left-height + right-height = us node se guzarne wala longest path.
```python
def diameterOfBinaryTree(root):
    best = 0
    def height(node):
        nonlocal best
        if not node: return 0
        l = height(node.left); r = height(node.right)
        best = max(best, l + r)          # path through this node
        return 1 + max(l, r)
    height(root)
    return best
```
**Complexity:** O(n). **Key insight:** ek DFS me height return + global best update.

## 46. Lowest Common Ancestor (Binary Tree) — Medium ★
**Samajh:** agar dono target alag subtrees me hain, current node hi LCA.
```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right: return root       # dono side mile → yahi LCA
    return left or right
```
**Complexity:** O(n). **Key insight:** dono side non-null → current = LCA. (BST me: value compare se O(h).)

## 47. Validate BST — Medium (Tree DFS)
**Samajh:** har node ke liye valid range (min,max) maintain karo.
```python
def isValidBST(root):
    def valid(node, low, high):
        if not node: return True
        if not (low < node.val < high): return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float('-inf'), float('inf'))
```
**Complexity:** O(n). **Key insight:** BST = left < node < right, range narrow karte jao.

## 48. Binary Tree Level Order Traversal — Medium (Tree BFS)
```python
from collections import deque
def levelOrder(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```
**Complexity:** O(n). **Key insight:** level-wise = BFS with `for _ in range(len(q))`.

## 49. Reverse Linked List — Easy (Linked List) — pattern 15
**Samajh:** har node ka next reverse karo, 3 pointers (prev, cur, next).
```python
def reverseList(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```
**Complexity:** O(n) time, O(1) space. **Key insight:** prev/cur/next teen pointer — LL ka #1 sawaal.

## 50. Detect Cycle in Linked List — Easy (Fast-Slow / Floyd) ★
**Samajh:** slow 1 step, fast 2 step; cycle hai to milenge.
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Complexity:** O(n) time, O(1) space. **Key insight:** Floyd's tortoise-hare. Middle-of-list bhi isi se.

## 51. Merge Two Sorted Lists — Easy (Linked List)
```python
def mergeTwoLists(l1, l2):
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1; l1 = l1.next
        else:
            tail.next = l2; l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2                  # bacha hua attach
    return dummy.next
```
**Complexity:** O(m+n). **Key insight:** **dummy node** se head-handling easy. (Merge-sort ka base.)

---
# 🔑 UPDATED PATTERN CHEAT-SHEET (ab 15 patterns = full coverage)
> Tier 1-3 ke 12 patterns + ye 3:
13. **Backtracking** — Subsets, Permutations, Combination Sum, N-Queens (choose→recurse→undo)
14. **Tree DFS/BFS** — Max Depth, Diameter, LCA, Validate BST, Level Order
15. **Fast-Slow pointer (Linked List)** — Reverse, Detect Cycle, Middle, Merge

> Ab DSA coverage complete: Tier 1-2 (test core, DSE→SP) · Tier 3 (SP hard edge) · Tier 4 (interview).
> SP ke liye Tier 1-4 sab; DSE ke liye Tier 1-2 kaafi + Tier 4 interview ke liye.


---
# 🟤 TIER 5 — REAL INFOSYS PYQ (actual reported questions, FULL solutions)
> Ye **actually Infosys SP/DSE / HackWithInfy me aaye** (sources: PrepInsta, GfG OA experiences 2024-25,
> Scribd PYQ, HWI). Statement meri words me, par pattern + difficulty bilkul real. Ye solve kar liye
> to test familiar lagega. (Note: exact same Q guarantee nahi — par yahi styles repeat hote hain.)

## R1. Split Array into K Segments, Min Cost — DP ★ (SP PYQ)
**Story:** N boxes line me (weights a[]). Exactly K contiguous groups banao. Group cost = (group sum)².
Total cost minimize karo.
**Constraints:** 1 ≤ K ≤ N ≤ 500.
```python
def min_cost_k_segments(a, K):
    n = len(a)
    pre = [0]*(n+1)
    for i in range(n): pre[i+1] = pre[i] + a[i]
    INF = float('inf')
    dp = [[INF]*(n+1) for _ in range(K+1)]
    dp[0][0] = 0
    for k in range(1, K+1):
        for i in range(1, n+1):
            for j in range(k-1, i):
                seg = pre[i] - pre[j]
                dp[k][i] = min(dp[k][i], dp[k-1][j] + seg*seg)
    return dp[K][n]
```
**Pattern:** Partition DP `dp[k][i]=min(dp[k-1][j]+cost(j..i))`. O(K·N²).

## R2. Painter's Partition / "Drying Walls" — Binary Search on Answer ★ (Scribd SP PYQ)
**Story:** N walls, wall i ko paint karne me time[i]. P painters (har painter contiguous walls hi
karega, parallel me). Aisa allot karo ki **sabse zyada busy painter ka time minimum** ho. Wo min time batao.
**Constraints:** 1 ≤ P ≤ N ≤ 10^5.
```python
def painters_partition(time, P):
    def can(limit):                        # P painters me ho jayega agar har chunk <= limit?
        painters, cur = 1, 0
        for t in time:
            if t > limit: return False
            if cur + t > limit:
                painters += 1; cur = t
            else:
                cur += t
        return painters <= P
    lo, hi = max(time), sum(time)
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid): hi = mid
        else: lo = mid + 1
    return lo
```
**Pattern:** "Minimize the maximum" = **binary search on the answer** + greedy feasibility. O(N log(sum)).

## R3. Aggressive Cows / Place Elements — Binary Search on Answer ★ (Infosys style)
**Story:** N stalls positions[] me hain (line pe). C cows ko rakhna hai aise ki **kisi do cows ke beech
minimum distance maximum** ho. Wo max-min distance batao.
**Constraints:** 2 ≤ C ≤ N ≤ 10^5.
```python
def max_min_distance(pos, C):
    pos.sort()
    def can(d):
        count, last = 1, pos[0]
        for p in pos[1:]:
            if p - last >= d:
                count += 1; last = p
                if count == C: return True
        return count >= C
    lo, hi = 1, pos[-1] - pos[0]
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid): ans = mid; lo = mid + 1
        else: hi = mid - 1
    return ans
```
**Pattern:** "Maximize the minimum" = binary search on answer. (R2 ka bhai.)

## R4. Job Sequencing with Deadlines — Greedy ★ (classic Infosys)
**Story:** N jobs; har job ka (deadline, profit). Ek job 1 unit time leta; ek time-slot me ek job.
Deadline se pehle complete jobs ka **max profit** nikaalo.
```python
def job_sequencing(jobs):                  # jobs = [(deadline, profit), ...]
    jobs.sort(key=lambda x: -x[1])         # profit desc
    max_d = max(d for d, p in jobs)
    slot = [False]*(max_d+1)
    profit = 0
    for d, p in jobs:
        for t in range(min(max_d, d), 0, -1):   # latest free slot <= deadline
            if not slot[t]:
                slot[t] = True; profit += p; break
    return profit
```
**Pattern:** Greedy — high profit pehle, latest possible slot me daalo. O(N·maxD) / O(N log N + N·α with DSU).

## R5. Prime Pairs / Sieve — Number Theory ★ (Scribd PYQ "prime pairs")
**Story:** 1..N me kitne **pairs (a,b), a<b** hain jinke dono prime hain aur a+b bhi ek diya hua target?
(ya: N tak saare primes count karo.) Base: Sieve of Eratosthenes.
```python
def sieve(n):
    is_p = [True]*(n+1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_p[i]:
            for j in range(i*i, n+1, i):
                is_p[j] = False
    return [i for i in range(2, n+1) if is_p[i]]

def prime_pairs_sum(n, target):
    primes = set(sieve(n))
    count = 0
    for p in primes:
        if p < target - p and (target - p) in primes:
            count += 1
    return count
```
**Pattern:** Sieve O(N log log N) → phir pair check. Number-theory questions ka base.

## R6. Count Distinct in Every Window of Size K — Sliding Window + Hash ★
**Story:** Array A, window size K. Har window (K consecutive) me **distinct elements ki count** print karo.
```python
from collections import defaultdict
def distinct_in_windows(a, k):
    freq = defaultdict(int)
    res = []
    for i, x in enumerate(a):
        freq[x] += 1
        if i >= k:
            left = a[i-k]
            freq[left] -= 1
            if freq[left] == 0: del freq[left]
        if i >= k-1:
            res.append(len(freq))
    return res
```
**Pattern:** Sliding window + frequency map (distinct = len(map)). O(N).

## R7. Subset Sum (boolean) — DP ★ (karthikreddy repo PYQ)
**Story:** Non-negative integers ka set + target `sum`. Koi subset hai jiska sum = target? True/False.
```python
def subset_sum(nums, target):
    dp = [False]*(target+1)
    dp[0] = True
    for x in nums:
        for s in range(target, x-1, -1):
            dp[s] = dp[s] or dp[s-x]
    return dp[target]
```
**Pattern:** Boolean knapsack. (Partition #25 same skeleton.)

## R8. Treasure Picker (Khaled) — at most N/2 max sum — Greedy ★ (DSE PYQ)
**Story:** Array A (N even). At most **N/2** elements chuno (non-consecutive allowed), **max sum**.
```python
def max_sum_half(a):
    a.sort(reverse=True)
    total = 0
    for i in range(len(a)//2):
        if a[i] > 0: total += a[i]
        else: break
    return total
```
**Pattern:** Sort desc + top-K positive. O(N log N).

---
# 🟤 TIER 5 (contd.) — baaki REAL PYQ ke bhi FULL solutions (ab koi "approach-only" nahi)

## R9. Hungry Fish — Min Moves to 1 Fish ★ (GfG SP)
**Story:** Injected fish size x kisi chhoti fish y (y<x) ko kha ke x+y ho jaati hai. Aquarium me kai
normal fish. Scientist **add** (koi bhi size) ya **remove** (existing) kar sakta hai. Objective: ant me
sirf 1 fish (injected, sabko kha ke). Min moves batao.
**Example:** injected=10, others=[9,20,25,100] → **2**.
```python
def min_moves_fish(fishes, injected):
    fishes.sort()                          # ascending
    cur = injected
    moves = 0
    i, n = 0, len(fishes)
    while i < n:
        if cur > fishes[i]:
            cur += fishes[i]               # eat, free
            i += 1
        else:
            # ye fish eat karne ko kitni chhoti fish add karni padegi (fastest grow = size cur-1)
            adds, temp = 0, cur
            while temp <= fishes[i] and temp >= 2:
                temp += (temp - 1)         # add fish (cur-1), eat it → cur almost doubles
                adds += 1
            remaining = n - i              # yahan se aage sab bade → warna sabko remove karna padega
            if temp > fishes[i] and adds <= remaining:
                moves += adds; cur = temp
                cur += fishes[i]; i += 1   # ab ye fish bhi kha lo
            else:
                moves += remaining         # baaki sab remove karo
                break
    return moves
# min_moves_fish([9,20,25,100], 10) -> 2
```
**Pattern:** Greedy + sort. Har block pe: "grow (adds) vs remove-remaining" ka min. O(N log N).

## R10. GET(l,r) Max Pairs — count pairs with maximum value ★ (GfG SP OA Dec 2024)
**Story:** Array a[n]. `GET(l,r)` = a[l] + a[r] (pair-sum variant). Un pairs (l<r) ki **count** batao
jinke liye GET(l,r) **maximum** hai.
```python
def count_max_pairs(a):
    mx = max(a)
    cnt_max = a.count(mx)                   # kitne elements == max
    if cnt_max >= 2:
        return cnt_max * (cnt_max - 1) // 2 # max+max sabse bada → in me se koi 2
    second = max(x for x in a if x != mx)   # ek hi max → second-largest ke saath
    return a.count(second)
```
**Pattern:** Max nikaalo → count karo (combinatorics). O(n).
> Agar GET alag ho (XOR / a[l]&a[r] / subarray-sum): **same technique** — max compute karo, phir count.

## R11. Guest Serving Order — Next Greater Element ★ (Scribd PYQ)
**Story:** N guests queue me, har guest ki "priority". Har guest ke liye batao **uske aage pehla guest
jiski priority zyada hai** (nahi to -1). (= Next Greater Element.)
```python
def next_greater(priority):
    n = len(priority)
    res = [-1]*n
    stack = []                              # indices, decreasing priority
    for i in range(n):
        while stack and priority[stack[-1]] < priority[i]:
            res[stack.pop()] = priority[i]
        stack.append(i)
    return res
```
**Pattern:** Monotonic stack. O(n).

## R12. Spiral Matrix — traversal ★ (HackWithInfy 2026)
**Story:** M×N matrix ko spiral order (top→right→bottom→left, andar aate) me print karo.
```python
def spiralOrder(mat):
    if not mat: return []
    res = []
    top, bot = 0, len(mat)-1
    left, right = 0, len(mat[0])-1
    while top <= bot and left <= right:
        for j in range(left, right+1): res.append(mat[top][j])
        top += 1
        for i in range(top, bot+1): res.append(mat[i][right])
        right -= 1
        if top <= bot:
            for j in range(right, left-1, -1): res.append(mat[bot][j])
            bot -= 1
        if left <= right:
            for i in range(bot, top-1, -1): res.append(mat[i][left])
            left += 1
    return res
```
**Pattern:** 4 boundaries shrink. O(M·N).

## R13. Longest Run / Max Consecutive Ones with K Flips ★ (binary-string PYQ)
**Story-A:** Binary string me sabse lambi **consecutive same characters** ki length.
**Story-B (common):** 0/1 array me at most **K zeros flip** karke sabse lambi **consecutive 1s** kitni?
```python
# A) longest run of same char
def longest_run(s):
    if not s: return 0
    best = run = 1
    for i in range(1, len(s)):
        run = run + 1 if s[i] == s[i-1] else 1
        best = max(best, run)
    return best

# B) max consecutive 1s after flipping at most k zeros (sliding window)
def longest_ones(nums, k):
    left = zeros = best = 0
    for right in range(len(nums)):
        if nums[right] == 0: zeros += 1
        while zeros > k:
            if nums[left] == 0: zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```
**Pattern:** A = single pass; B = **sliding window** (window me at most k zeros). O(n).

---
> ✅ Ab **poora self-contained**: 51 core (Tier1-4) + 13 real-PYQ FULL solutions (Tier5 R1-R13) +
> 2 timed mock sets (`09`). Koi "approach-only / reference-only" nahi bacha — sab code yahin hai.
> Anyhow selection: Q1 full + Q2/Q3 partial = DSE lock; 2 full = SP.
