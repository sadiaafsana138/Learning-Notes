# CNN: Handwritten Letter Recognition --- A Complete Worked Example

**Topic:** Convolutional Neural Network (CNN)\
**Task:** Classify a simplified 6 × 6 binary image as one of the 26
English letters.\
**Goal:** Understand every forward-propagation step, including the
numerical calculations.

------------------------------------------------------------------------

## 1. What problem are we solving?

Imagine a small grayscale image containing the handwritten uppercase
letter **I**. For this classroom example, the letter is represented by a
single vertical dark stroke.

-   Pixel value `1` means dark ink.
-   Pixel value `0` means white background.
-   The image has 6 rows and 6 columns.

A CNN does not directly understand the meaning of the letter. It
receives pixel values and uses filters to detect visual patterns.

## 2. Input image

The 6 × 6 input matrix is:

\[ X =
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

The third column contains the vertical ink stroke. Every row is
identical: `[0, 0, 1, 0, 0, 0]`.

> This is a deliberately simplified uppercase I. Real handwritten
> letters may have top and bottom bars or other variations.

## 3. Convolution kernel: vertical-stroke detector

We use one 3 × 3 filter:

\[ K =
```{=tex}
\begin{bmatrix}
-1&2&-1\\
-1&2&-1\\
-1&2&-1
\end{bmatrix}
```
\]

**How does this filter work?**

-   The middle column has positive weights (`2`).
-   The left and right columns have negative weights (`-1`).
-   When a vertical dark stroke lines up with the middle column, the
    filter produces a strong positive score.
-   When the stroke is on the left or right side of the filter, the
    score becomes negative.

We use: - Kernel size: 3 × 3 - Padding: 0, also called **valid
padding** - Stride: 1

### Output-size calculation

For one dimension:

\[ `\text{Output size}`{=tex} = `\frac{N-F+2P}{S}`{=tex}+1 \]

Here, (N=6), (F=3), (P=0), and (S=1).

\[ `\frac{6-3+2(0)}{1}`{=tex}+1=4 \]

So the convolution output has size **4 × 4**.

## 4. Perform convolution

Convolution means: 1. Place the 3 × 3 kernel over a 3 × 3 image patch.
2. Multiply corresponding entries. 3. Add all nine products. 4. Move the
kernel one position and repeat.

Since all input rows are identical, the four horizontal calculations
will be identical for each of the four vertical positions.

### Position 1: input columns 1--3

Patch:

\[ P_1 =
```{=tex}
\begin{bmatrix}
0&0&1\\
0&0&1\\
0&0&1
\end{bmatrix}
```
\]

Element-wise multiplication and addition:

\[ s_1=(-1`\cdot0`{=tex}+2`\cdot0`{=tex}-1`\cdot1`{=tex})
+(-1`\cdot0`{=tex}+2`\cdot0`{=tex}-1`\cdot1`{=tex})
+(-1`\cdot0`{=tex}+2`\cdot0`{=tex}-1`\cdot1`{=tex}) \]

\[ s_1=-1-1-1=`\boxed{-3}`{=tex} \]

### Position 2: input columns 2--4

Patch:

\[ P_2 =
```{=tex}
\begin{bmatrix}
0&1&0\\
0&1&0\\
0&1&0
\end{bmatrix}
```
\]

\[ s_2=(2)+(2)+(2)=`\boxed{6}`{=tex} \]

The vertical stroke is aligned with the positive middle column, so the
response is strongly positive.

### Position 3: input columns 3--5

Patch:

\[ P_3 =
```{=tex}
\begin{bmatrix}
1&0&0\\
1&0&0\\
1&0&0
\end{bmatrix}
```
\]

\[ s_3=(-1)+(-1)+(-1)=`\boxed{-3}`{=tex} \]

### Position 4: input columns 4--6

Patch:

\[ P_4 =
```{=tex}
\begin{bmatrix}
0&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}
```
\]

\[ s_4=`\boxed{0}`{=tex} \]

### Complete convolution feature map

The four horizontal scores are `[-3, 6, -3, 0]`. The same pattern
appears in all four output rows:

\[ Z =
```{=tex}
\begin{bmatrix}
-3&6&-3&0\\
-3&6&-3&0\\
-3&6&-3&0\\
-3&6&-3&0
\end{bmatrix}
```
\]

**Interpretation:** The value `6` appears where the vertical stroke
aligns with the centre column of the filter.

## 5. Apply ReLU activation

ReLU means **Rectified Linear Unit**. It is defined as:

\[ `\operatorname{ReLU}`{=tex}(x)=`\max`{=tex}(0,x) \]

In simple terms: - Positive values remain unchanged. - Negative values
become zero. - Zero remains zero.

Apply ReLU to every element of (Z):

\[
-3`\rightarrow0`{=tex},`\qquad 6`{=tex}`\rightarrow6`{=tex},`\qquad 0`{=tex}`\rightarrow0`{=tex}
\]

Therefore, the activation map is:

\[ A =
```{=tex}
\begin{bmatrix}
0&6&0&0\\
0&6&0&0\\
0&6&0&0\\
0&6&0&0
\end{bmatrix}
```
\]

**Why use ReLU?** It introduces non-linearity and keeps positive feature
responses while removing negative responses.

## 6. Apply 2 × 2 max pooling

Max pooling selects the largest value from each local region.

Settings: - Pooling window: 2 × 2 - Stride: 2 - The 4 × 4 activation map
is divided into four non-overlapping blocks.

Activation map:

\[ A =
```{=tex}
\begin{bmatrix}
0&6&0&0\\
0&6&0&0\\
0&6&0&0\\
0&6&0&0
\end{bmatrix}
```
\]

Calculate the maximum in each block.

**Block 1 --- top-left:**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&6\\0&6\end{bmatrix}
```
=6 \]

**Block 2 --- top-right:**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&0\\0&0\end{bmatrix}
```
=0 \]

**Block 3 --- bottom-left:**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&6\\0&6\end{bmatrix}
```
=6 \]

**Block 4 --- bottom-right:**

\[ `\max`{=tex}
```{=tex}
\begin{bmatrix}0&0\\0&0\end{bmatrix}
```
=0 \]

The pooled feature map is:

\[ P =
```{=tex}
\begin{bmatrix}
6&0\\
6&0
\end{bmatrix}
```
\]

Pooling reduces the number of values from 16 to 4. It keeps strong local
activations and does not learn filter weights itself.

## 7. Flatten the pooled feature map

A fully connected layer expects a one-dimensional vector. **Flattening**
converts the 2 × 2 matrix into a vector by reading row by row:

\[ P =
```{=tex}
\begin{bmatrix}
6&0\\
6&0
\end{bmatrix}
\quad\Longrightarrow\quad
```
F =
```{=tex}
\begin{bmatrix}
6\\0\\6\\0
\end{bmatrix}
```
\]

Thus:

\[ `\boxed{F=[6,0,6,0]^T}`{=tex} \]

The feature vector contains four values.

## 8. Fully connected layer: 26 output classes

The model must choose one of the 26 English letters:

\[ C={A,B,C,D,E,F,G,H,I,J,`\ldots`{=tex},Z} \]

There are 26 output neurons, one for each letter.

The fully connected layer calculates a score, called a **logit**, for
each class:

\[ z=WF+b \]

Dimensions:

-   (W`\in`{=tex}`\mathbb{R}`{=tex}\^{26`\times4`{=tex}})
-   (F`\in`{=tex}`\mathbb{R}`{=tex}\^{4`\times1`{=tex}})
-   (b`\in`{=tex}`\mathbb{R}`{=tex}\^{26`\times1`{=tex}})
-   (z`\in`{=tex}`\mathbb{R}`{=tex}\^{26`\times1`{=tex}})

For this hand-worked example, the weight row for class I is:

\[ w_I=\[0.5, 0, 0.5, 0\] \]

All other 25 class rows contain zeros. All biases are zero.

**Important:** These are illustrative weights selected to make the
arithmetic easy. They are not weights learned by training.

### Calculate the logit for letter I

Take the dot product of the I-class weight row and the flattened feature
vector:

\[ z_I=0.5(6)+0(0)+0.5(6)+0(0) \]

\[ z_I=3+0+3+0=`\boxed{6}`{=tex} \]

All other output logits are zero. Therefore, the 26 logits contain: -
Logit for I: 6 - Logit for each of the other 25 letters: 0

**Logits are not probabilities.** They are raw scores and can be any
real numbers. Softmax converts them into probabilities.

## 9. Apply Softmax

Softmax converts all 26 logits into probabilities that sum to 1.

For class (i):

\[ P(i)=`\frac{e^{z_i}}{\sum_{j=1}^{26}e^{z_j}}`{=tex} \]

For letter I, (z_I=6). The other 25 logits are zero.

\[ P(I)=`\frac{e^6}{e^6+25e^0}`{=tex} \]

Since (e\^0=1) and (e\^6`\approx403.4288`{=tex}):

\[ P(I)=`\frac{403.4288}{403.4288+25}`{=tex} \]

\[ P(I)=`\frac{403.4288}{428.4288}`{=tex} `\approx0.941647`{=tex} \]

Convert to a percentage:

\[ 0.941647`\times100`{=tex}%`\approx`{=tex}`\boxed{94.16\%}`{=tex} \]

## 10. Final result

The CNN assigns approximately **94.16% probability** to the input image
being the uppercase letter I.

  Stage              Output
  ------------------ ------------------------
  Input              6 × 6 binary image
  Convolution        4 × 4 feature map
  ReLU               4 × 4 activation map
  Max pooling        2 × 2 pooled map
  Flatten            4-element vector
  Fully connected    26 logits
  Softmax            26 class probabilities
  Probability of I   **94.16%**

## 11. CNN concepts to remember

1.  **Convolution:** A filter slides over the image and detects local
    patterns.
2.  **Kernel/filter:** A small matrix of weights used to detect a
    feature.
3.  **Stride:** How many pixels the filter moves at each step.
4.  **Padding:** Extra border values added around an image; here,
    padding is zero.
5.  **Feature map:** The output produced by applying a filter.
6.  **ReLU:** Replaces negative values with zero.
7.  **Max pooling:** Keeps the maximum value from each local region.
8.  **Flatten:** Converts a multidimensional feature map into a vector.
9.  **Fully connected layer:** Produces a score for every output class.
10. **Softmax:** Converts logits into probabilities that sum to 1.

## 12. Complete forward-propagation flow

\[ `\boxed{
\text{Input}
\rightarrow\text{Convolution}
\rightarrow\text{ReLU}
\rightarrow\text{Max Pooling}
\rightarrow\text{Flatten}
\rightarrow\text{Fully Connected}
\rightarrow\text{Softmax}
}`{=tex} \]

**Scope note:** This worked example demonstrates forward propagation
only. It does not calculate training, backpropagation, or weight
updates.
