# PDF 3 — KL/Cross-Entropy, Logistic Regression, XOR, Output Units, Architecture ও Backprop

> **Source:** `Merged-KL-XOR-Grad-Arch.pdf` (38 page) · লেখক: Refai Arafat Rossi · October 2026 · Goodfellow, Bengio, Courville *Deep Learning* Chapter 6 অবলম্বনে
> **এই file-এর উদ্দেশ্য:** PDF-এর প্রতিটা page-এর প্রতিটা point এখানে আছে। এই file পড়লে PDF আলাদা করে পড়ার দরকার নেই।
> **Syllabus tag** (B3, B4 …) = `QUIZ1_Syllabus.md`-এর topic। সব log = **natural log (ln)**, unit = **nats**।
> সব সংখ্যা computer দিয়ে আবার হিসাব করে মিলানো।

---

## 0. PDF-এর গঠন

| Page | কী আছে | Syllabus |
|---|---|---|
| p1–4 | **Problem 1:** Entropy, Cross-Entropy, KL Divergence | B3 |
| p4–8 | **Problem 2:** Logistic Regression ও SGD | B4, B5 |
| p9–18 | **Feedforward Networks Lecture Notes:** neuron, XOR, hidden layer, nonlinearity, ReLU | B1, B2, B7 |
| p19–27 | **Gradient-Based Learning, Output Units, ReLU:** cost function, sigmoid, softmax, hidden units | B4–B7 |
| p28–38 | **Architecture, Universal Approximation, Backprop:** 2–2–3 MLP, chain rule, Jacobian | B8–B10 |

> ⚠️ **Backprop-এর numerical math (§33, p32–38) notice অনুযায়ী exam-এ আসবে না।** শুধু concept। বোঝার জন্য সব ধাপ রাখা আছে।

---

# PART 1 — Problem 1: KL Divergence ও Cross-Entropy (p1–4)

## 1. Setup `[B3]`

> **Source:** p1 · Goodfellow Sections 3.13, 5.7.1, 5.9, 6.2.1

PDF-এর শুরু: "Your lesson can begin with two practical problems. The first explains how a neural network **measures the mismatch** between predicted and target probability distributions. The second explains how a model **learns to improve its predictions** by updating its parameters."

**Problem 1 প্রশ্ন:** "How can a deep learning model learn the correct probability distribution?"

Medical image classification: দুটো class — **Class A** ও **Class B**। Target distribution label-এর uncertainty বোঝায়:

| Class | Target probability $P$ | Model prediction $Q$ |
|---|---|---|
| Class A | 0.70 | 0.60 |
| Class B | 0.30 | 0.40 |
| Total | 1.00 | 1.00 |

Model 60%/40% predict করছে, target 70%/30%। **লক্ষ্য:** model-এর prediction target থেকে কতটা আলাদা তা মাপা, আর learning algorithm-কে minimize করার জন্য একটা **loss** দেওয়া।

PDF-এর প্রশ্ন: "How can we measure this mismatch mathematically?" (Goodfellow §3.13 দুটো কাছাকাছি measure দেয়)
- **Cross-entropy:** $Q$ দিয়ে $P$-এর outcome লিখলে গড় information cost
- **KL divergence:** $P$ ও $Q$-এর অমিলের কারণে **extra** information cost

দুটোই probability-র log ব্যবহার করে। PDF: "we use the natural logarithm, ln, so the results are expressed in **nats**."

## 2. তিনটা রাশি: Entropy, Cross-Entropy, KL `[B3]`

> **Source:** p2

### A. Entropy — target distribution-এর অনিশ্চয়তা
$$H(P) = -\sum_i P(i)\log P(i)$$
"It measures uncertainty in the target distribution itself." $P = (0.7, 0.3)$:

$$H(P) = -[0.7\ln(0.7) + 0.3\ln(0.3)] = \boxed{0.6109\text{ nats}}$$

### B. Cross-Entropy — model-এর probability দিয়ে অমিল
$$H(P,Q) = -\sum_i P(i)\log Q(i)$$
Target probability $P(i)$ model-এর probability $Q(i)$-এর log-কে weight করে।

### C. KL Divergence — অমিলের extra cost
$$D_{KL}(P\|Q) = \sum_i P(i)\log\frac{P(i)}{Q(i)}$$
- **Non-negative** ($\ge 0$), দুই distribution মিললে **শূন্য**
- ⚠️ **Symmetric distance না:** $P$ ও $Q$ বদলালে সাধারণত মান বদলায়

## 3. মূল সম্পর্ক `[B3]`

> **Source:** p2 ("3. The essential relationship")

$$\boxed{H(P,Q) = H(P) + D_{KL}(P\|Q)}$$

**কথায় (PDF):** Cross-entropy = target entropy + KL divergence।

$H(P)$ model parameter-এর উপর নির্ভর করে না। তাই **fixed target distribution-এর জন্য cross-entropy minimize = KL divergence minimize**। (Goodfellow §3.13-এর কেন্দ্রীয় সম্পর্ক)

## 4. ধাপে ধাপে সমাধান `[B3]`

> **Source:** p2–3 ("4. Solve the problem step by step") · $P = (0.7, 0.3),\ Q = (0.6, 0.4)$

| Step | হিসাব | মান |
|---|---|---|
| 1. Cross-entropy | $-[0.7\ln(0.6) + 0.3\ln(0.4)] = 0.3576 + 0.2749$ | $\boxed{0.6325}$ nats |
| 2. KL | $0.7\ln\frac{0.7}{0.6} + 0.3\ln\frac{0.3}{0.4} = 0.1079 - 0.0863$ | $\boxed{0.0216}$ nats |
| 3. Verify | $H(P) + D_{KL} = 0.6109 + 0.0216$ | $0.6325$ ✓ (cross-entropy-র সাথে মিলেছে) |

**Step 4 — model ভালো হলে:** $Q$ যদি $P$ হয়ে যায় $(0.7, 0.3)$, তাহলে $D_{KL} = 0$ আর $H(P,Q) = H(P) = 0.6109$ nats।

| Model distribution $Q$ | Cross-entropy | KL divergence |
|---|---|---|
| (0.6, 0.4) | 0.6325 | 0.0216 |
| (0.7, 0.3) | 0.6109 | 0.0000 |

PDF: "The target distribution is fixed at $P = (0.7, 0.3)$. When $Q = P$, the mismatch disappears, but **the target entropy remains**."

## 5. সাধারণ classification: One-hot target `[B3]`

> **Source:** p3 ("5. How does this apply to ordinary deep learning classification?")

সাধারণ supervised classification-এ একটা example-এর একটাই জানা class থাকে। True class = Class A হলে target **one-hot:** $P = (1, 0)$।

- Model Class A-কে $0.70$ দিলে: $H(P,Q) = -\ln(0.70) = \boxed{0.3567}$
- Model improve করে $0.95$ দিলে: $H(P,Q) = -\ln(0.95) = \boxed{0.0513}$
- Loss কমেছে, কারণ correct class-এ probability বেড়েছে।

**One-hot target-এর entropy শূন্য** ($H(P) = 0$) ⟹ $H(P,Q) = D_{KL}(P\|Q)$। (এজন্য cross-entropy আর KL সম্পর্কিত কিন্তু সবসময় সংখ্যায় এক নয়।)

## 6. কেন cross-entropy ভুল prediction-কে শাস্তি দেয় (graph) `[B4]`

> **Source:** p3–4 ("6. Visualize why cross-entropy penalizes wrong predictions", Figure 1)

Binary classification, $p$ = Class 1-এর probability। Loss আসল label $y$-এর উপর নির্ভর করে:
- $y = 1$ হলে: $L(p) = -\ln p$
- $y = 0$ হলে: $L(p) = -\ln(1-p)$

**Figure 1:** x-axis = predicted probability $p$ (0.1 … 1); y-axis = cross-entropy loss (nats) 1, 2, 3।
- নীল রেখা ($y=1$, $-\ln p$): $p \to 1$-এ ছোট loss, $p \to 0$-এ অনেক বড়
- লাল dashed ($y=0$, $-\ln(1-p)$): উল্টো (reverse)
- ~$p = 0.5$-এ দুই রেখা cross করে

PDF: "This makes cross-entropy useful for training probabilistic classifiers: it **rewards confident correct predictions** and **penalizes confident incorrect predictions**."

### Exam-ready Q&A
**Q. H(P,Q), H(P), KL-এর সম্পর্ক কী?** A. $H(P,Q) = H(P) + D_{KL}(P\|Q)$।
**Q. KL symmetric কি?** A. না।
**Q. Q = P হলে KL আর CE কত?** A. KL = 0; CE = H(P) (entropy থেকে যায়)।
**Q. One-hot target-এর entropy?** A. 0; তাই CE = KL।
**Q. P fixed হলে CE minimize করলে কী minimize হয়?** A. KL divergence-ও।

---

# PART 2 — Problem 2: Logistic Regression ও SGD (p4–8)

## 7. Setup `[B4, B5]`

> **Source:** p4–5 · Goodfellow §5.7.1 (Logistic Regression), §5.9 (SGD), §6.2.1 (Cost Functions)

**প্রশ্ন:** "How can logistic regression learn using SGD?" — এখন আমরা error মাপা থেকে **parameter বদলে error কমানো**-তে যাচ্ছি।

Network traffic classification: $y = 0$ **benign**, $y = 1$ **malicious**। একটা numerical feature $x$ (simplified suspicious-traffic score)। **$x = 2$, label $y = 1$** (malicious)।
Initial parameters: $w = 0,\ b = 0$। লক্ষ্য: logistic regression ও **এক SGD update** দিয়ে prediction improve করা।

## 8. Logistic Regression কী? `[B4]`

> **Source:** p4–5 ("2. What is logistic regression?")

PDF: "Although its name contains regression, logistic regression is commonly used for **binary classification**. It estimates the probability that an input belongs to Class 1."

**ধাপ 1 — Linear score:** $z = wx + b$ ($x$ = input feature, $w$ = weight, $b$ = bias, $z$ = output activation-এর আগের linear score)

**ধাপ 2 — Sigmoid:**
$$p = P(y=1|x) = \sigma(wx+b), \qquad \sigma(z) = \frac{1}{1+e^{-z}}$$
Sigmoid যেকোনো real score-কে **strictly 0 আর 1-এর মাঝে** probability-তে নেয়।

**ধাপ 3 — Classification rule:**
$$\hat y = \begin{cases}1, & p \ge 0.5\\0, & p < 0.5\end{cases}$$
PDF: "The threshold determines the predicted class, but training normally uses the probability $p$, not just the final binary prediction."

## 9. ধাপে ধাপে এক SGD update `[B4, B5]`

> **Source:** p5–7 ("3. Initial prediction" … "7. Calculate the new prediction and loss")

**3. Initial prediction:** $x=2, y=1, w=0, b=0$ → $z = (0)(2)+0 = 0$ → $p = \frac{1}{1+e^0} = \frac12 = \mathbf{0.5}$। Model 50% malicious বলছে = অনিশ্চিত prediction।

**4. Cost: binary cross-entropy** (Goodfellow-এর maximum-likelihood framework):
$$L(y,p) = -[y\ln p + (1-y)\ln(1-p)]$$
এটা Bernoulli output distribution-এর **negative log-likelihood**; training objective হলো এটা minimize করা। $y=1$: $L = -[1\cdot\ln(0.5) + 0] = -\ln(0.5) = \mathbf{0.6931}$ nats।

**5. Gradient:** Gradient বলে parameter বদলালে loss কীভাবে বদলায়; locally কোন দিকে গেলে loss কমে।

Sigmoid + BCE-এর জন্য সরল হয়ে যায়:
$$\boxed{\frac{\partial L}{\partial z} = p - y,\quad \frac{\partial L}{\partial w} = (p-y)x,\quad \frac{\partial L}{\partial b} = p - y}$$

$p = 0.5, y = 1, x = 2$:
- $\frac{\partial L}{\partial w} = (0.5 - 1)(2) = \boxed{-1}$
- $\frac{\partial L}{\partial b} = 0.5 - 1 = \boxed{-0.5}$

দুটোই negative → loss কমাতে parameter **বাড়াতে** হবে।

**6. SGD (Goodfellow §5.9):** estimated gradient-এর **উল্টো দিকে** parameter update:
$$\theta \leftarrow \theta - \eta\hat g$$
($\theta$ = সব trainable parameter, $\hat g$ = gradient estimate, $\eta$ = learning rate)

$\eta = 0.1$:
- $w_{new} = 0 - (0.1)(-1) = \boxed{0.1}$
- $b_{new} = 0 - (0.1)(-0.5) = \boxed{0.05}$

Gradient negative বলে বিয়োগ করায় parameter বেড়েছে।

**7. নতুন prediction ও loss:**
$$z_{new} = (0.1)(2) + 0.05 = 0.25,\quad p_{new} = \frac{1}{1+e^{-0.25}} \approx \boxed{0.5622},\quad L_{new} = -\ln(0.5622) \approx \boxed{0.5759}$$

| | Loss (nats) | Predicted attack probability |
|---|---|---|
| Before the update | 0.6931 | 50.00% |
| After the update | 0.5759 | 56.22% |

Loss প্রায় **0.1172 nats** কমেছে।

## 10. Logistic regression, cross-entropy, SGD-এর সম্পর্ক `[B4, B5]`

> **Source:** p7–8 ("8. What is the relationship…", Figure 2)

**Pipeline (Figure 2):** Input feature $x=2$ → Linear model $z = wx+b$ → Sigmoid $p = \sigma(z)$ → Cross-entropy loss $L(y,p)$ → Gradient calculation $\nabla_\theta L$ → SGD parameter update $\theta \leftarrow \theta - \eta\hat g$

| উপাদান | ভূমিকা |
|---|---|
| **Logistic regression** | prediction model: linear score + sigmoid |
| **Cross-entropy** | predicted probability আর true label কতটা মেলে তা মাপে |
| **Gradient calculation** | trainable parameter কীভাবে loss-কে প্রভাবিত করে |
| **SGD** | gradient estimate দিয়ে parameter update করে |

**Key message (PDF):** "Cross-entropy tells the learning algorithm how wrong its probability predictions are. The gradient tells it how its parameters influence that error. SGD then changes those parameters in an attempt to reduce the error."

Primary reference: Goodfellow et al., *Deep Learning* (MIT Press 2016); follow-up reading **§6.2.1 Cost Functions** (cross-entropy ↔ maximum likelihood)।

### Exam-ready Q&A
**Q. Logistic regression-কে regression বলা হয় কেন, অথচ classification করে?** A. এটা linear score $z=w^Tx+b$ বের করে sigmoid দিয়ে $P(y=1|x)$ estimate করে; threshold দিয়ে class ঠিক হয়।
**Q. Sigmoid+BCE-এর gradient?** A. $\partial L/\partial z = p-y$; $\partial L/\partial w=(p-y)x$; $\partial L/\partial b=p-y$।
**Q. SGD কীভাবে gradient ব্যবহার করে?** A. $\theta \leftarrow \theta - \eta\hat g$ (estimated gradient-এর উল্টো দিকে)।

---

# PART 3 — Feedforward Network, XOR, ReLU (p9–18)

> **Title:** "Deep Feedforward Networks — Lecture Notes Based on Chapter 6 of *Deep Learning*" (Goodfellow, Bengio, Courville)

## 11. Lecture Overview ও Learning Objectives `[B1]`

> **Source:** p9–10 (Contents, "1 Lecture Overview")

**Contents (p9):** 1 Lecture Overview · 2 Why Do We Need Deep Learning? · 3 What Is a Feedforward Network? · 4 The Basic Computational Unit: A Neuron · 5 The Critical Problem: XOR · 6 Can One Perceptron Learn XOR? · 7 Solution: Add a Hidden Layer · 8 Why Nonlinear Activation Functions Are Necessary · 9 Common Activation Functions · 10 ReLU Activation Function · 11 Quick Review and Classroom Questions · 12 Key Takeaways

**Lecture flow (PDF):** Problem → Perceptron → XOR limitation → Hidden layer → Nonlinearity → ReLU → Deep feedforward network → Forward propagation → Loss → Gradient descent and backpropagation

Target audience: Master's students; assumed background: basic algebra ও elementary ML (advanced math লাগে না)।

**Learning objectives (PDF):** Students should be able to:
- Explain what a feedforward neural network is
- Understand why a single perceptron cannot learn XOR
- Explain how a hidden layer can solve XOR
- Explain why nonlinear activation functions are necessary
- Calculate a neuron's output step by step
- Define and calculate the ReLU activation
- Describe the architecture of a deep feedforward network
- Explain forward propagation using equations
- Describe the roles of weights, biases, and activation functions
- Solve simple numerical problems involving a neural network

## 12. কেন Deep Learning দরকার? `[B1]`

> **Source:** p10 ("2 Why Do We Need Deep Learning?")

প্রশ্ন (PDF): "Can a machine learn every pattern using a simple linear model?"

Student-pass prediction: $x_1$ = study hours, $x_2$ = attendance। Target $y = 1$ (pass), $0$ (fail)। Linear model $z = w_1x_1 + w_2x_2 + b$, তারপর $y = \text{activation}(z)$; উদাহরণ $z = 2x_1 + 3x_2 - 5$। Model এমন parameter শেখে যা **decision boundary** ঠিক করে। PDF: "A linear model can solve many tasks, but it **cannot represent every possible** input-output relationship."

## 13. Feedforward Network কী? `[B1]`

> **Source:** p11 (§3, Figure 1)

"A feedforward network processes information from **input to output**. In a standard feedforward network, information does **not travel around recurrent loops**."

Input → Computation → Output। Figure 1: input layer ($x_1, x_2, x_3$) → hidden layer ($h_1, h_2$) → output layer ($y$)।

$$\boxed{x \longrightarrow h \longrightarrow y}$$
($x$ = input, $h$ = hidden representation, $y$ = output)

## 14. Neuron `[B1]`

> **Source:** p11–12 (§4, §4.1)

Inputs $x_1 = 2,\ x_2 = 3$; weights $w_1 = 0.5,\ w_2 = 0.2$; bias $b = 1$।

**Weighted sum:** $z = w_1x_1 + w_2x_2 + b = (0.5)(2) + (0.2)(3) + 1 = 1 + 0.6 + 1 = \boxed{2.6}$

**Activation:** $a = f(z)$; পূর্ণ computation: $\boxed{a = f(\mathbf{w}^\top\mathbf{x} + b)}$ ("one of the central equations in the chapter")

### 4.1 প্রতিটা term বোঝা (PDF)
| Term | মানে | উদাহরণ |
|---|---|---|
| $\mathbf{x}$ | input/features | $[2, 3]^\top$ |
| $\mathbf{w}$ | weights | $[0.5, 0.2]^\top$ |
| $\mathbf{w}^\top\mathbf{x}$ | weighted sum | $(0.5)(2)+(0.2)(3) = 1.6$ |
| $b$ | bias: trainable offset, pre-activation shift করে | 1 |
| $f$ | activation function: weighted sum-এ প্রয়োগ। **Nonlinear** activation network-কে nonlinear সম্পর্ক শেখায় | — |

## 15. XOR সমস্যা `[B2]`

> **Source:** p12 (§5)

XOR = **exclusive OR**: দুই binary input **আলাদা** হলে output 1, **এক** হলে 0।

| $x_1$ | $x_2$ | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

সমতুল্য: $0\oplus0 = 0,\ 0\oplus1 = 1,\ 1\oplus0 = 1,\ 1\oplus1 = 0$।

## 16. এক Perceptron কি XOR শিখতে পারে? `[B2]`

> **Source:** p12–14 (§6, §6.1–6.3)

Single perceptron: $z = w_1x_1 + w_2x_2 + b$; threshold activation $y = \begin{cases}1 & z>0\\0 & z\le0\end{cases}$। Decision boundary: $w_1x_1 + w_2x_2 + b = 0$ = **দুই feature-এ একটা সরলরেখা**।

### Visual understanding (Figure 2)
চার XOR বিন্দু: $(0,0)\mapsto0,\ (0,1)\mapsto1,\ (1,0)\mapsto1,\ (1,1)\mapsto0$। দুই positive বিন্দু বিপরীত কোণে, দুই negative-ও বিপরীত কোণে। **কোনো একটা সরলরেখা দুই class আলাদা করতে পারে না।**
(Figure: $(0,0)$ ও $(1,1)$ লাল $y=0$; $(0,1)$ ও $(1,0)$ নীল $y=1$।) PDF-এর প্রশ্ন: "Can you draw one straight line that separates both 1s from both 0s?" → **No**।

### "Not linearly separable" মানে কী?
Dataset **linearly separable** যদি একটা line/plane/hyperplane class আলাদা করতে পারে।

| AND | | | OR | | |
|---|---|---|---|---|---|
| $x_1$ | $x_2$ | AND | $x_1$ | $x_2$ | OR |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 |

- **AND** linearly separable (শুধু $(1,1) = 1$)
- **OR** linearly separable (শুধু $(0,0) = 0$)
- **XOR linearly separable না** ⟹ **একটা single perceptron XOR শিখতে পারে না।**

### XOR কেন গুরুত্বপূর্ণ
একটা ছোট সমস্যা, কিন্তু মৌলিক সীমা দেখায়: **একটা single linear neuron সব function represent করতে পারে না।** এটাই multiple neurons, hidden layers ও nonlinear activation-এর কারণ।

## 17. সমাধান: Hidden Layer যোগ করা `[B2]`

> **Source:** p14–15 (§7, §7.1–7.3)

Input → Hidden layer → Output। Hidden neuron **intermediate representation** শেখে: $x \to h \to y$।

### 7.1 AND, OR, NOT দিয়ে XOR
$$\text{XOR}(x_1,x_2) = (x_1\ \text{OR}\ x_2)\ \text{AND NOT}\ (x_1\ \text{AND}\ x_2)$$

Hidden neurons: $h_1 = x_1\ \text{OR}\ x_2,\quad h_2 = x_1\ \text{AND}\ x_2$। Output: $y = h_1\ \text{AND NOT}(h_2)$।

| $x_1$ | $x_2$ | $h_1 = $ OR | $h_2 = $ AND | $y = h_1\wedge\neg h_2$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

### 7.2 Threshold neuron দিয়ে numerical construction
$\text{step}(z) = \begin{cases}1 & z>0\\0 & z\le 0\end{cases}$

- OR: $h_1 = \text{step}(x_1 + x_2 - 0.5)$
- AND: $h_2 = \text{step}(x_1 + x_2 - 1.5)$
- Output: $y = \text{step}(h_1 - h_2 - 0.5)$

Check (সব চার case):
- $(0,0)$: $h_1 = 0,\ h_2 = 0$ ⟹ $y = 0$
- $(0,1)$: $h_1 = 1,\ h_2 = 0$ ⟹ $y = 1$
- $(1,0)$: $h_1 = 1,\ h_2 = 0$ ⟹ $y = 1$
- $(1,1)$: $h_1 = 1,\ h_2 = 1$ ⟹ $y = 0$

PDF: "Thus, the hidden layer enables a network of threshold neurons to represent XOR."

### 7.3 Representation learning
মূল input representation $(x_1, x_2)$; hidden representation $(h_1, h_2)$। Network কেবল মূল input coordinate-এর উপর নির্ভর না করে **দরকারি intermediate feature শেখে।**

## 18. Nonlinear Activation কেন দরকার `[A5, B7]`

> **Source:** p15 (§8, §9)

শুধু affine transformation করলে: $h = W_1x + b_1,\quad y = W_2h + b_2$। প্রথমটা দ্বিতীয়টায় বসালে:

$$y = W_2(W_1x + b_1) + b_2 = W_2W_1x + W_2b_1 + b_2$$

এটা **এখনও $x$-এর affine transformation**। তাই nonlinear activation ছাড়া affine layer stack করে deep network-এর প্রত্যাশিত expressive power আসে না।

Nonlinear activation $h = f(Wx + b)$ হলে network nonlinear সম্পর্ক শিখতে পারে। সংক্ষেপে: **অনেক affine layer (nonlinearity ছাড়া) ≡ একটা affine transformation।**

**Common activation functions (PDF):** Step function · Sigmoid · Hyperbolic tangent (tanh) · Rectified Linear Unit (ReLU) · Leaky ReLU · Softmax। এই lecture-এর focus **ReLU**।

## 19. ReLU Activation Function `[B7, A5]`

> **Source:** p16–17 (§10, §10.1–10.4)

ReLU = **Rectified Linear Unit**।

$$\boxed{ReLU(x) = \max(0,x)} \quad\text{অথবা}\quad ReLU(x) = \begin{cases}0 & x<0\\x & x\ge0\end{cases}$$

সহজ ভাষায়: **Negative input → output 0 · Positive input → input অপরিবর্তিত · Zero input → output 0**

### 10.1 উদাহরণ (PDF)
$ReLU(5) = 5$ · $ReLU(-3) = 0$ · $ReLU(0) = 0$ · $ReLU(2.7) = 2.7$ · $ReLU(-8.4) = 0$
প্রশ্ন (PDF): $ReLU(-2.5) = ?$ → **0**

### 10.2 ReLU graph (Figure 3)
x-axis $-4 \ldots 4$, y-axis $1 \ldots 4$; $x<0$-তে flat $y=0$; $x \ge 0$-তে রেখা $y = x$ ($(4,4)$ পর্যন্ত)।

### 10.3 ReLU কেন জনপ্রিয়?
1. **Simple:** $ReLU(x) = \max(0,x)$
2. **Computationally inexpensive:** comparison ও selection লাগে, exponential না
3. **Nonlinear:** piecewise linear হলেও layer জুড়ে nonlinear function represent করতে পারে
4. **Often helps optimization:** positive side-এ derivative = 1, তাই sigmoid/tanh-এর মতো **positive-side saturation** নেই

### 10.4 ReLU derivative-এর note
$$ReLU'(x) = \begin{cases}0 & x<0\\1 & x>0\end{cases}$$
**$x = 0$-তে ReLU classical অর্থে differentiable না;** implementation একটা **subgradient convention** নেয়, সাধারণত **0**।

**Limitation:** কোনো neuron সব input-এর জন্য negative region-এ থাকলে ReLU-র মধ্য দিয়ে gradient zero → ওই path-এ update বন্ধ। একে **dying ReLU problem** বলে।

## 20. Quick Review ও Key Takeaways `[B1, B2, B7]`

> **Source:** p17

**Classroom questions (PDF):**
1. What is a feedforward neural network?
2. What do weights and biases do in a neuron?
3. Why can a single perceptron represent AND and OR but not XOR?
4. What does it mean for a dataset to be linearly separable?
5. How does a hidden layer help solve XOR?
6. Why are nonlinear activation functions necessary?
7. Calculate $ReLU(-4)$, $ReLU(0)$, $ReLU(3.5)$ → **0, 0, 3.5**
8. What can happen if a network stacks many affine layers without nonlinear activation? → সবটা মিলে **একটাই affine transformation** হয়।

**Key Takeaways (PDF):**
- A neuron computes a weighted sum plus a bias and applies an activation function.
- A single perceptron has a linear decision boundary and cannot represent XOR.
- A hidden layer can construct intermediate features that make XOR solvable.
- Stacking affine layers alone does not create a nonlinear model.
- Nonlinear activations are essential for the expressive power of deep feedforward networks.
- ReLU is simple and computationally efficient, and often supports effective gradient-based training.

(Reference: Goodfellow et al., *Deep Learning*, MIT Press 2016, Chapter 6 "Deep Feedforward Networks" — p18)

---

# PART 4 — Gradient-Based Learning, Output Units, Hidden Units (p19–27)

> **Title:** "Deep Learning Lecture: Gradient-Based Learning, Output Units and ReLU"

## 21. Problem: Network Attack চেনা `[B4, B5]`

> **Source:** p19–20 ("1 Start with the problem")

একটা cybersecurity classification সমস্যা পুরো lesson জুড়ে: network traffic benign না malicious; পরে benign / DDoS / port scan। এই এক উদাহরণ থেকে বোঝা যায়: কেন cost function লাগে, কেন বিভিন্ন output unit, hidden unit কী feature বের করে, ReLU কীভাবে gradient-based learning-কে সাহায্য করে।

| Feature | Meaning | Example value |
|---|---|---|
| $x_1$ | Normalized packet-rate feature | 2 |
| $x_2$ | Normalized connection-failure feature | 1 |

Input vector $\mathbf{x} = [2, 1]^\top$। প্রথম task-এর target: $y = 0$ Benign, $y = 1$ Malicious; training label $y = 1$। Model probability $P(y=1|\mathbf{x})$ শিখবে (arbitrary numerical score না)।

**চারটা প্রশ্ন (PDF):** (1) Model কীভাবে probability বানায়? (2) Prediction ও সঠিক উত্তরের পার্থক্য কীভাবে মাপি? (3) Error কমাতে weight কীভাবে বদলায়? (4) Hidden unit ও ReLU কেন লাগে?

**Network diagram (§1.1):**
- Input layer: $\mathbf{x} = [2,1]^\top$
- Hidden layer (ReLU): $\mathbf{h} = ReLU(W^\top\mathbf{x} + \mathbf{b})$ (learned feature)
- Output layer: Sigmoid (binary) অথবা Softmax (multiclass)
- Cost: $J(\theta) = -\log P(y|\mathbf{x};\theta)$

Network forward pass-এ prediction বানায়, তারপর cost, gradient হিসাব করে parameter বদলায়। Section 6.2-এর মূল idea: **model define → cost function বাছা → optimization procedure দিয়ে cost কমানো।**

## 22. Gradient-Based Learning `[B5]`

> **Source:** p20–21 ("2 Section 6.2")

**মানে:** Network-এ trainable parameter (weights, biases)-কে vector $\theta$-তে রাখি। Prediction $\hat y = f(x;\theta)$। Cost: $J(\theta) = L(f(x;\theta), y)$। Training objective:

$$\theta^* = \arg\min_\theta J(\theta)$$

**Gradient** $\nabla_\theta J(\theta)$ বলে parameter বদলালে cost কীভাবে বদলায়। Basic update:

$$\boxed{\theta_{new} = \theta_{old} - \eta\nabla_\theta J}$$

($\eta$ = learning rate)। PDF-এর উপমা: "Think of the cost as the **height of a landscape**. The gradient indicates the direction of the **steepest increase**, so subtracting the gradient moves the parameters locally in the direction of **decreasing cost**."

### Training-এ কী হয় (4 ধাপ)
1. **Forward pass:** input layer দিয়ে চালিয়ে prediction
2. **Cost calculate:** known label-এর সাথে suitable loss function দিয়ে তুলনা
3. **Gradient calculate:** weight ও bias-এর সাপেক্ষে cost কীভাবে বদলায়
4. **Parameters update:** gradient descent বা SGD-র মতো optimizer; তারপর repeat

(Network জুড়ে gradient efficiently বের করার algorithm = **backpropagation**, Goodfellow §6.5)

## 23. Cost Function (Maximum Likelihood) `[B4]`

> **Source:** p21 ("2.3 The cost function in Goodfellow's framework")

$$J(\theta) = -\mathbb{E}_{(x,y)\sim\hat p_{data}}[\log p_{model}(y|x;\theta)]$$

- $\hat p_{data}$ = training data-র empirical distribution
- $p_{model}(y|x;\theta)$ = model যে probability correct target-কে দেয়
- Negative log: model correct answer-কে **কম** probability দিলে শাস্তি

$N$ উদাহরণে: $J(\theta) = -\frac1N\sum_{i=1}^N\log p_{model}(y_i|x_i;\theta)$ = **negative log-likelihood**, modeled output distribution-এর জন্য উপযুক্ত **cross-entropy** objective-এর সমতুল্য।

## 24. Binary Cross-Entropy ও Logistic Regression `[B4]`

> **Source:** p21–22 (§3, §3.1–3.3)

Model malicious probability দেয়; true $y=1$। Model $0.80$ দিলে quality কীভাবে মাপি?

$$L(y,p) = -[y\log p + (1-y)\log(1-p)],\quad p = P(y=1|\mathbf{x})$$
$y = 1$ হলে $L = -\log p$।

- $p = 0.80$: $L = -\ln(0.80) = \boxed{0.2231}$
- Confidently wrong $p = 0.10$: $L = -\ln(0.10) = \boxed{2.3026}$

দ্বিতীয় model অনেক বড় loss পায়, কারণ correct class-কে কম probability দিয়েছে। **Teaching point:** cross-entropy শুধু class ঠিক/ভুল দেখে না, **correct answer-কে কত probability দিয়েছে** তাও দেখে।

| Predicted probability of malicious | True label | Cross-entropy loss |
|---|---|---|
| 0.95 | 1 | 0.0513 |
| 0.80 | 1 | 0.2231 |
| 0.50 | 1 | 0.6931 |
| 0.10 | 1 | 2.3026 |

### 3.2 Logistic regression
Binary classification model: আগে linear score, তারপর sigmoid। $z = \mathbf{w}^\top\mathbf{x} + b$; $p = P(y=1|\mathbf{x}) = \sigma(z) = \frac{1}{1+e^{-z}}$; threshold সাধারণত $0.5$।

উদাহরণ $z = 1$: $p = \frac{1}{1+e^{-1}} \approx \mathbf{0.7311}$ (73.11% malicious)। $y = 1$: $L = -\ln(0.7311) \approx \mathbf{0.3133}$।

Sigmoid output + cross-entropy **স্বাভাবিক choice**, কারণ binary target-এর probability distribution define করে ও maximum likelihood দিয়ে train করে।

### 3.3 Logistic regression ও deep neural network
- Standard logistic regression: $p = \sigma(\mathbf{w}^\top\mathbf{x} + b)$ (মূল feature সরাসরি)
- Neural network: hidden layer আগে learned representation $\mathbf{h}$ বানায়, তারপর output layer logistic regression চালায়: $p = \sigma(\mathbf{w}^\top\mathbf{h} + b)$
- Difference: network **representation $\mathbf{h}$ শেখে**; logistic regression সরাসরি $\mathbf{x}$ ব্যবহার করে। Network nonlinear hidden transformation + পরিচিত logistic-regression output layer মেলাতে পারে।

## 25. Output Units `[B6]`

> **Source:** p22 (§4, "Section 6.2.2")

Goodfellow-এর জোর: **output unit-এর পছন্দ cost function-এর সাথে ঘনিষ্ঠভাবে যুক্ত।** Output layer-কে target variable-এর ধরন represent করতে হবে। দুই task:
- **Task A:** Traffic benign না malicious? (binary)
- **Task B:** Traffic benign, DDoS না port scan? (multiclass)

### 25.1 Sigmoid unit — Bernoulli output `[B6]`
> **Source:** p23 (§5, §5.1–5.3)

**কখন:** binary random variable (benign/malicious, spam/not spam, disease detected/not)। Bernoulli distribution **এক probability** $p = P(y=1|\mathbf{x})$ দিয়েই সম্পূর্ণ; অন্য outcome $P(y=0|\mathbf{x}) = 1-p$।

$$\hat y = \sigma(z),\quad z = \mathbf{w}^\top\mathbf{h} + b,\qquad P(y|\mathbf{x}) = \hat y^{\,y}(1-\hat y)^{1-y}$$
এর negative log-likelihood = **binary cross-entropy loss**।

**Sigmoid graph:** S-আকার; finite input-এ output strictly 0 ও 1-এর মাঝে।

| Logit $z$ | Sigmoid output | Interpretation |
|---|---|---|
| −2 | 0.1192 | Low probability of an attack |
| 0 | 0.5000 | Equal predicted probabilities |
| 1 | 0.7311 | Higher probability of an attack |
| 2 | 0.8808 | High probability of an attack |

Sigmoid output **probability estimate**, prediction সঠিক হওয়ার গ্যারান্টি না। Class label-এর জন্য threshold লাগে; 0.5 common, কিন্তু operational security system false positive/false negative cost অনুযায়ী ভিন্ন threshold নিতে পারে।

**এক পূর্ণ prediction:** hidden layer $\mathbf{h} = [2, 1]^\top$ দেয়; output weights: $z = 0.7h_1 + 0.4h_2 - 0.8 = 0.7(2) + 0.4(1) - 0.8 = 1$। তাই $p = \sigma(1) = 0.7311$; malicious ($y=1$) হলে $L = -\ln(0.7311) = 0.3133$। Model সঠিক দিকে, কিন্তু target-কে probability 1 দেয়নি।

**Gradient-based learning দিয়ে উন্নতি (p24):** Sigmoid + BCE-র জন্য output logit-এর সাপেক্ষে derivative:
$$\frac{\partial L}{\partial z} = p - y = 0.7311 - 1 = \mathbf{-0.2689}$$
Negative gradient: $z$ বাড়ালে loss কমে। $\eta = 0.1$, শুধু output weight ও bias update: $\frac{\partial L}{\partial w_j} = (p-y)h_j$, $\frac{\partial L}{\partial b} = p-y$।

| Parameter | Before | After one update |
|---|---|---|
| $w_1$ | 0.7000 | 0.7538 |
| $w_2$ | 0.4000 | 0.4269 |
| $b$ | −0.8000 | −0.7731 |

নতুন logit ≈ 1.1614 ⟹ $p_{new} \approx 0.7615$ (exact 0.7616), $L_{new} = -\ln(p_{new}) \approx 0.2725$ (exact 0.2724)। Loss ≈ 0.3133 থেকে ≈ 0.2725 কমেছে। PDF: "one illustrative update; a complete training procedure also propagates gradients through the hidden layer."

### 25.2 Softmax unit — Multinoulli output `[B6]`
> **Source:** p24–25 (§6, §6.1–6.4)

Task B: Benign, DDoS attack, Port scan — **mutually exclusive** (প্রতি input-এর একটাই সঠিক class)। এখানে single sigmoid পুরো distribution-এর স্বাভাবিক উপায় না; **softmax** লাগে।

**Softmax equation:** logits $\mathbf{z} = [z_1, \ldots, z_K]$:
$$\boxed{p_k = \frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}}},\qquad 0 < p_k < 1,\quad \sum_{k=1}^K p_k = 1$$
Softmax-এর আগের score = **logits**; এরা probability না, যেকোনো real number হতে পারে।

**তিন-class উদাহরণ:** logits: Benign 0, DDoS 2, Port scan 1। $e^0 = 1,\ e^2 = 7.389,\ e^1 = 2.718$; sum $\approx 11.107$:
- $P(\text{Benign}|x) = 1/11.107 \approx \mathbf{0.090}$
- $P(\text{DDoS}|x) = 7.389/11.107 \approx \mathbf{0.665}$
- $P(\text{Port scan}|x) = 2.718/11.107 \approx \mathbf{0.245}$
- Predicted class = **DDoS** (সবচেয়ে বড় probability)

**Softmax ও cross-entropy:** True class DDoS, one-hot $\mathbf{y} = [0,1,0]$। Single-label multiclass-এ $L = -\sum_{k=1}^K y_k\log p_k$। শুধু DDoS entry 1, তাই $L = -\ln(0.665) \approx \mathbf{0.408}$। Correct class-এ probability বাড়ালে loss কমে।

Softmax + cross-entropy-র logit gradient সরল: $\boxed{\dfrac{\partial L}{\partial z_k} = p_k - y_k}$

### Sigmoid versus Softmax (PDF table)
| Property | Sigmoid output | Softmax output |
|---|---|---|
| Typical application | Binary classification | Single-label multiclass classification |
| Output structure | One probability for positive class | One probability per class |
| Probability relationship | Negative class has probability $1-p$ | All class probabilities sum to 1 |
| Distribution | Bernoulli | Multinoulli / categorical |
| Loss | Binary cross-entropy | Multiclass cross-entropy |
| Example | Benign versus attack | Benign, DDoS or port scan |

**Important distinction (PDF):** একই traffic sample-এ **একসাথে একাধিক label সত্য** হতে পারলে (একাধিক independent attribute), **আলাদা আলাদা sigmoid output** বেশি উপযুক্ত। Softmax **mutually exclusive alternatives**-এর probability distribution-এর জন্য।

## 26. Hidden Units ও ReLU `[B7]`

> **Source:** p26–27 (§7, §8)

এতক্ষণ output layer; এখন hidden feature $\mathbf{h}$ কোথা থেকে আসে? Hidden layer weights, biases ও activation function দিয়ে original input রূপান্তর করে। Goodfellow notation:

$$\mathbf{h} = g(W^\top\mathbf{x} + \mathbf{b})$$
($W$ = layer-এর weights, $\mathbf{b}$ = biases, $g$ = activation function, $\mathbf{h}$ = hidden activations)

### 7.1 ReLU দিয়ে hidden layer হিসাব
$\mathbf{x} = [2, 1]^\top$; উদাহরণ linear score:
- $z_1 = x_1 + x_2 - 1 = 2$
- $z_2 = x_1 - x_2 = 1$

ReLU: $h_1 = ReLU(2) = 2,\ h_2 = ReLU(1) = 1$ ⟹ $\mathbf{h} = [2, 1]^\top$।

### 8.1 ReLU কী (§6.3.1)
$$g(z) = \max(0,z) = \begin{cases}0 & z\le 0\\z & z>0\end{cases}$$

### 8.2 ReLU বনাম Sigmoid
- **ReLU:** negative input-এ zero; positive input অপরিবর্তিত; derivative $z>0$-তে 1, $z<0$-তে 0; zero-তে not differentiable (subgradient convention)।
- **Sigmoid:** output 0 ও 1-এর মাঝে, binary probability-র জন্য কাজের; extreme input-এ 0/1-এর দিকে **saturate** করে; gradient খুব ছোট হতে পারে।

Goodfellow ReLU-কে hidden unit-এর **excellent default** বলে, কারণ active region-এ linearly আচরণ করে ও input খুব positive হলেও gradient কমে না।

| Linear score $z$ | ReLU output $\max(0,z)$ | Interpretation |
|---|---|---|
| −2 | 0 | Unit inactive for this input |
| −0.5 | 0 | Unit inactive for this input |
| 0 | 0 | Output is zero |
| 0.5 | 0.5 | Positive activation |
| 2 | 2 | Positive activation |

### 8.4 ReLU কেন training-এ সাহায্য করে
$$g'(z) = \begin{cases}0 & z<0\\1 & z>0\end{cases}$$
ReLU unit active হলে derivative 1, তাই gradient activation দিয়ে **saturation ছাড়াই** পার হয় (sigmoid hidden unit-এর সমস্যা এড়ায়)। ReLU piecewise linear-ও।

### 8.5 Generalization কী?
**Generalization** = trained model-এর **আগে-না-দেখা উদাহরণে** ভালো করার ক্ষমতা। **ReLU generalization গ্যারান্টি করে না;** hidden layer optimize করা সহজ করে, কিন্তু generalization নির্ভর করে training data, model capacity, architecture ও validation-এর উপর।

## 27. সব মিলিয়ে (Put all the concepts together) `[B4–B7]`

> **Source:** p27 ("9 Put all the concepts together")

| Concept | Purpose |
|---|---|
| Gradient-based learning | neural network-এর parameter optimize করে |
| Cross-entropy | predicted output distribution ও target-এর mismatch মাপে |
| Logistic regression | linear score থেকে binary-class probability বানায় |
| Sigmoid output | Bernoulli probability represent করে |
| Softmax output | mutually exclusive class-এর probability distribution |
| Hidden units | intermediate feature representation শেখে |
| ReLU | nonlinearity আনে, gradient-কে পার হতে দেয় |
| Generalization | unseen data-তে performance মাপে |

Primary reading: Goodfellow, Bengio, Courville — Chapter 6; Sections 6.2, 6.2.1, 6.2.2.2, 6.2.2.3, 6.3, 6.3.1।

### Exam-ready Q&A
**Q. Sigmoid কখন, softmax কখন?** A. Binary-তে sigmoid (Bernoulli); mutually exclusive multiclass-এ softmax (সব probability-র যোগফল 1)।
**Q. Softmax + CE-র gradient?** A. $\partial L/\partial z_k = p_k - y_k$।
**Q. ReLU কেন hidden unit-এ popular?** A. সহজ, সস্তা, positive side-এ derivative 1 (saturate করে না)।
**Q. ReLU generalization গ্যারান্টি করে?** A. না।

---

# PART 5 — Architecture, Universal Approximation, Backpropagation (p28–38)

> **Title:** "Architecture Design, Universal Approximation and Backpropagation" · Goodfellow Chapter 6, Sections 6.4, 6.4.1, 6.5, 6.5.2, 6.5.4

## 28. Problem `[B8]`

> **Source:** p28 ("1 Begin with our classification problem")

PDF: একই network-security সমস্যা (Benign, DDoS, Port scan)। XOR উদাহরণ এখানে ব্যবহার হবে না। Lesson একটা ছোট **fully connected multilayer perceptron (MLP)** বানিয়ে forward pass, loss, gradient, parameter update **হাতে হিসাব** করে; এটা দিয়ে architecture design, universal approximation theorem, Jacobian, chain rule ও backpropagation বোঝানো হয়। Goodfellow: deep feedforward network = function-approximation model; backprop = network জুড়ে gradient হিসাবের efficient উপায়।

Input $\mathbf{x} = [2,1]^\top$ ($x_1$ packet-rate = 2, $x_2$ connection-failure = 1)। তিন mutually exclusive class: $C_1$ = Benign, $C_2$ = DDoS, $C_3$ = Port scan। Training example-এর সঠিক class **DDoS**; one-hot $\mathbf{y} = [0,1,0]^\top$ (সঠিক class-এ 1, বাকিতে 0)। লক্ষ্য: $P(C_k|\mathbf{x})$ ($k=1,2,3$) হিসাব করা ও সঠিক class-এ বেশি probability দেওয়া শেখা।

## 29. Architecture Design (Section 6.4) `[B8]`

> **Source:** p29–30 (§2, §2.1–2.4)

**Architecture** = network-এর সংগঠন: layers, প্রতি layer-এ unit-সংখ্যা, connections, input→output রূপান্তরের operation। আমাদের পছন্দ:
- **Input layer:** 2 features (packet rate, connection failures)
- **Hidden layer:** 2 **ReLU** unit (input feature-এর combination শেখে)
- **Output layer:** 3 **Softmax** unit (Benign, DDoS, Port scan probability)

এটাকে **2–2–3 MLP** বলে: 2 input, 2 hidden, 3 output; **এক hidden layer**। Hidden-এ ReLU, output-এ Softmax (তিন mutually exclusive class)। এটা ইচ্ছাকৃতভাবে ছোট teaching network; বাস্তব traffic classifier-এ আরও feature লাগবে ও validation experiment দিয়ে architecture বাছা হবে।

### Fully connected layer মানে
প্রতিটা unit আগের layer-এর **সব** unit থেকে input পায়: প্রতিটা hidden unit দুই input feature-ই পায়; প্রতিটা output unit দুই hidden activation-ই পায়।

First layer: $z^{(1)} = \mathbf{x}^\top W^{(1)} + b^{(1)}$, $\ \mathbf{h} = ReLU(z^{(1)})$। Output layer: $z^{(2)} = \mathbf{h}^\top W^{(2)} + b^{(2)}$ (column-vector notation-এ transposed; row-vector-এ $x^\top W^{(1)}$, $h^\top W^{(2)}$)। Softmax:
$$p_k = \frac{e^{z_k^{(2)}}}{\sum_{j=1}^3 e^{z_j^{(2)}}}$$
সবচেয়ে বড় probability-র output = predicted class।

### Trainable parameter count `[B8]` ⭐
| Layer | হিসাব | Parameters |
|---|---|---|
| Input → hidden | $2\times2 = 4$ weights + 2 hidden biases | **6** |
| Hidden → output | $2\times3 = 6$ weights + 3 output biases | **9** |

$$\boxed{6 + 9 = 15\text{ trainable parameters}}$$
সাধারণ সূত্র: $\sum(\text{in}\times\text{out} + \text{out})$। এই সংখ্যা model capacity, memory, computational cost ও দরকারি training data-কে প্রভাবিত করে।

### Architecture কীভাবে বাছে?
কোনো একক architecture সব task-এর জন্য সেরা না। Goodfellow: **width, depth, connectivity** design decision; practical পছন্দ **validation performance** দিয়ে।

| Design decision | Teaching interpretation | Our example |
|---|---|---|
| Input width | কয়টা feature model-এ ঢোকে | 2 |
| Hidden width | প্রতি hidden layer-এ কয়টা unit | 2 |
| Depth | কয়টা পর পর transformation | 1 hidden layer |
| Output width | কয়টা output = সম্ভাব্য class | 3 |
| Connectivity | adjacent layer-এর unit কীভাবে যুক্ত | Fully connected |

Model খুব ছোট হলে গুরুত্বপূর্ণ pattern ধরতে পারে না; অকারণে বড় হলে train করা ব্যয়বহুল ও overfitting-এর ঝুঁকি। পছন্দ নির্ভর করে task-এর জটিলতা, data ও computational resource-এর উপর।

## 30. Universal Approximation Theorem (Section 6.4.1) `[B9]`

> **Source:** p30–31 (§3, §3.1–3.3)

**Theorem:** suitable **nonlinear hidden-unit activation** ও **যথেষ্ট hidden unit**-সহ feedforward network অনেক বড় function class **যেকোনো precision-এ approximate** করতে পারে। যেমন একটা sufficiently wide one-hidden-layer network compact input domain-এ যেকোনো continuous function approximate করতে পারে। **ReLU networks-এরও** universal approximation ফল আছে।

**সহজ ভাষায (PDF):** প্রতিটা pattern-এর জন্য আলাদা বিশেষ সূত্র লাগে না; weights, biases ও nonlinear activation মিলে জটিল input-output সম্পর্ক approximate করে। আমাদের target function:

$$f^*: \mathbf{x} \longrightarrow \begin{bmatrix}P(\text{Benign}|\mathbf{x})\\P(\text{DDoS}|\mathbf{x})\\P(\text{Port scan}|\mathbf{x})\end{bmatrix}$$

Network labeled example থেকে এই function-এর approximation শেখে।

### শুধু linear model কেন না?
Nonlinear hidden activation ছাড়া linear layer stack = আবার linear/affine। $h = W^{(1)\top}x + b^{(1)}$ ও $z = W^{(2)\top}h + b^{(2)}$ বসালে $x$-এর আরেকটা affine function; extra layer একা nonlinear feature transformation আনে না। ReLU আনে:
$$h = ReLU(W^{(1)\top}x + b^{(1)})$$
ReLU nonlinear বলে network input feature ও output class-এর মধ্যে nonlinear সম্পর্ক represent করে (যেমন benign বনাম DDoS শুধু এক feature না, packet rate ও connection failure-এর combination-এর উপর)।

### এক hidden layer তাত্ত্বিকভাবে যথেষ্ট হলে deep network কেন?
Theorem **representational capability**-র কথা বলে; কোনো practical network desired function **efficiently শিখবে** তার গ্যারান্টি না। এক hidden layer কিছু function-এর জন্য **বিপুল সংখ্যক unit** লাগতে পারে। বাড়তি layer compositional/hierarchical function **কম parameter**-এ represent করতে পারে। Goodfellow: deeper ReLU network-এর linear region-এর সংখ্যা গভীরতার সাথে দ্রুত বাড়ে।
- **Shallow:** এক hidden layer তাত্ত্বিকভাবে জটিল function approximate করে, কিন্তু অনেক unit লাগে
- **Deep:** একাধিক hidden layer ক্রমান্বয়ে representation গড়ে, জটিল গঠন efficiently ধরে

### তিনটা গুরুত্বপূর্ণ limitation (মুখস্থ) ❗
1. ❌ Training algorithm সঠিক parameter **পাবে** তার গ্যারান্টি দেয় না
2. ❌ অদেখা traffic-এ **good generalization**-এর গ্যারান্টি দেয় না
3. ❌ Deeper network **সবসময় better বা সহজে optimize হয়** — এমন বলে না

বাস্তবে depth ও width **hyperparameter**, data দিয়ে select/evaluate করতে হয়।

### Exam-ready Q&A
**Q. 2–2–3 MLP-এ parameter কয়টা?** A. $(2\cdot2+2) + (2\cdot3+3) = 15$।
**Q. UAT কি বলে GD সঠিক parameter পাবে?** A. না; এটা শুধু representation capability নিয়ে।
**Q. Deeper network কি সবসময় better?** A. না।

## 31. Backpropagation — concept (Section 6.5) `[B10]`

> **Source:** p31 ("4 Section 6.5 — Backpropagation")

প্রশ্ন: Network 15টা parameter-এর মান শেখে কীভাবে? উত্তর: **backpropagation + optimization method (যেমন SGD)।**

**গুরুত্বপূর্ণ পার্থক্য (Goodfellow):** **Backpropagation gradient *calculate* করে; gradient descent বা অন্য optimizer সেই gradient দিয়ে parameter *update* করে।** Backprop নিজে computational graph-এ derivative efficiently মূল্যায়নের **general procedure**।

- **Forward propagation:** input layer থেকে output-এর দিকে activation, logits, probability ও loss
- **Backward propagation:** loss-এর derivative থেকে শুরু করে output ও hidden layer দিয়ে পেছনে gradient, প্রতিটা parameter loss-কে কীভাবে প্রভাবিত করে
- **Parameter update:** gradient দিয়ে weight/bias update, তারপর repeat

## 32. Chain Rule, Gradient, Jacobian (Section 6.5.2) `[B10]`

> **Source:** p33–34 (§5, §5.1–5.5)

### 5.1 Chain rule — সরল উদাহরণ
$u = 2x,\ L = u^2$ ⟹ $L = (2x)^2$। Chain rule: $\dfrac{dL}{dx} = \dfrac{dL}{du}\dfrac{du}{dx}$; $\dfrac{dL}{du} = 2u,\ \dfrac{du}{dx} = 2$ ⟹ $\dfrac{dL}{dx} = 2u \times 2 = 4u$। $x = 3$: $u = 6$ ⟹ **$\dfrac{dL}{dx} = 12 \times 2 = \boxed{24}$**।

মূল ধারণা (PDF): একটা variable অন্যটার উপর মধ্যবর্তী operation দিয়ে নির্ভর করলে **পথ বরাবর local derivative গুণ** করি। Neural network = অনেক operation-এর বড় composition; **backprop এই একই নীতি প্রতিটা প্রাসঙ্গিক weight ও bias-এ পদ্ধতিগতভাবে প্রয়োগ করে।**

### 5.2 Gradient কী
Scalar loss $L$ ও parameter vector $\theta$:
$$\nabla_\theta L = \begin{bmatrix}\partial L/\partial\theta_1\\\partial L/\partial\theta_2\\\vdots\\\partial L/\partial\theta_n\end{bmatrix}$$
প্রতি entry দেখায়: **অন্য parameter ঠিক রেখে** এক parameter বদলালে loss কতটা বদলায়। আমাদের network-এ parameter = $W^{(1)}, W^{(2)}$-র সব entry ও দুই bias vector।

### 5.3 Jacobian matrix কী
Gradient = scalar function-এর input-এর সাপেক্ষে derivative। **Jacobian** = vector → vector function-এর generalization। $\mathbf{y} = f(\mathbf{x})$, $\mathbf{x}\in\mathbb{R}^m$, $\mathbf{y}\in\mathbb{R}^n$:
$$J_f(\mathbf{x}) = \frac{\partial\mathbf{y}}{\partial\mathbf{x}} = \begin{bmatrix}\frac{\partial y_1}{\partial x_1} & \cdots & \frac{\partial y_1}{\partial x_m}\\\vdots & \ddots & \vdots\\\frac{\partial y_n}{\partial x_1} & \cdots & \frac{\partial y_n}{\partial x_m}\end{bmatrix}$$
প্রতিটা output component প্রতিটা input component-এ কীভাবে সাড়া দেয় তার তালিকা। Scalar loss $L$ $\mathbf{y}$-এর উপর নির্ভর করলে **vector chain rule:**
$$\boxed{\nabla_\mathbf{x}L = J_f(\mathbf{x})^\top\nabla_\mathbf{y}L}$$
(superscript $\top$ = transpose)। **এটাই backprop-এর কেন্দ্রীয় গাণিতিক ক্রিয়া:** এক operation থেকে তার input-এ gradient পাঠানো **local Jacobian** দিয়ে।

### 5.4 Softmax-এর Jacobian
$p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$-এর Jacobian entry:
$$\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j),\quad \delta_{ij} = \begin{cases}1&i=j\\0&i\neq j\end{cases}$$

$\mathbf{p} = [0.090031, 0.665241, 0.244728]^\top$-এ approximate:
$$J_{softmax} \approx \begin{bmatrix}0.081925 & -0.059892 & -0.022033\\-0.059892 & 0.222695 & -0.162803\\-0.022033 & -0.162803 & 0.184836\end{bmatrix}$$
প্রতিটা row দেখায় এক predicted probability তিন logit বদলালে কীভাবে বদলায়। **এক logit বদলালে একাধিক class probability বদলায়,** কারণ softmax সব class একসাথে normalize করে (যোগফল 1)।

### 5.5 Softmax Jacobian + cross-entropy
One-hot target-এ $L = -\sum_i y_i\ln p_i$; probability-র সাপেক্ষে $\dfrac{\partial L}{\partial p_i} = -\dfrac{y_i}{p_i}$। Softmax দিয়ে chain rule: $\dfrac{\partial L}{\partial z_j} = \sum_i\dfrac{\partial L}{\partial p_i}\dfrac{\partial p_i}{\partial z_j}$, যা সরল হয়ে:
$$\boxed{\frac{\partial L}{\partial z_j} = p_j - y_j}\quad\Longrightarrow\quad\delta^{(2)} = \mathbf{p} - \mathbf{y}$$

DDoS উদাহরণ:
$$\delta^{(2)} = \begin{bmatrix}0.090031\\0.665241\\0.244728\end{bmatrix} - \begin{bmatrix}0\\1\\0\end{bmatrix} = \begin{bmatrix}0.090031\\-0.334759\\0.244728\end{bmatrix}$$
এগুলো তিন output logit-এর সাপেক্ষে loss-এর gradient; **backward calculation শুরু করে।**

## 33. ⚠️ 2–2–3 MLP-এর পুরো Forward + Backprop + SGD (p32–38) — exam-এ math আসবে না

> **Source:** p32 (§4.2), p34–38 (§6, §7, §8) · শুধু বোঝার জন্য; সব সংখ্যা computer দিয়ে মিলানো ✓

### Forward pass (p32)
Column-vector notation। $\mathbf{x} = [2,1]^\top$। Illustrative (প্রশিক্ষিত না) initial values:

$$W^{(1)} = \begin{bmatrix}0.5 & -0.5\\-0.5 & 1.0\end{bmatrix},\ \mathbf{b}^{(1)} = \begin{bmatrix}0\\0.5\end{bmatrix},\qquad W^{(2)} = \begin{bmatrix}0&1&2\\0&3&0\end{bmatrix},\ \mathbf{b}^{(2)} = \begin{bmatrix}0\\0\\0\end{bmatrix}$$

Hidden pre-activation $\mathbf{z}^{(1)} = W^{(1)\top}\mathbf{x} + \mathbf{b}^{(1)} = [0.5, 0]^\top + [0, 0.5]^\top = [0.5, 0.5]^\top$। দুটোই positive ⟹ $\mathbf{h} = ReLU(\mathbf{z}^{(1)}) = [0.5, 0.5]^\top$।
Output logits $\mathbf{z}^{(2)} = W^{(2)\top}\mathbf{h} + \mathbf{b}^{(2)} = [0, 2, 1]^\top$ (Benign, DDoS, Port scan)। Softmax: $\mathbf{p} = [0.090031, 0.665241, 0.244728]^\top$। **Loss** (true DDoS): $L = -\ln(0.665241) = \boxed{0.407606}$।

### Backward (p34–36)
**Output layer:** $\delta^{(2)} = [0.090031, -0.334759, 0.244728]^\top$; $\nabla_{W^{(2)}}L = \mathbf{h}\,\delta^{(2)\top}$, $\mathbf{h} = [0.5, 0.5]^\top$:
$$\nabla_{W^{(2)}}L \approx \begin{bmatrix}0.045015 & -0.167380 & 0.122364\\0.045015 & -0.167380 & 0.122364\end{bmatrix}$$
Output-bias gradient $\nabla_{\mathbf{b}^{(2)}}L = \delta^{(2)}$ (প্রতি logit নিজের bias-এর উপর নির্ভর করে, derivative 1)।

**Hidden-এ gradient:** $\nabla_\mathbf{h}L = W^{(2)}\delta^{(2)}$:
- $\dfrac{\partial L}{\partial h_1} = 0(0.090031) + 1(-0.334759) + 2(0.244728) = \mathbf{0.154698}$
- $\dfrac{\partial L}{\partial h_2} = 0(0.090031) + 3(-0.334759) + 0(0.244728) = \mathbf{-1.004277}$

চিহ্ন আলাদা, কারণ hidden unit দুটো আলাদা weight দিয়ে output class-কে প্রভাবিত করে।

**ReLU দিয়ে:** $ReLU'(z_i^{(1)}) = 0$ ($z<0$), $1$ ($z>0$)। দুটো pre-activation $0.5$ ⟹ দুই unit active; ReLU Jacobian $J_{ReLU} = \begin{bmatrix}1&0\\0&1\end{bmatrix}$। 
$$\delta^{(1)} = \nabla_\mathbf{h}L \odot ReLU'(\mathbf{z}^{(1)}) = [0.154698, -1.004277]^\top$$
($\odot$ = element-wise গুণ)। **কোনো hidden unit-এর pre-activation negative হলে ওই ReLU derivative 0 হত, ওই current input-এর জন্য gradient ওই activation-এ blocked হত।**

**First layer (p36):** $\nabla_{W^{(1)}}L = \mathbf{x}\,\delta^{(1)\top} = \begin{bmatrix}2\\1\end{bmatrix}[0.154698\ \ -1.004277]$:
$$\nabla_{W^{(1)}}L \approx \begin{bmatrix}0.309396 & -2.008554\\0.154698 & -1.004277\end{bmatrix},\qquad \nabla_{\mathbf{b}^{(1)}}L = \delta^{(1)}$$
➜ এখন **সব 15টা trainable parameter-এর gradient** আছে। Backprop দক্ষ কারণ প্রতি layer-এ gradient **উপরের layer-এর হিসাব reuse** করে; প্রতি parameter-এর জন্য পুরো network আলাদা করে differentiate করতে হয় না।

### SGD update ($\eta = 0.1$, $\theta_{new} = \theta_{old} - \eta\nabla_\theta L$) — p36–37
$$W^{(1)}_{new} \approx \begin{bmatrix}0.469060 & -0.299145\\-0.515470 & 1.100428\end{bmatrix},\quad \mathbf{b}^{(1)}_{new} \approx \begin{bmatrix}-0.015470\\0.600428\end{bmatrix}$$
$$W^{(2)}_{new} \approx \begin{bmatrix}-0.004502 & 1.016738 & 1.987764\\-0.004502 & 3.016738 & -0.012236\end{bmatrix},\quad \mathbf{b}^{(2)}_{new} \approx \begin{bmatrix}-0.009003\\0.033476\\-0.024473\end{bmatrix}$$
Negative gradient ⟹ parameter বাড়ে (SGD বিয়োগ করে)। সব 15টা parameter update হয়েছে।

### নতুন forward pass (p37)
$$\mathbf{z}^{(1)}_{new} \approx [0.407181,\ 1.102566]^\top = \mathbf{h}_{new},\quad \mathbf{z}^{(2)}_{new} \approx [-0.015799,\ 3.773626,\ 0.771416]^\top$$
$$\mathbf{p}_{new} \approx [0.021084,\ 0.932587,\ 0.046328]^\top,\qquad L_{new} = -\ln(0.932587) \approx \mathbf{0.069793}$$

| State | Cross-entropy loss | Predicted DDoS probability |
|---|---|---|
| Before SGD | 0.407606 | 66.52% |
| After SGD | 0.069793 | 93.26% |

**সতর্কতা (PDF):** এটা এক example-এর এক update (learning rate 0.1)। বাস্তবে SGD অনেক sample-এ অনেক iteration/epoch চলে, আর **একটা update সবসময় loss কমায় না।**

**সার-সংক্ষেপ (p38):** Architecture computation define করে; forward propagation prediction হিসাব করে; cost function error মাপে; chain rule ও Jacobian gradient হিসাব করে; backpropagation সেগুলো efficiently পাঠায়; SGD parameter update করে।

**Final picture (p38):** পুরো network-এর নকশা: node, edge-এ initial weight, hidden ও output node-এ computed value, ডানে target ও loss, নিচে backward gradient ও এক SGD update-এর ফল সারাংশ। Primary textbook: Goodfellow et al. Ch 6 (§6.4–6.5.4)।

---

# PART 6 — Gradient Descent math (PNG problem) `[B5]`

> এই PDF-এ SGD ($\theta \leftarrow \theta - \eta\hat g$) ও logistic regression-এর এক step আছে (§9)। নিচে `f_x_gradient_descent.webp`-এর সম্পূর্ণ সমাধান:

> এটা sir-এর notice-এর **Gradient Descent math problem (PNG)**। Exam-এ নিশ্চিত আসার মতো। নিচের সব হিসাব computer দিয়ে মিলানো।

#### 1. Problem
`f(x) = x²` minimize করো। শুরু x₀ = 4, learning rate η = 0.1।
Minimum x* = 0, f(0) = 0।

#### 2. যা লাগবে (3 লাইন)
- Function: f(x) = x²
- Derivative (slope): f′(x) = 2x
- Update rule: **x_new = x_old − η · f′(x_old) = x_old − 0.1·(2·x_old) = 0.8 · x_old**

#### 3. ধাপে ধাপে (PNG-র Step-by-step)

| Iteration | x_old | f′(x_old) = 2x | x_new = x_old − 0.1·f′ |
|---|---|---|---|
| 0 | 4 | 2(4) = 8 | 4 − (0.1)(8) = **3.2** |
| 1 | 3.2 | 2(3.2) = 6.4 | 3.2 − (0.1)(6.4) = **2.56** |
| 2 | 2.56 | 2(2.56) = 5.12 | 2.56 − (0.1)(5.12) = **2.048** |
| 3 | 2.048 | 2(2.048) = 4.096 | 2.048 − (0.1)(4.096) = **1.6384** |

#### 4. Iteration table (সঠিক মান)

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

#### 5. Shortcut সূত্র (exam-এ সময় বাঁচায়)
- **xₜ = 4 · (0.8)ᵗ** (প্রতি ধাপে 0.8 গুণ)
- **f(xₜ) = 16 · (0.64)ᵗ** (প্রতি ধাপে 0.64 গুণ)
- **f′(xₜ) = 8 · (0.8)ᵗ**
- যেমন t=5: x₅ = 4·0.8⁵ = 4·0.32768 = 1.3107 ✓; f(x₅) = 1.3107² = 1.7180 ✓

#### 6. Variation — প্রশ্নে সংখ্যা বদলে আসতে পারে

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

#### 7. Graph (PNG-র নিচের অংশ)
- x-axis −4…4, y-axis f(x): 0, 1, 4, 8, 12, 16
- Curve f(x)=x² (U-shape); minimum (0,0) লেখো: "Minimum at x = 0"
- Red dot: (4,16), (3.2,10.24), (2.56,6.5536), (2.048,4.1943), (1.6384,2.6844)
- x-axis-এ লাল তীর **বাম দিকে** ("Gradient Descent moves LEFT toward 0")
- ধাপ ক্রমশ ছোট (slope ছোট হচ্ছে)

#### 8. কী বলবে (PNG-র "What is happening?")
- x=4 তে slope = 8 (positive) → function বাড়ছে
- তাই **বাম দিকে** (negative direction) যাই f কমাতে
- 0-এর কাছে গেলে slope ছোট → update ছোট → x→0
- Minimum value f(0)=0

#### 9. (Generated) Linear regression-এ GD — একটা ছোট উদাহরণ
> PDF 1 p5-এ rule আছে: wⱼ ← wⱼ − η ∂J/∂wⱼ, b ← b − η ∂J/∂b। নিচের সংখ্যা আমি বানিয়েছি (sir-এর question না)।

ŷ = wx + b; একটা sample x=2, y=5; শুরু w=0, b=0; η=0.1; loss L=½(ŷ−y)²
- ŷ = 0 → L = ½(0−5)² = 12.5
- ∂L/∂w = (ŷ−y)x = (−5)(2) = −10; ∂L/∂b = ŷ−y = −5
- w_new = 0 − 0.1(−10) = **1.0**; b_new = 0 − 0.1(−5) = **0.5**
- নতুন ŷ = 1.0·2 + 0.5 = 2.5 → L = ½(2.5−5)² = **3.125** (12.5 থেকে কমেছে)

---

# PART 7 — Graph table

| Graph | Key points | আকৃতি/বৈশিষ্ট্য | Syllabus | কোথায় |
|---|---|---|---|---|
| **BCE দুই curve** ($y=1$: $-\ln p$, $y=0$: $-\ln(1-p)$) | x: $p = 0.1\ldots1$; y: loss 1, 2, 3; $y=1$: $p=0.1\to2.3026$, $0.5\to0.6931$, $0.9\to0.1054$ | $y=1$ নামে, $y=0$ ওঠে, ~$p=0.5$-এ cross; confident wrong-এ loss বড় | B4 | p4 Figure 1 |
| **XOR 4 point** | $(0,0)=0, (0,1)=1, (1,0)=1, (1,1)=0$ | কর্ণ বরাবর class বদলায়; একটা রেখা আলাদা করে না; দুই symbol (0 = লাল, 1 = নীল) | B2 | p13 Figure 2 |
| **AND 4 point** | শুধু $(1,1)=1$ | linearly separable | B2 | p13 table |
| **OR 4 point** | শুধু $(0,0)=0$ | linearly separable | B2 | p13 table |
| **ReLU**, $x\in[-4,4]$ | $(-4,0),(-2,0),(0,0),(1,1),(2,2),(4,4)$ | $x<0$ flat 0, $x\ge0$ $y=x$ | B7 | p16 Figure 3 |
| **ReLU′** | $x<0\to0$; $x>0\to1$; $x=0$ convention 0 | দুই ধাপ; $z=0$-তে jump | B7 | p17 (সূত্র), sir-এর sketch |
| **Sigmoid** | $(-2,0.1192),(0,0.5),(1,0.7311),(2,0.8808)$ | S-curve 0–1, $z=0$-তে 0.5 | B6 | p23 table |
| Pipeline diagram | $x\to z=wx+b\to\sigma\to L\to\nabla L\to$ SGD | block diagram | B5 | p7 Figure 2 |
| Network diagram | 2–2–3 MLP, edge-এ initial weights | nodes ও edges | B8 | p38 শেষে |

---

# PART 8 — Syllabus match ও যাচাই

## Syllabus match

| Syllabus | এই PDF-এর section / page |
|---|---|
| A5 Activation (sigmoid, softmax, ReLU) | §18, 19, 25, 26 (p15–17, 23–27) |
| B1 Neuron ও Feedforward | §11–14 (p9–12) |
| B2 XOR | §15–17 (p12–15) |
| B3 Entropy, CE, KL | §1–5 (p1–3) |
| B4 Logistic regression ও BCE | §6, 8–10, 23–24 (p4–8, 21–24) |
| B5 SGD ও Gradient | §9–10, 22 (p6–8, 19–21) |
| B6 Output units (sigmoid/softmax) | §25 (p22–25) |
| B7 Hidden units ও ReLU | §19, 26 (p16–17, 26–27) |
| B8 Architecture | §29 (p29–30) |
| B9 Universal Approximation | §30 (p30–31) |
| B10 Chain rule, Jacobian, Backprop | §31–33 (p31–38) |

## সংখ্যা-যাচাই (computer দিয়ে)
- $H(P) = 0.6109$, $H(P,Q) = 0.6325$, $D_{KL} = 0.0216$, $0.6109 + 0.0216 = 0.6325$ ✓
- $-\ln 0.70 = 0.3567$, $-\ln 0.95 = 0.0513$, $-\ln 0.80 = 0.2231$, $-\ln 0.10 = 2.3026$ ✓
- Logistic SGD: gradients $-1, -0.5$; $w = 0.10$, $b = 0.05$; $p_{new} = 0.5622$; $L = 0.5759$ ✓
- $\sigma(1) = 0.7311$; $-\ln(0.7311) = 0.3133$; update $w_1 = 0.7538$, $w_2 = 0.4269$, $b = -0.7731$, $z = 1.1614$ ✓
- Softmax $[0,2,1] \to [0.0900, 0.6652, 0.2447]$; $L = 0.4076$; Jacobian সব 9 entry ✓
- 2–2–3 MLP: $\mathbf{z}^{(1)}$, $\mathbf{h}$, $\mathbf{z}^{(2)}$, $\nabla\mathbf{h}$, $\nabla W^{(1)}$, $\nabla W^{(2)}$, updated $W/b$, $\mathbf{p}_{new}$, $L_{new} = 0.069793$ সব ✓ (PDF-এর সাথে হুবহু মিলেছে)

**ছোট rounding পার্থক্য (ভুল না):** $p_{new}$ (§25.1) PDF 0.7615, exact 0.7616; $L_{new}$ PDF 0.2725, exact 0.2724। BCE $p = 0.9$: exact 0.1054 (অন্য bank-এ 0.1053)।

**Notation নোট:** কোথাও $W^\top x$ (column-vector), কোথাও $x^\top W$ (row-vector); দুটো সমতুল্য। **সংখ্যা বা ছাপার কোনো ভুল পাইনি।**
