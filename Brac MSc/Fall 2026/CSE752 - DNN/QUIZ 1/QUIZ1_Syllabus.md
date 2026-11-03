# CSE752 – Deep Neural Networks | QUIZ 1 Syllabus (Fall 2026)

> এই ফাইলটা folder-এর সব PDF, slide, ছবি আর course description দেখে বানানো। Topic-এর নাম English-এ, ব্যাখ্যা বাংলায়।
> Quiz Bank দুটো (L-2/L-3 এবং Chapter 6) আর notice থেকে scope ধরা হয়েছে।

---

## 0. Exam Format (image.webp থেকে)

| Session | Question Type | Number of Q | Marks |
|---|---|---|---|
| 1 | Short Q&A | 10 | 10 |
| 1 | True/False (with reason) | 10 | 10 |
| 2 | Math Problem | 2 | 10 |
| 2 | Graph (paper supplied) | 2 | 20 |
| | **Total** | | **50** |
| | Time | | 60 min |

**Notice-এর সারকথা:**
- ❌ **Forward/Backward Propagation-এর math problem আসবে না** (Quiz 1-এ)। তবে forward/back propagation-এর *concept* (Short Q&A / T-F) আসতে পারে।
- Session 1 (Short Q&A + T/F): মোবাইল নিষেধ, open-book না।
- Session 2 (Math + Graph): মোবাইল/calculator শুধু calculation-এর জন্য।
- Pencil/eraser/sharpener আনো, কারণ page আর জায়গা কম।

**Marks-এর হিসাব:** Graph = 20 marks (সবচেয়ে বেশি, 40%)। তাই graph-এর practice সবচেয়ে বেশি দাও।

---

## 1. Course Description থেকে কী পাওয়া গেল

**Course:** CSE752 – Deep Neural Networks (PDF-এ CSE753 Advanced RL-ও আছে, ওটা আমাদের না)

Weekly plan অনুযায়ী Quiz-এর আওতার topic (Week 1–4):

| Week | Topic (course description) | Quiz 1-এ কোথায় পড়ছে |
|---|---|---|
| 1 | Introduction to Deep Learning | Linear regression, Gradient Descent |
| 2 | Neural Networks: Basics, Activation Functions, Loss Functions | Neuron, ReLU, Sigmoid, Softmax, MSE, Cross-Entropy |
| 3 | Forward & Backward Propagation | Concept + chain rule (math আসবে না) |
| 4 | Multi-Layer Perceptron (MLP) | XOR, hidden layer, architecture, parameters |

CNN, RNN, LSTM, GAN, Transformer ইত্যাদি (Week 5+) **এই Quiz-এ নেই।**

---

## 2. Folder-এ কী কী আছে (serially)

### 2.1 Root: `CSE752 - DNN`
1. `CSE-752 DNN Postgrad Course Description.pdf` – course description + weekly plan (3 page, scanned)

### 2.2 `Lec 1 2 __oct 7 14 2026` (Lecture 1 & 2)
| # | File | কী আছে |
|---|---|---|
| 1 | `CSE-572 1 ... Gradient_Descent.pdf` | Gradient Descent, f(x)=x² example |
| 2 | `CSE-572 2 ... Linear_Regression_Feature_Bias_Weight_MSE.pdf` | Regression, feature, target, weight, bias, residual, MSE |
| 3 | `CSE-572 3 ... Activation Function_Non Linear.pdf` | ReLU, Sigmoid, Softmax, capacity/overfitting |
| 4 | `CSE-572 4 ... Forward and Back Propagation.pdf` | Hidden/output parameter, forward pass, backward pass, update |
| 5 | `Deep_Learning___Chap-6 X-OR.pdf` | XOR, perceptron limit, hidden layer |
| 6 | `CSE-752_DNN_Lecture1.pptx` | Lecture 1 slide |
| 7 | `Ian Goodfellow ... Deep Learning (2017, MIT).pdf` | মূল textbook (Chapter 5.1.4, Chapter 6) |
| 8 | `f_x_gradient_descent.webp` | f(x)=x² GD-এর iteration table + graph |
| 9 | `CSE572_Linear_Regression_..._MSE.webp` | Linear regression-এর infographic (residual graph, bias graph, MSE table) |
| 10 | `Calculation_-_fwd_back_propagation.webp` | 1 hidden-layer ReLU network-এর fwd/back হাতে-কলমে হিসাব |

### 2.3 `Lec 3__oct 28 2026` (Lecture 3)
| # | File | কী আছে |
|---|---|---|
| 1 | `KL Divergence, Cross-Entropy, Logistic Regression and SGD.pdf` | Entropy, CE, KL, logistic regression, SGD update |
| 2 | `X-OR ReLU.pdf` | XOR, feedforward network, neuron, ReLU |
| 3 | `Gradient-Based Learning, Output Units and ReLU.pdf` | Cost function, BCE, sigmoid/softmax output unit, ReLU |
| 4 | `Architecture Design, Universal Approximation and Backpropagation.pdf` | 2–2–3 MLP, parameter count, universal approximation, Jacobian, chain rule, backprop |
| 5 | `MLP-DDoS_Classification-FWD_Prop.webp` | 2–2–3 MLP (Benign/DDoS/Port scan) forward pass |
| 6 | `2-back_prop.webp` | পুরো cycle: forward → backprop → update → forward |

### 2.4 `QUIZ 1` (এই folder)
| # | File | কী আছে |
|---|---|---|
| 1 | `image.webp` | Exam format table (Section 0) |
| 2 | `Deep_Learning_Quiz_Bank_L-2_L-3.pdf` | Lec 2–3 (Ch 3,4,5): 19 Short Q, 25 T/F, 11 Math, 10 Graph |
| 3 | `Deep_Learning_Chapter6_Quiz_Bank.pdf` | Chapter 6: 19 Short Q, 16 T/F, 16 Math, 6 Graph + formula sheet |
| 4 | `merged_L2_GD-LR-B-W-MSE-ActF-FB Prop.pdf` | Lec 1–2 PDF গুলোর merge (24 page) |
| 5 | `Merged-KL-XOR-Grad-Arch.pdf` | Lec 3 PDF গুলোর merge (38 page) |
| 6 | `f_x_gradient_descent.webp` | GD f(x)=x² infographic |

> **Reading order:** আগে `Merged` দুটো (theory), তারপর দুটো Quiz Bank (practice)।

---

## 3. SYLLABUS (Serial Order)

> ⭐ = বেশি গুরুত্বপূর্ণ (Graph/Math-এ আসার সম্ভাবনা বেশি)

### PART A — Basics (Lecture 1 & 2)

#### A1. Machine Learning Task
- **Regression** – continuous value predict (training time, house price, temperature)
- **Classification** – discrete label predict (benign/malicious, cat/dog)
- Difference বলতে পারতে হবে (Short Q আসে)

#### A2. Linear Regression ⭐
- **Feature (x)** = model-এর input attribute
- **Target (y)** = true value যেটা predict করতে চাই
- **Feature vector** x = [x₁, x₂]
- **Weight (w)** = এক unit feature বাড়লে prediction কতটা বদলায় (অন্য feature fixed)
- **Bias (b)** = line/plane-কে origin থেকে shift করে; bias না থাকলে ŷ = wx origin দিয়ে যেতে বাধ্য
- **Parameters (θ)** = সব learnable value = {w₁, w₂, …, b}
- Formula: **ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b**
- মনে রাখো: বড় weight মানেই important feature না (scale-এর উপর নির্ভর করে)
- Linear regression = একটা single neuron with identity activation

#### A3. Residual & MSE ⭐
- **Residual r = y − ŷ** (actual − predicted)
  - r > 0 → model কম predict করেছে; r < 0 → বেশি predict করেছে
- **MSE = (1/m) Σ (ŷ − y)²**
- কেন square? sign cancel হয় না + বড় error বেশি শাস্তি পায়
- MSE ≥ 0, সব prediction ঠিক হলে MSE = 0
- **Half-squared loss (single sample):** L = ½(ŷ − y)², ∂L/∂ŷ = ŷ − y

#### A4. Gradient Descent ⭐⭐ (Graph + Math দুটোতেই আসবে)
- Update rule: **θ_new = θ_old − η ∇L**, η = learning rate
- Gradient-এর উল্টো দিকে যাই (gradient যোগ করা ভুল!)
- Example **f(x) = x²**, f′(x) = 2x, x₀ = 4, η = 0.1:
  - x₁ = 3.2, x₂ = 2.56, x₃ = 2.048, x₄ = 1.6384 … → 0
  - Minimum: x* = 0, f(0) = 0
- Learning rate step size ঠিক করে; slope ছোট হলে step-ও ছোট হয়

#### A5. Activation Functions ⭐⭐
- **কেন non-linearity দরকার?** Linear layer stack করলে আসলে একটা linear layer-ই হয়
  - W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂)
- **ReLU:** max(0, z)
  - ReLU(−3) = 0, ReLU(0) = 0, ReLU(2.5) = 2.5
  - z > 0 হলে derivative = 1; z < 0 হলে derivative = 0
  - **Dying ReLU:** negative region-এ আটকে গেলে gradient বন্ধ, update হয় না
  - কেন জনপ্রিয়: সহজ, সস্তা, positive side-এ saturate করে না
- **Sigmoid:** σ(z) = 1/(1 + e⁻ᶻ)
  - Output (0,1)-এর মধ্যে (finite z-এ কখনো ঠিক 0 বা 1 না)
  - σ(0) = 0.5, σ(2) ≈ 0.881, σ(−2) ≈ 0.119, σ(1) ≈ 0.7311
  - Binary classification-এ ব্যবহার
- **Softmax:** pₖ = e^(zₖ) / Σ e^(zⱼ)
  - Mutually exclusive multiclass-এ ব্যবহার, probability-র যোগফল = 1
  - Logits [2,1,0] → [0.665, 0.245, 0.090]
- **Sigmoid vs Softmax:** sigmoid = 1টা output (class-1 probability); softmax = প্রতি class-এর জন্য 1টা

#### A6. Capacity (Under/Overfitting) – হালকা
- Model খুব ছোট → underfit; খুব বড় → overfit + costly
- Architecture validation performance দেখে বাছতে হয়

#### A7. Forward & Backward Propagation (শুধু Concept) ⭐
> Math আসবে না, কিন্তু Short Q/T-F আসবে।
- **Forward propagation:** input → hidden → output; z, h, ŷ, loss বের করে
- **Backpropagation:** chain rule দিয়ে loss থেকে পিছনের দিকে প্রতিটা parameter-এর gradient বের করে
- **Backprop ≠ Gradient Descent.** Backprop gradient *calculate* করে; GD/SGD *update* করে
- **Chain rule কেন জরুরি:** parameter loss-কে intermediate step দিয়ে প্রভাবিত করে; local derivative গুণ করতে হয়
- ReLU inactive (z<0) হলে ঐ path-এ gradient বন্ধ
- Hidden params (w, b) আর output params (v, c) আলাদা trainable parameter; output weight hidden weight থেকে বের করা হয় না
- Notation: ŷ = v₁h₁ + v₂h₂ + c; ∂L/∂v₁ = (ŷ−y)h₁; ∂L/∂c = ŷ−y
- (Reference: `Calculation_-_fwd_back_propagation.webp` – এই quiz-এ math না আসলেও concept বুঝতে দেখো)

---

### PART B — Chapter 6: Deep Feedforward Networks (Lecture 3)

#### B1. Feedforward Network & Neuron
- Input → hidden → output, কোনো recurrent loop নেই
- Neuron: **z = wᵀx + b, a = f(z)**
- উদাহরণ: x=[2,3], w=[0.5,0.2], b=1 → **z = 2.6**
- Representation learning: x → h → y

#### B2. XOR Problem ⭐⭐ (Graph-এ আসার সম্ভাবনা বেশি)
- XOR truth table: (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0
- **Single perceptron XOR শিখতে পারে না** – XOR linearly separable না (একটা straight line দিয়ে আলাদা করা যায় না)
- AND, OR → linearly separable
- **Hidden layer দিয়ে সমাধান:** h₁ = x₁ OR x₂, h₂ = x₁ AND x₂, y = h₁ AND NOT h₂
- Hidden layer input space-কে নতুন feature space-এ নেয় যেখানে সমস্যাটা linearly separable হয়

#### B3. Gradient-Based Learning & Cost Function
- θ* = argmin J(θ); update θ_new = θ_old − η∇J
- Gradient = loss parameter-এর সাথে কীভাবে বদলায় তার direction + sensitivity
- **Maximum likelihood / NLL:** J(θ) = −E[log p_model(y|x;θ)]
- Training steps: Forward → Cost → Gradient → Update (repeat)
- Gradient (scalar loss) vs **Jacobian** (vector output): Jacobian-এ প্রতিটা output-এর input-এর সাথে derivative থাকে

#### B4. Entropy, Cross-Entropy, KL Divergence ⭐⭐ (Math-এ আসার সম্ভাবনা বেশি)
- **Entropy:** H(P) = −Σ P(i) ln P(i) → target distribution-এর অনিশ্চয়তা
- **Cross-Entropy:** H(P,Q) = −Σ P(i) ln Q(i)
- **KL Divergence:** D_KL(P‖Q) = Σ P(i) ln[P(i)/Q(i)]
- **সম্পর্ক: H(P,Q) = H(P) + D_KL(P‖Q)**
- KL ≥ 0; Q = P হলে KL = 0 (কিন্তু cross-entropy = H(P), entropy হারায় না)
- KL **symmetric না**
- P fixed হলে CE minimize = KL minimize
- One-hot target-এর entropy = 0
- Example: P=(0.7,0.3), Q=(0.6,0.4) → H(P)=0.6109, H(P,Q)=0.6325, KL=0.0216 (nats)

#### B5. Logistic Regression & Binary Cross-Entropy ⭐⭐
- z = wx + b, **p = σ(z) = P(y=1|x)**; threshold দিয়ে class বাছাই
- **BCE: L = −[y ln p + (1−y) ln(1−p)]**
  - y=1 হলে L = −ln p
- Confidently wrong হলে loss অনেক বড়: p=0.8 → 0.2231; p=0.1 → 2.3026
- **Gradient (sigmoid + BCE):** ∂L/∂z = p − y, ∂L/∂w = (p−y)x, ∂L/∂b = p − y
- Example (x=2, y=1, w=0, b=0, η=0.1): grad = −1, −0.5 → w=0.10, b=0.05 → নতুন p = 0.5622, loss 0.6931 → 0.5759

#### B6. SGD
- θ_new = θ_old − η g, g = estimated gradient
- Single update সবসময় loss কমায় না, অনেক iteration/epoch-এ trend নিচে যায়

#### B7. Output Units
- **Sigmoid** → Bernoulli (binary)
- **Softmax** → multiclass (mutually exclusive)
- **Softmax + CE gradient:** ∂L/∂zₖ = pₖ − yₖ
- Example (logits [0,2,1], target DDoS): p = [0.090, 0.665, 0.245], L = 0.4076, ∇z = [0.0900, −0.3348, 0.2447]

#### B8. Architecture Design
- 2–2–3 MLP = 2 input, 2 hidden (ReLU), 3 output (Softmax)
- **Fully connected:** প্রতিটা unit আগের layer-এর সব unit থেকে input নেয়
- **Parameter count ⭐:** (in×hidden + hidden) + (hidden×out + out)
  - 2–2–3 → (4+2) + (6+3) = **15**
- Design decision: width, depth, connectivity; validation দিয়ে ঠিক করা হয়
- বেশি বড় = costly + overfit; বেশি ছোট = pattern ধরতে পারে না

#### B9. Universal Approximation Theorem
- Suitable nonlinear activation + enough hidden units থাকলে feedforward network অনেক function approximate করতে পারে
- **সতর্কতা:** এটা *representation capability*-র কথা; GD যে সঠিক parameter পাবে তার guarantee **না**
- Deeper সবসময় better/সহজে optimize হয় — এটা **ভুল**

#### B10. Chain Rule, Jacobian, Backprop in MLP (Concept)
- Chain rule: dL/dx = (dL/du)(du/dx). Example: u=2x, L=u², x=3 → 24
- Vector chain rule: ∇ₓL = Jᵀ ∇ᵤL
- Backprop = computational graph-এ chain rule + local Jacobian দিয়ে efficient gradient calculation
- Backprop gradient বের করে, optimizer update করে
- ReLU Jacobian: z>0 → 1, z<0 → 0

---

## 4. Question Type অনুযায়ী প্রস্তুতি

### 4.1 Short Q&A (10 × 1 mark) – এগুলো ভালো করে পড়ো
1. Regression vs Classification
2. Feature vs Target; Feature vector; Parameters
3. Weight-এর মানে; Bias কেন
4. Residual + sign-এর মানে
5. MSE-তে square কেন
6. Gradient Descent কী করে; learning rate-এর কাজ; derivative কী বলে
7. ReLU আচরণ + limitation (dying ReLU)
8. Sigmoid, σ(0)=0.5; sigmoid vs softmax
9. Hidden vs output parameter
10. Forward vs Backward propagation; chain rule কেন
11. Entropy, CE, KL-এর পার্থক্য + H(P,Q)=H(P)+KL
12. Logistic regression নাম regression অথচ classification কেন
13. BCE কী; SGD gradient কীভাবে ব্যবহার করে
14. Perceptron XOR পারে না কেন; hidden layer কীভাবে পারে
15. Nonlinear activation কেন দরকার
16. Feedforward network কী
17. Gradient vs Jacobian vs Backprop vs Optimizer

### 4.2 True/False with reason (10 × 1 mark) – ফাঁদ প্রশ্ন (Trap list)
| Statement | সঠিক উত্তর |
|---|---|
| বড় weight = বেশি important feature | False (scale নির্ভর) |
| Bias ছাড়া y=wx (0,0) দিয়ে যায় | True |
| Squaring error cancel হতে দেয় | False |
| GD gradient **যোগ** করে | False (বিয়োগ) |
| ReLU(−3) = −3 | False (0) |
| ReLU derivative z<0-তে 0 | True |
| Sigmoid ঠিক 0 বা 1 দেয় | False |
| σ(0) = 0.5 | True |
| Softmax sum = 1 | True |
| Output weight (v) hidden weight (w) থেকে বের হয় | False |
| Backprop = GD | False |
| KL symmetric | False |
| KL ≥ 0, P=Q হলে 0 | True |
| CE min = KL min (P fixed) | True |
| One-hot entropy = 0 | True |
| XOR linearly separable | False |
| AND/OR linearly separable | True |
| Single sigmoid = 3-class softmax structure | False |
| 2–2–3 MLP-এ 15 parameter | True |
| UAT মানে GD ঠিক parameter পাবে | False |
| Deeper সবসময় better | False |
| ReLU negative z → gradient path blocked | True |

### 4.3 Math Problem (2 × 5 marks) – Fwd/Back prop **বাদ**, এগুলো করো
1. Linear regression prediction: ŷ = 2x₁+3x₂+5, x=(2,2) → 15
2. Residual ও squared error (y=17 → r=2, r²=4)
3. **GD steps** f(x)=x², x₀=4, η=0.1 → 3.2, 2.56 …
4. MSE হিসাব (table থেকে, যেমন 0.25)
5. ReLU / Sigmoid মান বের করা
6. Neuron z হিসাব (z=2.6), hidden h=ReLU(z)
7. Half-squared loss L = ½(ŷ−y)²
8. **Entropy / CE / KL** (P=(0.7,0.3), Q=(0.6,0.4))
9. **BCE** (p=0.8, y=1/0)
10. **Softmax** probability + CE loss (logits [2,1,0] / [0,2,1])
11. Logistic regression একটা SGD step (grad p−y)
12. **Parameter count** MLP-এর
13. Chain rule (u=2x, L=u²)

> Calculator দিয়ে: ln(0.7)=−0.3567, ln(0.3)=−1.2040, ln(0.6)=−0.5108, ln(0.4)=−0.9163, e²=7.389, e¹=2.718

### 4.4 Graph (2 × 10 marks) ⭐⭐⭐ সবচেয়ে বেশি marks
প্রতিটা graph-এ: **axis label, scale, key point, curve shape, minimum/special point label** দাও।

| # | Graph | Key points / বৈশিষ্ট্য |
|---|---|---|
| G1 | **f(x)=x²** (−2 থেকে 2) | (−2,4), (−1,1), (0,0), (1,1), (2,4); U-shape, min (0,0) |
| G2 | **GD on f(x)=x²** | x=4, 3.2, 2.56, 2.048, 1.6384; arrow বাম দিকে, 0-র দিকে |
| G3 | **Residual** y=x+1, observed (2,2) | predicted (2,3), dashed vertical line, r = −1 |
| G4 | **ReLU** (−4 থেকে 4) | নেগেটিভে 0 flat, positive-এ y=z; (1,1), (2,2), (4,4) |
| G5 | **Sigmoid** | (−2,0.119), (0,0.5), (2,0.881); S-curve, 0 আর 1 asymptote |
| G6 | **BCE (y=1)** L=−ln p | (0.1,2.3026), (0.2,1.6094), (0.3,1.2040), (0.4,0.9163), (0.5,0.6931), (0.6,0.5108), (0.7,0.3567), (0.8,0.2231), (0.9,0.1053); নামতে থাকা curve |
| G7 | **XOR 4 points** | (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0; আলাদা symbol; কোনো line আলাদা করে না |
| G8 | **AND points** | শুধু (1,1)→1; linearly separable |
| G9 | **OR points** | শুধু (0,0)→0; linearly separable |
| G10 | **Bias effect** | ŷ=2x (b=0) vs ŷ=2x+5; parallel line, একটা origin দিয়ে যায় |

> Lecture image-এ আরও আছে: GD table-এ x₅=1.3107, x₆=1.0486, x₇=0.8389 … (`f_x_gradient_descent.webp`)

---

## 5. Quick Formula Sheet (পরীক্ষার আগের দিন এটা দেখো)

| Concept | Formula |
|---|---|
| Linear regression | ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b |
| Residual | r = y − ŷ |
| MSE | (1/m) Σ (ŷ − y)² |
| Half-squared loss | L = ½(ŷ − y)², ∂L/∂ŷ = ŷ − y |
| Gradient Descent | θ_new = θ_old − η ∇L |
| GD on x² | f′(x)=2x; x_new = x_old − η(2x_old) |
| Neuron | z = wᵀx + b; a = f(z) |
| ReLU | max(0, z) |
| Sigmoid | 1/(1+e⁻ᶻ) |
| Softmax | pₖ = e^(zₖ)/Σ e^(zⱼ) |
| Entropy | H(P) = −Σ P ln P |
| Cross-Entropy | H(P,Q) = −Σ P ln Q |
| KL | D_KL(P‖Q) = Σ P ln(P/Q) |
| Relation | H(P,Q) = H(P) + D_KL(P‖Q) |
| BCE | −[y ln p + (1−y) ln(1−p)] |
| Sigmoid+BCE grad | ∂L/∂z = p−y; ∂L/∂w = (p−y)x; ∂L/∂b = p−y |
| Softmax+CE grad | ∂L/∂zₖ = pₖ − yₖ |
| SGD | θ_new = θ_old − η g |
| Params (fully connected) | Σ (in×out + out) |
| Chain rule | dL/dx = (dL/du)(du/dx) |
| Vector chain rule | ∇ₓL = Jᵀ ∇ᵤL |

---

## 6. Study Plan (সুপারিশ)

1. **Day 1:** Part A (Linear regression, MSE, GD, Activation) – `merged_L2...pdf` + `Quiz_Bank_L-2_L-3.pdf` Part I-III
2. **Day 2:** Part B (Entropy/KL/CE, Logistic, Softmax, XOR, Architecture) – `Merged-KL-XOR-Grad-Arch.pdf` + `Chapter6_Quiz_Bank.pdf` Section A-C
3. **Day 3:** **Graph practice** – উপরের G1–G10 হাতে এঁকে দেখো (paper-এ, pencil দিয়ে)
4. **Day 4:** T/F trap list মুখস্থ + Math (4.3) আবার solve + formula sheet

---

## 7. মনে রাখার বিষয়
- ❌ Fwd/Back prop-এর numerical আসবে না। কিন্তু **Short Q/T-F-এ concept** আসতে পারে।
- Graph-এ সবসময় **axis label + key point + curve shape + special point (minimum / 0.5 / asymptote)** দাও।
- Calculator শুধু Session 2-তে।
- GD-তে **minus**, Backprop ≠ GD, KL symmetric না, XOR separable না, UAT ≠ training guarantee।
