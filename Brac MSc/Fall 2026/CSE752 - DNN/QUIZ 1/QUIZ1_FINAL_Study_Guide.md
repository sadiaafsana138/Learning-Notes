# CSE752 – Deep Neural Networks | QUIZ 1 — Final Study Guide (Fall 2026)

> **Quiz-1: Wednesday 4 Nov 2026, 7:00 PM.**
> এই syllabus সরাসরি ৪টা PDF, ২টা ছবি (PNG/webp) আর sir-এর notice পড়ে বানানো। প্রতিটা সংখ্যা PDF থেকে গুনে verify করা।
> Topic-এর নাম English-এ, ব্যাখ্যা বাংলায়।

---

## 0. Scope (sir-এর notice অনুযায়ী)

**প্রশ্ন আসবে শুধু এই ৫টা ফাইল থেকে:**

| # | ফাইল | কী আছে (verified) |
|---|---|---|
| 1 | `Deep_Learning_Quiz_Bank_L-2_L-3.pdf` (8 page) | 19 Short Q, **19 T/F** + 6 generated (header-এ 25), 11 Math, **5 Graph** + 5 generated (header-এ 10) → নিচে **Appendix A** |
| 2 | `Deep_Learning_Chapter6_Quiz_Bank.pdf` (9 page) | 19 Short Q (A1–A19), 16 T/F (B1–B16), 16 Math (C1–C16), **6 Graph** (D1–D6) + formula sheet |
| 3 | `merged_L2_GD-LR-B-W-MSE-ActF-FB Prop.pdf` (24 page) | p1–6 Gradient Descent + Linear Regression; p7–12 Linear Regression (feature/weight/bias/MSE); p13–19 Activation Functions + nonlinear learning; p20–24 Forward & Back Propagation |
| 4 | `Merged-KL-XOR-Grad-Arch.pdf` (38 page) | p1–8 KL/CE/Logistic/SGD; p9–18 Ch6 notes (feedforward, XOR, ReLU); p19–27 Gradient-based learning, output units, ReLU; p28–38 Architecture, UAT, chain rule, backprop |
| 5 | `f_x_gradient_descent.webp` | **Gradient Descent math problem** f(x)=x² (নিচে section 4.3-এ) |

**অতিরিক্ত (sir-এর নতুন announcement):** `image (1).webp` = sir-এর আঁকা **ReLU′(z)** graph, আর ReLU(z) graph। দুটোই practice করতে বলেছেন।

**Format (`image.webp`):**

| Session | Type | Q | Marks |
|---|---|---|---|
| 1 | Short Q&A | 10 | 10 |
| 1 | True/False (with reason) | 10 | 10 |
| 2 | Math Problem | 2 | 10 |
| 2 | Graph (paper supplied) | 2 | 20 |
| | **Total** | | **50** (60 min) |

**Notice-এর নিয়ম:**
- ❌ **Forward/Back Propagation-এর math problem আসবে না।** (concept আসতে পারে)
- Session 1 (Short Q&A + T/F): মোবাইল নিষেধ, open-book না।
- Session 2 (Math + Graph): মোবাইল/calculator শুধু calculation-এর জন্য।
- Pencil/eraser/sharpener আনো (page ও জায়গা কম)।
- **Graph = 20/50 marks (40%)** → graph-এ সবচেয়ে বেশি সময় দাও।

> ⚠️ L-2/L-3 bank-এর **Problem 5, 6, 7** হলো ছোট forward-pass (hidden unit + output + loss)। Notice-এ fwd/back prop math বাদ, তাই সম্ভবত আসবে না। তবে সহজ, তাই একবার করে রাখো।

---

## 1. SYLLABUS (serial order)

> ⭐ = বেশি গুরুত্বপূর্ণ

### PART A — Lecture 1 & 2 (Quiz Bank L-2/L-3 + merged_L2)

**A1. ML Task:** Regression = continuous (training time, house price, temperature); Classification = discrete label (benign/malicious).

**A2. Linear Regression ⭐**
- Feature = input attribute; Target = true value; Feature vector x=[x₁,x₂]ᵀ
- Weight = এক unit feature বাড়লে prediction কত বদলায় (অন্য feature fixed)
- Bias = line-কে origin থেকে shift করে; bias ছাড়া ŷ=wx অবশ্যই (0,0) দিয়ে যায়
- Parameters θ = {w₁, w₂, …, b}
- **ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b**
- বড় weight ≠ বেশি important feature (scale নির্ভর)
- Example: ŷ = 2x₁+3x₂+5 (+2 min/epoch, +3 min/batch unit)
- Linear regression = **একটা neuron with identity activation f(z)=z**; multi-layer network = এই (wᵀx+b) অনেক layer + nonlinear activation
- Linear model শুধু straight line fit করে; U-shaped y=x² (electricity demand, x=−2..2 → 4,1,0,1,4) পারে না → hidden layer + nonlinearity দরকার
- Task → Output activation → Loss: Regression → Linear/Identity → MSE; Binary → Sigmoid → BCE; Multiclass → Softmax → Categorical CE

**A3. Residual & MSE ⭐**
- Residual **r = y − ŷ**; r>0 → model কম predict করেছে; r<0 → বেশি
- **MSE = (1/m) Σ(ŷ−y)²**; square করলে sign cancel হয় না + বড় error বেশি শাস্তি পায়; MSE ≥ 0, সব ঠিক হলে 0
- Single sample half-squared loss: **L = ½(ŷ−y)²**, ∂L/∂ŷ = ŷ−y
- **Dataset table (merged PDF):** ŷ=2x₁+3x₂+5; A(2,2,y=15)→15, err 0; B(4,3,22)→22; C(6,4,29)→29; D(8,5,35)→36, err −1, sq 1 → **MSE = (0+0+0+1)/4 = 0.25**
- **Exercise (merged PDF):** ŷ=3x₁+2x₂+4: x=[5,3], y=25 → ŷ=25, e=0, e²=0; x=[6,4], y=32 → ŷ=30, e=2, e²=4
- Residual = actual ও predicted-এর vertical distance (graph-এ dashed line)

**A4. Gradient Descent ⭐⭐**
- **θ_new = θ_old − η∇L** (বিয়োগ, যোগ না)। η = learning rate = step size
- f(x)=x², f′(x)=2x, x₀=4, η=0.1: x₁=3.2, x₂=2.56, x₃=2.048, x₄=1.6384 → 0
- Derivative = local slope; positive slope হলে x বাম দিকে যায়; slope ছোট হলে step ছোট

**A5. Activation Functions ⭐⭐**
- Nonlinearity কেন: linear layer stack = একটা linear layer
- **ReLU = max(0,z)**: ReLU(−3)=0, ReLU(0)=0, ReLU(2.5)=2.5; z>0 → derivative 1; z<0 → derivative 0; **ReLU′(0): mathematically undefined, convention 0** (sir-এর graph-এ z=0 তে 0)
- Dying ReLU: negative region-এ gradient blocked
- **Sigmoid = 1/(1+e⁻ᶻ)**: (0,1)-এর মধ্যে, কখনো exact 0/1 না; σ(0)=0.5, σ(2)≈0.881, σ(−2)≈0.119, σ(1)≈0.7311
- **Softmax**: pₖ=e^zₖ/Σe^zⱼ, sum=1, mutually exclusive multiclass; [2,1,0] → [0.665, 0.245, 0.090]
- Sigmoid = 1 output (class-1 probability); Softmax = প্রতি class-এ 1 output
- Common activations (list): Step, Sigmoid, tanh, ReLU, Leaky ReLU, Softmax। Sigmoid চরম মানে saturate করে (gradient ছোট)
- ReLU আরও উদাহরণ: ReLU(5)=5, ReLU(2.7)=2.7, ReLU(−8.4)=0, ReLU(−2.5)=0, ReLU(−4)=0, ReLU(3.5)=3.5; table z=−2,−0.5,0 → 0; z=0.5→0.5; z=2→2
- Sigmoid table: z=−2→0.1192, 0→0.5, 1→0.7311, 2→0.8808
- Softmax = Multinoulli/categorical; sigmoid = Bernoulli। একসাথে একাধিক label সত্য হলে আলাদা sigmoid, softmax না
- Logits = softmax-এর আগের score, probability না, যেকোনো real হতে পারে

**A5b. Capacity / Bias–Variance (merged_L2 p17) – হালকা**
- Underfitting: capacity কম; E_train high, E_test high; high bias
- Optimal: E_train low, E_test low; good generalization
- Overfitting: capacity বেশি; E_train≈0, E_test high; high variance
- Expected error = Bias² + Variance + Irreducible noise
- Generalization = unseen data-তে ভালো performance; ReLU generalization guarantee করে না (data, capacity, architecture, validation-ও লাগে)

**A6. Forward & Back Propagation (শুধু concept) ⭐**
- Forward: input → hidden → output; z, h, ŷ, loss বের করে
- Backprop: chain rule দিয়ে loss থেকে পেছনে gradient বের করে। **Backprop ≠ GD** (backprop gradient *calculate*, GD *update*)
- Chain rule কেন: parameter loss-কে intermediate step দিয়ে প্রভাবিত করে
- Hidden params (w,b) আর output params (v,c) আলাদা trainable; v, w থেকে বের হয় না
- ReLU inactive (z<0) হলে path blocked

### PART B — Chapter 6 (Quiz Bank Ch6 + Merged-KL)

**B1. Neuron & Feedforward Network:** z=wᵀx+b, a=f(z); x=[2,3], w=[0.5,0.2], b=1 → z=2.6. Feedforward = input→output, recurrent loop নেই.

**B2. XOR ⭐⭐:** (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0। Single perceptron পারে না (linearly separable না)। AND, OR separable। Hidden layer: h₁=x₁ OR x₂, h₂=x₁ AND x₂, y=h₁ AND NOT h₂। Example: x=[2,1] → z₁=2, z₂=1 → h=[2,1]ᵀ.
- XOR = exclusive OR (দুই input আলাদা হলে 1)। Perceptron: y=1 if z>0 else 0; decision boundary w₁x₁+w₂x₂+b=0 (2D-তে সরলরেখা)
- **Threshold-neuron construction (merged PDF p14–15):** step(z)=1 if z>0 else 0; **h₁=step(x₁+x₂−0.5) (OR), h₂=step(x₁+x₂−1.5) (AND), y=step(h₁−h₂−0.5)**; চার case: (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0
- Hidden table: (x₁,x₂)→(h₁,h₂,y): (0,0)→(0,0,0); (0,1)→(1,0,1); (1,0)→(1,0,1); (1,1)→(1,1,0)
- Representation learning: (x₁,x₂) → (h₁,h₂)
- Student-pass example: z=2x₁+3x₂−5 (linear model, decision boundary)

**B3. Entropy, CE, KL ⭐⭐:** H(P)=−ΣP ln P; H(P,Q)=−ΣP ln Q; D_KL=ΣP ln(P/Q); **H(P,Q)=H(P)+KL**। KL≥0, P=Q → 0 (কিন্তু CE=H(P))। KL symmetric না। P fixed হলে CE min = KL min। One-hot entropy = 0। P=(0.7,0.3), Q=(0.6,0.4) → 0.6109, 0.6325, 0.0216।
- Q=P=(0.7,0.3) হলে: CE=0.6109, KL=0 (table)। **One-hot P হলে H(P)=0, তাই CE = KL**
- One-hot: p=0.70 → −ln0.70=0.3567; p=0.95 → 0.0513
- Cross-entropy = target-এর weight দিয়ে model-এর log probability; confident wrong prediction-কে বেশি শাস্তি দেয়

**B4. Logistic Regression & BCE ⭐⭐:** p=σ(wᵀx+b)=P(y=1|x); **BCE = −[y ln p + (1−y)ln(1−p)]**; y=1 → −ln p। p=0.8: y=1 → 0.2231, y=0 → 1.6094; p=0.1,y=1 → 2.3026। Gradient: ∂L/∂z=p−y, ∂L/∂w=(p−y)x, ∂L/∂b=p−y। SGD step (x=2,y=1,w=b=0,η=0.1): w=0.10, b=0.05, p=0.5622, loss 0.6931→0.5759।
- Classification rule: ŷ=1 যদি p≥0.5, নাহলে 0 (threshold বদলানো যায়)। Training probability p দিয়ে, শুধু 0/1 দিয়ে না
- BCE table (y=1): p=0.95→0.0513, 0.80→0.2231, 0.50→0.6931, 0.10→2.3026। y=0 হলে L=−ln(1−p)
- **Logistic example 2 (merged PDF p23–24):** h=[2,1], z=0.7h₁+0.4h₂−0.8 = 1 → p=σ(1)=0.7311, L=0.3133; ∂L/∂z=p−y=−0.2689; η=0.1 → w₁:0.7→0.7538, w₂:0.4→0.4269, b:−0.8→−0.7731; নতুন z≈1.1614, p≈0.7615, L≈0.2725
- Neural network = hidden layer representation h শিখে তারপর logistic regression p=σ(wᵀh+b); standard logistic regression সরাসরি x ব্যবহার করে
- Cost (maximum likelihood): J(θ)=−E[log p_model(y|x;θ)] = negative log-likelihood; sigmoid+CE = Bernoulli NLL
- Training loop: Forward pass → Cost → Gradient → Update, repeat

**B5. SGD & Gradient:** θ_new=θ_old−ηĝ। Gradient = loss-এর sensitivity/direction। Gradient (scalar loss) vs Jacobian (vector output)। Backprop = chain rule + local Jacobian; optimizer update করে.

**B6. Output Units:** Sigmoid → Bernoulli; Softmax → multiclass। Softmax+CE: ∂L/∂zₖ=pₖ−yₖ। Logits [0,2,1] → p=[0.090,0.665,0.245], L=0.4076, δ=[0.0900,−0.3348,0.2447].

**B7. ReLU (hidden units):** simple, সস্তা (comparison, exponential না), piecewise linear হলেও layer জুড়ে nonlinear, positive side-এ derivative 1 তাই saturate করে না; dying ReLU limitation। ReLU(x)=0 (x<0), x (x≥0); ReLU′: x<0→0, x>0→1, x=0 → classical অর্থে differentiable না, subgradient convention সাধারণত 0.

**B8. Architecture ⭐:** 2–2–3 MLP, fully connected। **Params = Σ(in×out + out)** = (4+2)+(6+3) = **15**। বেশি বড় → overfit/costly; ছোট → underfit; validation দিয়ে ঠিক করা হয়।
- Design decision: input width (2), hidden width (2), depth (1 hidden layer), output width (3), connectivity (fully connected)
- Hidden layer: ReLU; output layer: Softmax (3 mutually exclusive class: Benign, DDoS, Port scan)
- Layer formula h = g(Wᵀx + b)

**B9. Universal Approximation:** representation capability, GD সঠিক parameter পাবে এর guarantee **না**; deeper সবসময় better ≠ সত্য।
- **UAT-এর ৩টা limitation:** (1) training algorithm সঠিক parameter পাবে তার guarantee নেই; (2) unseen data-তে generalization guarantee নেই; (3) deeper সবসময় better/সহজে optimize হয় না
- এক hidden layer তাত্ত্বিকভাবে যথেষ্ট কিন্তু অনেক unit লাগতে পারে; deep network hierarchical function কম parameter-এ represent করতে পারে
- Depth ও width = hyperparameter, data দিয়ে evaluate করতে হয়

**B10. Chain Rule:** dL/dx=(dL/du)(du/dx); u=2x, L=u², x=3 → 12×2=**24**। Vector: ∇ₓL=Jᵀ∇ᵤL.
- Jacobian J=∂y/∂x (m input, n output → n×m matrix)। Softmax Jacobian: ∂pᵢ/∂zⱼ=pᵢ(δᵢⱼ−pⱼ)। ∂L/∂pᵢ=−yᵢ/pᵢ, চেইন করলে ∂L/∂zⱼ=pⱼ−yⱼ
- Backprop efficient কারণ প্রতি layer উপরের layer-এর গণনা reuse করে; backprop = গ্রাফে chain rule + local Jacobian
- ReLU Jacobian = diag(1 বা 0); δ⁽¹⁾=∇ₕL ⊙ ReLU′(z); negative pre-activation → gradient ওই input-এর জন্য blocked
- (2–2–3 MLP-এর পুরো backprop ও SGD হিসাব merged PDF p32–38-এ আছে; notice অনুযায়ী এর math আসবে না, concept পড়ো। Loss 0.4076→0.0698, DDoS prob 66.52%→93.26%)

---

## 2. Short Q&A (10 × 1 mark) — bank থেকে গুনে নেওয়া list

**L-2/L-3 bank (Q1–Q19):** regression vs classification; feature vs target; weight; bias কেন; feature vector; parameters; residual ও sign; MSE-তে square কেন; GD কী করে; derivative কী বলে; learning rate; ReLU আচরণ; ReLU limitation (backprop-এ); sigmoid কী/কোথায়; σ(0)=0.5 কেন; hidden vs output parameter; forward prop কী calculate করে; backprop কী calculate করে; chain rule কেন জরুরি.

**Ch6 bank (A1–A19):** entropy কী মাপে; CE vs KL; H(P,Q)=H(P)+KL; Q=P হলে KL; logistic regression নাম কেন; sigmoid-এর কাজ; BCE কী; gradient কী তথ্য দেয়; SGD gradient কীভাবে ব্যবহার করে; forward vs backprop; neuron কী compute করে; feedforward network; perceptron XOR পারে না কেন; hidden layer XOR কীভাবে; nonlinear activation কেন; ReLU কেন জনপ্রিয়; ReLU limitation (dying); sigmoid vs softmax; gradient/Jacobian/backprop/optimizer সম্পর্ক.

## 3. True/False (10 × 1 mark) — trap list

> L-2/L-3 bank-এ header-এ 25 T/F, কিন্তু আছে 19। বাকি 6টা (T/F 20–25) আমি generate করেছি: **Appendix A**। নিচের শেষ ৬ সারি সেগুলো (Generated চিহ্নিত)।

| Statement | উত্তর |
|---|---|
| Target = model-এর input attribute | False (feature input; target true value) |
| বড় weight = বেশি important | False |
| ŷ=wx (no bias) (0,0) দিয়ে যায় | True |
| Squaring error cancel হতে দেয় | False |
| MSE=0 যখন সব prediction ঠিক | True |
| GD gradient যোগ করে | False |
| x₁ = 3.2 (x₀=4, η=0.1) | True |
| ReLU(−3)=−3 | False (0) |
| ReLU z<0-তে derivative 0 | True |
| Sigmoid finite z-এ ঠিক 0/1 দেয় | False |
| σ(0)=0.5 | True |
| Softmax sum=1; mutually exclusive-এ ব্যবহার | True |
| v₁,v₂ হলো w₁,w₂ থেকে calculated | False |
| Backprop = GD | False |
| KL symmetric | False |
| KL ≥ 0, P=Q হলে 0 | True |
| CE min = KL min (P fixed) | True |
| One-hot entropy = 0 | True |
| y=1 হলে BCE = −ln p | True |
| XOR linearly separable | False |
| AND/OR linearly separable | True |
| Single sigmoid = 3-class softmax structure | False |
| 2–2–3 MLP-এ 15 parameter | True |
| UAT মানে GD সঠিক parameter পাবে | False |
| Deeper সবসময় better/সহজে optimize | False |
| Backprop নিজেই optimizer | False |
| Hidden ReLU z<0 → gradient path blocked | True |
| *(Generated)* Linear regression = single neuron, identity activation | True |
| *(Generated)* Linear layers stack (no activation) y=x² represent করতে পারে | False |
| *(Generated)* ½(ŷ−y)² → ∂L/∂ŷ=ŷ−y | True |
| *(Generated)* errors 0,0,0,−1 → MSE=1 | False (0.25) |
| *(Generated)* h₂=0 হলে ∂L/∂v₂=0 | True |
| *(Generated)* Output activation task অনুযায়ী (linear/sigmoid/softmax) | True |

## 4. Math (2 × 5 marks)

### 4.1 Bank-এর সব math (calculator শুধু calculation-এ)
**L-2/L-3 Problems 1–11:** (1) ŷ=2x₁+3x₂+5 at (2,2)=15 · (2) y=17: r=2, r²=4 · (3) GD x₁=3.2, f=10.24 · (4) ReLU(−3,0,2.5) · (5) *forward pass ŷ=0.4* · (6) *L=½(0.4−1)²=0.18* · (7) *inactive ReLU ŷ=0.8* · (8) σ(0)=0.5, σ(2)≈0.881 · (9) BCE p=0.8 y=1/0 · (10) softmax [2,1,0] · (11) CCE class 2: −ln0.245=1.407. (*5–7 = ছোট fwd pass, ঝুঁকি কম*)

**Ch6 C1–C16:** C1 entropy 0.6109 · C2 CE 0.6325 · C3 KL 0.0216 · C4 −ln0.70=0.3567 vs −ln0.95=0.0513 · C5 z=0, p=0.5 · C6 BCE 0.2231 vs 2.3026 · C7 gradients −1, −0.5; w=0.10, b=0.05 · C8 p=0.5622, loss 0.5759 · C9 z=2.6 · C10 ReLU(−3,0,2.7) · C11 h=[2,1] · C12 σ(1)=0.7311, L=0.3133 · C13 softmax [0,2,1] · C14 L=0.4076, δ=p−y · C15 params=15 · C16 chain rule=24.

**শুধু merged PDF-এ আছে (bank-এ নেই) — এগুলোও করে রাখো:**
- MSE 4-run table = 0.25; exercise ŷ=3x₁+2x₂+4 ([5,3]→e²=0; [6,4], y=32 → e=2, e²=4) (merged_L2 p4–5)
- σ(2)=0.881, BCE p=0.881,y=1 → −log(0.881)≈0.127 (merged_L2 p17)
- XOR threshold neurons: h₁=step(x₁+x₂−0.5), h₂=step(x₁+x₂−1.5), y=step(h₁−h₂−0.5) চার case-এ check (merged-KL p14–15)
- Logistic example 2: h=[2,1], z=0.7h₁+0.4h₂−0.8=1 → p=0.7311, L=0.3133, ∂L/∂z=−0.2689, এক SGD step-এর পর L≈0.2725 (merged-KL p23–24)
- One-hot CE: −ln0.70=0.3567, −ln0.95=0.0513; BCE table p=0.95/0.80/0.50/0.10 → 0.0513/0.2231/0.6931/2.3026
- Neuron z=2.6; ReLU(−4), ReLU(0), ReLU(3.5) (merged-KL p17)

> ⚠️ **Fwd/back prop math যেগুলো notice অনুযায়ী আসবে না:** merged_L2 p15–17 (x=1 numerical forward+backprop+update), p20–24 (x₁=3, x₂=−1, v₁,v₂,c update); merged-KL p32–38 (2–2–3 MLP backprop)। শুধু concept পড়ো।

### 4.2 Gradient Descent PNG (`f_x_gradient_descent.webp`) ⭐⭐ — নিশ্চিত আসবে
f(x)=x², f′(x)=2x, x₀=4, η=0.1, x_new = x_old − η·2x_old (= 0.8·x_old).

| t | xₜ | f′(xₜ)=2xₜ | f(xₜ)=xₜ² |
|---|---|---|---|
| 0 | 4.0000 | 8.0000 | 16.0000 |
| 1 | 3.2000 | 6.4000 | 10.2400 |
| 2 | 2.5600 | 5.1200 | 6.5536 |
| 3 | 2.0480 | 4.0960 | 4.1943 |
| 4 | 1.6384 | 3.2768 | 2.6844 |
| 5 | 1.3107 | 2.6214 | 1.7180 *(image: 1.7189)* |
| 6 | 1.0486 | 2.0972 | 1.0995 *(image: 1.1005)* |
| 7 | 0.8389 | 1.6777 | 0.7037 |
| 8 | 0.6711 | 1.3422 | 0.4504 *(image: 0.4503)* |
| 9 | 0.5369 | 1.0737 | 0.2882 *(image: 0.2883)* |

⚠️ **Image-এর ছোট ভুল:** `f_x_gradient_descent.webp`-এ f(x₅), f(x₆), f(x₈), f(x₉) একটু ভুল ছাপা (1.7189, 1.1005, 0.4503, 0.2883)। সঠিক মান (x এর exact value থেকে): **1.7180, 1.0995, 0.4504, 0.2882**। xₜ আর f′(xₜ) কলামে কোনো ভুল নেই; x₀…x₄ ও f(x₀…x₄) মেলে। Exam-এ নিজে হিসাব করলে exact মান লেখো, আর sir-এর মান আলাদা হলে ছোট rounding পার্থক্য বলে ধরো।

Minimum x*=0, f(0)=0। **নিজে হাতে x₁…x₄ বের করা practice করো**, সংখ্যা না বদলে (যেমন অন্য x₀ বা η দিলে) করতে পারবে কি না দেখো.

## 5. Graph (2 × 10 marks) ⭐⭐⭐

প্রতিটায় দাও: **axis label, scale, key point, curve shape, special point (minimum / 0.5 / asymptote)**।

**L-2/L-3 bank (5টা):**

| # | Graph | Key points |
|---|---|---|
| G1 | f(x)=x², x∈[−2,2] | (−2,4),(−1,1),(0,0),(1,1),(2,4); U-shape; min (0,0) label |
| G2 | GD on f(x)=x² | x₀=4, 3.2, 2.56, 2.048, 1.6384 curve-এর উপর (xₜ,xₜ²); arrow বাম দিকে |
| G3 | Residual: ŷ=x+1, observed (2,2) | predicted (2,3); dashed vertical line; r=2−3=−1 |
| G4 | ReLU(z), z∈[−4,4] | negative → 0; (0,0),(1,1),(2,2),(3,3) |
| G5 | Sigmoid | (−2,0.119),(0,0.5),(2,0.881); S-curve; 0 ও 1 asymptote |

**Ch6 bank (D1–D6):**

| # | Graph | Key points |
|---|---|---|
| D1 | ReLU, x∈[−4,4] | (−4,0),(−2,0),(0,0),(1,1),(2,2),(4,4) |
| D2 | Sigmoid | z=−2→0.1192, 0→0.5, 1→0.7311, 2→0.8808 |
| D3 | BCE y=1, L=−ln p | (0.1,2.3026),(0.2,1.6094),(0.3,1.2040),(0.4,0.9163),(0.5,0.6931),(0.6,0.5108),(0.7,0.3567),(0.8,0.2231),(0.9,0.1054); নামতে থাকা curve |
| D4 | XOR 4 points | (0,0)→0,(0,1)→1,(1,0)→1,(1,1)→0; আলাদা symbol; কোনো এক line আলাদা করে না |
| D5 | AND points | শুধু (1,1)→1; linearly separable |
| D6 | OR points | শুধু (0,0)→0; linearly separable |

**Missing Ex. 6–10 (bank-এ নাম আছে, PDF-এ নেই → আমি generate করেছি, **Appendix A** + `Generated_Graphs_6-10.png`):**

| # | Graph | Key points |
|---|---|---|
| G6 | Bias effect: ŷ=2x vs ŷ=2x+5 *(generated; merged_L2 p4–5-এর bias ব্যাখ্যা থেকে)* | parallel; (0,0) ও (0,5); (1,2)/(1,7); (2,4)/(2,9) |
| G7 | Softmax bar chart, logits [2,1,0] | 0.665, 0.245, 0.090; sum=1 |
| G8 | BCE y=1, −ln p | (0.1,2.3026) … (0.9,0.1054); নামতে থাকা curve |
| G9 | GD loss vs iteration t | 16.00, 10.24, 6.55, 4.19, 2.68, 1.72, 1.10, 0.70, 0.45, 0.29 |
| G10 | One SGD step loss before/after | 0.6931 → 0.5759; p 0.5000 → 0.5622 |

**Merged PDF-এ আঁকা figure (bank-এ exercise না, কিন্তু graph হিসেবে আসতে পারে):**

| # | Graph | Key points |
|---|---|---|
| M1 | **BCE দুই curve** (merged-KL p4, Figure 1) | y=1: L=−ln p (p বাড়লে কমে, p→0 এ বড়); y=0: L=−ln(1−p) (উল্টো, p→1 এ বড়); x=predicted p (0.1…1), y=loss (nats) |
| M2 | **Residual দৃশ্য** (merged_L2 p4) | ŷ=wx+b রেখা, data point (xᵢ,yᵢ), dashed vertical rᵢ (G3-এর মতো) |
| M3 | **XOR 4 corner** (merged-KL p13) | (0,0)=0,(1,0)=1,(0,1)=1,(1,1)=0; কোনো single line আলাদা করে না (D4-এর মতো) |

**Sir-এর নতুন (announcement), sketch ফাইল: `image (2).webp` = ReLU(z) (z∈[−4,4], নেগেটিভে 0, (1,1),(2,2),(3,3),(4,4)), `image (1).webp` = ReLU′(z):**

| # | Graph | Key points |
|---|---|---|
| R1 | ReLU(z) (forward) — sir-এর sketch: `image (2).webp` | z∈[−4,4]; নেগেটিভে 0; positive-এ y=z |
| R2 ⭐ | **ReLU′(z)** (backward) | z∈[−4,4]; z≤0 → y=0 (z=0-তে dot, ReLU′(0)=0); z>0 → y=1 (y-axis-এ 1 mark); z=0-তে jump। ছবি: `ReLU_and_derivative.png`, sir-এর স্কেচ: `image (1).webp` |

> Bias effect এখন G6 হিসেবে generated Ex. 6-এ আছে (উপরে)।

---

## 6. Formula Sheet

| Concept | Formula |
|---|---|
| Linear regression | ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b |
| Residual | r = y − ŷ |
| MSE | (1/m) Σ(ŷ−y)² |
| Half-squared loss | L=½(ŷ−y)², ∂L/∂ŷ=ŷ−y |
| Gradient Descent | θ_new = θ_old − η∇L |
| GD on x² | x_new = x_old − η(2x_old) |
| Neuron | z=wᵀx+b; a=f(z) |
| ReLU / ReLU′ | max(0,z) / 1 if z>0, 0 if z<0 (z=0: convention 0) |
| Sigmoid | 1/(1+e⁻ᶻ) |
| Softmax | pₖ=e^zₖ/Σe^zⱼ |
| Entropy | H(P)=−ΣP ln P |
| Cross-Entropy | H(P,Q)=−ΣP ln Q |
| KL | ΣP ln(P/Q) |
| Relation | H(P,Q)=H(P)+D_KL(P‖Q) |
| BCE | −[y ln p+(1−y)ln(1−p)] |
| Sigmoid+BCE grad | ∂L/∂z=p−y; ∂L/∂w=(p−y)x; ∂L/∂b=p−y |
| Softmax+CE grad | ∂L/∂zₖ=pₖ−yₖ |
| SGD | θ_new=θ_old−ηĝ |
| Params (FC) | Σ(in×out+out) |
| Chain rule | dL/dx=(dL/du)(du/dx) |
| Vector chain rule | ∇ₓL=Jᵀ∇ᵤL |

Calculator values: ln0.7=−0.3567, ln0.3=−1.2040, ln0.6=−0.5108, ln0.4=−0.9163, ln0.8=−0.2231, ln0.2=−1.6094, e²=7.389, e¹=2.718.

---

## 7. Study Plan

1. **Day 1:** Part A → `merged_L2…pdf` + `Quiz_Bank_L-2_L-3` Part I–III
2. **Day 2:** Part B → `Merged-KL-XOR-Grad-Arch.pdf` + `Chapter6_Quiz_Bank` Section A–C
3. **Day 3:** **Graph practice** — G1–G5, G6–G10 (generated), D1–D6, M1 (BCE দুই curve), R1–R2 সব হাতে এঁকে (pencil, graph paper) + GD table হাতে
4. **Day 4:** T/F trap list + Math (4.1, 4.2) আবার + formula sheet

## 8. মনে রাখার বিষয়
- GD-তে **বিয়োগ**; Backprop ≠ GD; KL symmetric না; XOR separable না; UAT ≠ training guarantee
- ReLU′: negative → 0, positive → 1, z=0 → convention 0
- Graph-এ axis label + key point + curve shape + special point দিতে ভুলো না
- Calculator শুধু Session 2-তে

---

# Appendix A — Generated: L-2/L-3 Quiz Bank-এর missing T/F ও Graph

> ⚠️ **এগুলো PDF-এ নেই, আমি generate করেছি।** Bank-এর header-এ "25 T/F" আর "10 graph" লেখা, কিন্তু PDF-এ আছে 19 T/F আর 5 graph।
> সব মান/fact merged PDF + bank থেকে নেওয়া (source প্রতিটার পাশে)। অনুমান কিছু নেই।

---

## Part II (continued) — T/F 20–25 (generated)

20. Linear regression can be viewed as a single neuron with an identity activation function.
    **True.** ŷ=wᵀx+b ; neuron z=wᵀx+b, a=f(z) with f(z)=z. *(merged_L2 p3)*

21. Stacking several linear layers without any nonlinear activation can represent a nonlinear function such as y=x².
    **False.** W₂(W₁x+b₁)+b₂ = (W₂W₁)x+(W₂b₁+b₂), এখনও linear/affine। *(merged_L2 p14; merged-KL p15)*

22. For the half-squared loss L=½(ŷ−y)², the derivative is ∂L/∂ŷ = ŷ−y.
    **True.** ½ factor 2-এর সাথে কেটে যায়। *(bank notation guide)*

23. For a dataset with errors 0, 0, 0 and −1, the MSE is 1.
    **False.** MSE = (0+0+0+1)/4 = **0.25**, শুধু sum না, average। *(merged_L2 p4)*

24. If a hidden unit's ReLU output h₂ is 0, the gradient ∂L/∂v₂ is also 0 for that example.
    **True.** ∂L/∂v₂=(ŷ−y)h₂=0; inactive neuron error back করে না। *(merged_L2 p22–24)*

25. The output activation of a network is chosen by the task type: linear for continuous regression, sigmoid for binary and softmax for multiclass classification.
    **True.** Hidden layer-এ ReLU, output activation task নির্ধারণ করে। *(merged_L2 p18)*

---

## Part IV (continued) — Graph Plotting Exercises 6–10 (generated)

Reference plot: `Generated_Graphs_6-10.png` (এই folder-এ; ৬ষ্ঠ panel extra)

### Graph Plotting Exercise 6. Bias effect
**Task:** Plot ŷ=2x (b=0) and ŷ=2x+5 on the same axes.
**Points:** x=0 → (0,0) ও (0,5); x=1 → (1,2) ও (1,7); x=2 → (2,4) ও (2,9)।
**Check:** দুটো line parallel (slope w=2 একই); প্রথমটা origin দিয়ে যায়; দ্বিতীয়টা y-axis কাটে 5-এ, bias = intercept। *(merged_L2 p4–5)*

### Graph Plotting Exercise 7. Softmax output
**Task:** Draw a bar chart of the softmax probabilities for logits z=[2,1,0].
**Points:** e²=7.389, e¹=2.718, e⁰=1, sum=11.107 → bars 0.665, 0.245, 0.090।
**Check:** সবচেয়ে বড় logit-এর bar সবচেয়ে উঁচু; bar-এর যোগফল 1.000। *(Problem 10)*

### Graph Plotting Exercise 8. Binary cross-entropy, y=1
**Task:** Plot L(p)=−ln p for p from 0.1 to 0.9 and mark p=0.1, 0.5, 0.8.
**Points:** (0.1,2.3026), (0.2,1.6094), (0.3,1.2040), (0.4,0.9163), (0.5,0.6931), (0.6,0.5108), (0.7,0.3567), (0.8,0.2231), (0.9,0.1054)।
**Check:** p বাড়লে loss কমে; p→0 হলে loss খুব বড়; p=1-এ loss 0। *(Ch6 D3; merged-KL p4)*

### Graph Plotting Exercise 9. Loss versus iteration in gradient descent
**Task:** For f(x)=x², x₀=4, η=0.1, plot f(xₜ) against iteration t for t=0…9.
**Points:** 16.0000, 10.2400, 6.5536, 4.1943, 2.6844, 1.7180, 1.0995, 0.7037, 0.4504, 0.2882 (exact; image-এ t=5,6,8,9-এ ছোট ছাপার ভুল আছে: 1.7189, 1.1005, 0.4503, 0.2883)।
**Check:** প্রতি step-এ কমে; কমার পরিমাণ ক্রমশ ছোট (slope ছোট হচ্ছে); 0-এর দিকে যায়। *(f_x_gradient_descent.webp)*

### Graph Plotting Exercise 10. One SGD update on logistic regression
**Task:** Draw a bar chart of the BCE loss before and after one SGD step (x=2, y=1, w=b=0, η=0.1).
**Points:** before 0.6931 (p=0.5000); after 0.5759 (p=0.5622); w=0.10, b=0.05।
**Check:** loss কমেছে ~0.1172; p সঠিক class (y=1)-এর দিকে বেড়েছে। *(Ch6 C7–C8; merged-KL p6–7)*

*(Extra, panel 6:)* Dataset A–D residual: ŷ=2x₁+3x₂+5-এর D point-এ y=35, ŷ=36, r=−1, error²=1, MSE=0.25। *(merged_L2 p4)*

---

## Updated counts (generated সহ)
| | PDF-এ আছে | Generated | মোট (header অনুযায়ী) |
|---|---|---|---|
| T/F | 19 | 6 (T/F 20–25) | 25 |
| Graph | 5 | 5 (Ex. 6–10) | 10 |

---

# Appendix B — Errata (ছাপার ভুল) ও সঠিক মান

> QUIZ 1 folder-এর সব PDF/image-এর প্রতিটা সংখ্যা computer দিয়ে আবার হিসাব করে মিলানো।
> **পড়ার সময় এই file-এর মান ধরো।** যেখানে source ভুল, সঠিক মান বোল্ড।

---

## A. সত্যিকারের ছাপার ভুল (সঠিক মান লেখো)

| # | কোথায় | ছাপা আছে | **সঠিক** | কারণ |
|---|---|---|---|---|
| 1 | `f_x_gradient_descent.webp`, iteration table, t=5, f(xₜ) | 1.7189 | **1.7180** | 1.3107² = 1.7180 |
| 2 | একই table, t=6, f(xₜ) | 1.1005 | **1.0995** | 1.0486² = 1.0995 |
| 3 | একই table, t=8, f(xₜ) | 0.4503 | **0.4504** | 0.6711² = 0.4504 |
| 4 | একই table, t=9, f(xₜ) | 0.2883 | **0.2882** | 0.5369² = 0.2882 |
| 5 | `Deep_Learning_Quiz_Bank_L-2_L-3.pdf`, header (Part II) | "25 True/False" | **19 টা আছে** | PDF-এ ১–১৯ পর্যন্তই |
| 6 | একই bank, Part IV header | "10 graph-plotting exercises" | **5 টা আছে** | Ex. 1–5 পর্যন্তই |

> Source-এর বাকি সব মান (xₜ কলাম, f′(xₜ) কলাম, f(x₀…x₄), f(x₇)) ঠিক।

## B. ছোট rounding পার্থক্য (ভুল না; দুটোই গ্রহণযোগ্য)

| বিষয় | Bank/PDF-এ | Exact | নোট |
|---|---|---|---|
| BCE p=0.9, y=1 | 0.1053 | 0.10536 → **0.1054** | bank কেটে ফেলেছে; 0.1053 বা 0.1054 দুটোই চলবে |
| σ(2) | 0.881 (L-2/L-3), 0.8808 (Ch6) | 0.88080 | একই মান, ভিন্ন precision |
| σ(−2) | 0.119 / 0.1192 | 0.11920 | একই |
| σ(1) | 0.7311 | 0.73106 | একই |
| −ln(0.7311) | 0.3133 | 0.3132 (rounded p) / 0.3133 (exact p) | bank unrounded p ধরেছে |
| Softmax CE (logits [2,1,0], class 2) | 1.407 | 1.4065 (p=0.245) | rounded p-এর কারণে |
| Softmax CE (logits [0,2,1]) | 0.4076 / 0.408 | 0.40761 | একই |
| Logistic example 2 (merged-KL p24) নতুন p | 0.7615 | 0.7616 | L: 0.2725 vs 0.2724 |
| Loss কমার % (merged_L2) | 53.9% | 53.9% | ঠিক (0.18→0.0830) |

## C. ভুল নয়, কিন্তু দেখতে confusing

1. **Output weight-এর নাম:** L-2/L-3 bank-এ c₁, c₂ (≡ v₁, v₂), আর c = output bias। merged PDF-এ v₁, v₂, c। দুটো একই জিনিস।
2. **একই forward-pass উদাহরণে আলাদা parameter:** bank Problem 5: w₂=1, b₂=0; merged_L2 p15: w₂=0.5, b₂=0.5। দুই ক্ষেত্রেই z₂=1, h₂=1, ŷ=0.4। ফলাফল একই।
3. **ReLU(0) ও ReLU′(0):** কোথাও "z ≥ 0 → z", কোথাও "z ≤ 0 → 0"। ReLU(0)=0 দুই ক্ষেত্রেই। ReLU′(0): গাণিতিকভাবে undefined, convention 0 (merged-KL p17; sir-এর sketch-এও z=0-তে 0)।
4. **KL/CE-এর log:** সব জায়গায় natural log (ln), unit = nats।
5. **2–2–3 MLP-এর W⁽¹⁾ ও W⁽²⁾ notation** (merged-KL p32): Wᵀx ব্যবহার। এই backprop অংশ Quiz 1-এ math হিসেবে আসবে না।

## D. সঠিক মানের সংক্ষিপ্ত তালিকা (এখান থেকে মুখস্থ)

**Gradient Descent f(x)=x², x₀=4, η=0.1 (xₜ₊₁ = 0.8·xₜ)**

| t | xₜ | f′(xₜ)=2xₜ | f(xₜ) |
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

**BCE, y=1, L=−ln p:** 0.1→2.3026; 0.2→1.6094; 0.3→1.2040; 0.4→0.9163; 0.5→0.6931; 0.6→0.5108; 0.7→0.3567; 0.8→0.2231; 0.9→**0.1054** (bank: 0.1053); 0.95→0.0513
**BCE, y=0, p=0.8:** −ln(0.2)=1.6094

**Sigmoid:** σ(−2)=0.1192, σ(0)=0.5, σ(1)=0.7311, σ(2)=0.8808

**Softmax [2,1,0]:** [0.665, 0.245, 0.090] ; **[0,2,1]:** [0.090, 0.665, 0.245]
**CE:** −ln0.245=1.407 (class 2 of [2,1,0]); −ln0.665=0.408 (DDoS of [0,2,1])

**Entropy/CE/KL (P=(0.7,0.3), Q=(0.6,0.4)):** H(P)=0.6109, H(P,Q)=0.6325, KL=0.0216 (0.6109+0.0216=0.6325 ✓)
**One-hot:** −ln0.70=0.3567; −ln0.95=0.0513

**Logistic SGD (x=2,y=1,w=b=0,η=0.1):** p=0.5, L=0.6931; ∂L/∂w=−1, ∂L/∂b=−0.5; w=0.10, b=0.05; z=0.25, p=0.5622, L=0.5759

**Linear regression:** ŷ=2x₁+3x₂+5 → (2,2)→15; y=17 → r=2, r²=4; 4-run MSE=0.25
**Parameter count 2–2–3:** (2·2+2)+(2·3+3)=15 | **Chain rule:** u=2x, L=u², x=3 → 24

## E. Graph: কোন মান কোথায় বসাবে
- ReLU (−4…4): (−4,0), (−2,0), (0,0), (1,1), (2,2), (3,3), (4,4)
- ReLU′ (−4…4): z≤0 → y=0 (z=0-তে dot); z>0 → y=1
- Sigmoid: (−2,0.1192), (0,0.5), (1,0.7311), (2,0.8808)
- x² (−2…2): (−2,4), (−1,1), (0,0), (1,1), (2,4)
- GD: (4,16), (3.2,10.24), (2.56,6.5536), (2.048,4.1943), (1.6384,2.6844)
- Residual: ŷ=x+1, observed (2,2), predicted (2,3), r=−1
- Bias: ŷ=2x vs ŷ=2x+5
