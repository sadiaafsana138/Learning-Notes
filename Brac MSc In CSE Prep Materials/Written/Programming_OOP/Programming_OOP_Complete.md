# 💻 PROGRAMMING & OOP — সম্পূর্ণ নোট
### CSE 110 / 111 / 310 — BRAC MSc CSE Admission

> **Sample paper-এ ৩টা প্রশ্ন** (Q6 fmod, Q7 round, Q8 Java loop trace, Q9 platform independence — আসলে ৪টা)।
> **Q8-এর সম্পূর্ণ trace** Module 3-এ আছে — ওটাই এই বিষয়ের সবচেয়ে গুরুত্বপূর্ণ অংশ।

---

## 📑 সূচি
| Module | বিষয় | Dry Run |
|---|---|---|
| 1 | Data Type · Operator · Precedence | ✅ |
| 2 | **math.h / Math Functions** ⭐ | ✅ |
| 3 | **Loop Tracing (Q8)** ⭐⭐⭐ | ✅ |
| 4 | Pointer · Array · Function | ✅ |
| 5 | **OOP-এর ৪ স্তম্ভ** ⭐⭐⭐ | — |
| 6 | **Overloading vs Overriding** ⭐ | ✅ |
| 7 | **Platform Independence (Q9)** ⭐⭐⭐ | ✅ |
| 8 | Exception · String | — |
| 9 | Final Revision | — |

---
---

# MODULE 1 — DATA TYPE, OPERATOR, PRECEDENCE

## Topic 1: Data Type ও আকার ⭐

| Type | আকার (byte) | পরিসর |
|---|---|---|
| `char` | **1** | −128 to 127 |
| `int` | **4** | −2,147,483,648 to 2,147,483,647 |
| `float` | **4** | ~7 দশমিক ঘর নির্ভুল |
| `double` | **8** | ~15 দশমিক ঘর নির্ভুল |
| `long` (Java) | 8 | বড় পূর্ণসংখ্যা |
| `boolean` (Java) | 1 | true / false |

**Formula:** n bit-এর signed type-এর পরিসর = **−2ⁿ⁻¹ থেকে 2ⁿ⁻¹ − 1**
*উদাহরণ:* `int` = 32 bit → −2³¹ থেকে 2³¹−1

## Topic 2: Operator Precedence ⭐⭐⭐

**উপর থেকে নিচে — উপরেরটা আগে চলে:**

| ক্রম | Operator | দিক |
|---|---|---|
| 1 | `()` `[]` `.` | বাম → ডান |
| 2 | `++` `--` `!` `~` (unary) | **ডান → বাম** |
| 3 | `*` `/` `%` | বাম → ডান |
| 4 | `+` `-` | বাম → ডান |
| 5 | `<<` `>>` | বাম → ডান |
| 6 | `<` `<=` `>` `>=` | বাম → ডান |
| 7 | `==` `!=` | বাম → ডান |
| 8 | `&&` | বাম → ডান |
| 9 | `\|\|` | বাম → ডান |
| 10 | `?:` | ডান → বাম |
| 11 | `=` `+=` `-=` | **ডান → বাম** |

⭐ **মুখস্থ:** **PUMA-RS-LA**
**P**arenthesis → **U**nary → **M**ultiply/Divide/Mod → **A**dd/Sub → **R**elational → **S**hift... মূল কথা: `()` > `++` > `*/%` > `+-` > তুলনা > `&&` > `||` > `=`

### 🔍 DRY RUN — Precedence
```c
int result = 2 + 3 * 4;
```
```
* আগে চলবে → 3*4 = 12
তারপর +    → 2+12 = 14

result = 14   (20 নয়!) ✅
```

```c
int x = 10 + 20 % 3 * 2;
```
```
% আর * সমান precedence → বাম থেকে ডানে
20 % 3 = 2
2 * 2  = 4
10 + 4 = 14   ✅
```

## Topic 3: `i++` vs `++i` ⭐⭐⭐

| | **`i++` (Post-increment)** | **`++i` (Pre-increment)** |
|---|---|---|
| কাজের ক্রম | **আগে ব্যবহার, পরে বাড়ে** | **আগে বাড়ে, পরে ব্যবহার** |

### 🔍 DRY RUN
```c
int i = 5;
printf("%d", i++);    // ছাপবে 5, তারপর i হবে 6
printf("%d", i);      // ছাপবে 6

int j = 5;
printf("%d", ++j);    // j আগে 6 হবে, তারপর ছাপবে 6
```

```c
int a = 5;
int b = a++ + ++a;
```
```
ধাপ 1: a++ → বর্তমান মান 5 ব্যবহার হবে, তারপর a = 6
ধাপ 2: ++a → a আগে 7 হবে, তারপর 7 ব্যবহার হবে
ধাপ 3: b = 5 + 7 = 12,  a = 7  ✅
```

## Topic 4: Division ও Modulus ⭐

```c
5 / 2      = 2      ⚠️ Integer division — দশমিক কেটে যায়
5.0 / 2    = 2.5    ✅ একটা float হলেই float division
5 % 2      = 1      ✅ ভাগশেষ

-5 / 2     = -2     (C-তে শূন্যের দিকে কাটে)
-5 % 2     = -1
```

⚠️ **`%` শুধু integer-এ চলে।** `5.5 % 2` লিখলে C-তে **compile error** ⭐

### 🔁 Revision Box
`int`=4 byte, `char`=1, `float`=4, `double`=8। Precedence: **`()` > `++` > `*/%` > `+-` > তুলনা > `&&` > `||` > `=`**। **`i++` = আগে ব্যবহার পরে বাড়ে**, **`++i` = আগে বাড়ে পরে ব্যবহার**। **`5/2 = 2`** (integer division), **`5.0/2 = 2.5`**। **`%` শুধু integer-এ**।

---
---

# MODULE 2 — MATH FUNCTIONS ⭐⭐⭐

> **Q6 ও Q7 এখান থেকে সরাসরি।**

## Topic 1: C-তে `math.h`

| Function | কাজ | উদাহরণ |
|---|---|---|
| **`fmod(a, b)`** | **float-এর ভাগশেষ** ⭐ | `fmod(3.14, 2.1)` = 1.04 |
| **`round(x)`** | নিকটতম পূর্ণসংখ্যায় ⭐ | `round(1.66)` = 2.0 |
| `ceil(x)` | **উপরের** পূর্ণসংখ্যা | `ceil(1.2)` = 2.0 |
| `floor(x)` | **নিচের** পূর্ণসংখ্যা | `floor(1.8)` = 1.0 |
| `pow(a, b)` | a-এর b ঘাত | `pow(2,3)` = 8 |
| `sqrt(x)` | বর্গমূল | `sqrt(16)` = 4 |
| `fabs(x)` | float-এর পরম মান | `fabs(-3.5)` = 3.5 |
| `abs(x)` | int-এর পরম মান | `abs(-5)` = 5 |

⚠️ ব্যবহার করতে হলে **`#include <math.h>`** লিখতে হবে, আর compile-এ **`-lm`** flag লাগতে পারে।

## 🔍 Q6-এর উত্তর — 3.14 ÷ 2.1-এর ভাগশেষ

```c
#include <stdio.h>
#include <math.h>

int main() {
    double result = fmod(3.14, 2.1);
    printf("%.2lf", result);      // ফলাফল: 1.04
    return 0;
}
```

**কেন `%` নয়?**
```c
double r = 3.14 % 2.1;    // ❌ Compile Error!
                          // % operator শুধু integer-এ কাজ করে
```

**হিসাব যাচাই:**
```
3.14 ÷ 2.1 = 1.495...
পূর্ণ ভাগফল = 1
ভাগশেষ = 3.14 − (1 × 2.1) = 3.14 − 2.1 = 1.04  ✅
```

**Java-তে:**
```java
double result = 3.14 % 2.1;    // ✅ Java-তে % float-এও চলে!
// অথবা
double result = Math.IEEEremainder(3.14, 2.1);
```
⭐ **এটাই C ও Java-র বড় পার্থক্য — Java-তে `%` float-এ চলে, C-তে চলে না।**

## 🔍 Q7-এর উত্তর — 1.66 কে 2.0 করা

```c
// C
double x = round(1.66);       // 2.0  ✅
```
```java
// Java
long x = Math.round(1.66);    // 2  ✅
double y = Math.ceil(1.66);   // 2.0 ✅ (এটাও কাজ করবে)
```

### ⚠️ round vs ceil vs floor — পার্থক্য দেখো

| মান | `round()` | `ceil()` | `floor()` |
|---|---|---|---|
| 1.2 | **1** | **2** | **1** |
| 1.5 | **2** | 2 | 1 |
| **1.66** | **2** ✅ | **2** | 1 |
| −1.5 | −2 (C) / −1 (Java) | −1 | −2 |

⚠️ **Trap:** `ceil(1.2)` = **2** কিন্তু `round(1.2)` = **1** — এই পার্থক্যটা MCQ-তে আসে।

### 🔁 Revision Box
**`fmod(3.14, 2.1)` = 1.04** — C-তে float-এর ভাগশেষ (`%` চলে না)। **Java-তে `%` float-এও চলে**। **`round(1.66)` = 2.0** / `Math.round(1.66)` = 2। **`ceil` = উপরে, `floor` = নিচে, `round` = নিকটতম**।

---
---

# MODULE 3 — LOOP TRACING ⭐⭐⭐

> **Q8 এখানে। এটাই সবচেয়ে বেশি নম্বরের একক প্রশ্ন — ধাপে ধাপে করছি।**

## Topic 1: Short-Circuit Evaluation ⭐⭐⭐

### নিয়ম
| Operator | নিয়ম |
|---|---|
| **`&&` (AND)** | **প্রথমটা `false` হলে দ্বিতীয়টা মোটেও চলবে না** ⭐ |
| **`\|\|` (OR)** | **প্রথমটা `true` হলে দ্বিতীয়টা মোটেও চলবে না** |

```c
int i = 0;
if (0 && (i++ > 5))  { }
// প্রথমটা false → i++ কখনো চলবে না → i রয়ে গেল 0 ⚠️

if (1 || (i++ > 5))  { }
// প্রথমটা true → i++ চলবে না → i এখনো 0
```

⭐ **এটাই Q8-এর পুরো ফাঁদ।**

## Topic 2: `for` loop-এর চলার ক্রম ⭐

```c
for (initialization ; condition ; update) {
    body
}
```

**চলার ক্রম:**
```
1. Initialization      (একবারই)
2. Condition যাচাই  →  false হলে loop শেষ
3. Body চলে
4. Update চলে
5. আবার ধাপ 2-এ ফিরে যায়
```

⚠️ **গুরুত্বপূর্ণ:** Update (`i++`) **body-র পরে** চলে, আগে নয়।

---

## 🔍 Q8-এর সম্পূর্ণ DRY RUN ⭐⭐⭐

```java
public class Test {
    public static void main(String args[]) {
        int i = 0, j = 5;
        for( ; (i < 3) && (j++ < 10) ; i++ ) {
            System.out.print(" " + i + " " + j );
        }
        System.out.print(" " + i + " " + j );
    }
}
```

### লক্ষ্য করার তিনটি বিষয়
1. **Initialization খালি** — `i=0, j=5` আগেই সেট করা
2. Condition-এ **`j++`** আছে — condition যাচাই করার সময়ই j বাড়ে
3. **`&&` short-circuit** — `i < 3` false হলে `j++` চলবেই না ⚠️

### ধাপে ধাপে

```
শুরু: i = 0, j = 5
```

**─── পুনরাবৃত্তি ১ ───**
```
Condition যাচাই:
  (i < 3)  →  0 < 3  →  TRUE ✅
  (j++ < 10) →  j-র বর্তমান মান 5 ব্যবহার হবে → 5 < 10 → TRUE ✅
              তারপর j বেড়ে হলো 6
  সামগ্রিক: TRUE && TRUE = TRUE → loop চলবে

Body:  print " " + i + " " + j  →  " 0 6"

Update: i++  →  i = 1
```

**─── পুনরাবৃত্তি ২ ───**
```
Condition:
  (1 < 3) → TRUE ✅
  (j++ < 10) → 6 < 10 → TRUE ✅, তারপর j = 7
  → loop চলবে

Body:  " 1 7"

Update: i++  →  i = 2
```

**─── পুনরাবৃত্তি ৩ ───**
```
Condition:
  (2 < 3) → TRUE ✅
  (j++ < 10) → 7 < 10 → TRUE ✅, তারপর j = 8
  → loop চলবে

Body:  " 2 8"

Update: i++  →  i = 3
```

**─── পুনরাবৃত্তি ৪ (চেষ্টা) ───**
```
Condition:
  (3 < 3) → FALSE ❌

  ⚠️ SHORT-CIRCUIT!  && এর প্রথমটা false, তাই
     (j++ < 10) মোটেও চলবে না
     → j বাড়বে না, j রয়ে গেল 8

  → loop শেষ
```

**─── Loop-এর বাইরের print ───**
```
i = 3,  j = 8
print " 3 8"
```

### ✅ চূড়ান্ত উত্তর

```
Output:  0 6 1 7 2 8 3 8
```

### সারণী আকারে
| পুনরাবৃত্তি | i | j (যাচাইয়ের আগে) | i<3 | j++<10 | j (পরে) | ছাপা হলো |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | ✅ | ✅ | 6 | ` 0 6` |
| 2 | 1 | 6 | ✅ | ✅ | 7 | ` 1 7` |
| 3 | 2 | 7 | ✅ | ✅ | 8 | ` 2 8` |
| 4 | 3 | 8 | ❌ | **চলেনি** | **8** | — |
| শেষ | 3 | 8 | — | — | — | ` 3 8` |

### ⚠️ সবচেয়ে বড় ভুল যেটা মানুষ করে
> শেষে `j = 9` লেখা।
> **কেন ভুল?** কারণ `i < 3` false হওয়ায় short-circuit-এর কারণে `j++` **চলেইনি**। j আটকে গেছে **8**-এ। ⭐

## Topic 3: আরও কিছু Loop Trace

### `while` vs `do-while`
```c
int i = 10;
while (i < 5) { printf("A"); }      // কিছুই ছাপবে না (শর্ত শুরুতেই false)

int j = 10;
do { printf("B"); } while (j < 5);  // "B" একবার ছাপবে ⭐
```
⭐ **`do-while` অন্তত একবার চলবেই** — শর্ত পরে যাচাই হয়।

### Nested loop
```c
for(int i=1; i<=3; i++)
    for(int j=1; j<=2; j++)
        printf("%d%d ", i, j);
```
```
i=1: j=1 → "11", j=2 → "12"
i=2: j=1 → "21", j=2 → "22"
i=3: j=1 → "31", j=2 → "32"

Output: 11 12 21 22 31 32
মোট চলল: 3 × 2 = 6 বার
```

### 🔁 Revision Box
`for` চলার ক্রম: **init → condition → body → update → condition...**। **`&&`-এ প্রথমটা false হলে দ্বিতীয়টা চলে না** (short-circuit) — **Q8-এর পুরো ফাঁদ এটাই**। Q8-এর উত্তর: **` 0 6 1 7 2 8 3 8`**। **`do-while` অন্তত একবার চলে**।

---
---

# MODULE 4 — POINTER, ARRAY, FUNCTION

## Topic 1: Pointer ⭐

```c
int a = 10;
int *p = &a;      // p তে a-র ঠিকানা

printf("%d", a);    // 10   — মান
printf("%p", &a);   // 0x7ffd...  — ঠিকানা
printf("%p", p);    // 0x7ffd...  — একই ঠিকানা
printf("%d", *p);   // 10   — ঠিকানার ভিতরের মান (dereference)
```

```
     a                    p
┌────────┐          ┌──────────┐
│   10   │◄─────────│ 0x1000   │
└────────┘          └──────────┘
 ঠিকানা              p-তে a-র
 0x1000              ঠিকানা রাখা
```

| প্রতীক | অর্থ |
|---|---|
| `&a` | a-র **ঠিকানা** |
| `*p` | p যে ঠিকানায় আছে সেখানকার **মান** |

## Topic 2: Call by Value vs Call by Reference ⭐⭐

### 🔍 DRY RUN
```c
// Call by Value — নকল পাঠানো হয়
void swap1(int x, int y) { int t=x; x=y; y=t; }

// Call by Reference — ঠিকানা পাঠানো হয়
void swap2(int *x, int *y) { int t=*x; *x=*y; *y=t; }

int main() {
    int a=5, b=10;
    swap1(a, b);   printf("%d %d", a, b);   // 5 10  ⚠️ বদলায়নি!
    swap2(&a, &b); printf("%d %d", a, b);   // 10 5  ✅ বদলেছে
}
```

| | **Call by Value** | **Call by Reference** |
|---|---|---|
| কী পাঠায় | মানের **নকল** | **ঠিকানা** |
| মূল variable | **বদলায় না** | **বদলায়** |
| Java-তে | primitive-এর জন্য | object-এর জন্য (reference-এর নকল) |

⚠️ **Java-তে সবকিছুই আসলে call by value** — তবে object-এর ক্ষেত্রে **reference-এর মান** কপি হয়, তাই object-এর ভিতরের data বদলানো যায়।

## Topic 3: Array ও Pointer-এর সম্পর্ক
```c
int arr[5] = {10,20,30,40,50};

arr        ≡  &arr[0]      // array-র নাম = প্রথম element-এর ঠিকানা
*(arr + 2) ≡  arr[2]       // = 30
```

## Topic 4: Storage Class (C)
| Class | কোথায় | আয়ু |
|---|---|---|
| `auto` | Stack | function-এর ভিতরে |
| `static` | Data segment | **পুরো program জুড়ে** ⭐ |
| `extern` | Global | পুরো program |
| `register` | CPU register (অনুরোধ) | function-এর ভিতরে |

### 🔁 Revision Box
`&a` = ঠিকানা, `*p` = ঠিকানার মান। **Call by Value = নকল, মূল বদলায় না**; **Call by Reference = ঠিকানা, মূল বদলায়**। `arr ≡ &arr[0]`, `*(arr+i) ≡ arr[i]`। **`static` variable-এর মান function শেষেও থাকে**।

---
---

# MODULE 5 — OOP-এর ৪ স্তম্ভ ⭐⭐⭐

## Topic 1: Class vs Object

```java
class Car {              // Class = নকশা / blueprint
    String color;        // Attribute (state)
    void drive() { }     // Method (behavior)
}

Car myCar = new Car();   // Object = নকশা থেকে বানানো বাস্তব জিনিস
```

⭐ **Class = নকশা** (একটাই), **Object = সেই নকশা থেকে বানানো** (অনেকগুলো হতে পারে)।

## Topic 2: ৪ স্তম্ভ ⭐⭐⭐

### 1️⃣ Encapsulation
**Definition:** Wrapping **data and methods** together into a single unit and **restricting direct access** to the data.

```java
class Account {
    private double balance;                    // ← বাইরে থেকে ছোঁয়া যাবে না

    public double getBalance() { return balance; }        // Getter
    public void deposit(double amt) {                     // Setter
        if (amt > 0) balance += amt;                      // ← নিয়ন্ত্রণ
    }
}
```
⭐ **Data Hiding** — `private` করে `getter/setter` দিয়ে নিয়ন্ত্রিত access দেওয়া।

### 2️⃣ Inheritance
**Definition:** A class **acquires properties and methods** of another class.

```java
class Vehicle {                          // Parent / Super class
    void start() { }
}
class Car extends Vehicle {              // Child / Sub class
    void openSunroof() { }
}
// Car পাবে start() + নিজের openSunroof()
```

**ধরন:**
| Type | গঠন | Java-তে? |
|---|---|---|
| **Single** | A → B | ✅ |
| **Multilevel** | A → B → C | ✅ |
| **Hierarchical** | A → B, A → C | ✅ |
| **Multiple** | A, B → C | ❌ **class দিয়ে নয়** ⭐ |
| **Hybrid** | মিশ্র | ❌ |

⚠️ **Java-তে multiple inheritance নেই কেন?**
**Diamond Problem** — দুই parent-এ একই নামের method থাকলে child কোনটা নেবে? দ্ব্যর্থতা এড়াতে Java এটা বাদ দিয়েছে। **Interface দিয়ে** এই কাজ করা যায়। ⭐

### 3️⃣ Polymorphism
**Definition:** The ability of one interface to take **many forms**.

| Type | কখন ঠিক হয় | কীভাবে |
|---|---|---|
| **Compile-time (Static)** | **Compile-এর সময়** | **Method Overloading** |
| **Run-time (Dynamic)** | **চলার সময়** | **Method Overriding** |

### 4️⃣ Abstraction
**Definition:** Showing only **essential features** and hiding implementation details.

```java
abstract class Shape {
    abstract void draw();       // শুধু ঘোষণা, কাজ নেই
}
class Circle extends Shape {
    void draw() { /* বৃত্ত আঁকার কাজ */ }
}
```
⭐ **Encapsulation vs Abstraction:**
- **Encapsulation** = **কীভাবে** লুকানো হয় (private + getter/setter)
- **Abstraction** = **কী** লুকানো হয় (implementation-এর জটিলতা)

### 🔁 Revision Box
**Class = নকশা, Object = বাস্তব রূপ**। ৪ স্তম্ভ: **Encapsulation** (data + method একসাথে, private + getter/setter), **Inheritance** (গুণাবলি উত্তরাধিকার, `extends`), **Polymorphism** (এক interface অনেক রূপ), **Abstraction** (শুধু প্রয়োজনীয়টা দেখানো)। **Java-তে multiple inheritance নেই — Diamond Problem; interface দিয়ে হয়**।

---
---

# MODULE 6 — OVERLOADING vs OVERRIDING ⭐⭐⭐

## 🔍 DRY RUN — পার্থক্য দেখো

### Method Overloading (Compile-time)
```java
class Calculator {
    int add(int a, int b)          { return a + b; }        // ১
    int add(int a, int b, int c)   { return a+b+c; }        // ২ — parameter সংখ্যা ভিন্ন
    double add(double a, double b) { return a + b; }        // ৩ — type ভিন্ন
}

Calculator c = new Calculator();
c.add(2, 3);          // ১ নম্বরটা চলবে → 5
c.add(2, 3, 4);       // ২ নম্বরটা চলবে → 9
c.add(2.5, 3.5);      // ৩ নম্বরটা চলবে → 6.0
```
⭐ **একই class-এ একই নামের method, কিন্তু parameter ভিন্ন।**

### Method Overriding (Run-time)
```java
class Animal {
    void sound() { System.out.println("Some sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("Bark"); }     // parent-এর টা বদলে দিলো
}

Animal a = new Dog();     // ⭐ reference Animal, object Dog
a.sound();                // "Bark" ছাপবে (Dog-এর টা)
```
⭐ **এটাই Dynamic Method Dispatch** — কোন method চলবে তা **চলার সময়** object দেখে ঠিক হয়, reference-এর type দেখে নয়। **Run-time polymorphism-এর মূল।**

## Comparison ⭐⭐⭐

| Feature | **Overloading** | **Overriding** |
|---|---|---|
| কখন ঠিক হয় | **Compile time** | **Run time** |
| Polymorphism | **Static** | **Dynamic** |
| কোথায় | **একই class-এ** | **Parent-Child class-এ** |
| Parameter | **ভিন্ন হতেই হবে** | **হুবহু একই হতে হবে** |
| Return type | ভিন্ন হতে পারে | একই (বা covariant) |
| Inheritance | লাগে না | **লাগে** |

⚠️ **Trap:** শুধু **return type ভিন্ন** করে overload করা যায় **না** — parameter ভিন্ন হতেই হবে ⭐

## Abstract Class vs Interface ⭐

| Feature | **Abstract Class** | **Interface** |
|---|---|---|
| Method | Abstract + concrete দুটোই | সব abstract (Java 8+ এ default/static চলে) |
| Variable | যেকোনো ধরনের | সব `public static final` |
| Constructor | ✅ আছে | ❌ নেই |
| Multiple | ❌ একটাই extend করা যায় | ✅ **একাধিক implement করা যায়** ⭐ |
| Keyword | `extends` | `implements` |
| কখন | কিছু সাধারণ code শেয়ার করতে | শুধু চুক্তি (contract) ঠিক করতে |

## Access Modifiers ⭐

| Modifier | একই class | একই package | Child class | সব জায়গায় |
|---|---|---|---|---|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

### 🔁 Revision Box
**Overloading = একই class, parameter ভিন্ন, compile-time**। **Overriding = parent-child, parameter হুবহু একই, run-time**। শুধু return type বদলে overload হয় **না**। **Abstract class = `extends`, একটাই**; **Interface = `implements`, একাধিক**। Access: `private < default < protected < public`।

---
---

# MODULE 7 — PLATFORM INDEPENDENCE ⭐⭐⭐

> **Q9-এর উত্তর।**

## 🔍 DRY RUN — Java কীভাবে চলে

```
     Test.java  (Source Code — মানুষের পড়ার মতো)
         │
         │  javac Test.java
         ▼
   ┌─────────────────┐
   │  Java Compiler  │
   └─────────────────┘
         │
         ▼
     Test.class  (BYTECODE — মধ্যবর্তী রূপ) ⭐
         │
         │  একই .class file সব OS-এ চলবে
         │
    ┌────┴──────┬──────────┐
    ▼           ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│JVM for │ │JVM for │ │JVM for │   ← JVM প্রতিটি OS-এর জন্য আলাদা
│Windows │ │ Linux  │ │  Mac   │
└────────┘ └────────┘ └────────┘
    │           │          │
    ▼           ▼          ▼
 Machine     Machine    Machine
  Code        Code       Code
```

## মূল কথা ⭐⭐⭐

> **Bytecode হলো platform-independent। JVM হলো platform-dependent।**

এই এক বাক্যেই Q9-এর উত্তরের সারমর্ম।

### Q9-এর পূর্ণ উত্তর

> **Platform Independence** মানে একটি programming language-এ লেখা program একবার compile করে **যেকোনো operating system-এ কোনো পরিবর্তন ছাড়াই** চালানো যাওয়া।
>
> Java এটি অর্জন করে **Bytecode** ব্যবহার করে। Java compiler (`javac`) source code-কে সরাসরি machine code-এ নয়, **Bytecode** (`.class` file)-এ রূপান্তর করে। এই Bytecode কোনো নির্দিষ্ট OS-নির্ভর নয়।
>
> প্রতিটি operating system-এর জন্য আলাদা **JVM (Java Virtual Machine)** থাকে, যা সেই Bytecode-কে ঐ machine-এর নিজস্ব code-এ রূপান্তর করে চালায়।
>
> এজন্যই Java-র নীতি: **"Write Once, Run Anywhere" (WORA)**।
>
> সংক্ষেপে — **Bytecode platform-independent, কিন্তু JVM platform-dependent**।

## Java vs C/C++ ⭐

| | **Java** | **C / C++** |
|---|---|---|
| Compile হয়ে যায় | **Bytecode** | **Machine code** |
| Platform | **Independent** ✅ | **Dependent** ❌ |
| চালায় | **JVM** | সরাসরি OS |
| গতি | কিছুটা ধীর (JVM layer) | **দ্রুত** |
| Memory | **Garbage Collector** | manual (`free`, `delete`) |
| Pointer | নেই (reference আছে) | আছে |

## JDK vs JRE vs JVM ⭐⭐

```
┌─────────────────────────────────────┐
│  JDK  (Java Development Kit)        │  ← বানানোর জন্য
│  ┌───────────────────────────────┐  │
│  │  JRE  (Java Runtime Env.)     │  │  ← চালানোর জন্য
│  │  ┌─────────────────────────┐  │  │
│  │  │  JVM (Virtual Machine)  │  │  │  ← আসল ইঞ্জিন
│  │  └─────────────────────────┘  │  │
│  │      + Library                │  │
│  └───────────────────────────────┘  │
│      + Compiler (javac), Debugger    │
└─────────────────────────────────────┘
```

| | কী আছে | কার জন্য |
|---|---|---|
| **JVM** | Bytecode চালানোর ইঞ্জিন | — |
| **JRE** | JVM + Library | যারা **শুধু চালাবে** |
| **JDK** | JRE + Compiler + Tools | **Developer** |

### 🔁 Revision Box
**Source (.java) → Compiler (javac) → Bytecode (.class) → JVM → Machine code**।
⭐ **Bytecode platform-independent, JVM platform-dependent** — এটাই মূল উত্তর।
নীতি: **"Write Once, Run Anywhere"**। **JDK ⊃ JRE ⊃ JVM**।

---
---

# MODULE 8 — EXCEPTION & STRING

## Topic 1: Exception Handling ⭐

```java
try {
    int x = 10 / 0;                          // ঝুঁকিপূর্ণ code
} catch (ArithmeticException e) {
    System.out.println("Divide by zero!");   // ভুল সামলানো
} finally {
    System.out.println("সবসময় চলবে");        // ⭐ ভুল হোক না হোক, চলবেই
}
```

| Keyword | কাজ |
|---|---|
| `try` | ঝুঁকিপূর্ণ code |
| `catch` | ভুল ধরা |
| `finally` | **সবসময়** চলে (resource বন্ধ করতে) |
| `throw` | **নিজে** exception তৈরি করা |
| `throws` | Method **ঘোষণা** করে যে সে exception ছুঁড়তে পারে |

### Checked vs Unchecked ⭐

| | **Checked** | **Unchecked (Runtime)** |
|---|---|---|
| কখন ধরা পড়ে | **Compile time** | **Run time** |
| Handle করা | **বাধ্যতামূলক** | ঐচ্ছিক |
| উদাহরণ | `IOException`, `SQLException`, `ClassNotFoundException` | `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException` |

## Topic 2: String ⭐

| | `String` | `StringBuffer` | `StringBuilder` |
|---|---|---|---|
| পরিবর্তনযোগ্য? | ❌ **Immutable** | ✅ Mutable | ✅ Mutable |
| Thread-safe? | ✅ | ✅ **হ্যাঁ** (synchronized) | ❌ না |
| গতি | ধীর (বারবার বদলালে) | ধীর | **দ্রুত** ⭐ |

### ⚠️ `==` vs `.equals()` ⭐⭐⭐
```java
String a = "hello";
String b = "hello";
String c = new String("hello");

a == b          // true   (দুটোই string pool-এর একই object)
a == c          // false  ⚠️ (c আলাদা object, ঠিকানা ভিন্ন)
a.equals(c)     // true   ✅ (মান তুলনা করে)
```
⭐ **`==` ঠিকানা তুলনা করে, `.equals()` মান তুলনা করে।** নিশ্চিত MCQ।

### 🔁 Revision Box
`try-catch-finally`; **`finally` সবসময় চলে**। **Checked = compile-time, handle বাধ্যতামূলক** (IOException); **Unchecked = runtime** (NullPointerException)। **String immutable**, StringBuffer **thread-safe**, StringBuilder **দ্রুত**। **`==` ঠিকানা, `.equals()` মান**।

---
---

# ★ FINAL REVISION

## 1. Sample Paper-এর উত্তর ⭐⭐⭐

**Q6.** `fmod(3.14, 2.1)` → **1.04** (C-তে `%` float-এ চলে না; Java-তে `3.14 % 2.1` লেখা যায়)

**Q7.** `round(1.66)` → **2.0** · Java-তে `Math.round(1.66)` → **2**

**Q8.** Output: **` 0 6 1 7 2 8 3 8`**
> মূল কারণ — শেষবার `i < 3` false হওয়ায় **short-circuit**-এর জন্য `j++` চলেনি, তাই j আটকে গেছে 8-এ।

**Q9.** Bytecode + JVM = "Write Once, Run Anywhere"। **Bytecode platform-independent, JVM platform-dependent**।

## 2. Top 20 MCQ Traps ⭐

1. **`5/2 = 2`** (integer division), **`5.0/2 = 2.5`**
2. **C-তে `%` float-এ চলে না** — `fmod()` লাগে; **Java-তে চলে**
3. **`round(1.2) = 1` কিন্তু `ceil(1.2) = 2`**
4. **`&&`-এ প্রথমটা false হলে দ্বিতীয়টা চলে না** (short-circuit)
5. **`i++` = আগে ব্যবহার**, **`++i` = আগে বাড়ে**
6. **`do-while` অন্তত একবার চলে**
7. `for`-এ **update body-র পরে** চলে
8. **Java-তে multiple inheritance নেই** (Diamond Problem) — interface দিয়ে হয়
9. **Overloading = compile-time**, **Overriding = run-time**
10. শুধু **return type বদলে overload করা যায় না**
11. **Interface একাধিক implement করা যায়**, class একটাই extend
12. **Constructor-এর return type থাকে না**, class-এর নামেই হয়
13. **`==` ঠিকানা তুলনা, `.equals()` মান তুলনা**
14. **String immutable**
15. **`finally` সবসময় চলে** (return থাকলেও)
16. **Checked = compile-time** (IOException), **Unchecked = runtime** (NullPointerException)
17. **Bytecode platform-independent, JVM platform-dependent**
18. **JDK ⊃ JRE ⊃ JVM**
19. **`static` method-এ `this` ব্যবহার করা যায় না**
20. **Call by Value-তে মূল variable বদলায় না**

## 3. দ্রুত সংজ্ঞা

| Term | এক লাইনে |
|---|---|
| **Class** | Object তৈরির নকশা |
| **Object** | Class-এর বাস্তব রূপ |
| **Constructor** | Object তৈরির সময় নিজে থেকে চলা method, return type নেই |
| **Encapsulation** | Data + method একসাথে, private + getter/setter |
| **Inheritance** | Parent-এর গুণাবলি child পায় |
| **Polymorphism** | এক নাম, অনেক রূপ |
| **Abstraction** | শুধু প্রয়োজনীয়টা দেখানো |
| **Bytecode** | Platform-independent মধ্যবর্তী code |
| **JVM** | Bytecode চালানোর platform-নির্ভর ইঞ্জিন |
| **Garbage Collector** | অব্যবহৃত memory স্বয়ংক্রিয়ভাবে মুক্ত করা |

---

# ✍️ নিজে করো (উত্তর নিচে)

```java
// 1.
int i = 0;
while (i++ < 3) { System.out.print(i + " "); }
System.out.print(i);

// 2.
int a = 5;
int b = ++a + a++;
System.out.println(a + " " + b);

// 3.
int x = 0;
if (x++ > 0 && ++x > 1) { }
System.out.println(x);
```

<details>
<summary>উত্তর</summary>

**1.**
```
i=0: 0<3 ✅, i হয় 1 → ছাপে "1 "
i=1: 1<3 ✅, i হয় 2 → ছাপে "2 "
i=2: 2<3 ✅, i হয় 3 → ছাপে "3 "
i=3: 3<3 ❌, i হয় 4 → loop শেষ
শেষে ছাপে 4

Output: 1 2 3 4
```

**2.**
```
++a → a আগে 6 হয়, 6 ব্যবহার হয়
a++ → বর্তমান 6 ব্যবহার হয়, তারপর a = 7
b = 6 + 6 = 12,  a = 7

Output: 7 12
```

**3.**
```
x++ > 0  →  0 > 0 → FALSE, কিন্তু x বেড়ে হলো 1
&& এর প্রথমটা false → SHORT-CIRCUIT → ++x চলবেই না
x রয়ে গেল 1

Output: 1
```
(⭐ এটাও Q8-এর মতোই short-circuit-এর ফাঁদ)

</details>
