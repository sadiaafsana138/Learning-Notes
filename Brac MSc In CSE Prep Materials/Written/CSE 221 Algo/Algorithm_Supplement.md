# ➕ ALGORITHM SUPPLEMENT
### বাকি যে Algorithm-গুলো আগের file-এ ছিল না

> আগের ৩টা file-এ **৮টা sort + ২টা search** ছিল। এই file-এ বাকিগুলো — যাতে তালিকা সম্পূর্ণ হয়।
> **Priority:** এখানকার বেশিরভাগই 🟡 **Medium/Low** — মূল ৮+২টা আগে ঠিক করো, তারপর এটা।

---

## 📊 প্রথমে দেখো — কোনটা কোথায়

| Algorithm | কোথায় আছে | Priority |
|---|---|---|
| Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix | `Algorithm_Steps_and_DryRun.md` | 🔴 |
| Linear Search, Binary Search | `Algorithm_Steps_and_DryRun.md` | 🔴 |
| BFS, DFS, Dijkstra, Bellman-Ford, Floyd, Prim, Kruskal, Topological | `Algorithm_Steps_and_DryRun.md` | 🔴 |
| **Shell, Bucket, Tim Sort** | **এই file** | 🟡 |
| **Jump, Interpolation, Exponential, Ternary Search** | **এই file** | 🟡 |
| **KMP, Rabin-Karp (String matching)** | **এই file** | 🟡 |
| **Union-Find, SCC, A\*** | **এই file** | 🔵 |

---
---

# A. বাকি SORTING ALGORITHMS

## A1. Shell Sort 🟡

### Definition (English)
**Shell Sort** is a generalization of Insertion Sort that compares elements separated by a **gap**, gradually reducing the gap to 1.

### Concept (বাংলায়)
Insertion Sort-এর সমস্যা: একটা element-কে অনেক দূর সরাতে হলে বহুবার shift করতে হয়।
Shell Sort দূরের element-দের **আগে থেকেই** মোটামুটি জায়গামতো এনে রাখে, শেষে gap=1 দিয়ে সাধারণ Insertion Sort চালায় — তখন কাজ অনেক কম।

### Steps
1. একটা **gap** বেছে নাও (সাধারণত `n/2`)।
2. `A[i]` ও `A[i + gap]` তুলনা করে gapped insertion sort চালাও।
3. **Gap অর্ধেক করো** (`gap = gap / 2`)।
4. Gap = 1 না হওয়া পর্যন্ত ধাপ 2–3 পুনরাবৃত্তি করো।
5. Gap = 1-এ শেষবার সাধারণ Insertion Sort — কিন্তু data প্রায় sorted বলে দ্রুত।

### Dry Run
`A = [23, 12, 1, 8]`, n = 4
```
gap = 2:
  A[0]=23 vs A[2]=1  → swap → [1, 12, 23, 8]
  A[1]=12 vs A[3]=8  → swap → [1, 8, 23, 12]

gap = 1:  (সাধারণ insertion sort)
  [1, 8, 23, 12] → 12 কে 23-এর আগে বসাও → [1, 8, 12, 23]

Result: [1, 8, 12, 23]
```

| Best | Average | Worst | Space | Stable |
|---|---|---|---|---|
| O(n log n) | O(n^1.3) মোটামুটি | **O(n²)** | **O(1)** | ❌ **না** |

⭐ **Insertion Sort-এর উন্নত রূপ**, in-place, কিন্তু unstable।

---

## A2. Bucket Sort 🟡

### Definition (English)
**Bucket Sort** distributes elements into a number of **buckets**, sorts each bucket individually, then concatenates them.

### Concept (বাংলায়)
Data-কে কয়েকটা **রেঞ্জ-ভিত্তিক bucket**-এ ভাগ করো, প্রতিটা bucket আলাদা sort করো (সাধারণত Insertion Sort দিয়ে), তারপর ক্রমানুসারে জোড়া লাগাও।

**শর্ত:** Data **সমানভাবে ছড়ানো (uniformly distributed)** হলে সবচেয়ে ভালো কাজ করে।

### Steps
1. `k` টি খালি bucket বানাও।
2. প্রতিটি element-কে তার মান অনুযায়ী উপযুক্ত bucket-এ ফেলো।
3. প্রতিটি bucket আলাদাভাবে sort করো।
4. Bucket-গুলো **ক্রমানুসারে জোড়া লাগাও**।

### Dry Run
`A = [0.42, 0.32, 0.75, 0.12]`, 4টি bucket (0–0.25, 0.25–0.5, 0.5–0.75, 0.75–1.0)
```
Bucket 0: [0.12]
Bucket 1: [0.42, 0.32]  → sort → [0.32, 0.42]
Bucket 2: []
Bucket 3: [0.75]

জোড়া লাগাও: [0.12, 0.32, 0.42, 0.75]
```

| Best | Average | Worst | Space | Stable |
|---|---|---|---|---|
| O(n + k) | **O(n + k)** | **O(n²)** (সব এক bucket-এ) | O(n + k) | ✅ (ভিতরে stable sort হলে) |

⭐ Floating point বা uniform distribution-এ ভালো।

---

## A3. Tim Sort 🔵 (শুধু জেনে রাখো)

**Definition:** A **hybrid** stable sorting algorithm combining **Merge Sort and Insertion Sort**.

**Concept:** Array-কে ছোট ছোট "run"-এ ভাগ করে প্রতিটা **Insertion Sort** দিয়ে sort করে, তারপর **Merge Sort** দিয়ে জোড়া লাগায়।

⭐ **Python-এর `sorted()` ও Java-র `Arrays.sort()` (object-এর জন্য) এটাই ব্যবহার করে।**

| Best | Average | Worst | Space | Stable |
|---|---|---|---|---|
| **O(n)** | O(n log n) | **O(n log n)** | O(n) | ✅ |

---

## ★ সম্পূর্ণ SORTING MASTER TABLE (১১টা)

| Algorithm | Best | Average | Worst | Space | Stable | In-place | ধরন |
|---|---|---|---|---|---|---|---|
| **Bubble** | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | Exchange |
| **Selection** | **O(n²)** | O(n²) | O(n²) | O(1) | ❌ | ✅ | Selection |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | Insertion |
| **Shell** | O(n log n) | ~O(n^1.3) | O(n²) | O(1) | ❌ | ✅ | Insertion |
| **Merge** | O(n log n) | O(n log n) | **O(n log n)** | **O(n)** | ✅ | ❌ | D&C |
| **Quick** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ | ✅ | D&C |
| **Heap** | O(n log n) | O(n log n) | **O(n log n)** | **O(1)** | ❌ | ✅ | Selection |
| **Counting** | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | ❌ | Counting |
| **Radix** | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ | ❌ | Digit |
| **Bucket** | O(n+k) | O(n+k) | **O(n²)** | O(n+k) | ✅ | ❌ | Distribution |
| **Tim Sort** | **O(n)** | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | Hybrid |

### ⭐ মুখস্থ Shortcut
- **Unstable = Selection, Quick, Heap, Shell** (SQHS)
- **Not in-place = Merge, Counting, Radix, Bucket, Tim**
- **Worst O(n²) = Bubble, Selection, Insertion, Shell, Quick, Bucket**
- **Guaranteed O(n log n) = Merge, Heap, Tim**
- **Comparison করে না = Counting, Radix, Bucket** (তাই O(n log n)-এর সীমা ভাঙতে পারে)

---
---

# B. বাকি SEARCHING ALGORITHMS

## B1. Jump Search 🟡

### Definition (English)
**Jump Search** works on a **sorted array** by jumping ahead by fixed steps (**√n**) and then performing a linear search in the identified block.

### Steps
1. **Block size = √n** ঠিক করো।
2. `√n` ধাপ করে লাফাও, প্রতিবার block-এর শেষ element দেখো।
3. যে block-এ target-এর চেয়ে বড় element পেলে → **থামো**।
4. সেই block-এর **শুরু থেকে Linear Search** করো।

### Dry Run
`A = [0,1,2,3,4,5,6,7,8,9]`, n=10, target = **7**, block = √10 ≈ 3
```
index 0 → 0 < 7 → লাফাও
index 3 → 3 < 7 → লাফাও
index 6 → 6 < 7 → লাফাও
index 9 → 9 > 7 → থামো

Block: index 6 থেকে 9 পর্যন্ত linear search
index 7 → 7 ✅ Found
```
**Time: O(√n)** · Space O(1) · **Sorted array লাগে**
⭐ Linear O(n)-এর চেয়ে ভালো, Binary O(log n)-এর চেয়ে খারাপ।

---

## B2. Interpolation Search 🟡

### Definition (English)
**Interpolation Search** improves on Binary Search by estimating the **probable position** of the target based on its value, assuming **uniformly distributed** sorted data.

### Concept (বাংলায়)
Binary Search সবসময় **মাঝখানে** যায়। Interpolation Search **আন্দাজ করে** target কোথায় থাকতে পারে।

ফোনবুকে "Z" খুঁজতে আমরা মাঝখানে না গিয়ে **শেষের দিকে** যাই — এটাই ধারণা।

### Formula ⭐
```
pos = low + [ (target − A[low]) × (high − low) ] / (A[high] − A[low])
```

### Steps
1. উপরের সূত্র দিয়ে `pos` হিসাব করো।
2. `A[pos] == target` → **পেলাম**
3. `A[pos] < target` → `low = pos + 1`
4. `A[pos] > target` → `high = pos − 1`
5. পুনরাবৃত্তি করো।

### Dry Run
`A = [10, 20, 30, 40, 50]`, target = **40**
```
low=0, high=4
pos = 0 + [(40−10) × (4−0)] / (50−10)
    = 0 + (30 × 4) / 40 = 3

A[3] = 40 ✅ Found — মাত্র ১ ধাপে!
```
| Best | Average | Worst |
|---|---|---|
| O(1) | **O(log log n)** ⭐ | **O(n)** (অসম distribution-এ) |

⚠️ **Uniform distribution না হলে Binary Search-এর চেয়ে খারাপ।**

---

## B3. Exponential Search 🔵

### Definition (English)
**Exponential Search** finds a range where the element may exist by **doubling the index**, then applies Binary Search within that range.

### Steps
1. `i = 1` থেকে শুরু করো।
2. `A[i] < target` যতক্ষণ → **`i` দ্বিগুণ করো** (1, 2, 4, 8, 16…)।
3. Range পাওয়া গেলে (`i/2` থেকে `i`) → সেখানে **Binary Search** চালাও।

### Dry Run
`A = [1,2,3,4,5,6,7,8]`, target = **6**
```
i=1: A[1]=2 < 6 → i=2
i=2: A[2]=3 < 6 → i=4
i=4: A[4]=5 < 6 → i=8 (সীমা ছাড়িয়ে গেল)

Range: index 4 থেকে 7 → Binary Search → index 5 = 6 ✅
```
**Time: O(log n)** · ⭐ **Unbounded / infinite array**-এ কাজে লাগে।

---

## B4. Ternary Search 🔵

### Definition (English)
**Ternary Search** divides a sorted array into **three parts** using two midpoints instead of one.

### Steps
1. `mid1 = low + (high−low)/3`, `mid2 = high − (high−low)/3`
2. Target `mid1` বা `mid2`-এর সমান হলে → পেলাম
3. `target < A[mid1]` → বাম অংশে খোঁজো
4. `target > A[mid2]` → ডান অংশে খোঁজো
5. নাহলে → মাঝের অংশে খোঁজো

**Time: O(log₃ n)**
⚠️ **Binary Search-এর চেয়ে ধীর!** কারণ প্রতি ধাপে **২টা comparison** লাগে, Binary-তে ১টা।
⭐ মূলত **unimodal function-এর সর্বোচ্চ/সর্বনিম্ন** বের করতে ব্যবহৃত, array search-এ নয়।

---

## ★ সম্পূর্ণ SEARCHING MASTER TABLE (৭টা)

| Algorithm | Time | Space | Sorted লাগে? | কখন ব্যবহার |
|---|---|---|---|---|
| **Linear Search** | **O(n)** | O(1) | ❌ না | ছোট / unsorted data |
| **Binary Search** | **O(log n)** | O(1) | ✅ হ্যাঁ | Sorted array — **default পছন্দ** |
| **Jump Search** | **O(√n)** | O(1) | ✅ হ্যাঁ | Linked-list-সদৃশ, jump সস্তা হলে |
| **Interpolation** | **O(log log n)** avg / O(n) worst | O(1) | ✅ + uniform | সমানভাবে ছড়ানো data |
| **Exponential** | **O(log n)** | O(1) | ✅ হ্যাঁ | Unbounded / infinite array |
| **Ternary** | O(log₃ n) | O(1) | ✅ হ্যাঁ | Unimodal function optimization |
| **Hash Table** | **O(1)** avg / O(n) worst | O(n) | ❌ না | Key-ভিত্তিক দ্রুত lookup |

### ⭐ MCQ Shortcut
```
Hash O(1) < Interpolation O(log log n) < Binary O(log n) < Jump O(√n) < Linear O(n)
```

---
---

# C. STRING MATCHING ALGORITHMS 🟡

## C1. Naive Pattern Matching

### Steps
1. Text-এর প্রতিটি position `i`-তে pattern বসিয়ে দেখো।
2. Pattern-এর প্রতিটি character মিলিয়ে দেখো।
3. সব মিললে → **match পাওয়া গেল**।
4. না মিললে → `i` এক ধাপ এগিয়ে আবার শুরু।

**Time: O(n × m)** (n = text length, m = pattern length)

---

## C2. KMP (Knuth-Morris-Pratt) ⭐

### Definition (English)
**KMP** avoids re-comparing characters by precomputing an **LPS (Longest Prefix Suffix)** array that tells how far to shift on a mismatch.

### Concept (বাংলায়)
Naive-এ mismatch হলে একদম শুরু থেকে আবার শুরু করতে হয়।
KMP আগেই হিসাব করে রাখে — mismatch হলে **কতটুকু পিছিয়ে গেলেই যথেষ্ট**। তাই text-এ **কখনো পিছনে ফিরতে হয় না**।

### Steps
1. Pattern-এর জন্য **LPS array** বানাও (প্রতিটি position পর্যন্ত সবচেয়ে বড় proper prefix যেটা suffix-ও)।
2. Text ও pattern একসাথে স্ক্যান করো।
3. Character মিললে → দুটোরই index বাড়াও।
4. Mismatch হলে → **LPS array দেখে pattern-এর index পিছাও**, text-এর index **একই রাখো** ⭐
5. Pattern-এর শেষে পৌঁছালে → **match পাওয়া গেল**।

### LPS Example
Pattern = `"ABAB"` → LPS = `[0, 0, 1, 2]`

**Time: O(n + m)** ⭐ · Space O(m)

---

## C3. Rabin-Karp 🔵

### Definition
Uses **hashing** — computes a hash of the pattern and of each text window, comparing hashes instead of characters.

### Steps
1. Pattern-এর **hash** হিসাব করো।
2. Text-এর প্রথম window-এর hash হিসাব করো।
3. Hash মিললে → **character মিলিয়ে নিশ্চিত করো** (false positive হতে পারে)।
4. Window এক ধাপ সরাও, **rolling hash** দিয়ে O(1)-এ নতুন hash বের করো।

**Average O(n + m)** · **Worst O(n × m)** (সব hash collision হলে)
⭐ একসাথে **একাধিক pattern** খুঁজতে ভালো।

---
---

# D. বাকি GRAPH ALGORITHMS 🔵

## D1. Union-Find (Disjoint Set) ⭐

### Definition (English)
A **Disjoint Set** data structure tracks elements partitioned into non-overlapping sets, supporting **Find** (কোন set-এ আছে) and **Union** (দুই set জোড়া) operations.

### Steps
**Find(x):** x-এর **root/representative** খুঁজে বের করো (parent ধরে ধরে উপরে ওঠো)।
**Union(x, y):** দুটোর root বের করো; আলাদা হলে একটার root-কে অন্যটার child বানাও।

### দুই Optimization ⭐
| নাম | কী করে |
|---|---|
| **Path Compression** | Find করার সময় পথের সব node-কে সরাসরি root-এর সাথে জুড়ে দেয় |
| **Union by Rank/Size** | ছোট tree-কে বড় tree-র নিচে জোড়ে, তাই tree উঁচু হয় না |

**Complexity:** দুটো optimization সহ প্রায় **O(α(n)) ≈ O(1)** amortized

⭐ **ব্যবহার:** **Kruskal's MST** (cycle detection), Connected components, Network connectivity

---

## D2. Strongly Connected Components (SCC) 🔵

**Definition:** In a directed graph, an **SCC** is a maximal set of vertices where **every vertex is reachable from every other** vertex in the set.

### Kosaraju's Algorithm — Steps
1. Graph-এ **DFS** চালিয়ে finish time অনুযায়ী vertex গুলো **stack**-এ রাখো।
2. Graph-এর সব edge **উল্টে দাও** (transpose)।
3. Stack থেকে একে একে vertex নিয়ে **transposed graph-এ DFS** চালাও।
4. প্রতিটি DFS tree = **একটি SCC**।

**Time: O(V + E)** · **Tarjan's Algorithm** একই কাজ **একবার DFS**-এই করে।

---

## D3. A* Search 🔵

**Definition:** A **best-first search** that finds the shortest path using **f(n) = g(n) + h(n)**, where `g(n)` is cost from start and `h(n)` is a **heuristic** estimate to the goal.

| উপাদান | অর্থ |
|---|---|
| **g(n)** | Start থেকে এই node পর্যন্ত প্রকৃত খরচ |
| **h(n)** | এই node থেকে goal পর্যন্ত **আন্দাজ** (heuristic) |
| **f(n)** | মোট আন্দাজি খরচ = g + h |

⭐ **h(n) = 0 হলে A\* আসলে Dijkstra হয়ে যায়।**
**ব্যবহার:** Game pathfinding, GPS navigation, Robot planning

---

## D4. Warshall's Transitive Closure 🔵

Floyd-Warshall-এর মতোই, কিন্তু distance নয় — শুধু **"i থেকে j-তে যাওয়া যায় কিনা"** (0/1) বের করে।
```
reach[i][j] = reach[i][j] OR (reach[i][k] AND reach[k][j])
```
**Time: O(V³)**

---
---

# ★ সব মিলিয়ে চূড়ান্ত তালিকা

## Sorting — ১১টা ✅
Bubble · Selection · Insertion · **Shell** · Merge · Quick · Heap · Counting · Radix · **Bucket** · **Tim**

## Searching — ৭টা ✅
Linear · Binary · **Jump** · **Interpolation** · **Exponential** · **Ternary** · Hash

## Graph — ১৩টা ✅
BFS · DFS · Dijkstra · Bellman-Ford · Floyd-Warshall · Prim · Kruskal · Topological Sort · Ford-Fulkerson · **Union-Find** · **Kosaraju (SCC)** · **A\*** · **Warshall**

## String — ৩টা ✅
Naive · **KMP** · **Rabin-Karp**

## DP — ১০টা ✅
Fibonacci · 0/1 Knapsack · LCS · Matrix Chain · Floyd-Warshall · Bellman-Ford · Coin Change · LIS · Edit Distance · TSP

## Greedy — ৬টা ✅
Dijkstra · Prim · Kruskal · Huffman · Fractional Knapsack · Activity Selection

## Backtracking — ৬টা ✅
N-Queens · Sudoku · Graph Coloring · Hamiltonian Cycle · Subset Sum · Rat in a Maze

## Number — ৫টা ✅
Euclidean GCD · Primality (√n) · Sieve · Modular Exponentiation · Strassen

---

# ⚠️ কিন্তু এটা মনে রেখো

**Admission test-এ এই supplement-এর ৯০% আসবে না।** Sample paper-এ sorting/searching-এর একটাও প্রশ্ন ছিল না।

**যদি সময় কম থাকে, শুধু এইটুকু:**
1. **সম্পূর্ণ Sorting Master Table**-এর ৩টা কলাম: Worst case, Stable, In-place
2. **Searching Master Table**-এর ক্রম: `Hash O(1) < Binary O(log n) < Jump O(√n) < Linear O(n)`
3. **Union-Find → Kruskal-এ ব্যবহৃত** (এটা MCQ-তে আসে)
4. বাকিগুলো শুধু **নাম চিনে রাখো** — সংজ্ঞা জিজ্ঞেস করলে এক লাইনে বলতে পারলেই যথেষ্ট
