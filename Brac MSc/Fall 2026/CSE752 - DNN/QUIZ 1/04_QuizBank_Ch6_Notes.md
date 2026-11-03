# PDF 4 — Deep Learning Chapter 6 Quiz Bank (Lecture 3)

> **Source:** `Deep_Learning_Chapter6_Quiz_Bank.pdf` (9 page). প্রশ্ন ও উত্তর PDF থেকে হুবহু; শুধু syllabus tag (A1…B10) আর note আমার যোগ করা।
> Syllabus tag = `QUIZ1_Syllabus.md`-এর কোন topic-এর সাথে মেলে।

**গোনা (PDF থেকে):** 19 Short Q (A1–A19) · 16 T/F (B1–B16) · 16 Math (C1–C16) · 6 Graph (D1–D6) + formula sheet

## 0. এই PDF-এর মূল কথা (এক নজরে)

- **Entropy / Cross-Entropy / KL:** H(P,Q)=H(P)+D_KL(P‖Q); KL≥0, symmetric না; P=Q হলে KL=0 কিন্তু CE=H(P)।
- **Logistic regression + BCE:** p=σ(wᵀx+b); L=−[y ln p+(1−y)ln(1−p)]; gradient ∂L/∂z=p−y।
- **SGD:** θ_new=θ_old−ηĝ।
- **XOR:** single perceptron পারে না; hidden layer পারে (h₁=OR, h₂=AND, y=h₁ AND NOT h₂)।
- **ReLU, Sigmoid, Softmax:** hidden-এ ReLU; binary-তে sigmoid; multiclass-এ softmax (∂L/∂zₖ=pₖ−yₖ)।
- **Architecture:** 2–2–3 MLP → **15** parameter; UAT ≠ training guarantee।
- **Chain rule / Jacobian / Backprop (concept):** backprop gradient বের করে; optimizer update করে।

## 1. Syllabus-এর সাথে মিল

| Syllabus topic | এই PDF-এর প্রশ্ন |
|---|---|
| A5 Activation (ReLU, sigmoid, softmax) | Short A15 · T/F B6, B8 · Math C10 · Graph D1, D2 |
| A7 Forward/Backprop (concept) | Short A10 · T/F B16 |
| B1 Neuron ও Feedforward | Short A11, A12 · Math C9 |
| B2 XOR | Short A13, A14 · T/F B9 · Graph D4, D5, D6 |
| B3 Entropy, CE, KL | Short A1–A4 · T/F B1–B4 · Math C1–C4 |
| B4 Logistic regression ও BCE | Short A5–A7 · T/F B5, B7 · Math C5, C6, C12 · Graph D3 |
| B5 SGD ও gradient | Short A8, A9 · Math C7, C8 |
| B6 Output units (sigmoid/softmax) | Short A18 · T/F B10, B11 · Math C13, C14 |
| B7 Hidden units ও ReLU | Short A16, A17 · T/F B16 · Math C11 |
| B8 Architecture | T/F B12 · Math C15 |
| B9 Universal Approximation | T/F B13, B14 |
| B10 Chain rule, Jacobian, Backprop | Short A19 · T/F B15 · Math C16 |

## 2. Section A — Short Conceptual Q&A (19)

**A1. What does entropy measure in a target distribution?**  `[Syllabus: B3]`

**উত্তর:** Entropy H(P) measures uncertainty in the target distribution itself. For P = (0.7, 0.3), H(P) = -[0.7 ln(0.7) + 0.3 ln(0.3)] = 0.6109 nats.

**A2. How are cross-entropy and KL divergence different?**  `[Syllabus: B3]`

**উত্তর:** Cross-entropy H(P,Q) is the average information cost when the model distribution Q represents outcomes from target P. KL divergence D_KL(P||Q) is the extra information cost caused by the mismatch between P and Q.

**A3. State the key relationship between entropy, cross-entropy, and KL divergence.**  `[Syllabus: B3]`

**উত্তর:** H(P,Q) = H(P) + D_KL(P||Q). The target entropy is fixed when P is fixed, so minimizing cross-entropy also minimizes the KL divergence.

**A4. What happens to KL divergence when the predicted distribution equals the target distribution?**  `[Syllabus: B3]`

**উত্তর:** If Q = P, then D_KL(P||Q) = 0. Cross-entropy then equals the target entropy H(P); the entropy does not disappear.

**A5. Why is logistic regression used for classification despite its name?**  `[Syllabus: B4]`

**উত্তর:** It calculates a linear score z = wᵀx + b and applies sigmoid to estimate P(y=1|x). That probability can be thresholded to predict one of two classes.

**A6. What does the sigmoid function do in logistic regression?**  `[Syllabus: B4]`

**উত্তর:** σ(z) = 1/(1+e^(-z)) transforms a real-valued score into a probability strictly between zero and one for finite z.

**A7. What does binary cross-entropy represent?**  `[Syllabus: B4]`

**উত্তর:** L(y,p) = -[y ln(p) + (1-y) ln(1-p)] is the negative log-likelihood of a Bernoulli output distribution. The training objective is to minimize it.

**A8. What information does a gradient provide?**  `[Syllabus: B5]`

**উত্তর:** A gradient describes how the loss changes with each trainable parameter. Its sign and magnitude indicate the local direction and sensitivity of the loss to parameter changes.

**A9. How does SGD use a gradient?**  `[Syllabus: B5]`

**উত্তর:** SGD updates parameters using θ_new = θ_old - ηĝ, where ĝ is an estimated gradient and η is the learning rate. It moves in the direction opposite to the estimated gradient.

**A10. What is the difference between forward propagation and backpropagation?**  `[Syllabus: A7]`

**উত্তর:** Forward propagation computes hidden activations, logits, output probabilities, and loss from input to output. Backpropagation starts from the loss derivative and propagates gradients backward through the network.

**A11. What does a basic neuron compute?**  `[Syllabus: B1]`

**উত্তর:** It forms a weighted sum plus a bias, z = wᵀx + b, then applies an activation a = f(z). Weights control feature contributions; the bias shifts the pre-activation.

**A12. What is a feedforward network?**  `[Syllabus: B1]`

**উত্তর:** It processes information from input to output without recurrent loops. A simple network transforms x into hidden representation h and then into output y.

**A13. Why can a single perceptron not learn XOR?**  `[Syllabus: B2]`

**উত্তর:** A single perceptron has a straight-line decision boundary for two inputs. XOR’s positive and negative labels alternate across the four corners, so no one straight line separates them.

**A14. How can a hidden layer represent XOR?**  `[Syllabus: B2]`

**উত্তর:** It defines h1 = x1 OR x2 and h2 = x1 AND x2, then y = h1 AND NOT(h2). The hidden units create an intermediate representation that makes the final decision possible.

**A15. Why are nonlinear activation functions necessary?**  `[Syllabus: A5]`

**উত্তর:** A nonlinear activation such as ReLU allows the network to represent nonlinear relationships.

**A16. Why is ReLU commonly used for hidden units?**  `[Syllabus: B7]`

**উত্তর:** ReLU(x) = max(0,x) is simple and computationally inexpensive. For positive inputs its derivative is one, so it avoids the positive-side saturation associated with sigmoid and tanh.

**A17. What is a limitation of ReLU?**  `[Syllabus: B7]`

**উত্তর:** For a negative pre-activation, ReLU outputs zero and its derivative is zero. If a unit stays in that region for all its inputs, it may stop updating through that path; this is called the dying ReLU problem.

**A18. When is sigmoid appropriate, and when is softmax appropriate?**  `[Syllabus: B6]`

**উত্তর:** Sigmoid represents a Bernoulli output for a binary target. Softmax represents a probability distribution over mutually exclusive classes, with all class probabilities summing to one.

**A19. How are gradient, Jacobian, backpropagation, and an optimizer related?**  `[Syllabus: B10]`

**উত্তর:** A gradient is for a scalar loss; a Jacobian records how vector outputs change with vector inputs. Backpropagation applies the chain rule and local Jacobians efficiently to calculate gradients; SGD or another optimizer then updates parameters. 

## 3. Section B — True/False with reasons (16)

**B1. KL divergence is always symmetric: D_KL(P||Q) = D_KL(Q||P).**  `[Syllabus: B3]`

→ **FALSE** — exchanging P and Q generally changes the value.

**B2. KL divergence is non-negative and equals zero when P = Q.**  `[Syllabus: B3]`

→ **TRUE** — Matching target and model distributions removes the mismatch.

**B3. For fixed target P, minimizing cross-entropy is equivalent to minimizing KL divergence.**  `[Syllabus: B3]`

→ **TRUE** — H(P,Q) = H(P) + D_KL(P||Q), and H(P) is constant with respect to the model parameters.

**B4. The entropy of a one-hot target distribution is zero.**  `[Syllabus: B3]`

→ **TRUE** — A one-hot target assigns probability one to the true class and zero to the others.

**B5. Logistic regression uses a linear score followed by sigmoid to estimate a binary -class probability.**  `[Syllabus: B4]`

→ **TRUE** — as p = σ(wᵀx+b).

**B6. For every finite logit z, sigmoid outputs exactly 0 or exactly 1.**  `[Syllabus: A5]`

→ **FALSE** — For finite z, sigmoid lies strictly between zero and one.

**B7. When the true label is y=1, binary cross-entropy simplifies to -ln(p).**  `[Syllabus: B4]`

→ **TRUE** — Substituting y=1 into the binary cross-entropy formula leaves -ln(p).

**B8. ReLU returns zero for a negative input and passes a positive input through unchanged.**  `[Syllabus: A5, B7]`

→ **TRUE** — ReLU(x)=max(0,x).

**B9. XOR is linearly separable, so a single perceptron can learn it.**  `[Syllabus: B2]`

→ **FALSE** — XOR is not linearly separable; a single straight boundary cannot separate its classes.

**B10. Softmax is the natural complete output distribution when multiple mutually exclusive classes are possible.**  `[Syllabus: B6]`

→ **TRUE** — It returns one probability per class and the probabilities sum to one.

**B11. A single sigmoid output and a three-class Softmax output have identical output structures.**  `[Syllabus: B6]`

→ **FALSE** — Sigmoid gives one positive-class probability; Softmax gives one probability for each mutually exclusive class.

**B12. The fully connected 2–2–3 MLP has 15 trainable parameters.**  `[Syllabus: B8]`

→ **TRUE** — There are 4 input-to-hidden weights + 2 hidden biases + 6 hidden-to-output weights + 3 output biases = 15.

**B13. The universal approximation theorem guarantees that gradient descent will find the exact desired parameters.**  `[Syllabus: B9]`

→ **FALSE** — The theorem concerns representational capability; it does not guarantee that a training algorithm finds the right parameters.

**B14. It claims that deeper networks are always better and easier to optimize.**  `[Syllabus: B9]`

→ **FALSE** — Depth and width must be selected and evaluated; deeper networks are not always better or easier to optimize.

**B15. Backpropagation itself is the parameter-update optimizer.**  `[Syllabus: B10]`

→ **FALSE** — Backpropagation calculates gradients; SGD or another optimizer uses them to update parameters.

**B16. If a hidden ReLU pre-activation is negative, its local ReLU derivative is zero and that gradient path is blocked for the current input.**  `[Syllabus: B7, A7]`

→ **TRUE** — it gives ReLU′(z)=0 for z<0. 

## 4. Section C — Mathematical problems with worked solutions (16)

### C1.  `[Syllabus: B3]`

**Q:** Calculate the entropy of the target distribution P=(0.7, 0.3).

**Solution:**

- Formula: H(P) = -Σᵢ P(i) ln P(i).
- Substitute: H(P) = -[0.7 ln(0.7) + 0.3 ln(0.3)].
- Using ln(0.7) ≈ -0.3567 and ln(0.3) ≈ -1.2040: H(P) ≈ 0.2497 + 0.3612 = 0.6109 nats.
- Answer: 0.6109 nats.

### C2.  `[Syllabus: B3]`

**Q:** For target P=(0.7,0.3) and model Q=(0.6,0.4), calculate cross-entropy.

**Solution:**

- Formula: H(P,Q) = -Σᵢ P(i) ln Q(i).
- H(P,Q) = -[0.7 ln(0.6) + 0.3 ln(0.4)].
- Using ln(0.6) ≈ -0.5108 and ln(0.4) ≈ -0.9163: H(P,Q) ≈ 0.3576 + 0.2749 = 0.6325 nats.
- Answer: 0.6325 nats.

### C3.  `[Syllabus: B3]`

**Q:** Using P=(0.7,0.3) and Q=(0.6,0.4), calculate KL divergence and verify the identity.

**Solution:**

- D_KL(P||Q) = Σᵢ P(i) ln[P(i)/Q(i)].
- D_KL = 0.7 ln(0.7/0.6) + 0.3 ln(0.3/0.4) ≈ 0.1079 - 0.0863 = 0.0216 nats.

### C4.  `[Syllabus: B3]`

**Q:** A one-hot target has true class A. Compare the cross-entropy when the model assigns p=0.70 and p=0.95 to class A.

**Solution:**

- For a one-hot target, L = -ln(p) for the true class.
- At p=0.70: L = -ln(0.70) ≈ 0.3567 nats.
- At p=0.95: L = -ln(0.95) ≈ 0.0513 nats.
- The second loss is smaller because the model assigns a higher probability to the correct class.

### C5.  `[Syllabus: B4]`

**Q:** Logistic regression receives x=2 with w=0 and b=0. Calculate z and p.

**Solution:**

- Linear score: z=wx+b=(0)(2)+0=0.
- Sigmoid: p=1/(1+e^(-z))=1/(1+e⁰)=1/2=0.5.
- Answer: z=0 and p=0.50, an uncertain binary prediction.

### C6.  `[Syllabus: B4]`

**Q:** For a true malicious label y=1, compare binary cross-entropy for p=0.80 and p=0.10.

**Solution:**

- When y=1, L=-ln(p).
- p=0.80: L=-ln(0.80)≈0.2231 nats.
- p=0.10: L=-ln(0.10)≈2.3026 nats.
- The confidently wrong prediction p=0.10 receives the much larger loss.

### C7.  `[Syllabus: B5]`

**Q:** For x=2, y=1, w=0, b=0, p=0.5, calculate the gradients and one SGD update with η=0.1.

**Solution:**

- For sigmoid + binary cross-entropy: ∂L/∂z=p-y, ∂L/∂w=(p-y)x, ∂L/∂b=p-y.
- Weight gradient: (0.5-1)(2)=-1. Bias gradient: 0.5-1=-0.5.
- w_new = 0 - 0.1(-1)=0.10. b_new = 0 - 0.1(-0.5)=0.05.
- Answer: gradients are -1 and -0.5; updated parameters are w=0.10 and b=0.05.

### C8.  `[Syllabus: B5]`

**Q:** Continue C7. Calculate the updated prediction and loss.

**Solution:**

- z_new = w_new x + b_new = (0.1)(2)+0.05=0.25.
- p_new=σ(0.25)=1/(1+e^(-0.25))≈0.5622.
- Because y=1, L_new=-ln(0.5622)≈0.5759 nats.
- Comparison: loss falls from 0.6931 to 0.5759 nats; attack probability rises from 50.00% to about 56.22%.

### C9.  `[Syllabus: B1]`

**Q:** A neuron has x₁=2, x₂=3, w₁=0.5, w₂=0.2, b=1. Find its pre-activation z.

**Solution:**

- z=w₁x₁+w₂x₂+b.
- z=(0.5)(2)+(0.2)(3)+1=1+0.6+1=2.6.
- Answer: z=2.6.

### C10.  `[Syllabus: A5]`

**Q:** Calculate ReLU(-3), ReLU(0), and ReLU(2.7).

**Solution:**

- ReLU(x)=max(0,x).
- ReLU(-3)=0; ReLU(0)=0; ReLU(2.7)=2.7.
- Rule: negative inputs become zero; positive inputs pass through unchanged.

### C11.  `[Syllabus: B7]`

**Q:** For x₁=2 and x₂=1, calculate the two hidden scores z₁=x₁+x₂-1 and z₂=x₁-x₂, then apply ReLU.

**Solution:**

- z₁=2+1-1=2. z₂=2-1=1.
- h₁=ReLU(2)=2; h₂=ReLU(1)=1.
- Answer: hidden representation h=[2,1]ᵀ.

### C12.  `[Syllabus: B4]`

**Q:** A binary classifier has logit z=1 and true label y=1. Calculate p and loss.

**Solution:**

- p=σ(1)=1/(1+e^(-1))≈0.7311.
- L=-ln(0.7311)≈0.3133 nats.
- Answer: p≈0.7311 and L≈0.3133 nats.

### C13.  `[Syllabus: B6]`

**Q:** Calculate the Softmax probabilities for logits [0,2,1] for Benign, DDoS, and Port scan.

**Solution:**

- Exponentials: e⁰=1, e²≈7.389, e¹≈2.718; sum≈11.107.
- P(Benign)=1/11.107≈0.090; P(DDoS)=7.389/11.107≈0.665; P(Port scan)=2.718/11.107≈0.245.
- The probabilities sum to approximately 1.000. The largest is DDoS.

### C14.  `[Syllabus: B6]`

**Q:** For C13, if the correct class is DDoS with one-hot target y=[0,1,0], calculate cross-entropy and the logit gradient.

**Solution:**

- Loss: L=-ln(0.665241)≈0.407606 nats (about 0.408).
- Softmax + cross-entropy gives δ=p-y.
- δ≈[0.090031, 0.665241-1, 0.244728]ᵀ = [0.090031, -0.334759, 0.244728]ᵀ.

### C15.  `[Syllabus: B8]`

**Q:** Count trainable parameters in a fully connected 2–2–3 MLP with biases.

**Solution:**

- Input-to-hidden: 2×2=4 weights + 2 hidden biases = 6 parameters.
- Hidden-to-output: 2×3=6 weights + 3 output biases = 9 parameters.
- Total = 6+9=15 trainable parameters.

### C16.  `[Syllabus: B10]`

**Q:** Let u=2x and L=u². Use the chain rule to calculate dL/dx at x=3.

**Solution:**

- At x=3, u=2(3)=6.
- dL/du=2u=12 and du/dx=2.
- dL/dx=(dL/du)(du/dx)=12×2=24.

## Gradient Descent — Math (PNG `f_x_gradient_descent.webp` + bank Problem 3)

> এটা sir-এর notice-এর **Gradient Descent math problem (PNG)**। Exam-এ নিশ্চিত আসার মতো। নিচের সব হিসাব computer দিয়ে মিলানো।

### 1. Problem
`f(x) = x²` minimize করো। শুরু x₀ = 4, learning rate η = 0.1।
Minimum x* = 0, f(0) = 0।

### 2. যা লাগবে (3 লাইন)
- Function: f(x) = x²
- Derivative (slope): f′(x) = 2x
- Update rule: **x_new = x_old − η · f′(x_old) = x_old − 0.1·(2·x_old) = 0.8 · x_old**

### 3. ধাপে ধাপে (PNG-র Step-by-step)

| Iteration | x_old | f′(x_old) = 2x | x_new = x_old − 0.1·f′ |
|---|---|---|---|
| 0 | 4 | 2(4) = 8 | 4 − (0.1)(8) = **3.2** |
| 1 | 3.2 | 2(3.2) = 6.4 | 3.2 − (0.1)(6.4) = **2.56** |
| 2 | 2.56 | 2(2.56) = 5.12 | 2.56 − (0.1)(5.12) = **2.048** |
| 3 | 2.048 | 2(2.048) = 4.096 | 2.048 − (0.1)(4.096) = **1.6384** |

### 4. Iteration table (সঠিক মান)

| t | xₜ | f′(xₜ)=2xₜ | f(xₜ)=xₜ² |
|---|---|---|---|
| 0 | 4.0000 | 8.0000 | 16.0000 |
| 1 | 3.2000 | 6.4000 | 10.2400 |
| 2 | 2.5600 | 5.1200 | 6.5536 |
| 3 | 2.0480 | 4.0960 | 4.1943 |
| 4 | 1.6384 | 3.2768 | 2.6844 |
| 5 | 1.3107 | 2.6214 | **1.7180** |
| 6 | 1.0486 | 2.0972 | **1.0995** |
| 7 | 0.8389 | 1.6777 | 0.7037 |
| 8 | 0.6711 | 1.3422 | **0.4504** |
| 9 | 0.5369 | 1.0737 | **0.2882** |

⚠️ **PNG-র ছাপার ভুল:** f(xₜ) কলামে t=5, 6, 8, 9-এ PNG-তে ছাপা আছে 1.7189, 1.1005, 0.4503, 0.2883। সঠিক মান বোল্ডে (xₜ²-কে exact xₜ দিয়ে হিসাব করলে)। xₜ ও f′(xₜ) কলামে কোনো ভুল নেই।

### 5. Shortcut সূত্র (exam-এ সময় বাঁচায়)
- **xₜ = 4 · (0.8)ᵗ** (প্রতি ধাপে 0.8 গুণ)
- **f(xₜ) = 16 · (0.64)ᵗ** (প্রতি ধাপে 0.64 গুণ)
- **f′(xₜ) = 8 · (0.8)ᵗ**
- যেমন t=5: x₅ = 4·0.8⁵ = 4·0.32768 = 1.3107 ✓; f(x₅) = 1.3107² = 1.7180 ✓

### 6. Variation — প্রশ্নে সংখ্যা বদলে আসতে পারে

**(ক) অন্য starting point** x₀ = −4 (η=0.1): f′(−4) = −8 → x₁ = −4 − 0.1(−8) = **−3.2**। Negative slope → x ডান দিকে (0-এর দিকে) যায়।

**(খ) অন্য learning rate** (x₀=4):
| η | x₁ = 4 − η·8 | কী হয় |
|---|---|---|
| 0.1 | 3.2 | ধীরে 0-এর দিকে |
| 0.5 | 0 | এক ধাপেই minimum |
| 1.0 | −4 | দুই পাশে লাফায় (4, −4, 4…), converge করে না |
| 1.1 | −4.8 | diverge (দূরে চলে যায়) |

সাধারণ নিয়ম: x_new = (1 − 2η)·x_old। |1−2η| < 1 (মানে 0 < η < 1) হলে converge।

**(গ) কত ধাপে x < 0.01?** 4·0.8ᵗ < 0.01 → t > ln(400)/ln(1.25) ≈ 26.9 → **t = 27** (x₂₇ ≈ 0.0097)।

### 7. Graph (PNG-র নিচের অংশ)
- x-axis −4…4, y-axis f(x): 0, 1, 4, 8, 12, 16
- Curve f(x)=x² (U-shape); minimum (0,0) লেখো: "Minimum at x = 0"
- Red dot: (4,16), (3.2,10.24), (2.56,6.5536), (2.048,4.1943), (1.6384,2.6844)
- x-axis-এ লাল তীর **বাম দিকে** ("Gradient Descent moves LEFT toward 0")
- ধাপ ক্রমশ ছোট (slope ছোট হচ্ছে)

### 8. কী বলবে (PNG-র "What is happening?")
- x=4 তে slope = 8 (positive) → function বাড়ছে
- তাই **বাম দিকে** (negative direction) যাই f কমাতে
- 0-এর কাছে গেলে slope ছোট → update ছোট → x→0
- Minimum value f(0)=0

### 9. (Generated) Linear regression-এ GD — একটা ছোট উদাহরণ
> PDF 1 p5-এ rule আছে: wⱼ ← wⱼ − η ∂J/∂wⱼ, b ← b − η ∂J/∂b। নিচের সংখ্যা আমি বানিয়েছি (sir-এর question না)।

ŷ = wx + b; একটা sample x=2, y=5; শুরু w=0, b=0; η=0.1; loss L=½(ŷ−y)²
- ŷ = 0 → L = ½(0−5)² = 12.5
- ∂L/∂w = (ŷ−y)x = (−5)(2) = −10; ∂L/∂b = ŷ−y = −5
- w_new = 0 − 0.1(−10) = **1.0**; b_new = 0 − 0.1(−5) = **0.5**
- নতুন ŷ = 1.0·2 + 0.5 = 2.5 → L = ½(2.5−5)² = **3.125** (12.5 থেকে কমেছে)


## 5. Section D — Graph-plotting exercises (6)

### Graph table

| # | Graph | Task | Key points | Expected result | PDF basis | Syllabus |
|---|---|---|---|---|---|---|
| D1 | ReLU | Plot y = ReLU(x) = max(0,x) for x from -4 to 4. | (-4,0), (-2,0), (0,0), (1,1), (2,2), and (4,4) | The graph is flat at y=0 for x<0 and follows y=x for x≥0. | ReLU(x) = max(0,x). | A5 |
| D2 | Sigmoid | Plot σ(z)=1/(1+e^(-z)). | z=-2→0.1192, z=0→0.5000, z=1→0.7311, and z=2→0.8808 | Draw a smooth S-shaped curve between 0 and 1. The output is 0.5 when z=0. | Sigmoid converts a real-valued logit into a probability strictly between 0 and 1 for finite z. | A5 |
| D3 | BCE (y=1) | Plot L(p)=-ln(p). | (0.1,2.3026), (0.2,1.6094), (0.3,1.2040), (0.4,0.9163), (0.5,0.6931), (0.6,0.5108), (0.7,0.3567), (0.8,0.2231), (0.9,0.1053) | The curve decreases as p increases. A probability near 1 gives a small loss; a probability near 0 gives a large loss. | For a true label y=1, L(p)=-ln(p). | B4 |
| D4 | XOR 4 point | Plot (x₁,x₂) and label the output: (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0. Use different symbols for output 0 and output 1. | task-এ দেওয়া 4 point | The labels alternate at the corners. No single straight line separates the two positive points from the two negative points. | — | B2 |
| D5 | AND 4 point | Plot (0,0)→0, (0,1)→0, (1,0)→0, (1,1)→1. | task-এ দেওয়া 4 point | Only the point (1,1) has output 1; the classes are linearly separable. | AND is linearly separable. | B2 |
| D6 | OR 4 point | Plot (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→1. | task-এ দেওয়া 4 point | Only (0,0) has output 0; the classes are linearly separable. | OR is linearly separable. | B2 |

### প্রতিটা graph কীভাবে আঁকবে

- **D1 ReLU:** x-axis −4…4, y-axis 0…4; (−4,0),(−2,0),(0,0),(1,1),(2,2),(4,4) mark; x<0 flat y=0, x≥0 y=x।
- **D2 Sigmoid:** S-curve 0 আর 1-এর মাঝে; (−2,0.1192),(0,0.5),(1,0.7311),(2,0.8808); z=0-তে 0.5।
- **D3 BCE y=1:** L=−ln p; (0.1,2.3026),(0.2,1.6094),(0.3,1.2040),(0.4,0.9163),(0.5,0.6931),(0.6,0.5108),(0.7,0.3567),(0.8,0.2231),(0.9,0.1054 *(PDF: 0.1053)*); p বাড়লে loss কমে, p→0 হলে loss অনেক বড়, p=1-এ 0।
- **D4 XOR:** square-এর চার কোণ; (0,0)=0, (1,1)=0 একই symbol; (0,1)=1, (1,0)=1 আরেক symbol; কোনো এক সরলরেখা দুই class আলাদা করতে পারে না (PDF figure-এ 0=লাল, 1=নীল)।
- **D5 AND:** শুধু (1,1)=1, বাকি তিনটা 0; একটা রেখা দিয়ে আলাদা করা যায়।
- **D6 OR:** শুধু (0,0)=0, বাকি তিনটা 1; একটা রেখা দিয়ে আলাদা করা যায়।

### Merged PDF 3-এ আঁকা figure (bank-এ exercise না, graph হিসেবে আসতে পারে)

- **BCE দুই curve** (PDF 3 p4): y=1 → −ln p (নামে); y=0 → −ln(1−p) (ওঠে, লাল dashed); দুটো p≈0.5-এ cross; x-axis p (0.1…1), y-axis loss 1,2,3।
- **XOR 4 point** (PDF 3 p13), **ReLU** (PDF 3 p16): D4 ও D1-এর মতো।

### ReLU′(z) — sir-এর নতুন announcement (এই bank-এ নেই)

| Graph | Key points |
|---|---|
| ReLU′(z), z∈[−4,4] | z≤0 → 0 (z=0-তে dot); z>0 → 1; z=0-তে jump |

Sketch ফাইল: `image (1).webp`; ছবি: `ReLU_and_derivative.png`।

## 6. Quick formula sheet (PDF-এর শেষ page)

| Concept | Formula / rule |
|---|---|
| Entropy | H(P) = −Σᵢ P(i) ln P(i) |
| Cross-entropy | H(P,Q) = −Σᵢ P(i) ln Q(i) |
| KL divergence | D_KL(P‖Q) = Σᵢ P(i) ln[P(i)/Q(i)] |
| Relationship | H(P,Q) = H(P) + D_KL(P‖Q) |
| Logistic score | z = wᵀx + b |
| Sigmoid | σ(z) = 1 / (1 + e^(−z)) |
| Binary cross-entropy | L(y,p) = −[y ln(p) + (1−y) ln(1−p)] |
| Gradient for sigmoid + BCE | ∂L/∂z = p−y; ∂L/∂w = (p−y)x; ∂L/∂b = p−y |
| SGD update | θ_new = θ_old − ηĝ |
| ReLU | ReLU(z) = max(0,z) |
| Softmax | pₖ = e^(zₖ) / Σⱼ e^(zⱼ) |
| Softmax + cross-entropy gradient | ∂L/∂zₖ = pₖ − yₖ |
| Chain rule | dL/dx = (dL/du)(du/dx) |
| Vector chain rule | ∇ₓL = J_f(x)ᵀ ∇ᵧL |

## 7. সংখ্যা-যাচাই ও ছাপার ভুল

সব সংখ্যা computer দিয়ে আবার হিসাব করা (ln = natural log):
- H(P)=0.6109 ✓ · H(P,Q)=0.6325 ✓ · KL=0.0216 ✓ · 0.6109+0.0216=0.6325 ✓
- −ln(0.70)=0.3567 ✓ · −ln(0.95)=0.0513 ✓ · −ln(0.80)=0.2231 ✓ · −ln(0.10)=2.3026 ✓
- C7/C8: w=0.10, b=0.05, z=0.25, p=0.5622, L=0.5759 ✓
- C12: σ(1)=0.7311, L=0.3133 ✓ · C13: [0.090, 0.665, 0.245] ✓ · C14: L=0.4076, δ=[0.0900, −0.3348, 0.2447] ✓
- C15: (2·2+2)+(2·3+3)=15 ✓ · C16: 12×2=24 ✓

**ছাপার ভুল/rounding (এই PDF-এ):**
- D3 point (0.9, **0.1053**): exact −ln(0.9)=0.10536 → **0.1054**। 0.1053 বা 0.1054 দুটোই চলবে।
- D2: σ(−2)=0.1192 (ঠিক), σ(2)=0.8808 (ঠিক; অন্য bank-এ 0.881)।
- Section A-র কিছু উত্তরে "B12" notation ইত্যাদি PDF-এর জন্য ঠিক; কোনো সংখ্যাগত ভুল পাইনি।

**লেখার ধরন নিয়ে নোট:** B13/B14 পুরো statement PDF-এ আংশিক ("It claims that deeper networks…")। অর্থ: *deeper নেটওয়ার্ক সবসময় better ও সহজে optimize হয়* — এটা **FALSE**।
