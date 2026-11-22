# CSE 711 — Math 4: Random Forest Regression
**বাংলা step-by-step notes | Bootstrap regression trees, SSR, averaging**

> Random Forest Regression-এর জন্য আলাদা Sir practice problem এই মুহূর্তে শনাক্ত হয়নি। তাই এই নোটে Regression Tree-এর Sir-এর Livability dataset ব্যবহার করে Random Forest Regression-এর calculation method দেখানো হয়েছে। এটি method বোঝানোর worked illustration—Sir-এর আলাদা RF Regression question বলে দাবি করা হচ্ছে না।

## 1. Classification বনাম Regression

- Target numerical হলে Random Forest Regression।
- প্রতিটি tree একটি numerical prediction দেয়।
- Final prediction = সব tree prediction-এর average।

\[
\hat y_{RF}(x)=\frac{1}{B}\sum_{b=1}^{B}\hat y_b(x)
\]

\(B\) = tree সংখ্যা; \(\hat y_b(x)\) = b-th tree-এর prediction।

## 2. Regression Tree-এর split criterion

\[
Mean=\frac{\sum y_i}{n},\qquad SSR=\sum(y_i-Mean)^2
\]

\[
SSR_{split}=SSR_L+SSR_R
\]

প্রতিটি tree-তে bootstrap sample নেওয়া হয়, তারপর feature subset থেকে split নির্বাচন করা হয়। Regression tree-র leaf prediction হলো ওই leaf-এর target mean।

## 3. Leaf mean-এর worked calculation

Sir-এর RT dataset-এ Dhaka-র root path-এর YES branch (Environment=Unhealthy) এ:
- Delhi target = 50
- Karachi target = 47

\[
LeafMean=\frac{50+47}{2}=\frac{97}{2}=48.5
\]

অতএব একটি tree যদি Dhaka-কে এই leaf-এ পাঠায়, তার prediction হবে 48.5।

## 4. Random Forest-এর final averaging — উদাহরণ

ধরা যাক একই query-র জন্য তিনটি independently trained regression tree prediction দিল:

| Tree | Prediction |
|---|---:|
| Tree 1 | 48.5 |
| Tree 2 | 50.0 |
| Tree 3 | 47.5 |

তাহলে:

\[
\hat y_{RF}=\frac{48.5+50.0+47.5}{3}
=\frac{146}{3}=48.6667
\]

Final RF prediction ≈ **48.67**।

**এখানে 50.0 ও 47.5 শুধু averaging process দেখানোর illustrative tree outputs; Sir-এর PDF থেকে আসা values নয়।** Actual exam-এ tree-wise predictions প্রশ্নে দেওয়া থাকবে অথবা tree traverse করে বের করতে হবে।

## 5. End-to-end procedure

1. Original training set থেকে bootstrap samples তৈরি করো।
2. প্রতিটি sample-এ random feature subset নিয়ে Regression Tree train করো।
3. প্রতিটি split-এর total SSR হিসাব করো।
4. Minimum SSR split নির্বাচন করো।
5. Stopping condition অনুযায়ী leaf তৈরি করো।
6. Query প্রতিটি tree-তে পাঠাও।
7. প্রতিটি tree-এর leaf mean prediction লেখো।
8. সব prediction যোগ করে tree সংখ্যায় ভাগ করো।

## 6. Common mistakes

- Regression target থাকা সত্ত্বেও Gini ব্যবহার করা।
- Tree prediction-এর বদলে training target-গুলোর সরাসরি average নেওয়া।
- Random Forest Regression-এ majority vote করা—এটি Classification-এর নিয়ম।
- Bootstrap sample-এ একই row একাধিকবার আসতে পারে—এটি ভুল নয়।

**Golden rule:** Random Forest Regression = many Regression Trees + bootstrap/feature randomness + average of numerical outputs।
