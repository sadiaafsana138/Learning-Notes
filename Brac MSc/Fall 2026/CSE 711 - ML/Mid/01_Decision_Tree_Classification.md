# CSE 711 — Math 1: Decision Tree Classification
**বাংলা step-by-step notes | Gini, Entropy, Information Gain, Best Split**

> Classification-এ target class/category হয়। এই নোটে Gini দিয়ে split বের করার complete worked example দেওয়া হয়েছে। Sir-এর RF practice-এর D1–D5 dataset-ও একই Gini process ব্যবহার করে।

## 1. কখন এই math?
যখন target categorical: যেমন Ideal/Non-ideal, Yes/No, Pass/Fail। Decision Tree-এর প্রতিটি node-এ প্রশ্ন করে data-কে ভাগ করা হয়। যে split-এর impurity সবচেয়ে কমে, সেটি বেছে নেওয়া হয়।

## 2. Gini Impurity

\[
Gini(S)=1-\sum_{k=1}^{K}p_k^2
\]

Binary class হলে:

\[
Gini(S)=1-(p_1^2+p_2^2)
\]

- \(p_k\) = node-এ class \(k\)-এর proportion।
- সব sample একই class হলে Gini = 0 (pure node)।
- দুই class সমান হলে Gini = 0.5 (binary case-এ maximum)।

Split-এর পর দুই child-এর weighted impurity:

\[
Gini_{split}=\frac{n_L}{n}Gini(L)+\frac{n_R}{n}Gini(R)
\]

**Best split = minimum Weighted Gini।** শুধু একটি child-এর Gini দেখে সিদ্ধান্ত নেবে না; দুই child-ই যোগ করতে হবে।

## 3. Worked example: Sir-এর RF practice-এর প্রথম পাঁচ দিন

| Day | Temp | Wind | Class |
|---|---:|---|---|
| D1 | 20 | Weak | Ideal |
| D2 | 22 | Strong | Non-ideal |
| D3 | 30 | Strong | Ideal |
| D4 | 24 | Weak | Ideal |
| D5 | 32 | Strong | Non-ideal |

Parent node: Ideal = 3, Non-ideal = 2।

\[
Gini(parent)=1-(3/5)^2-(2/5)^2
=1-9/25-4/25=12/25=0.48
\]

### Step A — Wind split

**Wind = Weak:** D1,D4 → Ideal=2, Non-ideal=0

\[
Gini(Weak)=1-(2/2)^2-(0/2)^2=0
\]

**Wind = Strong:** D2,D3,D5 → Ideal=1, Non-ideal=2

\[
Gini(Strong)=1-(1/3)^2-(2/3)^2
=1-1/9-4/9=4/9=0.4444
\]

দুই child-এর weighted average:

\[
Gini_{Wind}=\frac25(0)+\frac35(0.4444)=0.2667
\]

### Step B — Temperature split

প্রথমে Temp ascending order-এ সাজাও:

20(I), 22(N), 24(I), 30(I), 32(N)

Adjacent value-গুলোর midpoint candidate:

\[
21,\ 23,\ 27,\ 31
\]

উদাহরণ threshold = 31:

- Left: Temp < 31 → D1,D2,D3,D4 → I=3, N=1
- Right: Temp ≥ 31 → D5 → N=1

\[
Gini(L)=1-(3/4)^2-(1/4)^2=1-9/16-1/16=0.375
\]

\[
Gini(R)=1-(0/1)^2-(1/1)^2=0
\]

\[
Gini_{31}=\frac45(0.375)+\frac15(0)=0.3000
\]

সব threshold-এর হিসাব:

| Threshold | Left class counts (I,N) | Right class counts (I,N) | Weighted Gini |
|---:|---|---|---:|
| 21 | (1,0) | (2,2) | 0.4000 |
| 23 | (1,1) | (2,1) | 0.4667 |
| 27 | (2,1) | (1,1) | 0.4667 |
| 31 | (3,1) | (0,1) | **0.3000** |

### Step C — Root নির্বাচন

- Wind = 0.2667
- Best Temperature threshold = 0.3000

তাই Root হবে **Wind**, কারণ 0.2667 কম।

```text
                 Wind
               /      \
           Weak        Strong
            |             |
          Ideal       split further
```

### Step D — Strong branch split

Strong subset: D2(22,N), D3(30,I), D5(32,N)।

Candidate midpoint: (22+30)/2 = 26 এবং (30+32)/2 = 31।

**Threshold 26:**
- Left: D2 → pure N → Gini=0
- Right: D3,D5 → I=1,N=1 → Gini=0.5

\[
Gini_{26}=\frac13(0)+\frac23(0.5)=0.3333
\]

**Threshold 31:**
- Left: D2,D3 → N=1,I=1 → Gini=0.5
- Right: D5 → pure N → Gini=0

\[
Gini_{31}=\frac23(0.5)+\frac13(0)=0.3333
\]

Tie: দুই split-ই সমান ভালো। Sir-এর PDF-এও এই tie আছে।

## 4. Entropy ও Information Gain (যদি প্রশ্নে এগুলো চায়)

\[
Entropy(S)=-\sum p_k\log_2(p_k)
\]

\[
IG=Entropy(parent)-\sum_j\frac{n_j}{n}Entropy(child_j)
\]

Example parent-এ I=3,N=2:

\[
Entropy(parent)=-(3/5)\log_2(3/5)-(2/5)\log_2(2/5)
\approx0.971
\]

Pure node-এর entropy = 0। **Best split = maximum Information Gain** (অথবা minimum weighted child entropy)।

## 5. Exam-এ calculation করার checklist

1. Target categorical কি না দেখো।
2. Parent-এর class count ও impurity বের করো।
3. Numeric feature হলে sort করে adjacent midpoint threshold বের করো।
4. প্রতিটি candidate-এ Left/Right class count লেখো।
5. প্রতিটি child-এর Gini/Entropy বের করো।
6. Child impurity-কে sample count দিয়ে weight করো।
7. Gini হলে minimum; Information Gain হলে maximum বেছে নাও।
8. Stop condition / expansion threshold থাকলে সেটি মানো।

## 6. Common mistakes

- Child-এর Gini দুটো যোগ না করে একটিকে compare করা।
- Weighted average-এ child sample count ব্যবহার না করা।
- Numeric threshold-এ `<` ও `≥` rule গুলিয়ে ফেলা।
- Gini minimum আর Information Gain maximum—দুটো উল্টো করে ফেলা।

**মনে রাখবে:** Classification Tree-তে target class; split impurity কমায়; leaf-এ class label/majority class prediction হয়।
