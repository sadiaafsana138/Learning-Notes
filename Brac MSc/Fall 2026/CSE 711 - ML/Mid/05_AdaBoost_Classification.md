# CSE 711 — Math 5: AdaBoost Classification
**বাংলা step-by-step notes | Sample weights, weighted error, alpha, update, resampling**

> Sir-এর Library-তে পাওয়া **Practice Problem AdaBoost.pdf**-এ 2D points A–F, positive/negative labels, first stump, weight update এবং random-number দিয়ে নতুন dataset তৈরির প্রশ্ন আছে। নিচে সেই PDF-এর দৃশ্যমান numerical setup ও standard AdaBoost steps ব্যাখ্যা করা হলো।

## 1. AdaBoost-এর মূল ধারণা

AdaBoost sequentially weak learners (সাধারণত decision stumps) train করে। প্রতিটি round-এ ভুল classify হওয়া sample-এর weight বাড়ে, সঠিক classify হওয়া sample-এর relative weight কমে। পরের learner কঠিন sample-এ বেশি মনোযোগ দেয়।

## 2. Initial sample weights

PDF-এর প্রথম dataset-এ 6টি point A–F এবং শুরুতে uniform weight:

\[
w_i=\frac{1}{N}=\frac16=0.1667
\]

| Point | Initial weight |
|---|---:|
| A | 1/6 |
| B | 1/6 |
| C | 1/6 |
| D | 1/6 |
| E | 1/6 |
| F | 1/6 |
| Total | 6×1/6 = 1 |

## 3. First stump ও weighted error

Sir-এর PDF-এর first splitter হিসেবে `X < 2.5` দেখানো হয়েছে। Diagram অনুযায়ী:
- Left side: A, B → Positive
- Right side: C, D, E, F → predicted Positive orientation-এর বিপরীতে labels অনুযায়ী ভুল point E? PDF-এর printed total error নিচে দেওয়া।

PDF-এর table-এ first stump-এর total error:

\[
Error=0\times\frac16+1\times\frac16=\frac16=0.1666667
\]

এখানে ভুল point-এর weight 1/6; সঠিক point-গুলোর weighted error contribution 0।

**খেয়াল:** stump-এর orientation (কোন side Positive/Negative) বদলালে ভুল point বদলে যেতে পারে। PDF-এর positive orientation diagram অনুসরণ করবে।

## 4. Weak learner weight / alpha

Binary AdaBoost-এর formula:

\[
\alpha=\frac12\ln\left(\frac{1-Error}{Error}\right)
\]

PDF-এর Error = 1/6 বসাই:

\[
\alpha=\frac12\ln\left(\frac{1-1/6}{1/6}\right)
\]

\[
=\frac12\ln\left(\frac{5/6}{1/6}\right)
=\frac12\ln(5)
\]

\[
=\frac12(1.6094)=\boxed{0.8047}
\]

Error কম হলে alpha বড় হয়; learner-এর vote/importance বেশি হয়।

## 5. Weight update

Binary labels \(y_i\in\{-1,+1\}\), prediction \(h(x_i)\in\{-1,+1\}\) হলে:

\[
w_i^{new}=w_i^{old}\exp(-\alpha y_i h(x_i))
\]

- Correct prediction: \(y_ih(x_i)=+1\) → multiply by \(e^{-\alpha}\), weight কমে।
- Wrong prediction: \(y_ih(x_i)=-1\) → multiply by \(e^{+\alpha}\), weight বাড়ে।

Unnormalized weights-এর যোগফল 1 নাও হতে পারে, তাই normalize করো:

\[
Z=\sum_i w_i^{new},\qquad
\tilde w_i=\frac{w_i^{new}}{Z}
\]

**PDF-এ ভুল point-এর weight বাড়বে—এটাই প্রশ্নের গুরুত্বপূর্ণ অংশ।** কোন point ভুল হয়েছে তা stump-এর positive orientation diagram থেকে নির্ধারণ করবে।

## 6. New dataset তৈরির random-number method

Sir-এর প্রশ্নে random numbers:

`[0.15, 0.30, 0.45, 0.60, 0.75, 0.90]`

প্রথমে updated normalized weights থেকে cumulative probability বানাও:

| Point | Updated normalized weight | Cumulative range |
|---|---:|---|
| A | \(w_A\) | 0 to \(w_A\) |
| B | \(w_B\) | \(w_A\) to \(w_A+w_B\) |
| C | \(w_C\) | ... |
| D | \(w_D\) | ... |
| E | \(w_E\) | ... |
| F | \(w_F\) | ... |
| Total | 1.000 | ends at 1.000 |

প্রতিটি random number যে cumulative interval-এ পড়ে, সেই point sample হবে। একই point একাধিকবার আসতে পারে।

## 7. AdaBoost-এর final classifier

একাধিক stump-এর weighted vote:

\[
H(x)=sign\left(\sum_{m=1}^{M}\alpha_m h_m(x)\right)
\]

ধাপ:
1. প্রতিটি stump-এর prediction \(h_m(x)\) বের করো।
2. সেটিকে তার alpha দিয়ে গুণ করো।
3. সব weighted prediction যোগ করো।
4. Sum positive হলে +1, negative হলে −1।

## 8. Exam checklist

- Initial weights: \(1/N\)
- Weighted error: ভুল sample-এর weights যোগ
- Alpha: \(\frac12\ln((1-Error)/Error)\)
- Wrong sample-এর weight বাড়ে; correct sample-এর relative weight কমে
- Normalize: updated weights-এর sum 1
- Cumulative weights দিয়ে random resampling
- Final: weighted stump vote-এর sign

**Important:** এই PDF-এর stump orientation ও point labels-এর diagram দেখে ভুল point চিহ্নিত করবে; শুধু X threshold দেখে ভুল point অনুমান করবে না।
