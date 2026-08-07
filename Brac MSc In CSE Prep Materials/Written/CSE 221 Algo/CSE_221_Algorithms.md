# CSE 221 — ALGORITHMS
### BRAC MSc CSE Admission — Complete Notes

> **এই ফাইলে শুধু Algorithm।** Data Structure আলাদা ফাইলে (CSE 220)।
>
> **পার্থক্যটা মাথায় গেঁথে নাও:**
> **Data Structure = data কীভাবে রাখা হবে (Storage)**
> **Algorithm = সেই data নিয়ে কী করা হবে (Process)**
>
> যেমন: **Binary Search Tree** = DS, কিন্তু **Binary Search** = Algorithm।

---
---

# MODULE 1 — ALGORITHM ANALYSIS

## Topic 1: Algorithm

### Definition (English)
An **Algorithm** is a **finite**, **step-by-step**, **well-defined** sequence of instructions to solve a particular problem.

⭐ **Keywords:** Finite · Step-by-step · Well-defined · Unambiguous

### Concept (বাংলায়)
Algorithm মানে সমস্যা সমাধানের একটা নির্দিষ্ট নিয়ম বা পদ্ধতি — কোনো নির্দিষ্ট programming language-এর সাথে এর সম্পর্ক নেই।
একই algorithm C, Java, Python — যেকোনো ভাষায় লেখা যায়।

### 5 Characteristics of an Algorithm ⭐⭐⭐ (মুখস্থ)

| # | Characteristic | অর্থ |
|---|---|---|
| 1 | **Input** | শূন্য বা তার বেশি input থাকবে |
| 2 | **Output** | অন্তত একটি output থাকতেই হবে |
| 3 | **Definiteness** | প্রতিটি step স্পষ্ট ও দ্ব্যর্থহীন |
| 4 | **Finiteness** | নির্দিষ্ট সংখ্যক step-এর পর অবশ্যই শেষ হবে |
| 5 | **Effectiveness** | প্রতিটি step বাস্তবে সম্পাদনযোগ্য |

⚠️ **Trap:** Input **শূন্যও** হতে পারে, কিন্তু Output **অন্তত একটি** থাকতেই হবে।

### Algorithm vs Program

| Algorithm | Program |
|---|---|
| Language-independent | নির্দিষ্ট language-এ লেখা |
| Design phase | Implementation phase |
| শেষ হতেই হবে (finite) | Infinite loop-ও চলতে পারে (যেমন OS) |
| Pseudocode/Flowchart | Executable code |

### 🔁 Admission Revision Box
Algorithm = finite, well-defined step-এর sequence। **৫টি বৈশিষ্ট্য: Input, Output, Definiteness, Finiteness, Effectiveness।** Input শূন্য হতে পারে, Output অন্তত ১টি লাগবেই। Algorithm language-independent, Program language-dependent।

---

## Topic 2: Asymptotic Notation ⭐⭐⭐ (সবচেয়ে গুরুত্বপূর্ণ টপিক)

### Definition (English)
**Asymptotic Notation** is a mathematical tool used to describe the **running time or space** of an algorithm as the **input size approaches infinity**, ignoring constants and lower-order terms.

⭐ **Keywords:** Growth Rate · Input Size (n) · Upper Bound · Lower Bound · Tight Bound

### Concept (বাংলায়)
আমরা algorithm-এর সময় সেকেন্ডে মাপি না — কারণ সেটা computer-ভেদে আলাদা হবে।
আমরা মাপি: **input বড় হলে কাজের পরিমাণ কত দ্রুত বাড়ে।**

Constant ও ছোট term বাদ দেওয়া হয়:
`3n² + 5n + 100` → **O(n²)**
কারণ n খুব বড় হলে `n²`-ই প্রাধান্য পায়।

### The Three Notations ⭐⭐⭐

| Notation | নাম | অর্থ | কোন case |
|---|---|---|---|
| **O (Big-O)** | Upper Bound | সর্বোচ্চ এত সময় লাগবে | **Worst Case** |
| **Ω (Big-Omega)** | Lower Bound | অন্তত এত সময় লাগবে | **Best Case** |
| **Θ (Big-Theta)** | Tight Bound | ঠিক এই হারেই বাড়বে | **Average / Exact** |

**সহজ ভাষায়:**
- **O** = "এর চেয়ে খারাপ হবে না"
- **Ω** = "এর চেয়ে ভালো হবে না"
- **Θ** = "উপর-নিচ দুটোই এক" (O এবং Ω একসাথে সত্য হলে Θ)

### Formula / Rules

| Notation | Formal Definition |
|---|---|
| f(n) = **O(g(n))** | ∃ c, n₀ > 0 : `f(n) ≤ c·g(n)` for all n ≥ n₀ |
| f(n) = **Ω(g(n))** | ∃ c, n₀ > 0 : `f(n) ≥ c·g(n)` for all n ≥ n₀ |
| f(n) = **Θ(g(n))** | ∃ c₁,c₂,n₀ : `c₁·g(n) ≤ f(n) ≤ c₂·g(n)` |

### Order of Growth ⭐⭐⭐ (এই ক্রম মুখস্থ — MCQ নিশ্চিত)

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

| Complexity | নাম | উদাহরণ |
|---|---|---|
| **O(1)** | Constant | Array access, Hash lookup |
| **O(log n)** | Logarithmic | Binary Search, BST search |
| **O(n)** | Linear | Linear Search, single loop |
| **O(n log n)** | Linearithmic | Merge/Heap/Quick Sort |
| **O(n²)** | Quadratic | Bubble/Selection/Insertion Sort, nested loop |
| **O(n³)** | Cubic | Floyd-Warshall, 3 nested loops |
| **O(2ⁿ)** | Exponential | Naive Fibonacci, Subset generation |
| **O(n!)** | Factorial | Travelling Salesman (brute force), Permutation |

### Rules for Simplification ⭐
1. **Constant বাদ:** `O(5n)` → **O(n)**
2. **Lower-order term বাদ:** `O(n² + n)` → **O(n²)**
3. **Sequential code:** যোগ হয়, বড়টা থাকে → `O(n) + O(n²)` = **O(n²)**
4. **Nested loop:** গুণ হয় → `O(n) × O(n)` = **O(n²)**
5. **Loop যেখানে i দ্বিগুণ হয়** (`i = i*2`) → **O(log n)**

### Quick Loop Analysis (MCQ-তে সরাসরি আসে)
```c
for(i=0; i<n; i++)              → O(n)

for(i=0; i<n; i++)
   for(j=0; j<n; j++)           → O(n²)

for(i=0; i<n; i++)
   for(j=0; j<i; j++)           → O(n²)   ⚠️ n/2 নয়, constant বাদ যায়

for(i=1; i<n; i=i*2)            → O(log n)

for(i=0; i<n; i++)
   for(j=1; j<n; j=j*2)         → O(n log n)
```

### ⚠️ Common MCQ Traps
- **Big-O = Worst case নয় সবসময়।** Big-O হলো upper bound; worst case-ও Ω বা Θ দিয়ে বলা যায়। তবে প্রচলিতভাবে O ≈ worst case ধরা হয়।
- `O(log n)`-এ base লেখা হয় না, কারণ base পরিবর্তন শুধু constant পরিবর্তন করে।
- `O(2n)` = `O(n)` ✅ কিন্তু `O(2ⁿ)` ≠ `O(n)` ❌ — এই দুটো গুলিয়ে ফেলবে না।
- `O(n²)` কি `O(n³)`? → **হ্যাঁ**, technically সত্য (upper bound), কিন্তু tight নয়।

### 🔁 Admission Revision Box
**O = Upper (worst), Ω = Lower (best), Θ = Tight (average)।** Growth order: **1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!**। Constant ও lower-order term বাদ যায়। Nested loop = গুণ, sequential = বড়টা। `i = i*2` loop = **O(log n)**।

---

## Topic 3: Recurrence Relation & Master Theorem

### Definition (English)
A **Recurrence Relation** expresses the running time of a recursive algorithm in terms of the running time on smaller inputs.

### Concept (বাংলায়)
Recursive algorithm-এর complexity সরাসরি বলা যায় না। তাই লিখি:
**T(n) = (ছোট problem-এর সময়) + (ভাগ ও জোড়া লাগানোর সময়)**

Merge Sort: `T(n) = 2T(n/2) + O(n)`
মানে — দুইটা অর্ধেক sort করো, তারপর O(n) সময়ে merge করো।

### Master Theorem ⭐⭐

For **T(n) = a·T(n/b) + f(n)**, where a ≥ 1, b > 1:

Compare **f(n)** with **n^(log_b a)**:

| Case | শর্ত | ফলাফল |
|---|---|---|
| **1** | f(n) ছোট (n^(log_b a) বড়) | **Θ(n^(log_b a))** |
| **2** | f(n) ≈ n^(log_b a) | **Θ(n^(log_b a) · log n)** |
| **3** | f(n) বড় | **Θ(f(n))** |

### Ready-Made Results ⭐ (মুখস্থ করে ফেলো, derive করার দরকার নেই)

| Recurrence | Algorithm | Complexity |
|---|---|---|
| T(n) = T(n/2) + O(1) | Binary Search | **O(log n)** |
| T(n) = 2T(n/2) + O(n) | Merge Sort | **O(n log n)** |
| T(n) = 2T(n/2) + O(1) | Tree Traversal | **O(n)** |
| T(n) = T(n−1) + O(1) | Factorial / Linear Search | **O(n)** |
| T(n) = T(n−1) + O(n) | Quick Sort (worst) | **O(n²)** |
| T(n) = 2T(n−1) + O(1) | Tower of Hanoi | **O(2ⁿ)** |
| T(n) = 7T(n/2) + O(n²) | Strassen's Matrix | **O(n^2.81)** |

### 🔁 Admission Revision Box
Recurrence = recursive algorithm-এর সময়ের সমীকরণ। **Master Theorem: T(n) = aT(n/b) + f(n)** — f(n)-কে n^(log_b a)-এর সাথে তুলনা করো। মুখস্থ: **Binary Search O(log n)**, **Merge Sort O(n log n)**, **Tower of Hanoi O(2ⁿ)**।

---
---

# MODULE 2 — ALGORITHM DESIGN TECHNIQUES ⭐⭐⭐

## Topic 1: Divide and Conquer

### Definition (English)
**Divide and Conquer** is an algorithm design paradigm that solves a problem by **dividing** it into smaller subproblems, **conquering** (solving) them recursively, and **combining** their solutions.

⭐ **Keywords:** Divide · Conquer · Combine · Recursion

### Concept (বাংলায়)
তিনটা ধাপ:
1. **Divide** — বড় সমস্যাকে ছোট ছোট ভাগে ভাঙো
2. **Conquer** — প্রতিটি ছোট ভাগ recursively সমাধান করো
3. **Combine** — ছোট সমাধানগুলো জোড়া লাগিয়ে বড় সমাধান বানাও

**Merge Sort-এ:** Array-কে অর্ধেক করো → দুই অর্ধেক sort করো → merge করো।

### Classic Examples ⭐

| Algorithm | Complexity |
|---|---|
| **Binary Search** | O(log n) |
| **Merge Sort** | O(n log n) |
| **Quick Sort** | Avg O(n log n), Worst O(n²) |
| **Strassen's Matrix Multiplication** | O(n^2.81) |
| **Closest Pair of Points** | O(n log n) |
| Karatsuba Multiplication | O(n^1.58) |

### Key Points
1. Subproblem-গুলো **independent** — একটার ফল অন্যটার উপর নির্ভর করে না। ⭐ (এটাই DP-র সাথে মূল পার্থক্য)
2. সাধারণত **recursion** দিয়ে implement করা হয়।
3. **Parallel processing**-এ ভালো কাজ করে (subproblem আলাদা করে চালানো যায়)।
4. Recursion-এর কারণে **extra stack space** লাগে।

### ⚠️ MCQ Trap
- **Binary Search** কি Divide & Conquer? → **হ্যাঁ** ✅ (যদিও এতে combine step নেই)
- **Quick Sort**-এ কাজ হয় **Divide (partition)** step-এ; **Merge Sort**-এ কাজ হয় **Combine (merge)** step-এ। ⭐

### 🔁 Admission Revision Box
D&C = **Divide → Conquer → Combine**, subproblem **independent**। উদাহরণ: **Binary Search, Merge Sort, Quick Sort, Strassen**। Quick Sort-এ কাজ Divide-এ, Merge Sort-এ কাজ Combine-এ।

---

## Topic 2: Greedy Algorithm

### Definition (English)
A **Greedy Algorithm** builds a solution step by step, always choosing the option that looks **best at the current moment (local optimum)**, hoping to reach the **global optimum**.

⭐ **Keywords:** Local Optimum · Greedy Choice Property · Optimal Substructure · No Backtracking

### Concept (বাংলায়)
Greedy মানে "এই মুহূর্তে যেটা সবচেয়ে ভালো, সেটাই নাও" — ভবিষ্যতের কথা ভাববে না, এবং সিদ্ধান্ত **কখনো বদলাবে না** (no backtracking)।

**Real Example — Coin Change:** ৭০ টাকা দিতে হবে, notes: 50, 20, 10, 5।
Greedy: 50 → বাকি 20 → 20 → শেষ। মোট 2টি note। ✅

⚠️ কিন্তু Greedy **সবসময় optimal দেয় না**। Coin = {1, 3, 4}, amount = 6 হলে Greedy দেবে 4+1+1 = 3 coin, কিন্তু optimal হলো 3+3 = **2 coin**।

### Two Required Properties ⭐
1. **Greedy Choice Property** — locally optimal choice নিয়ে globally optimal-এ পৌঁছানো যায়
2. **Optimal Substructure** — বড় সমস্যার optimal solution ছোট সমস্যার optimal solution দিয়ে গঠিত

### Classic Greedy Algorithms ⭐⭐⭐

| Algorithm | কাজ | Complexity |
|---|---|---|
| **Dijkstra's** | Single-source shortest path | O((V+E) log V) |
| **Prim's** | Minimum Spanning Tree | O(E log V) |
| **Kruskal's** | Minimum Spanning Tree | O(E log E) |
| **Huffman Coding** | Data compression | O(n log n) |
| **Fractional Knapsack** | Max value with weight limit | O(n log n) |
| **Activity Selection** | Max non-overlapping activities | O(n log n) |
| Job Sequencing with Deadline | Max profit | O(n²) |

### ⚠️ Common MCQ Traps ⭐⭐⭐
- **Fractional Knapsack → Greedy** ✅
- **0/1 Knapsack → Greedy দিয়ে হয় না, DP লাগে** ❌ — এটা প্রায় নিশ্চিত MCQ!
- **Dijkstra negative weight-এ কাজ করে না** ❌
- Greedy সবসময় optimal solution দেয় **না**।

### Greedy vs Dynamic Programming ⭐

| Feature | Greedy | Dynamic Programming |
|---|---|---|
| সিদ্ধান্ত | Local best, বদলায় না | সব option বিবেচনা করে |
| Backtrack | নেই | নেই, কিন্তু সব case দেখে |
| Speed | **দ্রুত** | ধীর |
| Memory | কম | বেশি (table লাগে) |
| Optimal? | সবসময় নয় | **সবসময় (যদি প্রযোজ্য হয়)** |
| উদাহরণ | Fractional Knapsack | **0/1 Knapsack** |

### 🔁 Admission Revision Box
Greedy = প্রতি ধাপে **locally best** choice, backtrack নেই, সবসময় optimal দেয় না। শর্ত: **Greedy Choice Property + Optimal Substructure**। উদাহরণ: **Dijkstra, Prim, Kruskal, Huffman, Fractional Knapsack, Activity Selection**। ⚠️ **0/1 Knapsack = DP, Greedy নয়।**

---

## Topic 3: Dynamic Programming (DP) ⭐⭐⭐

### Definition (English)
**Dynamic Programming** is an optimization technique that solves complex problems by breaking them into **overlapping subproblems**, solving each subproblem **only once**, and **storing** the results for reuse.

⭐ **Keywords:** Overlapping Subproblems · Optimal Substructure · Memoization · Tabulation

### Concept (বাংলায়)
Recursion-এ একই কাজ বারবার হয়। DP সেই ফলাফল **মনে রেখে দেয়**, তাই দ্বিতীয়বার আর হিসাব করতে হয় না।

**Fibonacci-র উদাহরণ:**
Naive recursion-এ `fib(3)` বহুবার হিসাব হয় → **O(2ⁿ)**
DP-তে একবার হিসাব করে সংরক্ষণ → **O(n)** ✅

### Two Required Conditions ⭐⭐
1. **Overlapping Subproblems** — একই subproblem বারবার আসে
2. **Optimal Substructure** — ছোট optimal solution দিয়ে বড় optimal solution গঠিত

⚠️ দুইটাই থাকতে হবে। Divide & Conquer-এ subproblem **overlap করে না** — এটাই মূল পার্থক্য।

### Two Approaches ⭐

| | **Memoization (Top-Down)** | **Tabulation (Bottom-Up)** |
|---|---|---|
| পদ্ধতি | Recursion + cache | Loop + table |
| শুরু | বড় থেকে ছোট | ছোট থেকে বড় |
| Stack | Recursion stack লাগে | লাগে না |
| যা লাগে | দরকারি subproblem-ই solve হয় | সব subproblem solve হয় |

### Classic DP Problems ⭐⭐⭐

| Problem | Complexity |
|---|---|
| **Fibonacci** | O(n) |
| **0/1 Knapsack** | O(n·W) |
| **Longest Common Subsequence (LCS)** | O(m·n) |
| **Matrix Chain Multiplication** | O(n³) |
| **Floyd-Warshall** (All-pairs shortest path) | O(V³) |
| **Bellman-Ford** | O(V·E) |
| Coin Change | O(n·amount) |
| Longest Increasing Subsequence | O(n²) or O(n log n) |
| Edit Distance | O(m·n) |
| Travelling Salesman (DP) | O(n²·2ⁿ) |

### Comparison: D&C vs DP ⭐

| Feature | Divide & Conquer | Dynamic Programming |
|---|---|---|
| Subproblem | **Independent** | **Overlapping** |
| Result store? | না | **হ্যাঁ (memo/table)** |
| Recompute? | হ্যাঁ | না |
| উদাহরণ | Merge Sort, Binary Search | Knapsack, LCS, Floyd-Warshall |

### ⚠️ Common MCQ Traps
- **Merge Sort কি DP?** → **না**, Divide & Conquer (subproblem overlap করে না)।
- **0/1 Knapsack = DP** ✅, **Fractional Knapsack = Greedy** ✅ — এই জোড়া মুখস্থ।
- **Floyd-Warshall = DP**, **Dijkstra = Greedy** ⭐
- DP সবসময় বেশি memory নেয় (space-time tradeoff)।

### 🔁 Admission Revision Box
DP = **Overlapping Subproblems + Optimal Substructure**, result store করে reuse। দুই ধরন: **Memoization (top-down)**, **Tabulation (bottom-up)**। উদাহরণ: **0/1 Knapsack, LCS, Matrix Chain, Floyd-Warshall, Bellman-Ford, Fibonacci**। D&C-এ subproblem independent, DP-তে overlapping।

---

## Topic 4: Backtracking

### Definition (English)
**Backtracking** is an algorithmic technique that builds a solution incrementally and **abandons (backtracks from) a partial solution** as soon as it determines that it cannot lead to a valid complete solution.

⭐ **Keywords:** Incremental · Trial and Error · Prune · State-Space Tree

### Concept (বাংলায়)
Backtracking = **চেষ্টা করো, ভুল হলে পিছিয়ে যাও, অন্য পথ চেষ্টা করো।**

একটা সম্ভাব্য সমাধান তৈরি করতে থাকো। যদি বুঝতে পারো এই পথে সমাধান হবে না, তখন এক ধাপ পিছিয়ে (backtrack) অন্য option চেষ্টা করো।

**Real Example — Sudoku:** একটা ঘরে সংখ্যা বসাও। পরে যদি দেখো কোনো সংখ্যাই বসছে না, তাহলে আগের ঘরে ফিরে গিয়ে অন্য সংখ্যা বসাও।

### Classic Backtracking Problems ⭐

| Problem | কাজ |
|---|---|
| **N-Queens** | n×n board-এ n queen বসানো যেন কেউ কাউকে আক্রমণ না করে |
| **Sudoku Solver** | Grid পূরণ |
| **Graph Coloring** | পাশাপাশি vertex-এ ভিন্ন রঙ |
| **Hamiltonian Cycle** | সব vertex একবার করে ঘুরে ফেরত আসা |
| **Subset Sum** | কোন subset-এর যোগফল দেওয়া মানের সমান |
| **Rat in a Maze** | Maze থেকে বের হওয়ার পথ |

### Key Points
1. Backtracking মূলত **DFS on a state-space tree**।
2. **Recursion** দিয়ে implement করা হয়।
3. **Pruning** — খারাপ শাখা তাড়াতাড়ি কেটে দিলে অনেক সময় বাঁচে।
4. Complexity সাধারণত **exponential O(2ⁿ)** বা তার বেশি।
5. **Branch and Bound** = Backtracking-এর optimization version (optimization problem-এ ব্যবহৃত)।

### Comparison

| Backtracking | Branch and Bound |
|---|---|
| সব solution খোঁজে | **Optimal** solution খোঁজে |
| DFS ব্যবহার করে | BFS / Best-first ব্যবহার করে |
| Feasibility check | Bound function দিয়ে prune |
| N-Queens, Sudoku | 0/1 Knapsack, TSP |

### 🔁 Admission Revision Box
Backtracking = **incremental build + অকার্যকর হলে পিছিয়ে যাওয়া**। মূলত **DFS on state-space tree**, recursion দিয়ে। উদাহরণ: **N-Queens, Sudoku, Graph Coloring, Hamiltonian Cycle, Subset Sum**। Complexity সাধারণত exponential। Branch & Bound = এর optimization version।

---
---

# MODULE 3 — SORTING ALGORITHMS ⭐⭐⭐

## Topic 1: Sorting Overview

### Definition (English)
**Sorting** is the process of arranging elements of a list in a particular order — **ascending** or **descending**.

### Two Important Terms ⭐⭐⭐

**Stable Sort:** সমান মানের element-দের **আপেক্ষিক ক্রম** sort-এর পরও একই থাকে।
**In-place Sort:** অতিরিক্ত memory প্রায় লাগে না — **O(1) extra space**।

| Algorithm | **Stable?** | **In-place?** |
|---|---|---|
| Bubble Sort | ✅ হ্যাঁ | ✅ হ্যাঁ |
| Insertion Sort | ✅ হ্যাঁ | ✅ হ্যাঁ |
| **Selection Sort** | ❌ **না** | ✅ হ্যাঁ |
| **Merge Sort** | ✅ হ্যাঁ | ❌ **না** (O(n) লাগে) |
| **Quick Sort** | ❌ **না** | ✅ হ্যাঁ |
| **Heap Sort** | ❌ **না** | ✅ হ্যাঁ |
| Counting Sort | ✅ হ্যাঁ | ❌ না |

⭐ **মুখস্থ shortcut:** **Unstable = Selection, Quick, Heap** (SQH)। বাকিরা stable।

---

## Topic 2: Sorting Algorithms — একে একে

### 1. Bubble Sort
পাশাপাশি দুটো element তুলনা করে বড়টাকে ডানে পাঠানো। প্রতি pass-এ সবচেয়ে বড় element শেষে চলে যায় (বুদবুদের মতো ভেসে ওঠে)।
- Best **O(n)** (swap flag optimization থাকলে, already sorted হলে), Avg/Worst **O(n²)**, Space **O(1)**
- Stable ✅, In-place ✅

### 2. Selection Sort
প্রতি pass-এ বাকি অংশের সবচেয়ে ছোট element খুঁজে সামনে আনা।
- Best/Avg/Worst **সবই O(n²)** ⭐ (already sorted হলেও O(n²) — এটাই এর বৈশিষ্ট্য)
- Space O(1), **Unstable** ❌
- **Swap সংখ্যা সবচেয়ে কম (n−1)** — memory write খরচ বেশি হলে ভালো

### 3. Insertion Sort
তাস সাজানোর মতো — প্রতিটি element-কে তার সঠিক জায়গায় ঢুকিয়ে দেওয়া।
- Best **O(n)** (already sorted), Avg/Worst **O(n²)**, Space O(1)
- Stable ✅, In-place ✅
- **ছোট বা প্রায়-sorted array-তে সবচেয়ে ভালো** ⭐

### 4. Merge Sort ⭐
Divide & Conquer — array অর্ধেক ভাগ করে, recursively sort করে, তারপর merge করে।
- Best/Avg/**Worst সবই O(n log n)** ⭐ (guaranteed)
- Space **O(n)** ❌ — extra array লাগে
- Stable ✅
- **Linked List sort করার জন্য সেরা** (random access লাগে না)
- **External sorting**-এ ব্যবহৃত (বিশাল file, RAM-এ আঁটে না)

### 5. Quick Sort ⭐⭐⭐
একটি **pivot** নিয়ে partition করা — pivot-এর বামে ছোট, ডানে বড়।
- Best/Avg **O(n log n)**, **Worst O(n²)** ⚠️
- Worst case কখন? → **pivot সবসময় সবচেয়ে ছোট/বড় হলে** (already sorted array-তে first element pivot নিলে)
- Space **O(log n)** (recursion stack)
- **Unstable** ❌, In-place ✅
- **বাস্তবে সবচেয়ে দ্রুত** — cache-friendly, constant factor ছোট ⭐

### 6. Heap Sort
Max-Heap বানিয়ে বারবার root (max) বের করে শেষে বসানো।
- Best/Avg/**Worst সবই O(n log n)** ⭐
- Space **O(1)** ⭐ — Merge Sort-এর চেয়ে এখানেই সুবিধা
- **Unstable** ❌

### 7. Counting Sort (Non-comparison)
প্রতিটি মান কতবার আছে গুনে রাখা। তুলনা করে না, তাই O(n log n)-এর সীমা ভাঙতে পারে।
- **O(n + k)** যেখানে k = মানের পরিসর
- শুধুমাত্র **integer / সীমিত range**-এর জন্য

### 8. Radix Sort
অঙ্ক ধরে ধরে (unit, tens, hundreds) sort করা, ভিতরে Counting Sort ব্যবহার করে।
- **O(d × (n + k))**, d = সর্বোচ্চ অঙ্ক সংখ্যা

---

## Sorting Master Table ⭐⭐⭐ (এটাই সবচেয়ে বেশি আসা টেবিল)

| Algorithm | Best | Average | Worst | Space | Stable | Method |
|---|---|---|---|---|---|---|
| **Bubble Sort** | **O(n)** | O(n²) | O(n²) | O(1) | ✅ | Exchange |
| **Selection Sort** | **O(n²)** | O(n²) | O(n²) | O(1) | ❌ | Selection |
| **Insertion Sort** | **O(n)** | O(n²) | O(n²) | O(1) | ✅ | Insertion |
| **Merge Sort** | O(n log n) | O(n log n) | **O(n log n)** | **O(n)** | ✅ | D&C |
| **Quick Sort** | O(n log n) | O(n log n) | **O(n²)** ⚠️ | O(log n) | ❌ | D&C |
| **Heap Sort** | O(n log n) | O(n log n) | **O(n log n)** | **O(1)** | ❌ | Selection |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | Counting |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ | Digit |

### ⚠️ Top Sorting MCQ Traps ⭐⭐⭐
1. **Selection Sort-এর Best Case-ও O(n²)** — already sorted হলেও কমে না
2. **Quick Sort-এর Worst Case O(n²)** — already sorted array-তে, first element pivot নিলে
3. **Merge Sort in-place নয়** — O(n) extra space লাগে
4. **Heap Sort in-place, কিন্তু unstable**
5. **Quick Sort বাস্তবে দ্রুততম** যদিও Merge Sort-এর worst case ভালো
6. **Comparison-based sorting-এর lower bound = Ω(n log n)** ⭐ — এর চেয়ে দ্রুত করা অসম্ভব
7. **Counting/Radix Sort O(n log n)-এর চেয়ে দ্রুত** কারণ এরা comparison করে না
8. **Linked List sort করতে Merge Sort সেরা** (Quick Sort নয় — random access নেই)

### কোন Sort কখন?
| পরিস্থিতি | সেরা Sort |
|---|---|
| সাধারণ, দ্রুত চাই | **Quick Sort** |
| Worst case guarantee চাই | **Merge / Heap Sort** |
| Memory কম, guarantee চাই | **Heap Sort** |
| Stability চাই | **Merge Sort** |
| ছোট বা প্রায়-sorted data | **Insertion Sort** |
| Linked List | **Merge Sort** |
| ছোট range-এর integer | **Counting Sort** |
| বিশাল file (external) | **Merge Sort** |

### 🔁 Admission Revision Box
**O(n²): Bubble, Selection, Insertion** (Selection-এর best-ও O(n²))। **O(n log n): Merge, Quick (avg), Heap**। **Quick worst = O(n²)**। **Merge = O(n) space, stable**; **Heap = O(1) space, unstable**। **Unstable = Selection, Quick, Heap**। Comparison sorting-এর সীমা **Ω(n log n)**; Counting/Radix তুলনা করে না বলে দ্রুত।

---
---

# MODULE 4 — SEARCHING ALGORITHMS

## Topic 1: Linear Search

### Definition (English)
**Linear Search** sequentially checks each element of a list until the target is found or the list ends.

### Key Points
- Sorted হওয়ার **দরকার নেই** ✅
- Best **O(1)** (প্রথমেই পেলে), Average/Worst **O(n)**
- Space O(1)
- যেকোনো data structure-এ কাজ করে (Array, Linked List)

## Topic 2: Binary Search ⭐⭐⭐

### Definition (English)
**Binary Search** finds an element in a **sorted** array by repeatedly dividing the search interval **in half**, comparing the target with the **middle** element.

⭐ **Keywords:** Sorted Array (আবশ্যক) · Middle · Divide in Half

### Concept (বাংলায়)
মাঝের element-এর সাথে তুলনা করো:
- সমান → পেয়ে গেছি
- ছোট → বাম অর্ধেকে খোঁজো
- বড় → ডান অর্ধেকে খোঁজো

প্রতিবার অর্ধেক বাদ পড়ে যায় — তাই **O(log n)**।

**Example:** 1000 element-এ Linear Search-এ সর্বোচ্চ 1000 comparison, Binary Search-এ মাত্র **10** (log₂1000 ≈ 10)।

### Formula
```
mid = low + (high − low) / 2
```
⚠️ `(low + high)/2` না লিখে এভাবে লিখলে **integer overflow** এড়ানো যায় — এটাও MCQ-তে আসে।

**Maximum comparisons = ⌊log₂ n⌋ + 1**

### Key Points ⭐
1. **Array অবশ্যই sorted হতে হবে** — না হলে ভুল ফল দেবে।
2. **Random access দরকার** → Linked List-এ Binary Search **কার্যকর নয়** ❌ (O(n) হয়ে যায়)
3. Iterative version-এর space **O(1)**; Recursive version-এর **O(log n)**
4. Binary Search একটি **Divide & Conquer** algorithm।

### Comparison ⭐

| Feature | Linear Search | Binary Search |
|---|---|---|
| Sorted লাগে? | **না** | **হ্যাঁ** |
| Time | O(n) | **O(log n)** |
| Data Structure | যেকোনো | **Array (random access)** |
| ছোট data-তে | ভালো | overhead বেশি |

### 🔁 Admission Revision Box
Linear Search: sorted লাগে না, **O(n)**। Binary Search: **sorted array আবশ্যক**, প্রতিবার অর্ধেক বাদ, **O(log n)**, max comparison ⌊log₂n⌋+1। Linked List-এ Binary Search কার্যকর নয়। Iterative space O(1), recursive O(log n)।

---
---

# MODULE 5 — GRAPH ALGORITHMS ⭐⭐⭐

## Topic 1: BFS (Breadth First Search)

### Definition (English)
**BFS** traverses a graph **level by level**, visiting all neighbours of a vertex before moving to the next level. It uses a **Queue**.

⭐ **Keywords:** Level by Level · **Queue** · FIFO · Shortest path (unweighted)

### Concept (বাংলায়)
Start vertex থেকে শুরু করে **প্রথমে সব প্রতিবেশী**, তারপর তাদের প্রতিবেশী — এভাবে স্তরে স্তরে ছড়িয়ে যাওয়া।

**Real Example:** Facebook-এ "People You May Know" — তোমার বন্ধু, তারপর বন্ধুর বন্ধু।

### Key Points ⭐
1. **Queue** ব্যবহার করে (FIFO)
2. **Unweighted graph-এ shortest path দেয়** ⭐⭐⭐ — এটা নিশ্চিত MCQ
3. Time **O(V + E)** (adjacency list), **O(V²)** (adjacency matrix)
4. Space **O(V)** — queue + visited array
5. ব্যবহার: Shortest path (unweighted), Level order traversal, Web crawler, Social network, Connected components

## Topic 2: DFS (Depth First Search)

### Definition (English)
**DFS** traverses a graph by going as **deep as possible** along each branch before **backtracking**. It uses a **Stack** (or recursion).

⭐ **Keywords:** Depth · **Stack / Recursion** · Backtrack

### Concept (বাংলায়)
একটা পথ ধরে যতদূর যাওয়া যায় যাও। আর যাওয়ার জায়গা না থাকলে পিছিয়ে এসে অন্য পথ ধরো।

### Key Points ⭐
1. **Stack** বা **Recursion** ব্যবহার করে (LIFO)
2. **Shortest path দেয় না** ❌
3. Time **O(V + E)**, Space **O(V)**
4. ব্যবহার: **Cycle detection**, **Topological Sort**, Connected components, Maze solving, Path finding

### BFS vs DFS ⭐⭐⭐ (এই টেবিল থেকে MCQ প্রায় নিশ্চিত)

| Feature | **BFS** | **DFS** |
|---|---|---|
| Data Structure | **Queue** | **Stack / Recursion** |
| পদ্ধতি | Level by level | যতদূর গভীরে যাওয়া যায় |
| Shortest path (unweighted) | ✅ **দেয়** | ❌ দেয় না |
| Time | O(V + E) | O(V + E) |
| Space | O(V) (width) | O(V) (depth) |
| ভালো যখন | লক্ষ্য কাছে | লক্ষ্য গভীরে |
| প্রধান ব্যবহার | Shortest path, Level order | Cycle detection, Topological sort |

---

## Topic 3: Shortest Path Algorithms ⭐⭐⭐

### Dijkstra's Algorithm
**Definition:** Finds the **shortest path from a single source** to all other vertices in a **weighted graph with non-negative weights**.

- **Greedy** algorithm
- ⚠️ **Negative weight-এ কাজ করে না** — সবচেয়ে বেশি আসা trap
- Time: **O(V²)** (matrix) বা **O((V+E) log V)** (Min-Heap/Priority Queue)
- Real use: **Google Maps**, network routing

### Bellman-Ford Algorithm
**Definition:** Finds shortest paths from a single source, and **works with negative edge weights**. Can **detect negative cycles**.

- **Dynamic Programming** based
- Time: **O(V·E)** — Dijkstra-র চেয়ে ধীর
- ✅ Negative weight handle করে, negative cycle ধরতে পারে

### Floyd-Warshall Algorithm
**Definition:** Finds shortest paths between **all pairs** of vertices.

- **Dynamic Programming**, 3টি nested loop
- Time: **O(V³)**, Space: **O(V²)**
- Negative weight ✅ (negative cycle নয়)

### Comparison Table ⭐⭐⭐

| Algorithm | Type | Negative Weight | Time | Source |
|---|---|---|---|---|
| **BFS** | — | শুধু unweighted | O(V+E) | Single |
| **Dijkstra** | **Greedy** | ❌ **না** | O((V+E) log V) | Single |
| **Bellman-Ford** | **DP** | ✅ হ্যাঁ | **O(V·E)** | Single |
| **Floyd-Warshall** | **DP** | ✅ হ্যাঁ | **O(V³)** | **All pairs** |

---

## Topic 4: Minimum Spanning Tree (MST)

### Definition (English)
A **Minimum Spanning Tree** is a subset of edges that connects **all vertices** with the **minimum total edge weight** and **no cycles**.

⭐ MST-তে edge সংখ্যা সবসময় **V − 1**।

### Prim's vs Kruskal's ⭐

| Feature | **Prim's** | **Kruskal's** |
|---|---|---|
| পদ্ধতি | **Vertex** ধরে বাড়ে | **Edge** ধরে বাড়ে |
| শুরু | যেকোনো একটি vertex থেকে | সবচেয়ে ছোট edge থেকে |
| Data Structure | **Priority Queue / Min-Heap** | **Union-Find (Disjoint Set)** |
| Time | O(E log V) | **O(E log E)** |
| ভালো যেখানে | **Dense** graph | **Sparse** graph |
| Type | Greedy | Greedy |

---

## Topic 5: Topological Sort

### Definition (English)
**Topological Sort** is a **linear ordering** of vertices in a **Directed Acyclic Graph (DAG)** such that for every edge u→v, u comes **before** v.

### Key Points
1. শুধুমাত্র **DAG**-এ সম্ভব ⭐ (cycle থাকলে হবে না)
2. Time **O(V + E)**
3. দুই পদ্ধতি: **DFS-based** ও **Kahn's Algorithm** (in-degree based, BFS)
4. ব্যবহার: **Course prerequisite** ordering, Build system (Makefile), Task scheduling

**Real Example:** CSE 220 করার আগে CSE 111 করতে হবে — এই dependency-র সঠিক ক্রম বের করাই topological sort।

## Topic 6: Network Flow (সংক্ষেপে — Low Priority)
- **Max-Flow Min-Cut Theorem:** সর্বোচ্চ flow = সর্বনিম্ন cut-এর capacity
- **Ford-Fulkerson** algorithm — O(E × max_flow)
- **Edmonds-Karp** (BFS ব্যবহার করে) — O(V·E²)
- ব্যবহার: Network bandwidth, Bipartite matching

### 🔁 Admission Revision Box (Graph Algorithms)
**BFS = Queue = unweighted shortest path**, **DFS = Stack = cycle detection/topological sort**, দুটোই **O(V+E)**। **Dijkstra = Greedy, negative weight-এ না**। **Bellman-Ford = DP, O(VE), negative OK**। **Floyd-Warshall = DP, O(V³), all-pairs**। **MST edge = V−1**; **Prim = vertex/heap/dense**, **Kruskal = edge/union-find/sparse**। **Topological Sort শুধু DAG-এ, O(V+E)**।

---
---

# MODULE 6 — ADVANCED TOPICS

## Topic 1: Amortized Analysis

### Definition (English)
**Amortized Analysis** determines the **average cost per operation over a sequence of operations**, ensuring the average is small even if one operation is expensive.

### Concept (বাংলায়)
কিছু operation মাঝে মাঝে খুব ব্যয়বহুল হয়, কিন্তু বেশিরভাগ সময় সস্তা। গড় করলে দেখা যায় খরচ আসলে কম।

**Classic Example — Dynamic Array (Python `list`, Java `ArrayList`):**
Array ভরে গেলে দ্বিগুণ আকারের নতুন array বানিয়ে সব copy করতে হয় → সেই একটি insert **O(n)**।
কিন্তু এটা খুব কম হয়। n বার insert-এর মোট খরচ ভাগ করলে প্রতিটির গড় = **O(1) amortized**। ⭐

### Three Methods
1. **Aggregate Method** — মোট খরচ ÷ operation সংখ্যা
2. **Accounting Method** — সস্তা operation থেকে "credit" জমিয়ে ব্যয়বহুলটার খরচ মেটানো
3. **Potential Method** — একটি potential function দিয়ে হিসাব

### Key Points
1. **Amortized ≠ Average case।** ⭐ Amortized হলো worst-case sequence-এর গড় (কোনো probability নেই); Average case হলো input-এর probability-ভিত্তিক গড়।
2. Dynamic Array insert = **O(1) amortized**
3. Union-Find with path compression ≈ O(α(n)) amortized (প্রায় constant)

### 🔁 Admission Revision Box
Amortized Analysis = পরপর অনেক operation-এর **গড় খরচ**। উদাহরণ: **Dynamic Array (ArrayList) insert = O(1) amortized**, যদিও মাঝে মাঝে resize-এ O(n) লাগে। পদ্ধতি: Aggregate, Accounting, Potential। **Amortized ≠ Average case**।

---

## Topic 2: P, NP, NP-Hard, NP-Complete ⭐

### Definitions (English)

| Class | Definition |
|---|---|
| **P** | Problems **solvable** in polynomial time by a deterministic machine |
| **NP** | Problems whose solutions can be **verified** in polynomial time |
| **NP-Hard** | At least as hard as the hardest NP problems (**need not be in NP**) |
| **NP-Complete** | **In NP AND NP-Hard** — both conditions |

### Concept (বাংলায়)
- **P** = দ্রুত **সমাধান** করা যায়
- **NP** = দ্রুত **যাচাই** করা যায় (সমাধান দেওয়া থাকলে ঠিক কিনা দেখা যায়)
- **NP-Complete** = NP-এর সবচেয়ে কঠিন সমস্যা। একটার polynomial solution পেলে **সবগুলোরই** পাওয়া যাবে।
- **NP-Hard** = NP-Complete-এর মতো কঠিন বা তার চেয়ে বেশি, কিন্তু NP-তে না-ও থাকতে পারে

**সম্পর্ক:** **P ⊆ NP**। সবচেয়ে বড় অমীমাংসিত প্রশ্ন: **P = NP?** (এখনো কেউ জানে না)

### Examples ⭐

| Class | উদাহরণ |
|---|---|
| **P** | Sorting, Binary Search, Shortest Path (Dijkstra), MST |
| **NP-Complete** | **SAT** (প্রথম প্রমাণিত), 3-SAT, **Travelling Salesman (decision)**, **0/1 Knapsack**, Graph Coloring, Hamiltonian Cycle, Subset Sum, Vertex Cover, Clique |
| **NP-Hard** | **Halting Problem**, TSP (optimization version) |

### ⚠️ Common MCQ Traps
- **প্রথম NP-Complete problem = SAT (Boolean Satisfiability)** — Cook's Theorem ⭐
- **NP-Complete = NP + NP-Hard** ✅ (দুটোই লাগবে)
- **Halting Problem = NP-Hard কিন্তু NP-Complete নয়** (এটা undecidable, NP-তে নেই)
- P ⊆ NP ✅, কিন্তু P = NP কিনা **অজানা**

### 🔁 Admission Revision Box
**P** = polynomial time-এ solve করা যায়। **NP** = polynomial time-এ verify করা যায়। **NP-Hard** = অন্তত NP-এর সবচেয়ে কঠিনের সমান। **NP-Complete = NP ∩ NP-Hard**। **P ⊆ NP**, P=NP অমীমাংসিত। **প্রথম NPC = SAT (Cook's Theorem)**। NPC উদাহরণ: TSP, 0/1 Knapsack, Graph Coloring, Hamiltonian Cycle।

---

## Topic 3: Integer & Numeric Algorithms

### 1. Euclidean Algorithm (GCD) ⭐
**Definition:** Computes the **Greatest Common Divisor** of two integers using repeated division.

**Rule:** `GCD(a, b) = GCD(b, a mod b)`, and `GCD(a, 0) = a`

**Example — GCD(48, 18):**
```
GCD(48,18) → 48 mod 18 = 12
GCD(18,12) → 18 mod 12 = 6
GCD(12,6)  → 12 mod 6  = 0
GCD(6,0)   → 6  ✅
```
**Complexity: O(log(min(a, b)))** ⭐

**LCM Formula:** `LCM(a,b) = (a × b) / GCD(a,b)` ⭐

### 2. Primality Test
- **Naive:** 2 থেকে n−1 পর্যন্ত ভাগ → O(n)
- **Optimized:** শুধু **√n** পর্যন্ত দেখলেই হয় → **O(√n)** ⭐
- **Sieve of Eratosthenes:** 1 থেকে n পর্যন্ত সব prime বের করা → **O(n log log n)** ⭐
- **Miller-Rabin:** Probabilistic, খুব বড় সংখ্যার জন্য (RSA-তে ব্যবহৃত)

### 3. Modular Exponentiation
`(a^b) mod m` হিসাব করা **O(log b)** সময়ে (fast/binary exponentiation)। RSA cryptography-র ভিত্তি।

### 4. Matrix & Polynomial (Low Priority)
| Algorithm | Complexity |
|---|---|
| Naive Matrix Multiplication | O(n³) |
| **Strassen's Multiplication** | **O(n^2.81)** ⭐ |
| **Horner's Rule** (polynomial evaluation) | **O(n)** |
| **FFT** (polynomial multiplication) | **O(n log n)** |

### 🔁 Admission Revision Box
**GCD (Euclidean): GCD(a,b) = GCD(b, a mod b), O(log min(a,b))**। **LCM = (a×b)/GCD**। Primality test **O(√n)**, Sieve **O(n log log n)**। Modular exponentiation **O(log b)**। **Strassen O(n^2.81)**, Horner's Rule **O(n)**, FFT **O(n log n)**।

---
---

# 📋 CSE 221 — FINAL ONE-PAGE REVISION

## Design Technique Classification ⭐⭐⭐ (মুখস্থ করার সবচেয়ে দরকারি টেবিল)

| Algorithm | Technique |
|---|---|
| Binary Search | **Divide & Conquer** |
| Merge Sort | **Divide & Conquer** |
| Quick Sort | **Divide & Conquer** |
| Strassen's Matrix | **Divide & Conquer** |
| **Dijkstra's** | **Greedy** |
| **Prim's / Kruskal's** | **Greedy** |
| **Huffman Coding** | **Greedy** |
| **Fractional Knapsack** | **Greedy** |
| Activity Selection | **Greedy** |
| **0/1 Knapsack** | **Dynamic Programming** |
| **LCS / Edit Distance** | **Dynamic Programming** |
| **Matrix Chain Multiplication** | **Dynamic Programming** |
| **Floyd-Warshall** | **Dynamic Programming** |
| **Bellman-Ford** | **Dynamic Programming** |
| **N-Queens / Sudoku** | **Backtracking** |
| **Graph Coloring / Hamiltonian** | **Backtracking** |

## Complexity Cheat Sheet

| Algorithm | Time | Space |
|---|---|---|
| Linear Search | O(n) | O(1) |
| Binary Search | **O(log n)** | O(1) |
| Bubble / Selection / Insertion | **O(n²)** | O(1) |
| Merge Sort | **O(n log n)** | **O(n)** |
| Quick Sort | O(n log n) avg / **O(n²)** worst | O(log n) |
| Heap Sort | **O(n log n)** | **O(1)** |
| Counting Sort | O(n+k) | O(k) |
| BFS / DFS | **O(V+E)** | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |
| Bellman-Ford | **O(V·E)** | O(V) |
| Floyd-Warshall | **O(V³)** | O(V²) |
| Prim's | O(E log V) | O(V) |
| Kruskal's | O(E log E) | O(V) |
| Topological Sort | O(V+E) | O(V) |
| GCD (Euclid) | O(log n) | O(1) |
| Sieve of Eratosthenes | O(n log log n) | O(n) |

## 20 Guaranteed-Type MCQ Facts
1. Growth order: **1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!**
2. **O = worst (upper), Ω = best (lower), Θ = tight**
3. Comparison sorting-এর lower bound = **Ω(n log n)**
4. **Selection Sort-এর best case-ও O(n²)**
5. **Quick Sort worst case = O(n²)** (sorted array + first pivot)
6. **Merge Sort = O(n) space, stable, guaranteed O(n log n)**
7. **Heap Sort = O(1) space, unstable**
8. **Unstable sorts: Selection, Quick, Heap**
9. **Binary Search-এ array sorted থাকতেই হবে**
10. **BFS = Queue, DFS = Stack** — দুটোই O(V+E)
11. **BFS unweighted graph-এ shortest path দেয়**
12. **Dijkstra negative weight-এ কাজ করে না** — Bellman-Ford লাগবে
13. **Floyd-Warshall = O(V³), all-pairs, DP**
14. **MST-এ edge = V − 1**
15. **Fractional Knapsack = Greedy, 0/1 Knapsack = DP**
16. **DP = Overlapping subproblems + Optimal substructure**
17. **D&C-এ subproblem independent, DP-তে overlapping**
18. **Topological Sort শুধু DAG-এ**
19. **NP-Complete = NP ∩ NP-Hard; প্রথমটি = SAT**
20. **Dynamic Array insert = O(1) amortized**

## DS vs Algo — বিভ্রান্তি দূর করার টেবিল ⭐

| এটি Data Structure (CSE 220) | এটি Algorithm (CSE 221) |
|---|---|
| Binary Search **Tree** | Binary **Search** |
| **Heap** (structure) | **Heap Sort** |
| **Hash Table** | **Hashing function / probing** |
| **Graph** (Matrix/List) | **BFS, DFS, Dijkstra, Prim** |
| **Stack, Queue** | **Recursion, Backtracking** |
| **Priority Queue** | **Dijkstra, Huffman** |
| **Array, Linked List** | **Sorting algorithms** |
