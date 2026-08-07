# CSE 220 — DATA STRUCTURES (COMPLETE)
### BRAC University MSc CSE Admission Test — Full Notes

> **এই ফাইলে শুধু Data Structure।** Algorithm আলাদা ফাইলে (CSE 221)।
>
> **পার্থক্য মাথায় গেঁথে নাও:**
> **Data Structure = data কীভাবে রাখা হবে (Storage)**
> **Algorithm = সেই data নিয়ে কী করা হবে (Process)**

---

## 📑 সূচিপত্র

| Module | Topics |
|---|---|
| **1. Introduction** | Data Structure · Data Objects · Classification · ADT · Primitive Operations · Performance |
| **2. Array** | Array · Operations · Types |
| **3. Linked List** | Linked List · Types · Operations |
| **4. Stack** | Stack · Applications |
| **5. Queue** | Queue · Types of Queue |
| **6. Tree** | Tree · Binary Tree · Traversal · BST · AVL · Heap |
| **7. Hashing** | Hash Table · Collision |
| **8. Graph** | Graph · Representation |
| **9. Others** | Priority Queue · Set · Dictionary · Compound |
| **10. Recursion** | Recursion (DS view) |
| **11. Memory** | Memory Management |
| **★ Final** | Master Tables · 15 MCQ Traps |

---
---

# MODULE 1 — INTRODUCTION TO DATA STRUCTURES

## Topic 1: Data Structure

### Definition (English)
A **Data Structure** is a specialized way of **organizing**, **storing**, and **managing** data in a computer so that it can be **accessed and modified efficiently**.

⭐ **Keywords:** Organizing · Storing · Efficient Access · Memory

### Concept (বাংলায়)
তিনটি শব্দ গুরুত্বপূর্ণ:
- **Organizing** → Data কীভাবে সাজানো হবে
- **Storing** → Memory-তে কীভাবে রাখা হবে
- **Processing** → Search, Insert, Delete, Update কত দ্রুত হবে

মূল লক্ষ্য = **Efficiency** (কম সময় + কম memory)।

**Real Example:** একটি flood monitoring system-এ ৫১৬০টি union-এর তথ্য আছে।
- পুরো list scan করলে → **O(n)**
- Union Code-কে key ধরে **Hash Table** ব্যবহার করলে → **O(1)** average

সমস্যা একই, কিন্তু Data Structure বদলালে performance সম্পূর্ণ বদলে যায়।

### Key Points
1. একটিই DS সব সমস্যার জন্য সেরা নয় — problem অনুযায়ী নির্বাচন করতে হয়।
2. ভালো DS-এর গুণ: fast search, fast insert/delete, কম memory, scalable।
3. Algorithm-এর performance অনেকটাই DS-এর উপর নির্ভরশীল।
4. DS দুই ভাগে: **Primitive** ও **Non-Primitive**।

### Data Structure vs Algorithm ⭐

| Data Structure | Algorithm |
|---|---|
| Data কীভাবে **রাখা** হবে | Data নিয়ে কীভাবে **কাজ** হবে |
| Storage / Organization | Process / Steps |
| উদাহরণ: Binary Search **Tree** | উদাহরণ: Binary **Search** |
| উদাহরণ: **Heap** | উদাহরণ: **Heap Sort** |
| Static concept | Dynamic concept |

### 🔁 Admission Revision Box
Data Structure = data organize + store + efficiently access করার পদ্ধতি। লক্ষ্য **efficiency (time + space)**। DS = storage, Algorithm = process। **Binary Search Tree = DS**, **Binary Search = Algorithm**। সঠিক DS নির্বাচন করলেই performance বদলে যায় (O(n) → O(1))।

---

## Topic 2: Data Objects

### Definition (English)
A **Data Object** is a collection of **related data elements** that are treated as a **single unit** by a program.

⭐ **Keywords:** Collection · Related · Single Unit

### Concept (বাংলায়)
**Data Item ≠ Data Object**
- **Data Item** = একটি একক (single) value
- **Data Object** = একাধিক related data item-এর সমষ্টি, যাকে একটি entity ধরা হয়

**Real Example — Student Record:**
```
Student
--------
ID        ← Data Item
Name      ← Data Item
CGPA      ← Data Item
```
কিন্তু পুরো **Student** = একটি **Data Object**।

Database থেকে একটি row retrieve করা মানে একটি Data Object retrieve করা।

### Types of Data Objects ⭐

| Type | Definition | Examples |
|---|---|---|
| **Elementary (Atomic)** | একটিমাত্র data item, ভাঙা যায় না | int, float, char, boolean |
| **Composite (Group)** | একাধিক related item একসাথে | Student Record, Employee, Bank Account |

### Key Points
1. প্রায় সব DS (Array, Linked List, Tree) আসলে **Data Object** store করে।
2. একটি Linked List-এর প্রতিটি node-এ শুধু int নয়, পুরো Student Object থাকতে পারে।
3. Elementary = ভাঙা যায় না; Composite = ভাঙা যায়।

### 🔁 Admission Revision Box
**Data Item = একটি value**, **Data Object = একাধিক related item একসাথে, single unit হিসেবে**। দুই ধরন: **Elementary** (int, char, float) ও **Composite** (Student Record, Employee Record)।

---

## Topic 3: Classification of Data Structures ⭐

### Definition (English)
Data structures are broadly classified into **Primitive** and **Non-Primitive**; non-primitive structures are further divided into **Linear** and **Non-Linear**.

### Classification Chart ⭐⭐ (মুখস্থ)

```
                Data Structure
                      │
        ┌─────────────┴─────────────┐
    Primitive                  Non-Primitive
   (int, float,                     │
   char, pointer)      ┌────────────┴────────────┐
                    Linear                  Non-Linear
                       │                         │
        ┌──────┬───────┼───────┐          ┌──────┴──────┐
      Array  Stack  Queue  Linked List   Tree         Graph
```

### Definitions

| Type | Definition |
|---|---|
| **Primitive** | সরাসরি machine-এ define করা basic data type |
| **Non-Primitive** | Primitive দিয়ে তৈরি জটিল structure |
| **Linear** | Element-গুলো **ধারাবাহিকভাবে (sequentially)** সাজানো |
| **Non-Linear** | Element-গুলো **hierarchical বা network** আকারে সাজানো |

### Linear vs Non-Linear ⭐⭐⭐

| Feature | **Linear** | **Non-Linear** |
|---|---|---|
| সাজানো | পরপর, একটির পর একটি | Hierarchical / Network |
| Traversal | এক pass-এ সব element | এক pass-এ সম্ভব নয় |
| Memory ব্যবহার | তুলনামূলক অদক্ষ | দক্ষ |
| Level | একটি level | একাধিক level |
| **উদাহরণ** | **Array, Stack, Queue, Linked List** | **Tree, Graph** |

### আরেকটি শ্রেণিবিভাগ

| Type | Definition | উদাহরণ |
|---|---|---|
| **Static** | Size compile time-এ নির্ধারিত | Array |
| **Dynamic** | Size run time-এ পরিবর্তনযোগ্য | Linked List, Tree, Graph |
| **Homogeneous** | সব element একই type | Array |
| **Heterogeneous** | ভিন্ন type-এর element | Structure, Class, Record |

### ⚠️ Common MCQ Traps
- **Stack ও Queue = Linear** ✅ (অনেকে non-linear ভাবে)
- **Tree ও Graph = Non-Linear** ✅
- **Array = Static & Homogeneous**, **Linked List = Dynamic**

### 🔁 Admission Revision Box
DS = **Primitive** (int, char, float, pointer) + **Non-Primitive**। Non-Primitive = **Linear** (Array, Stack, Queue, Linked List) + **Non-Linear** (Tree, Graph)। Linear = sequential, এক pass-এ traverse; Non-Linear = hierarchical। **Static = Array**, **Dynamic = Linked List/Tree**।

---

## Topic 4: Data Abstraction & Abstract Data Type (ADT) ⭐

### 4.1 Data Abstraction

**Definition (English):** **Data Abstraction** is the process of **hiding implementation details** while exposing only the **essential features and operations** of a data object.

⭐ **Keywords:** Hiding · What not How · Encapsulation

**Concept (বাংলায়):**
মূল উদ্দেশ্য — **"What" দেখানো, "How" লুকিয়ে রাখা।**
User জানবে কী operation করা যায়, কিন্তু ভিতরে কীভাবে হচ্ছে জানার দরকার নেই।

**Real Example 1 — Python Dictionary:**
`student["id"] = 101` লিখলেই কাজ হয়ে যায়। কিন্তু Python কীভাবে memory allocate করে, collision handle করে, resize করে — জানতে হয় না।

**Real Example 2 — SQL:**
`SELECT * FROM student;` লিখলেই data আসে। Database ভিতরে B+ Tree না Hash Index ব্যবহার করছে — তোমার জানার দরকার নেই।

**Advantages:** Complexity কমে · Security বাড়ে · Maintenance সহজ · Modular programming

### 4.2 Abstract Data Type (ADT) ⭐⭐⭐

**Definition (English):** An **Abstract Data Type (ADT)** is a **logical specification** of a data type that defines **what data** it holds and **what operations** can be performed on it, **without specifying how** those operations are implemented.

⭐ **Keywords:** Logical · Specification · Operations · No Implementation

**Concept (বাংলায়):**
ADT কোনো Data Structure **নয়** — এটি একটি **Specification**।
এটি বলে কী operation থাকবে, কিন্তু কীভাবে হবে বলে না।

**Stack ADT** define করে: `Push(x)`, `Pop()`, `Top()`, `isEmpty()`, `Size()`
কিন্তু বলে না Array দিয়ে হবে না Linked List দিয়ে — সেটা programmer-এর সিদ্ধান্ত।

**Real Example — Java:**
```java
List<Integer> list = new ArrayList<>();   // List = ADT, ArrayList = Implementation
List<Integer> list = new LinkedList<>();  // implementation বদলালো, বাকি code একই
```

**Real Example — Browser Back Button:**
নতুন page → push, Back → pop। এটাই **Stack ADT**। Developer Array বা Linked List — যেকোনোটা দিয়ে বানাতে পারে, user-এর কাছে একই।

### ADT vs Data Structure ⭐⭐⭐

| **Abstract Data Type (ADT)** | **Data Structure** |
|---|---|
| Logical concept | Physical implementation |
| Defines **what** (behavior) | Defines **how** (implementation) |
| Language independent | Language dependent |
| Stack **ADT** | Stack using **Array** |
| Queue **ADT** | Queue using **Linked List** |
| List, Map, Set | ArrayList, HashMap, HashSet |

### Key Points
1. একটি ADT-র **একাধিক implementation** থাকতে পারে। ⭐
2. Stack, Queue, List, Set, Map, Priority Queue — সবই **ADT**।
3. Array, Linked List, Hash Table, Heap — এগুলো **Data Structure/Implementation**।
4. সুবিধা: implementation বদলানো যায়, code reusable, maintenance সহজ, testing সহজ।

### ⚠️ Common MCQ Traps
- **"ADT কি Data Structure?" → না।** ADT = specification, DS = implementation।
- **Stack একটি ADT** ✅ কিন্তু **Array একটি Data Structure** ✅

### 🔁 Admission Revision Box
**Data Abstraction** = implementation লুকিয়ে শুধু operation দেখানো (What, not How)। **ADT** = logical specification — কী operation আছে বলে, কীভাবে হবে বলে না। **ADT ≠ Data Structure**। Stack/Queue/List/Map = ADT; Array/Linked List/Hash Table = Implementation। এক ADT-র একাধিক implementation সম্ভব।

---

## Topic 5: Primitive Operations on Data Structures

### Definition (English)
**Primitive Operations** are the basic operations that can be performed on any data structure: **Traversing, Searching, Insertion, Deletion, Updating, Sorting, and Merging**.

### The 7 Operations ⭐

| # | Operation | Definition | সাধারণ Complexity |
|---|---|---|---|
| 1 | **Traversing** | প্রতিটি element **ঠিক একবার** visit করা | O(n) |
| 2 | **Searching** | নির্দিষ্ট element-এর অবস্থান খোঁজা | O(n) / O(log n) / O(1) |
| 3 | **Insertion** | নতুন element যোগ করা | DS-ভেদে O(1)–O(n) |
| 4 | **Deletion** | বিদ্যমান element মুছে ফেলা | DS-ভেদে O(1)–O(n) |
| 5 | **Updating** | কোনো element-এর মান পরিবর্তন | O(1) যদি position জানা থাকে |
| 6 | **Sorting** | নির্দিষ্ট ক্রমে সাজানো | O(n log n) |
| 7 | **Merging** | দুটি structure একত্র করা | O(n + m) |

### Key Points
1. **Traversal** সব DS-এ সম্ভব, এবং সবসময় **O(n)**।
2. একই operation ভিন্ন DS-এ ভিন্ন complexity দেয় — এটাই DS নির্বাচনের মূল ভিত্তি।
   - Array-তে Access **O(1)**, Linked List-এ **O(n)**
   - Array-তে Insert **O(n)**, Linked List-এ (beginning) **O(1)**
3. Sorting ও Merging-কে অনেক বই **secondary/advanced** operation বলে।

### 🔁 Admission Revision Box
৭টি primitive operation: **Traversing, Searching, Insertion, Deletion, Updating, Sorting, Merging**। Traversal সবসময় **O(n)**। একই operation ভিন্ন DS-এ ভিন্ন খরচ — Array Access O(1)/Insert O(n), Linked List Access O(n)/Insert O(1)।

---

## Topic 6: Performance of Data Structures ⭐⭐⭐

### Definition (English)
**Performance** of a data structure refers to how efficiently it performs operations in terms of **Time** and **Memory (Space)**.

⭐ **Keywords:** Efficiency · Time · Space · Input Size

### Concept (বাংলায়)
একটি DS ভালো কি না তা নাম দেখে নয় — কত দ্রুত (Time) এবং কত কম memory (Space) ব্যবহার করে সেটার উপর নির্ভর করে।

Performance বিচার হয় এই operation-গুলোর উপর: Insertion, Deletion, Searching, Traversing, Updating, Sorting।

### Time Complexity
**Definition:** The amount of time an algorithm takes as the **input size increases**.

⚠️ এটি ঘড়ির সময় নয় — এটি **বৃদ্ধির হার**।
10 → 10 comparison, 100 → 100 comparison, 1000 → 1000 comparison = **O(n)**

### Space Complexity
**Definition:** The amount of **memory** required by an algorithm during execution.

শুধু ২–৩টি variable ব্যবহার করলে → O(1)। নতুন বড় array বানালে → O(n)।

### Types of Cases ⭐

| Case | Definition | Notation |
|---|---|---|
| **Best Case** | সর্বনিম্ন সময় (সবচেয়ে অনুকূল input) | Ω (Omega) |
| **Average Case** | সাধারণ input-এ প্রত্যাশিত সময় | Θ (Theta) |
| **Worst Case** | সর্বোচ্চ সময় (সবচেয়ে খারাপ input) | **O (Big-O)** |

⭐ Admission test-এ প্রায় সবসময় **Worst Case** জিজ্ঞেস করা হয়।

### Order of Growth ⭐⭐⭐ (মুখস্থ)
```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

| Complexity | নাম | উদাহরণ |
|---|---|---|
| **O(1)** | Constant | Array access, Hash lookup |
| **O(log n)** | Logarithmic | Binary Search, BST search |
| **O(n)** | Linear | Linear Search, Traversal |
| **O(n log n)** | Linearithmic | Merge/Heap/Quick Sort |
| **O(n²)** | Quadratic | Bubble/Selection/Insertion Sort |
| **O(2ⁿ)** | Exponential | Naive Fibonacci, Subset |

### Sorting Complexity Table ⭐⭐⭐

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1)* |
| **Bubble Sort** | O(n)** | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | **O(n)** |
| **Quick Sort** | O(n log n) | O(n log n) | **O(n²)** | O(log n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | **O(1)** |

\* Iterative Binary Search = O(1) space; Recursive = O(log n)
\*\* Bubble Sort-এর Best O(n) শুধুমাত্র swap-flag optimization থাকলে

### Search Complexity by Data Structure ⭐⭐⭐

| Data Structure | Search Time | Space |
|---|---|---|
| Array (Unsorted) | O(n) | O(n) |
| Array (Sorted + Binary Search) | **O(log n)** | O(n) |
| Linked List | O(n) | O(n) |
| Stack / Queue | O(n) | O(n) |
| BST (Average) | **O(log n)** | O(n) |
| BST (Worst / Skewed) | **O(n)** | O(n) |
| Balanced BST (AVL / Red-Black) | **O(log n)** | O(n) |
| Hash Table (Average) | **O(1)** | O(n) |
| Hash Table (Worst) | **O(n)** | O(n) |

### ⭐ MCQ Shortcut (৩০ সেকেন্ডে মুখস্থ)
- Linear Search → **O(n)**
- Binary Search → **O(log n)**
- Hash Table → **O(1)** average, O(n) worst
- BST → **O(log n)** average, O(n) worst
- Bubble / Selection / Insertion → **O(n²)**
- Merge / Heap → **O(n log n)** সবসময়
- Quick Sort → Average **O(n log n)**, Worst **O(n²)**

### 🔁 Admission Revision Box
Performance = **Time + Space**। Time Complexity = input বাড়লে কাজ কত দ্রুত বাড়ে। **Best = Ω, Average = Θ, Worst = O** (admission-এ Worst-ই বেশি আসে)। Growth: **1 < log n < n < n log n < n² < 2ⁿ**। Search: Hash **O(1)** < BST/Binary **O(log n)** < Linear **O(n)**।

---
---

# MODULE 2 — ARRAY ⭐⭐⭐

## Topic 1: Array

### Definition (English)
An **Array** is a **linear** data structure that stores a **fixed-size** collection of elements of the **same data type** in **contiguous memory locations**.

⭐ **Keywords:** Linear · Same Data Type · Fixed Size · Contiguous Memory · Index

### Concept (বাংলায়)
Array-তে একই ধরনের অনেকগুলো data **পরপর (contiguous)** memory-তে রাখা হয়। প্রতিটি element-এর একটি **index** থাকে।

```
Index :   0    1    2    3    4
Value :  10   20   30   40   50
```

Memory contiguous বলেই যেকোনো element-এর address সরাসরি হিসাব করা যায় — এজন্যই **random access O(1)**।

### Formula / Rules ⭐⭐⭐

**Address(A[i]) = Base Address + (i × Size of Data Type)**

**Example:** Base = 1000, int = 4 bytes
```
A[0] = 1000
A[1] = 1004
A[2] = 1008
A[3] = 1012
```

**2D Array address (Row-Major, C/C++/Java):**
`Address(A[i][j]) = Base + [(i × total_columns) + j] × size`

**2D Array address (Column-Major, FORTRAN):**
`Address(A[i][j]) = Base + [(j × total_rows) + i] × size`

**কেন index 0 থেকে শুরু?** A[0]-এর offset = 0, তাই address গণনা সবচেয়ে সহজ ও দ্রুত।

### Characteristics
1. Linear Data Structure
2. **Homogeneous** — সব element একই type
3. **Fixed size** (static allocation)
4. **Contiguous** memory
5. **Random access** by index

### Advantages / Disadvantages

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Fast random access **O(1)** | Size fixed, বাড়ানো যায় না |
| Simple implementation | Insertion/Deletion ব্যয়বহুল O(n) |
| Pointer overhead নেই | Memory অপচয় হতে পারে |
| **Cache-friendly** (contiguous) | শুধু একই data type রাখা যায় |

### Time & Space Complexity ⭐

| Operation | Complexity |
|---|---|
| **Access by index** | **O(1)** |
| Traversal | O(n) |
| Linear Search | O(n) |
| Binary Search (sorted) | **O(log n)** |
| Insertion (beginning/middle) | O(n) |
| Insertion (end, খালি জায়গা থাকলে) | O(1) |
| Deletion (beginning/middle) | O(n) |
| Update (index জানা) | **O(1)** |
| Space | O(n) |

### ⚠️ Common MCQ Traps
- Array-তে **access O(1)**, কিন্তু **search O(n)** — এই দুটো আলাদা।
- Array **static**, size compile time-এ নির্ধারিত।
- 2D Array memory-তেও শেষ পর্যন্ত **linear** ভাবেই থাকে (Row-Major)।

### 🔁 Admission Revision Box
Array = **Linear + Same type + Fixed size + Contiguous memory + Index**। **Access O(1)**, Search O(n), Binary Search O(log n), Insert/Delete **O(n)**, Update O(1)। Address = **Base + i × size**। Index 0 থেকে শুরু কারণ offset = 0। Cache-friendly কিন্তু size fixed।

---

## Topic 2: Array Operations

### 1. Traversing
**Definition:** Visiting each element of an array **exactly once**.
```
FOR i = 0 to n-1: Print A[i]
```
**Time: O(n)** — display, sum, average, max, min বের করতে ব্যবহৃত।

### 2. Insertion
**Definition:** Adding a new element at a specified position.
মাঝে বসাতে হলে ডান পাশের সব element **এক ধাপ ডানে shift** করতে হয়।
```
আগে:  10 20 __ 40 50
index 2-তে 30 বসানো → 40, 50 shift → 10 20 30 40 50
```
| Position | Complexity |
|---|---|
| Beginning | **O(n)** |
| Middle | **O(n)** |
| End | **O(1)** (খালি জায়গা থাকলে) |

### 3. Deletion
**Definition:** Removing an existing element.
Delete করার পর ডান পাশের element-গুলো **বামে shift** হয়।
```
10 20 30 40 50 → (30 delete) → 10 20 40 50
```
| Position | Complexity |
|---|---|
| Beginning / Middle | **O(n)** |
| End | **O(1)** |

### 4. Searching
| Type | শর্ত | Complexity |
|---|---|---|
| **Linear Search** | কোনো শর্ত নেই | **O(n)** |
| **Binary Search** | Array **sorted** হতে হবে | **O(log n)** |

### 5. Updating
Index জানা থাকলে সরাসরি মান পরিবর্তন → **O(1)**।

### Summary Table ⭐

| Operation | Time Complexity |
|---|---|
| Traversal | O(n) |
| Insertion | O(n) |
| Deletion | O(n) |
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Update / Access | **O(1)** |

### 🔁 Admission Revision Box
Array Operations: **Traversal O(n)**, **Insert O(n)** (end-এ O(1)), **Delete O(n)** (end-এ O(1)), **Linear Search O(n)**, **Binary Search O(log n)** (sorted লাগবে), **Update/Access O(1)**। Insert-এ ডানে shift, Delete-এ বামে shift।

---

## Topic 3: Types of Arrays

### 1. One-Dimensional (1D) Array
**Definition:** A linear collection of elements accessed using a **single index**.
```c
int A[5];        // Index: 0 1 2 3 4
```

### 2. Two-Dimensional (2D) Array
**Definition:** An **array of arrays** where elements are arranged in **rows and columns**.
⭐ **Keyword:** Rows and Columns · Matrix
```c
int A[3][3];
      C0  C1  C2
R0     1   2   3
R1     4   5   6
R2     7   8   9

A[1][2] = 6
```
**Real Example:** ছাত্রদের বিষয়ভিত্তিক নম্বর (row = student, column = subject)।

### 3. Multidimensional Array
**Definition:** An array with **more than two dimensions**.
```c
int A[2][3][4];   // 3 dimensions
```

### Memory Representation ⭐
2D Array হলেও memory-তে element-গুলো **linear ভাবেই** সংরক্ষিত হয়।

| Order | কীভাবে | ব্যবহৃত ভাষা |
|---|---|---|
| **Row-Major** | সারি ধরে ধরে: 1 2 3 4 5 6 7 8 9 | **C, C++, Java, Python** |
| **Column-Major** | কলাম ধরে ধরে: 1 4 7 2 5 8 3 6 9 | **FORTRAN, MATLAB, R** |

### Comparison

| Feature | 1D Array | 2D Array |
|---|---|---|
| Index | একটি | **দুটি** |
| Structure | Linear (List) | Matrix (Rows & Columns) |
| Declaration | `int A[5]` | `int A[3][3]` |
| Total elements | n | rows × columns |

### ⚠️ MCQ Trap
- `int A[3][4]`-এ মোট element = **12**, index চলে A[0][0] থেকে A[2][3] পর্যন্ত।
- C/C++ **Row-Major**, FORTRAN **Column-Major** ⭐

### 🔁 Admission Revision Box
**1D** = এক index, linear। **2D** = দুই index, rows × columns (matrix)। **Multidimensional** = 2-এর বেশি dimension। Memory-তে 2D-ও linear ভাবে থাকে — **C/C++/Java = Row-Major**, **FORTRAN = Column-Major**। Address = Base + [(i×cols)+j] × size।

---
---

# MODULE 3 — LINKED LIST ⭐⭐⭐

## Topic 1: Linked List

### Definition (English)
A **Linked List** is a **linear** data structure in which elements are stored as **nodes**, where each node contains **data** and a **pointer (link)** to the next node.

⭐ **Keywords:** Linear · Node · Pointer/Link · Dynamic Memory · Non-contiguous

### Concept (বাংলায়)
Array-তে element পাশাপাশি (contiguous) থাকে। কিন্তু Linked List-এ node memory-র **যেকোনো জায়গায়** থাকতে পারে — তারা **pointer** দিয়ে একে অপরের সাথে যুক্ত।

**একটি Node-এর গঠন:**
```
+---------+---------+
|  Data   |  Next   |
+---------+---------+
```

**পুরো List:**
```
Head
 ↓
[10 | •]→[20 | •]→[30 | NULL]
```
- **Head** = প্রথম node-এর address
- **NULL** = শেষ node

### কেন Linked List দরকার?
Array-এর বড় সমস্যা **fixed size**। ভরে গেলে নতুন element যোগ করা যায় না।
Linked List-এ memory **runtime-এ allocate** হয় (Heap-এ), তাই প্রয়োজন অনুযায়ী node যোগ/বাদ দেওয়া যায়।

### Characteristics
1. Linear Data Structure
2. **Dynamic Size**
3. **Non-contiguous** memory allocation
4. **Pointer** ব্যবহার করে
5. **Sequential Access** only (random access নেই)

### Advantages / Disadvantages

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Dynamic size | **Random access নেই** |
| Insertion/Deletion সহজ | Pointer-এর জন্য extra memory |
| Fixed size-এর অপচয় নেই | Search ধীর |
| Contiguous memory লাগে না | **Cache-unfriendly** |

### 🔁 Admission Revision Box
Linked List = **Node (Data + Pointer)** দিয়ে গঠিত linear DS। Memory **non-contiguous**, size **dynamic**, allocation **runtime**-এ (Heap)। **Head** = প্রথম node, **NULL** = শেষ। Random access নেই — **sequential** only।

---

## Topic 2: Types of Linked List ⭐

### 1. Singly Linked List (SLL)
```
[10|•]→[20|•]→[30|NULL]
```
- একটি pointer (**Next**)
- **শুধু forward traversal**
- সবচেয়ে কম memory

### 2. Doubly Linked List (DLL)
```
NULL←[10]⇄[20]⇄[30]→NULL
```
- **দুটি pointer** (**Prev** ও **Next**)
- **Forward ও Backward** দুই দিকেই traversal
- বেশি memory লাগে
- **Deletion সহজ** — আগের node-এ ফেরা যায়
- **ব্যবহার:** Browser history (forward/back), Music player, LRU Cache

### 3. Circular Linked List (CLL)
```
[10]→[20]→[30]
 ↑___________|
```
- শেষ node প্রথম node-কে দেখায়
- **কোনো NULL নেই**
- **ব্যবহার:** Round Robin CPU Scheduling, Multiplayer game turns

### 4. Circular Doubly Linked List
DLL + Circular — উভয় দিকে ঘোরা যায়, শেষ-শুরু যুক্ত।

### Comparison ⭐

| Type | Pointers | Traversal | NULL আছে? |
|---|---|---|---|
| **Singly** | 1 (Next) | Forward only | ✅ শেষে |
| **Doubly** | 2 (Prev, Next) | **Both ways** | ✅ দুই প্রান্তে |
| **Circular** | 1 | Forward, circular | ❌ **নেই** |
| **Circular Doubly** | 2 | Both, circular | ❌ নেই |

### 🔁 Admission Revision Box
**SLL** = 1 pointer, forward only। **DLL** = 2 pointer (prev+next), দুই দিকে traversal, deletion সহজ, browser history। **CLL** = শেষ node → প্রথম node, **NULL নেই**, Round Robin scheduling।

---

## Topic 3: Linked List Operations & Complexity

### Time Complexity ⭐⭐⭐

| Operation | Complexity |
|---|---|
| Access by position | **O(n)** |
| Search | **O(n)** |
| **Insert at Beginning** | **O(1)** ⭐ |
| Insert at End | O(n)* |
| Insert at Middle (position জানা) | O(n) (খুঁজতে) |
| **Delete at Beginning** | **O(1)** ⭐ |
| Delete at End | O(n) |
| Delete by Value | O(n) |
| Space | O(n) |

\* Tail pointer থাকলে Insert at End = **O(1)**

### Array vs Linked List ⭐⭐⭐ (সবচেয়ে বেশি আসা তুলনা)

| Feature | **Array** | **Linked List** |
|---|---|---|
| Memory | **Contiguous** | **Non-contiguous** |
| Size | **Fixed (Static)** | **Dynamic** |
| Allocation | Compile time (Stack) | Run time (**Heap**) |
| **Access** | **O(1)** random | **O(n)** sequential |
| **Insert/Delete (beginning)** | **O(n)** | **O(1)** |
| Pointer | লাগে না | **লাগে (extra memory)** |
| Cache | **Cache-friendly** | Cache-unfriendly |
| Memory অপচয় | হতে পারে (unused slot) | হয় না (কিন্তু pointer overhead) |
| Binary Search | ✅ সম্ভব | ❌ কার্যকর নয় |

### ⚠️ Common MCQ Traps
- Linked List-এ **Binary Search কার্যকর নয়** (random access নেই) ⭐
- "Linked List-এ insertion সবসময় O(1)" → **ভুল**। Beginning-এ O(1), কিন্তু নির্দিষ্ট position খুঁজে বের করতে O(n)।
- Linked List **memory বাঁচায় না** সবসময় — pointer-এর জন্য extra memory লাগে।
- Linked List sort করতে **Merge Sort সেরা** (Quick Sort নয়)।

### 🔁 Admission Revision Box
Linked List: **Access O(n)**, **Search O(n)**, **Insert/Delete at beginning O(1)**, end-এ O(n) (tail থাকলে O(1))। **Array vs LL:** Array = contiguous, fixed, access O(1), insert O(n)। LL = non-contiguous, dynamic, access O(n), insert O(1)। LL-এ **Binary Search চলে না**।

---
---

# MODULE 4 — STACK ⭐⭐⭐

## Topic 1: Stack

### Definition (English)
A **Stack** is a **linear** data structure that follows the **LIFO (Last In, First Out)** principle, where insertion and deletion occur at **one end** called the **Top**.

⭐ **Keywords:** Linear · **LIFO** · Top · Push · Pop

### Concept (বাংলায়)
যে element সবার **শেষে ঢোকে**, সেটাই সবার **আগে বের হয়** — এটাই **LIFO**।
সব কাজ হয় শুধু **এক প্রান্তে (Top)**।

```
Push 10, Push 20, Push 30:

       TOP
        ↓
      ┌────┐
      │ 30 │ ← প্রথমে বের হবে
      ├────┤
      │ 20 │
      ├────┤
      │ 10 │
      └────┘

Pop() → 30, তারপর Pop() → 20
```

### Main Operations ⭐

| Operation | কাজ | Time |
|---|---|---|
| **Push(x)** | Top-এ element ঢোকানো | **O(1)** |
| **Pop()** | Top-এর element বের করা | **O(1)** |
| **Peek() / Top()** | Top-এর element দেখা (বের না করে) | **O(1)** |
| **isEmpty()** | Stack খালি কিনা | **O(1)** |
| **isFull()** | Stack ভরা কিনা (array-তে) | **O(1)** |

⭐ Stack-এর **সব operation O(1)** — এটাই এর প্রধান শক্তি।
কিন্তু **Search = O(n)** (সব element pop করতে হয়)।

### Overflow & Underflow ⭐⭐⭐

| Condition | কখন হয় |
|---|---|
| **Stack Overflow** | **Full** stack-এ **Push** করলে |
| **Stack Underflow** | **Empty** stack থেকে **Pop** করলে |

⭐ Shortcut: **Full + Push = Overflow** · **Empty + Pop = Underflow**

### Implementation
Stack দুইভাবে implement করা যায় — **Array** ও **Linked List**। ✅
- Array দিয়ে: সহজ, কিন্তু size fixed → Overflow সম্ভব
- Linked List দিয়ে: dynamic, Overflow নেই (memory থাকা পর্যন্ত)

### Time & Space Complexity

| Operation | Complexity |
|---|---|
| Push / Pop / Peek / isEmpty | **O(1)** |
| Search | O(n) |
| Space | O(n) |

### 🔁 Admission Revision Box
Stack = **Linear + LIFO**, সব কাজ **Top**-এ। Operations: **Push, Pop, Peek, isEmpty — সবই O(1)**, Search O(n)। **Full+Push = Overflow**, **Empty+Pop = Underflow**। Array ও Linked List — **দুইভাবেই** implement করা যায়।

---

## Topic 2: Applications of Stack ⭐⭐⭐

### 1. Function Call Management
```
main() → login() → verifyPassword()
```
`verifyPassword()` আগে শেষ হবে, তারপর `login()`, তারপর `main()`।
➡️ **Last Called → First Returned** = LIFO। এটাই **Call Stack**।

### 2. Recursion
```
factorial(3) → factorial(2) → factorial(1)
Return:  1 → 2 → 6
```
প্রতিটি recursive call Stack-এ জমা হয়। Stack ভরে গেলে → **Stack Overflow**।

### 3. Undo / Redo
MS Word-এ Type A → Type B → Type C। Undo চাপলে **C আগে** মুছবে, তারপর B।

### 4. Browser Back Button
Google → YouTube → Facebook। Back চাপলে Facebook → YouTube → Google।
➡️ Last visited → First back।

### 5. Expression Evaluation & Conversion ⭐
`A + B * C` — `*`-এর precedence বেশি। Compiler Stack ব্যবহার করে সঠিক order নির্ধারণ করে।

**Expression Notations (MCQ-তে আসে):**

| Notation | রূপ | উদাহরণ |
|---|---|---|
| **Infix** | operand **operator** operand | `A + B` |
| **Prefix (Polish)** | **operator** operand operand | `+ A B` |
| **Postfix (Reverse Polish)** | operand operand **operator** | `A B +` |

⭐ Infix → Postfix/Prefix রূপান্তর এবং Postfix evaluation — দুটোতেই **Stack** ব্যবহৃত হয়।
উদাহরণ: `(A+B)*C` → Postfix: `AB+C*`

### 6. Parentheses / Bracket Matching ⭐
`(` দেখলে **Push**, `)` দেখলে **Pop**।
শেষে Stack **empty** হলে → Balanced ✅
`((A+B)` → শেষে Stack empty নয় → **Not Balanced** ❌

### 7. DFS (Depth First Search)
Graph traversal-এ Stack (বা recursion) ব্যবহৃত হয়।

### Summary Table ⭐

| Application | Real Example |
|---|---|
| Function Calls | main() → A() → B() |
| Recursion | factorial(n), Tower of Hanoi |
| Undo/Redo | MS Word, Photoshop |
| Browser Back | Chrome Back button |
| Expression Evaluation | Infix → Postfix, `(A+B)*C` |
| Parentheses Matching | `(( ))` balanced check |
| **DFS** | Graph traversal |

### 🔁 Admission Revision Box
Stack Applications: **Function call (call stack), Recursion, Undo/Redo, Browser Back, Expression evaluation (Infix→Postfix), Parentheses matching, DFS**। Notations: Infix `A+B`, Prefix `+AB`, Postfix `AB+`। Bracket matching: `(` push, `)` pop, শেষে empty = balanced।

---
---

# MODULE 5 — QUEUE ⭐⭐⭐

## Topic 1: Queue

### Definition (English)
A **Queue** is a **linear** data structure that follows the **FIFO (First In, First Out)** principle, where insertion occurs at the **Rear** and deletion at the **Front**.

⭐ **Keywords:** Linear · **FIFO** · Front · Rear · Enqueue · Dequeue

### Concept (বাংলায়)
যে element **আগে আসে**, সেটাই **আগে বের হয়** — **FIFO**।
Stack-এর মতো এক প্রান্ত নয়, Queue-তে **দুই প্রান্ত** ব্যবহৃত হয়।

```
Front                     Rear
  ↓                         ↓
 10  →  20  →  30  →  40

Deletion ← Front        Rear ← Insertion
```

**Real Example:** ব্যাংকের লাইন — যে আগে এসেছে, সে আগে service পাবে।

### Main Operations ⭐

| Operation | কাজ | Time |
|---|---|---|
| **Enqueue** | Rear-এ element ঢোকানো | **O(1)** |
| **Dequeue** | Front থেকে element বের করা | **O(1)** |
| **Front / Peek** | প্রথম element দেখা | **O(1)** |
| **isEmpty** | খালি কিনা | **O(1)** |

### Overflow & Underflow
- **Queue Overflow** — **Full** queue-তে **Enqueue** করলে
- **Queue Underflow** — **Empty** queue থেকে **Dequeue** করলে

### Applications of Queue ⭐

| Application | ব্যাখ্যা |
|---|---|
| **Printer Queue / Spooling** | যে job আগে এসেছে, আগে print হবে |
| **CPU Scheduling** | FCFS, Round Robin |
| **BFS (Breadth First Search)** ⭐ | Graph/Tree traversal |
| **Call Center** | আগে call করা customer আগে service |
| **Ticket Counter** | আগে আসা ব্যক্তি আগে ticket |
| **Buffer / Data Streaming** | Keyboard buffer, IO buffer |
| **Level Order Traversal** | Tree-তে স্তরে স্তরে ঘোরা |

### Stack vs Queue ⭐⭐⭐

| Feature | **Stack** | **Queue** |
|---|---|---|
| নীতি | **LIFO** | **FIFO** |
| Insert | **Push** (Top) | **Enqueue** (Rear) |
| Delete | **Pop** (Top) | **Dequeue** (Front) |
| প্রান্ত | **এক প্রান্ত (Top)** | **দুই প্রান্ত (Front, Rear)** |
| Pointer | Top | Front & Rear |
| ব্যবহার | Recursion, Undo, Browser Back, **DFS** | Scheduling, Printer, **BFS** |

⭐ **DFS = Stack, BFS = Queue** — এটা নিশ্চিত MCQ।

### 🔁 Admission Revision Box
Queue = **Linear + FIFO**, Insert **Rear** (Enqueue), Delete **Front** (Dequeue), সব O(1)। Full+Enqueue = Overflow, Empty+Dequeue = Underflow। ব্যবহার: **Printer, CPU Scheduling, BFS, Buffer**। **Stack = LIFO/এক প্রান্ত/DFS**, **Queue = FIFO/দুই প্রান্ত/BFS**।

---

## Topic 2: Types of Queue ⭐

### 1. Simple Queue (Linear Queue)
**Definition:** A linear queue that follows FIFO — insert at Rear, delete at Front.

⚠️ **Limitation:** Front থেকে delete করার পর শুরুতে যে খালি জায়গা তৈরি হয়, সেটা **আর ব্যবহার করা যায় না** (array implementation-এ)। এটাকে বলে **false overflow**।

### 2. Circular Queue
**Definition:** A queue in which the **last position is connected back to the first**, forming a circle.

```
      0
   ┌─────┐
 3 │     │ 1
   └─────┘
      2
```
✅ Simple Queue-এর খালি জায়গার সমস্যা সমাধান করে — memory পুনর্ব্যবহার হয়।

**Formula ⭐:**
- `Rear = (Rear + 1) % SIZE`
- `Front = (Front + 1) % SIZE`

**Real Example:** **Round Robin CPU Scheduling**, Traffic light system।

### 3. Priority Queue
**Definition:** A queue in which elements are removed based on **priority**, not arrival order.

```
Patient A (Critical), B (Normal), C (Emergency)
Service order: Emergency → Critical → Normal
```
**Real Example:** Hospital Emergency, OS Priority Scheduling, Dijkstra's algorithm।
সাধারণত **Heap** দিয়ে implement করা হয় → O(log n)।

### 4. Double Ended Queue (Deque)
**Definition:** A queue in which insertion and deletion can be performed at **both ends** (Front and Rear).

```
← 10 ⇄ 20 ⇄ 30 →
```
**দুই উপপ্রকার:**
- **Input-restricted Deque** — শুধু এক প্রান্তে insert, দুই প্রান্তে delete
- **Output-restricted Deque** — দুই প্রান্তে insert, শুধু এক প্রান্তে delete

**Real Example:** Browser history, Sliding Window algorithms, Undo/Redo।
⭐ Deque দিয়ে **Stack ও Queue দুটোই** বানানো যায়।

### Comparison Table ⭐⭐⭐

| Type | Insert | Delete | Special Feature |
|---|---|---|---|
| **Simple Queue** | Rear | Front | FIFO, খালি জায়গা নষ্ট হয় |
| **Circular Queue** | Rear | Front | **খালি জায়গা পুনর্ব্যবহার** |
| **Priority Queue** | Priority অনুযায়ী | সর্বোচ্চ priority আগে | **Priority-based, FIFO নয়** |
| **Deque** | Front বা Rear | Front বা Rear | **দুই প্রান্তই ব্যবহারযোগ্য** |

### ⚠️ MCQ Traps
- **Priority Queue FIFO মানে না** ⚠️ — এটা সবচেয়ে বেশি ভুল হয়।
- Circular Queue-তে `%` (modulus) দিয়ে index wrap করা হয়।
- Deque = Stack + Queue দুটোরই কাজ করতে পারে।

### 🔁 Admission Revision Box
৪ ধরনের Queue: **Simple** (FIFO, খালি জায়গা নষ্ট), **Circular** (`%` দিয়ে wrap, জায়গা পুনর্ব্যবহার, Round Robin), **Priority** (priority অনুযায়ী, FIFO নয়, Heap দিয়ে), **Deque** (দুই প্রান্তেই insert/delete, Stack+Queue দুটোই বানানো যায়)।

---
---

# MODULE 6 — TREE ⭐⭐⭐

## Topic 1: Tree

### Definition (English)
A **Tree** is a **non-linear**, **hierarchical** data structure consisting of **nodes** connected by **edges**, with one node designated as the **root** and **no cycles**.

⭐ **Keywords:** Non-Linear · Hierarchical · Root · Node · Edge · Acyclic

### Concept (বাংলায়)
Array, Linked List, Stack, Queue — সব **Linear**।
Tree হলো **Non-Linear** — data উপর থেকে নিচে **hierarchy** আকারে সাজানো।
একটি node-এর নিচে একাধিক child থাকতে পারে, কিন্তু **parent একটাই**।

**Real Example 1 — File System:** Folder-এর ভিতরে folder।
**Real Example 2 — HTML DOM:** `<html>` → `<body>` → `<div>` → `<p>`

### Terminology ⭐

| Term | অর্থ |
|---|---|
| **Root** | সবার উপরের node (parent নেই) |
| **Parent** | যার নিচে অন্য node আছে |
| **Child** | কোনো node-এর নিচের node |
| **Siblings** | একই parent-এর children |
| **Leaf (Terminal)** | যার কোনো child নেই |
| **Internal Node** | যার অন্তত একটি child আছে |
| **Degree of node** | ঐ node-এর children সংখ্যা |
| **Degree of tree** | সর্বোচ্চ degree |
| **Level** | Root = 0, নিচে 1, 2 … |
| **Height of tree** | Root থেকে সবচেয়ে দূরের leaf পর্যন্ত **edge** সংখ্যা |
| **Depth of node** | Root থেকে ঐ node পর্যন্ত edge সংখ্যা |
| **Subtree** | কোনো node ও তার সব descendant |

### Key Points
1. **n নোড থাকলে edge = n − 1** ⭐⭐⭐ (নিশ্চিত MCQ)
2. Tree-তে **কোনো cycle নেই**
3. Root থেকে প্রতিটি node-এ **ঠিক একটি path**
4. Root ছাড়া প্রতিটি node-এর **exactly one parent**
5. **Tree = Connected + Acyclic Graph** — Tree হলো Graph-এর একটি বিশেষ রূপ

### ⚠️ MCQ Traps
- Height গণনায় **edge** না **node**? — প্রশ্নে "edges" বললে একক node-এর tree-র height = **0**।
- Tree হলো Graph-এর subset, উল্টোটা নয়।

### 🔁 Admission Revision Box
Tree = **Non-linear + Hierarchical + Acyclic**, root একটাই, প্রতিটি node-এর parent একটাই। **n নোড → n−1 edge**। Leaf = child নেই। Height = root থেকে সবচেয়ে দূরের leaf পর্যন্ত edge। Tree = connected acyclic graph। উদাহরণ: File System, HTML DOM।

---

## Topic 2: Binary Tree

### Definition (English)
A **Binary Tree** is a tree in which every node has **at most two children**, called the **left child** and **right child**.

⭐ **Keywords:** At most 2 children · Left · Right

### Types of Binary Tree ⭐⭐⭐

| Type | Definition |
|---|---|
| **Full (Strict)** | প্রতিটি node-এর **0 বা 2** টি child (কখনো 1 নয়) |
| **Complete** | শেষ level ছাড়া সব level পূর্ণ, শেষ level **বাম থেকে** পূরণ |
| **Perfect** | সব internal node-এর 2টি child **এবং** সব leaf একই level-এ |
| **Balanced** | বাম-ডান subtree-র height পার্থক্য ≤ 1 |
| **Skewed** | সব node এক পাশে (Linked List-এর মতো) — worst case |
| **Degenerate** | প্রতিটি parent-এর ঠিক 1টি child |

### Formula / Rules ⭐⭐⭐ (এখান থেকেই সরাসরি MCQ)

| # | Formula |
|---|---|
| 1 | Level `i`-তে সর্বোচ্চ node = **2^i** (root = level 0) |
| 2 | Height `h`-এর tree-তে সর্বোচ্চ node = **2^(h+1) − 1** |
| 3 | `n` নোডের **minimum height = ⌊log₂ n⌋** |
| 4 | `n` নোডের **maximum height = n − 1** (skewed) |
| 5 | Full binary tree: **Leaf = Internal + 1** |
| 6 | যেকোনো binary tree: **L = D₂ + 1** (Leaf = 2-child node + 1) |
| 7 | `n` নোডের binary tree-তে **NULL pointer = n + 1** |

**Example:** Height 3-এর perfect binary tree → node = 2⁴ − 1 = **15**

### Key Points
1. **Complete ≠ Full ≠ Perfect** — এই তিনটা গুলিয়ে ফেলা সবচেয়ে বড় ভুল।
2. **Perfect** হলে সেটা অবশ্যই Full **ও** Complete।
3. **Heap সবসময় Complete Binary Tree**।
4. Skewed tree-তে সব operation **O(n)** — এজন্যই balancing দরকার।

### 🔁 Admission Revision Box
Binary Tree = প্রতিটি node-এর ≤ 2 child। **Full** = 0 বা 2 child, **Complete** = শেষ level বাদে ভরা + বাম থেকে, **Perfect** = সব leaf একই level। মুখস্থ: **Level i-তে max = 2^i**, **height h-এ max node = 2^(h+1) − 1**, **min height = ⌊log₂n⌋**, **n নোডে NULL pointer = n+1**।

---

## Topic 3: Tree Traversal ⭐⭐⭐

### Definition (English)
**Tree Traversal** is the process of visiting each node of a tree **exactly once** in a systematic order.

### The 4 Traversals

**Tree:**
```
        1
       / \
      2   3
     / \
    4   5
```

| Traversal | Order | Result |
|---|---|---|
| **Preorder** | **Root → Left → Right** | 1, 2, 4, 5, 3 |
| **Inorder** | **Left → Root → Right** | 4, 2, 5, 1, 3 |
| **Postorder** | **Left → Right → Root** | 4, 5, 2, 3, 1 |
| **Level Order** | স্তরে স্তরে (BFS) | 1, 2, 3, 4, 5 |

### মনে রাখার Shortcut ⭐
**Root কোথায় বসে, সেটাই নাম:**
- **Pre**order → Root **আগে**
- **In**order → Root **মাঝে**
- **Post**order → Root **শেষে**

Left সবসময় Right-এর আগে।

### Key Points
1. **BST-এর Inorder traversal = Sorted (ascending) order** ⭐⭐⭐ — সবচেয়ে বেশি আসা MCQ
2. Pre/In/Post → **Stack / Recursion** ব্যবহার করে
3. **Level Order → Queue** ব্যবহার করে (BFS)
4. **Postorder** → tree delete করতে (child আগে delete)
5. **Preorder** → tree copy করতে, expression-এর **Prefix** form
6. **Postorder** → expression-এর **Postfix** form
7. **Inorder** → expression-এর **Infix** form

### ⚠️ Common MCQ Traps ⭐
- **Inorder + Preorder** → unique tree **✅ যায়**
- **Inorder + Postorder** → unique tree **✅ যায়**
- **Preorder + Postorder** → unique tree **❌ যায় না** (Inorder ছাড়া হয় না)

### Time & Space Complexity

| | Time | Space |
|---|---|---|
| যেকোনো traversal | **O(n)** | O(h) stack (worst O(n)) |
| Level Order | **O(n)** | O(n) queue |

### 🔁 Admission Revision Box
**Pre = Root-Left-Right, In = Left-Root-Right, Post = Left-Right-Root, Level = BFS (Queue)**। **BST-এর Inorder = sorted** ⭐। Pre/In/Post = Stack/Recursion। **Preorder+Postorder দিয়ে unique tree হয় না**। সব traversal **O(n)**।

---

## Topic 4: Binary Search Tree (BST) ⭐⭐⭐

### Definition (English)
A **Binary Search Tree (BST)** is a binary tree in which, for every node, all values in the **left subtree are smaller** and all values in the **right subtree are greater** than the node's value.

⭐ **Keywords:** Left < Root < Right · Ordered · No Duplicates

### Concept (বাংলায়)
> **বামে ছোট, ডানে বড়।**

এই নিয়মের কারণেই প্রতিবার তুলনা করে **অর্ধেক tree বাদ** দেওয়া যায় — তাই search **O(log n)**।

```
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```
Inorder: 20, 30, 40, 50, 60, 70, 80 → **sorted** ✅

**Real Example:** Database **Index** (B-Tree/B+ Tree হলো BST-এর extension)। এজন্যই indexed column-এ `WHERE` query দ্রুত চলে।

### Operations

**Search 40:** 50 → বামে (40<50) → 30 → ডানে (40>30) → পেলাম। **3 comparison**, 7টা নয়।

**Insert:** Search-এর মতো নিচে নামো, NULL পেলে সেখানে বসাও। নতুন node সবসময় **leaf**।

**Delete — ৩টি Case ⭐**

| Case | কী করবে |
|---|---|
| **Leaf** | সরাসরি delete |
| **1 child** | Child-কে parent-এর সাথে জুড়ে দাও |
| **2 children** | **Inorder successor** (ডান subtree-র সবচেয়ে ছোট) বা **inorder predecessor** দিয়ে replace করে সেটা delete করো |

### Key Points
1. **Inorder = sorted output** — BST-এর সবচেয়ে বড় property
2. সাধারণত **duplicate রাখা হয় না**
3. Average **O(log n)**, কিন্তু **Skewed হলে O(n)** — Linked List-এ পরিণত হয়
4. **Sorted data insert করলে BST skewed হয়ে যায়** ⚠️ — এটাই BST-র বড় দুর্বলতা
5. সমাধান = **Self-balancing BST** (AVL, Red-Black)

### Time & Space Complexity ⭐⭐⭐

| Operation | Best/Average | Worst (Skewed) |
|---|---|---|
| Search | **O(log n)** | **O(n)** |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Space | O(n) | O(n) |

### ⚠️ MCQ Traps
- "BST-তে search always O(log n)" → **ভুল**, worst O(n)।
- **Balanced BST (AVL/Red-Black)**-এ worst case-ও **O(log n)** — এটাই পার্থক্য।

### 🔁 Admission Revision Box
BST = **বামে ছোট, ডানে বড়**। **Inorder = sorted**। Search/Insert/Delete average **O(log n)**, skewed হলে **O(n)**। Delete-এ 2-child case → **inorder successor** দিয়ে replace। Sorted data insert করলে skew হয় → AVL/Red-Black দিয়ে সমাধান।

---

## Topic 5: AVL Tree & Balanced Trees

### Definition (English)
An **AVL Tree** is a **self-balancing BST** in which the **balance factor** (height of left subtree − height of right subtree) of every node is **−1, 0, or +1**.

⭐ **Keywords:** Self-balancing · Balance Factor · Rotation

### Concept (বাংলায়)
BST-র সমস্যা ছিল skew হওয়া। AVL সেটার সমাধান — insert/delete-এর পর নিজে নিজেই **rotation** করে balance ঠিক রাখে।

**Balance Factor = Height(Left) − Height(Right)**
মান −1, 0, +1-এর বাইরে গেলেই rotation।

### 4 Rotations ⭐

| Case | Rotation |
|---|---|
| **LL** (বামের বামে) | Single **Right** Rotation |
| **RR** (ডানের ডানে) | Single **Left** Rotation |
| **LR** (বামের ডানে) | Left তারপর Right (Double) |
| **RL** (ডানের বামে) | Right তারপর Left (Double) |

### Key Points
1. AVL-এ **সব operation guaranteed O(log n)** — worst case-ও
2. **Red-Black Tree** = আরেকটি balanced BST, কম কড়া balance, তাই insert/delete দ্রুত
3. AVL = **search-heavy**-এ ভালো; Red-Black = **insert/delete-heavy**-এ ভালো
4. Java `TreeMap`, C++ `map` → **Red-Black Tree**
5. **B-Tree / B+ Tree** → Database ও File System-এর index (disk-friendly, multi-way)

### Comparison

| Feature | BST | AVL | Red-Black |
|---|---|---|---|
| Balanced? | না | কঠোরভাবে | শিথিলভাবে |
| Search (worst) | **O(n)** | **O(log n)** | **O(log n)** |
| Rotation | নেই | বেশি | কম |
| Best for | সাধারণ | Search | Insert/Delete |

### 🔁 Admission Revision Box
AVL = **self-balancing BST**, **Balance Factor ∈ {−1, 0, +1}**, নাহলে rotation (**LL→Right, RR→Left, LR & RL→Double**)। সব operation **O(log n) guaranteed**। Red-Black = কম কড়া, insert/delete দ্রুত (`TreeMap`, `map`)। **B+ Tree = Database index**।

---

## Topic 6: Heap ⭐⭐⭐

### Definition (English)
A **Heap** is a **complete binary tree** satisfying the **heap property**: in a **Max-Heap** every parent is **≥** its children; in a **Min-Heap** every parent is **≤** its children.

⭐ **Keywords:** Complete Binary Tree · Max-Heap · Min-Heap · Heap Property

### Concept (বাংলায়)
Heap দুইটা শর্ত একসাথে মানে:
1. **Complete Binary Tree** (উপর থেকে নিচে, বাম থেকে ডানে ভরা)
2. **Heap Property** — parent সবসময় children-এর চেয়ে বড় (Max) বা ছোট (Min)

⚠️ **Heap কোনো BST নয়।** Heap-এ বাম-ডানের order নেই, শুধু parent-child সম্পর্ক আছে।

```
Max-Heap:              Min-Heap:
      50                    10
     /  \                  /  \
   30    40              30    20
   / \                   / \
  10  20               50  40
```

**Real Example:** OS-এর **Priority Scheduling** — সবচেয়ে বেশি priority-র process আগে চলে।

### Array Representation ⭐⭐⭐ (MCQ favourite)

Heap array-তে রাখা হয় — pointer লাগে না (কারণ complete tree, কোনো gap নেই)।

**0-based indexing (C/Java/Python):**
- Parent of `i` = **(i − 1) / 2**
- Left child = **2i + 1**
- Right child = **2i + 2**

**1-based indexing:**
- Parent = **i / 2**
- Left = **2i**, Right = **2i + 1**

**Example:** `[50, 30, 40, 10, 20]` → index 0 (50)-এর children index 1 (30) ও 2 (40) ✅

### Key Points
1. Heap = **Complete Binary Tree** → array-তে gap ছাড়া রাখা যায়
2. Max-Heap-এ **root = সবচেয়ে বড়**; Min-Heap-এ root = সবচেয়ে ছোট
3. **Priority Queue** সাধারণত Heap দিয়ে implement করা হয় ⭐
4. **Build Heap = O(n)** — O(n log n) নয়! ⚠️ Classic trap
5. Heap-এ **searching O(n)** — কোনো sorted order নেই

### Time & Space Complexity ⭐

| Operation | Complexity |
|---|---|
| Find Max/Min (peek) | **O(1)** |
| Insert | **O(log n)** |
| Delete Max/Min | **O(log n)** |
| **Build Heap** | **O(n)** ⭐ |
| Search arbitrary | **O(n)** |
| Heap Sort | O(n log n) |
| Space | O(n) |

### ⚠️ MCQ Traps
- "Heap is a BST" → **ভুল**
- "Build Heap = O(n log n)" → **ভুল, O(n)**
- Heap-এ Inorder traversal sorted দেয় **না**

### Heap vs BST ⭐

| Feature | **Heap** | **BST** |
|---|---|---|
| Order | Parent-child মাত্র | Left < Root < Right |
| Find Min/Max | **O(1)** | O(log n) |
| Search | **O(n)** | **O(log n)** |
| Structure | Complete tree (array) | যেকোনো shape |
| ব্যবহার | Priority Queue, Heap Sort | Searching, Sorted data |

### 🔁 Admission Revision Box
Heap = **Complete Binary Tree + Heap Property**। Max-Heap: parent ≥ child। Array-তে: **left = 2i+1, right = 2i+2, parent = (i−1)/2**। Peek **O(1)**, Insert/Delete **O(log n)**, **Build Heap O(n)**, Search **O(n)**। Priority Queue-এর ভিত্তি। **Heap ≠ BST**।

---
---

# MODULE 7 — HASHING ⭐⭐⭐

## Topic 1: Hashing & Hash Table

### Definition (English)
**Hashing** is a technique that maps a **key** to an **index** in a table using a **hash function**, allowing storage and retrieval in **average O(1)** time. The structure is called a **Hash Table**.

⭐ **Keywords:** Hash Function · Key · Index/Bucket · O(1) Average · Collision

### Concept (বাংলায়)
Array-তে খুঁজতে index লাগে, কিন্তু আমরা তো **key** জানি (যেমন Student ID)।
Hashing এই সমস্যার সমাধান — একটি **function** key-কে index-এ রূপান্তর করে।

```
Key → [Hash Function] → Index → Value
```

**Example:** `h(key) = key % 10` → Key 25 → index 5, Key 37 → index 7

**Real Example:** Python `dict`, Java `HashMap`, Database Hash Index, Password storage, Cache।

### Hash Function
ভালো hash function-এর গুণ:
1. দ্রুত compute হয়
2. Key-গুলো **সমানভাবে বিতরণ** করে
3. কম collision তৈরি করে

**সবচেয়ে common — Division Method:** `h(k) = k mod m` (m = table size, সাধারণত **prime number**)

অন্যান্য: Multiplication Method, Mid-Square Method, Folding Method।

### Collision ⭐

**Definition:** **Collision** occurs when two different keys produce the **same hash index**.

Key 25 ও Key 35 — দুটোরই `% 10` = 5। এটাই collision।
Collision **অনিবার্য** (Pigeonhole Principle), তাই handle করতেই হবে।

### Collision Resolution Techniques ⭐⭐⭐

**1. Chaining (Separate Chaining / Open Hashing)**
প্রতিটি index-এ একটি **Linked List**।
```
index 5 → [25] → [35] → [45] → NULL
```
✅ Table কখনো full হয় না ❌ Pointer-এর extra memory

**2. Open Addressing (Closed Hashing)**
Collision হলে table-এর **ভিতরেই** অন্য খালি জায়গা খোঁজা।

| Method | Probe Sequence | সমস্যা |
|---|---|---|
| **Linear Probing** | h(k)+1, h(k)+2, … | **Primary clustering** |
| **Quadratic Probing** | h(k)+1², h(k)+2², … | **Secondary clustering** |
| **Double Hashing** | h₁(k) + i·h₂(k) | সবচেয়ে ভালো distribution |

### Formula / Rules

**Load Factor (α) = n / m**
(n = stored elements, m = table size)

- Open Addressing-এ **α ≤ 1** থাকতেই হবে
- α বাড়লে collision বাড়ে, performance কমে
- সাধারণত **α > 0.7** হলে **rehash** (table দ্বিগুণ করে নতুন করে hash)

### Key Points
1. Average search/insert/delete = **O(1)** — এটাই hashing-এর মূল আকর্ষণ
2. Worst case = **O(n)** (সব key একই index-এ পড়লে)
3. Hash Table-এ data **sorted order-এ থাকে না** ⚠️ — range query (BETWEEN) করা যায় না
4. **Chaining** = table full হয় না; **Open Addressing** = memory efficient কিন্তু full হতে পারে
5. Java `HashMap` = Chaining (বড় bucket-এ Tree-তে রূপান্তরিত হয়)

### Time & Space Complexity ⭐

| Operation | Average | Worst |
|---|---|---|
| Search | **O(1)** | **O(n)** |
| Insert | **O(1)** | O(n) |
| Delete | **O(1)** | O(n) |
| Space | O(n) | O(n) |

### ⚠️ MCQ Traps
- "Hash Table search always O(1)" → **ভুল**, average O(1), worst O(n)
- Hash Table-এ **sorted traversal সম্ভব নয়** — দরকার হলে Balanced BST
- Table size **prime number** নেওয়া ভালো

### 🔁 Admission Revision Box
Hashing = key → hash function → index, average **O(1)**, worst **O(n)**। **Collision** = দুই key একই index। সমাধান: **Chaining** (linked list) ও **Open Addressing** (Linear/Quadratic/Double Hashing)। **Load Factor α = n/m**, α>0.7 হলে rehash। Hash Table-এ sorted order নেই। Example: Python dict, Java HashMap।

---
---

# MODULE 8 — GRAPH ⭐⭐⭐

## Topic 1: Graph

### Definition (English)
A **Graph** is a **non-linear** data structure consisting of a finite set of **vertices (V)** and a set of **edges (E)** connecting pairs of vertices. Denoted **G = (V, E)**.

⭐ **Keywords:** Non-Linear · Vertex · Edge · G = (V, E)

### Concept (বাংলায়)
Tree-তে hierarchy ছিল, cycle ছিল না। Graph-এ কোনো নিয়ম নেই — যেকোনো node যেকোনো node-এর সাথে যুক্ত হতে পারে, cycle-ও থাকতে পারে।

**Real Example 1 — Facebook:** user = vertex, friendship = edge → **Undirected Graph**
**Real Example 2 — Google Maps:** জায়গা = vertex, রাস্তা = edge, দূরত্ব = **weight**, one-way = **Directed**

### Types of Graph

| Type | Definition |
|---|---|
| **Undirected** | Edge-এর দিক নেই (A—B = B—A) |
| **Directed (Digraph)** | Edge-এর দিক আছে (A→B ≠ B→A) |
| **Weighted** | প্রতিটি edge-এ cost/মান |
| **Cyclic** | অন্তত একটি cycle আছে |
| **Acyclic (DAG)** | কোনো cycle নেই |
| **Connected** | প্রতিটি vertex থেকে অন্য সবগুলোতে যাওয়া যায় |
| **Complete** | প্রতিটি vertex অন্য সবার সাথে যুক্ত |

### Terminology

| Term | অর্থ |
|---|---|
| **Degree** | একটি vertex-এ যুক্ত edge সংখ্যা |
| **In-degree / Out-degree** | Directed graph-এ ভিতরে আসা / বাইরে যাওয়া edge |
| **Path** | এক vertex থেকে আরেকটিতে যাওয়ার sequence |
| **Cycle** | শুরু ও শেষ একই vertex-এ |
| **Adjacent** | সরাসরি edge দিয়ে যুক্ত দুই vertex |

### Formula / Rules ⭐⭐⭐

| Rule | Formula |
|---|---|
| Complete **undirected** graph-এ edge | **n(n − 1) / 2** |
| Complete **directed** graph-এ edge | **n(n − 1)** |
| Undirected graph: sum of all degrees | **2 × E** (Handshaking Lemma) |
| **Tree** (connected + acyclic) | **E = V − 1** |
| Undirected graph-এ max edge | n(n−1)/2 |

### Graph Representation ⭐⭐⭐ (সবচেয়ে বেশি আসা প্রশ্ন)

**1. Adjacency Matrix** — V×V আকারের 2D array
```
    A  B  C
A [ 0  1  1 ]
B [ 1  0  0 ]
C [ 1  0  0 ]
```
✅ Edge check **O(1)** ❌ Space **O(V²)**

**2. Adjacency List** — প্রতিটি vertex-এর প্রতিবেশীদের list
```
A → B → C
B → A
C → A
```
✅ Space **O(V + E)** ❌ Edge check O(degree)

### Comparison ⭐⭐⭐

| Feature | **Adjacency Matrix** | **Adjacency List** |
|---|---|---|
| **Space** | **O(V²)** | **O(V + E)** |
| Check edge (u,v) | **O(1)** | O(degree of u) |
| সব প্রতিবেশী খোঁজা | O(V) | **O(degree)** |
| Add edge | O(1) | O(1) |
| ভালো যেখানে | **Dense** graph | **Sparse** graph |
| BFS/DFS time | O(V²) | **O(V + E)** |

### Key Points
1. Graph-এ **cycle থাকতে পারে**, Tree-তে পারে না
2. **Tree = Connected + Acyclic Graph, E = V − 1**
3. Real-world graph সাধারণত **sparse** → **Adjacency List** বেশি ব্যবহৃত
4. **BFS = Queue**, **DFS = Stack/Recursion** ⭐
5. Adjacency List দিয়ে BFS/DFS = **O(V + E)**
6. Undirected graph-এর adjacency matrix **symmetric**

### ⚠️ MCQ Traps
- "Graph-এ n নোড → n−1 edge" → **ভুল**, সেটা Tree-র নিয়ম
- Adjacency Matrix-এর space **O(V²)** — edge সংখ্যা নির্বিশেষে

### 🔁 Admission Revision Box
Graph = **G(V, E)**, non-linear, cycle থাকতে পারে। Directed/Undirected/Weighted/DAG। **Matrix: O(V²) space, O(1) edge check — dense**; **List: O(V+E) space — sparse**। Complete undirected edge = **n(n−1)/2**। **BFS→Queue, DFS→Stack**। **Tree = connected acyclic graph, E = V−1**।

---
---

# MODULE 9 — OTHER DATA STRUCTURES

## Topic 1: Priority Queue

### Definition (English)
A **Priority Queue** is an **ADT** in which each element has a **priority**, and elements are removed in order of **priority** rather than order of insertion.

### Concept (বাংলায়)
সাধারণ Queue-তে FIFO। Priority Queue-তে **যার priority বেশি, সে আগে যায়**।

**Real Example:** Hospital Emergency — heart attack-এর রোগী আগে আসা সর্দি-জ্বরের রোগীর আগেই চিকিৎসা পাবে।
**Software:** OS Priority Scheduling, **Dijkstra**, **Prim**, **Huffman Coding**।

### Key Points
1. Priority Queue একটি **ADT**, **Heap** তার implementation
2. Heap দিয়ে insert/delete **O(log n)**, peek **O(1)**
3. Min-Priority Queue → Min-Heap; Max-Priority Queue → Max-Heap

### Time Complexity Comparison ⭐

| Implementation | Insert | Delete Max | Find Max |
|---|---|---|---|
| Unsorted Array | O(1) | O(n) | O(n) |
| Sorted Array | O(n) | O(1) | O(1) |
| **Heap** | **O(log n)** | **O(log n)** | **O(1)** |

### 🔁 Admission Revision Box
Priority Queue = priority অনুযায়ী delete, arrival order নয়। **ADT** — **Heap** দিয়ে implement → Insert/Delete **O(log n)**, Peek **O(1)**। ব্যবহার: OS scheduling, Dijkstra, Prim, Huffman।

---

## Topic 2: Set

### Definition (English)
A **Set** is a collection of **distinct, unordered** elements — **no duplicates** allowed.

### Concept (বাংলায়)
Set-এ কোনো element **দুইবার** থাকতে পারে না, এবং নির্দিষ্ট order নেই।
**Real Example:** Website-এর **unique visitor** count — একই user বারবার এলেও একবারই গোনা হবে।

### Operations

| Operation | Symbol | অর্থ |
|---|---|---|
| Union | A ∪ B | দুই set-এর সব element |
| Intersection | A ∩ B | দুই set-এ common |
| Difference | A − B | A-তে আছে, B-তে নেই |
| Membership | x ∈ A | x আছে কিনা |

### Key Points
1. **No duplicates, no fixed order** — মূল দুই বৈশিষ্ট্য
2. **Hash Table** দিয়ে implement → membership check **O(1)** (Python `set`, Java `HashSet`)
3. Balanced BST দিয়ে (`TreeSet`) → sorted থাকে, O(log n)
4. **Disjoint Set (Union-Find)** — বিশেষ set structure, **Kruskal's MST**-এ ব্যবহৃত

### 🔁 Admission Revision Box
Set = **distinct + unordered**। Operations: **Union, Intersection, Difference, Membership**। HashSet → **O(1)** average; TreeSet → O(log n) sorted। **Disjoint Set (Union-Find) → Kruskal-এ ব্যবহৃত**।

---

## Topic 3: Dictionary (Map)

### Definition (English)
A **Dictionary (Map)** is an ADT that stores data as **key–value pairs**, where each **key is unique**.

### Concept (বাংলায়)
Array-তে index দিয়ে access (0,1,2…)। Dictionary-তে **যেকোনো key** দিয়ে — string, number, যা খুশি।
```python
student = {"id": 101, "name": "Rahim"}
student["name"]   # → "Rahim"
```
**Real Example:** Database record retrieval, Cache (Redis), Config file।

### Key Points
1. Key **unique**, value duplicate হতে পারে
2. Implementation: **Hash Table** (O(1) avg) বা **Balanced BST** (O(log n), sorted)
3. Python `dict`, Java `HashMap`/`TreeMap`, C++ `unordered_map`/`map`
4. Dictionary একটি **ADT** — Hash Table তার implementation

### Comparison ⭐

| Feature | **HashMap** (Hash Table) | **TreeMap** (Red-Black Tree) |
|---|---|---|
| Search/Insert | **O(1)** average | O(log n) |
| Order | নেই | **Sorted by key** |
| Worst case | **O(n)** | **O(log n)** |

### 🔁 Admission Revision Box
Dictionary/Map = **key–value pair**, key unique। ADT — Hash Table দিয়ে **O(1)** average, Balanced BST দিয়ে O(log n) + sorted। Python dict, Java HashMap/TreeMap।

---

## Topic 4: Compound Data Structures

### Definition (English)
A **Compound Data Structure** is formed by **combining two or more basic data structures** to solve a specific problem more efficiently.

### Common Examples ⭐

| Compound Structure | কী দিয়ে তৈরি | কোথায় ব্যবহৃত |
|---|---|---|
| **Adjacency List** | Array + Linked List | Graph representation |
| **Hash Table with Chaining** | Array + Linked List | Java HashMap |
| **Sparse Matrix** | Triplet Array / Linked List | বেশিরভাগ 0 থাকা matrix |
| **Multilist** | একাধিক Linked List | Student → Courses mapping |
| **Trie** | Tree + Array/Map | Autocomplete, Spell check |
| **LRU Cache** | HashMap + Doubly Linked List | Browser/CPU cache |

### 🔁 Admission Revision Box
Compound DS = দুই বা তার বেশি basic DS মিলিয়ে তৈরি। উদাহরণ: **Adjacency List** (Array+LL), **Hash Table with Chaining**, **Sparse Matrix**, **Trie**, **LRU Cache** (HashMap+DLL)।

---
---

# MODULE 10 — RECURSION (DS Perspective)

## Topic 1: Recursion

### Definition (English)
**Recursion** is a technique in which a function **calls itself** to solve smaller instances of the same problem until a **base case** is reached.

⭐ **Keywords:** Self-call · **Base Case** · Recursive Case · Call Stack

### Concept (বাংলায়)
দুইটা অংশ **অবশ্যই** থাকতে হবে:
1. **Base Case** — কোথায় থামবে (না থাকলে infinite recursion → **Stack Overflow**)
2. **Recursive Case** — নিজেকে ছোট input দিয়ে ডাকা

```
factorial(n):
    if n <= 1: return 1          # Base Case
    return n * factorial(n-1)    # Recursive Case
```

**factorial(4):**
```
factorial(4) → 4 × factorial(3)
               3 × factorial(2)
                   2 × factorial(1) → 1  ← Base Case
Return: 1 → 2 → 6 → 24
```

### Recursion ও Stack-এর সম্পর্ক ⭐
প্রতিটি recursive call **Call Stack**-এ জমা হয়। Base case-এ পৌঁছালে উল্টো দিক থেকে return হয় — এটাই **LIFO**।
➡️ **Recursion internally uses Stack.**

### Key Points
1. **Base case ছাড়া recursion = Stack Overflow** ⭐
2. Recursion **Stack** ব্যবহার করে → extra space **O(depth)**
3. যেকোনো recursion **iteration দিয়ে লেখা যায়** (Stack ব্যবহার করে) — উল্টোটাও সত্য
4. **Tail Recursion** = recursive call-ই শেষ statement → compiler optimize করতে পারে
5. Tree traversal, DFS, Divide & Conquer, Backtracking — সব recursion-ভিত্তিক

### Recursion vs Iteration ⭐

| Feature | **Recursion** | **Iteration** |
|---|---|---|
| Space | **O(n)** (call stack) | **O(1)** |
| Speed | ধীর (call overhead) | দ্রুত |
| Code | ছোট, পরিষ্কার | তুলনামূলক বড় |
| Risk | **Stack Overflow** | নেই |
| ভালো যেখানে | Tree, Graph, D&C | Simple loop |

### Common Recursion Complexities ⭐

| Problem | Recurrence | Complexity |
|---|---|---|
| Factorial | T(n) = T(n−1) + 1 | O(n) |
| **Fibonacci (naive)** | T(n) = T(n−1) + T(n−2) | **O(2ⁿ)** ⚠️ |
| Binary Search | T(n) = T(n/2) + 1 | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + n | O(n log n) |
| **Tower of Hanoi** | T(n) = 2T(n−1) + 1 | **O(2ⁿ)**, moves = **2ⁿ − 1** ⭐ |

### ⚠️ MCQ Traps
- Naive Fibonacci = **O(2ⁿ)**, O(n) নয় (DP দিয়ে O(n) করা যায়)
- Tower of Hanoi-তে n disk → minimum moves = **2ⁿ − 1**। n=3 → **7 moves**

### 🔁 Admission Revision Box
Recursion = function নিজেকে ডাকে। **Base Case + Recursive Case** — base case না থাকলে **Stack Overflow**। Internally **Stack** ব্যবহার করে, space O(depth)। **Naive Fibonacci = O(2ⁿ)**, **Tower of Hanoi moves = 2ⁿ − 1**। Recursion ↔ Iteration পরস্পর রূপান্তরযোগ্য।

---
---

# MODULE 11 — MEMORY MANAGEMENT

## Topic 1: Memory Management

### Definition (English)
**Memory Management** is the process of **allocating, using, and releasing** memory during program execution for efficient use of available memory.

⭐ **Keywords:** Allocation · Deallocation · Stack · Heap · Fragmentation

### Concept (বাংলায়)

**Stack Memory**
- Function call, local variable, parameter
- **Automatic** — function শেষ হলে নিজেই মুছে যায়
- ছোট, fixed, **খুব দ্রুত**
- ভরে গেলে → **Stack Overflow**

**Heap Memory**
- **Dynamic allocation** (`malloc`, `new`)
- Programmer বা Garbage Collector মুছে দেয়
- বড়, তুলনামূলক **ধীর**
- **Linked List, Tree, Graph-এর node** এখানে তৈরি হয়

### Static vs Dynamic Allocation ⭐

| Feature | **Static Allocation** | **Dynamic Allocation** |
|---|---|---|
| কখন | **Compile time** | **Run time** |
| কোথায় | **Stack** | **Heap** |
| Size | আগে থেকে ঠিক | চলার সময় ঠিক হয় |
| উদাহরণ | `int a[10];` | `malloc()`, `new` |
| **DS উদাহরণ** | **Array** | **Linked List, Tree, Graph** |

### Key Concepts

| Term | অর্থ |
|---|---|
| **Garbage Collection** | অব্যবহৃত memory automatically মুক্ত করা (Java, Python, C# — **C/C++-এ নেই**) |
| **Memory Leak** | Allocate করা memory কখনো free না করা |
| **Dangling Pointer** | Free করা memory-কে দেখানো pointer |
| **Internal Fragmentation** | Allocate করা block-এর **ভিতরে** খালি জায়গা নষ্ট |
| **External Fragmentation** | মোট খালি memory যথেষ্ট, কিন্তু **ছড়িয়ে-ছিটিয়ে** থাকায় বড় block দেওয়া যাচ্ছে না |
| **Compaction** | ছড়ানো খালি জায়গা একত্র করা |

### Allocation Functions (C)

| Function | কাজ |
|---|---|
| `malloc(size)` | নির্দিষ্ট byte allocate (initialize করে না) |
| `calloc(n, size)` | n টি block allocate + **0 দিয়ে initialize** |
| `realloc(ptr, size)` | আগের block-এর size পরিবর্তন |
| `free(ptr)` | Memory মুক্ত করা |

C++-এ: `new` / `delete`

### Key Points
1. **Array = Static (Stack)**, **Linked List = Dynamic (Heap)** ⭐ সবচেয়ে বেশি আসা তুলনা
2. Recursion গভীর হলে → **Stack Overflow**
3. Java/Python-এ **Garbage Collector** আছে, তাই memory leak কম
4. Linked List-এ প্রতিটি node-এর **pointer-এর extra memory** = এর overhead
5. `calloc` initialize করে, `malloc` করে না ⭐

### 🔁 Admission Revision Box
Memory = **Stack** (function call, local var, automatic, ছোট, দ্রুত) + **Heap** (dynamic, বড়, ধীর)। **Static = compile time = Array**, **Dynamic = run time = Linked List/Tree**। C: `malloc`/`calloc`/`realloc`/`free`; C++: `new`/`delete`; Java/Python: **Garbage Collection**। **Memory Leak** = free না করা; **Fragmentation** = Internal / External।

---
---

# ★ FINAL REVISION — শেষ ৩০ মিনিটে এটুকুই পড়ো

## 1. Complexity Master Table ⭐⭐⭐

| Data Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| **Array** | **O(1)** | O(n) | O(n) | O(n) | O(n) |
| **Sorted Array** | O(1) | **O(log n)** | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | **O(1)** * | **O(1)** * | O(n) |
| **Stack** | O(n) | O(n) | **O(1)** | **O(1)** | O(n) |
| **Queue** | O(n) | O(n) | **O(1)** | **O(1)** | O(n) |
| **BST (avg)** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **BST (worst)** | O(n) | **O(n)** | O(n) | O(n) | O(n) |
| **AVL / Red-Black** | O(log n) | **O(log n)** | O(log n) | O(log n) | O(n) |
| **Heap** | O(1) max/min | O(n) | O(log n) | O(log n) | O(n) |
| **Hash Table (avg)** | — | **O(1)** | **O(1)** | **O(1)** | O(n) |
| **Hash Table (worst)** | — | **O(n)** | O(n) | O(n) | O(n) |

\* Linked List: beginning-এ। End-এ tail pointer ছাড়া O(n)।

## 2. এক লাইনে প্রতিটি DS

| Structure | এক লাইনে |
|---|---|
| **Array** | Contiguous, fixed size, **Access O(1)**, Insert O(n) |
| **Linked List** | Node + pointer, dynamic, **Access O(n)**, Insert O(1) |
| **Stack** | **LIFO**, Push/Pop/Peek O(1), browser back, recursion, **DFS** |
| **Queue** | **FIFO**, Enqueue/Dequeue O(1), printer, scheduling, **BFS** |
| **Tree** | Non-linear, hierarchical, **n নোড → n−1 edge** |
| **Binary Tree** | ≤2 child, level i-তে max 2^i, height h-এ max 2^(h+1)−1 |
| **BST** | বামে ছোট ডানে বড়, **Inorder = sorted**, avg O(log n) |
| **AVL** | Self-balancing, BF ∈ {−1,0,1}, **O(log n) guaranteed** |
| **Heap** | Complete tree, parent≥child, **Build O(n)**, Peek O(1) |
| **Hash Table** | key→index, **O(1) avg / O(n) worst**, collision → chaining |
| **Graph** | G(V,E), **Matrix O(V²) / List O(V+E)** |

## 3. Structure Selection Cheat Sheet

| দরকার | সঠিক DS |
|---|---|
| দ্রুত index access | **Array** |
| ঘন ঘন insert/delete | **Linked List** |
| LIFO / undo / recursion | **Stack** |
| FIFO / scheduling | **Queue** |
| Key দিয়ে O(1) lookup | **Hash Table** |
| Sorted + fast search | **Balanced BST (AVL)** |
| বারবার max/min বের করা | **Heap** |
| Network / সম্পর্ক model | **Graph** |
| Duplicate বাদ দেওয়া | **Set** |
| Priority অনুযায়ী কাজ | **Priority Queue** |

## 4. আবশ্যিক Formula List

| Formula | কোথায় |
|---|---|
| `Address(A[i]) = Base + i × size` | Array |
| `Address(A[i][j]) = Base + [(i×cols)+j] × size` | 2D Array (Row-Major) |
| Tree-তে **edge = n − 1** | Tree |
| Level i-তে max node = **2^i** | Binary Tree |
| Height h-এ max node = **2^(h+1) − 1** | Binary Tree |
| Min height = **⌊log₂ n⌋** | Binary Tree |
| Leaf = **D₂ + 1** | Binary Tree |
| NULL pointer = **n + 1** | Binary Tree |
| Heap: left=**2i+1**, right=**2i+2**, parent=**(i−1)/2** | Heap (0-based) |
| Load Factor **α = n / m** | Hashing |
| Complete undirected edge = **n(n−1)/2** | Graph |
| Sum of degrees = **2E** | Graph |
| Tower of Hanoi moves = **2ⁿ − 1** | Recursion |

## 5. Top 20 MCQ Traps ⭐⭐⭐

1. **Stack ও Queue = Linear** (non-linear নয়)
2. **ADT ≠ Data Structure** — ADT specification, DS implementation
3. Array-তে **Access O(1)** কিন্তু **Search O(n)** — আলাদা জিনিস
4. **Linked List-এ Binary Search কার্যকর নয়** (random access নেই)
5. **Full + Push = Overflow**, **Empty + Pop = Underflow**
6. **Priority Queue FIFO মানে না**
7. **DFS = Stack, BFS = Queue** ✅
8. **Complete ≠ Full ≠ Perfect** binary tree
9. **BST-এর Inorder = ascending sorted** ✅
10. **BST search worst case O(n)**, always O(log n) নয়
11. **Preorder + Postorder দিয়ে unique tree হয় না**
12. **Heap ≠ BST** — heap-এ left/right order নেই
13. **Build Heap = O(n)**, O(n log n) নয়
14. **Hash Table search worst = O(n)**, always O(1) নয়
15. **Hash Table-এ sorted traversal সম্ভব নয়**
16. **Adjacency Matrix space O(V²)** — edge সংখ্যা নির্বিশেষে
17. **Tree-তে edge = n−1**; **Graph-এ এই নিয়ম খাটে না**
18. **Naive Fibonacci = O(2ⁿ)**; **Tower of Hanoi = 2ⁿ−1 moves**
19. **Array = static (compile time)**, **Linked List = dynamic (run time)**
20. **C/C++ = Row-Major**, **FORTRAN = Column-Major**

## 6. DS vs Algo — বিভ্রান্তি দূর

| এটি **Data Structure** (CSE 220) | এটি **Algorithm** (CSE 221) |
|---|---|
| Binary Search **Tree** | Binary **Search** |
| **Heap** | **Heap Sort** |
| **Hash Table** | Hashing function / probing |
| **Graph** (Matrix / List) | **BFS, DFS, Dijkstra, Prim** |
| **Stack, Queue** | **Recursion, Backtracking** |
| **Priority Queue** | **Dijkstra, Huffman** |
| **Array, Linked List** | **Sorting algorithms** |
