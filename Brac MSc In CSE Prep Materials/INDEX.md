# 📑 INDEX — BRAC MSc CSE Admission
### সম্পূর্ণ Topic তালিকা (Subject → Module → Topic)

> শুধু **কী কী পড়তে হবে** তার তালিকা। সময়ের ভাগ ও পরিকল্পনা আলাদা file-এ (`STUDY_PLAN.md`)।
> পড়া শেষ হলে ☐ box-এ টিক দাও।

---

## 🗂️ Subject List

| # | Subject | Course Code | Module | ফাইল |
|---|---|---|---|---|
| 1 | Networking | CSE 320 / 421 / 490 | 6 | — |
| 2 | Database Systems | CSE 370 | 6 | — |
| 3 | Programming & OOP | CSE 110 / 111 / 310 | 6 | — |
| 4 | Operating Systems | CSE 321 | 4 | — |
| 5 | Software Engineering | CSE 470 | 3 | — |
| 6 | Digital Logic & Number System | CSE 260 | 3 | — |
| 7 | Data Structures | CSE 220 | 11 | `CSE_220_Data_Structures.md` |
| 8 | Algorithms | CSE 221 | 6 | `CSE_221_Algorithms.md` |
| 9 | Algorithm Steps & Dry Run | CSE 220+221 | 11 | `Algorithm_Steps_and_DryRun.md` |
| 10 | Machine Learning & Deep Learning | CSE 425 / 427 | 6 | `ML_DL_Basics.md` |
| 11 | English Composition | — | 1 | — |
| 12 | Optional (Architecture, Automata, Discrete Math) | CSE 340 / 331 / 230 | 3 | — |

---
---

# 1️⃣ NETWORKING — CSE 320 / 421 / 490

### Module 1: OSI & TCP/IP Model
- ☐ OSI-এর ৭ layer — নাম ও ক্রম
- ☐ TCP/IP-এর ৪ layer — নাম ও ক্রম
- ☐ প্রতিটি layer-এর কাজ
- ☐ কোন layer-এ কোন device (Hub, Switch, Router)
- ☐ কোন layer-এ কোন protocol (HTTP, TCP, IP)
- ☐ PDU: Bit → Frame → Packet → Segment → Data
- ☐ OSI vs TCP/IP mapping

### Module 2: IP Addressing
- ☐ IPv4 = 32 bit, dotted decimal
- ☐ IPv6 = 128 bit, hexadecimal + example
- ☐ Class A / B / C / D / E — range ও default mask
- ☐ Private IP ranges
- ☐ Loopback address
- ☐ IPv4 vs IPv6 comparison

### Module 3: Subnetting, VLSM, CIDR
- ☐ Subnet mask
- ☐ CIDR notation (/24, /26) → mask রূপান্তর
- ☐ VLSM — সংজ্ঞা ও প্রয়োজন
- ☐ CIDR — সংজ্ঞা ও প্রয়োজন
- ☐ Host সংখ্যা = 2ⁿ − 2
- ☐ Subnet সংখ্যা = 2ᵐ
- ☐ একটা subnetting সমস্যা হাতে solve

### Module 4: Wireless & LAN Standards
- ☐ 802.11b / a / g / n / ac — frequency ও bandwidth
- ☐ IEEE 802.3 (Ethernet), 802.5 (Token Ring), 802.15 (Bluetooth)
- ☐ LAN / MAN / WAN
- ☐ Topology: Bus, Star, Ring, Mesh, Hybrid

### Module 5: Protocols & Devices
- ☐ TCP vs UDP
- ☐ Port numbers (80, 443, 21, 22, 23, 25, 53)
- ☐ DHCP, DNS, NAT, PAT
- ☐ Hub vs Switch vs Router vs Bridge vs Gateway
- ☐ Unicast / Broadcast / Multicast

### Module 6: Data Communication Basics
- ☐ Modulation
- ☐ Bandwidth vs Throughput vs Latency
- ☐ Multiplexing: FDM, TDM, WDM
- ☐ Error detection: Parity, Checksum, CRC
- ☐ Simplex / Half-duplex / Full-duplex
- ☐ Guided vs Unguided media

---

# 2️⃣ DATABASE SYSTEMS — CSE 370

### Module 1: DBMS Basics
- ☐ DBMS vs File System
- ☐ Schema, Instance, DDL/DML/DCL/TCL
- ☐ 3-level architecture
- ☐ Data independence (Physical / Logical)
- ☐ Database models

### Module 2: Relational Model & Keys
- ☐ Relation, Tuple, Attribute, Domain, Degree, Cardinality
- ☐ Primary Key
- ☐ Foreign Key
- ☐ Candidate / Super / Composite / Alternate Key
- ☐ Entity Integrity & Referential Integrity

### Module 3: SQL
- ☐ `CREATE DATABASE`
- ☐ `CREATE TABLE`
- ☐ `SELECT ... FROM ... WHERE`
- ☐ `INSERT` / `UPDATE` / `DELETE`
- ☐ `ORDER BY`, `GROUP BY`, `HAVING`, `DISTINCT`
- ☐ Aggregate: COUNT, SUM, AVG, MIN, MAX
- ☐ JOIN: INNER, LEFT, RIGHT, FULL
- ☐ `ALTER` / `DROP` vs `TRUNCATE` vs `DELETE`
- ☐ Constraints

### Module 4: Normalization
- ☐ Functional Dependency
- ☐ 1NF
- ☐ 2NF (partial dependency)
- ☐ 3NF (transitive dependency)
- ☐ BCNF
- ☐ Anomalies (Insert / Update / Delete)

### Module 5: ER Model
- ☐ Entity, Attribute, Relationship
- ☐ Cardinality (1:1, 1:M, M:N)
- ☐ Weak entity, Composite/Derived/Multivalued attribute
- ☐ ER → Table রূপান্তর

### Module 6: Transaction & Indexing
- ☐ ACID properties
- ☐ COMMIT, ROLLBACK, SAVEPOINT
- ☐ Indexing (B+ Tree)
- ☐ Clustered vs Non-clustered index

---

# 3️⃣ PROGRAMMING & OOP — CSE 110 / 111 / 310

### Module 1: C/C++ Basics
- ☐ Data types ও size
- ☐ Operator precedence
- ☐ `i++` vs `++i`
- ☐ Integer vs float division
- ☐ Modulus `%` (integer only)
- ☐ Type casting
- ☐ Pointer, call by value vs reference

### Module 2: math.h Functions
- ☐ `round()`
- ☐ `ceil()` / `floor()`
- ☐ `fmod()` — float remainder
- ☐ `pow()`, `sqrt()`, `abs()` / `fabs()`
- ☐ Java: `Math.round()`, `Math.ceil()`, `Math.floor()`

### Module 3: Control Flow & Loop Tracing
- ☐ `for` / `while` / `do-while`
- ☐ Short-circuit evaluation (`&&`, `||`)
- ☐ Loop-এর ভিতরে increment কখন চলে
- ☐ `break` vs `continue`
- ☐ Loop output trace practice

### Module 4: OOP Concepts
- ☐ Encapsulation, Inheritance, Polymorphism, Abstraction
- ☐ Class vs Object
- ☐ Constructor (default / parameterized / copy)
- ☐ Overloading vs Overriding
- ☐ Abstract class vs Interface
- ☐ Access modifiers
- ☐ `static`, `final`, `this`, `super`
- ☐ Inheritance types (Java-তে multiple নেই)

### Module 5: Platform Independence
- ☐ Source → Compiler → Bytecode → JVM → Machine code
- ☐ "Write Once, Run Anywhere"
- ☐ Bytecode independent, JVM dependent
- ☐ JDK vs JRE vs JVM
- ☐ Java vs C/C++ compilation

### Module 6: Exception & Basics
- ☐ try-catch-finally, throw vs throws
- ☐ Checked vs Unchecked exception
- ☐ String vs StringBuffer vs StringBuilder
- ☐ `==` vs `.equals()`

---

# 4️⃣ OPERATING SYSTEMS — CSE 321

### Module 1: Process & Thread
- ☐ Process সংজ্ঞা
- ☐ Thread সংজ্ঞা
- ☐ Multithreading
- ☐ Process vs Thread comparison
- ☐ Thread-এর সুবিধা
- ☐ Process states
- ☐ PCB, Context Switching

### Module 2: CPU Scheduling
- ☐ FCFS
- ☐ SJF
- ☐ Priority Scheduling
- ☐ Round Robin
- ☐ Preemptive vs Non-preemptive
- ☐ Turnaround / Waiting / Response time

### Module 3: Deadlock
- ☐ ৪ শর্ত (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait)
- ☐ Prevention / Avoidance / Detection / Recovery
- ☐ Banker's Algorithm
- ☐ Starvation vs Deadlock

### Module 4: Memory & Synchronization
- ☐ Paging vs Segmentation
- ☐ Virtual Memory, Page Fault, Thrashing
- ☐ Page replacement: FIFO, LRU, Optimal
- ☐ Internal vs External Fragmentation
- ☐ Semaphore, Mutex, Critical Section, Race Condition

---

# 5️⃣ SOFTWARE ENGINEERING — CSE 470

### Module 1: SDLC
- ☐ SDLC পূর্ণরূপ
- ☐ ৬ ধাপ (Requirement → Design → Implementation → Testing → Deployment → Maintenance)
- ☐ প্রতিটি ধাপের কাজ

### Module 2: SDLC Models
- ☐ Waterfall
- ☐ Iterative / Incremental
- ☐ Spiral
- ☐ Agile / Scrum
- ☐ V-Model
- ☐ Waterfall vs Agile

### Module 3: Testing & Design Principles
- ☐ Black Box vs White Box
- ☐ Unit → Integration → System → Acceptance
- ☐ Verification vs Validation
- ☐ Functional vs Non-functional requirement
- ☐ Cohesion vs Coupling

---

# 6️⃣ DIGITAL LOGIC & NUMBER SYSTEM — CSE 260

### Module 1: Number System
- ☐ Binary ↔ Decimal (ভগ্নাংশ সহ)
- ☐ Binary ↔ Octal ↔ Hexadecimal
- ☐ 1's complement, 2's complement
- ☐ Binary arithmetic
- ☐ BCD, Gray code, ASCII

### Module 2: Boolean Algebra & Gates
- ☐ AND, OR, NOT, NAND, NOR, XOR, XNOR — truth table
- ☐ NAND / NOR = Universal gate
- ☐ De Morgan's Theorem
- ☐ Boolean simplification, K-map
- ☐ SOP vs POS

### Module 3: Combinational & Sequential
- ☐ Half Adder, Full Adder
- ☐ Mux, Demux, Encoder, Decoder
- ☐ Flip-flops (SR, JK, D, T)
- ☐ Counter, Register, Shift Register
- ☐ Combinational vs Sequential

---

# 7️⃣ DATA STRUCTURES — CSE 220
`File: CSE_220_Data_Structures.md`

### Module 1: Introduction
- ☐ Data Structure
- ☐ Data Objects
- ☐ Classification (Primitive/Non-Primitive, Linear/Non-Linear)
- ☐ Data Abstraction & ADT
- ☐ Primitive Operations
- ☐ Performance & Complexity

### Module 2: Array
- ☐ Array
- ☐ Array Operations
- ☐ Types of Arrays (1D, 2D, Multidimensional)

### Module 3: Linked List
- ☐ Linked List
- ☐ Types (Singly, Doubly, Circular)
- ☐ Operations & Array vs Linked List

### Module 4: Stack
- ☐ Stack (LIFO, Push/Pop, Overflow/Underflow)
- ☐ Applications (Function call, Recursion, Undo, Infix→Postfix, Bracket matching)

### Module 5: Queue
- ☐ Queue (FIFO, Enqueue/Dequeue)
- ☐ Types (Simple, Circular, Priority, Deque)

### Module 6: Tree
- ☐ Tree & Terminology
- ☐ Binary Tree & Types
- ☐ Tree Traversal (Pre/In/Post/Level)
- ☐ Binary Search Tree
- ☐ AVL & Balanced Trees
- ☐ Heap

### Module 7: Hashing
- ☐ Hash Table & Hash Function
- ☐ Collision & Resolution (Chaining, Probing)

### Module 8: Graph
- ☐ Graph & Terminology
- ☐ Representation (Matrix vs List)

### Module 9: Other Data Structures
- ☐ Priority Queue
- ☐ Set
- ☐ Dictionary (Map)
- ☐ Compound Structures

### Module 10: Recursion
- ☐ Recursion (Base case, Call stack, vs Iteration)

### Module 11: Memory Management
- ☐ Stack vs Heap, Static vs Dynamic, Fragmentation

---

# 8️⃣ ALGORITHMS — CSE 221
`File: CSE_221_Algorithms.md`

### Module 1: Algorithm Analysis
- ☐ Algorithm & ৫ বৈশিষ্ট্য
- ☐ Asymptotic Notation (O, Ω, Θ)
- ☐ Order of Growth
- ☐ Recurrence & Master Theorem

### Module 2: Design Techniques
- ☐ Divide & Conquer
- ☐ Greedy Algorithm
- ☐ Dynamic Programming
- ☐ Backtracking

### Module 3: Sorting
- ☐ Bubble, Selection, Insertion
- ☐ Merge, Quick, Heap
- ☐ Counting, Radix
- ☐ Stable vs In-place
- ☐ Sorting Master Table

### Module 4: Searching
- ☐ Linear Search
- ☐ Binary Search

### Module 5: Graph Algorithms
- ☐ BFS
- ☐ DFS
- ☐ Dijkstra
- ☐ Bellman-Ford
- ☐ Floyd-Warshall
- ☐ Prim's & Kruskal's (MST)
- ☐ Topological Sort
- ☐ Network Flow (সংক্ষেপে)

### Module 6: Advanced
- ☐ Amortized Analysis
- ☐ P, NP, NP-Hard, NP-Complete
- ☐ GCD, Primality, Sieve
- ☐ Strassen, Horner's Rule

---

# 9️⃣ ALGORITHM STEPS & DRY RUN
`File: Algorithm_Steps_and_DryRun.md`

- ☐ A. Searching (Linear, Binary)
- ☐ B. Sorting (7টি)
- ☐ C. Stack/Queue (Push/Pop, Infix→Postfix, Bracket)
- ☐ D. Linked List (Insert, Delete, Reverse)
- ☐ E. Tree (Traversal, BST Search/Insert/Delete)
- ☐ F. Heap (Insert, Delete, Build Heap)
- ☐ G. Hashing (Chaining, Linear Probing)
- ☐ H. Graph (BFS, DFS, Dijkstra, Bellman-Ford, Floyd, Prim, Kruskal, Topological)
- ☐ I. DP/Greedy (Fibonacci, Knapsack, LCS, Activity Selection, Huffman)
- ☐ J. Backtracking (N-Queens)
- ☐ K. Number (GCD, Sieve, Primality)

---

# 🔟 MACHINE LEARNING & DEEP LEARNING
`File: ML_DL_Basics.md`

### Module 1: AI, ML, DL
- ☐ AI ⊃ ML ⊃ DL সম্পর্ক
- ☐ ML vs DL comparison

### Module 2: Types of ML
- ☐ Supervised (Classification vs Regression)
- ☐ Unsupervised (Clustering, Dimensionality Reduction)
- ☐ Semi-supervised
- ☐ Reinforcement Learning

### Module 3: Common Algorithms
- ☐ Linear & Logistic Regression
- ☐ KNN, Decision Tree, Random Forest
- ☐ SVM, Naive Bayes
- ☐ K-Means, PCA

### Module 4: Training & Evaluation
- ☐ Train / Validation / Test split, Cross-validation
- ☐ Overfitting vs Underfitting, Bias-Variance
- ☐ Regularization (L1, L2)
- ☐ Confusion Matrix, Precision, Recall, F1
- ☐ Regression metrics (MSE, RMSE, MAE, R²)

### Module 5: Deep Learning Basics
- ☐ Neural Network structure (weight, bias)
- ☐ Activation Functions (Sigmoid, ReLU, Tanh, Softmax)
- ☐ Forward Propagation → Loss → Backpropagation → Gradient Descent
- ☐ Epoch, Batch, Iteration, Learning Rate
- ☐ Vanishing Gradient, Dropout

### Module 6: Architectures
- ☐ CNN, RNN, LSTM
- ☐ Transformer, GAN, Autoencoder

---

# 1️⃣1️⃣ ENGLISH COMPOSITION

- ☐ ২০০ শব্দের সীমা মেনে লেখার অভ্যাস
- ☐ Structure: Introduction → Body → Conclusion
- ☐ Linking words
- ☐ একটা practice essay (১৫ মিনিটে)
- ☐ সম্ভাব্য টপিক ভেবে রাখা (AI, Social media, Online education, Climate change)

---

# 1️⃣2️⃣ OPTIONAL — সময় থাকলে

### Computer Architecture (CSE 340)
- ☐ RISC vs CISC
- ☐ Cache memory, Cache hit/miss
- ☐ Pipeline

### Automata & Compiler (CSE 331 / 420)
- ☐ Finite Automata (DFA/NFA)
- ☐ Turing Machine
- ☐ Halting Problem
- ☐ Compiler vs Interpreter
- ☐ Compiler phases (Lexical → Syntax → Semantic → Code gen)

### Discrete Mathematics (CSE 230)
- ☐ Set theory basics
- ☐ Propositional logic
- ☐ Graph theory basics
- ☐ Permutation & Combination

---
---

# ✅ Progress Summary

| # | Subject | Module | শেষ |
|---|---|---|---|
| 1 | Networking | 6 | ☐ |
| 2 | Database | 6 | ☐ |
| 3 | Programming & OOP | 6 | ☐ |
| 4 | Operating Systems | 4 | ☐ |
| 5 | Software Engineering | 3 | ☐ |
| 6 | Digital Logic | 3 | ☐ |
| 7 | Data Structures | 11 | ☐ |
| 8 | Algorithms | 6 | ☐ |
| 9 | Algorithm Steps | 11 | ☐ |
| 10 | ML & DL | 6 | ☐ |
| 11 | English | 1 | ☐ |
| 12 | Optional | 3 | ☐ |
| | **মোট** | **66 module** | |
