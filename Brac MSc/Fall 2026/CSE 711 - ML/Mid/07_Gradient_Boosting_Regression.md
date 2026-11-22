# CSE 711 — Math 7: Gradient Boosting Regression
**বাংলা step-by-step notes | Initial model, residual/negative gradient, regression tree, update**

> Sir-এর lecture text অনুযায়ী square-loss regression-এ negative gradient = residual। নিচে এই exact process-এর calculation দেওয়া হয়েছে। Sir-এর lecture extract-এ আলাদা full numeric dataset/tree table পাওয়া যায়নি, তাই arithmetic বোঝাতে ছোট labelled illustration যুক্ত করা হয়েছে।

## 1. মূল ধারণা

Gradient Boosting একটি additive model তৈরি করে। প্রথম model-এর ভুলগুলো residual/negative gradient হিসেবে বের করে, তারপর নতুন Regression Tree দিয়ে সেই ভুলের pattern শেখে।

\[
F_m(x)=F_{m-1}(x)+\rho h_m(x)
\]

- \(F_{m-1}(x)\): আগের model prediction
- \(h_m(x)\): নতুন tree-এর correction
- \(\rho\): learning rate

## 2. Square loss ও residual

Sir-এর slide-এ square loss:

\[
L(y,F)=\frac12(y-F)^2
\]

এখানে \(y\) actual target, \(F\) current prediction।

Prediction-এর respect-এ derivative:

\[
\frac{\partial L}{\partial F}=F-y
\]

Negative gradient:

\[
-\frac{\partial L}{\partial F}=y-F
\]

এটাই residual:

\[
r=y-\hat y
\]

- Residual positive → model কম predict করেছে।
- Residual negative → model বেশি predict করেছে।

## 3. Initial prediction

Square loss-এর জন্য standard initial constant model হলো target mean:

\[
F_0=\frac{1}{n}\sum_{i=1}^{n}y_i
\]

**Illustration dataset** (শুধু method বোঝাতে):

| Sample | Actual y |
|---|---:|
| 1 | 10 |
| 2 | 12 |
| 3 | 14 |
| 4 | 16 |

\[
F_0=(10+12+14+16)/4=52/4=13
\]

তাই প্রথমে প্রত্যেক sample-এর prediction 13।

## 4. Residual calculation

\[
r_i=y_i-F_0
\]

| Sample | Actual y | Initial prediction | Residual \(y-F_0\) |
|---|---:|---:|---:|
| 1 | 10 | 13 | -3 |
| 2 | 12 | 13 | -1 |
| 3 | 14 | 13 | +1 |
| 4 | 16 | 13 | +3 |

Check: residual sum = -3-1+1+3=0।

## 5. Residual-এ Regression Tree fit

এখন নতুন Regression Tree-র target আর original y নয়; target হলো residual:

| Sample | Feature x (illustration) | Residual target |
|---|---:|---:|
| 1 | 1 | -3 |
| 2 | 2 | -1 |
| 3 | 3 | +1 |
| 4 | 4 | +3 |

ধরা যাক tree split করে:
- Left leaf: x ≤ 2 → residuals -3,-1
- Right leaf: x > 2 → residuals +1,+3

Leaf outputs হবে residual mean:

\[
h_1(L)=(-3-1)/2=-2
\]

\[
h_1(R)=(1+3)/2=2
\]

অতএব নতুন tree correction:
- x≤2 হলে -2
- x>2 হলে +2

## 6. Model update

ধরা যাক learning rate \(\rho=0.5\)।

\[
F_1(x)=F_0(x)+0.5h_1(x)
\]

Left leaf:

\[
F_1=13+0.5(-2)=13-1=12
\]

Right leaf:

\[
F_1=13+0.5(2)=13+1=14
\]

Updated predictions:

| Sample | Actual y | Old prediction | Tree correction | New prediction |
|---|---:|---:|---:|---:|
| 1 | 10 | 13 | -2 | 12 |
| 2 | 12 | 13 | -2 | 12 |
| 3 | 14 | 13 | +2 | 14 |
| 4 | 16 | 13 | +2 | 14 |

নতুন residual:
- Sample 1: 10−12 = -2
- Sample 2: 12−12 = 0
- Sample 3: 14−14 = 0
- Sample 4: 16−14 = +2

আগের residual ছিল -3,-1,+1,+3; update-এর পরে absolute error কমেছে।

## 7. Next boosting round

নতুন residual/negative gradient আবার বের করো। দ্বিতীয় Regression Tree সেই নতুন residual fit করবে:

\[
F_2(x)=F_1(x)+\rho h_2(x)
\]

এভাবে নির্দিষ্ট সংখ্যক iteration বা convergence/stopping condition পর্যন্ত চলবে।

## 8. Sir-এর lecture-এর key points

- Square loss-এর negative gradient = \(y-F(x)\) = residual।
- Regression Tree residuals-এ fit হয়।
- নতুন tree আগের model-এর shortcomings compensate করে।
- General gradient boosting-এ অন্য differentiable loss function-ও ব্যবহার করা যায়।
- Absolute loss ও Huber loss square loss-এর তুলনায় outlier-এর প্রতি বেশি robust।
- Learning rate নতুন tree-এর contribution scale করে।

## 9. Exam checklist

1. Initial prediction = target mean (square loss constant model)।
2. Residual = actual − current prediction।
3. Residual-কে নতুন target ধরে Regression Tree fit।
4. Leaf output = ওই leaf-এর residual mean (basic squared-error tree)।
5. Update: old prediction + learning rate × tree output।
6. নতুন residual বের করে পরের round।
7. Final prediction = initial model + সব scaled tree contributions।

**Important:** এই illustration-এর x/y values শেখানোর জন্য তৈরি; Sir-এর slide-এ থাকা dataset হিসেবে লিখবে না। Exam-এ প্রশ্নে যে dataset দেবে, সেই values বসিয়ে একই steps করবে।
