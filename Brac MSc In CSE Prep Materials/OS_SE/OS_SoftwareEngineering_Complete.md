# ⚙️ OPERATING SYSTEMS & SOFTWARE ENGINEERING
### CSE 321 + CSE 470 — BRAC MSc CSE Admission

> **Sample paper-এ ২টা প্রশ্ন** (Q14 Thread/Multithread, Q15 SDLC)।
> **সময়: OS ১ ঘণ্টা + SE ৩০ মিনিট**

---

# 🖥️ PART A — OPERATING SYSTEMS

## 📑 সূচি
| Module | বিষয় | Dry Run |
|---|---|---|
| 1 | OS Basics | — |
| 2 | **Process & Thread (Q14)** ⭐⭐⭐ | ✅ |
| 3 | **CPU Scheduling** ⭐⭐ | ✅ Gantt chart |
| 4 | **Deadlock** ⭐⭐ | ✅ |
| 5 | **Memory Management** ⭐⭐ | ✅ Page replacement |
| 6 | Synchronization | — |

---
---

# MODULE 1 — OS BASICS

## Topic 1: Operating System

### Definition (English)
An **Operating System** is system software that acts as an **interface between the user and computer hardware**, managing all hardware and software resources.

⭐ **Keywords:** Interface · Resource Manager · System Software

### OS-এর প্রধান কাজ ⭐
```
┌─────────────────────────────┐
│      User / Application      │
├─────────────────────────────┤
│      OPERATING SYSTEM        │  ← Process, Memory, File, Device,
│                              │     Security ব্যবস্থাপনা
├─────────────────────────────┤
│        Hardware              │
└─────────────────────────────┘
```

1. **Process Management** — কোন program কখন CPU পাবে
2. **Memory Management** — কে কতটুকু RAM পাবে
3. **File Management** — file তৈরি, পড়া, মোছা
4. **Device Management** — printer, disk, keyboard নিয়ন্ত্রণ
5. **Security** — কে কী করতে পারবে

## Topic 2: OS-এর ধরন
| Type | বৈশিষ্ট্য |
|---|---|
| **Batch** | একই ধরনের job একসাথে, user সরাসরি যুক্ত নয় |
| **Time-sharing** | অনেক user একসাথে, প্রত্যেকে সময়ের ভাগ পায় |
| **Real-time** | **নির্দিষ্ট সময়সীমার মধ্যে** সাড়া দিতেই হবে (pacemaker, ABS) |
| **Distributed** | অনেক computer মিলে একসাথে কাজ |
| **Multiprogramming** | RAM-এ একাধিক program, একটা I/O করলে অন্যটা CPU পায় |
| **Multitasking** | একসাথে অনেক কাজ (time-sharing-এর রূপ) |

---
---

# MODULE 2 — PROCESS & THREAD ⭐⭐⭐

> **Q14-এর উত্তর এখানে।**

## Topic 1: Process

### Definition (English)
A **Process** is a **program in execution** — an active entity with its **own memory space**, program counter, stack, and set of resources.

⭐ **Keywords:** Program in execution · Own memory space · Active

### Program vs Process ⭐
| | **Program** | **Process** |
|---|---|---|
| ধরন | **Passive** (নিষ্ক্রিয়) | **Active** (সক্রিয়) |
| কোথায় | **Disk-এ** পড়ে থাকে | **RAM-এ** চলছে |
| আয়ু | স্থায়ী | সাময়িক |
| উদাহরণ | `chrome.exe` file-টা | Chrome খোলা আছে, চলছে |

⭐ **একটা program থেকে একাধিক process** চালানো যায় (Chrome-এর ৩টা window = ৩টা process)।

### Process-এর Memory Layout ⭐
```
উঁচু ঠিকানা
┌──────────────┐
│    STACK     │  ← Local variable, function call  (নিচের দিকে বাড়ে)
│      ↓       │
│              │
│      ↑       │
│    HEAP      │  ← Dynamic memory (malloc/new)    (উপরের দিকে বাড়ে)
├──────────────┤
│     DATA     │  ← Global ও static variable
├──────────────┤
│     TEXT     │  ← Program-এর code
└──────────────┘
নিচু ঠিকানা
```

### Process States ⭐⭐
```
                 ┌──────────┐
                 │   NEW    │  (তৈরি হচ্ছে)
                 └────┬─────┘
                      │ admit
                      ▼
    ┌────────────►┌───────┐  scheduler dispatch  ┌──────────┐
    │             │ READY │─────────────────────►│ RUNNING  │
    │             └───────┘◄─────────────────────└────┬─────┘
    │                 ▲       interrupt (time up)     │
    │  I/O শেষ         │                              │ I/O চাইলো
    │             ┌────┴──────┐                       │
    └─────────────│  WAITING  │◄──────────────────────┘
                  └───────────┘
                                      │ কাজ শেষ
                                      ▼
                               ┌────────────┐
                               │ TERMINATED │
                               └────────────┘
```

| State | অর্থ |
|---|---|
| **New** | Process তৈরি হচ্ছে |
| **Ready** | CPU পাওয়ার জন্য অপেক্ষা করছে |
| **Running** | **CPU-তে চলছে** |
| **Waiting/Blocked** | I/O বা কোনো ঘটনার জন্য অপেক্ষা |
| **Terminated** | শেষ হয়ে গেছে |

⚠️ **Running → Ready** হয় সময় শেষ হলে (preemption); **Running → Waiting** হয় I/O চাইলে।

### PCB (Process Control Block) ⭐
প্রতিটি process-এর তথ্য রাখার structure:
Process ID · State · **Program Counter** · Register-এর মান · Memory limit · Open file-এর তালিকা · Priority

**Context Switching** = এক process থেকে অন্যটায় যাওয়া — বর্তমানের অবস্থা PCB-তে **save** করে, নতুনটার অবস্থা **load** করা।
⚠️ এটা **overhead** — এই সময়ে কোনো কাজ হয় না।

## Topic 2: Thread ⭐⭐⭐ (Q14)

### Definition (English)
A **Thread** is the **smallest unit of execution** within a process. Multiple threads within the same process **share the same memory space** but have their own **stack and program counter**.

⭐ **Keywords:** Smallest execution unit · Lightweight · Shared memory

### Multithreading
**Definition:** **Multithreading** is the ability of a process to execute **multiple threads concurrently**, sharing the same resources.

### 🔍 ছবি দিয়ে বোঝা ⭐
```
       SINGLE-THREADED PROCESS          MULTI-THREADED PROCESS
       ┌─────────────────────┐          ┌─────────────────────────────┐
       │  Code │ Data │ File │          │    Code │ Data │ File       │  ← ভাগাভাগি
       ├─────────────────────┤          ├───────┬───────┬─────────────┤
       │ Reg │ Stack        │          │ Reg   │ Reg   │ Reg         │  ← আলাদা
       │                     │          │ Stack │ Stack │ Stack       │  ← আলাদা
       │        ▓ thread     │          │  ▓     ▓       ▓            │
       └─────────────────────┘          │ T1    T2      T3            │
                                        └─────────────────────────────┘
```

⭐ **Thread গুলো Code, Data, File ভাগ করে নেয়; কিন্তু Register ও Stack আলাদা রাখে।**

### 🔍 বাস্তব উদাহরণ — MS Word
একটা Word window (**একটি process**) চালানোর সময় একসাথে ঘটছে —
```
Thread 1 : তুমি টাইপ করছো (user input)
Thread 2 : বানান পরীক্ষা চলছে (spell check)
Thread 3 : পটভূমিতে auto-save হচ্ছে
```
সবাই একই document (shared memory) নিয়ে কাজ করছে — এটাই **Multithreading**।

### Process vs Thread ⭐⭐⭐ (Q14-এর মূল টেবিল)

| Feature | **Process** | **Thread** |
|---|---|---|
| সংজ্ঞা | চলমান program | Process-এর **ভিতরের** execution unit |
| Memory | **নিজস্ব আলাদা** memory space | **একই memory ভাগ করে** ⭐ |
| ওজন | **Heavyweight** | **Lightweight** ⭐ |
| তৈরির খরচ | **বেশি** | **কম** |
| Context switch | ধীর | **দ্রুত** |
| যোগাযোগ | **IPC** লাগে (কঠিন ও ধীর) | সরাসরি shared memory (**সহজ**) |
| একটা crash করলে | অন্য process অক্ষত ✅ | **পুরো process crash** ⚠️ |
| স্বাধীনতা | স্বাধীন | পরস্পরনির্ভর |

### Multithreading-এর সুবিধা ⭐
1. **Responsiveness** — একটা thread আটকে গেলেও UI চলতে থাকে
2. **Resource Sharing** — একই memory, তাই আলাদা বরাদ্দ লাগে না
3. **Economy** — process তৈরির চেয়ে thread তৈরি অনেক সস্তা
4. **Scalability** — multi-core CPU-তে সত্যিকারের সমান্তরাল কাজ

### ⚠️ MCQ Traps
- Thread-দের **Code, Data, File shared**; কিন্তু **Register ও Stack আলাদা** ⭐
- **Thread = lightweight process** বলা হয়
- একটা thread crash করলে **পুরো process পড়ে যায়** (process-এর ক্ষেত্রে এমন নয়)

### 🔁 Revision Box (Q14-এর উত্তর)
**Process** = চলমান program, নিজস্ব memory space, heavyweight।
**Thread** = process-এর ভিতরের ক্ষুদ্রতম execution unit, **একই memory ভাগ করে**, lightweight, নিজস্ব stack ও register রাখে।
**Multithreading** = একই process-এ একাধিক thread একসাথে চলা। সুবিধা: **responsiveness, resource sharing, economy, scalability**।

---
---

# MODULE 3 — CPU SCHEDULING ⭐⭐

## Topic 1: মূল হিসাব ⭐

```
Completion Time (CT)  = কখন কাজ শেষ হলো
Turnaround Time (TAT) = Completion Time − Arrival Time
Waiting Time (WT)     = Turnaround Time − Burst Time
Response Time         = প্রথমবার CPU পাওয়ার সময় − Arrival Time
```

## 🔍 DRY RUN 1 — FCFS (First Come First Served)

**নিয়ম:** যে আগে আসে, সে আগে CPU পায়। **Non-preemptive**। **Queue** ব্যবহার করে।

| Process | Arrival | Burst |
|---|---|---|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 8 |

**Gantt Chart:**
```
│   P1    │  P2  │      P3       │
0         5      8              16
```

| Process | CT | **TAT** = CT−AT | **WT** = TAT−BT |
|---|---|---|---|
| P1 | 5 | 5−0 = **5** | 5−5 = **0** |
| P2 | 8 | 8−1 = **7** | 7−3 = **4** |
| P3 | 16 | 16−2 = **14** | 14−8 = **6** |

```
গড় TAT = (5+7+14)/3 = 8.67
গড় WT  = (0+4+6)/3  = 3.33
```

⚠️ **Convoy Effect** — একটা বড় process সবার আগে থাকলে ছোটগুলোকে বহুক্ষণ অপেক্ষা করতে হয়।

---

## 🔍 DRY RUN 2 — SJF (Shortest Job First)

**নিয়ম:** যার burst time সবচেয়ে কম, সে আগে। **Non-preemptive** ধরছি।

একই data দিয়ে:
```
সময় 0: শুধু P1 এসেছে → P1 চলবে (0 থেকে 5)
সময় 5: P2(3) ও P3(8) দুজনেই এসে গেছে → ছোটটা আগে → P2 (5 থেকে 8)
সময় 8: P3 চলবে (8 থেকে 16)
```

**Gantt Chart:**
```
│   P1    │  P2  │      P3       │
0         5      8              16
```
(এই উদাহরণে FCFS-এর মতোই এসেছে, কিন্তু সবসময় হয় না)

⭐ **SJF গড় waiting time-এর দিক থেকে optimal**, কিন্তু ⚠️ **starvation** হতে পারে — বড় process কখনো CPU নাও পেতে পারে।

⚠️ আরেকটা সমস্যা: **burst time আগে থেকে জানা সম্ভব নয়** (আন্দাজ করতে হয়)।

**SRTF** = SJF-এর **preemptive** সংস্করণ (Shortest Remaining Time First)।

---

## 🔍 DRY RUN 3 — Round Robin (Time Quantum = 2) ⭐⭐

**নিয়ম:** প্রত্যেকে **নির্দিষ্ট সময়** (quantum) পায়, শেষ না হলে পিছনে গিয়ে লাইনে দাঁড়ায়। **Preemptive**, **Circular Queue** ব্যবহার করে।

| Process | Arrival | Burst |
|---|---|---|
| P1 | 0 | 5 |
| P2 | 0 | 3 |
| P3 | 0 | 4 |

**Quantum = 2**

```
Queue-র অবস্থা ধাপে ধাপে:

সময় 0-2  : P1 চলল 2   (বাকি 3)  → Queue: P2, P3, P1
সময় 2-4  : P2 চলল 2   (বাকি 1)  → Queue: P3, P1, P2
সময় 4-6  : P3 চলল 2   (বাকি 2)  → Queue: P1, P2, P3
সময় 6-8  : P1 চলল 2   (বাকি 1)  → Queue: P2, P3, P1
সময় 8-9  : P2 চলল 1   (শেষ ✅)   → Queue: P3, P1
সময় 9-11 : P3 চলল 2   (শেষ ✅)   → Queue: P1
সময় 11-12: P1 চলল 1   (শেষ ✅)
```

**Gantt Chart:**
```
│ P1 │ P2 │ P3 │ P1 │P2│ P3 │P1│
0    2    4    6    8  9   11 12
```

| Process | CT | TAT | WT |
|---|---|---|---|
| P1 | 12 | 12 | 12−5 = **7** |
| P2 | 9 | 9 | 9−3 = **6** |
| P3 | 11 | 11 | 11−4 = **7** |

```
গড় WT = (7+6+7)/3 = 6.67
```

⭐ **Quantum-এর প্রভাব:**
- **খুব ছোট** → বারবার context switch → overhead বেশি
- **খুব বড়** → FCFS-এর মতো হয়ে যায়

## Topic 2: তুলনা ⭐

| Algorithm | Preemptive? | সুবিধা | অসুবিধা |
|---|---|---|---|
| **FCFS** | ❌ | সহজ, ন্যায্য | **Convoy effect** |
| **SJF** | ❌ | **গড় WT সবচেয়ে কম** | **Starvation**, burst জানা যায় না |
| **SRTF** | ✅ | SJF-এর চেয়ে ভালো | Starvation |
| **Priority** | দুটোই হয় | গুরুত্ব অনুযায়ী | **Starvation** → **Aging** দিয়ে সমাধান |
| **Round Robin** | ✅ | **ন্যায্য**, response ভালো | Quantum-নির্ভর, context switch খরচ |

⭐ **Aging** = অপেক্ষারত process-এর priority ধীরে ধীরে বাড়িয়ে দেওয়া, যাতে starvation না হয়।

### 🔁 Revision Box
**TAT = CT − AT**, **WT = TAT − BT**। **FCFS** = Queue, non-preemptive, convoy effect। **SJF** = গড় WT optimal কিন্তু starvation। **Round Robin** = quantum ভাগ করে, preemptive, ন্যায্য, **Circular Queue**। **Priority** = starvation হয়, **Aging** দিয়ে সমাধান।

---
---

# MODULE 4 — DEADLOCK ⭐⭐

## Topic 1: সংজ্ঞা ও শর্ত

### Definition (English)
**Deadlock** is a situation where a set of processes are **blocked forever**, each holding a resource and waiting for another resource held by another process in the set.

### 🔍 ছবি
```
   ┌─────────┐   ধরে আছে R1    ┌────┐
   │   P1    │───────────────►│ R1 │
   └─────────┘                 └────┘
        │                         ▲
        │ চায় R2                  │ ধরে আছে
        ▼                         │
   ┌────┐                    ┌─────────┐
   │ R2 │◄───────────────────│   P2    │
   └────┘      চায় R1          └─────────┘

চক্র তৈরি হয়েছে → কেউই এগোতে পারছে না → DEADLOCK
```

**বাস্তব উপমা:** সরু সেতুর দুই প্রান্ত থেকে দুটো গাড়ি ঢুকে পড়েছে — কেউই পিছাচ্ছে না।

## Topic 2: ৪টি শর্ত ⭐⭐⭐

**চারটিই একসাথে সত্য হলে তবেই deadlock হয়। একটি ভাঙলেই deadlock হবে না।**

| # | শর্ত | অর্থ |
|---|---|---|
| 1 | **Mutual Exclusion** | একটি resource একসাথে **একজনই** ব্যবহার করতে পারে |
| 2 | **Hold and Wait** | একটা resource **ধরে রেখে** আরেকটার জন্য **অপেক্ষা** করা |
| 3 | **No Preemption** | জোর করে resource **কেড়ে নেওয়া যাবে না** |
| 4 | **Circular Wait** | Process গুলো **চক্রাকারে** একে অপরের জন্য অপেক্ষা করছে |

⭐ **মুখস্থ: M-H-N-C** (Mutual, Hold&wait, No preemption, Circular)

## Topic 3: সমাধানের ৪ কৌশল ⭐

| কৌশল | কী করে |
|---|---|
| **Prevention** | ৪টি শর্তের **একটি আগেই ভেঙে দেওয়া** (যেমন সব resource একসাথে নিতে বাধ্য করা) |
| **Avoidance** | সাবধানে বরাদ্দ দেওয়া যাতে কখনো unsafe state-এ না যায় → **Banker's Algorithm** ⭐ |
| **Detection & Recovery** | হতে দাও, পরে **ধরে ফেলে** process kill বা resource preempt করো |
| **Ignorance** | কিছুই করো না (**Ostrich Algorithm**) — বেশিরভাগ সাধারণ OS এটাই করে ⭐ |

### Banker's Algorithm সংক্ষেপে
প্রতিটি process আগেই বলে দেয় সে সর্বোচ্চ কত resource চাইতে পারে। OS বরাদ্দ দেওয়ার আগে যাচাই করে — এই বরাদ্দের পরও কি একটা **safe sequence** পাওয়া যাবে? পাওয়া গেলে দেয়, নাহলে অপেক্ষা করায়।

## Topic 4: Deadlock vs Starvation ⭐

| | **Deadlock** | **Starvation** |
|---|---|---|
| কী হয় | **কেউই** এগোতে পারে না | **একজন** বারবার বঞ্চিত হয় |
| স্থায়ী? | **চিরস্থায়ী** (হস্তক্ষেপ ছাড়া) | কখনো সুযোগ পেতে পারে |
| কারণ | চক্রাকার অপেক্ষা | অন্যায্য priority |
| সমাধান | ৪ শর্তের একটা ভাঙা | **Aging** |

### 🔁 Revision Box
Deadlock = process গুলো পরস্পরের resource-এর জন্য চিরকাল আটকে থাকা। **৪ শর্ত: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait** — চারটিই লাগবে। সমাধান: **Prevention, Avoidance (Banker's), Detection & Recovery, Ignorance**। **Starvation ≠ Deadlock**; starvation-এর সমাধান **Aging**।

---
---

# MODULE 5 — MEMORY MANAGEMENT ⭐⭐

## Topic 1: Paging vs Segmentation ⭐

| | **Paging** | **Segmentation** |
|---|---|---|
| ভাগ করে | **সমান আকারের** page-এ | **যুক্তিসঙ্গত অসমান** segment-এ |
| আকার | **স্থির** | **পরিবর্তনশীল** |
| Fragmentation | **Internal** | **External** |
| দৃষ্টিভঙ্গি | Physical (hardware) | Logical (programmer) |
| ঠিকানা | Page number + Offset | Segment number + Offset |

⭐ **Internal Fragmentation** = বরাদ্দ করা block-এর **ভিতরে** জায়গা নষ্ট (Paging-এ হয়)
⭐ **External Fragmentation** = মোট খালি জায়গা যথেষ্ট, কিন্তু **ছড়িয়ে-ছিটিয়ে** আছে (Segmentation-এ হয়)

## Topic 2: Virtual Memory
**Definition:** A technique that allows a process to execute even if it is **not entirely in main memory**, using disk space as an extension of RAM.

| Term | অর্থ |
|---|---|
| **Page Fault** | চাওয়া page RAM-এ নেই → disk থেকে আনতে হবে ⚠️ |
| **Thrashing** | এত বেশি page fault যে CPU কাজের চেয়ে page আনা-নেওয়াই বেশি করছে ⚠️ |
| **Demand Paging** | দরকার হলে তবেই page আনা |
| **TLB** | Page table-এর cache — ঠিকানা অনুবাদ দ্রুত করে |

## 🔍 DRY RUN — Page Replacement ⭐⭐

**Reference String:** `7, 0, 1, 2, 0, 3, 0, 4`
**Frame সংখ্যা: 3**

### FIFO (First In First Out)
**নিয়ম:** যে page **সবার আগে এসেছিল**, সেটাই আগে বের হবে।

| ধাপ | Page | Frame-এর অবস্থা | Fault? |
|---|---|---|---|
| 1 | 7 | [**7**, −, −] | ✅ Fault |
| 2 | 0 | [7, **0**, −] | ✅ Fault |
| 3 | 1 | [7, 0, **1**] | ✅ Fault |
| 4 | 2 | [**2**, 0, 1] | ✅ Fault (7 সবচেয়ে পুরনো → বের) |
| 5 | 0 | [2, 0, 1] | ❌ Hit (0 আছে) |
| 6 | 3 | [2, **3**, 1] | ✅ Fault (0 পুরনো → বের) |
| 7 | 0 | [2, 3, **0**] | ✅ Fault (1 পুরনো → বের) |
| 8 | 4 | [**4**, 3, 0] | ✅ Fault (2 পুরনো → বের) |

**মোট Page Fault = 7**

### LRU (Least Recently Used)
**নিয়ম:** যে page **সবচেয়ে অনেকক্ষণ ব্যবহার হয়নি**, সেটাই বের হবে।

| ধাপ | Page | Frame | Fault? | কে বের হলো |
|---|---|---|---|---|
| 1 | 7 | [7, −, −] | ✅ | — |
| 2 | 0 | [7, 0, −] | ✅ | — |
| 3 | 1 | [7, 0, 1] | ✅ | — |
| 4 | 2 | [2, 0, 1] | ✅ | **7** (সবচেয়ে আগে ব্যবহৃত) |
| 5 | 0 | [2, 0, 1] | ❌ Hit | — |
| 6 | 3 | [2, 0, 3] | ✅ | **1** (0 এইমাত্র ব্যবহার হলো) |
| 7 | 0 | [2, 0, 3] | ❌ Hit | — |
| 8 | 4 | [4, 0, 3] | ✅ | **2** |

**মোট Page Fault = 6** ⭐ (FIFO-র চেয়ে ভালো)

### ⚠️ Belady's Anomaly ⭐⭐
**FIFO-তে frame সংখ্যা বাড়ালেও page fault বেড়ে যেতে পারে!**
এটা অস্বাভাবিক ও পাল্টা-স্বজ্ঞাত — তাই MCQ-তে আসে।
⭐ **LRU ও Optimal-এ Belady's Anomaly হয় না।**

| Algorithm | নিয়ম | Belady's Anomaly? |
|---|---|---|
| **FIFO** | সবচেয়ে পুরনোটা বের | ✅ **হয়** ⚠️ |
| **LRU** | সবচেয়ে কম সাম্প্রতিক ব্যবহৃতটা বের | ❌ হয় না |
| **Optimal** | ভবিষ্যতে সবচেয়ে দেরিতে লাগবে যেটা | ❌ হয় না (তাত্ত্বিক, বাস্তবে সম্ভব নয়) |

### 🔁 Revision Box
**Paging = সমান আকার, Internal fragmentation**; **Segmentation = অসমান, External fragmentation**। **Page Fault** = চাওয়া page RAM-এ নেই। **Thrashing** = অতিরিক্ত page fault। Replacement: **FIFO** (পুরনোটা, **Belady's Anomaly হয়**), **LRU** (কম সাম্প্রতিকটা), **Optimal** (তাত্ত্বিক সেরা)।

---
---

# MODULE 6 — SYNCHRONIZATION ⭐

| Term | অর্থ |
|---|---|
| **Critical Section** | Code-এর যে অংশে shared resource ব্যবহার হয় |
| **Race Condition** | একাধিক thread একসাথে shared data বদলালে ফলাফল অনিশ্চিত হওয়া ⚠️ |
| **Mutual Exclusion** | একসাথে একজনই critical section-এ ঢুকবে |
| **Semaphore** | একটি counter, `wait()` ও `signal()` দিয়ে নিয়ন্ত্রিত |
| **Mutex** | Binary lock — একজনই ধরতে পারে, **যে lock করেছে সেই unlock করবে** |

### Semaphore vs Mutex ⭐
| | **Mutex** | **Semaphore** |
|---|---|---|
| মান | 0 বা 1 | **যেকোনো পূর্ণসংখ্যা** |
| মালিকানা | **আছে** (যে lock করে সেই unlock) | নেই (যে কেউ signal দিতে পারে) |
| কাজ | Locking | **Signaling** ও counting |

### 🔍 Race Condition-এর উদাহরণ
```
balance = 100

Thread A: balance = balance + 50    (পড়ল 100, লিখল 150)
Thread B: balance = balance + 30    (পড়ল 100, লিখল 130)

দুজনেই 100 পড়ে ফেলেছে → শেষ ফলাফল 130 বা 150
সঠিক হওয়ার কথা ছিল 180 ⚠️
```
**সমাধান:** Mutex/Semaphore দিয়ে critical section রক্ষা করা।

---
---
---

# 📋 PART B — SOFTWARE ENGINEERING

> **Q15-এর উত্তর এখানে।**

# MODULE 1 — SDLC ⭐⭐⭐

## Topic 1: সংজ্ঞা

### Definition (English)
**SDLC (Software Development Life Cycle)** is a structured process consisting of well-defined **phases** used to design, develop, test, and deliver high-quality software.

⭐ **Keywords:** Structured · Phases · Systematic

## Topic 2: ৬টি ধাপ ⭐⭐⭐

```
┌────────────────────────┐
│ 1. Requirement Analysis│  কী বানাতে হবে? SRS document তৈরি
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ 2. System Design       │  কীভাবে বানাবে? Architecture, DB design, UI
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ 3. Implementation      │  Code লেখা
│    (Coding)            │
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ 4. Testing             │  ভুল খুঁজে বের করা ও ঠিক করা
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ 5. Deployment          │  Client-এর কাছে পৌঁছানো, চালু করা
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ 6. Maintenance         │  Bug fix, update, নতুন feature
└────────────────────────┘
```

| ধাপ | কী হয় | ফলাফল (Deliverable) |
|---|---|---|
| **1. Requirement Analysis** | Client-এর চাহিদা সংগ্রহ ও বিশ্লেষণ | **SRS** (Software Requirement Specification) |
| **2. Design** | Architecture, database, UI-এর নকশা | Design document, ER diagram |
| **3. Implementation** | আসল code লেখা | Source code |
| **4. Testing** | Bug খুঁজে ঠিক করা | Test report |
| **5. Deployment** | Production-এ চালু করা | চলমান software |
| **6. Maintenance** | Bug fix, উন্নয়ন | Updated version |

⭐ **Maintenance-এ সবচেয়ে বেশি সময় ও খরচ যায়** (মোট খরচের ~60%)

## Topic 3: SDLC Models ⭐⭐

### 1️⃣ Waterfall Model
```
Requirement
    └──► Design
            └──► Implementation
                     └──► Testing
                              └──► Deployment
                                       └──► Maintenance
```
- **Sequential** — এক ধাপ শেষ না হলে পরেরটা শুরু হয় না
- **পিছনে ফেরা যায় না** ⚠️
- ✅ সহজ, নথিভুক্ত, ছোট ও স্থির প্রকল্পে ভালো
- ❌ Requirement বদলালে বিপদ, শেষে গিয়ে ভুল ধরা পড়ে

### 2️⃣ Iterative / Incremental
ছোট ছোট অংশে বানিয়ে ধাপে ধাপে বাড়ানো। প্রতিটি iteration-এ একটা কাজের সংস্করণ পাওয়া যায়।

### 3️⃣ Spiral Model
```
        ┌─ Planning
        │      ↘
   Customer      Risk Analysis
   Evaluation        ↙
        ↖ Engineering
```
- **Risk-driven** ⭐ — প্রতি চক্রে ঝুঁকি বিশ্লেষণ
- বড় ও ব্যয়বহুল প্রকল্পে ব্যবহৃত

### 4️⃣ V-Model
```
Requirement ─────────────────► Acceptance Testing
   Design ──────────────────► System Testing
     Architecture ──────────► Integration Testing
        Module Design ─────► Unit Testing
              ↘         ↙
                Coding
```
⭐ প্রতিটি development ধাপের **বিপরীতে একটি testing ধাপ** — তাই "Verification & Validation Model"

### 5️⃣ Agile / Scrum ⭐⭐
- **Iterative**, ছোট ছোট **Sprint** (২–৪ সপ্তাহ)
- প্রতিটি sprint-এ কাজের software delivery
- **Customer feedback** নিয়ে ক্রমাগত উন্নতি
- **Scrum roles:** Product Owner · Scrum Master · Development Team
- **Ceremonies:** Daily Standup · Sprint Planning · Sprint Review · Retrospective

### Waterfall vs Agile ⭐⭐⭐

| Feature | **Waterfall** | **Agile** |
|---|---|---|
| ধরন | **Sequential** | **Iterative** |
| Requirement | শুরুতেই **স্থির** | **পরিবর্তনযোগ্য** ⭐ |
| Delivery | **শেষে একবারে** | **প্রতি sprint-এ** |
| Customer যুক্ততা | শুরু ও শেষে | **সারাক্ষণ** |
| Testing | শেষে | **প্রতিটি iteration-এ** |
| Documentation | **ভারী** | হালকা |
| উপযুক্ত | ছোট, স্থির প্রকল্প | বড়, পরিবর্তনশীল প্রকল্প |
| ভুল ধরা পড়ে | দেরিতে ⚠️ | **তাড়াতাড়ি** ✅ |

### 🔁 Revision Box (Q15-এর উত্তর)
**SDLC = Software Development Life Cycle** — সুসংগঠিত ধাপে software বানানোর প্রক্রিয়া।
**৬ ধাপ:** Requirement Analysis (SRS) → Design → Implementation (Coding) → Testing → Deployment → Maintenance।
**Models:** Waterfall (sequential, পিছনে ফেরা যায় না), Iterative, Spiral (**risk-driven**), V-Model (প্রতি ধাপে testing), **Agile/Scrum** (sprint, feedback, সবচেয়ে জনপ্রিয়)।

---
---

# MODULE 2 — TESTING ⭐

## Topic 1: Black Box vs White Box ⭐⭐

| | **Black Box** | **White Box** |
|---|---|---|
| ভিতরের code | **জানা লাগে না** | **জানতে হয়** |
| দৃষ্টিভঙ্গি | Input → Output | Code-এর পথ ও শাখা |
| কে করে | **Tester** | **Developer** |
| উদাহরণ | Boundary value, Equivalence partitioning | Statement coverage, Branch coverage, Path coverage |
| আরেক নাম | Functional testing | Structural / Glass box testing |

**Grey Box** = দুটোর মাঝামাঝি (আংশিক code জ্ঞান)

## Topic 2: Testing Levels ⭐
```
┌───────────────────────────┐
│ 4. Acceptance Testing     │  ← Client যাচাই করে (UAT)
├───────────────────────────┤
│ 3. System Testing         │  ← পুরো system একসাথে
├───────────────────────────┤
│ 2. Integration Testing    │  ← module গুলো একসাথে কাজ করছে কিনা
├───────────────────────────┤
│ 1. Unit Testing           │  ← একেকটা function/module আলাদা
└───────────────────────────┘
```

## Topic 3: Verification vs Validation ⭐⭐

| | **Verification** | **Validation** |
|---|---|---|
| প্রশ্ন | **"সঠিকভাবে বানাচ্ছি?"** | **"সঠিক জিনিসটা বানাচ্ছি?"** |
| কী দেখে | Specification মানা হচ্ছে কিনা | User-এর প্রকৃত চাহিদা মিটছে কিনা |
| পদ্ধতি | Review, Walkthrough, Inspection | Actual testing |
| Code চালানো লাগে? | ❌ **না** (static) | ✅ **হ্যাঁ** (dynamic) |

⭐ **মুখস্থ:** Verification = **Are we building the product right?** · Validation = **Are we building the right product?**

## Topic 4: Requirement ও Design নীতি

**Requirement দুই ধরনের:**
| | উদাহরণ |
|---|---|
| **Functional** | "System-এ login করা যাবে", "Report তৈরি হবে" |
| **Non-functional** | Performance, Security, Usability, Scalability, Reliability |

**Cohesion vs Coupling ⭐⭐**
| | **Cohesion** | **Coupling** |
|---|---|---|
| কী | একটি module-এর ভিতরের অংশগুলো কতটা সম্পর্কিত | দুই module পরস্পরের উপর কতটা নির্ভরশীল |
| ভালো নকশা | **বেশি (High)** ✅ | **কম (Low)** ✅ |

⭐ **সোনালি নিয়ম: High Cohesion, Low Coupling**

### 🔁 Revision Box
**Black Box = code জানা লাগে না, tester করে**; **White Box = code দেখে, developer করে**। Levels: **Unit → Integration → System → Acceptance**। **Verification = সঠিকভাবে বানাচ্ছি (static, review)**; **Validation = সঠিক জিনিস বানাচ্ছি (dynamic, testing)**। **High Cohesion + Low Coupling = ভালো নকশা**।

---
---

# ★ FINAL REVISION

## 1. Sample Paper-এর উত্তর ⭐⭐⭐

**Q14. Thread ও Multithread বলতে কী বোঝায়?**
> **Thread** হলো একটি process-এর ভিতরের **ক্ষুদ্রতম execution unit**। একই process-এর thread গুলো **একই memory space, code ও file ভাগ করে নেয়**, কিন্তু প্রত্যেকের **নিজস্ব stack, register ও program counter** থাকে। এজন্য thread-কে **lightweight process** বলা হয়।
>
> **Multithreading** হলো একটি process-এর মধ্যে **একাধিক thread একসাথে (concurrently) চালানোর** ক্ষমতা। উদাহরণ: MS Word-এ একই সময়ে টাইপ করা, বানান পরীক্ষা করা ও auto-save চলা।
>
> **সুবিধা:** Responsiveness, resource sharing, কম খরচে তৈরি, এবং multi-core CPU-তে scalability।

**Q15. SDLC কী?**
> **SDLC (Software Development Life Cycle)** হলো software তৈরির একটি সুসংগঠিত প্রক্রিয়া, যা কয়েকটি নির্দিষ্ট ধাপে বিভক্ত: **Requirement Analysis → Design → Implementation (Coding) → Testing → Deployment → Maintenance**।
>
> এর উদ্দেশ্য হলো নির্ধারিত সময় ও খরচের মধ্যে **উচ্চমানের software** তৈরি করা। জনপ্রিয় SDLC model গুলোর মধ্যে রয়েছে **Waterfall, Iterative, Spiral, V-Model ও Agile**।

## 2. Top 20 MCQ Traps ⭐

1. **Program = passive (disk-এ)**, **Process = active (RAM-এ)**
2. **Thread-এ Code/Data/File shared, Stack/Register আলাদা**
3. একটা **thread crash করলে পুরো process পড়ে যায়**
4. **TAT = CT − AT**, **WT = TAT − BT**
5. **FCFS-এ Convoy Effect** হয়
6. **SJF গড় WT-তে optimal কিন্তু starvation** হয়
7. **Round Robin = Circular Queue, preemptive**
8. **Starvation-এর সমাধান = Aging**
9. **Deadlock-এর ৪ শর্ত: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait**
10. **চারটিই একসাথে লাগবে**, একটা ভাঙলেই deadlock হয় না
11. **Banker's Algorithm = Deadlock Avoidance** (prevention নয়) ⭐
12. **Paging → Internal fragmentation**, **Segmentation → External**
13. **Belady's Anomaly শুধু FIFO-তে**, LRU/Optimal-এ নয় ⭐
14. **Thrashing = অতিরিক্ত page fault**
15. **Mutex-এর মালিকানা আছে, Semaphore-এর নেই**
16. **SDLC-এর প্রথম ধাপ = Requirement Analysis** (Design নয়)
17. **Maintenance-এ সবচেয়ে বেশি খরচ**
18. **Spiral = risk-driven**, **V-Model = প্রতি ধাপে testing**
19. **Black Box = tester**, **White Box = developer**
20. **High Cohesion + Low Coupling = ভালো নকশা**

---

# ✍️ নিজে করো (উত্তর নিচে)

1. FCFS-এ P1(AT=0,BT=4), P2(AT=1,BT=3), P3(AT=2,BT=1) — গড় waiting time কত?
2. Reference string `1,2,3,4,1,2,5` এবং 3 frame — FIFO-তে কত page fault?
3. Deadlock-এর ৪ শর্তের কোনটা ভাঙলে **Hold and Wait** দূর হয়?

<details>
<summary>উত্তর</summary>

**1.**
```
Gantt: │ P1 │ P2 │P3│
       0    4    7  8

P1: CT=4, TAT=4−0=4, WT=4−4=0
P2: CT=7, TAT=7−1=6, WT=6−3=3
P3: CT=8, TAT=8−2=6, WT=6−1=5

গড় WT = (0+3+5)/3 = 2.67
```

**2.**
```
1 → [1,−,−]     Fault (1)
2 → [1,2,−]     Fault (2)
3 → [1,2,3]     Fault (3)
4 → [4,2,3]     Fault (4)  1 বের
1 → [4,1,3]     Fault (5)  2 বের
2 → [4,1,2]     Fault (6)  3 বের
5 → [5,1,2]     Fault (7)  4 বের

মোট = 7 page fault
```

**3.** Process-কে **শুরুতেই তার সব resource একসাথে চাইতে বাধ্য করা** — তাহলে সে কিছু ধরে রেখে বাকিটার জন্য অপেক্ষা করতে পারবে না।
(অসুবিধা: resource-এর অপচয় হয় ও starvation হতে পারে)

</details>
