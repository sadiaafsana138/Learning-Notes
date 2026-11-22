# CSE 711 — Math 3: Random Forest Classification
**বাংলা step-by-step notes | Bootstrap, feature randomness, Gini, tree vote**

> Sir-এর **Practice Problem on RF.pdf**-এর dataset ও tree-building flow অনুসরণ করা হয়েছে। PDF-এ কিছু জায়গায় printed calculation inconsistency আছে; corrected arithmetic স্পষ্ট করে দেখানো হয়েছে।

## 1. Random Forest কীভাবে কাজ করে?

Random Forest অনেক Decision Tree তৈরি করে:
1. Training data থেকে bootstrap sample নেয় (replacement সহ random sampling)।
2. প্রতিটি tree-তে feature subset বিবেচনা করে।
3. প্রতিটি tree আলাদা prediction দেয়।
4. Classification-এ majority vote final class হয়।

## 2. Sir-এর dataset

| Day | Temp | Wind | Humidity | Living Status |
|---|---:|---|---|---|
| D1 | 20 | Weak | Normal | Ideal |
| D2 | 22 | Strong | Abnormal | Non-ideal |
| D3 | 30 | Strong | Normal | Ideal |
| D4 | 24 | Weak | Abnormal | Ideal |
| D5 | 32 | Strong | Normal | Non-ideal |
| D6 | 34 | Weak | Normal | Ideal |
| D7 | 36 | Weak | Abnormal | Non-ideal |

Query D8: Temp=33, Wind=Strong, Humidity=Abnormal। Expansion threshold=2।

## 3. Tree 1: D1–D5

| Day | Temp | Wind | Class |
|---|---:|---|---|
| D1 | 20 | Weak | Ideal |
| D2 | 22 | Strong | Non-ideal |
| D3 | 30 | Strong | Ideal |
| D4 | 24 | Weak | Ideal |
| D5 | 32 | Strong | Non-ideal |

Parent: Ideal=3, Non-ideal=2।

\[
Gini(parent)=1-(3/5)^2-(2/5)^2=0.48
\]

### Wind split

Weak: D1,D4 → I=2,N=0 → Gini=0।

Strong: D2,D3,D5 → I=1,N=2।

\[
Gini(Strong)=1-(1/3)^2-(2/3)^2=4/9=0.4444
\]

\[
Gini_{Wind}=\frac25(0)+\frac35(0.4444)=\boxed{0.2667}
\]

### Temperature split — candidate midpoint

Sorted Temp: 20(I),22(N),24(I),30(I),32(N)।
Candidates: 21,23,27,31।

| Threshold | Weighted Gini |
|---:|---:|
| 21 | 0.4000 |
| 23 | 0.4667 |
| 27 | 0.4667 |
| 31 | **0.3000** |

Example `<31`: Left I=3,N=1 → Gini=0.375; Right N=1 → Gini=0।

\[
(4/5)(0.375)+(1/5)(0)=0.3000
\]

Wind=0.2667, Temperature best=0.3000। Root = **Wind**।

```text
                 Wind
               /      \
           Weak        Strong
            |             |
          Ideal       Temp split
```

### Strong branch split

Rows: D2(22,N), D3(30,I), D5(32,N)।
Candidates: 26,31।

For `<26`: Left D2 pure N (Gini=0); Right D3,D5 (I=1,N=1; Gini=0.5)।

\[
Gini_{26}=\frac13(0)+\frac23(0.5)=0.3333
\]

For `<31`: Left D2,D3 (Gini=0.5); Right D5 (Gini=0)।

\[
Gini_{31}=\frac23(0.5)+\frac13(0)=0.3333
\]

Tie: দুটো threshold সমান ভালো। Expansion threshold 2 হওয়ায় 2-sample child আর expand হবে না।

## 4. Tree 2: D2–D6

Sir-এর stated bootstrap rows: D2,D3,D4,D5,D6।

| Day | Wind | Humidity | Class |
|---|---|---|---|
| D2 | Strong | Abnormal | Non-ideal |
| D3 | Strong | Normal | Ideal |
| D4 | Weak | Abnormal | Ideal |
| D5 | Strong | Normal | Non-ideal |
| D6 | Weak | Normal | Ideal |

Wind:
- Strong: D2,D3,D5 → N=2,I=1 → Gini=4/9=0.4444
- Weak: D4,D6 → I=2,N=0 → Gini=0

\[
Gini_{Wind}=\frac35(0.4444)+\frac25(0)=0.2667
\]

Humidity:
- Abnormal: D2,D4 → N=1,I=1 → Gini=0.5
- Normal: D3,D5,D6 → I=2,N=1 → Gini=4/9=0.4444

\[
Gini_{Humidity}=\frac25(0.5)+\frac35(0.4444)
=0.2+0.2667=0.4667
\]

তাই Root = Wind (0.2667 < 0.4667)।

**PDF inconsistency:** Problem statement-এ Tree 2-এর feature subset Wind ও Humidity বলা হলেও পরের branch calculation-এ Temperature split দেখানো হয়েছে। তাই PDF-এর Tree 2 branch-এ Temp ব্যবহারের বিষয়টি source inconsistency হিসেবে ধরবে; নিজের থেকে feature list বদলে নিও না।

## 5. Query ও voting

D8: Temp=33, Wind=Strong, Humidity=Abnormal।

- Tree 1: Wind=Strong branch → temperature split; tie/leaf treatment অনুযায়ী output ambiguous হতে পারে।
- Tree 2: Wind=Strong branch; PDF-এর final page-এ Non-ideal দেখানো।
- PDF final vote table: Tree 1 = Non-ideal, Tree 2 = Non-ideal, Tree 3 = Ideal or Non-ideal (ambiguous)।

Final majority: Non-ideal।

\[
\boxed{\hat y_{D8}=\text{Non-ideal}}
\]

## 6. Random Forest Regression-এ পার্থক্য

Classification: tree outputs class → majority vote।
Regression: tree outputs number → average।

## 7. Exam checklist

1. Bootstrap sample কী কী row দিয়ে হয়েছে লিখো।
2. Candidate feature subset আলাদা করে লেখো।
3. প্রতিটি feature-এর split impurity calculate করো।
4. Best split দিয়ে tree তৈরি করো।
5. Query-র path follow করে প্রতিটি tree prediction লেখো।
6. Classification হলে majority vote; Regression হলে arithmetic mean।
7. Sir-এর PDF-এ mismatch থাকলে printed answer ও corrected calculation আলাদা করে উল্লেখ করো।
