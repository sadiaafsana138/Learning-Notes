# CNN: Handwritten Letter Recognition --- সহজ বাংলা Worked Example

**বিষয়:** Convolutional Neural Network (CNN)\
**কাজ:** ৬×৬ binary image দেখে ছবিটি ইংরেজি ২৬টি অক্ষরের মধ্যে কোনটি, তা
predict করা।\
**এই নোটের নিয়ম:** Technical term ও formula English-এ থাকবে; ব্যাখ্যা একদম
সহজ বাংলায় দেওয়া হয়েছে।

------------------------------------------------------------------------

## Step 1: প্রশ্নে কী করতে বলেছে?

একটি ৬×৬ image-এ বড় হাতের **I** অক্ষরটি দেখানো হয়েছে। এখানে অক্ষরটিকে শুধু
একটি সোজা vertical line হিসেবে ধরা হয়েছে।

-   `1` = কালো pixel বা ink
-   `0` = সাদা background
-   Image size = 6 × 6

আমাদের কাজ হলো CNN-এর ধাপগুলো একে একে করে শেষে **I হওয়ার probability**
বের করা।

## Step 2: Input Image

\[ X=
```{=tex}
\begin{bmatrix}
0&0&1&0&0&0\\
0&0&1&0&0&0\\
0&0&1&0&0&0\\
0&0&1&0&0&0\\
0&0&1&0&0&0\\
0&0&1&0&0&0
\end{bmatrix}
```
\]

এখানে ৩ নম্বর column-এ সবগুলো `1` আছে। তাই মাঝখানে একটি vertical stroke
তৈরি হয়েছে।

## Step 3: Convolution Kernel

আমাদের দেওয়া 3×3 Kernel:

\[ K=
```{=tex}
\begin{bmatrix}
-1&2&-1\\
-1&2&-1\\
-1&2&-1
\end{bmatrix}
```
\]

**Kernel কী?** Kernel হলো ছোট weight matrix, যেটা image-এর ওপর slide করে
কোনো pattern খুঁজে বের করে।

এই Kernel-এর: - মাঝের column-এর weight `2`। - বাম ও ডান column-এর weight
`-1`।

তাই image-এর vertical line যখন Kernel-এর মাঝের column-এর সঙ্গে মিলে যায়,
তখন বড় positive value পাওয়া যায়।

দেওয়া আছে: - Kernel size = 3×3 - Padding (P=0) (Valid Padding) - Stride
(S=1)

### Output size বের করি

Formula:

\[ `\text{Output size}`{=tex}=`\frac{N-F+2P}{S}`{=tex}+1 \]

এখানে (N=6, F=3, P=0, S=1)।

\[ =`\frac{6-3+2(0)}{1}`{=tex}+1=4 \]

তাই Convolution output হবে **4×4**।

## Step 4: Convolution Calculation

Convolution করার নিয়ম: 1. Kernel-কে image-এর 3×3 অংশের ওপর বসাই। 2.
পাশাপাশি থাকা value-গুলো multiply করি। 3. সব গুণফল যোগ করি। 4. Kernel এক
ঘর সরিয়ে আবার হিসাব করি।

প্রতিটি row একই হওয়ায় চারটি horizontal position-এর হিসাব সব output row-তে
একই হবে।

### Position 1: Column 1--3

\[ P_1=
```{=tex}
\begin{bmatrix}
0&0&1\\
0&0&1\\
0&0&1
\end{bmatrix}
```
\]

\[ s_1=(-1`\times0`{=tex}+2`\times0`{=tex}-1`\times1`{=tex})
+(-1`\times0`{=tex}+2`\times0`{=tex}-1`\times1`{=tex})
+(-1`\times0`{=tex}+2`\times0`{=tex}-1`\times1`{=tex}) \]

\[ s_1=-1-1-1=`\boxed{-3}`{=tex} \]

### Position 2: Column 2--4

\[ P_2=
```{=tex}
\begin{bmatrix}
0&1&0\\
0&1&0\\
0&1&0
\end{bmatrix}
```
\]

\[ s_2=(2)+(2)+(2)=`\boxed{6}`{=tex} \]

এখানে vertical line Kernel-এর মাঝের column-এ পড়েছে। তাই positive
response `6` এসেছে।

### Position 3: Column 3--5

\[ P_3=
```{=tex}
\begin{bmatrix}
1&0&0\\
1&0&0\\
1&0&0
\end{bmatrix}
```
\]

\[ s_3=(-1)+(-1)+(-1)=`\boxed{-3}`{=tex} \]

### Position 4: Column 4--6

\[ P_4=
```{=tex}
\begin{bmatrix}
0&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
```
\]

\[ s_4=`\boxed{0}`{=tex} \]

### সম্পূর্ণ Feature Map

চারটি result হলো (\[-3,6,-3,0\])। যেহেতু প্রতিটি image row একই, তাই
output-এর চারটি row-ও একই হবে।

\[ Z=
```{=tex}
\begin{bmatrix}
-3&6&-3&0\\
-3&6&-3&0\\
-3&6&-3&0\\
-3&6&-3&0
\end{bmatrix}
```
\]

**মনে রাখবে:** যেখানে vertical stroke Kernel-এর মাঝখানে পড়েছে, সেখানে
`6` পাওয়া গেছে।

## Step 5: ReLU Activation

ReLU-এর Formula:

\[ `\operatorname{ReLU}`{=tex}(x)=`\max`{=tex}(0,x) \]

সহজ নিয়ম: - Positive number আগের মতো থাকবে। - Negative number হলে `0`
হবে। - `0` হলে `0`-ই থাকবে।

তাই:

\[
-3`\rightarrow0`{=tex},`\quad 6`{=tex}`\rightarrow6`{=tex},`\quad 0`{=tex}`\rightarrow0`{=tex}
\]

ReLU করার পর:

\[ A=
```{=tex}
\begin{bmatrix}
0&6&0&0\\
0&6&0&0\\
0&6&0&0\\
0&6&0&0
\end{bmatrix}
```
\]

**কেন ReLU ব্যবহার করি?** Negative value বাদ দিয়ে positive feature
response রেখে দেয়।

## Step 6: Max Pooling

এখানে দেওয়া আছে: - Pooling window = 2×2 - Stride = 2

**Max Pooling কী?** প্রতিটি 2×2 block থেকে সবচেয়ে বড় value নেওয়া হয়।

ReLU-এর পরের matrix:

\[ A=
```{=tex}
\begin{bmatrix}
0&6&0&0\\
0&6&0&0\\
0&6&0&0\\
0&6&0&0
\end{bmatrix}
```
\]

এখন চারটি block-এর maximum বের করি।

**Block 1 (Top-left):**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&6\\0&6\end{bmatrix}
```
=6 \]

**Block 2 (Top-right):**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&0\\0&0\end{bmatrix}
```
=0 \]

**Block 3 (Bottom-left):**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&6\\0&6\end{bmatrix}
```
=6 \]

**Block 4 (Bottom-right):**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&0\\0&0\end{bmatrix}
```
=0 \]

তাই Pooled Feature Map:

\[ P=
```{=tex}
\begin{bmatrix}
6&0\\
6&0
\end{bmatrix}
```
\]

এখানে value-এর সংখ্যা ১৬টি থেকে কমে ৪টি হয়েছে। Max Pooling শুধু maximum
নেয়; এই ধাপে নতুন weight শেখে না।

## Step 7: Flatten

Fully Connected Layer-এ পাঠানোর আগে matrix-কে এক লাইনের vector বানাতে
হয়। এই কাজের নাম **Flatten**।

Row ধরে পড়লে:

\[ P=
```{=tex}
\begin{bmatrix}
6&0\\
6&0
\end{bmatrix}
\Rightarrow
```
F=
```{=tex}
\begin{bmatrix}
6\\0\\6\\0
\end{bmatrix}
```
\]

অর্থাৎ,

\[ `\boxed{F=[6,0,6,0]^T}`{=tex} \]

## Step 8: Fully Connected Layer

আমাদের ২৬টি class আছে:

\[ C={A,B,C,`\ldots`{=tex},Z} \]

তাই Output Layer-এ ২৬টি neuron থাকবে। প্রতিটি neuron একটি letter-এর score
বের করবে।

Formula:

\[ z=WF+b \]

এখানে: - (W) = Weight matrix (26×4) - (F) = Flattened vector (4×1) - (b)
= Bias (26×1) - (z) = Logits (26×1)

প্রশ্নে I-এর জন্য weight দেওয়া আছে:

\[ w_I=\[0.5, 0, 0.5, 0\] \]

অন্য ২৫টি letter-এর weight শূন্য এবং সব bias-ও শূন্য।

**মনে রাখবে:** এগুলো প্রশ্নে দেওয়া illustrative weight; Training করে শেখা
weight নয়।

### I-এর Logit বের করি

\[ z_I=0.5(6)+0(0)+0.5(6)+0(0) \]

\[ =3+0+3+0=`\boxed{6}`{=tex} \]

অন্য সব letter-এর logit `0`।

অর্থাৎ: - I-এর logit = 6 - বাকি ২৫টি letter-এর logit = 0

**Logit probability নয়।** Softmax প্রয়োগ করার আগে এগুলো শুধু score।

## Step 9: Softmax এবং I-এর Probability

Softmax-এর Formula:

\[ P(i)=`\frac{e^{z_i}}{\sum_{j=1}^{26}e^{z_j}}`{=tex} \]

I-এর logit `6`; অন্য ২৫টি logit `0`।

\[ P(I)=`\frac{e^6}{e^6+25e^0}`{=tex} \]

আমরা জানি:

\[ e^6`\approx403.4288`{=tex},`\qquad `{=tex}e^0=1 \]

তাই,

\[ P(I)=`\frac{403.4288}{403.4288+25}`{=tex} \]

\[ =`\frac{403.4288}{428.4288}`{=tex} \]

\[ `\boxed{P(I)\approx0.941647}`{=tex} \]

Percentage-এ:

\[ 0.941647`\times100`{=tex}%=`\boxed{94.16\%}`{=tex} \]

## Final Answer

CNN model ছবিটিকে uppercase **I** হিসেবে classify করার probability
দিয়েছে প্রায় **94.16%**।

  ধাপ                Output
  ------------------ ------------------
  Input Image        6×6
  Convolution        4×4
  ReLU               4×4
  Max Pooling        2×2
  Flatten            4 values
  Fully Connected    26 logits
  Softmax            26 probabilities
  Probability of I   **94.16%**

## পরীক্ষার জন্য যে কথাগুলো মনে রাখবে

1.  **Convolution:** Kernel image-এর ওপর slide করে feature খুঁজে।
2.  **Kernel/Filter:** Pattern detect করার weight matrix।
3.  **Stride:** Kernel কত ঘর করে সামনে যায়।
4.  **Padding:** Image-এর চারপাশে extra value যোগ করা; এখানে (P=0)।
5.  **Feature Map:** Convolution-এর output।
6.  **ReLU:** Negative value-কে zero করে।
7.  **Max Pooling:** প্রতিটি block-এর maximum value নেয়।
8.  **Flatten:** Matrix-কে vector বানায়।
9.  **Fully Connected:** প্রতিটি class-এর score বের করে।
10. **Softmax:** Score-কে probability-তে পরিণত করে; সব probability-এর
    যোগফল 1।

### পুরো CNN Flow

\[ `\boxed{
\text{Input}\rightarrow\text{Convolution}\rightarrow\text{ReLU}
\rightarrow\text{Max Pooling}\rightarrow\text{Flatten}
\rightarrow\text{Fully Connected}\rightarrow\text{Softmax}
}`{=tex} \]

**Scope:** এই example-এ শুধু Forward Propagation দেখানো হয়েছে।
Backpropagation বা weight update করা হয়নি।
