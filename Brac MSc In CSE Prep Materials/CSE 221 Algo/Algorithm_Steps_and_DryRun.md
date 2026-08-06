# ⚙️ ALGORITHM STEPS + DRY RUN
### প্রতিটা Algorithm কীভাবে কাজ করে — ধাপে ধাপে

> **কীভাবে পড়বে:** প্রথমে **Steps** পড়ো, তারপর **Dry Run**-এ নিজের খাতায় হাতে করে মিলাও।
> Dry run নিজে হাতে একবার করলেই process মাথায় বসে যাবে — শুধু পড়লে হবে না।

---

## 📑 সূচি

| # | বিভাগ | Algorithms |
|---|---|---|
| A | **Searching** | Linear · Binary |
| B | **Sorting** | Bubble · Selection · Insertion · Merge · Quick · Heap · Counting |
| C | **Stack/Queue** | Push/Pop · Enqueue/Dequeue · Infix→Postfix · Bracket Matching |
| D | **Linked List** | Insert · Delete · Reverse |
| E | **Tree** | Traversals · BST Search/Insert/Delete · Level Order |
| F | **Heap** | Insert · Delete · Heapify · Heap Sort |
| G | **Hashing** | Insert · Search · Chaining · Linear Probing |
| H | **Graph** | BFS · DFS · Dijkstra · Bellman-Ford · Floyd-Warshall · Prim · Kruskal · Topological Sort |
| I | **DP / Greedy** | Fibonacci · 0/1 Knapsack · LCS · Fractional Knapsack · Activity Selection · Huffman |
| J | **Backtracking** | N-Queens |
| K | **Number** | GCD · Sieve · Primality |

---
---

# A. SEARCHING

## A1. Linear Search

### Steps
1. `i = 0` থেকে শুরু করো।
2. `A[i]` কে target-এর সাথে তুলনা করো।
3. মিলে গেলে → **index return করো, শেষ**।
4. না মিললে → `i = i + 1`।
5. Array শেষ হয়ে গেলে → **"Not Found" return করো**।

### Dry Run
`A = [10, 25, 8, 40, 15]`, target = **40**
```
i=0 → 10 ≠ 40
i=1 → 25 ≠ 40
i=2 →  8 ≠ 40
i=3 → 40 = 40  ✅ Found at index 3
```
**4 comparisons** · Time **O(n)** · Sorted লাগে না

---

## A2. Binary Search ⭐⭐⭐

### Steps
1. **Array sorted হতে হবে** (না হলে আগে sort করো)।
2. `low = 0`, `high = n − 1` সেট করো।
3. `mid = low + (high − low) / 2` বের করো।
4. তিনটা case:
   - `A[mid] == target` → **পেয়ে গেছি, return mid**
   - `A[mid] > target` → target বামে আছে → `high = mid − 1`
   - `A[mid] < target` → target ডানে আছে → `low = mid + 1`
5. `low ≤ high` যতক্ষণ, ধাপ 3–4 আবার করো।
6. `low > high` হয়ে গেলে → **Not Found**।

### Dry Run
`A = [10, 20, 30, 40, 50, 60, 70]` (index 0–6), target = **60**

| Step | low | high | mid | A[mid] | সিদ্ধান্ত |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 40 | 40 < 60 → ডানে যাও, `low = 4` |
| 2 | 4 | 6 | 5 | 60 | **60 = 60 ✅ Found at index 5** |

**মাত্র 2 comparison** (Linear-এ লাগত 6) · Time **O(log n)**

### ⚠️ মনে রাখো
- `mid = (low+high)/2` না লিখে `low + (high−low)/2` লেখো → **overflow এড়ায়**
- Linked List-এ কাজ করে না (random access নেই)

---
---

# B. SORTING

## B1. Bubble Sort

### Steps
1. পাশাপাশি দুটো element তুলনা করো: `A[j]` ও `A[j+1]`।
2. `A[j] > A[j+1]` হলে **swap** করো।
3. `j` কে array-র শেষ পর্যন্ত চালাও → এক **pass** শেষ।
4. প্রতি pass শেষে **সবচেয়ে বড় element শেষে** চলে যায় (বুদবুদের মতো ভেসে ওঠে)।
5. মোট `n−1` pass চালাও।
6. **Optimization:** কোনো pass-এ একটাও swap না হলে → array sorted, থেমে যাও।

### Dry Run
`A = [5, 1, 4, 2]`
```
Pass 1: [5,1,4,2] → swap 5,1 → [1,5,4,2]
                  → swap 5,4 → [1,4,5,2]
                  → swap 5,2 → [1,4,2,5]   ✅ 5 জায়গামতো

Pass 2: [1,4,2,5] → 1<4 ok
                  → swap 4,2 → [1,2,4,5]   ✅ 4 জায়গামতো

Pass 3: [1,2,4,5] → কোনো swap নেই → থেমে যাও

Result: [1, 2, 4, 5]
```
**Best O(n)** (flag থাকলে) · Avg/Worst **O(n²)** · Space O(1) · **Stable**

---

## B2. Selection Sort

### Steps
1. পুরো array-তে **সবচেয়ে ছোট** element খুঁজে বের করো।
2. সেটাকে **index 0**-এর element-এর সাথে swap করো।
3. এখন index 0 sorted। বাকি অংশে (index 1 থেকে) আবার সবচেয়ে ছোট খোঁজো।
4. সেটাকে index 1-এর সাথে swap করো।
5. `n−1` বার এভাবে চালাও।

### Dry Run
`A = [64, 25, 12, 22]`
```
Pass 1: min = 12 (index 2) → swap with index 0 → [12, 25, 64, 22]
Pass 2: min = 22 (index 3) → swap with index 1 → [12, 22, 64, 25]
Pass 3: min = 25 (index 3) → swap with index 2 → [12, 22, 25, 64]

Result: [12, 22, 25, 64]
```
**Best = Avg = Worst = O(n²)** ⭐ (already sorted হলেও কমে না) · Space O(1) · **Unstable**
✅ Swap সংখ্যা সবচেয়ে কম (n−1)

---

## B3. Insertion Sort

### Steps
1. প্রথম element-কে sorted ধরে নাও (index 0)।
2. index 1 থেকে শুরু করে প্রতিটি element-কে **key** ধরো।
3. Key-কে তার বাম পাশের sorted অংশের সাথে তুলনা করো।
4. যতক্ষণ বাম পাশের element **key-এর চেয়ে বড়**, ততক্ষণ সেগুলোকে **এক ধাপ ডানে সরাও**।
5. যেখানে থামলে, সেখানে key বসাও।
6. Array-র শেষ পর্যন্ত পুনরাবৃত্তি করো।

### Dry Run
`A = [12, 11, 13, 5]`
```
key=11 : 12>11 → সরাও → [11, 12, 13, 5]
key=13 : 12<13 → জায়গামতোই → [11, 12, 13, 5]
key=5  : 13>5 → সরাও
         12>5 → সরাও
         11>5 → সরাও → [5, 11, 12, 13]

Result: [5, 11, 12, 13]
```
**Best O(n)** (already sorted) · Avg/Worst **O(n²)** · Space O(1) · **Stable**
✅ ছোট বা প্রায়-sorted array-তে সেরা

---

## B4. Merge Sort ⭐ (Divide & Conquer)

### Steps
1. **Divide:** Array-কে মাঝখান থেকে **দুই ভাগে** ভাগ করো।
2. **Conquer:** প্রতিটি অর্ধেককে **recursively** merge sort করো।
3. যতক্ষণ না প্রতিটি অংশে **একটিমাত্র element** থাকে (একটা element সবসময় sorted)।
4. **Combine (Merge):** দুটি sorted অংশ জোড়া লাগাও —
   - দুই অংশের **প্রথম element** তুলনা করো
   - **ছোটটা** নতুন array-তে নাও, সেই অংশে এক ধাপ এগোও
   - একটা অংশ শেষ হলে অন্যটার বাকি সব copy করো
5. উপরে উঠতে উঠতে পুরো array sorted হয়ে যাবে।

### Dry Run
`A = [38, 27, 43, 3]`
```
DIVIDE:
[38, 27, 43, 3]
   ↓
[38, 27]   [43, 3]
   ↓          ↓
[38] [27]  [43] [3]

MERGE (উপরে ওঠা):
[38] + [27]  → 27<38 → [27, 38]
[43] + [3]   → 3<43  → [3, 43]

[27,38] + [3,43]:
  27 vs 3  → 3 নাও   → [3]
  27 vs 43 → 27 নাও  → [3, 27]
  38 vs 43 → 38 নাও  → [3, 27, 38]
  বাকি 43 copy       → [3, 27, 38, 43]

Result: [3, 27, 38, 43]
```
**Best = Avg = Worst = O(n log n)** ⭐ · Space **O(n)** ❌ · **Stable** · Linked List-এর জন্য সেরা

---

## B5. Quick Sort ⭐⭐⭐ (Divide & Conquer)

### Steps
1. একটি **pivot** নির্বাচন করো (সাধারণত শেষ element, বা first/middle/random)।
2. **Partition করো:**
   - `i` = ছোট element-দের সীমানা (শুরুতে `low − 1`)
   - `j` কে `low` থেকে `high−1` পর্যন্ত চালাও
   - `A[j] < pivot` হলে → `i++` এবং `A[i]` ↔ `A[j]` swap
3. শেষে `A[i+1]` ↔ `pivot` swap করো → **pivot তার চূড়ান্ত জায়গায় বসে গেল**।
4. এখন pivot-এর **বামে সব ছোট**, **ডানে সব বড়**।
5. বাম অংশ ও ডান অংশে **recursively** একই কাজ করো।
6. অংশে ১ বা ০ element থাকলে থামো।

### Dry Run
`A = [10, 80, 30, 90, 40]`, pivot = **40** (শেষ element)
```
i = -1, pivot = 40

j=0: 10 < 40 → i=0 → swap A[0],A[0] → [10, 80, 30, 90, 40]
j=1: 80 > 40 → কিছু না
j=2: 30 < 40 → i=1 → swap A[1],A[2] → [10, 30, 80, 90, 40]
j=3: 90 > 40 → কিছু না

শেষে: swap A[i+1]=A[2] ↔ pivot A[4]
     → [10, 30, 40, 90, 80]
                ↑ pivot চূড়ান্ত জায়গায় (index 2)

বাম [10, 30] → recursively sort
ডান [90, 80] → recursively sort → [80, 90]

Result: [10, 30, 40, 80, 90]
```
**Best/Avg O(n log n)** · **Worst O(n²)** ⚠️ (already sorted + first pivot) · Space O(log n) · **Unstable**
✅ বাস্তবে সবচেয়ে দ্রুত

---

## B6. Heap Sort

### Steps
1. পুরো array থেকে একটি **Max-Heap** বানাও (Build Heap → **O(n)**)।
2. **Root (index 0) = সবচেয়ে বড়** element।
3. Root-কে **শেষ element**-এর সাথে swap করো → সবচেয়ে বড়টা সঠিক জায়গায়।
4. Heap-এর size **এক কমাও** (শেষেরটা এখন sorted অংশে)।
5. নতুন root-এ **Heapify (sift-down)** চালাও যাতে আবার Max-Heap হয়।
6. Heap-এ ১টা element বাকি থাকা পর্যন্ত ধাপ 3–5 পুনরাবৃত্তি করো।

### Dry Run
`A = [4, 10, 3, 5]`
```
Build Max-Heap → [10, 5, 3, 4]

Step 1: swap 10 ↔ 4 → [4, 5, 3 | 10]  heapify → [5, 4, 3 | 10]
Step 2: swap 5 ↔ 3  → [3, 4 | 5, 10]  heapify → [4, 3 | 5, 10]
Step 3: swap 4 ↔ 3  → [3 | 4, 5, 10]

Result: [3, 4, 5, 10]
```
**Best = Avg = Worst = O(n log n)** · Space **O(1)** ⭐ · **Unstable**

---

## B7. Counting Sort (Non-comparison)

### Steps
1. Array-র **সর্বোচ্চ মান (k)** বের করো।
2. আকার `k+1`-এর একটি **count array** বানাও, সব 0 দিয়ে ভরো।
3. প্রতিটি element-এর জন্য `count[value]++` করো (গুনে রাখো)।
4. Count array-তে **cumulative sum** করো (`count[i] += count[i-1]`)।
5. Original array **শেষ থেকে শুরুর দিকে** ঘোরো, প্রতিটি element-কে `count[value]−1` position-এ বসাও, তারপর `count[value]--`।

### Dry Run
`A = [4, 2, 2, 1]`, k = 4
```
count = [0, 1, 2, 0, 1]    (index 0..4)
cumulative = [0, 1, 3, 3, 4]

শেষ থেকে:
1 → position count[1]-1 = 0 → output[0]=1
2 → position count[2]-1 = 2 → output[2]=2
2 → position 1           → output[1]=2
4 → position count[4]-1 = 3 → output[3]=4

Result: [1, 2, 2, 4]
```
**O(n + k)** · **Stable** · শুধু integer/সীমিত range

---
---

# C. STACK & QUEUE

## C1. Stack Push / Pop

### Push(x) Steps
1. Stack **full** কিনা দেখো → হলে **Overflow**, থামো।
2. `top = top + 1`
3. `stack[top] = x`

### Pop() Steps
1. Stack **empty** (`top == −1`) কিনা দেখো → হলে **Underflow**, থামো।
2. `value = stack[top]`
3. `top = top − 1`
4. `value` return করো

### Dry Run
```
top=-1 (empty)
Push 10 → top=0 → [10]
Push 20 → top=1 → [10, 20]
Push 30 → top=2 → [10, 20, 30]
Pop()   → 30 return, top=1 → [10, 20]
Pop()   → 20 return, top=0 → [10]
```
সব operation **O(1)**

---

## C2. Queue Enqueue / Dequeue

### Enqueue(x) Steps
1. Queue full কিনা দেখো → **Overflow**
2. `rear = rear + 1`
3. `queue[rear] = x`

### Dequeue() Steps
1. Queue empty (`front > rear`) কিনা দেখো → **Underflow**
2. `value = queue[front]`
3. `front = front + 1`
4. return `value`

### Circular Queue-তে পার্থক্য ⭐
`rear = (rear + 1) % SIZE` এবং `front = (front + 1) % SIZE`

### Dry Run
```
front=0, rear=-1
Enqueue 10 → rear=0 → [10]
Enqueue 20 → rear=1 → [10, 20]
Dequeue()  → 10 return, front=1 → [_, 20]
Enqueue 30 → rear=2 → [_, 20, 30]
```

---

## C3. Infix → Postfix (Stack ব্যবহার করে) ⭐

### Steps
1. Left থেকে right-এ expression স্ক্যান করো।
2. **Operand** (A, B, 5) পেলে → সরাসরি **output**-এ লিখো।
3. **`(`** পেলে → **Stack-এ push** করো।
4. **`)`** পেলে → `(` না পাওয়া পর্যন্ত **pop করে output-এ লিখো**; `(` টা pop করে ফেলে দাও।
5. **Operator** পেলে →
   - Stack-এর top-এ **সমান বা বেশি precedence**-এর operator থাকলে সেগুলো pop করে output-এ দাও
   - তারপর নিজের operator push করো
6. শেষে Stack-এর **সব pop করে output**-এ দাও।

**Precedence:** `^` (3) > `*` `/` (2) > `+` `−` (1)

### Dry Run
Infix: **`A + B * C`**

| Symbol | Action | Stack | Output |
|---|---|---|---|
| A | Operand → output | | A |
| + | Stack খালি → push | + | A |
| B | Operand → output | + | AB |
| * | `*` > `+` → push | + * | AB |
| C | Operand → output | + * | ABC |
| শেষ | সব pop | | **ABC\*+** |

**Result: `ABC*+`**

আরেকটা: `(A + B) * C` → **`AB+C*`**

---

## C4. Bracket / Parentheses Matching

### Steps
1. Expression স্ক্যান করো।
2. **Opening bracket** `(` `[` `{` পেলে → **Push**।
3. **Closing bracket** পেলে →
   - Stack empty হলে → **Not Balanced** ❌
   - Pop করো; pop করা bracket-এর সাথে **type মিলছে কিনা** দেখো, না মিললে → Not Balanced
4. শেষে **Stack empty হলে → Balanced ✅**, নাহলে ❌

### Dry Run
`( ( A + B ) * C )`
```
(  → push        → Stack: ( (
(  → push
A, +, B → skip
)  → pop (        → Stack: (
*, C → skip
)  → pop (        → Stack: empty
শেষে Stack empty → ✅ Balanced
```
`((A+B)` → শেষে Stack-এ একটা `(` বাকি → **❌ Not Balanced**

---
---

# D. LINKED LIST

## D1. Insert at Beginning — **O(1)**

### Steps
1. নতুন node তৈরি করো, তাতে data রাখো।
2. `newNode->next = head`
3. `head = newNode`

```
আগে:  head → [20] → [30] → NULL
10 insert:
      [10] → [20] → [30] → NULL
       ↑head
```

## D2. Insert at End — **O(n)**

### Steps
1. নতুন node তৈরি করো, `newNode->next = NULL`
2. List খালি হলে → `head = newNode`, শেষ
3. একটি temp pointer দিয়ে **শেষ node পর্যন্ত হাঁটো** (`temp->next == NULL` যতক্ষণ না হয়)
4. `temp->next = newNode`

## D3. Insert at Position k

### Steps
1. নতুন node তৈরি করো।
2. `k−1` তম node পর্যন্ত হাঁটো (temp)।
3. `newNode->next = temp->next`  ⚠️ **এটা আগে**
4. `temp->next = newNode`

⚠️ ধাপ 3 ও 4-এর **ক্রম উল্টালে list ছিঁড়ে যাবে** — এটাই সবচেয়ে বড় ভুল।

## D4. Delete a Node

### Steps
1. Delete করার node-এর **আগের node** (`prev`) খুঁজে বের করো।
2. `temp = prev->next` (যেটা delete হবে)
3. `prev->next = temp->next` (bypass করে দাও)
4. `free(temp)` — memory মুক্ত করো

```
আগে:  [10] → [20] → [30] → NULL
20 delete:
      [10] ────────→ [30] → NULL
```

## D5. Reverse a Linked List ⭐ (Interview favourite)

### Steps
1. তিনটা pointer নাও: `prev = NULL`, `curr = head`, `next = NULL`
2. `curr != NULL` যতক্ষণ, লুপ চালাও:
   - `next = curr->next` (পরেরটা মনে রাখো)
   - `curr->next = prev` (তীর উল্টে দাও)
   - `prev = curr` (এক ধাপ এগোও)
   - `curr = next`
3. শেষে `head = prev`

### Dry Run
`10 → 20 → 30 → NULL`
```
Step 1: prev=NULL, curr=10 → 10→NULL,  prev=10, curr=20
Step 2: prev=10,   curr=20 → 20→10,    prev=20, curr=30
Step 3: prev=20,   curr=30 → 30→20,    prev=30, curr=NULL

head = 30 → 30 → 20 → 10 → NULL  ✅
```
**O(n)** time, **O(1)** space

---
---

# E. TREE

## E1. Preorder / Inorder / Postorder

### Preorder Steps (Root-Left-Right)
1. Root **print** করো
2. Left subtree-তে recursively Preorder
3. Right subtree-তে recursively Preorder

### Inorder Steps (Left-Root-Right)
1. Left subtree-তে recursively Inorder
2. Root **print** করো
3. Right subtree-তে recursively Inorder

### Postorder Steps (Left-Right-Root)
1. Left subtree-তে recursively Postorder
2. Right subtree-তে recursively Postorder
3. Root **print** করো

### Dry Run (একই tree, তিন ফল)
```
        1
       / \
      2   3
     / \
    4   5
```
| Traversal | হাঁটার পথ | ফল |
|---|---|---|
| **Preorder** | 1 → বামে(2 → বামে 4, ডানে 5) → ডানে 3 | **1 2 4 5 3** |
| **Inorder** | বামে(4 → 2 → 5) → 1 → ডানে 3 | **4 2 5 1 3** |
| **Postorder** | বামে(4, 5 → 2) → ডানে 3 → 1 | **4 5 2 3 1** |

---

## E2. Level Order Traversal (Queue ব্যবহার করে)

### Steps
1. Root-কে **Queue-তে enqueue** করো।
2. Queue খালি না হওয়া পর্যন্ত লুপ:
   - একটা node **dequeue** করো, **print** করো
   - তার **left child** থাকলে enqueue
   - তার **right child** থাকলে enqueue

### Dry Run
```
Queue: [1]
Dequeue 1 → print 1 → enqueue 2, 3  → Queue: [2, 3]
Dequeue 2 → print 2 → enqueue 4, 5  → Queue: [3, 4, 5]
Dequeue 3 → print 3 → child নেই     → Queue: [4, 5]
Dequeue 4 → print 4                 → Queue: [5]
Dequeue 5 → print 5                 → Queue: []

Result: 1 2 3 4 5
```

---

## E3. BST Search

### Steps
1. Root থেকে শুরু করো।
2. `key == node` → **পেয়ে গেছি ✅**
3. `key < node` → **বাম** subtree-তে যাও
4. `key > node` → **ডান** subtree-তে যাও
5. NULL-এ পৌঁছালে → **Not Found ❌**

### Dry Run — Search **40**
```
        50
       /  \
     30    70
    / \    / \
   20 40  60 80

50: 40 < 50 → বামে যাও
30: 40 > 30 → ডানে যাও
40: 40 = 40 ✅ Found (3 comparison)
```

---

## E4. BST Insert

### Steps
1. Root থেকে শুরু করো।
2. `key < node` → বামে যাও; `key > node` → ডানে যাও।
3. **NULL** পাওয়া পর্যন্ত নামতে থাকো।
4. সেই NULL জায়গায় নতুন node বসাও।
5. নতুন node সবসময় **leaf** হিসেবে যোগ হয় ⭐

### Dry Run — Insert **35**
```
50: 35 < 50 → বামে
30: 35 > 30 → ডানে
40: 35 < 40 → বামে → NULL ✅ এখানে বসাও

        50
       /  \
     30    70
    / \
   20  40
      /
    35   ← নতুন
```

---

## E5. BST Delete — ৩টি Case ⭐

### Steps
1. প্রথমে node-টা **খুঁজে বের করো** (search-এর মতো)।
2. তিনটি case দেখো:

**Case 1 — Leaf node (child নেই):**
- সরাসরি delete করো, parent-এর pointer NULL করো

**Case 2 — একটি child:**
- Node-কে সরাও, তার **child-কে parent-এর সাথে জুড়ে দাও**

**Case 3 — দুইটি child:** ⭐
- **Inorder successor** খুঁজো = **ডান subtree-র সবচেয়ে বাম (সবচেয়ে ছোট)** node
- সেই মান দিয়ে delete করার node-এর মান **replace** করো
- এখন ডান subtree থেকে সেই successor-টা delete করো (recursively)

### Dry Run — Delete **30** (দুই child আছে)
```
        50                      50
       /  \                    /  \
     30    70      →         40    70
    / \    / \              / \    / \
   20 40  60 80           20  ?   60 80

30-এর ডান subtree = {40}, তার সবচেয়ে ছোট = 40
→ 30-কে 40 দিয়ে replace
→ ডান subtree থেকে 40 delete (leaf, সহজ)

        50
       /  \
     40    70
    /      / \
   20     60 80
```

---
---

# F. HEAP

## F1. Heap Insert (Sift-Up / Bubble-Up)

### Steps
1. নতুন element-কে **array-র শেষে** যোগ করো (শেষ leaf position)।
2. তার **parent** বের করো: `(i − 1) / 2`
3. Max-Heap-এ `child > parent` হলে → **swap** করো।
4. উপরের দিকে যেতে থাকো যতক্ষণ না —
   - parent বড় হয়ে যায়, **অথবা**
   - root-এ পৌঁছে যাও।

### Dry Run — Max-Heap `[50, 30, 40]`-এ **60** insert
```
Array: [50, 30, 40, 60]     index 3-এ যোগ

index 3 (60) → parent = (3-1)/2 = 1 → A[1]=30
60 > 30 → swap → [50, 60, 40, 30]

index 1 (60) → parent = (1-1)/2 = 0 → A[0]=50
60 > 50 → swap → [60, 50, 40, 30]

index 0 = root → থামো ✅
```
**O(log n)**

---

## F2. Heap Delete Max (Sift-Down / Heapify)

### Steps
1. **Root (index 0)** = সবচেয়ে বড়, এটাই return করবে।
2. **শেষ element**-কে root-এ বসিয়ে দাও।
3. Array size **এক কমাও**।
4. Root থেকে **নিচে নামো (Heapify)**:
   - দুই child-এর মধ্যে **বড়টা** বের করো (`2i+1`, `2i+2`)
   - সেই child parent-এর চেয়ে বড় হলে → **swap**
   - সেই child-এর position থেকে আবার একই কাজ করো
5. Heap property ঠিক হয়ে গেলে থামো।

### Dry Run — `[60, 50, 40, 30]` থেকে max delete
```
Return 60।  শেষের 30 কে root-এ → [30, 50, 40]

index 0 (30): children = index1(50), index2(40) → বড় = 50
30 < 50 → swap → [50, 30, 40]

index 1 (30): child নেই → থামো ✅
Result: [50, 30, 40]
```
**O(log n)**

---

## F3. Build Heap (array থেকে) — **O(n)** ⭐

### Steps
1. **শেষ non-leaf node** থেকে শুরু করো: index `n/2 − 1`
2. সেখান থেকে **index 0 পর্যন্ত পিছন দিকে** যাও।
3. প্রতিটি index-এ **Heapify (sift-down)** চালাও।

⚠️ Leaf node-গুলোতে heapify লাগে না — তাই শুরু হয় `n/2 − 1` থেকে।

### Dry Run — `[4, 10, 3, 5, 1]`, n=5
```
শুরু index = 5/2 - 1 = 1

index 1 (10): children 5, 1 → 10 সবচেয়ে বড় → ঠিক আছে
index 0 (4):  children 10, 3 → 10 বড় → swap → [10, 4, 3, 5, 1]
              index 1 (4): children 5, 1 → 5 বড় → swap → [10, 5, 3, 4, 1]

Max-Heap: [10, 5, 3, 4, 1] ✅
```

---
---

# G. HASHING

## G1. Hash Insert & Search (Chaining)

### Insert Steps
1. `index = h(key) = key % m` হিসাব করো।
2. সেই index-এর **Linked List**-এ node যোগ করো (সাধারণত beginning-এ, O(1))।

### Search Steps
1. `index = key % m` বের করো।
2. সেই index-এর list-এ **linear search** করো।

### Dry Run — m = 10, keys: 25, 35, 47
```
h(25) = 25 % 10 = 5
h(35) = 35 % 10 = 5   ← Collision!
h(47) = 47 % 10 = 7

Table:
index 5 → [35] → [25] → NULL
index 7 → [47] → NULL

Search 25: index 5 → list-এ হাঁটো → 35 ≠ 25 → 25 ✅
```

---

## G2. Linear Probing (Open Addressing)

### Insert Steps
1. `index = h(key) = key % m`
2. `table[index]` **খালি** হলে → সেখানে বসাও, শেষ।
3. খালি না হলে → `index = (index + 1) % m` (পরের ঘরে যাও)।
4. খালি ঘর পাওয়া পর্যন্ত ধাপ 3 পুনরাবৃত্তি করো।
5. পুরো table ঘুরে ফেললেও খালি না পেলে → **Table Full**।

### Dry Run — m = 7, keys: 10, 17, 24
```
h(10) = 10 % 7 = 3  → খালি → table[3] = 10
h(17) = 17 % 7 = 3  → দখল! → try 4 → খালি → table[4] = 17
h(24) = 24 % 7 = 3  → দখল! → try 4 → দখল! → try 5 → খালি → table[5] = 24

Table: [_, _, _, 10, 17, 24, _]
```
⚠️ এভাবে পাশাপাশি জমে যাওয়াকে বলে **Primary Clustering**।

**Search-এ একই probe sequence অনুসরণ করতে হয়।**

---
---

# H. GRAPH ALGORITHMS ⭐⭐⭐

**সব উদাহরণে এই graph ব্যবহার করব:**
```
      A
     / \
    B   C
   / \   \
  D   E   F
```
Adjacency: A→B,C · B→D,E · C→F

---

## H1. BFS (Breadth First Search) — **Queue**

### Steps
1. Start vertex-কে **visited** চিহ্নিত করো এবং **Queue-তে enqueue** করো।
2. Queue খালি না হওয়া পর্যন্ত লুপ:
   - একটা vertex **dequeue** করো, **print** করো
   - তার **সব unvisited প্রতিবেশী**-কে visited চিহ্নিত করে **enqueue** করো
3. Queue খালি হলে শেষ।

### Dry Run (start = A)
| Step | Dequeue | Print | Enqueue | Queue |
|---|---|---|---|---|
| 0 | — | — | A | [A] |
| 1 | A | A | B, C | [B, C] |
| 2 | B | B | D, E | [C, D, E] |
| 3 | C | C | F | [D, E, F] |
| 4 | D | D | — | [E, F] |
| 5 | E | E | — | [F] |
| 6 | F | F | — | [] |

**BFS Order: A B C D E F** (স্তরে স্তরে)
**O(V + E)** · unweighted graph-এ **shortest path দেয়** ⭐

---

## H2. DFS (Depth First Search) — **Stack / Recursion**

### Steps (Recursive)
1. Vertex-কে **visited** চিহ্নিত করো, **print** করো।
2. তার প্রতিটি **unvisited প্রতিবেশী**-র জন্য → **recursively DFS** ডাকো।
3. আর unvisited প্রতিবেশী না থাকলে → **backtrack** (পিছিয়ে যাও)।

### Steps (Stack দিয়ে)
1. Start vertex **push** করো।
2. Stack খালি না হওয়া পর্যন্ত:
   - **Pop** করো; visited না হলে visited চিহ্নিত করে print করো
   - তার সব unvisited প্রতিবেশী **push** করো

### Dry Run (start = A, recursive)
```
A visit → print A
  → B visit → print B
      → D visit → print D → child নেই → backtrack
      → E visit → print E → child নেই → backtrack
  → backtrack to A
  → C visit → print C
      → F visit → print F → backtrack

DFS Order: A B D E C F  (যতদূর গভীরে যাওয়া যায়)
```
**O(V + E)** · **shortest path দেয় না** ❌

---

## H3. Dijkstra's Algorithm (Shortest Path) ⭐

### Steps
1. সব vertex-এর distance = **∞**, source-এর distance = **0**।
2. সব vertex **unvisited** রাখো।
3. Unvisited-দের মধ্যে **সবচেয়ে কম distance**-এর vertex `u` নাও।
4. `u` কে **visited** চিহ্নিত করো।
5. `u`-এর প্রতিটি প্রতিবেশী `v`-এর জন্য **Relaxation** করো:
   - `if dist[u] + weight(u,v) < dist[v] → dist[v] = dist[u] + weight(u,v)`
6. সব vertex visited না হওয়া পর্যন্ত ধাপ 3–5 পুনরাবৃত্তি করো।

### Dry Run
```
Graph:  A --4-- B
        |       |
        2       3
        |       |
        C --1-- D          (Source = A)
```
| Step | নেওয়া vertex | A | B | C | D |
|---|---|---|---|---|---|
| শুরু | — | **0** | ∞ | ∞ | ∞ |
| 1 | **A** (0) | 0 | 4 | 2 | ∞ |
| 2 | **C** (2) | 0 | 4 | **2** | 2+1=3 |
| 3 | **D** (3) | 0 | min(4, 3+3)=4 | 2 | **3** |
| 4 | **B** (4) | 0 | **4** | 2 | 3 |

**Shortest: A→B = 4, A→C = 2, A→D = 3**

⚠️ **Negative weight-এ কাজ করে না** · **Greedy** · O((V+E) log V)

---

## H4. Bellman-Ford

### Steps
1. সব distance = **∞**, source = **0**।
2. **`V − 1` বার** পুরো edge list-এর উপর লুপ চালাও:
   - প্রতিটি edge (u,v,w)-এর জন্য relaxation: `if dist[u]+w < dist[v] → dist[v] = dist[u]+w`
3. **V-তম বার** আরেকবার চালাও:
   - যদি এখনও কোনো distance কমে → **Negative Cycle আছে** ⚠️

### Key
- **O(V·E)** · Dijkstra-র চেয়ে ধীর
- ✅ **Negative weight handle করে**, negative cycle **detect করে**
- **Dynamic Programming** based

---

## H5. Floyd-Warshall (All-Pairs Shortest Path)

### Steps
1. একটি `V × V` distance matrix বানাও:
   - `dist[i][j] = edge weight` (edge থাকলে)
   - `dist[i][i] = 0`
   - `dist[i][j] = ∞` (edge না থাকলে)
2. প্রতিটি **intermediate vertex `k`**-এর জন্য (0 থেকে V−1):
   - প্রতিটি `i`-এর জন্য, প্রতিটি `j`-এর জন্য:
   - `if dist[i][k] + dist[k][j] < dist[i][j] → dist[i][j] = dist[i][k] + dist[k][j]`
3. তিনটি nested loop শেষ হলে matrix-এ সব জোড়ার shortest path।

**মূল ধারণা:** "i থেকে j যেতে k হয়ে গেলে কি কম লাগে?"

**O(V³)** · Space O(V²) · **DP** · negative weight ✅

⚠️ **Loop-এর ক্রম গুরুত্বপূর্ণ: k বাইরে, তারপর i, তারপর j।**

---

## H6. Prim's Algorithm (MST)

### Steps
1. যেকোনো **একটি vertex** দিয়ে শুরু করো, MST-তে যোগ করো।
2. MST-তে থাকা vertex থেকে বাইরের vertex-এ যাওয়া **সব edge** দেখো।
3. তার মধ্যে **সবচেয়ে কম weight**-এর edge নাও (যেটা **cycle বানায় না**)।
4. সেই edge ও নতুন vertex MST-তে যোগ করো।
5. **সব vertex** MST-তে না আসা পর্যন্ত ধাপ 2–4 পুনরাবৃত্তি করো।
6. শেষে edge সংখ্যা = **V − 1**।

### Dry Run
```
A--1--B
|     |
4     2
|     |
C--3--D          (start = A)

Step 1: MST = {A}
Step 2: A-B(1), A-C(4) → সবচেয়ে কম A-B(1) → MST = {A,B}
Step 3: A-C(4), B-D(2) → সবচেয়ে কম B-D(2) → MST = {A,B,D}
Step 4: A-C(4), D-C(3) → সবচেয়ে কম D-C(3) → MST = {A,B,D,C}

MST edges: A-B(1), B-D(2), D-C(3)   Total = 6
Edge সংখ্যা = 3 = V−1 ✅
```
**Vertex ধরে বাড়ে** · Min-Heap ব্যবহার করে · **O(E log V)** · Dense graph-এ ভালো

---

## H7. Kruskal's Algorithm (MST)

### Steps
1. **সব edge** weight অনুযায়ী **ছোট থেকে বড় sort** করো।
2. খালি MST দিয়ে শুরু করো।
3. Sorted list থেকে একটা করে edge নাও:
   - এই edge যোগ করলে **cycle তৈরি হয় কিনা** দেখো (**Union-Find** দিয়ে)
   - Cycle না হলে → **MST-তে যোগ করো**
   - Cycle হলে → **বাদ দাও**
4. MST-তে **V − 1** টা edge হয়ে গেলে থামো।

### Dry Run (একই graph)
```
Edges sorted: A-B(1), B-D(2), C-D(3), A-C(4)

A-B(1): cycle নেই → নাও ✅   MST = {A-B}
B-D(2): cycle নেই → নাও ✅   MST = {A-B, B-D}
C-D(3): cycle নেই → নাও ✅   MST = {A-B, B-D, C-D}
→ 3 edge = V−1, থামো

Total = 6 (Prim-এর সমান ✅)
```
**Edge ধরে বাড়ে** · **Union-Find** ব্যবহার করে · **O(E log E)** · Sparse graph-এ ভালো

---

## H8. Topological Sort (Kahn's Algorithm — BFS based)

### Steps
1. প্রতিটি vertex-এর **in-degree** (ভিতরে আসা edge সংখ্যা) হিসাব করো।
2. যাদের **in-degree = 0**, তাদের **Queue-তে enqueue** করো।
3. Queue খালি না হওয়া পর্যন্ত:
   - একটা vertex **dequeue** করে **output**-এ দাও
   - তার প্রতিটি প্রতিবেশীর **in-degree 1 কমাও**
   - কারো in-degree **0 হয়ে গেলে** → enqueue করো
4. Output-এ **সব vertex** এলে ✅ ; না এলে → **Cycle আছে** ❌ (topological sort সম্ভব নয়)

### Dry Run
```
CSE111 → CSE220 → CSE221
             ↘ CSE320

In-degree: CSE111=0, CSE220=1, CSE221=1, CSE320=1

Queue: [CSE111]
Dequeue CSE111 → output: CSE111 → CSE220-এর in-degree 0 → enqueue
Dequeue CSE220 → output: CSE220 → CSE221, CSE320 in-degree 0 → enqueue
Dequeue CSE221 → output: CSE221
Dequeue CSE320 → output: CSE320

Order: CSE111 → CSE220 → CSE221 → CSE320 ✅
```
⭐ শুধু **DAG**-এ সম্ভব · **O(V + E)**

---
---

# I. DP & GREEDY

## I1. Fibonacci (DP — Tabulation)

### Steps
1. আকার `n+1`-এর একটা array `dp` বানাও।
2. `dp[0] = 0`, `dp[1] = 1` (base case)
3. `i = 2` থেকে `n` পর্যন্ত: `dp[i] = dp[i-1] + dp[i-2]`
4. `dp[n]` return করো।

### Dry Run — n = 6
```
dp[0]=0, dp[1]=1
dp[2]=0+1=1
dp[3]=1+1=2
dp[4]=1+2=3
dp[5]=2+3=5
dp[6]=3+5=8  ✅
```
Naive recursion **O(2ⁿ)** → DP **O(n)** ⭐

---

## I2. 0/1 Knapsack (DP) ⭐

### Steps
1. `(n+1) × (W+1)` আকারের table `dp` বানাও, প্রথম row ও column = 0।
2. প্রতিটি item `i` (1..n) ও প্রতিটি capacity `w` (1..W)-এর জন্য:
   - **যদি `weight[i] > w`** (item ধরে না) → `dp[i][w] = dp[i-1][w]` (নিও না)
   - **নাহলে** দুটোর **বড়টা** নাও:
     - **না নিলে:** `dp[i-1][w]`
     - **নিলে:** `value[i] + dp[i-1][w - weight[i]]`
3. উত্তর = `dp[n][W]`

### Dry Run
Items: (wt=1, val=1), (wt=3, val=4), (wt=4, val=5) · **W = 4**

| i\w | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 (1,1) | 0 | 1 | 1 | 1 | 1 |
| 2 (3,4) | 0 | 1 | 1 | 4 | **5** |
| 3 (4,5) | 0 | 1 | 1 | 4 | **5** |

**উত্তর = 5** (item 1 + item 2 নিয়ে: weight 1+3=4, value 1+4=5)

**O(n·W)** · ⚠️ **0/1 Knapsack = DP, Greedy দিয়ে হয় না**

---

## I3. Longest Common Subsequence (LCS)

### Steps
1. `(m+1) × (n+1)` table বানাও, প্রথম row ও column = 0।
2. প্রতিটি `i`, `j`-এর জন্য:
   - **অক্ষর মিললে** (`X[i] == Y[j]`) → `dp[i][j] = dp[i-1][j-1] + 1` (তির্যক + 1)
   - **না মিললে** → `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (উপর ও বামের বড়টা)
3. উত্তর = `dp[m][n]`

### Dry Run — X = "AB", Y = "BA"
| | "" | B | A |
|---|---|---|---|
| **""** | 0 | 0 | 0 |
| **A** | 0 | 0 | **1** |
| **B** | 0 | **1** | **1** |

**LCS length = 1** ("A" বা "B") · **O(m·n)**

---

## I4. Fractional Knapsack (Greedy)

### Steps
1. প্রতিটি item-এর **value/weight ratio** হিসাব করো।
2. Ratio অনুযায়ী **বড় থেকে ছোট sort** করো।
3. উপর থেকে item নিতে থাকো যতক্ষণ পুরো item ধরে।
4. যে item পুরো ধরে না, তার **ভগ্নাংশ (fraction)** নাও ⭐
5. Capacity শেষ হলে থামো।

### Dry Run — W = 50
| Item | Value | Weight | Ratio |
|---|---|---|---|
| A | 60 | 10 | **6.0** |
| B | 100 | 20 | **5.0** |
| C | 120 | 30 | **4.0** |

```
A পুরো নাও (10)   → value 60,  বাকি capacity 40
B পুরো নাও (20)   → value 100, বাকি capacity 20
C-এর 20/30 নাও   → value 120 × (20/30) = 80

Total = 60 + 100 + 80 = 240 ✅
```
**O(n log n)** (sort-এর জন্য) · ⚠️ **ভগ্নাংশ নেওয়া যায় বলেই Greedy কাজ করে**

---

## I5. Activity Selection (Greedy)

### Steps
1. সব activity-কে **finish time** অনুযায়ী **ছোট থেকে বড় sort** করো। ⭐
2. প্রথম activity নাও।
3. পরের প্রতিটি activity-র জন্য:
   - তার **start time ≥ শেষ নেওয়া activity-র finish time** হলে → **নাও**
   - নাহলে → **বাদ দাও**

### Dry Run
| Activity | Start | Finish |
|---|---|---|
| A1 | 1 | 3 |
| A2 | 2 | 5 |
| A3 | 4 | 7 |
| A4 | 6 | 9 |

```
Finish অনুযায়ী sorted: A1(3), A2(5), A3(7), A4(9)

A1 নাও → শেষ finish = 3
A2: start 2 < 3 → বাদ
A3: start 4 ≥ 3 → নাও → শেষ finish = 7
A4: start 6 < 7 → বাদ

Selected: A1, A3  (মোট 2টি)
```
⚠️ **Finish time দিয়ে sort করা** — start time দিয়ে নয়। এটাই মূল trick।

---

## I6. Huffman Coding (Greedy)

### Steps
1. প্রতিটি character ও তার **frequency** নিয়ে একটি **Min-Heap** বানাও।
2. Heap-এ ১টার বেশি node থাকা পর্যন্ত:
   - **সবচেয়ে কম frequency-র দুটো** node বের করো
   - দুটোর frequency **যোগ করে** নতুন parent node বানাও
   - দুটোকে সেই parent-এর left ও right child করো
   - নতুন node **Heap-এ ফেরত দাও**
3. শেষে যে node বাকি থাকে = **Huffman Tree-র root**।
4. Root থেকে **left = 0, right = 1** ধরে প্রতিটি character-এর code পড়ো।

### Dry Run — A:5, B:2, C:1, D:1
```
Heap: [C:1, D:1, B:2, A:5]

Step 1: C(1) + D(1) = CD(2)  → Heap: [B:2, CD:2, A:5]
Step 2: B(2) + CD(2) = BCD(4) → Heap: [BCD:4, A:5]
Step 3: BCD(4) + A(5) = root(9)

Tree:        9
           /   \
        BCD:4   A:5
        /   \
      B:2   CD:2
            /  \
          C:1  D:1

Codes:  A = 1,  B = 00,  C = 010,  D = 011
```
⭐ **কম frequency → লম্বা code, বেশি frequency → ছোট code** · **O(n log n)**

---
---

# J. BACKTRACKING

## J1. N-Queens

### Steps
1. **প্রথম column (বা row)** থেকে শুরু করো।
2. এই column-এর প্রতিটি row-তে queen বসানোর চেষ্টা করো।
3. প্রতিবার **`isSafe()` চেক করো** — একই row, একই diagonal-এ অন্য queen আছে কিনা।
4. Safe হলে → queen বসাও, **পরের column**-এ recursively যাও।
5. পরের column-এ কোনো solution না পেলে → **queen সরিয়ে নাও (Backtrack)**, পরের row চেষ্টা করো।
6. সব column-এ queen বসে গেলে → **Solution পাওয়া গেছে ✅**
7. কোনো row-তেই safe না হলে → **false return করো** (আগের column backtrack করবে)।

### Dry Run — 4-Queens (সংক্ষেপে)
```
Col 0: Row 0-তে queen বসাও ✅
Col 1: Row 0 ❌ (একই row), Row 1 ❌ (diagonal), Row 2 ✅
Col 2: Row 0 ❌, Row 1 ❌, Row 2 ❌, Row 3 ❌ → সব fail
       → BACKTRACK: Col 1-এ ফিরে যাও, Row 3 চেষ্টা করো
Col 1: Row 3 ✅
Col 2: Row 1 ✅
Col 3: কোনো safe row নেই → BACKTRACK...
       → শেষ পর্যন্ত Col 0-এ Row 1 দিয়ে শুরু করলে solution মেলে

Solution: (1,0), (3,1), (0,2), (2,3)
```
**Exponential** complexity · এটাই **DFS on state-space tree**

---
---

# K. NUMBER ALGORITHMS

## K1. GCD — Euclidean Algorithm ⭐

### Steps
1. `b == 0` হলে → **`a` return করো** (এটাই GCD)।
2. নাহলে → `GCD(b, a mod b)` ডাকো।
3. পুনরাবৃত্তি করো যতক্ষণ না remainder 0 হয়।

**Rule:** `GCD(a, b) = GCD(b, a mod b)`, `GCD(a, 0) = a`

### Dry Run — GCD(48, 18)
```
GCD(48, 18) → 48 mod 18 = 12  → GCD(18, 12)
GCD(18, 12) → 18 mod 12 = 6   → GCD(12, 6)
GCD(12, 6)  → 12 mod 6  = 0   → GCD(6, 0)
GCD(6, 0)   → b=0 → return 6  ✅
```
**O(log(min(a,b)))** · **LCM = (a × b) / GCD(a, b)**

---

## K2. Sieve of Eratosthenes (সব prime বের করা)

### Steps
1. 2 থেকে n পর্যন্ত সব সংখ্যাকে **prime ধরে নাও** (সব `true`)।
2. `p = 2` থেকে শুরু করো।
3. `p` যদি এখনও prime থাকে → তার **সব গুণিতক** (`p²`, `p²+p`, `p²+2p`, …) কে **composite চিহ্নিত করো** (`false`)।
4. `p` বাড়াও, `p × p ≤ n` যতক্ষণ ধাপ 3 পুনরাবৃত্তি করো।
5. যেগুলো `true` রয়ে গেছে = **Prime**।

### Dry Run — n = 20
```
শুরু: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

p=2: 4,6,8,10,12,14,16,18,20 কাটো
p=3: 9,15 কাটো  (6,12,18 আগেই কাটা)
p=4: আগেই কাটা, skip
p=5: 5×5=25 > 20 → থামো

Primes: 2, 3, 5, 7, 11, 13, 17, 19 ✅
```
**O(n log log n)**

⚠️ ধাপ 3-এ `p²` থেকে শুরু করো (`2p` নয়) — কারণ ছোট গুণিতকগুলো আগেই কাটা পড়েছে।

---

## K3. Primality Test — O(√n)

### Steps
1. `n ≤ 1` হলে → **not prime**।
2. `n == 2` হলে → **prime**।
3. `n` জোড় হলে → **not prime**।
4. `i = 3` থেকে `√n` পর্যন্ত (2 করে বাড়াও):
   - `n % i == 0` হলে → **not prime**, থামো
5. কোনো ভাগফল না পেলে → **prime ✅**

### Dry Run — n = 29
```
√29 ≈ 5.38

i=3: 29 % 3 = 2 ≠ 0
i=5: 29 % 5 = 4 ≠ 0
i=7: 7 > 5.38 → থামো

29 is PRIME ✅
```
⭐ **শুধু √n পর্যন্ত দেখলেই হয়** — কারণ কোনো ভাজক √n-এর বেশি হলে তার জোড়া ভাজক √n-এর কম হবেই।

---
---

# ★ শেষ চেক — কোন Algorithm-এ কোন DS?

| Algorithm | ব্যবহৃত Data Structure |
|---|---|
| **BFS** | **Queue** |
| **DFS** | **Stack / Recursion** |
| **Level Order Traversal** | **Queue** |
| **Pre/In/Post order** | **Stack / Recursion** |
| **Dijkstra** | **Min-Heap (Priority Queue)** |
| **Prim's** | **Min-Heap (Priority Queue)** |
| **Kruskal's** | **Union-Find (Disjoint Set)** |
| **Huffman** | **Min-Heap** |
| **Heap Sort** | **Heap (Array)** |
| **Merge Sort** | **Extra Array O(n)** |
| **Quick Sort** | **Recursion Stack** |
| **Topological Sort (Kahn)** | **Queue** |
| **Infix → Postfix** | **Stack** |
| **Bracket Matching** | **Stack** |
| **Recursion** | **Call Stack** |
| **DP** | **Table (1D/2D Array)** |
| **Backtracking** | **Recursion Stack** |

## যেসব ধাপ ভুলে যাওয়া সবচেয়ে বেশি — একবার চোখ বুলাও

1. **Binary Search:** array **sorted** হতেই হবে
2. **Quick Sort:** partition-এর পর **pivot চূড়ান্ত জায়গায়** বসে
3. **Merge Sort:** কাজ হয় **merge (combine)** step-এ, quick-এ **partition (divide)** step-এ
4. **Build Heap:** শুরু index **`n/2 − 1`** থেকে, পিছন দিকে
5. **Heap Insert:** শেষে যোগ → **উপরে ওঠো**; **Delete:** শেষেরটা root-এ → **নিচে নামো**
6. **BST Delete (2 child):** **inorder successor** = ডান subtree-র সবচেয়ে বাম
7. **Linked List Insert:** `newNode->next = temp->next` **আগে**, তারপর `temp->next = newNode`
8. **Dijkstra:** প্রতি ধাপে **সবচেয়ে কম distance-এর unvisited** vertex নাও
9. **Floyd-Warshall:** loop ক্রম **k → i → j** (k বাইরে)
10. **Activity Selection:** **finish time** দিয়ে sort (start time নয়)
11. **Fractional Knapsack:** **value/weight ratio** দিয়ে sort
12. **Topological Sort:** **in-degree 0** দিয়ে শুরু, শুধু **DAG**-এ
13. **Sieve:** `p × p` থেকে কাটা শুরু করো
14. **GCD:** `GCD(b, a mod b)`, থামে যখন `b = 0`
