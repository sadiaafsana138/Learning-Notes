# CSE 220 + CSE 221 — SHORT MASTER VIVA NOTES
## Data Structures + Algorithms
### প্রতিটি syllabus topic: 1–5 lines | English Answer + বাংলা ব্যাখ্যা

---

# CSE 220 — DATA STRUCTURES

## 1. Data Organisation
**English:** Data organisation means arranging data in a systematic form so that it can be stored, accessed, and processed efficiently.  
**বাংলা:** Data-কে এমনভাবে সাজানো হয় যাতে প্রয়োজন অনুযায়ী দ্রুত access ও process করা যায়।

## 2. Data Structure
**English:** A data structure is a way of organizing and storing data so that operations can be performed efficiently.  
**বাংলা:** Data structure data-কে organize করে এবং search, insertion, deletion ইত্যাদি operation efficient করতে সাহায্য করে।

## 3. Algorithm
**English:** An algorithm is a finite, well-defined sequence of steps for solving a problem.  
**বাংলা:** কোনো problem solve করার জন্য নির্দিষ্ট ও finite step-এর sequence হলো algorithm।

## 4. Performance of Algorithms
**English:** Algorithm performance is mainly evaluated using time and space requirements.  
**বাংলা:** Algorithm কত সময় ও memory ব্যবহার করে তা performance analysis-এর মূল বিষয়।

## 5. Elementary Data Objects
**English:** Elementary data objects are basic units of data used to build more complex structures.  
**বাংলা:** Basic data elements থেকে পরে complex data structure তৈরি করা যায়।

## 6. Elementary Data Structures
**English:** Basic structures include arrays, lists, stacks, queues, trees, and graphs.  
**বাংলা:** এগুলো data store ও process করার fundamental structures।

## 7. Arrays
**English:** An array stores elements in an indexed structure; typical array access by index is O(1).  
**বাংলা:** Index ব্যবহার করে সরাসরি element access করা যায়, তাই access সাধারণত O(1)।

## 8. Lists
**English:** A list stores an ordered collection of elements; linked lists represent elements using connected nodes.  
**বাংলা:** List-এ ordered data থাকে; linked list-এ node ও link/reference দিয়ে data রাখা হয়।

## 9. Stacks
**English:** A stack is a LIFO structure where insertion and deletion occur at the top. Push and pop are typically O(1).  
**বাংলা:** সর্বশেষে ঢোকা element আগে বের হয়। Push ও Pop top থেকে হয়।

## 10. Queues
**English:** A queue follows FIFO: the first inserted element is removed first. Enqueue occurs at the rear and dequeue at the front.  
**বাংলা:** আগে ঢোকা element আগে বের হয়। Scheduling ও BFS-এ queue ব্যবহৃত হয়।

## 11. Graphs
**English:** A graph consists of vertices and edges representing relationships between entities.  
**বাংলা:** Vertex হলো entity এবং edge হলো তাদের connection/relationship।

## 12. Trees
**English:** A tree is a hierarchical non-linear structure made of nodes and edges, normally with a root.  
**বাংলা:** Tree hierarchy represent করে; root থেকে parent-child relationship তৈরি হয়।

## 13. Compound Structures
**English:** Compound data structures combine simpler data elements or structures to represent more complex relationships.  
**বাংলা:** একাধিক basic structure/data element combine করে complex structure তৈরি করা হয়।

## 14. Data Abstraction
**English:** Data abstraction exposes essential operations while hiding implementation details.  
**বাংলা:** কী কাজ করা যাবে তা দেখানো হয়, কিন্তু ভিতরে কীভাবে কাজটি হচ্ছে তা hide করা হয়।

## 15. Primitive Operations
**English:** Primitive operations are basic operations such as access, insertion, deletion, search, and update.  
**বাংলা:** Data structure-এর basic কাজগুলো primitive operation হিসেবে ধরা হয়।

## 16. Memory Management
**English:** Memory management deals with allocating, using, and releasing/reclaiming memory during program execution.  
**বাংলা:** Program-এর প্রয়োজন অনুযায়ী memory নেওয়া ও আর প্রয়োজন না হলে release/reclaim করা memory management-এর অংশ।

## 17. Sorting
**English:** Sorting arranges data according to a specified order, such as ascending or descending order.  
**বাংলা:** Data-কে নির্দিষ্ট order-এ সাজানোই sorting।

**Key:** Merge Sort = O(n log n), Quick Sort = O(n log n) average / O(n²) worst.

## 18. Searching
**English:** Searching finds whether a target exists and/or determines its location. Linear search is O(n), while binary search is O(log n) on an appropriate ordered search space.  
**বাংলা:** Data-এর মধ্যে নির্দিষ্ট item খোঁজা হলো searching।

## 19. Hash Techniques
**English:** Hashing maps keys to table positions using a hash function for fast expected access. Collisions can be handled by chaining or open addressing.  
**বাংলা:** Key থেকে hash function index তৈরি করে। দুই key একই position পেলে collision হয়।

## 20. Recursion
**English:** Recursion is a technique where a function solves a problem by calling itself on a smaller instance. A base case is required to stop recursion.  
**বাংলা:** Function নিজেকেই smaller problem-এর জন্য call করে। Base case recursion থামায়।

## 21. Backtrack Search
**English:** Backtracking explores choices incrementally and returns to an earlier state when a partial solution cannot work.  
**বাংলা:** ভুল/invalid path হলে previous state-এ ফিরে অন্য choice try করা হয়।

## 22. Lists — Fundamental Operations
**English:** Common list operations include traversal, search, insertion, deletion, and update.  
**বাংলা:** List-এর মূল কাজ হলো data দেখা, খোঁজা, যোগ, বাদ ও পরিবর্তন করা।

## 23. Stacks — Fundamental Operations
**English:** The main stack operations are push, pop, and peek/top.  
**বাংলা:** Push element ঢোকায়, Pop element বের করে, Peek top element দেখে।

## 24. Queues — Fundamental Operations
**English:** The main queue operations are enqueue, dequeue, and front/peek.  
**বাংলা:** Enqueue পিছনে element যোগ করে, Dequeue সামনে থেকে element বের করে।

## 25. Trees — Fundamental Operations
**English:** Common tree operations include traversal, searching, insertion, and deletion depending on the tree type.  
**বাংলা:** Tree-এর type অনুযায়ী search, insert, delete ও traversal করা হয়।

## 26. Operations on Sets
**English:** Common set operations include membership, insertion, deletion, union, intersection, and difference.  
**বাংলা:** Set-এ element আছে কি না দেখা, যোগ/বাদ এবং union/intersection/difference করা যায়।

## 27. Priority Queues
**English:** A priority queue removes elements according to priority rather than simple arrival order; heaps are common implementations.  
**বাংলা:** এখানে আগে আসা নয়, priority অনুযায়ী element বের হয়।

## 28. Graph Dictionary
**English:** A dictionary/map can represent a graph by mapping each vertex to its neighboring vertices or related information.  
**বাংলা:** Vertex-কে key এবং তার neighbor-দের value/list হিসেবে রাখা যায়।

## 29. Analysis of Algorithms
**English:** Algorithm analysis studies correctness and resource usage, especially time and space complexity.  
**বাংলা:** Algorithm কত দ্রুত ও কত memory ব্যবহার করে তা analyze করা হয়।

## 30. Basic Structures and Their Performance
**English:** Different structures have different operation costs, so the structure should match the dominant operations of the problem.  
**বাংলা:** কোন operation বেশি হবে তার ওপর data structure নির্বাচন করলে performance ভালো হয়।

## 31. Database Systems — Brief Connection
**English:** Database systems use organized data structures and indexes to support efficient storage, searching, and retrieval.  
**বাংলা:** Database-এ data structure ও index ব্যবহার করে search/retrieval দ্রুত করা হয়।

## 32. Data Structures in Database Performance
**English:** Choosing suitable structures and indexes can reduce the cost of database operations such as lookup and retrieval.  
**বাংলা:** সঠিক structure/index query-এর সময় ও data access cost কমাতে পারে।

---

# CSE 221 — ALGORITHMS

## 33. Efficient Algorithms
**English:** An efficient algorithm solves a problem correctly using acceptable time and memory resources.  
**বাংলা:** শুধু correct output নয়, কম time ও memory ব্যবহার করাও efficient algorithm-এর লক্ষ্য।

## 34. Algorithm Design Techniques
**English:** Algorithm design techniques are systematic approaches such as divide and conquer, greedy, dynamic programming, and backtracking.  
**বাংলা:** Problem-এর ধরন অনুযায়ী এসব design paradigm ব্যবহার করে efficient solution তৈরি করা হয়।

## 35. Analysis of Algorithms
**English:** Analysis estimates the resources required by an algorithm as input size grows.  
**বাংলা:** Input size বাড়লে algorithm-এর time/space কীভাবে বাড়ে তা analyze করা হয়।

## 36. Divide and Conquer
**English:** Divide and Conquer divides a problem into smaller subproblems, solves them, and combines their results.  
**বাংলা:** Problem ভাগ → subproblem solve → result combine করা হয়।

**Example:** Merge Sort, Binary Search.

## 37. Greedy Method
**English:** A greedy algorithm repeatedly chooses a locally best feasible option. It is optimal only when the problem has the required greedy-choice property.  
**বাংলা:** প্রতিটি step-এ local best choice নেওয়া হয়; সব problem-এ greedy optimal হয় না।

## 38. Dynamic Programming
**English:** Dynamic programming stores solutions to overlapping subproblems and reuses them. It commonly relies on optimal substructure.  
**বাংলা:** একই subproblem বারবার solve না করে result store করে reuse করা হয়।

**Types:** Memoization = top-down; Tabulation = bottom-up.

## 39. Backtracking
**English:** Backtracking builds a candidate solution and abandons it when it cannot lead to a valid solution.  
**বাংলা:** Invalid path হলে backtrack করে অন্য possibility try করা হয়।

**Examples:** N-Queens, Sudoku.

## 40. Basic Search Techniques
**English:** Basic searching includes linear search and binary search.  
**বাংলা:** Linear search একে একে দেখে; binary search ordered data-তে search space অর্ধেক করে।

## 41. Basic Traversal Techniques
**English:** Traversal systematically visits elements or graph vertices; common methods include BFS and DFS.  
**বাংলা:** Structure-এর elements/vertices systematicভাবে visit করাকে traversal বলে।

## 42. Graph Algorithms
**English:** Graph algorithms solve problems involving vertices and edges, including traversal, shortest paths, spanning trees, and flow.  
**বাংলা:** Graph-এর connection ব্যবহার করে বিভিন্ন search, path, spanning tree ও flow problem solve করা হয়।

## 43. Elementary Parallel Algorithms
**English:** Parallel algorithms divide work among multiple processing resources so independent computations can occur simultaneously.  
**বাংলা:** একাধিক processor/resource দিয়ে একই সময়ে independent কাজ করা হয়।

## 44. Algebraic Simplification
**English:** Algebraic simplification reduces an equivalent mathematical expression to a simpler form that may require less computation.  
**বাংলা:** একই result রেখে expression সহজ করা হয় যাতে computation কমতে পারে।

## 45. Algebraic Transformations
**English:** Algebraic transformation changes a mathematical representation while preserving the required result or relationship.  
**বাংলা:** Mathematical form পরিবর্তন করা হয় কিন্তু প্রয়োজনীয় result/relationship বজায় থাকে।

## 46. Lower Bound Theory
**English:** A lower bound gives a fundamental minimum asymptotic cost required for solving a problem under a specified computational model.  
**বাংলা:** কোনো problem solve করতে অন্তত কতটা computational work লাগবেই তা lower bound বোঝায়।

**Example:** Comparison sorting has Ω(n log n) lower bound.

## 47. NP
**English:** NP contains decision problems whose proposed solutions can be verified in polynomial time.  
**বাংলা:** Candidate solution পাওয়া গেলে polynomial time-এ verify করা যায় এমন decision problems-এর class হলো NP।

## 48. NP-Hard
**English:** An NP-Hard problem is at least as hard as every problem in NP under an appropriate polynomial-time reduction; it need not itself be in NP.  
**বাংলা:** NP-এর সব problem-এর মতো কঠিন বা তার চেয়েও কঠিন হতে পারে; NP-এর member হওয়া বাধ্যতামূলক নয়।

## 49. NP-Complete
**English:** A problem is NP-Complete if it is both in NP and NP-Hard.  
**বাংলা:** NP-এর মধ্যে আছে এবং NP-Hard—দুই condition একসাথে হলে NP-Complete।

## 50. Sorting
**English:** Sorting arranges elements into a specified order and is a major algorithmic problem used as a building block for other tasks.  
**বাংলা:** Data order করলে search ও processing অনেক ক্ষেত্রে সহজ হয়।

## 51. Set Data Structures
**English:** Set structures store distinct elements and support operations such as membership, insertion, deletion, and set operations.  
**বাংলা:** Set-এ সাধারণত duplicate element থাকে না এবং membership/union/intersection ইত্যাদি করা হয়।

## 52. Heaps
**English:** A heap is a complete binary tree satisfying heap order. A min-heap has the smallest key at the root; a max-heap has the largest.  
**বাংলা:** Heap-এ parent-child-এর নির্দিষ্ট ordering থাকে; priority queue-তে খুব common।

**Complexity:** Insert/Extract = O(log n), Peek = O(1), Build Heap = O(n).

## 53. Hashing
**English:** Hashing maps keys to table locations using a hash function, giving O(1) expected lookup under suitable assumptions.  
**বাংলা:** Hash function key থেকে table location দেয়। Collision হলে resolution technique লাগে।

## 54. Shortest Paths
**English:** Shortest-path algorithms find minimum-cost paths between vertices. BFS handles unweighted graphs; Dijkstra handles non-negative weights.  
**বাংলা:** এক vertex থেকে অন্য vertex-এ minimum cost/distance path খোঁজা হয়।

## 55. Depth-First Search (DFS)
**English:** DFS explores as deeply as possible before backtracking, using recursion or an explicit stack.  
**বাংলা:** একটি path ধরে যত গভীরে সম্ভব যায়, তারপর backtrack করে।

**Complexity:** O(V+E) with adjacency lists.

## 56. Network Flow
**English:** Network flow models movement through a directed capacitated network from a source to a sink.  
**বাংলা:** Source থেকে sink-এর দিকে capacity সীমার মধ্যে flow পাঠানোর problem।

## 57. Maximum Flow
**English:** Maximum flow finds the greatest feasible amount of flow from a source to a sink subject to capacity constraints.  
**বাংলা:** Capacity ভেঙে না গিয়ে source থেকে sink-এ maximum কত flow পাঠানো যায় তা বের করা হয়।

## 58. Min-Cut / Max-Flow Min-Cut
**English:** The max-flow min-cut theorem states that the value of a maximum flow equals the capacity of a minimum s-t cut.  
**বাংলা:** Maximum flow-এর value এবং minimum cut-এর capacity সমান।

## 59. Computational Geometry
**English:** Computational geometry designs algorithms for geometric objects such as points, lines, polygons, and regions.  
**বাংলা:** Geometric object নিয়ে algorithmic problem solve করার ক্ষেত্র।

## 60. Integer Arithmetic
**English:** Integer arithmetic algorithms perform efficient operations on integers, including arithmetic and number-theoretic computations.  
**বাংলা:** Integer-এর ওপর efficient calculation ও number-theoretic operation নিয়ে কাজ করে।

## 61. GCD
**English:** The greatest common divisor is the largest positive integer dividing both numbers. Euclid's algorithm repeatedly uses gcd(a,b)=gcd(b,a mod b).  
**বাংলা:** দুই সংখ্যাকে নিঃশেষে ভাগ করতে পারে এমন সবচেয়ে বড় positive integer হলো GCD।

**Euclidean Algorithm:** O(log min(a,b)) arithmetic steps in the standard model.

## 62. Primality
**English:** A primality test determines whether an integer greater than 1 is prime, meaning it has exactly two positive divisors: 1 and itself.  
**বাংলা:** Prime number-এর divisor শুধু 1 এবং সংখ্যাটি নিজে।

## 63. Polynomial Calculations
**English:** Polynomial algorithms perform operations such as evaluation, addition, multiplication, or transformation on polynomial expressions.  
**বাংলা:** Polynomial-এর value বের করা, যোগ, গুণ বা representation পরিবর্তন করা এর মধ্যে পড়ে।

## 64. Matrix Calculations
**English:** Matrix algorithms perform operations such as addition, multiplication, and other transformations on matrices.  
**বাংলা:** Matrix-এর addition, multiplication ও বিভিন্ন transformation algorithmically করা হয়।

## 65. Amortized Analysis
**English:** Amortized analysis determines the average cost per operation over a sequence without assuming a probability distribution.  
**বাংলা:** পুরো sequence-এর total cost নিয়ে প্রতি operation-এর average cost বের করা হয়; probability assumption লাগে না।

**Methods:** Aggregate, Accounting, Potential.

## 66. Performance Bounds
**English:** Performance bounds describe how much computational resource an algorithm may require, using upper, lower, or tight bounds.  
**বাংলা:** Algorithm-এর resource usage-এর limit O, Ω, Θ দিয়ে প্রকাশ করা হয়।

## 67. Asymptotic Analysis
**English:** Asymptotic analysis studies algorithm growth as input size approaches large values, ignoring constant factors and lower-order terms.  
**বাংলা:** Input অনেক বড় হলে algorithm-এর growth rate কী হয় তা দেখা হয়।

## 68. Big-O
**English:** Big-O gives an asymptotic upper bound on growth.  
**বাংলা:** Algorithm-এর growth সর্বোচ্চ কোন order-এর মধ্যে থাকে তা বোঝাতে Big-O ব্যবহার হয়।

## 69. Big-Omega
**English:** Big-Ω gives an asymptotic lower bound on growth.  
**বাংলা:** Algorithm-এর growth অন্তত কোন order-এর হবে তা বোঝায়।

## 70. Big-Theta
**English:** Big-Θ gives a tight asymptotic bound, meaning matching upper and lower growth orders.  
**বাংলা:** Exact asymptotic order বোঝাতে Θ ব্যবহার করা হয়।

## 71. Worst-Case Behaviour
**English:** Worst-case complexity measures the maximum cost among inputs of a given size.  
**বাংলা:** একই size-এর input-এর মধ্যে সবচেয়ে বেশি time/space লাগা case।

## 72. Average-Case Behaviour
**English:** Average-case analysis gives expected cost under a specified input distribution or model.  
**বাংলা:** Input distribution/model ধরে expected performance বের করা হয়।

## 73. Best-Case Behaviour
**English:** Best-case complexity measures the minimum cost among inputs of a given size.  
**বাংলা:** একই size-এর input-এর মধ্যে সবচেয়ে কম cost-এর case।

## 74. Correctness
**English:** An algorithm is correct if it produces the required output for every valid input according to its specification.  
**বাংলা:** সব valid input-এর জন্য expected/correct result দিতে পারলেই algorithm correct।

## 75. Complexity
**English:** Complexity measures the resources required by an algorithm, mainly time and space, as a function of input size.  
**বাংলা:** Input size বাড়লে time ও memory requirement কীভাবে বাড়ে সেটাই complexity।

## 76. Recurrence Relations
**English:** A recurrence expresses the cost of a recursive algorithm in terms of costs for smaller input sizes.  
**বাংলা:** Recursive algorithm-এর T(n) কে smaller T(...) দিয়ে প্রকাশ করা হয়।

## 77. Sorting Algorithms — Key Comparison
**English:** Bubble, Selection, and Insertion are generally O(n²); Merge and Heap are O(n log n), while Quick Sort is O(n log n) average and O(n²) worst.  
**বাংলা:** Exam-এর জন্য এই complexity comparison অবশ্যই মুখস্থ রাখতে হবে।

## 78. Searching Algorithms — Key Comparison
**English:** Linear Search is O(n), while Binary Search is O(log n) when the search space is appropriately ordered.  
**বাংলা:** Binary search-এর মূল advantage হলো প্রতিবার search space প্রায় অর্ধেক করা।

---

# IMPORTANT COMPLEXITY TABLE

| Topic | Complexity |
|---|---|
| Array access | O(1) |
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Queue Enqueue | O(1) with suitable implementation |
| Queue Dequeue | O(1) with suitable implementation |
| Linked List Search | O(n) |
| BST Search | O(log n) if balanced-like; O(n) worst |
| Heap Insert | O(log n) |
| Heap Extract | O(log n) |
| Heap Peek | O(1) |
| Build Heap | O(n) |
| Hash Lookup | O(1) expected; O(n) worst |
| Bubble Sort | O(n²) average/worst |
| Selection Sort | O(n²) |
| Insertion Sort | O(n²) average/worst; O(n) best |
| Merge Sort | O(n log n) |
| Quick Sort | O(n log n) average; O(n²) worst |
| Heap Sort | O(n log n) |
| BFS | O(V+E) with adjacency list |
| DFS | O(V+E) with adjacency list |
| Bellman-Ford | O(VE) |
| Floyd-Warshall | O(V³) |

---

# MUST-KNOW DIFFERENCES

## Stack vs Queue
**Stack:** LIFO.  
**Queue:** FIFO.  
**বাংলা:** Stack-এ last-in first-out, Queue-তে first-in first-out।

## BFS vs DFS
**BFS:** Queue + level-wise.  
**DFS:** Stack/recursion + depth-wise.  
**বাংলা:** BFS কাছের node আগে দেখে; DFS গভীরে যায়।

## BST vs Heap
**BST:** Search ordering; inorder gives sorted order.  
**Heap:** Parent-child priority ordering; root gives min/max.  
**বাংলা:** Heap পুরো sorted নয়।

## Greedy vs DP
**Greedy:** Local best choice.  
**DP:** Stores/reuses overlapping subproblems.  
**বাংলা:** Greedy choice-based; DP subproblem-result reuse করে।

## Divide & Conquer vs DP
**D&C:** Divide into mostly independent subproblems and combine.  
**DP:** Overlapping subproblems-এর result store/reuse করে।  
**বাংলা:** Merge Sort = D&C; LCS/Knapsack = DP।

## Kruskal vs Prim
**Kruskal:** Sort edges and add safe minimum edges.  
**Prim:** Grow one tree by repeatedly choosing the minimum outgoing edge.  
**বাংলা:** Kruskal edge-based; Prim tree-growing।

## Dijkstra vs Bellman-Ford
**Dijkstra:** Requires non-negative edge weights.  
**Bellman-Ford:** Allows negative edges and can detect reachable negative cycles.  
**বাংলা:** Negative edge থাকলে Dijkstra সাধারণভাবে ব্যবহার করা যায় না।

## NP-Hard vs NP-Complete
**NP-Hard:** At least as hard as NP problems; not necessarily in NP.  
**NP-Complete:** Both NP and NP-Hard.  
**বাংলা:** NP-Complete = NP + NP-Hard।

## Worst vs Average Case
**Worst:** Maximum cost.  
**Average:** Expected cost under an input model.  
**বাংলা:** Average-case করতে input distribution/model দরকার।

## Amortized vs Average-Case
**Amortized:** Sequence-এর total cost; probability লাগে না।  
**Average-case:** Input distribution/model-এর ওপর expected cost।  
**বাংলা:** দুটো এক জিনিস নয়।

---

# LAST-MINUTE VIVA REVISION

### 10 সবচেয়ে important definition
1. Data Structure = organized data + efficient operations.
2. Algorithm = finite steps to solve a problem.
3. Stack = LIFO.
4. Queue = FIFO.
5. Tree = hierarchical non-linear structure.
6. Graph = vertices + edges.
7. Hashing = key → hash table location.
8. Greedy = locally best choice.
9. DP = overlapping subproblems + stored results.
10. Backtracking = try → explore → undo.

### 10 সবচেয়ে important complexity
1. Array access = O(1)
2. Linear Search = O(n)
3. Binary Search = O(log n)
4. Stack Push/Pop = O(1)
5. Queue operations = O(1) with suitable implementation
6. Heap Insert/Extract = O(log n)
7. Hash expected lookup = O(1)
8. Merge Sort = O(n log n)
9. Quick Sort worst = O(n²)
10. BFS/DFS = O(V+E)

### 10 সবচেয়ে important traps
1. BST is not automatically balanced.
2. Heap is not fully sorted.
3. Binary Search needs appropriate ordering.
4. Hash O(1) is expected, not guaranteed worst-case.
5. Build Heap is O(n).
6. BFS uses Queue.
7. DFS uses Stack/Recursion.
8. Dijkstra does not generally allow negative edges.
9. Greedy does not always produce optimal solutions.
10. NP does not mean non-polynomial.

---

# SYLLABUS COVERAGE CHECKLIST

## CSE 220
- [x] Data organisation
- [x] Data structures
- [x] Algorithms
- [x] Performance
- [x] Concepts/examples
- [x] Elementary data objects
- [x] Elementary data structures
- [x] Arrays
- [x] Lists
- [x] Stacks
- [x] Queues
- [x] Graphs
- [x] Trees
- [x] Compound structures
- [x] Data abstraction
- [x] Primitive operations
- [x] Memory management
- [x] Sorting
- [x] Searching
- [x] Hash techniques
- [x] Recursion
- [x] Backtrack search
- [x] Operations on sets
- [x] Priority queues
- [x] Graph dictionary
- [x] Fundamental algorithms/data structures
- [x] Analysis of algorithms
- [x] Database systems
- [x] Data structure performance/use in databases

## CSE 221
- [x] Efficient algorithms
- [x] Algorithm design techniques
- [x] Analysis techniques
- [x] Divide and Conquer
- [x] Greedy method
- [x] Dynamic Programming
- [x] Backtracking
- [x] Basic search
- [x] Basic traversal
- [x] Graph algorithms
- [x] Elementary parallel algorithms
- [x] Algebraic simplification
- [x] Algebraic transformations
- [x] Lower bound theory
- [x] NP-Hard
- [x] NP-Complete
- [x] Sorting
- [x] Set data structures
- [x] Heaps
- [x] Hashing
- [x] Shortest paths
- [x] DFS
- [x] Network flow
- [x] Computational geometry
- [x] GCD
- [x] Primality
- [x] Polynomial calculations
- [x] Matrix calculations
- [x] Amortised analysis
- [x] Performance bounds
- [x] Asymptotic analysis
- [x] Worst-case behaviour
- [x] Average-case behaviour
- [x] Correctness
- [x] Complexity
- [x] Sorting in detail
- [x] Searching in detail
