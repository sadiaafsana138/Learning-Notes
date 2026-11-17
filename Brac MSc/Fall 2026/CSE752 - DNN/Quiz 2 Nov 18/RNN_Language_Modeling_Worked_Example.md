# RNN Language Modeling --- A Complete Worked Example

**Topic:** Recurrent Neural Network (RNN)\
**Task:** Read the sentence "The Titanic sank" one token at a time and
predict the next token.\
**Goal:** Understand one-hot encoding, recurrent hidden states, weight
sharing, logits, softmax, cross-entropy loss, and entropy through
complete numerical calculations.

------------------------------------------------------------------------

## 1. What problem are we solving?

A language model predicts the next token based on the tokens it has
already received.

Our sentence is:

> The Titanic sank

We add a special beginning-of-sentence token, written as `<BOS>`.

The model will make three predictions:

1.  Input `<BOS>` → predict `The`
2.  Input `The` → predict `Titanic`
3.  Input `Titanic` → predict `sank`

**Important scope:** We stop after the RNN reads `Titanic` at time step
3 and predicts `sank`. We do **not** feed `sank` into the RNN as a
fourth input.

## 2. Create the vocabulary

The vocabulary contains every token used in this small example,
including the beginning token:

\[
V=\[`\texttt{<BOS>}`{=tex}, `\text{The}`{=tex}, `\text{Titanic}`{=tex}, `\text{sank}`{=tex}\]
\]

Vocabulary size:

\[ `\boxed{|V|=4}`{=tex} \]

We keep this exact order throughout the example:

    Index Token
  ------- ---------
        1 `<BOS>`
        2 The
        3 Titanic
        4 sank

The output layer also has four units because the model predicts a
probability for every token in this four-token vocabulary.

## 3. One-hot encoding

**One-hot encoding** represents each token as a vector containing
exactly one `1`; all other entries are `0`. The position of the `1`
identifies the token.

  Token     One-hot vector
  --------- ------------------
  `<BOS>`   (\[1,0,0,0\]\^T)
  The       (\[0,1,0,0\]\^T)
  Titanic   (\[0,0,1,0\]\^T)
  sank      (\[0,0,0,1\]\^T)

Each input vector has four elements because the vocabulary has four
tokens.

## 4. Form the input--target pairs

A language model uses the current token to predict the next token.

    Time step Input token   Correct target   Meaning
  ----------- ------------- ---------------- ----------------
            1 `<BOS>`       The              Start → The
            2 The           Titanic          The → Titanic
            3 Titanic       sank             Titanic → sank

At time step 3: - Input = `Titanic` - Target = `sank`

The target is the correct answer used to evaluate the prediction. It is
not the input at this time step.

## 5. RNN architecture

At each time step, a basic RNN performs these operations:

1.  Combines the current input with the previous hidden state.
2.  Applies the `tanh` activation function to calculate the new hidden
    state.
3.  Converts the hidden state into output logits.
4.  Applies softmax to obtain next-token probabilities.

The recurrent connection passes the hidden state from one time step to
the next.

### Forward-propagation equations

**Equation 1 --- hidden-state pre-activation:**

\[ a_t=W_xx_t+W_hh\_{t-1}+b_h \]

**Equation 2 --- new hidden state:**

\[ h_t=`\tanh`{=tex}(a_t) \]

**Equation 3 --- output logits:**

\[ z_t=W_yh_t+b_y \]

**Equation 4 --- output probabilities:**

\[ p_t=`\operatorname{softmax}`{=tex}(z_t) \]

Where:

  Symbol       Meaning
  ------------ ------------------------------------------
  (x_t)        Current input vector
  (h\_{t-1})   Previous hidden state
  (a_t)        Hidden-state pre-activation
  (h_t)        New hidden state
  (W_x)        Input-to-hidden weight matrix
  (W_h)        Hidden-to-hidden recurrent weight matrix
  (W_y)        Hidden-to-output weight matrix
  (b_h)        Hidden-layer bias
  (b_y)        Output-layer bias
  (z_t)        Output logits
  (p_t)        Predicted probability distribution

## 6. Initialize weights and explain weight sharing

To keep the arithmetic simple, use these weights:

\[ W_x=I_4 \]

\[ W_h=0.1I_4 \]

\[ b_h=0,`\qquad `{=tex}b_y=0 \]

Here, (I_4) is the 4 × 4 identity matrix:

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

The output weight matrix is:

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

The vocabulary order for rows and columns is:

\[
\[`\texttt{<BOS>}`{=tex}, `\text{The}`{=tex}, `\text{Titanic}`{=tex}, `\text{sank}`{=tex}\]
\]

This output matrix is deliberately chosen so that the example favours
the intended next-token sequence:

\[
`\texttt{<BOS>}`{=tex}`\rightarrow`{=tex}`\text{The}`{=tex}`\rightarrow`{=tex}`\text{Titanic}`{=tex}`\rightarrow`{=tex}`\text{sank}`{=tex}
\]

The initial hidden state is:

\[ h_0=\[0,0,0,0\]\^T \]

### What is weight sharing?

The same matrices (W_x), (W_h), and (W_y) are reused at time steps 1, 2,
and 3.

We do not create a new set of weights for each word. Only the input and
hidden state change from one time step to the next.

This reuse of the same weights across time is called **weight sharing**.

## 7. Time step 1: Input `<BOS>`, target `The`

### 7.1 Input vector

The one-hot vector for `<BOS>` is:

\[ x_1=\[1,0,0,0\]\^T \]

The previous hidden state is:

\[ h_0=\[0,0,0,0\]\^T \]

### 7.2 Calculate the pre-activation

Use:

\[ a_1=W_xx_1+W_hh_0 \]

Substitute the values:

\[ a_1=I_4
```{=tex}
\begin{bmatrix}1\\0\\0\\0\end{bmatrix}
```
+0.1I_4
```{=tex}
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
```
\]

\[ `\boxed{a_1=[1,0,0,0]^T}`{=tex} \]

### 7.3 Apply tanh to calculate the hidden state

The tanh function is applied to every element:

\[ h_1=`\tanh`{=tex}(a_1) \]

\[ h_1=\[`\tanh`{=tex}(1),0,0,0\]\^T \]

Since (`\tanh`{=tex}(1)`\approx0.761594`{=tex}):

\[ `\boxed{h_1=[0.761594,0,0,0]^T}`{=tex} \]

### 7.4 Calculate output logits

\[ z_1=W_yh_1 \]

\[ z_1= 4
```{=tex}
\begin{bmatrix}
0&0&0&0\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{bmatrix}
\begin{bmatrix}
0.761594\\0\\0\\0
\end{bmatrix}
```
\]

\[ `\boxed{z_1=[0,3.046377,0,0]^T}`{=tex} \]

### 7.5 Apply softmax

Softmax converts logits into probabilities:

\[ p_i=`\frac{e^{z_i}}{\sum_{j=1}^{4}e^{z_j}}`{=tex} \]

For this time step, the exponentials are approximately:

\[ \[1, 21.038974, 1, 1\] \]

Their sum is:

\[ 1+21.038974+1+1=24.038974 \]

Therefore, in vocabulary order:

\[ `\boxed{
p_1=[0.041599,\ 0.875203,\ 0.041599,\ 0.041599]
}`{=tex} \]

The correct target is `The`. Its predicted probability is:

\[ `\boxed{P_1(\text{The})=0.875203\approx87.52\%}`{=tex} \]

## 8. Time step 2: Input `The`, target `Titanic`

### 8.1 Input and previous hidden state

\[ x_2=\[0,1,0,0\]\^T \]

The previous hidden state is the output from time step 1:

\[ h_1=\[0.761594,0,0,0\]\^T \]

### 8.2 Calculate the pre-activation

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

### 8.3 Apply tanh

\[ h_2=`\tanh`{=tex}(a_2) \]

\[ `\boxed{h_2=[0.076013,0.761594,0,0]^T}`{=tex} \]

### 8.4 Calculate output logits

\[ z_2=W_yh_2 \]

\[ `\boxed{z_2=[0,0.304050,3.046377,0]^T}`{=tex} \]

### 8.5 Apply softmax

The predicted probability distribution is:

\[ `\boxed{
p_2=[0.040993,\ 0.055560,\ 0.862454,\ 0.040993]
}`{=tex} \]

The correct target is `Titanic`:

\[ `\boxed{P_2(\text{Titanic})=0.862454\approx86.25\%}`{=tex} \]

## 9. Time step 3: Input `Titanic`, target `sank`

This is the final time step required in the question.

### 9.1 Input and previous hidden state

The one-hot input vector for `Titanic` is:

\[ x_3=\[0,0,1,0\]\^T \]

The previous hidden state is:

\[ h_2=\[0.076013,0.761594,0,0\]\^T \]

### 9.2 Calculate the pre-activation

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

### 9.3 Apply tanh

\[ h_3=`\tanh`{=tex}(a_3) \]

\[ `\boxed{h_3=[0.007601,0.076013,0.761594,0]^T}`{=tex} \]

### 9.4 Calculate output logits

\[ z_3=W_yh_3 \]

\[ `\boxed{z_3=[0,0.030404,0.304050,3.046377]^T}`{=tex} \]

### 9.5 Apply softmax

Calculate the exponentials:

\[ e\^{z_3}`\approx
[1,\ 1.030871,\ 1.355337,\ 21.038974]`{=tex}\]

Sum:

\[ 1+1.030871+1.355337+21.038974=24.425182 \]

Divide each exponential by the sum:

\[ p_3= `\frac{[1,\ 1.030871,\ 1.355337,\ 21.038974]}`{=tex} {24.425182}
\]

Therefore:

\[ `\boxed{
p_3=[0.040941,\ 0.042205,\ 0.055489,\ 0.861364]
}`{=tex} \]

### 9.6 Interpret the prediction

The vocabulary order is:

\[
\[`\texttt{<BOS>}`{=tex}, `\text{The}`{=tex}, `\text{Titanic}`{=tex}, `\text{sank}`{=tex}\]
\]

  Token        Predicted probability
  ---------- -----------------------
  `<BOS>`           0.040941 (4.09%)
  The               0.042205 (4.22%)
  Titanic           0.055489 (5.55%)
  **sank**     **0.861364 (86.14%)**

The model assigns the highest probability to `sank`, which is the
correct next token.

## 10. Calculate categorical cross-entropy loss at time step 3

Cross-entropy loss measures how much probability the model assigns to
the correct target.

The correct target is `sank`, so its one-hot target vector is:

\[ y_3=\[0,0,0,1\]\^T \]

Categorical cross-entropy is:

\[ L_3=-`\sum`{=tex}*{i=1}\^{4}y*{3,i}`\ln`{=tex}(p\_{3,i}) \]

Only the correct target position has value 1. Therefore, the expression
simplifies to:

\[ L_3=-`\ln`{=tex}(p_3(`\text{sank}`{=tex})) \]

Substitute the predicted probability:

\[ L_3=-`\ln`{=tex}(0.861364) \]

\[ `\boxed{L_3\approx0.149238\text{ nats}}`{=tex} \]

**Interpretation:** A higher probability for the correct target produces
a smaller loss. If the model assigned a probability very close to 1 to
`sank`, the loss would be close to zero.

### Losses for all three predictions

Using the target probabilities from the three time steps:

\[ L_1=-`\ln`{=tex}(0.875203)`\approx0.133300`{=tex} \]

\[ L_2=-`\ln`{=tex}(0.862454)`\approx0.147973`{=tex} \]

\[ L_3=-`\ln`{=tex}(0.861364)`\approx0.149238`{=tex} \]

Average loss:

\[ L\_{`\text{average}`{=tex}}= `\frac{L_1+L_2+L_3}{3}`{=tex} \]

\[ =`\frac{0.133300+0.147973+0.149238}{3}`{=tex} \]

\[ `\boxed{L_{\text{average}}\approx0.143504\text{ nats}}`{=tex} \]

## 11. Calculate prediction entropy at time step 3

Entropy measures the uncertainty of the **entire predicted probability
distribution**. It does not focus only on the correct target.

For a distribution with probabilities (p_1,p_2,`\ldots`{=tex},p_4):

\[ H(p_3)=-`\sum`{=tex}*{i=1}\^{4}p*{3,i}`\ln`{=tex}(p\_{3,i}) \]

Substitute the four probabilities:

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

### Entropy versus cross-entropy loss

These two quantities are related but answer different questions.

  -----------------------------------------------------------------------
  Entropy                             Cross-entropy loss
  ----------------------------------- -----------------------------------
  Measures uncertainty in the whole   Measures how well the prediction
  predicted distribution.             matches the correct target.

  Uses every predicted probability.   With a one-hot target, depends on
                                      the probability assigned to the
                                      correct class.

  Here: approximately 0.553421 nats.  Here: approximately 0.149238 nats.
  -----------------------------------------------------------------------

For this example:

-   **Entropy:** How spread out or uncertain is the model's predicted
    distribution?
-   **Cross-entropy loss:** How much probability did the model assign to
    the correct word, `sank`?

A distribution can have low entropy but still have high cross-entropy
loss if it is highly confident in the wrong answer.

## 12. Final summary

    Time step Input     Correct next word     Probability of target
  ----------- --------- ------------------- -----------------------
            1 `<BOS>`   The                                  87.52%
            2 The       Titanic                              86.25%
            3 Titanic   sank                                 86.14%

### Final requested results

\[
`\boxed{P(\text{sank}\mid\texttt{<BOS>},\text{The},\text{Titanic})\approx0.861364}`{=tex}
\]

\[ `\boxed{\text{Cross-entropy loss}\approx0.149238\text{ nats}}`{=tex}
\]

\[ `\boxed{\text{Prediction entropy}\approx0.553421\text{ nats}}`{=tex}
\]

## 13. What students should remember

1.  **Vocabulary:** The set of tokens the model can predict.
2.  **One-hot encoding:** Represents each token with a vector containing
    one `1`.
3.  **Hidden state:** Carries information forward from earlier time
    steps.
4.  **Weight sharing:** The same RNN weight matrices are reused at every
    time step.
5.  **Tanh:** Converts the pre-activation values into the new hidden
    state.
6.  **Logits:** Raw output scores before softmax.
7.  **Softmax:** Converts logits into probabilities that sum to 1.
8.  **Cross-entropy:** Evaluates the probability assigned to the correct
    target.
9.  **Entropy:** Measures uncertainty across the full predicted
    distribution.
10. **Time-step scope:** At time step 3, `Titanic` is the input and
    `sank` is the target. `sank` is not fed in as a fourth input.

## 14. Complete RNN forward-propagation flow

At each time step:

\[ `\boxed{
x_t,h_{t-1}
\rightarrow a_t
\rightarrow h_t
\rightarrow z_t
\rightarrow p_t
}`{=tex} \]

Across the three time steps:

\[ `\boxed{
\texttt{<BOS>}
\rightarrow\text{The}
\rightarrow\text{Titanic}
\rightarrow\text{sank}
}`{=tex} \]

**Scope note:** This example covers forward propagation and the stated
loss/entropy calculations. It does not perform backpropagation through
time or update the weights.
