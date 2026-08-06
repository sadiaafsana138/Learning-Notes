# 📕 MASTER SUMMARY SHEET
### সব বিষয়ের সব গুরুত্বপূর্ণ কথা — এক জায়গায়

> **পরীক্ষার আগে শুধু এইটা পড়ো।** অন্য কোনো ফাইল খুলতে হবে না।
> পড়ার সময়: **৩৫–৪০ মিনিট** · শুধু তথ্য, কোনো ব্যাখ্যা নেই

---

## 🗺️ সূচি

| # | বিষয় | প্রশ্ন |
|---|---|---|
| 1 | **Networking** | 4/15 |
| 2 | **Database & SQL** | 4/15 |
| 3 | **Programming & OOP** | 3/15 |
| 4 | **Operating Systems** | 1/15 |
| 5 | **Software Engineering** | 1/15 |
| 6 | **Number System & DLD** | 1/15 |
| 7 | Data Structures | — |
| 8 | Algorithms | — |
| 9 | ML & DL | — |
| 10 | English Essay | Section 2 |
| ★ | **সব সূত্র একসাথে** | |
| ★ | **Top 40 ভুল** | |

---
---

# 1️⃣ NETWORKING

## OSI vs TCP/IP
| # | OSI Layer (7) | PDU | Protocol / Device |
|---|---|---|---|
| 7 | **Application** | Data | HTTP, FTP, SMTP, DNS |
| 6 | **Presentation** | Data | **Encryption**, SSL, JPEG |
| 5 | **Session** | Data | NetBIOS, RPC |
| 4 | **Transport** | **Segment** | **TCP, UDP** |
| 3 | **Network** | **Packet** | **IP, ICMP, Router** |
| 2 | **Data Link** | **Frame** | Ethernet, **MAC, Switch** |
| 1 | **Physical** | **Bit** | Cable, **Hub**, Repeater |

**TCP/IP = 4 layer:** Application (7+6+5) · Transport (4) · Internet (3) · Network Access (2+1)

### ⚡ ৭ শব্দে পুরো OSI ⭐⭐⭐
> **App → Format → Connect → Packets → IP → MAC → Bits**
> (Application · Presentation · Session · Transport · Network · Data Link · Physical)

**Mnemonic:** All People Seem To Need Data Processing
**PDU ক্রম:** Data → **Segment** → Packet → Frame → Bit
⚠️ Trick-এ L4 = "Packets" মনে রাখার জন্য, কিন্তু **PDU চাইলে Segment** লিখবে

**বাস্তব উদাহরণ (google.com সার্চ):** Chrome request (7) → TLS encrypt (6) → session (5) → TCP + port 443 (4) → IP + routing (3) → MAC frame (2) → bits (1)

## IP Address
| | |
|---|---|
| IPv4 | **32 bit**, dotted decimal, ~4.3 বিলিয়ন |
| IPv6 | **128 bit**, hexadecimal, ৮ group |
| MAC | **48 bit**, Layer 2, স্থায়ী |
| Port | **16 bit**, মোট 65,536 |

| Class | Range | Mask | CIDR |
|---|---|---|---|
| **A** | 1–126 | 255.0.0.0 | /8 |
| **B** | 128–191 | 255.255.0.0 | /16 |
| **C** | 192–223 | 255.255.255.0 | /24 |
| D | 224–239 | Multicast | — |
| E | 240–255 | Experimental | — |

**127 = Loopback** · **Private: 10.x · 172.16–31.x · 192.168.x**

## Subnetting ⭐⭐⭐
```
Host = 2ⁿ − 2      Subnet = 2ᵐ      Block = 256 − mask octet
```
| CIDR | Mask | Block | Host |
|---|---|---|---|
| /24 | 0 | 256 | 254 |
| /25 | 128 | 128 | 126 |
| **/26** | **192** | **64** | **62** |
| **/27** | **224** | **32** | **30** |
| **/28** | **240** | **16** | **14** |
| /29 | 248 | 8 | 6 |
| **/30** | **252** | **4** | **2** |

**পদ্ধতি:** Block size বের করো → গুণিতক লেখো → IP কোন দুই গুণিতকের মাঝে দেখো → নিচেরটা = Network, পরেরটা−1 = Broadcast

**উদাহরণ:** `192.168.1.100/26` → block 64 → 64≤100<128 → **Network .64, Broadcast .127, Host .65–.126**

## VLSM & CIDR
- **VLSM** = এক network-এ ভিন্ন আকারের subnet, প্রয়োজনমতো বরাদ্দ। নিয়ম: **বড় চাহিদা আগে**
- **CIDR** = classless, /notation, IP অপচয় কমায় + **route aggregation**

## IPv6
`2001:0db8:0000:0000:0000:ff00:0042:8329` → `2001:db8::ff00:42:8329`
- Leading zero বাদ · পরপর শূন্য group = `::` (**একবারই**)
- Loopback = `::1` · **Broadcast নেই** → Unicast/Multicast/**Anycast**
- Header স্থির **40 byte**, IPsec অন্তর্নির্মিত

## TCP vs UDP
| | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Header | **20 byte** | **8 byte** |
| গতি | ধীর, নির্ভরযোগ্য | **দ্রুত** |
| উদাহরণ | HTTP, FTP, SMTP | **DNS, DHCP, VoIP, Streaming** |

**Handshake:** SYN → SYN-ACK → ACK · বিচ্ছেদ = FIN/ACK ×2

**Port:** 21 FTP · 22 SSH · 23 Telnet · 25 SMTP · **53 DNS** · 67/68 DHCP · **80 HTTP** · **443 HTTPS**

## Protocol & Device
**DNS** নাম→IP · **DHCP** স্বয়ংক্রিয় IP (**DORA**) · **NAT** private↔public · **ARP** IP→MAC · **ICMP** ping
**Hub L1** (সবাইকে) · **Switch L2** (MAC, শুধু গন্তব্যে) · **Router L3** (IP)

## Wireless
| Standard | Freq | Speed |
|---|---|---|
| 802.11a | 5 GHz | 54 Mbps |
| **802.11b** | **2.4 GHz** | **11 Mbps** ⭐ |
| 802.11g | 2.4 GHz | 54 Mbps |
| 802.11n | 2.4/5 | 600 Mbps |

**802.3 Ethernet · 802.5 Token Ring · 802.11 Wi-Fi · 802.15 Bluetooth · 802.16 WiMAX**

**অন্যান্য:** Simplex/Half/Full-duplex · Fiber = দ্রুততম · FDM/TDM/WDM · **Internet = Packet Switching** · Mesh link = n(n−1)/2

---
---

# 2️⃣ DATABASE & SQL

## Keys
| Key | নিয়ম |
|---|---|
| **Super Key** | unique (বাড়তি থাকতে পারে) |
| **Candidate Key** | **minimal** super key |
| **Primary Key** | **unique + NOT NULL**, table-এ **একটাই** |
| **Alternate Key** | candidate ছিল, primary হয়নি |
| **Foreign Key** | অন্য table-এর PK reference · **NULL ও duplicate চলে** · একাধিক চলে |

## SQL Command ধরন
**DDL** CREATE/ALTER/DROP/**TRUNCATE** · **DML** INSERT/UPDATE/DELETE · **DQL** SELECT · **DCL** GRANT/REVOKE · **TCL** COMMIT/ROLLBACK

## আবশ্যিক Syntax
```sql
CREATE DATABASE MainRecord;
USE MainRecord;

CREATE TABLE Record1 (
    ID   INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age  INT
);

INSERT INTO Record1 VALUES (101, 'Rahim', 32);
SELECT Age FROM Record1 WHERE Age = 32;
UPDATE Record1 SET Age = 33 WHERE ID = 101;
DELETE FROM Record1 WHERE ID = 101;

SELECT Dept, COUNT(*) FROM Student GROUP BY Dept HAVING COUNT(*) > 5;
SELECT * FROM Student WHERE Name LIKE 'R%' ORDER BY Age DESC;
```

## DELETE vs TRUNCATE vs DROP ⭐
| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Type | **DML** | **DDL** | **DDL** |
| WHERE | ✅ | ❌ | ❌ |
| Rollback | ✅ | ❌ | ❌ |
| গঠন থাকে | ✅ | ✅ | ❌ |

## WHERE vs HAVING ⭐
**WHERE** = GROUP BY-এর **আগে**, একক row, aggregate চলে না
**HAVING** = GROUP BY-এর **পরে**, group-এর উপর, aggregate চলে

**চলার ক্রম:** `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`

## JOIN
| JOIN | ফল |
|---|---|
| **INNER** | শুধু **দুই দিকেই মিল** |
| **LEFT** | **বামের সব** + ডানের মিল (NULL) |
| **RIGHT** | **ডানের সব** |
| **FULL** | দুই দিকের সব |
| **CROSS** | m × n |

## Normalization ⭐
| NF | শর্ত |
|---|---|
| **1NF** | সব মান **atomic** |
| **2NF** | 1NF + **partial dependency নেই** |
| **3NF** | 2NF + **transitive dependency নেই** |
| **BCNF** | প্রতিটি determinant = candidate key |

*PK একটা column হলে 1NF ⇒ 2NF স্বয়ংক্রিয়*

## অন্যান্য
**ACID** = Atomicity · Consistency · Isolation · Durability
**3-level:** External (view) → Conceptual (logical) → Internal (physical)
**Index = B+ Tree** — SELECT দ্রুত, INSERT ধীর · **Clustered একটাই**
**ER:** Entity আয়তক্ষেত্র · Relationship রম্বস · Attribute উপবৃত্ত · **1:M → M-দিকে FK** · **M:N → junction table**

---
---

# 3️⃣ PROGRAMMING & OOP

## Data Type (C)
`char 1` · `int 4` · `float 4` · `double 8` byte

## Operator ⭐
```
() > ++/-- > * / % > + - > < > > == != > && > || > =
```
| | |
|---|---|
| `i++` | **আগে ব্যবহার, পরে বাড়ে** |
| `++i` | **আগে বাড়ে, পরে ব্যবহার** |
| `5/2` | **2** (integer division) |
| `5.0/2` | 2.5 |
| `%` | **শুধু integer**, float-এ চলে না |

## Math Function ⭐
| কাজ | C | Java |
|---|---|---|
| Float ভাগশেষ | **`fmod(3.14, 2.1)`** | `3.14 % 2.1` |
| Round | **`round(1.66)` → 2.0** | `Math.round()` |
| উপরে | `ceil(1.2)` → 2 | `Math.ceil()` |
| নিচে | `floor(1.8)` → 1 | `Math.floor()` |

## Short-Circuit ⭐⭐⭐
```
A && B  →  A false হলে B চলেই না
A || B  →  A true হলে B চলেই না
```
**Q8 উদাহরণ:** `(i<3) && (j++ < 10)` — শেষে i=3 হলে j++ **চলে না**
Output: ` 0 6 1 7 2 8 3 9`

## OOP ৪ স্তম্ভ
| | |
|---|---|
| **Encapsulation** | Data + method একসাথে, private দিয়ে লুকানো |
| **Inheritance** | Parent থেকে property পাওয়া |
| **Polymorphism** | এক নাম, ভিন্ন আচরণ |
| **Abstraction** | জটিলতা লুকিয়ে শুধু দরকারিটা দেখানো |

## Overloading vs Overriding ⭐⭐⭐
| | **Overloading** | **Overriding** |
|---|---|---|
| কখন | **Compile-time** | **Run-time** |
| কোথায় | একই class | Parent-Child |
| Parameter | **ভিন্ন** | **একই** |
| আরেক নাম | Static/Early binding | Dynamic/Late binding |

## Platform Independence ⭐
```
Source (.java) → Compiler → Bytecode (.class) → JVM → Machine code
```
**Bytecode platform-independent, JVM platform-dependent** — "Write Once, Run Anywhere"
**JDK ⊃ JRE ⊃ JVM**

## অন্যান্য
Abstract class (আংশিক implementation, extends) vs **Interface** (সম্পূর্ণ abstract, implements, multiple চলে)
Access: `private < default < protected < public`
`==` reference তুলনা · `.equals()` মান তুলনা
**String immutable** · StringBuffer thread-safe · StringBuilder দ্রুত

---
---

# 4️⃣ OPERATING SYSTEMS

## Process vs Thread ⭐⭐⭐
| | **Process** | **Thread** |
|---|---|---|
| Memory | **নিজস্ব** | **শেয়ার করে** |
| তৈরির খরচ | বেশি | **কম (lightweight)** |
| Context switch | ধীর | দ্রুত |
| যোগাযোগ | IPC লাগে | সরাসরি |
| একটা crash করলে | অন্যরা ঠিক | **পুরো process যেতে পারে** |

**Multithreading** = এক process-এ একাধিক thread একসাথে
**Process states:** New → Ready → Running → Waiting → Terminated

## Scheduling
| | বৈশিষ্ট্য |
|---|---|
| **FCFS** | যে আগে আসে, Queue, convoy effect |
| **SJF** | সবচেয়ে ছোট কাজ আগে, optimal কিন্তু starvation |
| **Priority** | Starvation → **Aging** দিয়ে সমাধান |
| **Round Robin** | Time quantum, **Circular Queue** |

```
Turnaround = Completion − Arrival
Waiting    = Turnaround − Burst
```

## Deadlock ৪ শর্ত ⭐
**Mutual Exclusion · Hold and Wait · No Preemption · Circular Wait**
সমাধান: Prevention · Avoidance (**Banker's**) · Detection · Recovery
**Deadlock = আটকে আছে · Starvation = অপেক্ষা করছে**

## Memory
**Paging** = সমান আকারের page (internal fragmentation)
**Segmentation** = যৌক্তিক অংশ (external fragmentation)
Page replacement: **FIFO · LRU · Optimal** · **Belady's anomaly = FIFO-তে**
Thrashing = অতিরিক্ত page fault
**Semaphore · Mutex · Critical Section · Race Condition**

---
---

# 5️⃣ SOFTWARE ENGINEERING

## SDLC ৬ ধাপ ⭐
```
Requirement Analysis → Design → Implementation → Testing → Deployment → Maintenance
```

## Models
| Model | বৈশিষ্ট্য |
|---|---|
| **Waterfall** | Sequential, পিছনে ফেরা যায় না, requirement স্থির হলে |
| **Iterative** | ধাপে ধাপে বাড়ে |
| **Spiral** | **Risk-driven** |
| **Agile/Scrum** | Iterative + feedback, **সবচেয়ে জনপ্রিয়** |
| **V-Model** | প্রতিটি dev phase-এর সাথে একটি test phase |

## Testing
**Black Box** = ভিতরে না দেখে, functionality · **White Box** = code দেখে, logic
স্তর: Unit → Integration → System → Acceptance
**Verification** = "ঠিকভাবে বানাচ্ছি?" · **Validation** = "ঠিক জিনিস বানাচ্ছি?"
**Cohesion বেশি ভালো · Coupling কম ভালো**

---
---

# 6️⃣ NUMBER SYSTEM & DLD

## Conversion ⭐⭐⭐
**Binary → Decimal:** ঘর মান `128 64 32 16 8 4 2 1`, ভগ্নাংশে `½ ¼ ⅛ 1/16`

```
(1011.1101)₂
পূর্ণাংশ: 8+0+2+1 = 11
ভগ্নাংশ: 0.5+0.25+0+0.0625 = 0.8125
উত্তর = 11.8125
```

**Decimal → Binary:** পূর্ণাংশ 2 দিয়ে ভাগ (remainder নিচ থেকে উপরে) · ভগ্নাংশ 2 দিয়ে গুণ (উপর থেকে নিচে)
**Binary ↔ Octal:** ৩ bit করে · **Binary ↔ Hex:** ৪ bit করে

## Complement
**1's** = সব bit উল্টাও · **2's** = 1's + 1
বিয়োগ: `A − B = A + (B-এর 2's complement)`, শেষ carry ফেলে দাও
n bit-এ range: **−2ⁿ⁻¹ থেকে +2ⁿ⁻¹−1**

## Gates
| Gate | ফলাফল |
|---|---|
| AND | দুটোই 1 হলে 1 |
| OR | একটাও 1 হলে 1 |
| NOT | উল্টো |
| **NAND** | AND-এর উল্টো · **Universal** ⭐ |
| **NOR** | OR-এর উল্টো · **Universal** ⭐ |
| **XOR** | **ভিন্ন হলে 1** |
| XNOR | একই হলে 1 |

## De Morgan ⭐
```
(A·B)' = A' + B'
(A+B)' = A' · B'
```

## Adder
```
Half Adder:  Sum = A⊕B        Carry = A·B
Full Adder:  Sum = A⊕B⊕Cin    Cout = A·B + Cin·(A⊕B)
```
Full Adder = **২টি Half Adder + ১টি OR**

## Combinational vs Sequential
**Combinational** — memory নেই, output শুধু বর্তমান input-এর উপর (Adder, MUX, Decoder)
**Sequential** — memory আছে, clock লাগে (Flip-flop, Counter, Register)

**MUX** = 2ⁿ input → 1 output, n select line
**DEMUX** = 1 → 2ⁿ · **Decoder** = n → 2ⁿ · **Encoder** = 2ⁿ → n
**Flip-flop:** SR (invalid 1,1) · **JK (1,1 = toggle)** · D (delay) · T (toggle)

---
---

# 7️⃣ DATA STRUCTURES

## Complexity Master Table ⭐⭐⭐
| DS | Access | Search | Insert | Delete |
|---|---|---|---|---|
| **Array** | **O(1)** | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | **O(1)*** | **O(1)*** |
| **Stack/Queue** | O(n) | O(n) | **O(1)** | **O(1)** |
| **BST (avg)** | O(log n) | O(log n) | O(log n) | O(log n) |
| **BST (worst)** | O(n) | **O(n)** | O(n) | O(n) |
| **AVL** | O(log n) | **O(log n)** | O(log n) | O(log n) |
| **Heap** | O(1) max | O(n) | O(log n) | O(log n) |
| **Hash (avg)** | — | **O(1)** | **O(1)** | **O(1)** |
| **Hash (worst)** | — | O(n) | O(n) | O(n) |

*beginning-এ

## Classification
**Linear:** Array, Stack, Queue, Linked List · **Non-Linear:** Tree, Graph
**Static** = Array (compile time) · **Dynamic** = Linked List (run time, heap)
**ADT** = specification (Stack, Queue, List) · **DS** = implementation (Array, Heap)

## Stack & Queue
**Stack = LIFO**, Push/Pop/Peek O(1), এক প্রান্ত · **Full+Push=Overflow, Empty+Pop=Underflow**
**Queue = FIFO**, Enqueue (Rear)/Dequeue (Front), দুই প্রান্ত
**Stack → DFS, Recursion, Undo, Browser Back, Infix→Postfix**
**Queue → BFS, Printer, CPU Scheduling**
Infix `A+B` · Prefix `+AB` · Postfix `AB+`

## Tree ⭐
```
n নোড → n−1 edge
Level i-তে max node = 2ⁱ
Height h-এ max node = 2^(h+1) − 1
Min height = ⌊log₂ n⌋
NULL pointer = n + 1
```
**Pre** = Root-Left-Right · **In** = Left-Root-Right · **Post** = Left-Right-Root · **Level** = BFS/Queue
⭐ **BST-এর Inorder = sorted**
⚠️ **Preorder+Postorder দিয়ে unique tree হয় না**
BST delete (2 child) → **inorder successor**
**AVL** = Balance Factor ∈ {−1,0,1} · LL→Right, RR→Left, LR/RL→Double

## Heap ⭐
**Complete Binary Tree + heap property** · **Heap ≠ BST**
Array: `left = 2i+1, right = 2i+2, parent = (i−1)/2`
Peek **O(1)** · Insert/Delete **O(log n)** · **Build Heap O(n)** · Search O(n)

## Hashing
`h(k) = k mod m` · **Collision** → **Chaining** (linked list) বা **Open Addressing** (Linear/Quadratic/Double)
**Load factor α = n/m** · α>0.7 → rehash · **sorted order নেই**

## Graph
**G = (V,E)** · Matrix **O(V²)** (dense, edge check O(1)) · List **O(V+E)** (sparse)
Complete undirected edge = **n(n−1)/2** · Sum of degrees = **2E**
**Tree = connected + acyclic, E = V−1**

---
---

# 8️⃣ ALGORITHMS

## Asymptotic ⭐⭐⭐
**O = Upper (worst) · Ω = Lower (best) · Θ = Tight (average)**
```
1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!
```
Nested loop = গুণ · Sequential = বড়টা · `i = i*2` loop = **O(log n)**

## Sorting ⭐⭐⭐
| Algorithm | Best | Avg | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Selection** | **O(n²)** | O(n²) | O(n²) | O(1) | ❌ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Merge** | O(n log n) | O(n log n) | **O(n log n)** | **O(n)** | ✅ |
| **Quick** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ |
| **Heap** | O(n log n) | O(n log n) | **O(n log n)** | **O(1)** | ❌ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ |

**Unstable = Selection, Quick, Heap** · **Comparison sort-এর সীমা Ω(n log n)**
Quick worst = sorted array + first pivot · Linked List → **Merge Sort**

## Searching
**Linear O(n)** (sorted লাগে না) · **Binary O(log n)** (**sorted আবশ্যক**) · Jump O(√n) · **Hash O(1)**
`mid = low + (high−low)/2`

## Design Technique ⭐⭐⭐
| Technique | Algorithm |
|---|---|
| **Divide & Conquer** | Binary Search, Merge, Quick, Strassen |
| **Greedy** | **Dijkstra, Prim, Kruskal, Huffman, Fractional Knapsack, Activity Selection** |
| **DP** | **0/1 Knapsack, LCS, Matrix Chain, Floyd-Warshall, Bellman-Ford** |
| **Backtracking** | N-Queens, Sudoku, Graph Coloring, Hamiltonian |

⚠️ **Fractional Knapsack = Greedy · 0/1 Knapsack = DP**
**D&C** subproblem independent · **DP** overlapping + optimal substructure

## Graph Algorithm ⭐⭐⭐
| Algorithm | Type | Time | নোট |
|---|---|---|---|
| **BFS** | Queue | O(V+E) | **unweighted shortest path** |
| **DFS** | Stack | O(V+E) | cycle detection |
| **Dijkstra** | Greedy | O((V+E)log V) | ⚠️ **negative weight-এ না** |
| **Bellman-Ford** | DP | **O(V·E)** | negative OK |
| **Floyd-Warshall** | DP | **O(V³)** | **all-pairs** |
| **Prim** | Greedy | O(E log V) | vertex, heap, dense |
| **Kruskal** | Greedy | O(E log E) | edge, **Union-Find**, sparse |
| **Topological** | — | O(V+E) | **শুধু DAG** |

**MST edge = V − 1**

## অন্যান্য
**Master Theorem:** `T(n)=aT(n/b)+f(n)` · Merge O(n log n) · Binary Search O(log n) · Hanoi **2ⁿ−1**
**Amortized:** Dynamic Array insert = **O(1) amortized**
**P ⊆ NP** · **NP-Complete = NP ∩ NP-Hard** · প্রথম NPC = **SAT**
**GCD:** `GCD(a,b)=GCD(b, a mod b)`, O(log n) · **LCM = a×b/GCD**
Primality **O(√n)** · Sieve **O(n log log n)**

---
---

# 9️⃣ ML & DL

## ধরন
**AI ⊃ ML ⊃ DL** · ML = data + output → **rules**
| Type | Data | উদাহরণ |
|---|---|---|
| **Supervised** | Labeled | Linear/Logistic Reg, SVM, **KNN**, Decision Tree |
| **Unsupervised** | Unlabeled | **K-Means**, **PCA** |
| **Reinforcement** | Reward | Q-Learning |

⚠️ **KNN = Supervised, K-Means = Unsupervised** · **Logistic Regression = Classification**
**Classification** = "কোনটা?" · **Regression** = "কত?"

## Training
**Overfitting** = train ভালো test খারাপ = **High Variance** → Dropout, Regularization, বেশি data
**Underfitting** = দুটোই খারাপ = **High Bias**
**Parameter** = model শেখে (weight, bias) · **Hyperparameter** = তুমি দাও (lr, epoch, k)
**Bagging** = parallel, variance কমায়, **Random Forest** · **Boosting** = sequential, bias কমায়, **XGBoost**

## Metrics ⭐
```
Precision = TP/(TP+FP)     "যা বলেছি তার কতটা সত্যি"
Recall    = TP/(TP+FN)     "যা ছিল তার কতটা ধরেছি"
F1        = 2PR/(P+R)
```
**ক্যান্সার → Recall · Spam → Precision** · **Imbalanced data-তে Accuracy বিভ্রান্তিকর**

## Deep Learning
`output = Activation(Σwx + b)` · **Activation না থাকলে network পুরোটাই linear**
**Hidden → ReLU · Binary → Sigmoid · Multi-class → Softmax**
**Forward → Loss → Backpropagation → Gradient Descent** · `w = w − lr × gradient`
**CNN → Image · RNN/LSTM → Sequence · Transformer → NLP (Attention)**
Vanishing gradient → ReLU/LSTM · Overfitting → Dropout

---
---

# 🔟 ENGLISH ESSAY

## পাঁচ ধাপ ⭐
```
১. Stance (~25)        একটি পক্ষ স্পষ্টভাবে
২. Reason 1 + Example (~45)
৩. Reason 2 + Example (~45)
৪. Counter-point + Rebuttal (~45)   ← এখানেই নম্বর
৫. Conclusion (~30)    পুনরুক্তি, নতুন যুক্তি নয়
```
**লক্ষ্য ১৮৫–১৯৫ শব্দ · ৪–৫টি অনুচ্ছেদ**

## অবশ্য-ব্যবহার্য বাক্য
- *In my view, …*
- *The strongest argument for X is …*
- *For instance, in Bangladesh, …*
- **Some argue, on the contrary, that … The concern is legitimate, but …**
- *It is true that … Nevertheless, …*
- *In conclusion, …*

## নিয়ম
Contraction নয় (don't → **do not**) · "I think" বারবার নয় → **"In my view"**
মতামত = Present simple · উদাহরণ = Past simple · ভবিষ্যদ্বাণী = will

---
---

# ★ সব সূত্র একসাথে

| সূত্র | কোথায় |
|---|---|
| **Host = 2ⁿ − 2** · **Subnet = 2ᵐ** | Subnetting |
| **Block = 256 − mask octet** | Subnetting |
| Mesh link = **n(n−1)/2** | Topology |
| Port = 2¹⁶ = **65,536** | Transport |
| `Address(A[i]) = Base + i × size` | Array |
| `A[i][j] = Base + [(i×cols)+j] × size` | 2D Array |
| Tree edge = **n − 1** | Tree |
| Level i max = **2ⁱ** · Height h max = **2^(h+1) − 1** | Binary Tree |
| Min height = **⌊log₂ n⌋** · NULL pointer = **n+1** | Binary Tree |
| Heap: **2i+1, 2i+2, (i−1)/2** | Heap |
| **α = n/m** | Hashing |
| Complete graph edge = **n(n−1)/2** · Σdegree = **2E** | Graph |
| MST edge = **V − 1** | Graph |
| Hanoi = **2ⁿ − 1** | Recursion |
| `GCD(a,b) = GCD(b, a mod b)` · **LCM = ab/GCD** | Number |
| Sum = A⊕B, Carry = A·B | Half Adder |
| `(A·B)' = A'+B'` | De Morgan |
| Turnaround = C − A · Waiting = T − B | Scheduling |
| Precision = TP/(TP+FP) · Recall = TP/(TP+FN) | ML |

---
---

# ★ TOP 40 ভুল — একবার চোখ বুলাও

## Networking
1. **OSI 7, TCP/IP 4**
2. **Encryption = Presentation layer**
3. **Hub L1, Switch L2, Router L3**
4. **Class A 1–126** (127 = loopback)
5. **IPv6-এ Broadcast নেই**
6. **`::` একবারই**
7. **DNS ও DHCP = UDP**
8. **802.11b = 11 Mbps** (g = 54)
9. **Internet = Packet Switching**
10. **MAC 48 bit, IP 32 bit**

## Database
11. **PK = unique + NOT NULL**, FK-এ NULL চলে
12. **TRUNCATE = DDL**, rollback হয় না
13. **DELETE-এ WHERE চলে, TRUNCATE-এ নয়**
14. **WHERE-এ aggregate চলে না**
15. **1NF atomic, 2NF partial, 3NF transitive**
16. **INNER JOIN = শুধু মিল**
17. চলার ক্রম **FROM আগে, SELECT পরে**

## Programming
18. **`%` float-এ চলে না** → fmod
19. **`&&` short-circuit** — দ্বিতীয়টা চলতেই পারে না
20. **`5/2 = 2`** (integer division)
21. **Overloading compile-time, Overriding run-time**
22. **Bytecode independent, JVM dependent**
23. **Java-তে multiple inheritance নেই** (interface দিয়ে)

## OS / SE
24. **Thread memory শেয়ার করে, Process করে না**
25. **Round Robin = Circular Queue**
26. **Belady's anomaly = FIFO-তে**
27. **Verification ≠ Validation**
28. **Waterfall-এ পিছনে ফেরা যায় না**

## DLD
29. **NAND ও NOR = Universal gate**
30. **XOR = ভিন্ন হলে 1**
31. **JK-তে (1,1) = toggle**, SR-এ invalid
32. ভগ্নাংশে ঘর মান **½, ¼, ⅛, 1/16**

## DS / Algo
33. **BST-এর Inorder = sorted**
34. **BST worst = O(n)**, always O(log n) নয়
35. **Build Heap = O(n)**
36. **Heap ≠ BST**
37. **Preorder+Postorder দিয়ে unique tree হয় না**
38. **Selection Sort-এর best-ও O(n²)**
39. **Quick worst = O(n²)** · **Merge = O(n) space**
40. **Dijkstra negative weight-এ চলে না** · **Fractional=Greedy, 0/1=DP**

---

> **পড়া শেষ? আর কিছু খুলো না।**
> এখন শুধু শান্ত থাকো। যা জানো তা যথেষ্ট — এখন দরকার সময়ের সঠিক ভাগ।
> **প্রশ্নপত্র হাতে পেয়ে প্রথমেই মোট সময় দেখে নিও, তারপর English প্রবন্ধের জন্য ২০ মিনিট আলাদা করে রাখো।**
