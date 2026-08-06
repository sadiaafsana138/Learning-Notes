# 🗄️ DATABASE SYSTEMS & SQL — সম্পূর্ণ নোট
### CSE 370 — BRAC MSc CSE Admission

> **Sample paper-এ ৪টা প্রশ্ন এখান থেকে** (Q10 Key, Q11 CREATE DATABASE, Q12 CREATE TABLE, Q13 SELECT)।
> Networking-এর সমান ওজন — **২.৫ ঘণ্টা** দাও।

---

## 📑 সূচি
| Module | বিষয় | Dry Run |
|---|---|---|
| 1 | DBMS Basics · Architecture | — |
| 2 | **Relational Model & Keys** ⭐ | ✅ |
| 3 | **SQL — সব command** ⭐⭐⭐ | ✅ |
| 4 | **JOIN** ⭐⭐ | ✅ |
| 5 | **Normalization (1NF→2NF→3NF)** ⭐⭐⭐ | ✅ |
| 6 | ER Model | ✅ |
| 7 | Transaction · ACID · Index | — |
| 8 | Final Revision + Traps | — |

---
---

# MODULE 1 — DBMS BASICS

## Topic 1: DBMS

### Definition (English)
A **DBMS (Database Management System)** is software that allows users to **define, create, store, retrieve, and manage** data in a database efficiently and securely.

⭐ **Keywords:** Software · Store · Retrieve · Manage · Security

### DBMS vs File System ⭐

| Feature | **File System** | **DBMS** |
|---|---|---|
| Redundancy | **বেশি** (একই data বহু জায়গায়) | **কম** (normalization) |
| Consistency | সমস্যা হয় | বজায় থাকে |
| Security | দুর্বল | **শক্তিশালী** (user permission) |
| Concurrent access | সমস্যা | **নিয়ন্ত্রিত** |
| Backup/Recovery | manual | **স্বয়ংক্রিয়** |
| Query | কঠিন | **SQL দিয়ে সহজ** |

## Topic 2: 3-Level Architecture (ANSI-SPARC) ⭐

```
┌────────────────────────────────────┐
│  External Level (View)              │  ← প্রতিটি user যা দেখে
│  "Student শুধু নিজের result দেখে"    │
├────────────────────────────────────┤
│  Conceptual Level (Logical)         │  ← পুরো database-এর গঠন
│  "কী কী table, কী সম্পর্ক"           │
├────────────────────────────────────┤
│  Internal Level (Physical)          │  ← কীভাবে disk-এ রাখা
│  "B+ Tree index, file organization"  │
└────────────────────────────────────┘
```

**Data Independence ⭐**
- **Logical Data Independence** — Conceptual বদলালেও External অপরিবর্তিত (যেমন নতুন column যোগ করলেও পুরনো view কাজ করে)
- **Physical Data Independence** — Internal বদলালেও Conceptual অপরিবর্তিত (index বদলালেও query একই থাকে)

## Topic 3: SQL Command-এর ধরন ⭐⭐⭐

| ধরন | পূর্ণরূপ | Command |
|---|---|---|
| **DDL** | Data **Definition** Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data **Manipulation** Language | `INSERT`, `UPDATE`, `DELETE`, `SELECT`* |
| **DCL** | Data **Control** Language | `GRANT`, `REVOKE` |
| **TCL** | **Transaction** Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

\* কিছু বইয়ে `SELECT` কে আলাদা **DQL** (Data Query Language) বলা হয়।

⚠️ **MCQ trap:** `TRUNCATE` = **DDL** (DML নয়) কারণ এটা structure-level কাজ ও **rollback করা যায় না**।

### 🔁 Revision Box
DBMS = data define/store/retrieve/manage করার software। **File System-এর চেয়ে ভালো:** কম redundancy, ভালো security, concurrent access। **3-level: External (view) → Conceptual (logical) → Internal (physical)**। **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = INSERT/UPDATE/DELETE/SELECT**, **DCL = GRANT/REVOKE**, **TCL = COMMIT/ROLLBACK**।

---
---

# MODULE 2 — RELATIONAL MODEL & KEYS ⭐⭐⭐

> **Sample paper Q10 এখান থেকে।**

## Topic 1: মৌলিক পরিভাষা

```
Table নাম: Student  (একে বলে RELATION)

┌────────┬──────────┬──────┬───────┐
│ Std_ID │ Name     │ Dept │ CGPA  │   ← Attribute (Column)
├────────┼──────────┼──────┼───────┤
│ 101    │ Rahim    │ CSE  │ 3.75  │   ← Tuple (Row / Record)
│ 102    │ Karim    │ EEE  │ 3.50  │
│ 103    │ Sadia    │ CSE  │ 3.90  │
└────────┴──────────┴──────┴───────┘
```

| Term | অর্থ | উপরের উদাহরণে |
|---|---|---|
| **Relation** | Table | Student |
| **Tuple** | Row / Record | (101, Rahim, CSE, 3.75) |
| **Attribute** | Column | Std_ID, Name, Dept, CGPA |
| **Domain** | কোনো attribute-এর সম্ভাব্য মানের সেট | CGPA: 0.00–4.00 |
| **Degree** | **Column সংখ্যা** | **4** |
| **Cardinality** | **Row সংখ্যা** | **3** |

⚠️ **Trap:** **Degree = column**, **Cardinality = row** — উল্টো করে ফেলা খুব সাধারণ ভুল ⭐

## Topic 2: Keys ⭐⭐⭐

### Definitions

| Key | Definition (English) |
|---|---|
| **Super Key** | Any set of attributes that **uniquely identifies** a tuple. |
| **Candidate Key** | A **minimal** super key (কোনো attribute বাদ দিলে আর unique থাকে না)। |
| **Primary Key** | The candidate key **chosen** to identify tuples. Must be **UNIQUE + NOT NULL**. |
| **Alternate Key** | Candidate keys that were **not chosen** as primary key. |
| **Composite Key** | A primary key made of **two or more attributes**. |
| **Foreign Key** | An attribute that **references the primary key** of another table. |

### 🔍 DRY RUN — কোনটা কোন Key?

```
Table: Student
┌────────┬──────────┬──────────────┬────────┐
│ Std_ID │ Email    │ NID          │ Name   │
├────────┼──────────┼──────────────┼────────┤
│ 101    │ a@x.com  │ 1990123456   │ Rahim  │
│ 102    │ b@x.com  │ 1990654321   │ Karim  │
└────────┴──────────┴──────────────┴────────┘
```

| Key | কোনগুলো | কেন |
|---|---|---|
| **Super Key** | {Std_ID}, {Email}, {NID}, {Std_ID, Name}, {Email, Name}... | প্রত্যেকটাই unique চিহ্নিত করতে পারে |
| **Candidate Key** | **{Std_ID}, {Email}, {NID}** | minimal — একটা attribute-ই যথেষ্ট |
| **Primary Key** | **Std_ID** (আমরা বেছে নিলাম) | একটাই বাছা যায় |
| **Alternate Key** | **Email, NID** | Candidate ছিল কিন্তু বাছা হয়নি |

⚠️ `{Std_ID, Name}` **super key কিন্তু candidate key নয়** — কারণ Name বাদ দিলেও Std_ID একাই যথেষ্ট, তাই এটা minimal নয়।

## Topic 3: Primary Key vs Foreign Key ⭐⭐⭐ (Q10-এর উত্তর)

```
Table: Department (Parent)          Table: Student (Child)
┌─────────┬──────────┐              ┌────────┬────────┬──────────┐
│ Dept_ID │ Name     │              │ Std_ID │ Name   │ Dept_ID  │
│  (PK)   │          │              │  (PK)  │        │  (FK)    │
├─────────┼──────────┤              ├────────┼────────┼──────────┤
│ D01     │ CSE      │◄─────────────│ 101    │ Rahim  │ D01      │
│ D02     │ EEE      │◄─────────────│ 102    │ Karim  │ D02      │
└─────────┴──────────┘              │ 103    │ Sadia  │ D01      │
                                    └────────┴────────┴──────────┘
                                    Dept_ID এখানে FK — Department-এর PK-কে দেখাচ্ছে
```

| Feature | **Primary Key** | **Foreign Key** |
|---|---|---|
| কাজ | **Row কে unique চিহ্নিত** করে | **দুই table-এর সম্পর্ক** তৈরি করে |
| NULL | ❌ **হতে পারে না** | ✅ হতে পারে |
| Duplicate | ❌ হতে পারে না | ✅ হতে পারে |
| প্রতি table-এ | **একটাই** | **একাধিক** থাকতে পারে |
| কোথায় থাকে | নিজের table-এ | অন্য table-এর PK-কে reference করে |

### Integrity Constraints ⭐
- **Entity Integrity** — Primary key কখনো **NULL** হতে পারে না
- **Referential Integrity** — Foreign key-এর মান হয় **NULL**, নয়তো parent table-এ **অবশ্যই থাকতে হবে**
- **Domain Integrity** — Attribute-এর মান তার domain-এর ভিতরে থাকতে হবে

### 🔁 Revision Box
**Degree = column সংখ্যা**, **Cardinality = row সংখ্যা**। **Super Key ⊃ Candidate Key ⊃ Primary Key**। **Primary Key** = unique + NOT NULL, table-এ একটাই। **Foreign Key** = অন্য table-এর PK reference করে, NULL ও duplicate হতে পারে, একাধিক থাকতে পারে। **Entity Integrity = PK NULL নয়**, **Referential Integrity = FK-এর মান parent-এ থাকতে হবে**।

---
---

# MODULE 3 — SQL ⭐⭐⭐

> **Q11, Q12, Q13 এখান থেকে সরাসরি।** এই module হাতে লিখে practice করো।

## Topic 1: Database ও Table তৈরি

### 🔍 Q11-এর উত্তর — Database তৈরি
```sql
CREATE DATABASE MainRecord;
```
ব্যবহার শুরু করতে:
```sql
USE MainRecord;
```

### 🔍 Q12-এর উত্তর — Table তৈরি
```sql
CREATE TABLE Record1 (
    ID      INT          PRIMARY KEY,
    Name    VARCHAR(50)  NOT NULL,
    Age     INT,
    Email   VARCHAR(100) UNIQUE,
    Dept_ID VARCHAR(10),
    FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);
```

⭐ পরীক্ষায় এত বড় না লিখলেও চলবে। **সংক্ষিপ্ত গ্রহণযোগ্য উত্তর:**
```sql
CREATE TABLE Record1 (
    ID   INT PRIMARY KEY,
    Name VARCHAR(50),
    Age  INT
);
```

### 🔍 Q13-এর উত্তর — নির্দিষ্ট শর্তে row বের করা
```sql
SELECT Age FROM Record1 WHERE Age = 32;
```
পুরো row চাইলে:
```sql
SELECT * FROM Record1 WHERE Age = 32;
```

## Topic 2: Data Types ⭐

| Type | কী রাখে |
|---|---|
| `INT` | পূর্ণসংখ্যা |
| `FLOAT` / `DECIMAL(p,s)` | দশমিক |
| `CHAR(n)` | **স্থির** দৈর্ঘ্যের text |
| `VARCHAR(n)` | **পরিবর্তনশীল** দৈর্ঘ্যের text ⭐ |
| `DATE` / `DATETIME` | তারিখ / সময় |
| `BOOLEAN` | TRUE / FALSE |

⭐ **CHAR vs VARCHAR:** `CHAR(10)`-এ "abc" রাখলেও ১০ byte লাগে; `VARCHAR(10)`-এ মাত্র ৩ (+overhead)।

## Topic 3: Constraints ⭐

| Constraint | কাজ |
|---|---|
| `PRIMARY KEY` | Unique + NOT NULL |
| `FOREIGN KEY` | অন্য table-এর PK reference |
| `NOT NULL` | খালি রাখা যাবে না |
| `UNIQUE` | পুনরাবৃত্তি হবে না (কিন্তু NULL চলতে পারে) |
| `CHECK` | শর্ত মানতে হবে — `CHECK (Age >= 18)` |
| `DEFAULT` | কিছু না দিলে ডিফল্ট মান |
| `AUTO_INCREMENT` | নিজে নিজে ১ করে বাড়ে |

## Topic 4: প্রধান Command গুলো

```sql
-- ঢোকানো
INSERT INTO Record1 (ID, Name, Age) VALUES (1, 'Rahim', 32);
INSERT INTO Record1 VALUES (2, 'Karim', 25);

-- পড়া
SELECT * FROM Record1;
SELECT Name, Age FROM Record1;
SELECT DISTINCT Dept FROM Student;              -- পুনরাবৃত্তি বাদ
SELECT * FROM Record1 WHERE Age > 25;
SELECT * FROM Record1 WHERE Age BETWEEN 20 AND 30;
SELECT * FROM Record1 WHERE Name LIKE 'R%';     -- R দিয়ে শুরু
SELECT * FROM Record1 WHERE Dept IN ('CSE','EEE');
SELECT * FROM Record1 WHERE Email IS NULL;
SELECT * FROM Record1 ORDER BY Age DESC;
SELECT * FROM Record1 LIMIT 5;

-- বদলানো
UPDATE Record1 SET Age = 33 WHERE ID = 1;

-- মোছা
DELETE FROM Record1 WHERE ID = 2;

-- Structure বদলানো
ALTER TABLE Record1 ADD Email VARCHAR(100);
ALTER TABLE Record1 DROP COLUMN Email;
ALTER TABLE Record1 MODIFY Age FLOAT;

-- মুছে ফেলা
TRUNCATE TABLE Record1;    -- সব row, structure থাকবে
DROP TABLE Record1;        -- table-ই উধাও
```

### ⚠️ DELETE vs TRUNCATE vs DROP ⭐⭐⭐

| | **DELETE** | **TRUNCATE** | **DROP** |
|---|---|---|---|
| ধরন | **DML** | **DDL** | **DDL** |
| কী মোছে | নির্দিষ্ট row (WHERE) | **সব row** | **পুরো table** |
| Structure | থাকে | **থাকে** | **থাকে না** |
| Rollback | ✅ **সম্ভব** | ❌ সম্ভব নয় | ❌ সম্ভব নয় |
| গতি | ধীর | **দ্রুত** | দ্রুত |
| WHERE | ✅ ব্যবহার করা যায় | ❌ যায় না | ❌ যায় না |

## Topic 5: Aggregate Functions ও GROUP BY ⭐

```sql
SELECT COUNT(*) FROM Student;
SELECT AVG(CGPA) FROM Student;
SELECT MAX(CGPA), MIN(CGPA), SUM(CGPA) FROM Student;

-- বিভাগভিত্তিক গড়
SELECT Dept, AVG(CGPA)
FROM Student
GROUP BY Dept;

-- যেসব বিভাগে ২ জনের বেশি
SELECT Dept, COUNT(*)
FROM Student
GROUP BY Dept
HAVING COUNT(*) > 2;
```

### ⚠️ WHERE vs HAVING ⭐⭐⭐

| | **WHERE** | **HAVING** |
|---|---|---|
| কখন কাজ করে | **GROUP BY-এর আগে** | **GROUP BY-এর পরে** |
| কীসের উপর | **প্রতিটি row** | **প্রতিটি group** |
| Aggregate ব্যবহার | ❌ করা যায় না | ✅ করা যায় |

### SQL Execution Order ⭐ (লেখার ক্রম ≠ চলার ক্রম)
```
লেখার ক্রম:  SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY

চলার ক্রম:   FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```
⭐ এজন্যই `WHERE`-এ aggregate ব্যবহার করা যায় না — তখনো group তৈরিই হয়নি।

### 🔁 Revision Box
`CREATE DATABASE name;` · `CREATE TABLE t (col type constraint);` · `SELECT col FROM t WHERE cond;`
**DELETE = DML, rollback হয়, WHERE চলে**; **TRUNCATE = DDL, সব row, দ্রুত**; **DROP = table-ই মুছে যায়**।
**WHERE = row-এর উপর, GROUP BY-এর আগে**; **HAVING = group-এর উপর, পরে**। চলার ক্রম: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**।

---
---

# MODULE 4 — JOIN ⭐⭐⭐

## 🔍 DRY RUN — চার ধরনের JOIN

**দুটো table:**
```
Student                          Department
┌────┬────────┬─────────┐        ┌─────────┬────────┐
│ ID │ Name   │ Dept_ID │        │ Dept_ID │ Dname  │
├────┼────────┼─────────┤        ├─────────┼────────┤
│ 1  │ Rahim  │ D01     │        │ D01     │ CSE    │
│ 2  │ Karim  │ D02     │        │ D02     │ EEE    │
│ 3  │ Sadia  │ NULL    │        │ D03     │ BBA    │
└────┴────────┴─────────┘        └─────────┴────────┘
                                  (D03-এ কোনো student নেই)
                                  (Sadia-র কোনো dept নেই)
```

### 1️⃣ INNER JOIN — দুই দিকেই মিল আছে এমন
```sql
SELECT s.Name, d.Dname
FROM Student s
INNER JOIN Department d ON s.Dept_ID = d.Dept_ID;
```
**ফলাফল:**
```
┌────────┬───────┐
│ Rahim  │ CSE   │
│ Karim  │ EEE   │
└────────┴───────┘
```
⭐ Sadia নেই (Dept_ID NULL), BBA নেই (কোনো student নেই)

### 2️⃣ LEFT JOIN — বাম table-এর সব
```sql
SELECT s.Name, d.Dname
FROM Student s
LEFT JOIN Department d ON s.Dept_ID = d.Dept_ID;
```
**ফলাফল:**
```
┌────────┬───────┐
│ Rahim  │ CSE   │
│ Karim  │ EEE   │
│ Sadia  │ NULL  │   ← Student-এর সব থাকবে, মিল না থাকলে NULL
└────────┴───────┘
```

### 3️⃣ RIGHT JOIN — ডান table-এর সব
```sql
SELECT s.Name, d.Dname
FROM Student s
RIGHT JOIN Department d ON s.Dept_ID = d.Dept_ID;
```
**ফলাফল:**
```
┌────────┬───────┐
│ Rahim  │ CSE   │
│ Karim  │ EEE   │
│ NULL   │ BBA   │   ← Department-এর সব থাকবে
└────────┴───────┘
```

### 4️⃣ FULL OUTER JOIN — দুই দিকেরই সব
```
┌────────┬───────┐
│ Rahim  │ CSE   │
│ Karim  │ EEE   │
│ Sadia  │ NULL  │
│ NULL   │ BBA   │
└────────┴───────┘
```
⚠️ MySQL-এ `FULL OUTER JOIN` নেই — `LEFT UNION RIGHT` দিয়ে করতে হয়।

### ছবি দিয়ে বোঝা
```
INNER JOIN        LEFT JOIN         RIGHT JOIN        FULL JOIN
  ( ●●● )           (███●●● )         ( ●●●███)        (███●●●███)
   A ∩ B             A সব              B সব             A ∪ B
```

### অন্য দুটি
- **CROSS JOIN** — সব row × সব row (Cartesian product)। m×n row তৈরি হয় ⚠️
- **SELF JOIN** — একই table নিজের সাথে (যেমন Employee → Manager)

### 🔁 Revision Box
**INNER = দুই দিকে মিল**, **LEFT = বাম-এর সব + মিল**, **RIGHT = ডান-এর সব + মিল**, **FULL = দুই দিকেরই সব**। মিল না থাকলে **NULL** বসে। **CROSS JOIN = m × n row**। MySQL-এ FULL OUTER নেই।

---
---

# MODULE 5 — NORMALIZATION ⭐⭐⭐

## Topic 1: কেন দরকার?

### তিন Anomaly ⭐
| Anomaly | সমস্যা |
|---|---|
| **Insert Anomaly** | নতুন Department যোগ করতে চাইলে একটা Student লাগে (নাহলে row-ই বসানো যায় না) |
| **Update Anomaly** | Department-এর নাম বদলাতে **বহু row** বদলাতে হয়; একটা মিস হলে অসঙ্গতি |
| **Delete Anomaly** | শেষ Student মুছলে Department-এর তথ্যও হারিয়ে যায় |

**Functional Dependency (FD):** `A → B` মানে A জানলে B নির্দিষ্টভাবে জানা যায়।
*উদাহরণ:* `Std_ID → Name` (ID জানলে নাম জানা যায়)

## 🔍 DRY RUN — সম্পূর্ণ Normalization

### ধাপ 0: Unnormalized Table (UNF)
```
┌────────┬────────┬──────────────────┬─────────┬──────────┐
│ Std_ID │ Name   │ Courses          │ Dept_ID │ Dept_Name│
├────────┼────────┼──────────────────┼─────────┼──────────┤
│ 101    │ Rahim  │ CSE220, CSE221   │ D01     │ CSE      │
│ 102    │ Karim  │ EEE101           │ D02     │ EEE      │
└────────┴────────┴──────────────────┴─────────┴──────────┘
```
⚠️ সমস্যা: `Courses` column-এ **একাধিক মান** — atomic নয়।

---

### ধাপ 1: 1NF — Atomic value

**নিয়ম:** প্রতিটি cell-এ **একটিমাত্র মান**, কোনো repeating group নেই।

```
┌────────┬────────┬─────────┬─────────┬──────────┐
│ Std_ID │ Name   │ Course  │ Dept_ID │ Dept_Name│
├────────┼────────┼─────────┼─────────┼──────────┤
│ 101    │ Rahim  │ CSE220  │ D01     │ CSE      │
│ 101    │ Rahim  │ CSE221  │ D01     │ CSE      │  ← ভাঙা হলো
│ 102    │ Karim  │ EEE101  │ D02     │ EEE      │
└────────┴────────┴─────────┴─────────┴──────────┘

Primary Key = {Std_ID, Course}  ← Composite Key
```
✅ এখন 1NF। ⚠️ কিন্তু Rahim-এর নাম দুইবার লেখা হচ্ছে।

---

### ধাপ 2: 2NF — Partial Dependency দূর করা

**নিয়ম:** 1NF + **composite key-এর অংশবিশেষের উপর কোনো non-key attribute নির্ভর করবে না**।

**সমস্যা খুঁজি:**
```
PK = {Std_ID, Course}

Name       ← শুধু Std_ID-র উপর নির্ভর    ⚠️ Partial Dependency
Dept_ID    ← শুধু Std_ID-র উপর নির্ভর    ⚠️ Partial Dependency
Dept_Name  ← শুধু Std_ID-র উপর নির্ভর    ⚠️ Partial Dependency
```

**ভাগ করি:**
```
Table: Student                          Table: Enrollment
┌────────┬────────┬─────────┬──────────┐  ┌────────┬─────────┐
│ Std_ID │ Name   │ Dept_ID │ Dept_Name│  │ Std_ID │ Course  │
│  (PK)  │        │         │          │  │  (PK,FK)│ (PK)   │
├────────┼────────┼─────────┼──────────┤  ├────────┼─────────┤
│ 101    │ Rahim  │ D01     │ CSE      │  │ 101    │ CSE220  │
│ 102    │ Karim  │ D02     │ EEE      │  │ 101    │ CSE221  │
└────────┴────────┴─────────┴──────────┘  │ 102    │ EEE101  │
                                           └────────┴─────────┘
```
✅ এখন 2NF। ⚠️ কিন্তু Dept_Name এখনো Dept_ID-র উপর নির্ভরশীল।

---

### ধাপ 3: 3NF — Transitive Dependency দূর করা

**নিয়ম:** 2NF + **কোনো non-key attribute অন্য non-key attribute-এর উপর নির্ভর করবে না**।

**সমস্যা খুঁজি:**
```
Std_ID → Dept_ID → Dept_Name

অর্থাৎ Dept_Name পরোক্ষভাবে Std_ID-র উপর নির্ভরশীল
⚠️ এটাই Transitive Dependency
```

**ভাগ করি:**
```
Table: Student              Table: Department        Table: Enrollment
┌────────┬───────┬────────┐  ┌─────────┬──────────┐  ┌────────┬─────────┐
│ Std_ID │ Name  │Dept_ID │  │ Dept_ID │ Dept_Name│  │ Std_ID │ Course  │
│  (PK)  │       │ (FK)   │  │  (PK)   │          │  │        │         │
├────────┼───────┼────────┤  ├─────────┼──────────┤  ├────────┼─────────┤
│ 101    │ Rahim │ D01    │  │ D01     │ CSE      │  │ 101    │ CSE220  │
│ 102    │ Karim │ D02    │  │ D02     │ EEE      │  │ 101    │ CSE221  │
└────────┴───────┴────────┘  └─────────┴──────────┘  │ 102    │ EEE101  │
                                                      └────────┴─────────┘
```
✅ **এটাই 3NF** — তিনটা anomaly-ই দূর হলো।

---

### ধাপ 4: BCNF (সংক্ষেপে)
**নিয়ম:** 3NF + প্রতিটি **determinant** (যার উপর নির্ভরশীল) অবশ্যই একটি **candidate key** হতে হবে।
3NF-এর চেয়ে কড়া, তবে ব্যতিক্রমী ক্ষেত্রেই দরকার হয়।

## ★ Normalization Summary Table ⭐⭐⭐

| Form | শর্ত | কী দূর করে |
|---|---|---|
| **1NF** | Atomic value, repeating group নেই | Multi-valued attribute |
| **2NF** | 1NF + **Partial dependency নেই** | Composite key-এর অংশের উপর নির্ভরতা |
| **3NF** | 2NF + **Transitive dependency নেই** | Non-key → non-key নির্ভরতা |
| **BCNF** | 3NF + প্রতিটি determinant candidate key | 3NF-এর ব্যতিক্রম |

⭐ **এক লাইনে মুখস্থ:**
> **1NF = Atomic · 2NF = No Partial · 3NF = No Transitive · BCNF = Determinant is Key**

### ⚠️ Denormalization
পড়ার গতি বাড়াতে ইচ্ছাকৃতভাবে redundancy ফিরিয়ে আনা। **Read-heavy** system-এ (যেমন reporting) ব্যবহৃত।

### 🔁 Revision Box
Normalization = redundancy কমানো ও **Insert/Update/Delete anomaly** দূর করা। **1NF = atomic value**, **2NF = partial dependency নেই** (composite key-এর অংশের উপর নির্ভরতা), **3NF = transitive dependency নেই** (non-key → non-key), **BCNF = প্রতিটি determinant candidate key**।

---
---

# MODULE 6 — ER MODEL

## Topic 1: উপাদান ও প্রতীক ⭐

```
┌──────────┐         ╱‾‾‾‾‾‾‾╲          ○──────
│  Entity  │        ╱ Relation ╲       Attribute
└──────────┘        ╲          ╱
 (আয়তক্ষেত্র)         ╲________╱          (উপবৃত্ত)
                      (রম্বস)
```

| প্রতীক | কী |
|---|---|
| আয়তক্ষেত্র | **Entity** (Student, Course) |
| রম্বস | **Relationship** (enrolls, teaches) |
| উপবৃত্ত | **Attribute** (Name, Age) |
| **আন্ডারলাইন করা** উপবৃত্ত | **Key attribute** (Primary key) |
| দ্বিগুণ উপবৃত্ত | **Multivalued** attribute (Phone) |
| ভাঙা রেখার উপবৃত্ত | **Derived** attribute (Age — DOB থেকে হিসাব) |
| দ্বিগুণ আয়তক্ষেত্র | **Weak Entity** (নিজের PK নেই) |

## 🔍 DRY RUN — একটা ছোট ER Diagram

```
   ○Std_ID   ○Name              ○C_ID   ○Title
      \       /                    \      /
       \     /                      \    /
     ┌─────────┐   ╱‾‾‾‾‾‾‾‾╲    ┌────────┐
     │ Student │──╱ Enrolls  ╲───│ Course │
     └─────────┘  ╲          ╱   └────────┘
          M        ╲________╱         N

        M : N  সম্পর্ক
```

## Topic 2: Cardinality ⭐

| Type | অর্থ | উদাহরণ |
|---|---|---|
| **1 : 1** | একজনের একটাই | Person ↔ Passport |
| **1 : M** | একজনের অনেক | Department → Students |
| **M : N** | অনেকের অনেক | Students ↔ Courses |

## 🔍 DRY RUN — ER থেকে Table বানানো ⭐

| সম্পর্ক | কীভাবে table বানাবে |
|---|---|
| **1 : 1** | যেকোনো একটা table-এ অন্যটার PK কে FK হিসেবে রাখো |
| **1 : M** | **"M" দিকের table-এ** "1" দিকের PK কে FK হিসেবে রাখো ⭐ |
| **M : N** | **নতুন একটা junction table** বানাও, দুই দিকের PK নিয়ে ⭐⭐ |

**M:N উদাহরণ (উপরের diagram থেকে):**
```
Student(Std_ID, Name)
Course(C_ID, Title)
Enrollment(Std_ID, C_ID, Grade)    ← নতুন junction table
           └── composite PK, দুটোই FK
```

### 🔁 Revision Box
ER: আয়তক্ষেত্র=**Entity**, রম্বস=**Relationship**, উপবৃত্ত=**Attribute**, আন্ডারলাইন=**Key**, দ্বিগুণ উপবৃত্ত=**Multivalued**, ভাঙা রেখা=**Derived**, দ্বিগুণ আয়তক্ষেত্র=**Weak entity**। Cardinality: **1:1, 1:M, M:N**। **1:M → M-দিকে FK**; **M:N → নতুন junction table**।

---
---

# MODULE 7 — TRANSACTION, ACID & INDEX

## Topic 1: ACID ⭐⭐⭐

### Definition
A **Transaction** is a logical unit of work consisting of one or more operations that must be executed **as a whole**.

| Property | অর্থ | উদাহরণ |
|---|---|---|
| **A — Atomicity** | **সব হবে, নয়তো কিছুই হবে না** | টাকা transfer: debit হলো কিন্তু credit ব্যর্থ → পুরোটা rollback |
| **C — Consistency** | Database এক বৈধ অবস্থা থেকে আরেক বৈধ অবস্থায় যাবে | মোট টাকার পরিমাণ অপরিবর্তিত থাকবে |
| **I — Isolation** | একসাথে চলা transaction একে অপরকে প্রভাবিত করবে না | দুজন একসাথে টাকা তুললেও হিসাব ঠিক থাকবে |
| **D — Durability** | Commit হয়ে গেলে **স্থায়ী** — বিদ্যুৎ গেলেও থাকবে | Server crash হলেও লেনদেন থাকবে |

### 🔍 DRY RUN — ব্যাংক Transfer
```sql
BEGIN TRANSACTION;
    UPDATE Account SET balance = balance - 5000 WHERE id = 'A';   -- ধাপ 1
    UPDATE Account SET balance = balance + 5000 WHERE id = 'B';   -- ধাপ 2
COMMIT;
```
**যদি ধাপ 1-এর পরে বিদ্যুৎ চলে যায়?**
→ **Atomicity** নিশ্চিত করবে ধাপ 1-ও বাতিল হবে (**ROLLBACK**)। A-র টাকা হারাবে না ✅

## Topic 2: Indexing ⭐

### Definition
An **Index** is a data structure (usually a **B+ Tree**) that speeds up data retrieval at the cost of extra storage and slower writes.

**কেন দ্রুত?** Index ছাড়া full table scan **O(n)**; index থাকলে **O(log n)**।

| | **Clustered Index** | **Non-clustered Index** |
|---|---|---|
| কী করে | **Data নিজেই সাজিয়ে রাখে** | আলাদা structure, pointer রাখে |
| প্রতি table-এ | **একটাই** | **একাধিক** |
| গতি | দ্রুততর | কিছুটা ধীর |
| উদাহরণ | Primary key | Secondary index |

⚠️ **Index-এর খরচ:** `INSERT`, `UPDATE`, `DELETE` ধীর হয় (index-ও আপডেট করতে হয়) ও extra storage লাগে।

### 🔁 Revision Box
**ACID: Atomicity** (সব বা কিছুই না), **Consistency** (বৈধ অবস্থা), **Isolation** (পরস্পর স্বাধীন), **Durability** (commit = স্থায়ী)। **Index = B+ Tree**, search **O(log n)**, কিন্তু write ধীর করে। **Clustered = একটাই, data নিজেই সাজানো**; **Non-clustered = একাধিক**।

---
---

# ★ FINAL REVISION

## 1. Sample Paper-এর ৪টা উত্তর ⭐⭐⭐

**Q10. Primary Key ও Foreign Key কী?**
> **Primary Key** হলো এমন একটি attribute (বা attribute-এর সেট) যা table-এর প্রতিটি row-কে **unique** ভাবে চিহ্নিত করে। এটি কখনো **NULL** হতে পারে না এবং প্রতি table-এ একটাই থাকে।
> **Foreign Key** হলো এমন একটি attribute যা **অন্য একটি table-এর Primary Key**-কে reference করে। এটি দুই table-এর মধ্যে **সম্পর্ক (relationship)** তৈরি করে এবং **referential integrity** বজায় রাখে। এটি NULL বা duplicate হতে পারে, এবং এক table-এ একাধিক থাকতে পারে।

**Q11.** `CREATE DATABASE MainRecord;`

**Q12.**
```sql
CREATE TABLE Record1 (
    ID   INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age  INT
);
```

**Q13.** `SELECT Age FROM Record1 WHERE Age = 32;`

## 2. Top 20 MCQ Traps ⭐

1. **Degree = column সংখ্যা**, **Cardinality = row সংখ্যা**
2. **Primary Key NULL হতে পারে না**, Foreign Key পারে
3. **Unique key NULL নিতে পারে**, Primary key পারে না
4. Super Key ⊃ Candidate Key ⊃ Primary Key
5. **TRUNCATE = DDL** (DML নয়), rollback হয় না
6. **DELETE-এ WHERE চলে, TRUNCATE-এ চলে না**
7. **DROP = table-ই মুছে যায়**, TRUNCATE-এ structure থাকে
8. **WHERE = row-এর উপর**, **HAVING = group-এর উপর**
9. **WHERE-এ aggregate function ব্যবহার করা যায় না**
10. SQL চলার ক্রম: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY**
11. **INNER JOIN = শুধু মিল**, LEFT = বাম-এর সব
12. **CROSS JOIN = m × n row** (Cartesian product)
13. **1NF = atomic**, 2NF = **no partial**, 3NF = **no transitive**
14. **2NF-এর সমস্যা শুধু composite key থাকলেই হয়**
15. **BCNF 3NF-এর চেয়ে কড়া**
16. **ACID = Atomicity, Consistency, Isolation, Durability**
17. **Index search দ্রুত করে কিন্তু insert/update ধীর করে**
18. **Clustered index প্রতি table-এ একটাই**
19. **M:N সম্পর্ক → নতুন junction table লাগে**
20. **CHAR = স্থির দৈর্ঘ্য, VARCHAR = পরিবর্তনশীল**

## 3. দ্রুত সংজ্ঞা

| Term | এক লাইনে |
|---|---|
| **DBMS** | Data define/store/retrieve করার software |
| **Primary Key** | Unique + NOT NULL, row চিহ্নিত করে |
| **Foreign Key** | অন্য table-এর PK reference, সম্পর্ক তৈরি করে |
| **Normalization** | Redundancy ও anomaly দূর করতে table ভাঙা |
| **Transaction** | একটি অবিভাজ্য কাজের একক |
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **Index** | Search দ্রুত করার data structure (B+ Tree) |
| **JOIN** | দুই table-এর data একসাথে আনা |
| **View** | Query-র ফলাফলের ভার্চুয়াল table |
| **Trigger** | কোনো ঘটনার পর স্বয়ংক্রিয়ভাবে চলা code |

---

# ✍️ নিজে করো (উত্তর নিচে)

1. `Employee(EmpID, Name, DeptID, DeptName, Salary)` — এটা কোন NF-এ আছে? 3NF-এ আনো।
2. যেসব বিভাগে গড় CGPA 3.5-এর বেশি, সেগুলো বের করার SQL লেখো।
3. `Student` table-এর সব row মুছতে চাই কিন্তু structure রাখতে চাই — কোন command?

<details>
<summary>উত্তর</summary>

**1.** `DeptID → DeptName` — এটা **transitive dependency** (EmpID → DeptID → DeptName)। তাই এটা **2NF-এ আছে, 3NF-এ নেই**।
3NF-এ আনতে ভাঙো:
```
Employee(EmpID, Name, DeptID, Salary)
Department(DeptID, DeptName)
```

**2.**
```sql
SELECT Dept, AVG(CGPA)
FROM Student
GROUP BY Dept
HAVING AVG(CGPA) > 3.5;
```
(⚠️ `WHERE AVG(CGPA) > 3.5` লিখলে **ভুল** হবে)

**3.** `TRUNCATE TABLE Student;`

</details>
