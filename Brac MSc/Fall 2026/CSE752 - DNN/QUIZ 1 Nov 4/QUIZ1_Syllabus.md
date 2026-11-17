# CSE752 – Deep Neural Networks | QUIZ 1 Syllabus (Fall 2026)

**Quiz-1: Wednesday 4 Nov 2026, 7:00 PM** · 60 min · 50 marks

> QUIZ 1 folder-এর সব file দেখে বানানো। Topic-এর নাম English-এ, ব্যাখ্যা বাংলায়।

---

## 0. Scope ও Exam Format

**প্রশ্ন আসবে শুধু এই file গুলো থেকে:**

| # | File | পড়ার সময় |
|---|---|---|
| 1 | `merged_L2_GD-LR-B-W-MSE-ActF-FB Prop.pdf` (24 page) | আগে theory |
| 2 | `Deep_Learning_Quiz_Bank_L-2_L-3.pdf` (8 page) | PDF 1-এর practice |
| 3 | `Merged-KL-XOR-Grad-Arch.pdf` (38 page) | তারপর theory |
| 4 | `Deep_Learning_Chapter6_Quiz_Bank.pdf` (9 page) | PDF 3-এর practice |
| 5 | `f_x_gradient_descent.webp` | **Gradient Descent math problem** |
| + | `image (2).webp`, `image (1).webp` | sir-এর হাতে আঁকা **ReLU(z)** ও **ReLU′(z)** graph |

| Session | Type | Q | Marks |
|---|---|---|---|
| 1 | Short Q&A | 10 | 10 |
| 1 | True/False (with reason) | 10 | 10 |
| 2 | Math Problem | 2 | 10 |
| 2 | Graph (paper supplied) | 2 | 20 |
| | **Total** | | **50** |

**Notice:**
- ❌ **Forward/Backward Propagation-এর math আসবে না।** শুধু concept (Short Q/T-F) আসতে পারে।
- Session 1: মোবাইল নিষেধ, open-book না। Session 2: মোবাইল/calculator শুধু calculation-এর জন্য।
- Pencil/eraser/sharpener আনো।

**Bank-এর সংখ্যা (PDF থেকে গুনে):**

| Bank | Short Q | T/F | Math | Graph |
|---|---|---|---|---|
| L-2/L-3 | 19 | 19 *(header-এ 25 লেখা)* | 11 | 5 *(header-এ 10 লেখা)* |
| Chapter 6 | 19 | 16 | 16 | 6 |

> L-2/L-3 bank-এর graph ছবির title হলো Graph 1, 2, 5, 6, 7, কিন্তু লেখায় Exercise 1–5। মানে মূল bank-এ 10টা graph ছিল; 3, 4, 8, 9, 10 নম্বর এই copy-তে নেই।

---

## 1. SYLLABUS (serial order)

### PART A — Lecture 1 & 2 (PDF 1 + PDF 2)

**A1. Machine Learning Task**
- Regression (continuous: training time, house price, temperature) বনাম Classification (discrete label: benign/malicious, cat/dog)

**A2. Linear Regression ⭐** *(PDF 1 p1–6)*
- Feature, Target, Feature vector x=[x₁,x₂]ᵀ, Weight, Bias, Parameters θ={w₁,w₂,…,b}
- ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b; উদাহরণ ŷ = 2x₁ + 3x₂ + 5
- Weight = এক unit feature বাড়লে prediction কত বদলায়; বড় weight ≠ বেশি important (scale নির্ভর)
- Bias না থাকলে ŷ=wx অবশ্যই (0,0) দিয়ে যায়; bias line/plane-কে shift করে
- Linear regression = একটা neuron, identity activation f(z)=z
- Linear model U-shaped (y=x²) fit করতে পারে না → hidden layer + nonlinearity দরকার

**A3. Residual ও MSE ⭐**
- Residual r = y − ŷ (r>0 → কম predict; r<0 → বেশি); graph-এ vertical dashed line
- MSE = (1/m) Σ(ŷ−y)²; square করলে sign cancel হয় না, বড় error বেশি শাস্তি পায়; MSE=0 মানে সব ঠিক
- Half-squared loss: L = ½(ŷ−y)², ∂L/∂ŷ = ŷ−y
- 4-run table (A,B,C,D): MSE = 0.25

**A4. Gradient Descent ⭐⭐** *(PDF 1 p5–6, PNG)*
- θ_new = θ_old − η∇L (**বিয়োগ**); η = learning rate = step size; derivative = slope
- f(x)=x², f′(x)=2x, x_new = x_old − η(2x_old) = 0.8·x_old; x₀=4, η=0.1
- Positive slope → x বাম দিকে যায়; slope ছোট → step ছোট; minimum x*=0, f(0)=0

**A5. Activation Functions ⭐⭐** *(PDF 1 p13–19, PDF 3 p15–17)*
- কেন nonlinear: linear layer stack = একটা linear layer
- ReLU = max(0,z); ReLU′: z<0 → 0, z>0 → 1, z=0 → undefined (convention 0); dying ReLU
- Sigmoid σ(z)=1/(1+e⁻ᶻ): (0,1)-এর মধ্যে, finite z-এ exact 0/1 না; σ(0)=0.5
- Softmax pₖ=e^zₖ/Σe^zⱼ: সব p-এর যোগফল 1; mutually exclusive multiclass
- Sigmoid = 1 output (Bernoulli); Softmax = প্রতি class-এ 1 output (Multinoulli)
- Task → Output activation → Loss: Regression → Linear → MSE; Binary → Sigmoid → BCE; Multiclass → Softmax → CCE

**A6. Capacity / Bias–Variance (হালকা)** *(PDF 1 p17)*
- Underfit (train ও test error বেশি) · Optimal · Overfit (train≈0, test বেশি)
- Generalization = unseen data-তে performance

**A7. Forward & Backward Propagation (শুধু concept) ⭐** *(PDF 1 p16, 20–24)*
- Forward: input → hidden → output; z, h, ŷ, loss বের করে
- Backprop: chain rule দিয়ে loss থেকে পেছনের দিকে gradient বের করে; **Backprop ≠ GD** (backprop gradient বের করে, GD update করে)
- Hidden params (w,b) ও output params (v,c) আলাদা trainable; v, w থেকে বের হয় না
- ReLU inactive (z<0, h=0) হলে ওই path-এর gradient 0 (∂L/∂v₂ = (ŷ−y)h₂ = 0)

### PART B — Chapter 6 (PDF 3 + PDF 4)

**B1. Neuron ও Feedforward Network** *(PDF 3 p11–12)*
- z=wᵀx+b, a=f(z); x=[2,3], w=[0.5,0.2], b=1 → z=2.6
- Feedforward: input→output, recurrent loop নেই; x → h → y

**B2. XOR ⭐⭐** *(PDF 3 p12–15)*
- Truth table: (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0
- Single perceptron পারে না (linearly separable না); AND, OR separable
- Hidden layer: h₁=x₁ OR x₂, h₂=x₁ AND x₂, y = h₁ AND NOT h₂
- Threshold form: h₁=step(x₁+x₂−0.5), h₂=step(x₁+x₂−1.5), y=step(h₁−h₂−0.5)
- Representation learning (x₁,x₂)→(h₁,h₂)

**B3. Entropy, Cross-Entropy, KL ⭐⭐** *(PDF 3 p1–3)*
- H(P)=−ΣP ln P; H(P,Q)=−ΣP ln Q; D_KL=ΣP ln(P/Q); **H(P,Q)=H(P)+KL**
- KL ≥ 0, P=Q → 0 (কিন্তু CE=H(P)); KL symmetric না; P fixed → CE min = KL min
- One-hot target: H(P)=0, তাই CE=KL
- Natural log (nats)

**B4. Logistic Regression ও BCE ⭐⭐** *(PDF 3 p4–8, 21–24)*
- p=σ(wᵀx+b)=P(y=1|x); p≥0.5 → class 1
- BCE = −[y ln p + (1−y) ln(1−p)]; y=1 → −ln p; y=0 → −ln(1−p)
- Confidently wrong হলে loss বড়
- Gradient: ∂L/∂z=p−y, ∂L/∂w=(p−y)x, ∂L/∂b=p−y
- Cost = negative log-likelihood (maximum likelihood)

**B5. SGD ও Gradient-Based Learning** *(PDF 3 p6–8, 19–21)*
- θ_new = θ_old − ηĝ; একটা update সবসময় loss কমায় না
- Training loop: Forward → Cost → Gradient → Update
- Gradient (scalar loss) বনাম Jacobian (vector output)

**B6. Output Units** *(PDF 3 p22–25)*
- Sigmoid → binary (Bernoulli); Softmax → multiclass
- Softmax + CE: ∂L/∂zₖ = pₖ − yₖ
- একাধিক label একসাথে সত্য হলে আলাদা sigmoid

**B7. Hidden Units ও ReLU** *(PDF 3 p16–17, 26–27)*
- ReLU কেন জনপ্রিয়: সহজ, সস্তা, positive side-এ derivative 1 (saturate করে না)
- Limitation: dying ReLU; ReLU generalization guarantee করে না

**B8. Architecture Design ⭐** *(PDF 3 p28–30)*
- 2–2–3 MLP: 2 input, 2 hidden (ReLU), 3 output (Softmax); fully connected
- **Parameter = Σ(in×out + out)** = (4+2)+(6+3) = **15**
- Width, depth, connectivity validation দিয়ে ঠিক হয়; বেশি বড় → overfit/costly

**B9. Universal Approximation Theorem** *(PDF 3 p30–31)*
- Nonlinear activation + enough hidden units → অনেক function approximate করতে পারে
- ❌ GD সঠিক parameter পাবে তার guarantee নেই; ❌ generalization নেই; ❌ deeper সবসময় better না

**B10. Chain Rule, Jacobian, Backprop (concept)** *(PDF 3 p33–36)*
- dL/dx=(dL/du)(du/dx); u=2x, L=u², x=3 → 24
- ∇ₓL=Jᵀ∇ᵤL; softmax Jacobian ∂pᵢ/∂zⱼ=pᵢ(δᵢⱼ−pⱼ)
- Backprop = chain rule + local Jacobian; optimizer update করে
- ReLU Jacobian: z>0 → 1, z<0 → 0

---

## 2. Question Type অনুযায়ী কী পারতে হবে

**Short Q&A + T/F:** A1–B10-এর সব concept। দুই bank-এর Short Q (19+19) আর T/F (19+16) পুরো পড়ো।

**Math (2টা):**
- GD table (নিচে) নিজে হাতে
- Linear regression prediction/residual/MSE; ReLU, sigmoid মান
- Entropy/CE/KL (P=(0.7,0.3), Q=(0.6,0.4) → 0.6109 / 0.6325 / 0.0216)
- BCE (p=0.8, 0.1); softmax + CE; logistic regression এক SGD step; parameter count; chain rule
- Bank-এর সব Math (L-2/L-3 Problem 1–11, Ch6 C1–C16)। ❌ forward/back prop numerical বাদ।

**Gradient Descent PNG, সঠিক মান** (x₀=4, η=0.1):

| t | xₜ | f′(xₜ)=2xₜ | f(xₜ)=xₜ² |
|---|---|---|---|
| 0 | 4.0000 | 8.0000 | 16.0000 |
| 1 | 3.2000 | 6.4000 | 10.2400 |
| 2 | 2.5600 | 5.1200 | 6.5536 |
| 3 | 2.0480 | 4.0960 | 4.1943 |
| 4 | 1.6384 | 3.2768 | 2.6844 |
| 5 | 1.3107 | 2.6214 | 1.7180 |
| 6 | 1.0486 | 2.0972 | 1.0995 |
| 7 | 0.8389 | 1.6777 | 0.7037 |
| 8 | 0.6711 | 1.3422 | 0.4504 |
| 9 | 0.5369 | 1.0737 | 0.2882 |

⚠️ PNG-তে f(xₜ) কলামে t=5, 6, 8, 9-এ ছাপার ভুল আছে (1.7189, 1.1005, 0.4503, 0.2883)। উপরের মান সঠিক।

**Graph (2টা, 20 marks)** — প্রতিটায় axis label, scale, key point, curve shape, special point দাও:

| Graph | Key points | Source |
|---|---|---|
| f(x)=x², x∈[−2,2] | (−2,4),(−1,1),(0,0),(1,1),(2,4); U-shape; minimum label | L-2/L-3 Ex.1 |
| GD on x² | x₀=4, 3.2, 2.56, 2.048, 1.6384 curve-এর উপর; arrow বাম দিকে | Ex.2, PNG |
| Residual ŷ=x+1, point (2,2) | predicted (2,3); dashed vertical; r=−1 | Ex.3 |
| ReLU(z), z∈[−4,4] | (−4,0),(−2,0),(0,0),(1,1),(2,2),(3,3),(4,4) | Ex.4, Ch6 D1, sir-এর sketch |
| **ReLU′(z), z∈[−4,4]** | z≤0 → 0 (z=0-তে dot); z>0 → 1; z=0-তে jump | sir-এর sketch |
| Sigmoid | (−2,0.1192),(0,0.5),(1,0.7311),(2,0.8808); S-curve; 0 ও 1 asymptote | Ex.5, Ch6 D2 |
| BCE y=1, L=−ln p | (0.1,2.3026),(0.2,1.6094),(0.3,1.2040),(0.4,0.9163),(0.5,0.6931),(0.6,0.5108),(0.7,0.3567),(0.8,0.2231),(0.9,0.1054); নামতে থাকা | Ch6 D3 |
| BCE দুই curve (y=1: −ln p, y=0: −ln(1−p)) | দুটো পরস্পর উল্টো; p=0.5-এ cross | PDF 3 p4 |
| XOR 4 point | (0,0)=0,(0,1)=1,(1,0)=1,(1,1)=0; আলাদা symbol; কোনো এক line আলাদা করে না | Ch6 D4 |
| AND 4 point | শুধু (1,1)=1; separable | Ch6 D5 |
| OR 4 point | শুধু (0,0)=0; separable | Ch6 D6 |
| Bias effect ŷ=2x vs ŷ=2x+5 | parallel; (0,0) ও (0,5) | PDF 1 p4–5 *(bank-এ ছবি নেই)* |

*(L-2/L-3 bank-এর নেই-হওয়া Graph 3, 4, 8, 9, 10-এর জায়গায় আমি অতিরিক্ত বানিয়েছি: Bias, Softmax bar [2,1,0]→0.665/0.245/0.090, BCE, GD loss vs iteration, এক SGD step-এ loss 0.6931→0.5759। reference: `Generated_Graphs_6-10.png`। এগুলো sir-এর original question না।)*

---

## 3. মনে রাখার বিষয়
- GD-তে **বিয়োগ**; Backprop ≠ GD; KL symmetric না; XOR separable না; UAT ≠ training guarantee
- ReLU′: negative → 0, positive → 1, z=0 → convention 0
- ReLU(−3)=0 (−3 না); sigmoid exact 0/1 দেয় না
- 2–2–3 MLP → 15 parameter
- Calculator শুধু Session 2-তে
