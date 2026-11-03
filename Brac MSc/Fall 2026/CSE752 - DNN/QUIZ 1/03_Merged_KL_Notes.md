# PDF 3 — Merged-KL-XOR-Grad-Arch (KL/CE/Logistic/SGD · XOR/ReLU · Gradient-Based Learning/Output Units · Architecture/UAT/Backprop)

> **Source:** `Merged-KL-XOR-Grad-Arch.pdf` (38 page, লেখক: Refai Arafat Rossi, Oct 2026; Goodfellow *Deep Learning* Chapter 6-এর উপর)
> পুরো PDF পড়ে topic-wise note। প্রতিটা সংখ্যা computer দিয়ে আবার হিসাব করা।
> Syllabus tag (A1…B10) = `QUIZ1_Syllabus.md`-এর topic।

## 0. PDF-এর গঠন (page map)

| Page | কী আছে | Syllabus |
|---|---|---|
| p1–8 | **Problem 1** (Entropy, Cross-Entropy, KL) + **Problem 2** (Logistic regression + SGD) | B3, B4, B5 |
| p9–18 | Feedforward network lecture notes (neuron, XOR, hidden layer, nonlinearity, ReLU) | B1, B2, B7 |
| p19–27 | Gradient-based learning, cost function, output units (sigmoid, softmax), hidden units, ReLU | B4, B5, B6, B7 |
| p28–38 | Architecture design, Universal Approximation, chain rule/Jacobian, backprop (2–2–3 MLP) | B8, B9, B10 |

> ⚠️ **Backprop-এর numerical math (p32–38) notice অনুযায়ী আসবে না।** শুধু concept। বোঝার জন্য ধাপগুলো নিচে দেওয়া আছে।
> সব log = **natural log (ln)**, unit = **nats**।

---

## 1. Problem 1 — Entropy, Cross-Entropy, KL Divergence (p1–4) `[B3]`

### 1.1 Setup
Medical image classification: দুই class A, B।

| Class | Target P | Model Q |
|---|---|---|
| A | 0.70 | 0.60 |
| B | 0.30 | 0.40 |
| Total | 1.00 | 1.00 |

লক্ষ্য: Q আর P-এর অমিল মাপা → loss বানানো।

### 1.2 তিনটা সম্পর্কিত রাশি
- **Entropy** H(P) = −Σᵢ P(i) ln P(i) — target distribution-এর নিজের অনিশ্চয়তা
- **Cross-entropy** H(P,Q) = −Σᵢ P(i) ln Q(i) — Q দিয়ে P-এর outcome লিখলে গড় information cost
- **KL divergence** D_KL(P‖Q) = Σᵢ P(i) ln[P(i)/Q(i)] — অমিলের কারণে **extra** cost
  - KL ≥ 0; P=Q হলে 0
  - ⚠️ **symmetric না** (P, Q বদলালে মান বদলায়)

### 1.3 মূল সম্পর্ক
**H(P,Q) = H(P) + D_KL(P‖Q)** (Cross-entropy = target entropy + KL)
- P fixed হলে H(P) constant → **CE minimize = KL minimize**

### 1.4 হিসাব (P=(0.7,0.3), Q=(0.6,0.4))
| রাশি | হিসাব | মান |
|---|---|---|
| H(P) | −[0.7 ln 0.7 + 0.3 ln 0.3] | **0.6109** |
| H(P,Q) | −[0.7 ln 0.6 + 0.3 ln 0.4] = 0.3576 + 0.2749 | **0.6325** |
| D_KL | 0.7 ln(0.7/0.6) + 0.3 ln(0.3/0.4) = 0.1079 − 0.0863 | **0.0216** |
| Verify | H(P) + KL = 0.6109 + 0.0216 | 0.6325 ✓ |

### 1.5 মডেল ভালো হলে (Q = P = (0.7,0.3))
| Q | Cross-entropy | KL |
|---|---|---|
| (0.6, 0.4) | 0.6325 | 0.0216 |
| (0.7, 0.3) | 0.6109 | 0.0000 |

⚠️ Q=P হলে mismatch (KL) যায়, কিন্তু **target entropy থেকে যায়** (CE = H(P) = 0.6109)।

### 1.6 সাধারণ deep learning: one-hot target
True class A → P=(1,0)। Model p=0.70 → H(P,Q) = −ln(0.70) = **0.3567**; p=0.95 → −ln(0.95) = **0.0513**।
- **One-hot target-এর entropy 0** → তখন **CE = KL** (দুটো একই)
- Correct class-এ probability বাড়লে loss কমে।

### 1.7 BCE loss curve (p4, Figure 1) — graph `[B4]`
p = class 1-এর predicted probability।
- **y=1:** L(p) = −ln p → p→1 এ ছোট, p→0 এ অনেক বড়
- **y=0:** L(p) = −ln(1−p) → উল্টো
- Confident correct prediction-কে পুরস্কার, confident wrong-কে শাস্তি।
- (Figure: x-axis p = 0.1…1; y-axis loss 1,2,3; নীল রেখা y=1: −ln p নামছে; লাল dashed y=0: −ln(1−p) উঠছে; ~p=0.5 এ cross)

---

## 2. Problem 2 — Logistic Regression + SGD (p4–8) `[B4, B5]`

### 2.1 Setup
Network traffic: y=0 benign, y=1 malicious। এক feature x (suspicious score)। **x=2, y=1; initial w=0, b=0.**

### 2.2 Logistic regression কী
নামে regression, কাজে **binary classification**।
1. Linear score: z = wx + b
2. Sigmoid: **p = P(y=1|x) = σ(z) = 1/(1+e⁻ᶻ)** (finite z-এ (0,1)-এর মধ্যে strictly)
3. Rule: **ŷ = 1 যদি p ≥ 0.5, নইলে 0** (threshold class ঠিক করে; training p দিয়ে)

### 2.3 ধাপে ধাপে (এক SGD step, η = 0.1)
| ধাপ | হিসাব | ফল |
|---|---|---|
| Initial z | (0)(2)+0 | 0 |
| Initial p | σ(0) = 1/(1+e⁰) | **0.5** |
| Initial loss (y=1) | −ln(0.5) | **0.6931** |
| Gradient ∂L/∂z | p−y = 0.5−1 | −0.5 |
| ∂L/∂w | (p−y)x = (−0.5)(2) | **−1** |
| ∂L/∂b | p−y | **−0.5** |
| w_new | 0 − 0.1(−1) | **0.10** |
| b_new | 0 − 0.1(−0.5) | **0.05** |
| z_new | 0.1(2)+0.05 | 0.25 |
| p_new | σ(0.25) | **0.5622** |
| L_new | −ln(0.5622) | **0.5759** |

Loss 0.6931 → 0.5759 (প্রায় 0.1172 কমেছে); p 50.00% → 56.22%।
- Gradient দুটোই negative → বিয়োগ করায় parameter **বেড়েছে**।

**Sigmoid + BCE gradient (মুখস্থ):** ∂L/∂z = p−y, ∂L/∂w = (p−y)x, ∂L/∂b = p−y

### 2.4 Cost: BCE
**L(y,p) = −[y ln p + (1−y) ln(1−p)]** = Bernoulli output-এর **negative log-likelihood**; এটা minimize করা training objective।

### 2.5 SGD
**θ ← θ − η ĝ** (ĝ = estimated gradient, η = learning rate); estimated gradient-এর **উল্টো দিকে** যাই।

### 2.6 Pipeline (Figure 2)
Input x → Linear z=wx+b → Sigmoid p=σ(z) → Cross-entropy L(y,p) → Gradient ∇θL → SGD update θ←θ−ηĝ
- **Logistic regression** = prediction model; **Cross-entropy** = কতটা ভুল; **Gradient** = parameter কীভাবে loss প্রভাবিত করে; **SGD** = update করে।

---

## 3. Feedforward Networks, XOR, ReLU (p9–18) `[B1, B2, B7]`

### 3.1 Feedforward network কী
Input → computation → output; **recurrent loop নেই**। রূপান্তর: **x → h → y** (h = hidden representation)। Layers: input, hidden, output।

### 3.2 কেন deep learning (সরল linear model-এর সীমা)
Student-pass example: x₁ = study hours, x₂ = attendance; y=1 pass / 0 fail; z = 2x₁ + 3x₂ − 5; তারপর activation। Linear model অনেক কাজ করে, কিন্তু **সব input-output সম্পর্ক** represent করতে পারে না।

### 3.3 একটা Neuron `[B1]`
- **z = w₁x₁ + w₂x₂ + b = wᵀx + b**, তারপর **a = f(z) = f(wᵀx+b)** (chapter-এর কেন্দ্রীয় সমীকরণ)
- উদাহরণ x=[2,3]ᵀ, w=[0.5,0.2]ᵀ, b=1: wᵀx = (0.5)(2)+(0.2)(3) = 1.6; **z = 1.6 + 1 = 2.6**
- w = feature-এর contribution; b = pre-activation shift; f = activation (nonlinear হলে nonlinear সম্পর্ক শেখে)

### 3.4 XOR সমস্যা `[B2]`
XOR = exclusive OR; দুই input **আলাদা** হলে 1।

| x₁ | x₂ | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 3.5 এক Perceptron XOR শিখতে পারে না
- Perceptron: z = w₁x₁+w₂x₂+b; y = 1 যদি z>0, নইলে 0
- Decision boundary **w₁x₁+w₂x₂+b=0 = সরলরেখা** (2 input-এ)
- XOR-এ দুই positive (0,1),(1,0) একটা কর্ণে, দুই negative (0,0),(1,1) অন্য কর্ণে → **একটা সরলরেখায় আলাদা করা যায় না → linearly separable না**
- **AND** (শুধু (1,1)=1) ও **OR** (শুধু (0,0)=0) **linearly separable**
- Figure (p13): বর্গের চার কোণ; (0,0)=0 লাল, (1,0)=1 নীল, (0,1)=1 নীল, (1,1)=0 লাল (label একটু overlap করা)

### 3.6 সমাধান: Hidden layer `[B2]`
XOR(x₁,x₂) = (x₁ OR x₂) **AND NOT** (x₁ AND x₂)
- h₁ = x₁ OR x₂, h₂ = x₁ AND x₂, **y = h₁ AND NOT h₂**

| x₁ | x₂ | h₁=OR | h₂=AND | y=h₁∧¬h₂ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

**Threshold neuron দিয়ে (step(z)=1 যদি z>0, নইলে 0):**
- h₁ = step(x₁ + x₂ − 0.5) (OR)
- h₂ = step(x₁ + x₂ − 1.5) (AND)
- y = step(h₁ − h₂ − 0.5)
- Check: (0,0): h=(0,0) → y=step(−0.5)=0; (0,1): h=(1,0) → y=step(0.5)=1; (1,0): h=(1,0) → 1; (1,1): h=(1,1) → y=step(−0.5)=0 ✓

**Representation learning:** মূল input (x₁,x₂) → hidden representation (h₁,h₂)। Network নিজে দরকারি intermediate feature শেখে।

### 3.7 কেন nonlinear activation লাগে `[A5]`
শুধু affine layer: h=W₁x+b₁, y=W₂h+b₂ → **y = W₂W₁x + W₂b₁ + b₂ = আবার একটা affine transformation**।
→ অনেক affine layer ≡ একটা affine transformation। Nonlinear f দিয়ে h=f(Wx+b) হলে nonlinear সম্পর্ক শেখা যায়।

**Common activations:** Step, Sigmoid, tanh, ReLU, Leaky ReLU, Softmax (এই lecture-এর focus ReLU)।

### 3.8 ReLU `[B7]`
- **ReLU(x) = max(0,x)** = 0 (x<0), x (x≥0)
- Negative → 0; positive → unchanged; zero → 0
- উদাহরণ: ReLU(5)=5, ReLU(−3)=0, ReLU(0)=0, ReLU(2.7)=2.7, ReLU(−8.4)=0, **ReLU(−2.5)=0**
- Graph (Figure 3): −4…4; x<0 flat y=0; x≥0 y=x (4 পর্যন্ত গ্রিড)

**কেন জনপ্রিয়:** (1) সহজ (2) সস্তা (comparison, exponential না) (3) piecewise linear হলেও layer জুড়ে nonlinear (4) positive side-এ derivative 1 → sigmoid/tanh-এর মতো positive saturation নেই।

**Derivative:** ReLU′(x) = 0 (x<0), 1 (x>0); **x=0-তে classical অর্থে differentiable না, implementation subgradient convention নেয়, সাধারণত 0।**
**Limitation:** কোনো neuron সব input-এর জন্য negative region-এ থাকলে gradient 0 → update বন্ধ = **dying ReLU problem**।

### 3.9 Quick review (p17)
1. Feedforward NN কী? 2. Weight ও bias কী করে? 3. কেন perceptron AND/OR পারে, XOR পারে না? 4. Linearly separable মানে? 5. Hidden layer XOR কীভাবে solve করে? 6. Nonlinear activation কেন দরকার? 7. ReLU(−4), ReLU(0), ReLU(3.5) = **0, 0, 3.5** 8. Nonlinear ছাড়া অনেক affine layer stack করলে কী হয়? → একটা affine transformation-ই থাকে।

**Key takeaways:** neuron = weighted sum + bias + activation · perceptron-এর linear boundary XOR পারে না · hidden layer intermediate feature বানিয়ে XOR সমাধান করে · affine layer stack nonlinear মডেল দেয় না · nonlinear activation জরুরি · ReLU সহজ ও দক্ষ।

---

## 4. Gradient-Based Learning, Output Units, Hidden Units (p19–27) `[B4–B7]`

### 4.1 Problem: Network attack detection
Input x = [2, 1]ᵀ (x₁ = packet-rate feature = 2, x₂ = connection-failure feature = 1)। Task A: benign(0)/malicious(1); training label y=1। Task B: benign / DDoS / port scan।

### 4.2 Gradient-based learning
- Model ŷ = f(x;θ); **Cost J(θ) = L(f(x;θ), y)**; লক্ষ্য **θ* = argmin J(θ)**
- Gradient ∇θJ = cost parameter-এর সাথে কীভাবে বদলায়
- **θ_new = θ_old − η∇θJ** (gradient steepest **বৃদ্ধির** দিক, তাই বিয়োগ)
- **Training loop:** (1) Forward pass → prediction (2) Cost (3) Gradient (4) Update (SGD/optimizer), তারপর repeat
- Gradient ঠিকমতো বের করার efficient algorithm = **backpropagation** (Goodfellow §6.5)

### 4.3 Cost (Maximum likelihood)
**J(θ) = −E_(x,y)~p̂_data [log p_model(y|x;θ)]**; N উদাহরণে J(θ) = −(1/N) Σ log p_model(yᵢ|xᵢ;θ) = **negative log-likelihood** = উপযুক্ত cross-entropy।

### 4.4 Cross-entropy (binary) `[B4]`
L(y,p) = −[y log p + (1−y) log(1−p)], p=P(y=1|x); y=1 হলে **L = −log p**।
- p = 0.80 → **0.2231**; p = 0.10 (confidently wrong) → **2.3026**

| Predicted p | True y | Loss |
|---|---|---|
| 0.95 | 1 | 0.0513 |
| 0.80 | 1 | 0.2231 |
| 0.50 | 1 | 0.6931 |
| 0.10 | 1 | 2.3026 |

শিক্ষা: CE শুধু ঠিক/ভুল দেখে না, correct class-এ কত probability দিয়েছে তাও দেখে।

### 4.5 Logistic regression `[B4]`
z = wᵀx + b; **p = σ(z)**; threshold সাধারণত 0.5। z=1 → **p = 1/(1+e⁻¹) ≈ 0.7311**; y=1 হলে **L = −ln(0.7311) ≈ 0.3133**।
**Neural net-এর সাথে সম্পর্ক:** logistic regression সরাসরি x ব্যবহার করে p=σ(wᵀx+b); neural net-এ hidden layer আগে h শেখে, তারপর output layer logistic regression চালায়: **p = σ(wᵀh + b)**।

### 4.6 Output units — Sigmoid (Bernoulli) `[B6]`
- যখন target binary (benign/malicious, spam/not spam, disease/no disease)
- Bernoulli এক probability p=P(y=1|x) দিয়েই পূর্ণ; অন্য outcome = 1−p
- **ŷ = σ(z), z = wᵀh + b**; **P(y|x) = ŷʸ(1−ŷ)^(1−y)**; এর NLL = BCE

**Sigmoid table (p23):**
| Logit z | σ(z) | মানে |
|---|---|---|
| −2 | 0.1192 | attack-এর কম probability |
| 0 | 0.5000 | সমান probability |
| 1 | 0.7311 | attack-এর বেশি probability |
| 2 | 0.8808 | attack-এর উচ্চ probability |

Sigmoid probability estimate, গ্যারান্টি না; threshold 0.5 common (false positive/negative cost অনুযায়ী বদলানো যায়)।

**এক পূর্ণ prediction:** h=[2,1]ᵀ, **z = 0.7h₁ + 0.4h₂ − 0.8 = 0.7(2)+0.4(1)−0.8 = 1** → p = σ(1) = 0.7311; y=1 → L = 0.3133।

**এক update (η=0.1, শুধু output weight/bias):**
- ∂L/∂z = p−y = 0.7311−1 = **−0.2689**
- ∂L/∂wⱼ = (p−y)hⱼ; ∂L/∂b = p−y

| Parameter | আগে | পরে |
|---|---|---|
| w₁ | 0.7000 | 0.7538 |
| w₂ | 0.4000 | 0.4269 |
| b | −0.8000 | −0.7731 |

নতুন z ≈ 1.1614 → p_new ≈ 0.7615 (exact 0.7616) → **L_new ≈ 0.2725** (exact 0.2724); loss 0.3133 → 0.2725 কমেছে।

### 4.7 Output units — Softmax (Multinoulli) `[B6]`
Task B: Benign / DDoS / Port scan — **mutually exclusive**; একটা sigmoid যথেষ্ট না।
- **pₖ = e^(zₖ) / Σⱼ e^(zⱼ)**, 0 < pₖ < 1, **Σpₖ = 1**; softmax-এর আগের score = **logits** (probability না, যেকোনো real)
- Logits (Benign 0, DDoS 2, Port scan 1): e⁰=1, e²=7.389, e¹=2.718, sum=11.107
  - **P(Benign)=0.090, P(DDoS)=0.665, P(Port scan)=0.245** → predicted = DDoS
- True class DDoS (y=[0,1,0]ᵀ): **L = −Σ yₖ log pₖ = −ln(0.665) ≈ 0.408**
- **Softmax + CE gradient: ∂L/∂zₖ = pₖ − yₖ**

**Sigmoid বনাম Softmax:**
| | Sigmoid | Softmax |
|---|---|---|
| Application | Binary classification | Single-label multiclass |
| Output | positive class-এর 1টা probability | প্রতি class-এ 1টা probability |
| Probability relation | negative = 1−p | সব class-এর যোগফল = 1 |
| Distribution | Bernoulli | Multinoulli/categorical |
| Loss | Binary CE | Multiclass CE |
| উদাহরণ | benign vs attack | benign, DDoS, port scan |

⚠️ একসাথে **একাধিক label সত্য** হতে পারলে (যেমন এক traffic-এ একাধিক আলাদা attribute) **আলাদা আলাদা sigmoid** ভালো; softmax mutually exclusive-এর জন্য।

### 4.8 Hidden units ও ReLU (p26–27) `[B7]`
Layer: **h = g(Wᵀx + b)**। Example: x=[2,1]ᵀ; z₁ = x₁+x₂−1 = 2, z₂ = x₁−x₂ = 1; **h = [ReLU(2), ReLU(1)]ᵀ = [2, 1]ᵀ**।

- ReLU g(z) = max(0,z) = 0 (z≤0), z (z>0); active region-এ linear; gradient খুব বড় input-এও কমে না
- Sigmoid: 0–1 output, চরম input-এ saturate করে, gradient খুব ছোট হতে পারে

**ReLU table (p27):**
| z | ReLU | মানে |
|---|---|---|
| −2 | 0 | inactive |
| −0.5 | 0 | inactive |
| 0 | 0 | output zero |
| 0.5 | 0.5 | active |
| 2 | 2 | active |

**ReLU derivative:** g′(z) = 0 (z<0), 1 (z>0); active হলে gradient সোজা পার হয়।
**Generalization** = অদেখা data-তে ভালো করা। ReLU generalization **গ্যারান্টি করে না**; hidden layer optimize সহজ করে, কিন্তু generalization নির্ভর করে data, capacity, architecture, validation-এর উপর।

### 4.9 সব মিলিয়ে (p27)
Gradient-based learning = parameter optimize · Cross-entropy = predicted ও target distribution-এর mismatch · Logistic regression = linear score থেকে binary probability · Sigmoid = Bernoulli · Softmax = mutually exclusive class-এর distribution · Hidden units = intermediate feature শেখে · ReLU = nonlinearity + gradient passing · Generalization = unseen data performance।

---

## 5. Architecture, Universal Approximation, Backprop (p28–38) `[B8–B10]`

### 5.1 Problem
x = [2,1]ᵀ; তিন mutually exclusive class: C₁ Benign, C₂ DDoS, C₃ Port scan; training example-এর সঠিক class DDoS, **one-hot y = [0,1,0]ᵀ**।

### 5.2 Architecture design `[B8]`
- **2–2–3 MLP:** 2 input · 2 hidden (**ReLU**) · 3 output (**Softmax**); এক hidden layer।
- **Fully connected:** প্রতি unit আগের layer-এর **সব** unit থেকে input নেয়
- Hidden layer **ReLU** আর output **Softmax** (তিনটা mutually exclusive class)
- z⁽¹⁾ = W⁽¹⁾ᵀx + b⁽¹⁾; h = ReLU(z⁽¹⁾); z⁽²⁾ = W⁽²⁾ᵀh + b⁽²⁾; pₖ = softmax
- সবচেয়ে বড় probability-র output = predicted class

**Parameter count ⭐:**
- Input→hidden: 2×2 = 4 weight + 2 bias = **6**
- Hidden→output: 2×3 = 6 weight + 3 bias = **9**
- **মোট = 6 + 9 = 15** (সাধারণ সূত্র: Σ (in × out + out))

**কীভাবে architecture ঠিক করে:** কোনো একটা architecture সব task-এর জন্য সেরা না; width, depth, connectivity — validation performance দেখে।

| Design decision | মানে | আমাদের উদাহরণ |
|---|---|---|
| Input width | কয়টা feature | 2 |
| Hidden width | প্রতি hidden layer-এ unit | 2 |
| Depth | কয়টা hidden transformation | 1 hidden layer |
| Output width | কয়টা class | 3 |
| Connectivity | adjacent layer কীভাবে যুক্ত | Fully connected |

বেশি ছোট → pattern ধরতে পারে না; বেশি বড় → খরচ বেশি + overfit।

### 5.3 Universal Approximation Theorem `[B9]`
Suitable nonlinear hidden activation + **যথেষ্ট hidden unit** থাকলে feedforward network compact domain-এ যেকোনো continuous function যেকোনো precision-এ approximate করতে পারে; ReLU network-এর জন্যও result আছে।

**তিনটা limitation (মুখস্থ):**
1. ❌ Training algorithm সঠিক parameter **পাবে** তার গ্যারান্টি নেই
2. ❌ Unseen data-তে **generalization**-এর গ্যারান্টি নেই
3. ❌ Deeper network **সবসময় better বা সহজে optimize** হয় না

**Linear model কেন যথেষ্ট না:** nonlinear hidden activation ছাড়া linear layer stack = আবার affine function।
**Deep network কেন দরকার:** তাত্ত্বিকভাবে এক hidden layer যথেষ্ট, কিন্তু কিছু function-এ অনেক unit লাগে; deep network hierarchical function কম parameter-এ দেখাতে পারে (deeper ReLU network-এর linear region গভীরতার সাথে দ্রুত বাড়ে)। Depth ও width = hyperparameter, data দিয়ে evaluate করতে হয়।

### 5.4 Backpropagation — concept `[B10]`
**Backprop gradient *calculate* করে; GD/SGD বা অন্য optimizer *update* করে।**
- **Forward propagation:** input থেকে output-এর দিকে activation, logits, probability, loss
- **Backward propagation:** loss-এর derivative থেকে পেছনের দিকে gradient
- **Parameter update:** gradient দিয়ে weight/bias update, তারপর repeat
- Backprop = **computational graph-এ derivative efficiently** বের করার general procedure; প্রতি layer উপরের layer-এর gradient **reuse** করে (প্রতি parameter আলাদা করে পুরো network differentiate করতে হয় না)।

### 5.5 Chain rule, Gradient, Jacobian `[B10]`
**Chain rule:** u=2x, L=u²; dL/dx = (dL/du)(du/dx) = 2u × 2 = 4u; **x=3 → u=6 → dL/dx = 12 × 2 = 24**।
(চেইনের মূল কথা: এক variable অন্যের উপর মধ্যবর্তী ধাপ দিয়ে নির্ভর করলে local derivative **গুণ** করতে হয়।)

**Gradient** (scalar loss L): ∇θL = [∂L/∂θ₁, …, ∂L/∂θₙ]ᵀ — প্রতি entry দেখায় অন্য parameter ঠিক রেখে ওই parameter বদলালে loss কতটা বদলায়।

**Jacobian** (vector → vector y=f(x), x∈ℝᵐ, y∈ℝⁿ): J_f(x) = [∂yᵢ/∂xⱼ] (n×m matrix)। **Vector chain rule: ∇ₓL = J_f(x)ᵀ ∇ᵧL**। Backprop-এর মূল ক্রিয়া: local Jacobian দিয়ে gradient এক operation থেকে তার input-এ পাঠানো।

**Softmax Jacobian:** ∂pᵢ/∂zⱼ = pᵢ(δᵢⱼ − pⱼ) (i=j হলে δ=1, নইলে 0)। p=[0.090031, 0.665241, 0.244728]ᵀ:

| | z₁ | z₂ | z₃ |
|---|---|---|---|
| p₁ | 0.081925 | −0.059892 | −0.022033 |
| p₂ | −0.059892 | 0.222695 | −0.162803 |
| p₃ | −0.022033 | −0.162803 | 0.184836 |

(এক logit বদলালে একাধিক class-এর probability বদলায়, কারণ softmax সবাইকে একসাথে normalize করে।)

**Softmax + CE:** ∂L/∂pᵢ = −yᵢ/pᵢ; chain rule দিয়ে ∂L/∂zⱼ = Σᵢ(∂L/∂pᵢ)(∂pᵢ/∂zⱼ) = **pⱼ − yⱼ** → **δ⁽²⁾ = p − y**
- DDoS example: δ⁽²⁾ = [0.090031, 0.665241−1, 0.244728]ᵀ = **[0.090031, −0.334759, 0.244728]ᵀ**

### 5.6 2–2–3 MLP-এর পুরো হিসাব (p32–38) — ⚠️ exam-এ math আসবে না, শুধু বোঝার জন্য
**Forward:** W⁽¹⁾ = [[0.5,−0.5],[−0.5,1.0]], b⁽¹⁾ = [0, 0.5]ᵀ; W⁽²⁾ = [[0,1,2],[0,3,0]], b⁽²⁾ = 0
- z⁽¹⁾ = W⁽¹⁾ᵀx + b⁽¹⁾ = [0.5, 0]ᵀ + [0, 0.5]ᵀ = **[0.5, 0.5]ᵀ**; h = ReLU = [0.5, 0.5]ᵀ (দুটোই active)
- z⁽²⁾ = W⁽²⁾ᵀh = **[0, 2, 1]ᵀ** (Benign, DDoS, Port scan)
- p = **[0.090031, 0.665241, 0.244728]ᵀ**; **L = −ln(0.665241) = 0.407606**

**Backward:**
- Output layer: ∇W⁽²⁾L = h δ⁽²⁾ᵀ = [[0.045015, −0.167380, 0.122364],[0.045015, −0.167380, 0.122364]]; ∇b⁽²⁾L = δ⁽²⁾ (bias-এর derivative 1)
- Hidden-এ: ∇hL = W⁽²⁾δ⁽²⁾; ∂L/∂h₁ = 0(0.090031)+1(−0.334759)+2(0.244728) = **0.154698**; ∂L/∂h₂ = 3(−0.334759) = **−1.004277**
- ReLU: ReLU′ = 1 (z=0.5>0, দুটোই active; ReLU Jacobian = I) → **δ⁽¹⁾ = ∇hL ⊙ ReLU′(z⁽¹⁾) = [0.154698, −1.004277]ᵀ**
  - কোনো hidden unit-এর z negative হলে ওই ReLU derivative 0 → gradient ওই input-এর জন্য blocked
- First layer: ∇W⁽¹⁾L = x δ⁽¹⁾ᵀ = [[0.309396, −2.008554],[0.154698, −1.004277]]; ∇b⁽¹⁾L = δ⁽¹⁾
- ➜ **15টা parameter-এর gradient সব পাওয়া গেল।**

**SGD update (η=0.1):**
- W⁽¹⁾ ≈ [[0.469060, −0.299145],[−0.515470, 1.100428]]; b⁽¹⁾ ≈ [−0.015470, 0.600428]ᵀ
- W⁽²⁾ ≈ [[−0.004502, 1.016738, 1.987764],[−0.004502, 3.016738, −0.012236]]; b⁽²⁾ ≈ [−0.009003, 0.033476, −0.024473]ᵀ
- নেগেটিভ gradient → parameter বাড়ে (SGD বিয়োগ করে)

**নতুন forward:** z⁽¹⁾ ≈ [0.407181, 1.102566]ᵀ = h; z⁽²⁾ ≈ [−0.015799, 3.773626, 0.771416]ᵀ; p_new ≈ [0.021084, 0.932587, 0.046328]ᵀ

| State | CE loss | DDoS probability |
|---|---|---|
| Before SGD | 0.407606 | 66.52% |
| After SGD | 0.069793 | 93.26% |

⚠️ এটা **একটা example-এর একটা update**; বাস্তবে অনেক sample ও epoch-এ অনেক iteration হয়, আর **একটা update সবসময় loss কমায় না**।

---

## 6. Gradient Descent math — GD problem ও SGD

> এই PDF-এ SGD (θ←θ−ηĝ) ও logistic regression-এর এক step আছে (§2.3 উপরে)। নিচে `f_x_gradient_descent.webp`-এর সম্পূর্ণ সমাধান:

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

## 7. Graph table (এই PDF-এর graph/figure ও topic)

| Graph | Key points | Curve/বৈশিষ্ট্য | Syllabus | কোথায় |
|---|---|---|---|---|
| **BCE দুই curve** (y=1: −ln p, y=0: −ln(1−p)) | x: p = 0.1…1; y: loss 1, 2, 3; y=1 curve: p=0.1 → 2.3026, 0.5 → 0.6931, 0.9 → 0.1054 | y=1 নামে, y=0 ওঠে, ~p=0.5 এ cross; confident wrong-এ loss বড় | B4 | p4 Figure 1 |
| **XOR 4 point** | (0,0)=0, (0,1)=1, (1,0)=1, (1,1)=0 | কর্ণ বরাবর class বদলায়; একটা রেখা আলাদা করে না; দুই symbol (0=লাল, 1=নীল) | B2 | p13 Figure 2 |
| **AND 4 point** | শুধু (1,1)=1 | linearly separable | B2 | p13 table |
| **OR 4 point** | শুধু (0,0)=0 | linearly separable | B2 | p13 table |
| **ReLU, x∈[−4,4]** | (−4,0),(−2,0),(0,0),(1,1),(2,2),(4,4) | x<0 flat 0, x≥0 y=x | B7 | p16 Figure 3 |
| **ReLU′** | x<0 → 0; x>0 → 1; x=0 convention 0 | দুই ধাপ; z=0-তে jump | B7 | p17 (সূত্র), sir-এর sketch |
| **Sigmoid** | (−2,0.1192),(0,0.5),(1,0.7311),(2,0.8808) | S-curve 0–1, z=0-তে 0.5 | B6 | p23 table |
| Pipeline diagram | x → z=wx+b → σ → L → ∇L → SGD | block diagram | B5 | p7 Figure 2 |
| Network diagrams | 2–2–3 MLP, edge-এ initial weights | nodes ও edges | B8 | p28–38 (শেষে) |

---

## 8. Syllabus match (এই PDF → syllabus topic)

| Syllabus | এই PDF-এর page |
|---|---|
| A5 Activation (sigmoid, softmax, ReLU) | p15–17, 23–27 |
| B1 Neuron ও Feedforward | p11–12 |
| B2 XOR | p12–15 |
| B3 Entropy, CE, KL | p1–3 |
| B4 Logistic regression ও BCE | p4–8, 21–24 |
| B5 SGD ও Gradient | p6–8, 19–21 |
| B6 Output units (sigmoid/softmax) | p22–25 |
| B7 Hidden units ও ReLU | p16–17, 26–27 |
| B8 Architecture | p28–30 |
| B9 Universal Approximation | p30–31 |
| B10 Chain rule, Jacobian, Backprop | p31–38 |

---

## 9. সংখ্যা-যাচাই ও ছাপার ভুল
সব সংখ্যা computer দিয়ে আবার হিসাব করা:
- H(P)=0.6109 · H(P,Q)=0.6325 · KL=0.0216 · 0.6109+0.0216=0.6325 ✓
- −ln0.70=0.3567 · −ln0.95=0.0513 · −ln0.80=0.2231 · −ln0.10=2.3026 ✓
- Logistic SGD: grads −1, −0.5; w=0.10, b=0.05; p_new=0.5622; L=0.5759 ✓
- σ(1)=0.7311 · −ln(0.7311)=0.3133 ✓ · update: w₁=0.7538, w₂=0.4269, b=−0.7731, z=1.1614 ✓
- Softmax [0,2,1] → [0.0900, 0.6652, 0.2447]; L=0.4076 ✓ · Jacobian সব 9 entry ✓
- 2–2–3 MLP: z⁽¹⁾, h, z⁽²⁾, ∇h, ∇W⁽¹⁾, ∇W⁽²⁾, updated W/b, p_new, L_new=0.069793 সব ✓ (PDF-এর সাথে হুবহু মিলেছে)

**ছোট rounding পার্থক্য (ভুল না):**
- p_new (§4.6) PDF 0.7615, exact 0.7616; L_new PDF 0.2725, exact 0.2724।
- BCE p=0.9: exact 0.1054 (অন্য bank-এ 0.1053)।

**Notation নোট:** এই PDF-এ W⁽¹⁾ᵀx ব্যবহার (column-vector notation); p32-এ লেখা z⁽¹⁾ = W⁽¹⁾ᵀx + b⁽¹⁾; কোথাও কোথাও xᵀW লেখা, দুটো সমতুল্য। **ছাপার/সংখ্যার কোনো ভুল পাইনি।**
