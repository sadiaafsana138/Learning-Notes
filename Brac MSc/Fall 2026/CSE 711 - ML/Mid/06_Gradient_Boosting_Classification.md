# CSE 711 — Math 6: Gradient Boosting Classification
**বাংলা step-by-step notes | Class probabilities, softmax, cross-entropy/KL, negative gradient**

> Sir-এর lecture material-এ Gradient Boosting Classification-এর example হলো handwritten capital letter recognition: 26 classes A–Z। এটি numerical stump-calculation practice নয়; lecture-এর probability/loss calculation ধাপে ধাপে বোঝানো হয়েছে।

## 1. Problem setup

একটি handwritten letter-এর feature vector দেওয়া আছে; true label = G। Model প্রতিটি class-এর জন্য একটি score দেয়:

\[
F_A(x),F_B(x),\ldots,F_Z(x)
\]

এগুলো probability নয়; এগুলো class scores/logits।

## 2. Scores থেকে probability: Softmax

\[
P_c(x)=\frac{e^{F_c(x)}}{\sum_{j=A}^{Z}e^{F_j(x)}}
\]

- Numerator: নির্দিষ্ট class-এর exponentiated score।
- Denominator: সব class-এর exponentiated score-এর sum।
- সব class probability যোগ করলে 1 হয়।

**Mini calculation (৩-class illustration):** ধরা যাক scores A=2, B=1, C=0।

\[
e^2=7.389,\quad e^1=2.718,\quad e^0=1
\]

\[
Z=7.389+2.718+1=11.107
\]

\[
P_A=7.389/11.107=0.6652
\]
\[
P_B=2.718/11.107=0.2447,\quad
P_C=1/11.107=0.0900
\]

Check: 0.6652+0.2447+0.0900 ≈ 1.000।

এটি softmax বোঝানোর illustration; Sir-এর 26-class example-এর actual score list নয়।

## 3. True label-কে probability distribution বানানো

True label G হলে one-hot target:

\[
Y_G=1,\qquad Y_c=0\ (c\ne G)
\]

অর্থাৎ G-এর জন্য 1, বাকি 25 class-এর জন্য 0।

Sir-এর slide-এ একটি example predicted distribution-এ \(P_G=0.3\) দেখানো হয়েছে; বাকি class probabilities-ও থাকে এবং total 1 হয়।

## 4. Cross-Entropy / KL divergence

One-hot target-এর ক্ষেত্রে cross-entropy:

\[
CE(Y,P)=-\sum_c Y_c\log P_c
\]

যেহেতু true class শুধু G:

\[
CE=-\log P_G
\]

যদি \(P_G=0.3\):

\[
CE=-\ln(0.3)=1.2040
\]

G-এর predicted probability যত বাড়বে, loss তত কমবে। যেমন \(P_G=0.8\):

\[
CE=-\ln(0.8)=0.2231
\]

**Interpretation:** model true class-কে বেশি probability দিলে ভালো; ভুল class-কে বেশি probability দিলে loss বাড়ে।

KL divergence:

\[
D_{KL}(Y\|P)=\sum_c Y_c\ln\frac{Y_c}{P_c}
\]

One-hot target-এ zero terms বাদ দিলে এটি \(-\ln P_G\)-এর সমান (zero-probability convention অনুযায়ী)।

## 5. Gradient Boosting কীভাবে improve করে?

প্রতিটি round-এ:
1. Current model class scores \(F_c(x)\) থেকে probabilities \(P_c(x)\) বের করে।
2. True distribution \(Y_c(x)\) ও predicted distribution-এর difference/negative gradient হিসাব করে।
3. নতুন weak learner/tree এই negative-gradient information fit করে।
4. Class score update হয়; পরের round-এ probability true distribution-এর কাছাকাছি যায়।

Conceptually:

\[
F_c^{(m)}(x)=F_c^{(m-1)}(x)+\rho h_c^{(m)}(x)
\]

- \(h_c^{(m)}\): m-th round-এর correction learner
- \(\rho\): learning rate/shrinkage

## 6. Prediction

Final probabilities বের করার পর:

\[
\hat y=\arg\max_c P_c(x)
\]

অর্থাৎ যার probability সর্বোচ্চ, সেটিই predicted letter/class।

## 7. Exam answer structure

1. Class scores/logits লিখবে।
2. Softmax denominator \(Z=\sum e^{F_c}\) হিসাব করবে।
3. প্রতিটি class-এর probability বের করবে।
4. True label one-hot vector লিখবে।
5. Cross-entropy বা KL loss বের করবে।
6. Negative gradient দিয়ে next learner কীভাবে score adjust করে তা লিখবে।
7. Highest probability class = final prediction।

**Note:** Sir-এর slide-এ 26-class letter-recognition framework আছে; উপরের 3-class সংখ্যাগুলো softmax ও loss-এর arithmetic বোঝানোর আলাদা illustration।
