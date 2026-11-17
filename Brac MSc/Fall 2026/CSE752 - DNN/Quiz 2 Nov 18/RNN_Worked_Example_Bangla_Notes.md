# RNN Language Modeling --- সহজ বাংলা Worked Example

**বিষয়:** Recurrent Neural Network (RNN)\
**কাজ:** "The Titanic sank" বাক্যটি একবারে একটি token পড়ে পরের token
predict করা।\
**এই নোটের নিয়ম:** Technical term ও formula English-এ থাকবে; ব্যাখ্যা একদম
সহজ বাংলায় দেওয়া হয়েছে।

------------------------------------------------------------------------

## Step 1: প্রশ্নে কী করতে বলেছে?

আমাদের sentence:

**The Titanic sank**

বাক্যের শুরু বোঝাতে `<BOS>` (Beginning of Sentence) যোগ করা হয়েছে।

RNN তিন ধাপে prediction করবে:

  Time step   Input     Target
  ----------- --------- ---------
  1           `<BOS>`   The
  2           The       Titanic
  3           Titanic   sank

**খুব গুরুত্বপূর্ণ:** Time step 3-এ Input হলো `Titanic`, আর Target হলো `sank`।
আমরা `sank`-কে আবার input হিসেবে দেব না। এখানেই calculation শেষ।

## Step 2: Vocabulary তৈরি

Vocabulary মানে এই example-এ ব্যবহৃত সব token-এর তালিকা।

\[
V=\[`\texttt{<BOS>}`{=tex}, `\text{The}`{=tex}, `\text{Titanic}`{=tex}, `\text{sank}`{=tex}\]
\]

Vocabulary size:

\[ `\boxed{|V|=4}`{=tex} \]

আমরা সব calculation-এ এই একই order ব্যবহার করব।

    Index Token
  ------- ---------
        1 `<BOS>`
        2 The
        3 Titanic
        4 sank

Vocabulary-তে ৪টি token আছে, তাই Input vector-এ ৪টি value থাকবে এবং
Output Layer-এও ৪টি neuron থাকবে।

## Step 3: One-hot Encoding

**One-hot Encoding**-এ প্রতিটি token-এর জন্য এমন vector বানানো হয়, যেখানে
একটি value `1` এবং বাকি সব `0` থাকে।

  Token     One-hot vector
  --------- ------------------
  `<BOS>`   (\[1,0,0,0\]\^T)
  The       (\[0,1,0,0\]\^T)
  Titanic   (\[0,0,1,0\]\^T)
  sank      (\[0,0,0,1\]\^T)

যে position-এ `1` থাকবে, সেই position token-টিকে চিহ্নিত করবে।

## Step 4: RNN Architecture ও Formula

RNN প্রতিটি Time step-এ: 1. Current Input এবং Previous Hidden State
একসঙ্গে নেয়। 2. `tanh` প্রয়োগ করে নতুন Hidden State তৈরি করে। 3. Hidden
State থেকে Output Logits বের করে। 4. Softmax দিয়ে Probability বের করে।

### Forward Propagation Equations

**Equation 1:**

\[ a_t=W_xx_t+W_hh\_{t-1}+b_h \]

এখানে Input এবং আগের Hidden State মিলিয়ে নতুন state-এর আগের value তৈরি
হয়।

**Equation 2:**

\[ h_t=`\tanh`{=tex}(a_t) \]

এখানে `tanh` প্রয়োগ করে নতুন Hidden State পাওয়া যায়।

**Equation 3:**

\[ z_t=W_yh_t+b_y \]

এখানে Hidden State থেকে Output Logits পাওয়া যায়।

**Equation 4:**

\[ p_t=`\operatorname{softmax}`{=tex}(z_t) \]

এখানে Logits থেকে Probability পাওয়া যায়।

### Symbol-গুলোর অর্থ

  Symbol       সহজ অর্থ
  ------------ --------------------------
  (x_t)        বর্তমান Input
  (h\_{t-1})   আগের Hidden State
  (a_t)        Activation-এর আগের value
  (h_t)        নতুন Hidden State
  (W_x)        Input-to-hidden Weight
  (W_h)        Hidden-to-hidden Weight
  (W_y)        Hidden-to-output Weight
  (b_h)        Hidden Bias
  (b_y)        Output Bias
  (z_t)        Output Logits
  (p_t)        Predicted Probability

## Step 5: Weight Initialize করা এবং Weight Sharing

প্রশ্নে দেওয়া আছে:

\[ W_x=I_4 \]

\[ W_h=0.1I_4 \]

\[ b_h=0,`\qquad `{=tex}b_y=0 \]

এখানে (I_4) হলো 4×4 Identity Matrix:

\[ I_4=
```{=tex}
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}
```
\]

Output Weight Matrix:

\[ W_y=4
```{=tex}
\begin{bmatrix}
0&0&0&0\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{bmatrix}
```
\]

Vocabulary order: `[<BOS>, The, Titanic, sank]`।

এই matrix-টি এমনভাবে দেওয়া হয়েছে, যাতে example-এর পরের শব্দগুলোর জন্য বেশি
score আসে:

\[
`\texttt{<BOS>}`{=tex}`\rightarrow`{=tex}`\text{The}`{=tex}`\rightarrow`{=tex}`\text{Titanic}`{=tex}`\rightarrow`{=tex}`\text{sank}`{=tex}
\]

Initial Hidden State:

\[ `\boxed{h_0=[0,0,0,0]^T}`{=tex} \]

### Weight Sharing কী?

Time step 1, 2 ও 3---সব জায়গায় একই (W_x), (W_h), এবং (W_y) ব্যবহার হবে।

প্রতিটি word-এর জন্য নতুন Weight Matrix বানানো হবে না। Input এবং Hidden
State বদলাবে, কিন্তু Weight Matrix একই থাকবে।

এটাকেই **Weight Sharing** বলে।

## Step 6: Time Step 1 --- Input `<BOS>`, Target `The`

### 6.1 Input Vector

\[ x_1=\[1,0,0,0\]\^T \]

Previous Hidden State:

\[ h_0=\[0,0,0,0\]\^T \]

### 6.2 Pre-activation বের করি

Formula:

\[ a_1=W_xx_1+W_hh_0 \]

Value বসাই:

\[ a_1=I_4
```{=tex}
\begin{bmatrix}1\\0\\0\\0\end{bmatrix}
```
+0.1I_4
```{=tex}
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
```
\]

তাই,

\[ `\boxed{a_1=[1,0,0,0]^T}`{=tex} \]

### 6.3 tanh প্রয়োগ করে Hidden State বের করি

\[ h_1=`\tanh`{=tex}(a_1) \]

\[ =\[`\tanh`{=tex}(1),0,0,0\]\^T \]

যেহেতু (`\tanh`{=tex}(1)`\approx0.761594`{=tex}),

\[ `\boxed{h_1=[0.761594,0,0,0]^T}`{=tex} \]

### 6.4 Output Logits বের করি

\[ z_1=W_yh_1 \]

\[ `\boxed{z_1=[0,3.046377,0,0]^T}`{=tex} \]

### 6.5 Softmax প্রয়োগ করি

Formula:

\[ p_i=`\frac{e^{z_i}}{\sum_{j=1}^{4}e^{z_j}}`{=tex} \]

এই step-এর Exponential values:

\[ \[1, 21.038974, 1, 1\] \]

সবগুলো যোগ করলে:

\[ 1+21.038974+1+1=24.038974 \]

তাই Probability:

\[ `\boxed{
p_1=[0.041599,\ 0.875203,\ 0.041599,\ 0.041599]
}`{=tex} \]

Vocabulary order অনুযায়ী `The`-এর probability:

\[ `\boxed{P_1(\text{The})=0.875203=87.52\%}`{=tex} \]

অর্থাৎ RNN প্রথম ধাপে `The` predict করেছে।

## Step 7: Time Step 2 --- Input `The`, Target `Titanic`

### 7.1 Input ও Previous Hidden State

\[ x_2=\[0,1,0,0\]\^T \]

আগের ধাপের Hidden State:

\[ h_1=\[0.761594,0,0,0\]\^T \]

### 7.2 Pre-activation

\[ a_2=W_xx_2+W_hh_1 \]

# \[

```{=tex}
\begin{bmatrix}0\\1\\0\\0\end{bmatrix}
```
+0.1
```{=tex}
\begin{bmatrix}0.761594\\0\\0\\0\end{bmatrix}
```
\]

\[ `\boxed{a_2=[0.076159,1,0,0]^T}`{=tex} \]

### 7.3 tanh এবং Hidden State

\[ h_2=`\tanh`{=tex}(a_2) \]

\[ `\boxed{h_2=[0.076013,0.761594,0,0]^T}`{=tex} \]

### 7.4 Output Logits

\[ z_2=W_yh_2 \]

\[ `\boxed{z_2=[0,0.304050,3.046377,0]^T}`{=tex} \]

### 7.5 Softmax Probability

\[ `\boxed{
p_2=[0.040993,\ 0.055560,\ 0.862454,\ 0.040993]
}`{=tex} \]

Correct Target হলো `Titanic`। তাই:

\[ `\boxed{P_2(\text{Titanic})=0.862454=86.25\%}`{=tex} \]

## Step 8: Time Step 3 --- Input `Titanic`, Target `sank`

এটাই প্রশ্নের শেষ Time step।

### 8.1 Input ও Previous Hidden State

\[ x_3=\[0,0,1,0\]\^T \]

আগের Hidden State:

\[ h_2=\[0.076013,0.761594,0,0\]\^T \]

### 8.2 Pre-activation

\[ a_3=W_xx_3+W_hh_2 \]

# \[

```{=tex}
\begin{bmatrix}0\\0\\1\\0\end{bmatrix}
```
+0.1
```{=tex}
\begin{bmatrix}0.076013\\0.761594\\0\\0\end{bmatrix}
```
\]

\[ `\boxed{a_3=[0.007601,0.076159,1,0]^T}`{=tex} \]

### 8.3 tanh প্রয়োগ করে Hidden State

\[ h_3=`\tanh`{=tex}(a_3) \]

\[ `\boxed{h_3=[0.007601,0.076013,0.761594,0]^T}`{=tex} \]

### 8.4 Output Logits

\[ z_3=W_yh_3 \]

\[ `\boxed{z_3=[0,0.030404,0.304050,3.046377]^T}`{=tex} \]

### 8.5 Softmax Probability

প্রথমে Exponential values বের করি:

\[ e\^{z_3}`\approx[1,\ 1.030871,\ 1.355337,\ 21.038974]`{=tex}\]

সবগুলো যোগ করি:

\[ 1+1.030871+1.355337+21.038974=24.425182 \]

এখন প্রতিটি value-কে sum দিয়ে ভাগ করি:

\[ p_3= `\frac{[1,\ 1.030871,\ 1.355337,\ 21.038974]}`{=tex} {24.425182}
\]

তাই,

\[ `\boxed{
p_3=[0.040941,\ 0.042205,\ 0.055489,\ 0.861364]
}`{=tex} \]

### 8.6 Prediction বুঝি

Vocabulary order হলো `[<BOS>, The, Titanic, sank]`।

  Token                  Probability
  ---------- -----------------------
  `<BOS>`           0.040941 = 4.09%
  The               0.042205 = 4.22%
  Titanic           0.055489 = 5.55%
  **sank**     **0.861364 = 86.14%**

সবচেয়ে বেশি probability পেয়েছে `sank`। এটাই সঠিক Target।

## Step 9: Cross-Entropy Loss (Time Step 3)

**Cross-Entropy Loss কী?** Model সঠিক উত্তরকে কত probability দিয়েছে, তা
দিয়ে loss হিসাব করা হয়।

Correct Target `sank`-এর One-hot vector:

\[ y_3=\[0,0,0,1\]\^T \]

Categorical Cross-Entropy Formula:

\[ L_3=-`\sum`{=tex}*{i=1}\^{4}y*{3,i}`\ln`{=tex}(p\_{3,i}) \]

এখানে শুধু সঠিক target-এর জায়গায় `1` আছে। তাই বাকি term-গুলো শূন্য হয়ে যায়।

\[ L_3=-`\ln`{=tex}(p_3(`\text{sank}`{=tex})) \]

\[ =-`\ln`{=tex}(0.861364) \]

\[ `\boxed{L_3\approx0.149238\text{ nats}}`{=tex} \]

**সহজ কথা:** সঠিক উত্তরের probability যত বেশি হবে, Loss তত কম হবে।
Probability যদি 1-এর কাছাকাছি হয়, Loss প্রায় 0 হবে।

### তিনটি Time Step-এর Loss

\[ L_1=-`\ln`{=tex}(0.875203)`\approx0.133300`{=tex} \]

\[ L_2=-`\ln`{=tex}(0.862454)`\approx0.147973`{=tex} \]

\[ L_3=-`\ln`{=tex}(0.861364)`\approx0.149238`{=tex} \]

Average Loss:

\[ L\_{`\text{average}`{=tex}}=`\frac{L_1+L_2+L_3}{3}`{=tex} \]

\[ =`\frac{0.133300+0.147973+0.149238}{3}`{=tex} \]

\[ `\boxed{L_{\text{average}}\approx0.143504\text{ nats}}`{=tex} \]

## Step 10: Entropy (Time Step 3)

**Entropy কী?** Model-এর পুরো predicted probability distribution কতটা
uncertain বা ছড়ানো, তা Entropy দিয়ে বোঝা যায়।

Formula:

\[ H(p_3)=-`\sum`{=tex}*{i=1}\^{4}p*{3,i}`\ln`{=tex}(p\_{3,i}) \]

এখানে চারটি probability-ই ব্যবহার করতে হবে।

\[
```{=tex}
\begin{aligned}
H(p_3)=-[&
0.040941\ln(0.040941)\\
&+0.042205\ln(0.042205)\\
&+0.055489\ln(0.055489)\\
&+0.861364\ln(0.861364)]
\end{aligned}
```
\]

\[ `\boxed{H(p_3)\approx0.553421\text{ nats}}`{=tex} \]

### Entropy ও Cross-Entropy Loss-এর পার্থক্য

  -----------------------------------------------------------------------
  Entropy                             Cross-Entropy Loss
  ----------------------------------- -----------------------------------
  পুরো probability distribution-এর     সঠিক Target-কে দেওয়া probability
  uncertainty মাপে।                   দিয়ে loss মাপে।

  সব predicted probability ব্যবহার     One-hot target হলে সঠিক class-এর
  করে।                                probability-ই মূল বিষয়।

  এখানে 0.553421 nats।                এখানে 0.149238 nats।
  -----------------------------------------------------------------------

সহজভাবে: - **Entropy:** Model-এর prediction কতটা uncertain? -
**Cross-Entropy:** Model সঠিক উত্তর `sank`-কে কতটা probability দিয়েছে?

কোনো model ভুল উত্তরে খুব বেশি confident হলেও তার Entropy কম হতে পারে, কিন্তু
Cross-Entropy Loss বেশি হতে পারে।

## Final Summary

    Time step Input     Correct Target     Target Probability
  ----------- --------- ---------------- --------------------
            1 `<BOS>`   The                            87.52%
            2 The       Titanic                        86.25%
            3 Titanic   sank                           86.14%

### Final Answer

\[ `\boxed{
P(\text{sank}\mid\texttt{<BOS>},\text{The},\text{Titanic})
\approx0.861364
}`{=tex} \]

\[ `\boxed{\text{Cross-Entropy Loss}\approx0.149238\text{ nats}}`{=tex}
\]

\[ `\boxed{\text{Prediction Entropy}\approx0.553421\text{ nats}}`{=tex}
\]

## পরীক্ষার জন্য মনে রাখবে

1.  **Vocabulary:** Model যে token-গুলো predict করতে পারে, সেগুলোর তালিকা।
2.  **One-hot Encoding:** একটি `1` এবং বাকি সব `0` দিয়ে token প্রকাশ করা।
3.  **Hidden State:** আগের input-এর তথ্য পরের Time step-এ নিয়ে যায়।
4.  **Weight Sharing:** প্রতিটি Time step-এ একই Weight Matrix ব্যবহার করা।
5.  **tanh:** নতুন Hidden State তৈরি করতে ব্যবহৃত Activation Function।
6.  **Logits:** Softmax-এর আগের raw score।
7.  **Softmax:** Logits-কে Probability-তে বদলায়; সব Probability-এর যোগফল
    1।
8.  **Cross-Entropy:** সঠিক Target-এর prediction কত ভালো হয়েছে, তা মাপে।
9.  **Entropy:** পুরো Probability Distribution-এর uncertainty মাপে।
10. **Time step 3:** Input `Titanic`, Target `sank`; `sank`-কে Time step
    4-এর Input করা হবে না।

### পুরো RNN Flow

প্রতিটি Time step-এ:

\[
`\boxed{x_t,h_{t-1}\rightarrow a_t\rightarrow h_t\rightarrow z_t\rightarrow p_t}`{=tex}
\]

তিনটি Time step:

\[ `\boxed{
\texttt{<BOS>}\rightarrow\text{The}\rightarrow\text{Titanic}\rightarrow\text{sank}
}`{=tex} \]

**Scope:** এই example-এ Forward Propagation, Loss ও Entropy হিসাব করা
হয়েছে। Backpropagation Through Time বা Weight Update করা হয়নি।
