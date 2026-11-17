# PDF 1 — Linear Regression, Activation Function ও Forward/Back Propagation

> **Source:** `merged_L2_GD-LR-B-W-MSE-ActF-FB Prop.pdf` (24 page) · লেখক: Refai Arafat Rossi · October 2026
> **এই file-এর উদ্দেশ্য:** PDF-এর প্রতিটা page-এর প্রতিটা point এখানে আছে। এই file পড়লে PDF আলাদা করে পড়ার দরকার নেই।
> **Syllabus tag** (A1, A2 …) = `QUIZ1_Syllabus.md`-এর topic।
> সব সংখ্যা computer দিয়ে আবার হিসাব করে মিলানো।

---

## 0. PDF-এর গঠন (কোন page-এ কী)

| Page | কী আছে | Syllabus |
|---|---|---|
| p1–6 | **Deck 1:** Linear Regression (Feature, Weight, Bias, Residual, MSE, GD rule) | A1–A4 |
| p7–12 | **Deck 1-এর দ্বিতীয় copy** (হুবহু একই content, শুধু page ভাগ আলাদা) | A1–A4 |
| p13–19 | **Deck 2:** Activation Function ও Nonlinear Learning (ReLU, Sigmoid, Softmax, Bias–Variance, numerical example) | A5, A6, A7 |
| p20–24 | **Deck 3:** Forward ও Back Propagation (Output-layer parameter v₁, v₂, c) | A7 |

> ⚠️ **p7–12 = p1–6-এর repeat।** নিচে একবারই লেখা হয়েছে।
> ⚠️ **Forward/Backprop-এর numerical math (Part 2-এর §2.9–2.11 ও Part 3) notice অনুযায়ী exam-এ আসবে না।** শুধু concept। তবু বোঝার জন্য সব ধাপ রাখা আছে।

---

# PART 1 — Linear Regression: Features, Weights, Bias ও MSE (p1–6)

## 1. Problem: Deep Learning Model-এর Training Time predict করা `[A2]`

> **Source:** p1 · Chapter 5.1.4 (Goodfellow, *Deep Learning*) · Master's Level Lecture Deck

**PDF-এর statement:**
> "Suppose we want to estimate how many minutes a model will take to train based on two observed features."

**বাংলা অর্থ:** ধরো, একটা Deep Learning model train হতে কত মিনিট লাগবে সেটা আমরা অনুমান করতে চাই। এর জন্য দুটো observed feature আছে।

### Given Features

| Symbol | Meaning (PDF) | বাংলা |
|---|---|---|
| $x_1$ | Number of training epochs | কত epoch ধরে train হবে |
| $x_2$ | Batch size measured in units of 16 samples | batch size, এক unit = 16 sample |

উদাহরণ: batch size 64 sample হলে $x_2 = 64/16 = 4$।

### Model Equation

PDF: "We decide to model the relationship using a **Linear Regression Model**":

$$\hat y = w_1x_1 + w_2x_2 + b$$

| Symbol | Meaning (PDF) | বাংলা |
|---|---|---|
| $\hat y$ | predicted training time (minutes) | অনুমান করা training time |
| $w_1, w_2$ | weights | feature-এর weight |
| $b$ | bias | অতিরিক্ত যোগ হওয়া parameter |

**বাংলা অর্থ:** Model প্রতিটা feature-কে তার weight দিয়ে গুণ করে, সব যোগ করে, শেষে bias যোগ করে।

### Learned Model Example

PDF: "Suppose our algorithm has learned parameters $w_1 = 2,\ w_2 = 3,\ b = 5$"

General equation-এ বসালে:

$$\boxed{\hat y = 2x_1 + 3x_2 + 5}$$

### এখানে কী শিখলে?
- Linear regression = feature × weight-এর যোগফল + bias।
- Training-এর পর $w$ আর $b$-এর মান ঠিক হয়ে যায় (এখানে 2, 3, 5)।

---

## 2. Machine Learning Task কী? `[A1]`

> **Source:** p1–2

**PDF-এর definition:**
> "A machine learning task specifies what the model is supposed to do."

**বাংলা অর্থ:** Task মানে model-এর কী কাজ করার কথা সেটা ঠিক করা।

এই problem-এ PDF বলছে: "the task is mapping inputs to continuous real values":

$$\boxed{x \longrightarrow \hat y \in \mathbb{R}}$$

($\mathbb{R}$ = বাস্তব সংখ্যার সেট)

### 2.1 Regression Task ($\hat y \in \mathbb{R}$)
PDF: "Output is a **continuous variable**"

উদাহরণ (PDF): Model training time (minutes) · Housing prices ($) · GPU operating temperature (°C)

### 2.2 Classification Task ($\hat y \in \{0, 1, \ldots\}$)
PDF: "Output is a **discrete categorical label**"

উদাহরণ (PDF): Image identification (Cat vs. Dog) · Medical diagnosis (Benign vs. Malignant)

### তুলনা

| | Regression | Classification |
|---|---|---|
| Output | continuous number | discrete category/label |
| উদাহরণ | training time, price, temperature | Cat/Dog, Benign/Malignant |

**এই problem কোন task?** → **Regression**, কারণ model training time (minutes) predict করে, যা continuous real value।

### Exam-ready Q&A
**Q. Regression ও Classification-এর পার্থক্য কী?**
A. Regression continuous numerical value predict করে (যেমন training time)। Classification discrete class label predict করে (যেমন benign বনাম malicious)।

**Q. Problem 1 কেন Regression?**
A. কারণ output training time (minutes), যা continuous real value।

---

## 3. Feature ও Target `[A2]`

> **Source:** p2 ("3 & 4. Features and Targets")

| Term | PDF definition | বাংলা |
|---|---|---|
| **Feature ($x$)** | An input variable/attribute passed to the model to aid prediction | model-এ যে input দেওয়া হয় |
| **Target ($y$)** | The true ground-truth value we aim to predict | আসল মান, যেটা predict করতে চাই |

এই problem-এ: $x_1$ = number of epochs, $x_2$ = batch-size units; $y$ = actual observed training time (minutes)।

### Example Instance (PDF)
10 epoch, 4 batch unit, ground truth $y = 37$ minutes:

$$\hat y = 2(10) + 3(4) + 5 = 20 + 12 + 5 = 37$$

Error $= y - \hat y = 37 - 37 = 0$ → **perfect prediction**

---

## 4. Feature Vector `[A2]`

> **Source:** p2 ("5. What Is a Feature Vector?")

**PDF:** "Instead of handling variables individually, we package inputs into a **feature vector** $\mathbf{x}$"

$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 4 \end{bmatrix}$$

General $n$-dimensional feature vector: $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$

**PDF:** "Each sample in a dataset is represented mathematically as a point in $n$-dimensional vector space."

**বাংলা অর্থ:** প্রতিটা sample-এর সব feature একটা vector-এ রাখা হয়; প্রতিটা sample $n$-মাত্রার space-এর একটা বিন্দু।

---

## 5. Weight-এর মানে ও Feature Scale `[A2]`

> **Source:** p2–3 ("6 & 7. Weights and Feature Interpretation")

Model: $\hat y = 2x_1 + 3x_2 + 5$ ($w_1 = 2,\ w_2 = 3$)

**PDF:** "A weight $w_j$ represents the expected change in output $\hat y$ per unit change in $x_j$, holding all other features fixed."

| Weight | মানে |
|---|---|
| $w_1 = 2$ | +1 epoch → predicted time **+2 minutes** |
| $w_2 = 3$ | +1 batch-size unit → predicted time **+3 minutes** |

### ⚠️ Important Nuance: Weight Magnitude vs. Feature Scale
**PDF:** "A larger weight does NOT automatically imply a more important feature! Scale matters (e.g., $x_1$ = age in years vs. $x_2$ = income in dollars). Feature normalization is required before comparing weight magnitudes directly."

**বাংলা অর্থ:** বড় weight মানেই বেশি গুরুত্বপূর্ণ feature না। Feature-এর scale আলাদা হলে weight তুলনা করা যায় না; আগে normalize করতে হয়।

### Exam-ready Q&A
**Q. Weight কী বোঝায়?** A. অন্য feature fixed রেখে একটা feature এক unit বাড়লে prediction কত বদলায়।
**Q. বড় weight কি বেশি important feature?** A. না, scale-এর উপর নির্ভর করে; তুলনার আগে normalization লাগে।

---

## 6. Parameters ও Weights `[A2]`

> **Source:** p3 ("8 & 9. Parameters vs. Weights")

**Model Parameters ($\theta$):** "The set of all learnable values adjusted by training algorithms"

$$\theta = \{w_1, w_2, \ldots, w_n, b\}$$

**Structural Decomposition (PDF):**
- **Weights ($w_j$):** parameters multiplying features or activations
- **Bias ($b$):** additive parameter shifting output independent of inputs

PDF: "Weights and biases are specific subsets of model parameters $\theta$."

---

## 7. Vector Notation ও Neuron View `[A2]`

> **Source:** p3 ("10. Vector Notation", "11 & 12. Linear Regression as an Artificial Neuron")

### 7.1 Vector notation
$\mathbf{w} = [w_1, w_2]^T$, $\mathbf{x} = [x_1, x_2]^T$

$$\mathbf{w}^T\mathbf{x} = w_1x_1 + w_2x_2$$

$$\boxed{\hat y = \mathbf{w}^T\mathbf{x} + b}$$

PDF: "This linear combination is the exact foundational building block used in deep neural network layers."

### 7.2 Linear Regression = একটা Neuron
| | Formula |
|---|---|
| Linear Regression | $\hat y = \mathbf{w}^T\mathbf{x} + b$ |
| Artificial Neuron | $z = \mathbf{w}^T\mathbf{x} + b,\quad a = f(z)$ |

**PDF:** "Linear regression is simply a single neuron with an **identity activation function** ($f(z) = z$)."

Diagram (PDF-এ TikZ code ছাপা, figure নেই): $x_1, x_2$ → weight $w_1, w_2$ দিয়ে weighted sum $\sum$ → সাথে bias $+b$ → output $\hat y$।

### Exam-ready Q&A
**Q. Linear regression আর artificial neuron-এর সম্পর্ক কী?**
A. Linear regression = একটা neuron যার activation identity ($f(z) = z$)।

---

## 8. Dataset Evaluation ও MSE `[A3]`

> **Source:** p4 ("13–17. Dataset Evaluation Example", "18–21. MSE")

PDF: Model $\hat y = 2x_1 + 3x_2 + 5$ চারটা experiment-এ:

| Exp | Epochs $x_1$ | Batch $x_2$ | Actual $y$ | Predicted $\hat y$ | Error $(y - \hat y)$ | Squared Error |
|---|---|---|---|---|---|---|
| A | 2 | 2 | 15 | $2(2)+3(2)+5 = 15$ | 0 | 0 |
| B | 4 | 3 | 22 | $2(4)+3(3)+5 = 22$ | 0 | 0 |
| C | 6 | 4 | 29 | $2(6)+3(4)+5 = 29$ | 0 | 0 |
| D | 8 | 5 | 35 | $2(8)+3(5)+5 = 36$ | **−1** | **1** |

PDF: "Exp D exhibits a prediction discrepancy ($\hat y = 36$ vs. $y = 35$). We need a quantitative metric to measure overall dataset error."

### Mean Squared Error (MSE)

$$MSE = \frac{1}{m}\sum_{i=1}^{m}\left(\hat y^{(i)} - y^{(i)}\right)^2$$

**MSE Calculation (PDF):**

$$MSE = \frac{0 + 0 + 0 + 1}{4} = \boxed{0.25}$$

PDF: "An MSE of 0 represents perfect prediction across all samples."

### কেন residual square করি? (PDF)
- Positive আর negative error cancel হতে দেয় না ($+2 + (-2) = 0$)
- বড় deviation-কে অনেক বেশি শাস্তি দেয় ($1^2 = 1$ বনাম $5^2 = 25$)

### Exam-ready Q&A
**Q. MSE-তে square কেন?** A. Sign cancel হয় না, আর বড় error বেশি penalty পায়।
**Q. উপরের dataset-এর MSE কত?** A. $(0+0+0+1)/4 = 0.25$।

---

## 9. Residual ও Geometric Meaning `[A3]`

> **Source:** p4 ("25 & 26. Residuals and Geometric Interpretation")

**Residual Definition (PDF):** $r^{(i)}$ = sample $i$-এর actual value $y^{(i)}$ আর predicted value $\hat y^{(i)}$-এর **vertical distance**:

$$\boxed{r^{(i)} = y^{(i)} - \hat y^{(i)}}$$

| Residual | মানে |
|---|---|
| $r > 0$ | model কম predict করেছে (point রেখার উপরে) |
| $r < 0$ | model বেশি predict করেছে (point রেখার নিচে) |

**Key Concept (PDF):** "Linear regression finds parameters $w, b$ that minimize the average sum of these squared vertical distances across all data points."

Figure (PDF-এ code ছাপা): রেখা $\hat y = wx + b$; একটা point $(x^{(i)}, y^{(i)})$; দুটোর মাঝে লাল dashed vertical রেখা = $r^{(i)}$।

---

## 10. Bias কেন লাগে `[A2]`

> **Source:** p4 ("27–30. Geometric Meaning and Necessity of Bias") + p5

PDF প্রশ্ন: "Why do we need an explicit bias term $b$?"

| | Equation | কী হয় |
|---|---|---|
| **Without bias ($b = 0$)** | $\hat y = wx$ | রেখা **(0,0) দিয়ে যেতে বাধ্য**। $x=0$-তে target $y=5$ হলে model পুরোপুরি ব্যর্থ। |
| **With bias ($b \neq 0$)** | $\hat y = wx + b$ | affine transformation; রেখা/hyperplane উপরে-নিচে shift করে। |

**Geometric (PDF, p5):**
- **1D Line** $\hat y = wx + b$: $w$ = slope, $b$ = y-intercept
- **2D Plane** $\hat y = w_1x_1 + w_2x_2 + b$: $w_1, w_2$ = orientation; $b$ = plane-এর elevation (উচ্চতা)

### Exam-ready Q&A
**Q. Bias কেন দরকার?** A. Bias ছাড়া $\hat y = wx$ origin দিয়ে যেতে বাধ্য; bias line/plane-কে shift করে non-zero intercept দেয়।

---

## 11. Terminology Summary Table `[A2, A3]`

> **Source:** p5 ("35. Terminology Summary Table")

| Term | Meaning in Linear Regression Context |
|---|---|
| Task | Predict training runtime given model hyperparameters |
| Feature | Individual input attribute ($x_1$ = epochs, $x_2$ = batch units) |
| Feature Vector ($\mathbf{x}$) | Vector packaging all input variables for a single sample |
| Target ($y$) | Ground-truth true real-world observation |
| Prediction ($\hat y$) | Output generated by model $\mathbf{w}^T\mathbf{x} + b$ |
| Weight ($w$) | Multiplicative parameters defining feature contributions |
| Bias ($b$) | Additive parameter enabling affine shift of predictions |
| Parameters ($\theta$) | Set of all learnable variables ($\theta = \{w, b\}$) |
| Residual ($r$) | Raw prediction error ($y - \hat y$) |
| MSE | Mean Squared Error measuring performance over dataset |

---

## 12. Parameter শেখা = Optimization (Gradient Descent) `[A4]`

> **Source:** p5 ("32 & 33. Framing Parameter Learning via Optimization")

**PDF:** "We don't know ideal weights $\mathbf{w}$ and bias $b$ beforehand. We start with **random parameter initializations** and optimize via **Gradient Descent**."

**Loss Function to Minimize:**

$$J(w_1, w_2, b) = \frac{1}{m}\sum_{i=1}^{m}\left(\left(w_1x_1^{(i)} + w_2x_2^{(i)} + b\right) - y^{(i)}\right)^2$$

**Gradient Updates:**

$$\boxed{w_j \leftarrow w_j - \eta\frac{\partial J}{\partial w_j}, \qquad b \leftarrow b - \eta\frac{\partial J}{\partial b}}$$

**Flow (PDF):** Input $x$ → Prediction $\hat y$ → MSE Loss $J$ → Gradients $\nabla J$ → Parameter Updates

**Optimization Goal (p6):** $w^*, b^* = \arg\min_{w,b} MSE(w, b)$

> GD-র নিয়ম, step ও সংখ্যার হিসাব Part 4-এ (Gradient Descent math)।

---

## 13. Student Exercises `[A2, A3]`

> **Source:** p5 ("36 & 37. Student Classroom Exercises")

Model: $\hat y = 3x_1 + 2x_2 + 4$

**Exercise 1 (Zero Error):** $\mathbf{x} = [5, 3]^T$, actual $y = 25$.

$$\hat y = 3(5) + 2(3) + 4 = 15 + 6 + 4 = 25,\quad e = 25 - 25 = 0,\quad e^2 = 0$$

**Exercise 2 (Non-Zero Error):** $\mathbf{x} = [6, 4]^T$, actual $y = 32$.

$$\hat y = 3(6) + 2(4) + 4 = 18 + 8 + 4 = 30,\quad e = 32 - 30 = 2,\quad e^2 = 4$$

---

## 14. Core Equations ও Final Summary `[A2–A4]`

> **Source:** p5–6 ("38. Core Equations to Remember", "39. Final Summary")

**Core Equations (PDF):**
1. **Linear Regression Prediction:** $\hat y = \mathbf{w}^T\mathbf{x} + b$ (Prediction = Weights × Features + Bias)
2. **MSE Objective Function:** $MSE = \frac{1}{m}\sum_{i=1}^{m}(\hat y^{(i)} - y^{(i)})^2$
3. **Optimization Goal:** $w^*, b^* = \arg\min_{w,b} MSE(w, b)$

**Final Summary: Linear Model → Deep Neural Network (Progression of Model Complexity):**
1. **Linear Regression (Single Identity Neuron):** $\hat y = \mathbf{w}^T\mathbf{x} + b$
2. **Single Non-Linear Neuron:** $a = f(\mathbf{w}^T\mathbf{x} + b)$
3. **Multi-Layer Deep Neural Network:**
   $h^{(1)} = f_1(W^{(1)}x + b^{(1)})$, $h^{(2)} = f_2(W^{(2)}h^{(1)} + b^{(2)})$, …, $\hat y = f_L(W^{(L)}h^{(L-1)} + b^{(L)})$

**Final Conceptual Takeaway (PDF):** "Deep networks are constructed by stacking the fundamental linear regression operation ($\mathbf{w}^T\mathbf{x} + b$) across multiple layers interleaved with non-linear activation functions."

---

# PART 2 — Activation Functions ও Nonlinear Learning (p13–19)

> **Deck title:** "Nonlinear Learning From Activation Functions to Backpropagation" · Chapter 6: Nonlinear Learning

## 15. কেন Neural Network? (Electricity Demand) `[A2, A5]`

> **Source:** p13 ("1. Problem: Electricity Demand vs. Temperature")

PDF: একজন electricity grid operator প্রতিদিনের power generation plan করছেন।
- **Cold days:** electric heating-এর কারণে demand বাড়ে
- **Hot days:** air conditioning-এর কারণে demand বাড়ে
- **Comfortable days:** moderate temperature-এ demand সবচেয়ে কম

**Mathematical Formulation:**
- Input $x$: comfortable baseline থেকে temperature deviation
- Target $y$: additional electricity demand
- Illustrative ground truth: $y = x^2$

| Temp Deviation ($x$) | −2 | −1 | 0 | 1 | 2 |
|---|---|---|---|---|---|
| Demand ($y = x^2$) | 4 | 1 | 0 | 1 | 4 |

(Graph: **U-shape parabola**, minimum $(0,0)$।)

## 16. Model A, B, C `[A2, A5]`

> **Source:** p13–14 ("2. Why Do We Need a Neural Network?")

| Model | Equation | বৈশিষ্ট্য |
|---|---|---|
| **A: Linear Regression** | $\hat y = wx + b$ | Limitation: শুধু straight line fit করে। $y = x^2$-এর মতো U-shaped curve-এ **পুরোপুরি ব্যর্থ**। |
| **B: Single-Layer NN** | $h = f(wx + b)$ | Non-linear activation $f(\cdot)$ piecewise signal মিলিয়ে curve approximate করে। |
| **C: Deep NN** | $h^{(l)} = f(W^{(l)}h^{(l-1)} + b^{(l)})$ | অনেক stacked layer → hierarchical, জটিল functional representation। |

**Takeaway (PDF):** "A linear model cannot capture parabolic demand. Hidden layers with non-linear activations provide universal approximation capabilities."

## 17. ReLU ও Sigmoid `[A5]`

> **Source:** p14 ("3. Activation Functions: ReLU and Sigmoid")

Neuron: $z = wx + b$, তারপর activation $a = f(z)$।

### Rectified Linear Unit (ReLU)

$$\boxed{ReLU(z) = \max(0, z)}$$

- $ReLU(-3) = 0$
- $ReLU(2.5) = 2.5$
- Hidden layer-এর standard choice (**simple derivative, avoids gradient saturation**)

### Sigmoid Activation

$$\boxed{\sigma(z) = \frac{1}{1 + e^{-z}}}$$

- $\sigma(0) = 0.5$
- $\sigma(2) \approx 0.881$, $\sigma(-2) \approx 0.119$
- Maps $\mathbb{R} \to (0, 1)$; binary classification output-এর standard choice

### Graph: ReLU ও Sigmoid

| | Key points | আকৃতি |
|---|---|---|
| **ReLU** ($z \in [-4,4]$) | $(-4,0), (-2,0), (0,0), (1,1), (2,2), (3,3), (4,4)$ | negative-এ flat $y=0$; positive-এ $y=z$ |
| **ReLU′** ($z \in [-4,4]$) | $z<0 \to 0$; $z>0 \to 1$; $z=0$: convention 0 | দুই flat রেখা, $z=0$-তে jump |
| **Sigmoid** | $(-2, 0.119), (0, 0.5), (2, 0.881)$ | S-curve, 0 আর 1 asymptote |

## 18. Network Architecture (Electricity Demand) `[A7]`

> **Source:** p14–15 ("4. Network Architecture for Electricity Demand")

**1-Hidden-Layer Regression Network (এক input $x$, দুই hidden unit):**
- Hidden 1: $z_1 = w_1x + b_1,\quad h_1 = ReLU(z_1)$
- Hidden 2: $z_2 = w_2x + b_2,\quad h_2 = ReLU(z_2)$
- Output: $\hat y = v_1h_1 + v_2h_2 + c$

**Vector/Matrix form:** $z^{(1)} = W^{(1)}x + b^{(1)}$, $h^{(1)} = ReLU(z^{(1)})$, $\hat y = W^{(2)}h^{(1)} + b^{(2)}$

Diagram (code ছাপা): $x$ → দুটো hidden node $h_1, h_2$ (edge-এ $w_1,b_1$ ও $w_2,b_2$) → output $\hat y$ (edge-এ $v_1$ ও $v_2, c$)।

---

## 19. ⚠️ Numerical Forward Pass → Loss → Backprop → Update (p15–17)

> **Source:** p15–17 ("5 & 6. Part B — Numerical Forward Pass Example" … "10. Verifying Improvement")
> **Notice অনুযায়ী এই math exam-এ আসবে না।** Concept ও ধাপ বোঝার জন্য রাখা।

**Training Instance:** $x = 1$, True target $y = 1$
**Initial Parameters:** $w_1 = 1,\ b_1 = 0$ | $w_2 = 0.5,\ b_2 = 0.5$ | $v_1 = 0.2,\ v_2 = 0.2,\ c = 0$

### 19.1 Forward pass
| ধাপ | হিসাব | ফল |
|---|---|---|
| Hidden Neuron 1 | $z_1 = (1)(1) + 0 = 1$, $h_1 = ReLU(1)$ | $h_1 = 1$ |
| Hidden Neuron 2 | $z_2 = (0.5)(1) + 0.5 = 1$, $h_2 = ReLU(1)$ | $h_2 = 1$ |
| Output | $\hat y = (0.2)(1) + (0.2)(1) + 0$ | $\hat y = 0.4$ |
| Prediction error | $e = \hat y - y = 0.4 - 1.0$ | $-0.6$ (underpredict) |

### 19.2 Loss (half-squared error, single sample)
$$L = \tfrac{1}{2}(\hat y - y)^2 = \tfrac{1}{2}(0.4 - 1.0)^2 = \tfrac{1}{2}(0.36) = \boxed{0.18}$$

General MSE: $MSE = \frac{1}{m}\sum_{i=1}^m(\hat y_i - y_i)^2$। PDF: "The factor of $\frac12$ cancels out neatly during derivative operations."

### 19.3 Backpropagation (chain rule) — p16
PDF: "Backpropagation propagates error backward from output to input to calculate $\frac{\partial L}{\partial\theta}$."

- **Step 1** (output): $\frac{\partial L}{\partial \hat y} = \hat y - y = 0.4 - 1.0 = -0.6$
- **Step 2** (output weights/bias):
  - $\frac{\partial L}{\partial v_1} = \frac{\partial L}{\partial \hat y}\frac{\partial \hat y}{\partial v_1} = (-0.6)(h_1) = -0.6$
  - $\frac{\partial L}{\partial v_2} = (-0.6)(h_2) = -0.6$, $\quad\frac{\partial L}{\partial c} = (-0.6)(1) = -0.6$
- **Step 3** (hidden layer $w_1, b_1$):
  - $\frac{\partial L}{\partial h_1} = \frac{\partial L}{\partial \hat y}v_1 = (-0.6)(0.2) = -0.12$
  - $\frac{\partial L}{\partial z_1} = \frac{\partial L}{\partial h_1}\cdot ReLU'(1) = (-0.12)(1) = -0.12$
  - $\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial z_1}x = (-0.12)(1) = -0.12$, $\quad\frac{\partial L}{\partial b_1} = -0.12$

### 19.4 Gradient Descent update ($\eta = 0.1$, $\theta_{new} = \theta_{old} - \eta\frac{\partial L}{\partial \theta}$)
| Layer | Update | নতুন মান |
|---|---|---|
| Hidden | $w_1 = 1.0 - (0.1)(-0.12)$ | **1.012** |
| Hidden | $w_2 = 0.5 - (0.1)(-0.12)$ | **0.512** |
| Hidden | $b_1 = 0.0 - (0.1)(-0.12)$ | **0.012** |
| Hidden | $b_2 = 0.5 - (0.1)(-0.12)$ | **0.512** |
| Output | $v_1 = 0.2 - (0.1)(-0.6)$ | **0.26** |
| Output | $v_2 = 0.2 - (0.1)(-0.6)$ | **0.26** |
| Output | $c = 0.0 - (0.1)(-0.6)$ | **0.06** |

### 19.5 Verifying Improvement (Forward Pass 2) — p16–17
- $z_1 = (1.012)(1) + 0.012 = 1.024$, $h_1 = 1.024$
- $z_2 = (0.512)(1) + 0.512 = 1.024$, $h_2 = 1.024$
- New prediction $\hat y_{new} = 0.26(1.024) + 0.26(1.024) + 0.06 = \mathbf{0.5925}$
- New loss $L_{new} = \frac12(0.5925 - 1.0)^2 = \mathbf{0.0830}$

| Quantity | Before Update | After Update | Improvement |
|---|---|---|---|
| Prediction $\hat y$ | 0.4000 | 0.5925 | Closer to target 1.0 |
| Half-Squared Loss $L$ | 0.1800 | 0.0830 | **Reduced by 53.9%** |

---

## 20. Capacity ও Bias–Variance Trade-off `[A6]`

> **Source:** p17 ("11 & 12. Part C — Bias–Variance Trade-off")

| | Capacity | $E_{train}$ / $E_{test}$ | ফল |
|---|---|---|---|
| **Underfitting** | Model capacity খুব কম | $E_{train}$ High, $E_{test}$ High | High systematic bias |
| **Optimal Capacity** | Balanced complexity | $E_{train}$ Low, $E_{test}$ Low | Good generalization |
| **Overfitting** | Capacity অতিরিক্ত বেশি | $E_{train} \approx 0$, $E_{test}$ High | High variance |

**Expected Generalization Error Decomposition:**

$$\text{Expected Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$$

### Exam-ready Q&A
**Q. Underfit ও overfit কী?** A. Underfit: capacity কম, train ও test দুটোতেই error বেশি। Overfit: capacity বেশি, train error ≈ 0 কিন্তু test error বেশি।

---

## 21. Classification: Sigmoid ও Binary Cross-Entropy `[A5, B4]`

> **Source:** p17 ("13. Part D — Classification: Sigmoid & Binary Cross-Entropy")

Task regression থেকে **binary classification** ($y \in \{0, 1\}$)-এ।

**Step 1 — Logit → Probability (Sigmoid):**
$$p = \sigma(z) = \frac{1}{1 + e^{-z}},\quad z = 2.0:\ p = \frac{1}{1 + e^{-2}} \approx 0.881\ (88.1\%\text{ prob of Class 1})$$

**Step 2 — Binary Cross-Entropy (BCE):**
$$L_{BCE} = -[y\log p + (1-y)\log(1-p)]$$
- True label $y = 1$: $L = -\log(p)$
- $p = 0.881$: $L = -\log(0.881) \approx \mathbf{0.127}$ (সঠিক ও confident prediction-এ কম loss)

(PDF-এ "log" লেখা; এখানে natural log।)

---

## 22. Task অনুযায়ী Output Layer `[A5]`

> **Source:** p18 (table + "15. Summary: Task vs. Output Layer Selection")

| Task Type | Output Activation | Output Range | Loss Function |
|---|---|---|---|
| Continuous Regression | Linear / Identity ($f(z) = z$) | $(-\infty, \infty)$ | Mean Squared Error (MSE) |
| Binary Classification | Sigmoid ($\sigma(z)$) | $(0, 1)$ | Binary Cross-Entropy (BCE) |
| Multiclass Classification | Softmax ($p_i$) | $[0, 1]$, $\sum p_i = 1$ | Categorical Cross-Entropy |

**Golden Rule (PDF):** "Hidden layers use non-linear activations (e.g., ReLU) to learn representations; the output activation function is dictated strictly by the task type."

---

## 23. Softmax ও Categorical Cross-Entropy `[A5]`

> **Source:** p18 ("14. Multiclass Classification: Softmax Categorical Cross-Entropy")

K-class classification (PDF উদাহরণ: MRI tumor diagnosis — Glioma, Meningioma, Pituitary)।

**1. Softmax Activation Function:** raw logits $\mathbf{z} = [z_1, \ldots, z_K]^T$ → probability:

$$\boxed{p_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}}$$

**Numerical Example:** logits $\mathbf{z} = [2.0, 1.0, 0.0]^T$
- $e^{2.0} \approx 7.389,\ e^{1.0} \approx 2.718,\ e^{0.0} = 1.0$; Sum $= 11.107$
- $\mathbf{p} = [\frac{7.389}{11.107}, \frac{2.718}{11.107}, \frac{1.0}{11.107}] = \boxed{[0.665,\ 0.245,\ 0.090]}$

**2. Categorical Cross-Entropy Loss:** True class = category 2 ($\mathbf{y} = [0,1,0]^T$):

$$L_{CCE} = -\log(p_2) = -\log(0.245) \approx \boxed{1.407}$$

---

## 24. Core Equations ও End-to-End Loop `[A5, A7]`

> **Source:** p18–19 ("16. Core Equations Cheat Sheet", "17. Final Picture")

1. Neuron pre-activation: $z = \mathbf{w}^T\mathbf{x} + b$
2. ReLU: $ReLU(z) = \max(0, z)$
3. Sigmoid: $\sigma(z) = \frac{1}{1 + e^{-z}}$
4. Softmax: $p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$
5. MSE: $MSE = \frac{1}{m}\sum(\hat y_i - y_i)^2$
6. Gradient Descent update: $\theta \leftarrow \theta - \eta\nabla_\theta L$

**The End-to-End Learning Loop (PDF):**

Input $x$ → **Forward Pass** ($\hat y$) → **Loss** $L$ → **Backprop** ($\nabla_\theta L$) → **Gradient Update** ($\theta$)

**Final Summary Takeaway (PDF):**
- **Forward Pass:** generates model predictions
- **Loss Function:** ground-truth target-এর সাথে ফারাক মাপে
- **Backpropagation:** calculus chain rule দিয়ে প্রতিটা parameter-এ error gradient attribute করে
- **Gradient Descent:** loss কমাতে parameter update করে

---

# PART 3 — Forward ও Back Propagation: Output-Layer Parameters (p20–24)

> **Deck title:** "Output Layer Parameters and Backpropagation — Understanding Trainable Weights $v_1, v_2, c$ and Gradient Updates" `[A7]`

## 25. Output-Layer Parameter বোঝা

> **Source:** p20 ("1. Clarifying Output-Layer Parameters")

**⚠️ Core Misconception to Avoid (PDF):** "Output-layer weights $v_1, v_2$ and bias $c$ are **NOT** calculated or derived from input-to-hidden parameters ($w_1, w_2, b_1, b_2$)."

| Layer | Parameters | কাজ |
|---|---|---|
| **Hidden-Layer** | $w_1, w_2$: input-to-hidden weights · $b_1, b_2$: hidden neuron biases | transformation: $x \to h$ |
| **Output-Layer** | $v_1, v_2$: hidden-to-output weights · $c$: output neuron bias | transformation: $h \to \hat y$ |

**Takeaway (PDF):** "$v_1, v_2, c$ are independent, learnable model parameters. They are initialized randomly (or with small values) at the start of training and optimized via backpropagation."

### Exam-ready Q&A
**Q. $v_1, v_2$ কি $w_1, w_2$ থেকে বের করা হয়?** A. না। এরা স্বাধীন learnable parameter; শুরুতে random/ছোট মানে initialize হয়, backprop দিয়ে শেখা হয়।

---

## 26. ⚠️ Numerical Example (p20–24) — exam-এ math আসবে না

> **Source:** p20–23 ("2. Problem Setup" … "8. Step 6: Verifying Updated Output Performance")

### Setup
Simplified feedforward network:
- Input features: $x_1 = 3,\ x_2 = -1$
- Hidden weights: $w_1 = 1,\ w_2 = 2$; Hidden biases: $b_1 = 1,\ b_2 = 1$
- Ground truth target: $y = 1.0$
- $h_1 = ReLU(w_1x_1 + b_1)$, $h_2 = ReLU(w_2x_2 + b_2)$

**Architectural Note (PDF):** "In a fully connected layer with 2 inputs and 2 hidden units, there are normally 4 input-to-hidden weights ($W \in \mathbb{R}^{2\times2}$). Here we use a 1-to-1 connection mapping for step-by-step clarity."

### Step 1 — Hidden-layer outputs
- Neuron 1: $z_1 = (1)(3) + 1 = 4$ → $h_1 = \max(0, 4) = \mathbf{4}$
- Neuron 2: $z_2 = (2)(-1) + 1 = -1$ → $h_2 = \max(0, -1) = \mathbf{0}$ (deactivated)
- Hidden representation: $\mathbf{h} = [4, 0]^T$

### Step 2 — Output parameters কোথায় আসে
Output: $\hat y = v_1h_1 + v_2h_2 + c$। $h_1 = 4,\ h_2 = 0$ বসালে $\hat y = 4v_1 + c$।

Key Observations (PDF):
- $v_1$ active feature ($h_1 = 4$)-কে scale করে
- $v_2$ prediction-এ **0** contribute করে, কারণ $h_2 = 0$ (ReLU deactivated)
- $c$ baseline output shift করে

**Why Initialize Early? (PDF):** "Forward propagation cannot complete without numerical values for $v_1, v_2, c$. We pick initial estimates to start the training loop."

### Step 3 — Forward pass loss ($v_1 = 0.2,\ v_2 = 0.2,\ c = 0.0$)
1. $\hat y = 4(0.2) + 0(0.2) + 0 = \mathbf{0.8}$
2. $e = \hat y - y = 0.8 - 1.0 = -0.2$
3. $L = \frac12(\hat y - y)^2 = \frac12(-0.2)^2 = \frac12(0.04) = \mathbf{0.02}$

### Step 4 — Backprop: output parameter gradient
$$\frac{\partial L}{\partial \hat y} = \hat y - y = 0.8 - 1.0 = -0.2$$

| Gradient | হিসাব | মান |
|---|---|---|
| $\frac{\partial L}{\partial v_1}$ | $(\hat y - y)h_1 = (-0.2)(4)$ | **−0.8** |
| $\frac{\partial L}{\partial v_2}$ | $(\hat y - y)h_2 = (-0.2)(0)$ | **0.0** |
| $\frac{\partial L}{\partial c}$ | $(\hat y - y)(1)$ | **−0.2** |

### Step 5 — Gradient Descent update ($\eta = 0.1$)
- $v_{1,new} = 0.2 - 0.1(-0.8) = 0.2 + 0.08 = \mathbf{0.28}$
- $v_{2,new} = 0.2 - 0.1(0.0) = \mathbf{0.20}$ **(Unchanged!)**
- $c_{new} = 0.0 - 0.1(-0.2) = 0.0 + 0.02 = \mathbf{0.02}$

### Step 6 — Verify
- Hidden activations: $h_1 = 4,\ h_2 = 0$
- $\hat y_{new} = (0.28)(4) + (0.20)(0) + 0.02 = 1.12 + 0 + 0.02 = \mathbf{1.14}$
- Target $y = 1.0$ → $e_{new} = 1.14 - 1.0 = +0.14$
- $L_{new} = \frac12(0.14)^2 = \mathbf{0.0098}$

| Metric | Initial Pass | Updated Pass | Change |
|---|---|---|---|
| Prediction $\hat y$ | 0.8000 | 1.1400 | Moved toward target 1.0 |
| Loss $L$ | 0.0200 | 0.0098 | **Reduced by 51.0%** |

**Insight on Inactive Neurons (PDF):** "$v_2$ receives zero gradient update because its corresponding hidden neuron $h_2 = 0$. Inactive neurons transmit no error information back to their incoming weights."

### Complete Architecture & Data Flow (p23)
Summary equation: $\hat y = v_1 \cdot ReLU(w_1x_1 + b_1) + v_2 \cdot ReLU(w_2x_2 + b_2) + c$

Diagram: $x_1 = 3$ → $h_1 = 4$ (edge: $w_1 = 1, b_1 = 1$); $x_2 = -1$ → $h_2 = 0$ (edge: $w_2 = 2, b_2 = 1$); $h_1 \to \hat y$ ($v_1 = 0.28$), $h_2 \to \hat y$ ($v_2 = 0.20$), dashed bias $c = 0.02 \to \hat y$।

---

## 27. Summary Takeaways for Students `[A7]`

> **Source:** p23–24 ("10. Summary Takeaways for Students")

1. **Parameter Separation:** input-to-hidden parameter ($w_i, b_i$) feature representation ($h_i$) ঠিক করে। output-layer parameter ($v_i, c$) ঠিক করে সেই representation কীভাবে মিশে final prediction ($\hat y$) হবে।
2. **Trainable Nature:** output parameter স্বাধীন learnable quantity, training-এর আগে initialize হয়; input weight থেকে গাণিতিকভাবে derive হয় না।
3. **Gradient Masking by Activations:** neuron-এর activation zero ($h_2 = 0$) হলে তার outgoing weight-এর gradient zero ($\frac{\partial L}{\partial v_2} = 0$) → ওই connection-এর update সাময়িকভাবে থামে।
4. **The Core Learning Loop:** Inputs $x$ → Hidden $h$ → Output $\hat y$ → Loss $L$ → Gradients $\nabla L$ → Updates $\theta_{new}$

### Exam-ready Q&A
**Q. Forward propagation কী calculate করে?** A. Input থেকে hidden হয়ে output পর্যন্ত pre-activation, activation, prediction ও loss।
**Q. Backpropagation কী করে?** A. Chain rule দিয়ে loss থেকে পেছনের দিকে প্রতিটা parameter-এর gradient বের করে।
**Q. Backprop আর GD কি এক?** A. না। Backprop gradient *calculate* করে; GD সেই gradient দিয়ে parameter *update* করে।
**Q. $h_2 = 0$ হলে $v_2$-এর কী হয়?** A. $\partial L/\partial v_2 = (\hat y - y)h_2 = 0$, তাই $v_2$ update হয় না।

---

# PART 4 — Gradient Descent math (PNG problem) `[A4]`

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

# PART 5 — Graph table

> এই PDF-এর figure সব TikZ code ছাপা (render হয়নি): residual (p4), neuron/network diagram (p3, p15, p23)। নিচে এই PDF-এর topic-এ যে graph আসতে পারে:

| Graph | Key points | আকৃতি | Syllabus | কোথায় |
|---|---|---|---|---|
| $f(x) = x^2$, $x \in [-2,2]$ | $(-2,4), (-1,1), (0,0), (1,1), (2,4)$ | U-shape, minimum $(0,0)$, y-axis symmetric | A4 | p13 table; PDF 2 Ex.1 |
| GD on $x^2$ | $x_0 = 4, 3.2, 2.56, 2.048, 1.6384$ ($f = 16, 10.24, 6.5536, 4.1943, 2.6844$) | curve-এর উপর dot, তীর বাম দিকে, ধাপ ছোট | A4 | PNG; PDF 2 Ex.2 |
| Residual | $\hat y = x+1$, observed $(2,2)$, predicted $(2,3)$, $r = -1$ | dashed vertical; point রেখার নিচে → $r$ negative | A3 | p4; PDF 2 Ex.3 |
| Bias effect | $\hat y = 2x$ vs $2x+5$: $(0,0)$ ও $(0,5)$; $(1,2)/(1,7)$; $(2,4)/(2,9)$ | parallel; একটা origin দিয়ে, অন্যটা y-axis কাটে 5-এ | A2 | p4 (concept); ছবি PDF-এ নেই |
| ReLU | $(-4,0),(-2,0),(0,0),(1,1),(2,2),(3,3),(4,4)$ | negative-এ flat 0; positive-এ $y=z$ | A5 | p14; PDF 2 Ex.4 |
| ReLU′ | $z<0 \to 0$; $z>0 \to 1$ | $z=0$-তে jump | A5 | sir-এর sketch |
| Sigmoid | $(-2,0.119),(0,0.5),(2,0.881)$ | S-curve (0,1)-এর মধ্যে | A5 | p14; PDF 2 Ex.5 |
| Softmax bar, logits $[2,1,0]$ | 0.665, 0.245, 0.090 | সবচেয়ে বড় logit-এর bar উঁচু; যোগফল 1 | A5 | p18 (generated bar) |
| BCE $y=1$: $-\ln p$ | $(0.1, 2.3026) \ldots (0.9, 0.1054)$ | নামতে থাকা curve | B4 | PDF 3/4 |

---

# PART 6 — Syllabus match ও যাচাই

## Syllabus match

| Syllabus | এই PDF-এর section / page |
|---|---|
| A1 ML Task | §2 (p1–2) |
| A2 Linear Regression | §1, 3–7, 10–11, 13–14 (p1–6) |
| A3 Residual ও MSE | §8–9, 13 (p4–5) |
| A4 Gradient Descent | §12, Part 4 (p5–6, PNG) |
| A5 Activation (ReLU, Sigmoid, Softmax) | §15–17, 21–24 (p13–14, 17–19) |
| A6 Capacity/Bias–Variance | §20 (p17) |
| A7 Forward/Backprop (concept) | §18–19, 25–27 (p14–16, 20–24) |
| B4 BCE | §21 (p17) |

## সংখ্যা-যাচাই (computer দিয়ে)
- MSE $= 0.25$ ✓ · Exercise 1: $\hat y = 25$ ✓; Exercise 2: $\hat y = 30$, $e^2 = 4$ ✓
- p15 forward: $\hat y = 0.4$, $L = 0.18$ ✓ · p16 updates (1.012, 0.512, 0.012, 0.512, 0.26, 0.26, 0.06) ✓
- p17: $\hat y_{new} = 0.5925$ (exact 0.59248), $L_{new} = 0.0830$ ✓, reduction 53.9% ✓
- BCE $-\log(0.881) = 0.1267 \approx 0.127$ ✓ · softmax $[0.665, 0.245, 0.090]$ ✓; $-\log(0.245) = 1.407$ ✓
- p22–23: $\hat y = 0.8$, $L = 0.02$, $\partial L/\partial v_1 = -0.8$, $v_1 = 0.28$, $\hat y_{new} = 1.14$, $L_{new} = 0.0098$ ✓, reduction 51.0% ✓

**ছাপার সমস্যা (সংখ্যার ভুল না):** TikZ diagram code ও "0.5" উপ-শিরোনামের চিহ্ন text হিসেবে ছাপা (p3, p4, p15, p23)। Deck-এর title "Gradient Descent – Linear regression" হলেও p1–6-এ নতুন GD content নেই (শুধু শেষে GD rule/flow)। BCE-তে "log" = natural log।
