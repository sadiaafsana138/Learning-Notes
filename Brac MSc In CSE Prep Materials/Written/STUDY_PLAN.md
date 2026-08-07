# ⏱️ STUDY PLAN — BRAC MSc CSE Admission
### ১২ ঘণ্টার কৌশল

> Topic-এর তালিকা আলাদা file-এ (`INDEX.md`)। এই file-এ শুধু **কৌশল, সময়ভাগ ও শেষ মুহূর্তের তালিকা**।

---

## 🎯 Sample Paper কী বলছে

১৫টা প্রশ্ন এসেছে মাত্র **৭টা course** থেকে —

| Q# | প্রশ্ন | Subject |
|---|---|---|
| 1 | IPv6 length + example | Networking |
| 2 | IEEE 802.11b bandwidth | Networking |
| 3 | OSI ও TCP/IP layer সংখ্যা | Networking |
| 4 | VLSM ও CIDR | Networking |
| 5 | (1011.1101)₂ → decimal | Digital Logic |
| 6 | 3.14 ÷ 2.1 remainder | Programming |
| 7 | 1.66 → 2.0 round | Programming |
| 8 | Java loop output trace | Programming |
| 9 | Platform independency | OOP |
| 10 | Primary Key / Foreign Key | Database |
| 11 | CREATE DATABASE | Database |
| 12 | CREATE TABLE | Database |
| 13 | SELECT ... WHERE | Database |
| 14 | Thread / Multithread | Operating Systems |
| 15 | SDLC | Software Engineering |
| §2 | English composition (200 words) | English |

### প্রশ্নের বণ্টন
```
Networking       ████████  4/15  (27%)
Database + SQL   ████████  4/15  (27%)
Programming+OOP  ██████    3/15  (20%)
OS + SE          ████      2/15  (13%)
Number System    ██        1/15  ( 7%)
Data Structures  ░         0/15
Algorithms       ░         0/15
ML / DL          ░         0/15
```

**সিদ্ধান্ত:** DS/Algo/ML বাদ দেবে না (অন্য বছরে আসতে পারে, viva-তেও লাগবে), কিন্তু **সময়ের সিংহভাগ Networking + SQL + Programming-এ**।

---

## 📅 ১২ ঘণ্টার ভাগ

| Slot | সময় | বিষয় | কেন |
|---|---|---|---|
| **1** | **2.5 h** | 🔴 Networking | 4/15 প্রশ্ন |
| **2** | **2.5 h** | 🔴 Database + SQL | 4/15 প্রশ্ন |
| **3** | **2.0 h** | 🔴 Programming + OOP | 3/15 প্রশ্ন |
| **4** | **1.0 h** | 🔴 Operating Systems | Thread, Deadlock |
| **5** | **0.5 h** | 🔴 Software Engineering | শুধু SDLC |
| **6** | **0.5 h** | 🔴 Number System | শুধু conversion (Q5) |
| **7** | **1.5 h** | 🟡 DS + Algo | ৩টা file-এর Revision Box |
| **8** | **0.75 h** | 🟡 ML + DL | Viva-র জন্যও দরকার |
| **9** | **0.75 h** | 🔴 English + Final Revision | Section 2 |
| | **12 h** | | |

### ⚠️ সময় বাঁচানোর জায়গা
- **Digital Logic:** শুধু binary↔decimal conversion পড়ো। Gates, K-map, Flip-flop **বাদ** (Q5-এ শুধু conversion লেগেছে)।
- **DS/Algo:** পুরো file পড়ার দরকার নেই — শুধু **Revision Box + Complexity Table + MCQ Traps**।
- **Optional subjects** (Architecture, Automata, Discrete Math): সময় বাঁচলে, নাহলে বাদ।

---

## 🚫 যা পড়বে না

| Course | কেন বাদ |
|---|---|
| CSE 250 / 251 / 350 Electronics | Admission paper-এ আসে না |
| CSE 460 VLSI · 461 Robotics | আসে না |
| CSE 423 Graphics · 428 Image Processing | আসে না |
| CSE 330 Numerical Methods | খুব কম আসে |
| CSE 424 Pattern Recognition · 429 Multimedia | আসে না |
| CSE 462 Fault Tolerance · 430 DSP | আসে না |

Catalog-এ আছে বটে, কিন্তু ১২ ঘণ্টায় এগুলোতে সময় দিলে **Networking/SQL মার খাবে**।

---

## ⚡ শেষ ২ ঘণ্টার Emergency List

সময় ফুরিয়ে গেলে **শুধু এই ২০টা** — sample paper-এর ১৫-এর মধ্যে ১৩-১৪টা কভার হয়ে যাবে।

1. **IPv6 = 128 bit** + একটা example (`2001:0db8:85a3::8a2e:0370:7334`)
2. **802.11b = 2.4 GHz, 11 Mbps**
3. **OSI = 7 layer, TCP/IP = 4 layer** + নামগুলো
4. **VLSM** = variable length subnet mask · **CIDR** = classless routing (/24)
5. **(1011.1101)₂ = 11.8125**
   - পূর্ণাংশ: 8+0+2+1 = **11**
   - ভগ্নাংশ: ½ + ¼ + 0 + 1⁄16 = **0.8125**
6. **`fmod(3.14, 2.1)`** — float-এ `%` চলে না
7. **`round(1.66) = 2.0`** / Java-তে `Math.round()`
8. **Short-circuit `&&`** — প্রথমটা false হলে দ্বিতীয়টা evaluate হয় **না**
9. **Platform independence** = Bytecode + JVM, "Write Once Run Anywhere"
10. **Primary Key** = unique + NOT NULL · **Foreign Key** = অন্য table-এর PK reference
11. `CREATE DATABASE MainRecord;`
12. `CREATE TABLE Record1 (ID INT PRIMARY KEY, Name VARCHAR(50), Age INT);`
13. `SELECT Age FROM Record1 WHERE Age = 32;`
14. **Process vs Thread** + Multithreading সংজ্ঞা
15. **SDLC ৬ ধাপ** + Waterfall vs Agile
16. **TCP vs UDP**
17. **ACID** properties
18. **1NF, 2NF, 3NF**
19. **Deadlock-এর ৪ শর্ত**
20. **English 200-word structure** (Intro → Body → Conclusion)

---

## 📁 ফাইলগুলো

| ফাইল | কী আছে |
|---|---|
| `INDEX.md` | সব topic-এর সম্পূর্ণ তালিকা (66 module) |
| `STUDY_PLAN.md` | এই file — কৌশল ও সময়ভাগ |
| `CSE_220_Data_Structures.md` | DS সম্পূর্ণ (11 module) |
| `CSE_221_Algorithms.md` | Algorithms সম্পূর্ণ (6 module) |
| `Algorithm_Steps_and_DryRun.md` | ৪০+ algorithm-এর ধাপ ও hand trace |
| `ML_DL_Basics.md` | ML/DL basics + viva প্রশ্ন |
