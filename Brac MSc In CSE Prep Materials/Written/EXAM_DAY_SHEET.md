# 🎯 EXAM DAY SHEET
### BRAC MSc CSE — পরীক্ষার সকালে শুধু এইটুকু পড়ো

> তোমার ১৪টা ফাইলে ৪৫,০০০ শব্দ। **কাল সকালে ওগুলো খুলবে না।**
> শুধু এই এক পাতা — ২০ মিনিটে পড়া যায়।

---
---

# ১. উত্তর লেখার ফরম্যাট ⭐⭐⭐

## এটা MCQ পরীক্ষা নয় — **short answer** লিখতে হবে

প্রশ্নের ভাষা লক্ষ্য করো: *"Give an example"*, *"Write the command"*, *"What do you mean by"* — সবই লিখে দেখাতে হবে।

### তিন ধরনের প্রশ্ন, তিন ধরনের উত্তর

**ধরন ১ — সরাসরি তথ্য** (*"What is the length of an IPv6 address?"*)
```
✅ সঠিক:
   IPv6 is 128 bits long.
   Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

❌ ভুল: শুধু "128" লেখা (example চেয়েছে, দাওনি)
❌ ভুল: IPv6-এর ইতিহাস নিয়ে ৫ লাইন (সময় নষ্ট)
```
➡️ **উত্তর + যা চেয়েছে ঠিক তাই। এক-দুই লাইন।**

---

**ধরন ২ — সংজ্ঞা** (*"What do you mean by VLSM and CIDR?"*)
```
✅ সঠিক গঠন:  সংজ্ঞা এক বাক্যে  →  কেন দরকার এক বাক্যে

VLSM (Variable Length Subnet Mask) allows subnets of different
sizes within the same network, so each department receives only
as many addresses as it actually needs.

CIDR (Classless Inter-Domain Routing) removes fixed class
boundaries and allows any subnet mask length, written as /24
or /26. It reduces IP wastage and allows route aggregation.
```
➡️ **পূর্ণরূপ লিখো** (VLSM/CIDR/SDLC/ACID — সব ক্ষেত্রেই)। দুটো term আলাদা করে লিখো, একসাথে গুলিয়ে নয়।

---

**ধরন ৩ — কোড/কমান্ড** (*"Write SQL command to…"*)
```
✅ সঠিক:
   CREATE DATABASE MainRecord;

❌ ভুল: semicolon বাদ দেওয়া
❌ ভুল: ব্যাখ্যা লেখা — শুধু command চেয়েছে
```
➡️ **হুবহু syntax। Semicolon দাও। বানান ঠিক রাখো।**

---

## ⭐ সোনালি নিয়ম

| | |
|---|---|
| **প্রতিটি উত্তর** | ১–৩ বাক্য (সংজ্ঞা প্রশ্নে ৩–৪) |
| **Abbreviation** | সবসময় পূর্ণরূপ খুলে লিখো |
| **"Give an example"** | example না দিলে **অর্ধেক নম্বর** |
| **জানো না?** | **খালি রেখো না।** যা জানো লিখো — আংশিক নম্বর আছে |
| **সময়** | ১৫ প্রশ্ন × ~২.৫ মিনিট = ৪০ মিনিট, প্রবন্ধে ২০ মিনিট |

---
---

# ২. পরীক্ষার হলের কৌশল

```
মিনিট 0–2     পুরো প্রশ্নপত্র একবার চোখ বুলাও, মোট সময় দেখো
মিনিট 2–25    যেগুলো নিশ্চিত জানো — সেগুলো আগে করো (ক্রম মানার দরকার নেই)
মিনিট 25–40   বাকিগুলো, আংশিক হলেও লিখো
মিনিট 40–60   English প্রবন্ধ (এটা রেখে দিও না — পুরো section)
শেষ 3 মিনিট   কোনো প্রশ্ন খালি আছে কিনা দেখো
```

> ⚠️ **সবচেয়ে বড় ভুল যেটা মানুষ করে:** কঠিন প্রশ্নে আটকে থেকে সময় শেষ করে ফেলা, তারপর English প্রবন্ধ লেখার সময় না পাওয়া।
> **প্রবন্ধটা পুরো একটা section — ওটা কখনো বাদ যাবে না।**

---
---

# ৩. Sample Paper-এর ১৫টা প্রশ্নের তৈরি উত্তর ⭐⭐⭐

**Q1.** IPv6 is **128 bits** long, written as eight groups of four hexadecimal digits separated by colons.
Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

**Q2.** IEEE **802.11b** operating in the 2.4 GHz band provides a maximum bandwidth of **11 Mbps**.

**Q3.** The **OSI** model has **7 layers**; the **TCP/IP** model has **4 layers**.
OSI: Application, Presentation, Session, Transport, Network, Data Link, Physical.
TCP/IP: Application, Transport, Internet, Network Access.

**Q4.** **VLSM** — different-sized subnets within one network, so each gets only what it needs.
**CIDR** — classless addressing using /notation (e.g. /26), reduces IP wastage and enables route aggregation.

**Q5.** `(1011.1101)₂`
Integer: 8 + 0 + 2 + 1 = **11**
Fraction: 0.5 + 0.25 + 0 + 0.0625 = **0.8125**
**Answer = 11.8125**

**Q6.** `fmod(3.14, 2.1)` *(C — `%` does not work on floats)*
Java: `3.14 % 2.1`

**Q7.** `round(1.66)` → returns **2.0**
Java: `Math.round(1.66)`

**Q8.** Output: ` 0 6 1 7 2 8 3 9`
*(শেষ iteration-এ `i` 3 হয়ে যায় → `(i<3)` false → `&&` short-circuit → `j++` চলে না, তাই j 9-তেই থামে)*

**Q9.** Java source compiles to **bytecode**, which any **JVM** can execute. The bytecode is platform-independent while the JVM is platform-dependent — **"Write Once, Run Anywhere."**

**Q10.** **Primary Key** — uniquely identifies each row; must be **unique and NOT NULL**; only one per table.
**Foreign Key** — references another table's primary key to create a relationship; can be NULL or duplicate; multiple allowed per table.

**Q11.** `CREATE DATABASE MainRecord;`

**Q12.**
```sql
USE MainRecord;
CREATE TABLE Record1 (
    ID   INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age  INT
);
```

**Q13.** `SELECT Age FROM Record1 WHERE Age = 32;`

**Q14.** A **process** is a program in execution with its own memory space. A **thread** is a lightweight unit of execution inside a process; threads of the same process share memory. **Multithreading** means running multiple threads concurrently within one process, improving responsiveness and resource use.

**Q15.** **SDLC** (Software Development Life Cycle) is the structured process of building software through six phases: **Requirement Analysis → Design → Implementation → Testing → Deployment → Maintenance**. Common models include Waterfall, Agile, Spiral and V-Model.

---
---

# ৪. যদি অন্য প্রশ্ন আসে — ৩০টি নিশ্চিত তথ্য

## Networking
1. OSI **7**, TCP/IP **4** · PDU: Data → Segment → Packet → Frame → Bit
2. **Hub = L1, Switch = L2, Router = L3**
3. IPv4 = 32 bit · **MAC = 48 bit** · Port = 16 bit (65,536টি)
4. Class A **1–126**, B **128–191**, C **192–223** · **127 = loopback**
5. Private: **10.x · 172.16–31.x · 192.168.x**
6. Host = **2ⁿ − 2** · Block size = **256 − mask octet**
7. **/26 = 62 host · /27 = 30 · /28 = 14 · /30 = 2**
8. **TCP = 20 byte header, নির্ভরযোগ্য** · **UDP = 8 byte, দ্রুত** (DNS, DHCP)
9. Handshake: **SYN → SYN-ACK → ACK**
10. Port: 21 FTP · 22 SSH · 25 SMTP · **53 DNS** · 80 HTTP · **443 HTTPS**
11. **802.3 Ethernet · 802.11 Wi-Fi · 802.15 Bluetooth**
12. **ARP = IP→MAC** · **DHCP = DORA**

## Database
13. **TRUNCATE = DDL**, DELETE = DML · DELETE-এ WHERE চলে, TRUNCATE-এ নয়
14. **WHERE = GROUP BY-এর আগে, HAVING = পরে**
15. চলার ক্রম: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**
16. **1NF = atomic · 2NF = partial বাদ · 3NF = transitive বাদ**
17. **ACID** = Atomicity, Consistency, Isolation, Durability
18. **INNER = শুধু মিল · LEFT = বামের সব**

## Programming
19. **`%` float-এ চলে না** → `fmod()`
20. **`i++` = আগে ব্যবহার পরে বাড়ে** · `++i` = আগে বাড়ে
21. **`&&` short-circuit** — প্রথমটা false হলে দ্বিতীয়টা চলেই না
22. **Overloading = compile-time**, **Overriding = run-time**
23. **JDK ⊃ JRE ⊃ JVM**

## OS / SE
24. **Process আলাদা memory, Thread শেয়ার করে**
25. Deadlock ৪ শর্ত: **Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait**
26. **Round Robin = Circular Queue** · FCFS = Queue
27. **Verification = "ঠিকভাবে বানাচ্ছি?"** · **Validation = "ঠিক জিনিস বানাচ্ছি?"**

## DS / Algo
28. **BST-এর Inorder = sorted** · **Build Heap = O(n)**
29. **BFS = Queue · DFS = Stack** · দুটোই O(V+E)
30. **Merge/Heap = O(n log n) সবসময়** · **Quick worst = O(n²)** · **Selection best-ও O(n²)**

---
---

# ৫. English প্রবন্ধ — ৫টা কথা

```
১. শুরুতেই একটা পক্ষ নাও (দুই দিকই ভালো — এটা লিখো না)
২. পাঁচ ধাপ: Stance → Reason 1 → Reason 2 → Counter-point → Conclusion
৩. "Some argue that… However…" — এই অনুচ্ছেদটাই নম্বর আনে
৪. প্রতিটি যুক্তির সাথে একটা বাংলাদেশি উদাহরণ (bKash, ঢাকার যানজট, পোশাককর্মী)
৫. ১৮৫–১৯৫ শব্দে থামো। Contraction লিখো না (don't → do not)
```

---
---

# ৬. আজ রাতে ও কাল সকালে

## আজ রাতে
- [ ] **সব নোট পড়ার চেষ্টা করো না** — শুধু এই sheet + দুটো দুর্বল বিষয়ের Revision Box
- [ ] Subnetting-এর **একটা** সমস্যা হাতে করো (`192.168.1.100/26`)
- [ ] SQL তিনটা command **হাতে লিখে ফেলো** — টাইপ করে নয়, কলম দিয়ে
- [ ] **অন্তত ৬ ঘণ্টা ঘুমাও।** নির্ঘুম রাতে মুখস্থ করা জিনিস পরীক্ষার হলে মনে পড়ে না — এটা প্রমাণিত

## কাল সকালে
- [ ] এই sheet-টা একবার পড়ো (২০ মিনিট)
- [ ] নতুন কিছু পড়ো না — উদ্বেগ বাড়ে, লাভ হয় না
- [ ] কলম ২টা, প্রবেশপত্র, পরিচয়পত্র, ক্যালকুলেটর (অনুমতি থাকলে)
- [ ] হলে ঢুকে **প্রথমেই মোট সময় দেখে নাও**, তারপর ভাগ করো

---

> **শেষ কথা:** ১৫টা প্রশ্নের ১৩টা তোমার নোটে সরাসরি আছে। প্রস্তুতি হয়েছে।
> এখন দরকার শান্ত মাথা আর সময়ের সঠিক ভাগ — নতুন কোনো তথ্য নয়।
