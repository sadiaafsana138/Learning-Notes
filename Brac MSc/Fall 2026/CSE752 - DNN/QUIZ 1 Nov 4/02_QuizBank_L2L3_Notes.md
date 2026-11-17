# PDF 2 — Deep Learning Quiz Bank (Chapter 3, 4, 5 / Lecture 2–3)

> **Source:** `Deep_Learning_Quiz_Bank_L-2_L-3.pdf` (8 page). প্রশ্ন ও উত্তর PDF থেকে হুবহু নেওয়া; শুধু syllabus tag (A1…B10) ও note আমার যোগ করা।
> Syllabus tag মানে `QUIZ1_Syllabus.md`-এর কোন topic-এর সাথে মেলে।

**গোনা (PDF থেকে):** 19 Short Q · 19 T/F *(header-এ 25 লেখা)* · 11 Math · 5 Graph *(header-এ 10 লেখা)*

## 0. এই PDF-এর মূল কথা (এক নজরে)

- **Linear regression:** ŷ = wᵀx + b; weight = প্রতি unit feature-এ prediction-এর পরিবর্তন; bias না থাকলে line origin দিয়ে যায়।
- **Residual ও MSE:** r = y − ŷ; MSE = (1/m)Σ(ŷ−y)²; square করলে sign cancel হয় না।
- **Gradient Descent:** θ_new = θ_old − η∇L (**বিয়োগ**); f(x)=x², x₀=4, η=0.1 → 3.2, 2.56, …
- **Activation:** ReLU = max(0,z); sigmoid (0,1)-এর মধ্যে, σ(0)=0.5; softmax-এর যোগফল 1।
- **Forward/Backprop (concept):** backprop gradient বের করে, GD update করে। দুটো এক না।

## 1. Syllabus-এর সাথে মিল (কোন প্রশ্ন কোন topic)

| Syllabus topic | এই PDF-এর প্রশ্ন |
|---|---|
| A1 ML Task (Regression/Classification) | Short Q1 |
| A2 Linear Regression | Short Q2–6 · T/F 1–5 · Math P1 |
| A3 Residual ও MSE | Short Q7–8 · T/F 6–7 · Math P2, P6 |
| A4 Gradient Descent | Short Q9–11 · T/F 8–10 · Math P3 · Graph Ex.2 |
| A5 Activation (ReLU, Sigmoid, Softmax) | Short Q12–15 · T/F 11–17 · Math P4, P7, P8, P10 · Graph Ex.4, 5 |
| A7 Forward/Backprop (concept) | Short Q13, 16–19 · T/F 18–19 |
| B4 BCE | Math P9 |
| B6 Softmax + CE | Math P11 |
| Graph | Ex.1 x², Ex.2 GD, Ex.3 residual, Ex.4 ReLU, Ex.5 sigmoid |

> ⚠️ **Math P5, P6, P7** ছোট forward-pass (hidden unit → output → loss)। Notice অনুযায়ী Fwd/Back prop math আসবে না, তাই এগুলো আসার সম্ভাবনা কম; তবে সহজ, একবার করে রাখো।

## 2. Notation guide ও formula (PDF page 1, হুবহু)

*(PDF-এর subtitle: Chapter-3,4,5 — Linear Regression • Gradient Descent • Bias & MSE • Activation Functions • Forward & Backpropagation)*

**Notation guide (important for forward/backward propagation)**
- Hidden layer: z₁ = w₁x + b₁, h₁ = ReLU(z₁); z₂ = w₂x + b₂, h₂ = ReLU(z₂). These are the simple one-input-to-one-hidden-unit connections used for hand calculation.
- Output layer for regression: ŷ = v₁h₁ + v₂h₂ + c. In the supplied notes, the output weights are named v₁ and v₂, and c is the output bias.
- If your class calls the two outgoing weights c₁ and c₂, use c₁ ≡ v₁ and c₂ ≡ v₂. Keep c as the output bias; b₁ and b₂ are hidden-layer biases.
- For one sample, half-squared loss is L = ½(ŷ − y)² and ∂L/∂ŷ = ŷ − y. Dataset MSE is MSE = (1/m)Σ(ŷᵢ − yᵢ)²; these formulas differ by the factor ½ and by averaging over samples.
- The gradient is calculated by backpropagation. Gradient descent then updates a parameter: θ_new = θ_old − η(∂L/∂θ). Do not confuse calculating gradients with updating parameters.

**Core formulas to revise**

| Concept | Formula |
|---|---|
| Linear regression prediction | ŷ = w₁x₁ + w₂x₂ + b = wᵀx + b |
| Residual | r = y − ŷ |
| Mean squared error | MSE = (1/m) Σᵢ (ŷᵢ − yᵢ)² |
| Gradient descent | θ_new = θ_old − η∇θL |
| Gradient descent for f(x)=x² | f′(x)=2x;  x_new = x_old − η(2x_old) |
| ReLU | ReLU(z) = max(0,z) |
| Sigmoid | σ(z) = 1/(1+e^(−z)) |
| Half-squared loss | L = ½(ŷ − y)²;  ∂L/∂ŷ = ŷ − y |
| Linear output with two hidden units | ŷ = v₁h₁ + v₂h₂ + c |
| Output-layer gradients | ∂L/∂v₁ = (ŷ−y)h₁;  ∂L/∂v₂ = (ŷ−y)h₂;  ∂L/∂c = ŷ−y |
| Hidden-layer gradient (active ReLU) | ∂L/∂hᵢ = (ŷ−y)vᵢ;  ∂L/∂wᵢ = (∂L/∂hᵢ)ReLU′(zᵢ)x |
| Binary cross-entropy | L = −[y ln p + (1−y)ln(1−p)] |
| Softmax | pᵢ = e^(zᵢ) / Σⱼ e^(zⱼ) |

## 3. Part I — Short Conceptual Questions (19)

**1. What is the difference between regression and classification?**  `[Syllabus: A1]`

**PDF-এর উত্তর (exact):** Regression predicts a continuous numerical value, such as training time. Classification predicts a discrete class label, such as benign versus malicious.

**বাংলা অর্থ:** Regression continuous numerical value predict করে (যেমন training time)। Classification discrete class label predict করে (যেমন benign বনাম malicious)।

**2. What is a feature, and what is a target?**  `[Syllabus: A2]`

**PDF-এর উত্তর (exact):** A feature is an input attribute supplied to the model; the target is the true value the model is intended to predict. For the training-time example, epochs and batch-size units are features, while observed training minutes are the target.

**বাংলা অর্থ:** Feature = model-কে দেওয়া input attribute; Target = যে আসল মান predict করতে চাই। উদাহরণে epochs ও batch-size unit = feature, observed training minutes = target।

**3. What does a weight mean in linear regression?**  `[Syllabus: A2]`

**PDF-এর উত্তর (exact):** A weight describes the predicted change in output for a one-unit change in its feature, holding other features fixed. In ŷ = 2x₁ + 3x₂ + 5, the model adds 2 predicted minutes per extra epoch and 3 per batch-size unit.

**বাংলা অর্থ:** Weight বলে: অন্য feature fixed রেখে এক unit feature বাড়লে output কত বদলায়। ŷ = 2x₁+3x₂+5 তে প্রতি epoch-এ +2 মিনিট, প্রতি batch unit-এ +3 মিনিট।

**4. Why include a bias term?**  `[Syllabus: A2]`

**PDF-এর উত্তর (exact):** The bias shifts the line or plane independently of the input. Without bias, the linear model ŷ=wx is forced through the origin; with bias, it can have a nonzero intercept.

**বাংলা অর্থ:** Bias line/plane-কে input-নিরপেক্ষভাবে shift করে। Bias ছাড়া ŷ=wx অবশ্যই origin দিয়ে যায়; bias থাকলে nonzero intercept হতে পারে।

**5. What is a feature vector?**  `[Syllabus: A2]`

**PDF-এর উত্তর (exact):** It packages all features for one observation into a vector, such as x=[x₁,x₂]ᵀ. It provides a compact way to write the prediction as ŷ=wᵀx+b.

**বাংলা অর্থ:** Feature vector = এক observation-এর সব feature একটা vector-এ, x=[x₁,x₂]ᵀ। এতে prediction ŷ=wᵀx+b সংক্ষেপে লেখা যায়।

**6. What are model parameters?**  `[Syllabus: A2]`

**PDF-এর উত্তর (exact):** They are learnable values adjusted during training. In these simple models, the parameters include the weights and bias, written θ={w₁,w₂,…,b}.

**বাংলা অর্থ:** Parameters = training-এ শেখা/বদলানো মান: weights ও bias, θ={w₁,w₂,…,b}।

**7. What is a residual? Why does its sign matter?**  `[Syllabus: A3]`

**PDF-এর উত্তর (exact):** The residual is r=y−ŷ, the actual value minus the prediction. A positive residual means the model predicted too low; a negative residual means it predicted too high.

**বাংলা অর্থ:** Residual r = y − ŷ (actual − predicted)। r positive → model কম predict করেছে; r negative → বেশি predict করেছে।

**8. Why does MSE square the residuals?**  `[Syllabus: A3]`

**PDF-এর উত্তর (exact):** Squaring prevents positive and negative errors from cancelling and makes large deviations count more heavily. MSE is nonnegative and equals zero when every prediction matches its target.

**বাংলা অর্থ:** Square করলে positive ও negative error cancel হয় না, আর বড় error বেশি গুরুত্ব পায়। MSE ≥ 0; সব prediction ঠিক হলে MSE = 0।

**9. What does gradient descent do?**  `[Syllabus: A4]`

**PDF-এর উত্তর (exact):** It updates parameters in the direction opposite the loss gradient: θ_new=θ_old−η∇θL. The learning rate η controls the step size.

**বাংলা অর্থ:** Gradient Descent loss gradient-এর উল্টো দিকে parameter বদলায়: θ_new = θ_old − η∇L। η = learning rate = step size।

**10. What does the derivative tell us in gradient descent?**  `[Syllabus: A4]`

**PDF-এর উত্তর (exact):** The derivative gives the local slope of the objective. For f(x)=x², f′(x)=2x; at positive x, the slope is positive, so subtracting a positive gradient moves x toward zero.

**বাংলা অর্থ:** Derivative = local slope। f(x)=x²-এ f′(x)=2x; x positive হলে slope positive, তাই বিয়োগ করলে x 0-এর দিকে সরে।

**11. What is the role of the learning rate?**  `[Syllabus: A4]`

**PDF-এর উত্তর (exact):** It scales each gradient step. In the provided f(x)=x² example, starting at x₀=4 with η=0.1 gives x₁=4−0.1(8)=3.2.

**বাংলা অর্থ:** Learning rate প্রতি gradient step-কে scale করে। x₀=4, η=0.1: x₁ = 4 − 0.1(8) = 3.2।

**12. How does ReLU behave?**  `[Syllabus: A5]`

**PDF-এর উত্তর (exact):** ReLU(z)=max(0,z). It outputs zero for a negative input and passes a positive input through unchanged; examples include ReLU(−3)=0 and ReLU(2.5)=2.5.

**বাংলা অর্থ:** ReLU(z)=max(0,z): negative input → 0; positive input অপরিবর্তিত। ReLU(−3)=0, ReLU(2.5)=2.5।

**13. What is a potential limitation of ReLU during backpropagation?**  `[Syllabus: A5, A7]`

**PDF-এর উত্তর (exact):** For a negative pre-activation, the ReLU derivative is zero. The gradient through that unit is blocked for that sample, so its incoming parameters may receive no update through that path.

**বাংলা অর্থ:** Negative pre-activation-এ ReLU derivative 0, তাই ওই sample-এর জন্য ওই unit দিয়ে gradient blocked; incoming parameter ওই path-এ update পায় না।

**14. What does sigmoid do, and where is it useful?**  `[Syllabus: A5]`

**PDF-এর উত্তর (exact):** Sigmoid maps a real-valued logit to a probability strictly between 0 and 1. The notes use it for binary classification, where one value represents the probability of class 1.

**বাংলা অর্থ:** Sigmoid real-valued logit-কে strictly 0 ও 1-এর মাঝে probability-তে নেয়। Binary classification-এ class 1-এর probability হিসেবে ব্যবহার।

**15. Why is sigmoid(0)=0.5?**  `[Syllabus: A5]`

**PDF-এর উত্তর (exact):** Substituting z=0 gives 1/(1+e⁰)=1/(1+1)=0.5. A zero logit therefore gives equal probability to the two binary outcomes.

**বাংলা অর্থ:** z=0 বসালে σ(0) = 1/(1+e⁰) = 1/2 = 0.5; zero logit মানে দুই binary outcome-এর সমান probability।

**16. What is the difference between hidden-layer and output-layer parameters?**  `[Syllabus: A7]`

**PDF-এর উত্তর (exact):** In the simple two-hidden-unit example, w₁,w₂,b₁,b₂ control the feature transformations x→h. Output weights v₁,v₂ and output bias c combine h₁,h₂ into ŷ; these are independent trainable parameters.

**বাংলা অর্থ:** Hidden params (w₁,w₂,b₁,b₂) x→h রূপান্তর ঠিক করে; output params (v₁,v₂,c) h→ŷ। দুটোই স্বাধীন trainable parameter।

**17. What does forward propagation calculate?**  `[Syllabus: A7]`

**PDF-এর উত্তর (exact):** It moves from inputs through the hidden layer to the output, calculating pre-activations, activations, prediction and loss. It produces the values needed to start the backward calculation.

**বাংলা অর্থ:** Forward propagation input→hidden→output গিয়ে pre-activation, activation, prediction ও loss হিসাব করে; backward শুরুর মান যোগায়।

**18. What does backpropagation calculate?**  `[Syllabus: A7]`

**PDF-এর উত্তর (exact):** It applies the chain rule from the loss backward through the output and hidden layers to calculate each parameter’s gradient. An optimizer such as gradient descent uses those gradients to update the parameters.

**বাংলা অর্থ:** Backpropagation chain rule দিয়ে loss থেকে পেছনের দিকে প্রতি parameter-এর gradient বের করে। GD-এর মতো optimizer সেই gradient দিয়ে update করে।

**19. Why is the chain rule essential to backpropagation?**  `[Syllabus: A7]`

**PDF-এর উত্তর (exact):** A parameter affects the loss through intermediate computations. The chain rule multiplies local derivatives along that path, allowing the loss derivative to be computed efficiently.

**বাংলা অর্থ:** Parameter loss-কে মধ্যবর্তী ধাপ দিয়ে প্রভাবিত করে। Chain rule পথ বরাবর local derivative গুণ করে loss-derivative দক্ষভাবে বের করে.

## 4. Part II — True/False with reasons (19)

> PDF header-এ "25" লেখা, কিন্তু PDF-এ 19টাই আছে।

**1. Linear regression normally predicts a continuous numerical target.**  `[Syllabus: A2]`

→ **PDF-এর উত্তর (exact):** True. For example: training time, housing prices and temperature.

**বাংলা ব্যাখ্যা:** সঠিক। Regression continuous numerical target predict করে (training time, price, temperature)।

**2. In supervised learning, the target is the input attribute passed to the model.**  `[Syllabus: A2]`

→ **PDF-এর উত্তর (exact):** False. The feature is the input attribute; the target is the true value to predict.

**বাংলা ব্যাখ্যা:** ভুল। Input attribute = feature; target = আসল মান।

**3. A larger weight always means its feature is more important.**  `[Syllabus: A2]`

→ **PDF-এর উত্তর (exact):** False. Weights depend on feature scale; normalization can be needed before comparing magnitudes.

**বাংলা ব্যাখ্যা:** ভুল। Weight feature-এর scale-এর উপর নির্ভর করে; magnitude তুলনার আগে normalization লাগে।

**4. The model ŷ=wx with no bias must pass through (0,0).**  `[Syllabus: A2]`

→ **PDF-এর উত্তর (exact):** True. At x=0, the prediction is zero.

**বাংলা ব্যাখ্যা:** সঠিক। x=0 হলে prediction 0।

**5. In the simple linear model, weights and bias are learnable parameters.**  `[Syllabus: A2]`

→ **PDF-এর উত্তর (exact):** True. Training adjusts these values to reduce the objective.

**বাংলা ব্যাখ্যা:** সঠিক। Training এই মানগুলো বদলে objective কমায়।

**6. Squaring residuals allows positive and negative errors to cancel.**  `[Syllabus: A3]`

→ **PDF-এর উত্তর (exact):** False. Squaring makes each contribution nonnegative and prevents sign cancellation.

**বাংলা ব্যাখ্যা:** ভুল। Square-এ প্রতিটা অবদান non-negative, sign cancel হয় না।

**7. MSE is zero when every prediction equals its target.**  `[Syllabus: A3]`

→ **PDF-এর উত্তর (exact):** True. Every squared residual is zero, so their mean is zero.

**বাংলা ব্যাখ্যা:** সঠিক। সব squared residual 0 হলে গড়ও 0।

**8. Gradient descent updates parameters by adding the gradient.**  `[Syllabus: A4]`

→ **PDF-এর উত্তর (exact):** False. It subtracts the gradient: θ_new=θ_old−η∇θL.

**বাংলা ব্যাখ্যা:** ভুল। Gradient descent gradient **বিয়োগ** করে।

**9. For f(x)=x², the derivative is f′(x)=2x.**  `[Syllabus: A4]`

→ **PDF-এর উত্তর (exact):** True. Differentiating x² gives 2x.

**বাংলা ব্যাখ্যা:** সঠিক। x²-এর derivative 2x।

**10. With x₀=4 and η=0.1 for f(x)=x², the first gradient-descent value is 3.2.**  `[Syllabus: A4]`

→ **PDF-এর উত্তর (exact):** True. The gradient is 8, so x₁=4−0.1×8=3.2.

**বাংলা ব্যাখ্যা:** সঠিক। gradient 8, তাই x₁ = 4 − 0.8 = 3.2।

**11. ReLU(−3)=−3.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** False. ReLU returns max(0,z), so ReLU(−3)=0.

**বাংলা ব্যাখ্যা:** ভুল। ReLU(−3) = max(0,−3) = 0।

**12. For a positive input, ReLU passes the value through unchanged.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** True. When z>0, ReLU(z)=z and its derivative is 1.

**বাংলা ব্যাখ্যা:** সঠিক। z>0 হলে ReLU(z)=z, derivative 1।

**13. For z<0, the ReLU derivative is zero.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** True. The inactive negative branch has zero derivative.

**বাংলা ব্যাখ্যা:** সঠিক। Negative branch-এর derivative 0।

**14. The sigmoid function outputs exactly 0 or 1 for finite logits.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** False. For finite z, sigmoid lies strictly between 0 and 1.

**বাংলা ব্যাখ্যা:** ভুল। Finite z-এ sigmoid strictly 0 ও 1-এর মাঝে।

**15. Sigmoid(0)=0.5.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** True. σ(0)=1/(1+e⁰)=1/2.

**বাংলা ব্যাখ্যা:** সঠিক। σ(0)=1/2।

**16. Softmax probabilities across classes should sum to 1.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** True. Softmax normalizes the exponentiated logits into a probability distribution.

**বাংলা ব্যাখ্যা:** সঠিক। Softmax exponentiated logit normalize করে যোগফল 1 করে।

**17. Softmax is used for mutually exclusive multiclass classification.**  `[Syllabus: A5]`

→ **PDF-এর উত্তর (exact):** True. The example distinguishes one class among several alternatives.

**বাংলা ব্যাখ্যা:** সঠিক। Mutually exclusive multiclass-এর জন্য softmax।

**18. The output weights v₁ and v₂ are calculated from hidden weights w₁ and w₂.**  `[Syllabus: A7]`

→ **PDF-এর উত্তর (exact):** False. The output weights are separate learnable parameters; they are initialized and trained independently.

**বাংলা ব্যাখ্যা:** ভুল। v₁,v₂ স্বাধীন learnable parameter, w₁,w₂ থেকে হিসাব হয় না।

**19. Backpropagation and gradient descent are two names for the same operation.**  `[Syllabus: A7]`

→ **PDF-এর উত্তর (exact):** False. Backpropagation calculates gradients; gradient descent uses them to update parameters. 

**বাংলা ব্যাখ্যা:** ভুল। Backprop gradient বের করে; GD সেই gradient দিয়ে update করে।

## 5. Part III — Mathematical Problems (11), solution সহ

### Problem 1. Linear regression prediction  `[Syllabus: A2]`

**Given / Find:** ŷ = 2x₁ + 3x₂ + 5; x₁=2, x₂=2. Find ŷ.

**Solution:**

- ŷ = 2(2)+3(2)+5
- = 4+6+5
- = 15.

**Why it matters:** The prediction is a numerical output; no activation is applied in this linear model.

**শিখলে: Linear model-এ সোজা মান বসাও; কোনো activation নেই।**

### Problem 2. Residual and squared error  `[Syllabus: A3]`

**Given / Find:** Use the model in Problem 1. If the actual target is y=17, find r=y−ŷ and r².

**Solution:**

- ŷ=15
- r=y−ŷ=17−15=2
- Squared error = r² = 2² = 4.

**Why it matters:** A positive residual means the prediction was below the actual target.

**শিখলে: r = y − ŷ; r positive মানে prediction actual-এর চেয়ে কম।**

### Problem 3. First gradient-descent step  `[Syllabus: A4]`

**Given / Find:** Minimize f(x)=x² from x₀=4 with learning rate η=0.1. Find x₁ and f(x₁).

**Solution:**

- f′(x)=2x, so f′(4)=8.
- x₁=x₀−ηf′(x₀)=4−0.1(8)=3.2.
- f(x₁)=3.2²=10.24.

**Why it matters:** The positive gradient causes x to move left toward the minimum at zero.

**শিখলে: GD-র এক step: f′(x)=2x, x₁ = x₀ − η·f′(x₀)। Positive gradient x-কে বামে নেয়।**

### Problem 4. Calculate ReLU outputs  `[Syllabus: A5]`

**Given / Find:** Calculate ReLU(−3), ReLU(0), and ReLU(2.5).

**Solution:**

- ReLU(z)=max(0,z).
- ReLU(−3)=0; ReLU(0)=0; ReLU(2.5)=2.5.

**Why it matters:** The negative branch is zero; positive values pass through unchanged.

**শিখলে: ReLU = max(0,z); negative → 0, positive অপরিবর্তিত।**

### Problem 5. Easy forward pass: hidden units and output  `[Syllabus: A7 (forward pass)]`

**Given / Find:** Use x=1; w₁=1,b₁=0; w₂=1,b₂=0; hᵢ=ReLU(wᵢx+bᵢ). Output weights c₁=0.2,c₂=0.2 and output bias c=0. Find h₁,h₂ and ŷ.

**Solution:**

- z₁=1(1)+0=1, so h₁=ReLU(1)=1.
- z₂=1(1)+0=1, so h₂=ReLU(1)=1.
- ŷ=c₁h₁+c₂h₂+c=0.2(1)+0.2(1)+0=0.4.

**Why it matters:** The source notes call c₁ and c₂ output weights v₁ and v₂; here c₁≡v₁ and c₂≡v₂ to match the requested notation.

**শিখলে: Forward pass: z → h = ReLU(z) → ŷ = v₁h₁+v₂h₂+c। (⚠️ notice অনুযায়ী fwd/back math কম আসার কথা।)**

### Problem 6. Half-squared loss from the forward pass  `[Syllabus: A3, A7 (forward pass)]`

**Given / Find:** For ŷ=0.4 and target y=1, calculate L=½(ŷ−y)².

**Solution:**

- L=½(0.4−1)²=½(−0.6)².
- L=½(0.36)=0.18.

**Why it matters:** The half factor makes the derivative of this single-sample loss equal to ŷ−y.

**শিখলে: Half-squared loss L = ½(ŷ−y)²; ½ থাকায় derivative ŷ−y হয়।**

### Problem 7. Inactive ReLU  `[Syllabus: A5, A7 (forward pass)]`

**Given / Find:** Given x₁=3, x₂=−1,w₁=1,w₂=2,b₁=b₂=1. Use h₁=ReLU(w₁x₁+b₁), h₂=ReLU(w₂x₂+b₂). If output weights are v₁=v₂=0.2 and c=0, find h₁,h₂ and ŷ.

**Solution:**

- z₁=1(3)+1=4, so h₁=4.
- z₂=2(−1)+1=−1, so h₂=0.
- ŷ=0.2(4)+0.2(0)+0=0.8.

**Why it matters:** The second hidden unit is inactive for this input, so its outgoing-weight gradient is zero for this example.

**শিখলে: z<0 হলে h=0; ওই hidden unit ŷ-এ কিছু যোগ করে না, তার outgoing weight-এর gradient 0।**

### Problem 8. Sigmoid probability  `[Syllabus: A5]`

**Given / Find:** Calculate σ(0) and approximately calculate σ(2), using σ(z)=1/(1+e^(−z)).

**Solution:**

- σ(0)=1/(1+1)=0.5.
- σ(2)=1/(1+e^(−2))≈1/(1+0.1353)≈0.881.

**Why it matters:** Sigmoid converts a logit into a number between 0 and 1.

**শিখলে: σ(0)=0.5; σ(2)≈0.881; sigmoid logit-কে 0–1-এ আনে।**

### Problem 9. Binary cross-entropy  `[Syllabus: B4]`

**Given / Find:** For predicted class-1 probability p=0.8, calculate BCE for (a) true label y=1 and (b) true label y=0. Use natural logs.

**Solution:**

- For y=1: L=−ln(0.8)≈0.2231.
- For y=0: L=−ln(1−0.8)=−ln(0.2)≈1.6094.

**Why it matters:** The same probability can have very different loss depending on which label is correct.

**শিখলে: একই p-এ BCE নির্ভর করে true label y-এর উপর (y=1 → −ln p; y=0 → −ln(1−p))।**

### Problem 10. Softmax probability vector  `[Syllabus: A5]`

**Given / Find:** For logits z=[2,1,0], use e²≈7.389, e¹≈2.718 and e⁰=1. Calculate the softmax probabilities.

**Solution:**

- Sum=7.389+2.718+1=11.107.
- p₁=7.389/11.107≈0.665.
- p₂=2.718/11.107≈0.245; p₃=1/11.107≈0.090.
- Check: 0.665+0.245+0.090≈1.000.

**Why it matters:** Softmax forms a normalized probability distribution across mutually exclusive classes.

**শিখলে: Softmax = e^z / Σe^z; probability-র যোগফল 1।**

### Problem 11. Categorical cross-entropy for class 2  `[Syllabus: B6]`

**Given / Find:** Use the softmax result [0.665,0.245,0.090] and true one-hot label [0,1,0]. Calculate the categorical cross- entropy.

**Solution:**

- L=−Σ yₖ ln pₖ.
- Only the second target entry is 1, so L=−ln(0.245).
- L≈1.407.

**Why it matters:** The loss depends on the probability assigned to the true class, not just which class has the largest probability. 

**শিখলে: Categorical CE = −ln(true class-এর probability); সবচেয়ে বড় probability নয়, true class-এরটা গুরুত্বপূর্ণ।**

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


## 6. Part IV — Graph Plotting Exercises (5)

> PDF-এর header বলে "10 graph-plotting exercises", কিন্তু আছে 5টা। প্রতিটার reference chart PDF-এ আছে; chart-এর title **Graph 1, 2, 5, 6, 7** (লেখায় Exercise 1–5)। মানে মূল bank-এ 10টা ছিল; Graph 3, 4, 8, 9, 10 এই copy-তে নেই।

### Graph table

| Ex. | Graph | Task | Key points | Curve/বৈশিষ্ট্য (Check) | PDF chart title | Syllabus |
|---|---|---|---|---|---|---|
| 1 | f(x)=x² | Plot f(x)=x² for x from −2 to 2. Label the minimum. | Use points (−2,4), (−1,1), (0,0), (1,1), (2,4). Join smoothly with a U-shaped curve. | The curve is symmetric around x=0 and has its minimum f(0)=0. | Graph 1 | A4 |
| 2 | GD on f(x)=x² | Plot the curve f(x)=x² and mark the gradient-descent iterates for x₀=4, η=0.1. | Use x₀=4, x₁=3.2, x₂=2.56, x₃=2.048, x₄=1.6384. Plot each (xₜ, xₜ²) and draw arrows toward the next iterate. | The iterates move toward x=0, where the function is minimized; the objective values decrease. | Graph 2 | A4 |
| 3 | Residual (ŷ=x+1, point (2,2)) | Plot the model ŷ=x+1 and mark observed point (2,2). Show the residual with a dashed vertical line. | At x=2, model prediction is ŷ=3. Mark observed y=2 and predicted point (2,3), then connect them vertically. | Residual r=y−ŷ=2−3=−1, so the observed value is one unit below the prediction. | Graph 5 | A3 |
| 4 | ReLU | Plot ReLU(z)=max(0,z) for z from −4 to 4. | For negative z, plot y=0. For z=0, y=0. For positive values, use (1,1), (2,2), (3,3). | The negative branch is flat at zero; the positive branch follows y=z. | Graph 6 | A5 |
| 5 | Sigmoid | Sketch σ(z)=1/(1+e^(−z)) and mark z=−2, 0, 2. | Use approximate points (−2,0.119), (0,0.5), (2,0.881). Draw a smooth S-shaped curve approaching 0 and 1. | The output remains between 0 and 1 and σ(0)=0.5. | Graph 7 | A5 |

### প্রতিটা graph কীভাবে আঁকবে

- **Ex.1 f(x)=x²:** x-axis −3…3 (PDF chart), y-axis 0…9; point (−2,4),(−1,1),(0,0),(1,1),(2,4) বসাও; মসৃণ U-curve; (0,0) minimum label; y-axis বরাবর symmetric।
- **Ex.2 GD on x²:** x-axis 0…4.4, y-axis 0…18; curve x² আঁকো; dot: (4,16),(3.2,10.24),(2.56,6.5536),(2.048,4.1943),(1.6384,2.6844); প্রতিটা dot থেকে পরের dot-এ arrow (বাম-নিচে); step ক্রমশ ছোট।
- **Ex.3 Residual:** line ŷ=x+1 (y-intercept 1, slope 1); observed (2,2) dot; predicted (2,3); dashed vertical line দুই dot-এর মাঝে; label r=y−ŷ=−1; (2,2) line-এর নিচে।
- **Ex.4 ReLU:** x-axis −4…4; y-axis −0.5…4; negative z-তে flat y=0; (0,0) থেকে y=z; PDF chart-এ marked (−3,0),(0,0),(2.5,2.5)।
- **Ex.5 Sigmoid:** z-axis −6…6; y-axis 0…1; S-curve; marked (−2,0.119),(0,0.5),(2,0.881); y=0 ও y=1 asymptote।

### এই bank-এ নেই, তবু graph হিসেবে আসতে পারে (আমি generate করেছি, sir-এর question না)

| # | Graph | Key points |
|---|---|---|
| G6 | Bias effect ŷ=2x vs ŷ=2x+5 | parallel; (0,0) ও (0,5); (1,2)/(1,7); (2,4)/(2,9) |
| G7 | Softmax bar, logits [2,1,0] | 0.665, 0.245, 0.090 |
| G8 | BCE y=1, −ln p | (0.1,2.3026) … (0.9,0.1054) |
| G9 | GD loss f(xₜ) vs t | 16.00, 10.24, 6.55, 4.19, 2.68, 1.72, 1.10, 0.70, 0.45, 0.29 |
| G10 | এক SGD step-এ BCE loss | 0.6931 → 0.5759 |

Reference ছবি: `Generated_Graphs_6-10.png`।

## 7. T/F 20–25 (generated, PDF-এ নেই)

> header-এ 25 লেখা, কিন্তু PDF-এ 19। বাকি 6টা আমি বানিয়েছি; sir-এর original প্রশ্ন না।

20. Linear regression-কে identity activation-সহ একটা single neuron হিসেবে দেখা যায়। → **True.** ŷ=wᵀx+b; neuron z=wᵀx+b, a=f(z), f(z)=z।

21. Activation ছাড়া linear layer stack করলে y=x²-এর মতো nonlinear function represent করা যায়। → **False.** W₂(W₁x+b₁)+b₂=(W₂W₁)x+(W₂b₁+b₂), এখনও linear।

22. Half-squared loss L=½(ŷ−y)²-এর derivative ∂L/∂ŷ=ŷ−y। → **True.**

23. Error 0,0,0,−1 হলে MSE=1। → **False.** MSE=(0+0+0+1)/4=**0.25**।

24. Hidden unit-এর ReLU output h₂=0 হলে ∂L/∂v₂=0। → **True.** ∂L/∂v₂=(ŷ−y)h₂=0।

25. Output activation task নির্ধারণ করে: regression → linear, binary → sigmoid, multiclass → softmax। → **True.**

## 8. সংখ্যা-যাচাই ও ছাপার ভুল

সব সংখ্যা computer দিয়ে আবার হিসাব করে মিলানো:
- ŷ=2(2)+3(2)+5=15 ✓ · r=17−15=2, r²=4 ✓ · x₁=4−0.1(8)=3.2, f=10.24 ✓
- σ(2)=0.8808 (PDF-এ ≈0.881) ✓ · softmax [2,1,0]=[0.665,0.245,0.090] ✓
- BCE p=0.8: y=1 → 0.2231 ✓; y=0 → 1.6094 ✓ · CCE −ln(0.245)=1.4065≈1.407 ✓ (p rounded হওয়ায়)
- Problem 5, 6, 7: ŷ=0.4, L=0.18, ŷ(Problem 7)=0.8 ✓

**ছাপার ভুল (এই PDF-এ):** শুধু দুটো header-এর সংখ্যা: T/F "25" (আসলে 19), Graph "10" (আসলে 5)। প্রশ্ন বা উত্তরে সংখ্যার ভুল পাইনি।

**নোট:** Problem 5-এ output weight c₁,c₂ (≡ v₁,v₂) আর c = output bias। একই জিনিস, নামের পার্থক্য।
