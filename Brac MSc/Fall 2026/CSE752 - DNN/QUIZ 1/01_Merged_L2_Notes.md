# PDF 1 — merged_L2 (Gradient Descent · Linear Regression · Bias/MSE · Activation · Fwd/Back Prop)

> **Source:** `merged_L2_GD-LR-B-W-MSE-ActF-FB Prop.pdf` (24 page, লেখক: Refai Arafat Rossi, Oct 2026)
> পুরো PDF পড়ে topic-wise note। প্রতিটা সংখ্যা computer দিয়ে আবার হিসাব করে মিলানো।
> Syllabus tag (A1…B10) = `QUIZ1_Syllabus.md`-এর topic।

## 0. PDF-এর গঠন (page map)

| Page | কী আছে | Syllabus |
|---|---|---|
| p1–6 | Linear Regression deck (feature, weight, bias, residual, MSE, GD rule) *(deck-এর title "Gradient Descent – Linear regression")* | A1–A4 |
| p7–12 | **একই content আবার** (Linear Regression deck-এর দ্বিতীয় copy) | A1–A4 |
| p13–19 | Activation Functions & Nonlinear Learning (ReLU, sigmoid, softmax, bias–variance, numerical forward+backprop) | A5, A6, A7 |
| p20–24 | Forward & Back Propagation (output-layer parameters v₁, v₂, c, numerical example) | A7 |

> ⚠️ p1–6 আর p7–12 প্রায় হুবহু এক। একবার পড়লেই হবে।
> ⚠️ **Fwd/Back prop-এর numerical math (p15–17, p20–24) notice অনুযায়ী আসবে না।** শুধু concept পড়ো। নিচে বুঝে রাখার জন্য ধাপগুলো দেওয়া আছে।

---

## 1. Linear Regression (p1–6)

### 1.1 Problem
Model training time (minutes) predict করব দুই feature দিয়ে:
- x₁ = training epochs-এর সংখ্যা
- x₂ = batch size (এক unit = 16 samples)

Learned model: **ŷ = w₁x₁ + w₂x₂ + b**, উদাহরণ w₁=2, w₂=3, b=5 → **ŷ = 2x₁ + 3x₂ + 5**

### 1.2 ML Task: Regression বনাম Classification `[A1]`
| | Output | উদাহরণ |
|---|---|---|
| Regression | continuous (ŷ ∈ ℝ) | training time (minutes), housing price ($), GPU temperature (°C) |
| Classification | discrete label | Cat vs Dog, Benign vs Malignant |

### 1.3 Feature, Target, Feature vector `[A2]`
- **Feature (x):** model-এর input attribute (x₁=epochs, x₂=batch units)
- **Target (y):** true ground-truth value (observed training time)
- উদাহরণ: x₁=10, x₂=4, y=37 → ŷ = 2(10)+3(4)+5 = 20+12+5 = **37** → Error y−ŷ = 0 (perfect)
- **Feature vector** x = [x₁, x₂]ᵀ = [10, 4]ᵀ; n feature হলে x ∈ ℝⁿ। প্রতি sample একটা বিন্দু n-dimensional space-এ।

### 1.4 Weight, Bias, Parameters `[A2]`
- **Weight wⱼ** = এক unit xⱼ বাড়লে ŷ কত বদলায় (অন্য feature fixed)
  - w₁=2 → 1 epoch বাড়লে +2 মিনিট; w₂=3 → 1 batch unit বাড়লে +3 মিনিট
- ⚠️ **বড় weight ≠ বেশি important feature।** Scale matters (যেমন age in years বনাম income in dollars)। তুলনার আগে feature normalization দরকার।
- **Bias b** = additive parameter, input-নিরপেক্ষভাবে output shift করে
- **Parameters θ = {w₁, …, wₙ, b}** = সব learnable মান; weight ও bias হলো θ-র subset

### 1.5 Vector notation ও Neuron view `[A2]`
- w = [w₁,w₂]ᵀ, x = [x₁,x₂]ᵀ, **wᵀx = w₁x₁ + w₂x₂** → **ŷ = wᵀx + b**
- **Linear regression = একটা neuron, identity activation (f(z)=z)**
  - Artificial neuron: z = wᵀx + b, a = f(z)
  - Linear regression: ŷ = wᵀx + b (f = identity)
- (wᵀx + b) হলো deep network-এর layer-এর মৌলিক building block।

### 1.6 Dataset evaluation ও MSE `[A3]`
ŷ = 2x₁ + 3x₂ + 5, 4টা experiment:

| Exp | Epochs x₁ | Batch x₂ | Actual y | Predicted ŷ | Error (y−ŷ) | Squared |
|---|---|---|---|---|---|---|
| A | 2 | 2 | 15 | 2(2)+3(2)+5 = 15 | 0 | 0 |
| B | 4 | 3 | 22 | 2(4)+3(3)+5 = 22 | 0 | 0 |
| C | 6 | 4 | 29 | 2(6)+3(4)+5 = 29 | 0 | 0 |
| D | 8 | 5 | 35 | 2(8)+3(5)+5 = **36** | **−1** | **1** |

**MSE = (1/m) Σ (ŷ⁽ⁱ⁾ − y⁽ⁱ⁾)² = (0+0+0+1)/4 = 0.25**

কেন square?
- +2 আর −2 cancel হয়ে 0 হয়ে যেত (square করলে হয় না)
- বড় error বেশি শাস্তি পায় (1² = 1 বনাম 5² = 25)
- MSE = 0 মানে সব prediction ঠিক

### 1.7 Residual ও geometric meaning `[A3]`
- **r⁽ⁱ⁾ = y⁽ⁱ⁾ − ŷ⁽ⁱ⁾** = actual আর predicted-এর **vertical distance**
- Point রেখার **নিচে** থাকলে r negative; উপরে থাকলে positive
- Linear regression এমন w, b খোঁজে যাতে সব point-এর squared vertical distance-এর গড় সবচেয়ে কম।
- (PDF p4-এ residual-এর ছবি আঁকার code ছাপা হয়ে গেছে, figure render হয়নি। Concept: রেখা ŷ = wx+b, একটা point (x⁽ⁱ⁾, y⁽ⁱ⁾), তার নিচে/উপরে dashed লাল vertical রেখা r⁽ⁱ⁾।)

### 1.8 Bias কেন লাগে `[A2]`
- **Bias ছাড়া (b=0):** ŷ = wx **অবশ্যই (0,0) দিয়ে যায়।** x=0 তে target y=5 হলে model পুরোপুরি ব্যর্থ।
- **Bias সহ:** ŷ = wx + b রেখাকে উপরে/নিচে shift করে (affine transformation)।
- 1D রেখা ŷ=wx+b: **w = slope, b = y-intercept**
- 2D plane ŷ = w₁x₁+w₂x₂+b: w₁,w₂ = orientation; b = plane-এর উচ্চতা (elevation)

### 1.9 Terminology table (p5)
Task = hyperparameter দিয়ে runtime predict · Feature = input attribute · Feature Vector = এক sample-এর সব input · Target = ground truth · Prediction ŷ = wᵀx+b · Weight = multiplicative parameter · Bias = additive parameter · Parameters θ={w,b} · Residual r=y−ŷ · MSE = dataset-এর গড় squared error

### 1.10 Parameter learning = optimization `[A4]`
আমরা আগে থেকে সেরা w, b জানি না → **random initialization** → **Gradient Descent** দিয়ে optimize।
- Loss: J(w₁,w₂,b) = (1/m) Σ ((w₁x₁⁽ⁱ⁾ + w₂x₂⁽ⁱ⁾ + b) − y⁽ⁱ⁾)²
- Update: **wⱼ ← wⱼ − η ∂J/∂wⱼ**, **b ← b − η ∂J/∂b**
- Flow: Input x → Prediction ŷ → MSE Loss J → Gradients ∇J → Parameter Updates
- Goal: w*, b* = argmin MSE(w, b)

### 1.11 Student exercises (p5)
- **Ex.1:** ŷ = 3x₁+2x₂+4, x=[5,3], y=25 → ŷ = 15+6+4 = **25**, e=0, e²=0
- **Ex.2:** একই model, x=[6,4], y=32 → ŷ = 18+8+4 = **30**, e = 32−30 = **2**, e² = **4**

### 1.12 Final summary (p6): Linear model → Deep Network
1. Linear regression (single identity neuron): ŷ = wᵀx + b
2. Single non-linear neuron: a = f(wᵀx + b)
3. Multi-layer deep NN: h⁽¹⁾=f₁(W⁽¹⁾x+b⁽¹⁾), h⁽²⁾=f₂(W⁽²⁾h⁽¹⁾+b⁽²⁾), …, ŷ=f_L(W⁽ᴸ⁾h⁽ᴸ⁻¹⁾+b⁽ᴸ⁾)

**Takeaway:** deep network = (wᵀx+b) অনেক layer-এ stack, মাঝে nonlinear activation।

---

## 2. Activation Functions ও Nonlinear Learning (p13–19)

### 2.1 কেন Neural Network? (Electricity demand) `[A2, A5]`
- ঠান্ডা দিনে (heating) আর গরম দিনে (AC) demand বাড়ে; আরামদায়ক দিনে সবচেয়ে কম → **U-shape**
- Input x = temperature deviation, target y = অতিরিক্ত demand; ground truth **y = x²**

| x | −2 | −1 | 0 | 1 | 2 |
|---|---|---|---|---|---|
| y = x² | 4 | 1 | 0 | 1 | 4 |

- **Model A — Linear regression** ŷ=wx+b: শুধু সরলরেখা; U-curve (y=x²) পারে না।
- **Model B — Single-layer NN** h=f(wx+b): nonlinear activation টুকরো signal মিলিয়ে curve approximate করে।
- **Model C — Deep NN** h⁽ˡ⁾=f(W⁽ˡ⁾h⁽ˡ⁻¹⁾+b⁽ˡ⁾): hierarchical, জটিল representation।
- Takeaway: linear model parabola ধরতে পারে না; nonlinear activation-সহ hidden layer পারে (universal approximation)।

### 2.2 ReLU ও Sigmoid `[A5]`
Neuron: z = wx+b, তারপর a = f(z)।

**ReLU(z) = max(0, z)**
- ReLU(−3)=0, ReLU(2.5)=2.5
- Hidden layer-এর standard choice (সহজ derivative, gradient saturation এড়ায়)
- Derivative: z>0 → 1, z<0 → 0

**Sigmoid σ(z) = 1/(1+e⁻ᶻ)**
- σ(0)=0.5, σ(2)≈0.881, σ(−2)≈0.119
- ℝ → (0,1); binary classification output-এর standard choice

### 2.3 Architecture (1-hidden-layer regression) `[A7]`
- Hidden 1: z₁ = w₁x+b₁, h₁ = ReLU(z₁)
- Hidden 2: z₂ = w₂x+b₂, h₂ = ReLU(z₂)
- Output: **ŷ = v₁h₁ + v₂h₂ + c**
- Matrix form: z⁽¹⁾=W⁽¹⁾x+b⁽¹⁾, h⁽¹⁾=ReLU(z⁽¹⁾), ŷ=W⁽²⁾h⁽¹⁾+b⁽²⁾

### 2.4 Numerical forward + backprop + update (p15–17) — ⚠️ exam-এ math আসবে না, concept বোঝার জন্য
**Setup:** x=1, y=1; w₁=1,b₁=0; w₂=0.5,b₂=0.5; v₁=v₂=0.2, c=0

| ধাপ | হিসাব | ফল |
|---|---|---|
| z₁, h₁ | (1)(1)+0 = 1, ReLU(1) | h₁ = 1 |
| z₂, h₂ | (0.5)(1)+0.5 = 1, ReLU(1) | h₂ = 1 |
| ŷ | 0.2(1)+0.2(1)+0 | **0.4** |
| error e = ŷ−y | 0.4−1.0 | −0.6 |
| Loss L = ½(ŷ−y)² | ½(0.36) | **0.18** |

**Backprop (chain rule):**
- ∂L/∂ŷ = ŷ−y = −0.6
- ∂L/∂v₁ = (−0.6)(h₁) = −0.6; ∂L/∂v₂ = −0.6; ∂L/∂c = −0.6
- ∂L/∂h₁ = (−0.6)(v₁) = −0.12; ∂L/∂z₁ = −0.12·ReLU′(1) = −0.12; ∂L/∂w₁ = −0.12·x = −0.12; ∂L/∂b₁ = −0.12

**GD update (η=0.1, θ_new = θ_old − η ∂L/∂θ):**
- w₁ = 1.0 − 0.1(−0.12) = **1.012**; w₂ = 0.5 + 0.012 = **0.512**; b₁ = 0 + 0.012 = **0.012**; b₂ = 0.5 + 0.012 = **0.512**
- v₁ = 0.2 + 0.06 = **0.26**; v₂ = **0.26**; c = 0 + 0.06 = **0.06**

**Verify (নতুন forward):** z₁ = 1.012+0.012 = 1.024 = z₂; ŷ_new = 0.26(1.024)+0.26(1.024)+0.06 = **0.5925**; L_new = ½(0.5925−1)² = **0.0830**

| | আগে | পরে | |
|---|---|---|---|
| ŷ | 0.4000 | 0.5925 | target 1.0-এর কাছে |
| L | 0.1800 | 0.0830 | **53.9% কমেছে** |

### 2.5 Capacity ও Bias–Variance `[A6]`
| | Capacity | E_train / E_test | সমস্যা |
|---|---|---|---|
| Underfitting | খুব কম | দুটোই high | High systematic bias |
| Optimal | সঠিক | দুটোই low | Good generalization |
| Overfitting | খুব বেশি | E_train≈0, E_test high | High variance |

**Expected error = Bias² + Variance + Irreducible noise**

### 2.6 Classification: Sigmoid + BCE `[A5, B4]`
- Binary target y ∈ {0,1}
- p = σ(z); z=2.0 → p = 1/(1+e⁻²) ≈ **0.881** (class 1-এর probability 88.1%)
- **BCE: L = −[y log p + (1−y) log(1−p)]**
- y=1 → L = −log p; p=0.881 → L = −log(0.881) ≈ **0.127** (সঠিক ও confident prediction-এ কম loss)

### 2.7 Task অনুযায়ী Output activation ও Loss (p18) `[A5]`
| Task | Output activation | Output range | Loss |
|---|---|---|---|
| Continuous regression | Linear / Identity f(z)=z | (−∞, ∞) | MSE |
| Binary classification | Sigmoid σ(z) | (0, 1) | Binary Cross-Entropy (BCE) |
| Multiclass classification | Softmax pᵢ | [0,1], Σpᵢ=1 | Categorical Cross-Entropy |

**Golden Rule:** hidden layer-এ nonlinear activation (যেমন ReLU) representation শেখে; **output activation task type ঠিক করে।**

### 2.8 Softmax ও Categorical CE `[A5]`
K-class (যেমন MRI tumor: Glioma, Meningioma, Pituitary): **pᵢ = e^zᵢ / Σⱼ e^zⱼ**
- Logits z=[2.0, 1.0, 0.0]ᵀ → e²≈7.389, e¹≈2.718, e⁰=1, sum=11.107
- **p = [0.665, 0.245, 0.090]**
- True class 2 (y=[0,1,0]ᵀ): **L_CCE = −log(p₂) = −log(0.245) ≈ 1.407**

### 2.9 Core equations (p18–19)
z=wᵀx+b · ReLU(z)=max(0,z) · σ(z)=1/(1+e⁻ᶻ) · pᵢ=e^zᵢ/Σe^zⱼ · MSE=(1/m)Σ(ŷᵢ−yᵢ)² · θ←θ−η∇θL

**End-to-end learning loop:** Input x → Forward pass (ŷ) → Loss L → Backprop (∇θL) → Gradient update (θ)
- Forward pass = prediction বানায়
- Loss = target-এর সাথে ফারাক মাপে
- Backprop = chain rule দিয়ে প্রতি parameter-এর gradient (error attribution)
- Gradient Descent = parameter update করে loss কমায়

---

## 3. Forward & Back Propagation — Output-layer parameters (p20–24) `[A7]`

### 3.1 মূল ভুল ধারণা এড়াও
**Output-layer weight v₁, v₂ এবং bias c, hidden parameter (w₁,w₂,b₁,b₂) থেকে *হিসাব করে বের হয় না*।**

| | Parameters | কাজ |
|---|---|---|
| Hidden layer | w₁,w₂ (input→hidden weight); b₁,b₂ (hidden bias) | x → h transformation |
| Output layer | v₁,v₂ (hidden→output weight); c (output bias) | h → ŷ transformation |

v₁, v₂, c হলো **স্বাধীন, learnable parameter**: শুরুতে random/ছোট মানে initialize হয়, backprop দিয়ে optimize হয়। (Forward pass শুরু করতে এদের numeric মান লাগেই।)

### 3.2 Numerical example (p20–24) — ⚠️ exam-এ math আসবে না
**Setup:** x₁=3, x₂=−1; w₁=1, w₂=2; b₁=b₂=1; target y=1.0 (1-to-1 connection, বোঝার সুবিধার জন্য। সাধারণ fully connected 2→2 layer-এ 4টা weight থাকে।)

**Step 1 — hidden outputs:**
- z₁ = 1(3)+1 = 4 → **h₁ = 4**
- z₂ = 2(−1)+1 = −1 → **h₂ = ReLU(−1) = 0** (deactivated)
- h = [4, 0]ᵀ

**Step 2 — output:** ŷ = v₁h₁ + v₂h₂ + c = 4v₁ + c (v₂ কিছুই contribute করে না কারণ h₂=0; c baseline shift করে)

**Step 3 — initial v₁=0.2, v₂=0.2, c=0:** ŷ = 4(0.2)+0(0.2)+0 = **0.8**; e = 0.8−1.0 = −0.2; **L = ½(0.04) = 0.02**

**Step 4 — Backprop (output parameter):**
- ∂L/∂ŷ = ŷ−y = −0.2
- ∂L/∂v₁ = (ŷ−y)h₁ = (−0.2)(4) = **−0.8**
- ∂L/∂v₂ = (ŷ−y)h₂ = (−0.2)(0) = **0.0**
- ∂L/∂c = ŷ−y = **−0.2**

**Step 5 — Update (η=0.1):** v₁ = 0.2−0.1(−0.8) = **0.28**; v₂ = 0.2−0 = **0.20** (অপরিবর্তিত!); c = 0−0.1(−0.2) = **0.02**

**Step 6 — Verify:** ŷ_new = 0.28(4)+0.20(0)+0.02 = **1.14**; e_new = +0.14; L_new = ½(0.14)² = **0.0098**

| | আগে | পরে | |
|---|---|---|---|
| ŷ | 0.8000 | 1.1400 | target 1.0-এর দিকে |
| L | 0.0200 | 0.0098 | **51.0% কমেছে** |

### 3.3 শিক্ষণীয় বিষয়
1. **Parameter separation:** input→hidden (wᵢ,bᵢ) feature representation (hᵢ) ঠিক করে; output layer (vᵢ,c) ঠিক করে সেগুলো কীভাবে মিশে ŷ হয়।
2. **Trainable:** output parameter স্বাধীন learnable, input weight থেকে derive হয় না।
3. **Gradient masking:** neuron-এর activation 0 (h₂=0) হলে তার outgoing weight-এর gradient 0 (∂L/∂v₂=0) → ওই connection-এর update সাময়িকভাবে থামে। **Inactive neuron error পেছনে পাঠায় না।**
4. **Core learning loop:** Inputs x → Hidden h → Output ŷ → Loss L → Gradients ∇L → Updates θ_new

---

## 4. Gradient Descent math — GD problem ও PNG

> PDF 1-এর GD rule (p5: wⱼ←wⱼ−η∂J/∂wⱼ) + `f_x_gradient_descent.webp`-এর সম্পূর্ণ সমাধান:

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

## 5. Graph table (এই PDF-এ ও PDF-এর topic-এর graph)

> এই PDF-এর figure সব TikZ code ছাপা (render হয়নি): residual diagram (p4), neuron/network diagram (p3, p15, p23)। Data graph নেই। নিচে topic অনুযায়ী যে graph আসতে পারে:

| Graph | Key points | Curve/বৈশিষ্ট্য | Syllabus | কোথায় |
|---|---|---|---|---|
| f(x)=x², x∈[−2,2] | (−2,4),(−1,1),(0,0),(1,1),(2,4) | U-shape, minimum (0,0), y-axis symmetric | A4 | p13 table; PDF 2 Ex.1 |
| GD on x² | x₀=4, 3.2, 2.56, 2.048, 1.6384 (f=16, 10.24, 6.5536, 4.1943, 2.6844) | dot curve-এর উপর, তীর বাম দিকে, ধাপ ছোট হচ্ছে | A4 | PNG; PDF 2 Ex.2 |
| Residual: ŷ=wx+b, point (xⁱ,yⁱ) | উদাহরণ ŷ=x+1, observed (2,2), predicted (2,3), r=−1 | dashed vertical, point রেখার নিচে → r negative | A3 | p4; PDF 2 Ex.3 |
| Bias effect: ŷ=2x vs ŷ=2x+5 | (0,0) ও (0,5); (1,2)/(1,7); (2,4)/(2,9) | parallel রেখা; একটা origin দিয়ে যায়, অন্যটা y-axis কাটে 5-এ | A2 | p4 (concept); *ছবি PDF-এ নেই* |
| ReLU, z∈[−4,4] | (−4,0),(−2,0),(0,0),(1,1),(2,2),(3,3),(4,4) | negative → flat 0; positive → y=z | A5 | p14; PDF 2 Ex.4 |
| ReLU′(z), z∈[−4,4] | z≤0 → 0; z>0 → 1 | z=0-তে jump; dot | A5 | sir-এর sketch `image (1).webp` |
| Sigmoid | (−2,0.119),(0,0.5),(2,0.881) | S-curve (0,1)-এর মধ্যে | A5 | p14; PDF 2 Ex.5 |
| Softmax bar, logits [2,1,0] | 0.665, 0.245, 0.090 | সবচেয়ে বড় logit-এর bar উঁচু; যোগফল 1 | A5 | p18 (generated bar) |
| BCE y=1: −ln p | (0.1,2.3026) … (0.9,0.1054) | নামতে থাকা curve | B4 | PDF 3/PDF 4 |

---

## 6. Syllabus match (এই PDF → syllabus topic)

| Syllabus | এই PDF-এর page |
|---|---|
| A1 ML Task | p2 (§1.2) |
| A2 Linear Regression | p1–5 (feature, weight, bias, parameters, neuron view) |
| A3 Residual & MSE | p4 (table, MSE=0.25, residual) |
| A4 Gradient Descent | p5 (rule), PNG, §4 |
| A5 Activation (ReLU, Sigmoid, Softmax) | p14, 17–18 |
| A6 Capacity/Bias–Variance | p17 |
| A7 Forward & Backprop (concept) | p16, p20–24 |
| B4 BCE | p17 (§2.6) |

## 7. সংখ্যা-যাচাই ও ছাপার ভুল
- p4 MSE = 0.25 ✓ · Exercise 1,2 (25/30, e²=0/4) ✓ · p15 ŷ=0.4, L=0.18 ✓ · p16 updates (1.012, 0.512, 0.012, 0.512, 0.26, 0.06) ✓
- p17 ŷ_new=0.5925, L_new=0.0830 ✓ (0.08303), reduction 53.9% ✓
- p17 BCE: −log(0.881)=0.1267≈0.127 ✓ · p18 softmax [0.665,0.245,0.090] ✓, −log(0.245)=1.407 ✓
- p22–23: ŷ=0.8, L=0.02, ∂L/∂v₁=−0.8, v₁=0.28, ŷ_new=1.14, L_new=0.0098 ✓; reduction 51.0% ✓
- **ছাপা সমস্যা (সংখ্যার ভুল না):** TikZ diagram code ও "0.5" উপ-শিরোনামের চিহ্ন text হিসেবে ছাপা হয়ে গেছে (p3, p4, p15, p23)। এতে কোনো সংখ্যা/সূত্র ভুল হয়নি।
- **ছোট অসঙ্গতি:** p15-এ log (প্রকৃতপক্ষে ln, natural log) লেখা; BCE-তে natural log ধরো।
- **Deck-এর title:** "Gradient Descent – Linear regression" কিন্তু p1–6-এ GD-র নতুন কিছু নেই, শুধু Linear regression + শেষে GD rule/flow।
