# Assignment 01: NeuroNav — বাংলায় সম্পূর্ণ ব্যাখ্যা

এই নোটটা লেখা হয়েছে যাতে `Assignment_01.ipynb`-এর প্রতিটা অংশ তুমি নিজের ভাষায় বুঝে explain করতে পারো — ভাইভা বা রিভিউতে আটকে না যাও। প্রতিটা প্রশ্নের concept, formula আর code-এর পেছনের "কেন" — সবকিছু ধাপে ধাপে আছে।

---

## গল্পটা (Story) কী বলছে

তুমি **NeuroNav** নামের একটা কোম্পানিতে ML Engineer। কাজ: স্যাটেলাইট ছবি দেখে বলা এটা **Forest (জঙ্গল)** না **Urban (শহর)** এলাকা। দুইটা feature (input) দিয়ে বলতে হবে:

- **X1 = Greenness Index** — কতটা সবুজ/গাছপালা আছে
- **X2 = Building Density** — কতটা দালানকোঠা/স্থাপনা আছে

এটা একটা **Binary Classification** সমস্যা — output হবে দুইটার একটা: Forest (1) অথবা Urban (0)।

---

## Question 1 (Theory, 15 Marks)

### Part A — Activation function কেন লাগে, আর Sigmoid কেন output-এ ব্যবহার হয়

নিউরনের ভেতরে প্রথমে একটা **linear combination** হিসাব হয়:

```
Z = X · w + b
```

এই `Z` শুধু input-গুলোর weighted sum — এটা **linear**। যদি আমরা activation function ছাড়াই একাধিক layer বসাই, তাহলে linear-এর উপর linear বসিয়ে যতই layer বাড়াই না কেন, পুরো নেটওয়ার্ক শেষমেশ একটা মাত্র linear function-এর সমান হয়ে যায় (কারণ linear function-এর composition ও linear)। ফলে network কোনো **non-linear pattern** শিখতেই পারবে না — এইজন্যই **non-linearity** দরকার (mod 1-এর `non_linearity.pdf`-এ এটাই মূল কথা)।

**Sigmoid** ফাংশনটা হলো:

```
sigmoid(z) = 1 / (1 + e^(-z))
```

এটা output layer-এ ব্যবহার করার কারণ:

1. এর output সবসময় **(0, 1)** এর মধ্যে থাকে — মানে সরাসরি **probability** হিসেবে পড়া যায় (যেমন output = 0.9 মানে 90% নিশ্চিত এটা Forest)।
2. এটা **smooth ও differentiable** — অর্থাৎ gradient descent দিয়ে backpropagation করার সময় এর derivative হিসাব করা যায়, যা training-এর জন্য must।
3. এটা Binary Cross-Entropy loss-এর সাথে perfectly মিলে যায় (দুইটাই probability-ভিত্তিক)।

### Part B — Single perceptron কেন non-linearly separable ডেটাতে সমস্যায় পড়ে

একটা single-layer perceptron আসলে শুধু একটা **সরলরেখা (straight line)** — বা বেশি dimension-এ একটা **hyperplane** — দিয়ে দুই class-কে আলাদা করতে পারে। কারণ এর গোটা কাজটাই হলো `sigmoid(Xw + b)` — যেটা fundamentally linear boundary তৈরি করে।

- যদি Forest আর Urban-এর ডেটা পয়েন্টগুলো এমনভাবে ছড়ানো থাকে যে একটা সরলরেখা দিয়েই আলাদা করা যায় (এই assignment-এর `make_blobs` ডেটা যেমন) — তাহলে perceptron ভালোভাবে কাজ করবে।
- কিন্তু যদি দুই class একে অপরের ভেতর প্যাঁচানো থাকে (যেমন এক class আরেক class-কে ঘিরে আছে, বা XOR-এর মতো pattern) — তাহলে কোনো একটা সরলরেখা দিয়েই তাদের আলাদা করা সম্ভব না। এই অবস্থায় perceptron যতই train করো, loss একটা জায়গায় গিয়ে আটকে থাকবে (plateau করবে), accuracy আর বাড়বে না।

এর সমাধান হলো **MLP (Multi-Layer Perceptron)** — একাধিক perceptron/layer পরপর বসিয়ে, মাঝে non-linear activation দিয়ে, network-কে curved/non-linear boundary শেখানো যায়।

---

## Question 2 — Data Preparation (20 Marks)

```python
X, Y = make_blobs(n_samples=200, n_features=2, centers=2, random_state=42)
```

`make_blobs` দিয়ে ২০০টা সিন্থেটিক ডেটা পয়েন্ট বানানো হয়েছে, ২টা feature (X1, X2) আর ২টা cluster/center (Forest ও Urban)। এরপর ডেটাকে **normalize** করা হয়েছে (mean বিয়োগ করে std দিয়ে ভাগ) যাতে দুই feature-এর স্কেল কাছাকাছি থাকে — এতে gradient descent দ্রুত ও স্থিরভাবে converge করে।

Scatter plot-এ লাল (×) মানে Urban (0), সবুজ (o) মানে Forest (1) — চোখেই দেখা যায় দুইটা cluster মোটামুটি আলাদা জায়গায়, মানে **linearly separable**।

---

## Question 3 — Sigmoid ও Binary Cross-Entropy (20 Marks)

### Sigmoid
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```
উপরে যেই formula ব্যাখ্যা করা হলো, সেটাই সরাসরি বসানো।

### Binary Cross-Entropy (BCE) Loss
```python
def binary_cross_entropy(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
```

**BCE কী মাপে?** মডেল যে probability বলেছে (`y_pred`) আর আসল answer (`y_true`) কতটা কাছাকাছি — সেটার "শাস্তি (penalty)"।

- যদি আসল answer `y=1` হয়, তাহলে শুধু `-log(y_pred)` অংশটা কাজ করে — `y_pred` যত ১-এর কাছে যাবে, loss তত ছোট হবে; `y_pred` যদি ০-এর কাছাকাছি হয় (ভুল prediction), তাহলে `-log()` অনেক বড় (heavy penalty) হয়ে যায়।
- যদি `y=0` হয়, তাহলে `-log(1-y_pred)` অংশ কাজ করে — একই যুক্তি উল্টো দিকে।
- পুরো ডেটাসেটের জন্য গড় (mean) নেওয়া হয় যাতে একটা single scalar loss পাওয়া যায়, যেটা কমানোই training-এর লক্ষ্য।

---

## Question 4 — Forward Pass (20 Marks)

```python
def forward_pass(X, w, b):
    Z = np.dot(X, w) + b
    A = sigmoid(Z)
    return A
```

এটাই perceptron-এর পুরো "prediction" ধাপ, দুই সাব-স্টেপে:

1. **Linear step:** `Z = X·w + b` — প্রতিটা input feature-কে তার weight দিয়ে গুণ করে যোগ, তারপর bias যোগ। (Matrix হিসেবে: `X` shape `(m, n)`, `w` shape `(n, 1)`, ফলে `Z` shape `(m, 1)`।)
2. **Non-linear step:** `A = sigmoid(Z)` — Z-কে (0,1) রেঞ্জের probability-তে রূপান্তর।

---

## Question 5 — Training Loop / Gradient Descent (20 Marks)

```python
for epoch in range(epochs):
    A = forward_pass(X, w, b)              # ১. Predict
    loss = binary_cross_entropy(Y, A)      # ২. কতটা ভুল হলো মাপা
    losses.append(loss)

    dz = A - Y                             # BCE + sigmoid-এর derivative — সুন্দরভাবে এটাতেই simplify হয়
    dw = (1 / m) * np.dot(X.T, dz)         # weight-এর জন্য gradient
    db = (1 / m) * np.sum(dz)              # bias-এর জন্য gradient

    w = w - learning_rate * dw             # ৩. weight আপডেট
    b = b - learning_rate * db             # bias আপডেট
```

### Gradient Descent-এর মূল আইডিয়া
প্রতি epoch-এ:
1. **Forward pass** করে prediction বের করা।
2. Prediction কতটা ভুল, সেটা loss দিয়ে মাপা।
3. Loss-কে `w` আর `b`-এর সাপেক্ষে **gradient (derivative)** বের করা — gradient বলে দেয় loss কোন দিকে বাড়ছে।
4. Gradient-এর **উল্টো দিকে** ছোট একটা step নেওয়া (`learning_rate` দিয়ে scale করে) — কারণ আমরা loss কমাতে চাই, বাড়াতে না।

`dz = A - Y` একটা সুন্দর জিনিস — Sigmoid activation আর BCE loss একসাথে ব্যবহার করলে derivative হিসাবের সব জটিল chain-rule ধাপ simplify হয়ে শুধু `(prediction - actual)`-এ নেমে আসে। এইজন্যই কোড-এ dw, db-এর হিসাবটা এত ছোট দেখায়।

`w -= learning_rate * dw` আর `b -= learning_rate * db` — এটাই standard **Gradient Descent update rule**:
```
new_weight = old_weight − (learning_rate × gradient)
```

Training শেষে `loss_history` plot করলে দেখা যায় loss ধীরে ধীরে কমছে — মানে মডেল শিখছে (converge করছে)।

> **নোট:** assignment scaffold-এ একটা bug ছিল — নিচে demo call-এ `train_perceptron()` কোনো argument ছাড়াই লেখা ছিল, যেখানে function-টার `X, Y, epochs, learning_rate` — এই চারটা argument বাধ্যতামূলক। সেটা ঠিক করে `train_perceptron(X, Y, epochs=500, learning_rate=0.5)` লেখা হয়েছে, নাহলে `TypeError` আসত।

---

## Decision Boundary Explanation (5 Marks)

Train করার পর `plot_decision_boundary()` চালালে একটা straight line/boundary দেখা যায় যেটা লাল (Urban) আর সবুজ (Forest) region-কে আলাদা করেছে।

- এটা **সরলরেখা** হওয়ার কারণ — perceptron + sigmoid ফান্ডামেন্টালি একটা linear boundary-ই শিখতে পারে (Q1 Part B দ্রষ্টব্য)।
- `make_blobs` দিয়ে তৈরি ডেটা যেহেতু **linearly separable**, তাই এই সরলরেখাই যথেষ্ট — বেশিরভাগ পয়েন্ট সঠিক region-এ পড়ে।
- Loss curve নিচের দিকে নামা প্রমাণ করে gradient descent ঠিকভাবে converge করেছে — প্রতি epoch-এ `w, b` একটু একটু করে adjust হয়ে boundary-টাকে সঠিক জায়গায় নিয়ে এসেছে।
- বাস্তবে NeuroNav-এর আসল satellite data যদি linearly separable না হতো, তাহলে এই একই perceptron একটা জায়গায় আটকে (higher loss-এ plateau করে) ভুল classification করত — তখন MLP (একাধিক layer) দরকার হতো।

---

## এক নজরে পুরো Pipeline (Golden Order)

```
Data (X, Y)
   ↓
Forward Pass:  Z = Xw + b  →  A = sigmoid(Z)
   ↓
Loss:  BCE(Y, A)  → কতটা ভুল হলো
   ↓
Gradient:  dz = A - Y  →  dw, db
   ↓
Update:  w -= lr*dw,  b -= lr*db
   ↓
(Repeat প্রতি epoch-এ)  →  Loss কমতে থাকে  →  Model শেখে
```

এই একই pipeline — Forward → Loss → Gradient → Update — এটাই সব neural network training-এর (এমনকি বড় deep learning model-এরও) মূল কাঠামো, শুধু layer আর function জটিল হতে থাকে।
