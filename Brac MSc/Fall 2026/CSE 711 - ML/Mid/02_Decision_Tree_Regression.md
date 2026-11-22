# CSE 711 — Math 2: Decision Tree Regression
**বাংলা step-by-step notes | SSR, candidate split, tree expansion, prediction**

> এই নোট Sir-এর **Practice Problem on RT.pdf**-এর Livability dataset ধরে তৈরি। Target numerical, তাই Regression Tree।

## 1. Problem ও dataset

Target: Livability Score (numeric)। Features: Safeness Score, Environment, Affordability।

| City | Safeness | Environment | Affordability | Livability |
|---|---:|---|---|---:|
| Tokyo | 88 | Excellent | Expensive | 80 |
| Seoul | 86 | Good | Affordable | 78 |
| Singapore | 84 | Good | Expensive | 75 |
| Delhi | 50 | Unhealthy | Affordable | 50 |
| New York | 70 | Good | Expensive | 79 |
| Karachi | 40 | Unhealthy | Affordable | 47 |
| Amsterdam | 90 | Excellent | Affordable | 86 |

Query Dhaka: Safeness=52, Environment=Unhealthy, Affordability=Expensive। Expansion threshold=2।

## 2. Regression Tree-তে কোন formula?

Node-এর prediction হলো target-এর mean:

\[
\bar y=\frac{\sum y_i}{n}
\]

Sum of Squared Residuals:

\[
SSR=\sum_{i=1}^{n}(y_i-\bar y)^2
\]

Split-এর total:

\[
SSR_{split}=SSR_L+SSR_R
\]

**Best split = minimum total SSR।** মনে রাখবে, শুধু একটি side-এর SSR compare করা যাবে না।

## 3. Root split: Safeness threshold

Safeness ascending order:

| City | Safeness | Livability |
|---|---:|---:|
| Karachi | 40 | 47 |
| Delhi | 50 | 50 |
| New York | 70 | 79 |
| Singapore | 84 | 75 |
| Seoul | 86 | 78 |
| Tokyo | 88 | 80 |
| Amsterdam | 90 | 86 |

Adjacent midpoint candidates: 45, 60, 77, 85, 87, 89।

### Full calculation: threshold = 60

Left (`Safeness < 60`): Karachi=47, Delhi=50।

\[
Mean_L=(47+50)/2=48.5
\]

\[
SSR_L=(47-48.5)^2+(50-48.5)^2
=2.25+2.25=4.5
\]

Right (`Safeness ≥ 60`): 79,75,78,80,86।

\[
Mean_R=(79+75+78+80+86)/5=398/5=79.6
\]

\[
\begin{aligned}
SSR_R={}&(79-79.6)^2+(75-79.6)^2\\
&+(78-79.6)^2+(80-79.6)^2+(86-79.6)^2\\
={}&0.36+21.16+2.56+0.16+40.96=65.2
\end{aligned}
\]

\[
SSR_{total}=4.5+65.2=\boxed{69.7}
\]

Candidate summary (Sir-এর PDF):

| Threshold | Total SSR |
|---:|---:|
| 45 | 795.33 |
| 60 | **69.7** |
| 77 | 689.42 |
| 85 | 859.42 |
| 87 | 1028.8 |
| 89 | 1178.83 |

Safeness-এর best split `<60` with SSR=69.7।

## 4. Categorical feature split

### Environment = Unhealthy?

- YES: Delhi=50, Karachi=47 → mean=48.5, SSR=4.5
- NO: 80,78,75,79,86 → mean=79.6, SSR=65.2

\[
SSR_{Environment}=4.5+65.2=69.7
\]

অতএব Environment split-ও 69.7—Safeness `<60`-এর সঙ্গে tie।

### Affordability = Expensive?

Expensive: 80,75,79 → mean=78।

\[
SSR_E=(80-78)^2+(75-78)^2+(79-78)^2
=4+9+1=14
\]

Affordable: 78,50,47,86 → mean=65.25।

\[
SSR_A=(78-65.25)^2+(50-65.25)^2+(47-65.25)^2+(86-65.25)^2
\]
\[
=162.5625+232.5625+333.0625+430.5625=1158.75
\]

\[
SSR_{total}=14+1158.75=\boxed{1172.75}
\]

এখানে 14 হলো শুধু Expensive group-এর SSR; total নয়। তাই Affordability best split নয়।

## 5. Expansion-এর পর right branch

PDF-এর পরের ধাপের five rows: New York(70,79), Singapore(84,75), Seoul(86,78), Tokyo(88,80), Amsterdam(90,86)।

Candidate thresholds: 77,85,87,89। PDF-এর total SSR: 64.75, 42.6667, 26.6667, **14**। তাই `<89` best।

- Safeness <89: চারটি city → target 79,75,78,80; mean=78; SSR=14।
- Safeness ≥89: Amsterdam → target 86; SSR=0।
- Total = 14।

পরের চার-row branch (79,75,78,80): PDF অনুযায়ী `<87` split-এর SSR=8.6667; Environment Good/Excellent split-ও 8.6667 tie।
- `<87` group: New York, Singapore, Seoul → mean=(79+75+78)/3=77.3333।
- `≥87` group: Tokyo → prediction=80।

পরের তিন-row branch (79,75,78):
- Safeness `<77`: New York? এখানে Safeness values 70,84,86; তাই `<77` → New York, target=79।
- `≥77` → Singapore=75, Seoul=78; mean=(75+78)/2=76.5।
- PDF best SSR=4.5।

## 6. Sir-এর final query prediction

Sir-এর final page-এর root rule: `Environment = Unhealthy?`

```text
          Environment = Unhealthy?
                /          \
              YES           NO
               |             |
          Mean = 48.5     Mean = 79.6
```

Dhaka-র Environment = Unhealthy → YES leaf।

\[
\boxed{\hat y_{Dhaka}=48.5}
\]

## 7. Exam checklist

1. Numerical target → Regression Tree।
2. Candidate numeric threshold = adjacent sorted feature values-এর midpoint।
3. প্রতিটি side-এর target mean বের করো।
4. প্রতিটি observation-এর `(y−mean)^2` বের করে যোগ করো।
5. দুই side-এর SSR যোগ করো।
6. Minimum total SSR split নির্বাচন করো।
7. Query-র feature condition ধরে leaf-এ যাও; leaf prediction = target mean।
8. Expansion threshold 2 হলে 2 বা কম sample-এর node আর expand করবে না।

**সতর্কতা:** Root-এ Safeness `<60` ও Environment=`Unhealthy` দুটোই SSR 69.7—tie। Sir-এর final query page Environment route ব্যবহার করেছে, তাই Dhaka prediction 48.5।
