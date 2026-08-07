# 🤖 ML & DL — PART 2
### Part 1-এ যা বাদ পড়েছিল

> **Part 1** (`ML_DL_Basics.md`) = admission MCQ-র জন্য যথেষ্ট।
> **এই file** = viva ও গভীর প্রশ্নের জন্য। Priority 🟡 — Networking/SQL শেষ করে তারপর।

---
---

# MODULE 7 — MODEL PARAMETERS & TUNING

## Topic 1: Parameter vs Hyperparameter ⭐⭐⭐

> **Viva-তে সবচেয়ে বেশি জিজ্ঞেস করা প্রশ্নগুলোর একটি।**

### Definitions (English)
- **Parameter:** A value the model **learns from data** during training.
- **Hyperparameter:** A value **set by the developer before training** that controls the learning process.

### Concept (বাংলায়)
| | **Parameter** | **Hyperparameter** |
|---|---|---|
| কে ঠিক করে | **Model নিজে** (training-এ) | **তুমি** (training-এর আগে) |
| কখন | Training চলাকালীন | Training শুরুর আগে |
| উদাহরণ | **Weight, Bias**, regression-এর slope | **Learning rate, Epoch, Batch size, k (KNN), Tree depth, Number of hidden layers** |
| Save হয়? | ✅ Model-এর সাথে | ❌ Config-এ থাকে |

⭐ **সহজ পরীক্ষা:** "এটা কি model শিখেছে, নাকি আমি বসিয়েছি?"

### Hyperparameter Tuning পদ্ধতি
| পদ্ধতি | কীভাবে |
|---|---|
| **Grid Search** | সব সম্ভাব্য combination একে একে চেষ্টা — নিখুঁত কিন্তু ধীর |
| **Random Search** | Random combination — দ্রুত, বাস্তবে প্রায়ই ভালো |
| **Bayesian Optimization** | আগের ফলাফল দেখে পরের combination আন্দাজ করে |

### 🔁 Revision Box
**Parameter = model শেখে** (weight, bias)। **Hyperparameter = তুমি ঠিক করো** (learning rate, epoch, batch size, k, tree depth)। Tuning: **Grid Search / Random Search / Bayesian**।

---
---

# MODULE 8 — FEATURE ENGINEERING ⭐⭐

## Topic 1: Normalization vs Standardization ⭐

### Definitions
- **Normalization (Min-Max Scaling):** Rescales values to a fixed range, usually **[0, 1]**.
- **Standardization (Z-score):** Rescales data to have **mean = 0** and **standard deviation = 1**.

### Formula ⭐
```
Normalization:    x' = (x − min) / (max − min)              → range [0, 1]

Standardization:  x' = (x − μ) / σ                          → mean 0, std 1
```

### কেন দরকার? (বাংলায়)
ধরো dataset-এ দুটো column:
- Age: 20–60
- Salary: 20,000–200,000

Salary-র মান অনেক বড় বলে model ভাববে salary বেশি গুরুত্বপূর্ণ — অথচ তা নয়। **Scaling করলে সবাই সমান ওজন পায়।**

| | Normalization | Standardization |
|---|---|---|
| Range | **[0, 1]** নির্দিষ্ট | নির্দিষ্ট নয় |
| Outlier-এ | **সংবেদনশীল** ⚠️ | তুলনামূলক সহনশীল |
| কখন | Distribution জানা নেই, **Neural Network, KNN** | Data **Gaussian**-এর কাছাকাছি, **SVM, Linear/Logistic Regression, PCA** |

⚠️ **যেসব algorithm-এ scaling লাগে না:** Decision Tree, Random Forest, XGBoost (এরা split করে, দূরত্ব মাপে না)।

## Topic 2: Categorical Encoding ⭐

| পদ্ধতি | কীভাবে | কখন |
|---|---|---|
| **Label Encoding** | প্রতিটি category-কে একটা সংখ্যা (Red=0, Green=1, Blue=2) | **Ordinal** data (Low/Medium/High) |
| **One-Hot Encoding** | প্রতিটি category-র জন্য আলাদা 0/1 column | **Nominal** data (Red/Green/Blue) |

⚠️ **Nominal data-তে Label Encoding ব্যবহার করলে model ভুল বুঝবে** — ভাববে Blue(2) > Red(0), অথচ রঙের কোনো ক্রম নেই। ⭐ Classic mistake।

## Topic 3: অন্যান্য

| বিষয় | সমাধান |
|---|---|
| **Missing Values** | বাদ দেওয়া · Mean/Median/Mode দিয়ে পূরণ (Imputation) · Model দিয়ে predict |
| **Outlier** | IQR method · Z-score · Winsorization |
| **Imbalanced Data** | **Oversampling (SMOTE)** · Undersampling · Class weight |
| **Curse of Dimensionality** | Feature বাড়লে data ছড়িয়ে যায়, model খারাপ হয় → **PCA / Feature Selection** |
| **Data Leakage** ⚠️ | Test-এর তথ্য training-এ ঢুকে পড়া → ভুয়া উচ্চ accuracy। **Scaling শুধু train-এ fit করে test-এ apply করো** |

### 🔁 Revision Box
**Normalization = [0,1]**, outlier-সংবেদনশীল, NN/KNN-এ। **Standardization = mean 0, std 1**, SVM/PCA/Regression-এ। **Tree-based algorithm-এ scaling লাগে না**। **Nominal → One-Hot, Ordinal → Label**। Imbalance → **SMOTE**। **Data Leakage** = test-এর তথ্য train-এ ঢোকা।

---
---

# MODULE 9 — ENSEMBLE LEARNING ⭐⭐

## Topic 1: Bagging vs Boosting ⭐⭐⭐

### Definition (English)
**Ensemble Learning** combines multiple weak models to produce a **stronger** overall model.

### Concept (বাংলায়)
একজন বিশেষজ্ঞের মতামতের চেয়ে **দশজনের ভোট** সাধারণত ভালো — এটাই ensemble-এর ধারণা।

### দুই প্রধান কৌশল ⭐⭐⭐

| | **Bagging** (Bootstrap Aggregating) | **Boosting** |
|---|---|---|
| Model চলে | **সমান্তরালে (Parallel)** | **ক্রমানুসারে (Sequential)** |
| প্রতিটি model | স্বাধীন, random subset-এ train | **আগেরটার ভুল** থেকে শেখে |
| চূড়ান্ত সিদ্ধান্ত | **Majority vote / গড়** | **Weighted vote** |
| কী কমায় | **Variance** (overfitting) | **Bias** (underfitting) |
| উদাহরণ | **Random Forest** | **AdaBoost, Gradient Boosting, XGBoost** |
| Overfitting ঝুঁকি | কম | বেশি (সতর্ক থাকতে হয়) |

⭐ **মুখস্থ:** **Bagging → Variance কমায় → Random Forest** · **Boosting → Bias কমায় → XGBoost**

### Stacking 🔵
আলাদা ধরনের কয়েকটা model-এর output নিয়ে **আরেকটা model** (meta-learner) চূড়ান্ত সিদ্ধান্ত নেয়।

### 🔁 Revision Box
Ensemble = অনেক দুর্বল model মিলে শক্তিশালী। **Bagging = parallel + variance কমায় + Random Forest**। **Boosting = sequential + আগের ভুল থেকে শেখে + bias কমায় + XGBoost/AdaBoost**। **Stacking = meta-learner**।

---
---

# MODULE 10 — গুরুত্বপূর্ণ FORMULA ⭐⭐

## 1. Linear Regression
```
Prediction:  ŷ = w·x + b
Cost (MSE):  J = (1/n) Σ (y − ŷ)²
```

## 2. Sigmoid (Logistic Regression / Binary output)
```
σ(z) = 1 / (1 + e^(−z))          → output সবসময় 0 থেকে 1-এর মধ্যে
```

## 3. Softmax (Multi-class output)
```
softmax(zᵢ) = e^(zᵢ) / Σ e^(zⱼ)   → সব output-এর যোগফল = 1
```
⭐ **Sigmoid = binary (এক output)**, **Softmax = multi-class (সব মিলে যোগফল 1)**

## 4. Entropy & Information Gain (Decision Tree) ⭐
```
Entropy(S) = − Σ pᵢ · log₂(pᵢ)

Information Gain = Entropy(parent) − Weighted Entropy(children)
```
- Entropy **0** = একদম বিশুদ্ধ (সব একই class) ✅
- Entropy **1** = সম্পূর্ণ মিশ্র (50-50) ⚠️
- Decision Tree সবচেয়ে **বেশি Information Gain**-এর feature দিয়ে split করে ⭐

## 5. Gini Impurity (CART)
```
Gini = 1 − Σ (pᵢ)²
```
Entropy-র বিকল্প; হিসাব দ্রুত (log লাগে না), তাই বাস্তবে বেশি ব্যবহৃত।

## 6. Bayes Theorem (Naive Bayes) ⭐
```
P(A|B) = [ P(B|A) × P(A) ] / P(B)
```
| অংশ | নাম |
|---|---|
| P(A\|B) | **Posterior** (যা বের করতে চাই) |
| P(B\|A) | **Likelihood** |
| P(A) | **Prior** |
| P(B) | **Evidence** |

⭐ **"Naive" কেন?** কারণ ধরে নেওয়া হয় সব feature **পরস্পর স্বাধীন** — বাস্তবে সবসময় সত্য নয়, তবু ভালো কাজ করে।

## 7. Gradient Descent Update
```
w_new = w_old − (learning_rate × ∂J/∂w)
```

## 8. Euclidean Distance (KNN, K-Means)
```
d = √[ (x₂−x₁)² + (y₂−y₁)² + ... ]
```

---
---

# MODULE 11 — CONFUSION MATRIX (সংখ্যা দিয়ে) ⭐⭐⭐

## একটা পূর্ণ উদাহরণ

১০০টা email-এর মধ্যে ২০টা আসলে spam। Model বলল ২৫টা spam।
তার মধ্যে ১৫টা সত্যিই spam ছিল।

```
                    Predicted
                Spam      Not Spam
Actual  Spam    TP = 15    FN = 5      (আসল spam = 20)
        Not     FP = 10    TN = 70     (আসল not-spam = 80)
```

### হিসাব
```
Accuracy  = (TP + TN) / Total = (15 + 70) / 100 = 0.85  →  85%

Precision = TP / (TP + FP) = 15 / (15 + 10) = 15/25 = 0.60  →  60%
            ("spam বলেছি ২৫টা, সত্যি ছিল ১৫টা")

Recall    = TP / (TP + FN) = 15 / (15 + 5)  = 15/20 = 0.75  →  75%
            ("আসল spam ছিল ২০টা, ধরতে পেরেছি ১৫টা")

F1-Score  = 2 × (0.60 × 0.75) / (0.60 + 0.75) = 0.90/1.35 = 0.667  →  66.7%
```

### ⭐ কোনটা কখন বেশি গুরুত্বপূর্ণ

| পরিস্থিতি | কোনটা বেশি জরুরি | কেন |
|---|---|---|
| **ক্যান্সার নির্ণয়** | **Recall** | একজন রোগীও যেন বাদ না পড়ে (FN ভয়ংকর) |
| **Spam filter** | **Precision** | জরুরি mail যেন spam-এ না যায় (FP বিরক্তিকর) |
| **ব্যাংক জালিয়াতি** | **Recall** | জালিয়াতি ধরা না পড়া বেশি ক্ষতিকর |
| দুটোই দরকার | **F1-Score** | ভারসাম্য |

### মনে রাখার উপায় ⭐
- **FN (False Negative)** = "আছে, কিন্তু বলিনি" → **Recall** এটাকে শাস্তি দেয়
- **FP (False Positive)** = "নেই, তবু বলেছি" → **Precision** এটাকে শাস্তি দেয়

### 🔁 Revision Box
**Precision = TP/(TP+FP)** — "যা বলেছি তার কতটা সত্যি"। **Recall = TP/(TP+FN)** — "যা ছিল তার কতটা ধরেছি"। **F1 = 2PR/(P+R)**। **ক্যান্সার → Recall**, **Spam → Precision**।

---
---

# MODULE 12 — ALGORITHM-এর ভিতরের কথা

## 1. K-Means — k কত হবে? (Elbow Method) ⭐
1. বিভিন্ন k (1, 2, 3, …) দিয়ে K-Means চালাও।
2. প্রতিটার **WCSS** (Within-Cluster Sum of Squares) হিসাব করো।
3. k-এর বিপরীতে WCSS plot করো।
4. যেখানে curve হঠাৎ বাঁক নেয় (**কনুইয়ের মতো**) — সেটাই সেরা k ⭐

## 2. SVM — Kernel Trick ⭐
Data সরলরেখা দিয়ে ভাগ করা না গেলে **Kernel** সেটাকে উঁচু dimension-এ পাঠায়, যেখানে ভাগ করা যায়।

| Kernel | কখন |
|---|---|
| **Linear** | Data সরলরেখায় ভাগ হয় |
| **Polynomial** | মাঝারি জটিল |
| **RBF (Gaussian)** | সবচেয়ে ব্যবহৃত, খুব জটিল সীমানা |

**Support Vector** = সীমানার সবচেয়ে কাছের point-গুলো, যারা hyperplane নির্ধারণ করে।

## 3. KNN — k কত?
- **k ছোট** (যেমন 1) → noise-এ সংবেদনশীল, **overfitting**
- **k বড়** → সীমানা মসৃণ, কিন্তু **underfitting**
- ⭐ **k বিজোড় (odd) নাও** — binary classification-এ ভোট সমান হওয়া এড়াতে
- KNN = **Lazy learner** (training-এ কিছুই করে না, predict করার সময় সব হিসাব করে)

## 4. Random Forest কেন Decision Tree-র চেয়ে ভালো?
একটা Decision Tree সহজে **overfit** করে। Random Forest অনেক tree-র ভোট নেয়, প্রতিটা tree ভিন্ন data-subset ও ভিন্ন feature-subset দেখে — তাই **variance কমে**।

---
---

# MODULE 13 — DEEP LEARNING গভীরে

## Topic 1: CNN-এর বিস্তারিত ⭐⭐

### মূল উপাদান
| Term | অর্থ |
|---|---|
| **Filter / Kernel** | ছোট matrix (3×3, 5×5) যা ছবির উপর দিয়ে সরে feature বের করে |
| **Stride** | Filter প্রতিবার কত pixel সরবে |
| **Padding** | ছবির চারপাশে 0 যোগ করা, যাতে আকার না কমে (`same` vs `valid`) |
| **Feature Map** | Convolution-এর ফলাফল |
| **Pooling** | আকার কমানো — **Max Pooling** (সবচেয়ে বড় নেওয়া) সবচেয়ে common |
| **Flatten** | 2D feature map → 1D vector, FC layer-এ পাঠানোর জন্য |

### Output Size Formula ⭐⭐
```
Output = [ (W − F + 2P) / S ] + 1

W = input size,  F = filter size,  P = padding,  S = stride
```

**উদাহরণ:** Input 32×32, Filter 3×3, Padding 1, Stride 1
```
Output = (32 − 3 + 2)/1 + 1 = 32   →  আকার একই থাকল (same padding)
```

### CNN কেন ভালো?
1. **Parameter Sharing** — একই filter পুরো ছবিতে ব্যবহৃত → parameter অনেক কম
2. **Spatial Hierarchy** — শুরুর layer edge শেখে, পরের layer shape, শেষে পুরো object
3. **Translation Invariance** — বিড়াল ছবির যেখানেই থাকুক, চিনতে পারে

## Topic 2: Batch Normalization ⭐
প্রতিটি layer-এর input-কে normalize (mean 0, std 1) করা।
**সুবিধা:** Training দ্রুত হয় · Vanishing gradient কমে · কিছুটা regularization-এর কাজও করে

## Topic 3: Transfer Learning ⭐⭐
**Definition:** Using a **pre-trained model** (trained on a large dataset) as the starting point for a new, related task.

**Concept:** ImageNet-এ ১৪ লক্ষ ছবিতে train করা ResNet নিয়ে এসে শেষ কয়েকটা layer বদলে **নিজের ছোট dataset**-এ train করা।

**কেন দরকার:** কম data ও কম GPU-তেও ভালো ফল ⭐

| ধাপ | কী |
|---|---|
| **Feature Extraction** | আগের সব layer **freeze**, শুধু শেষ layer train |
| **Fine-tuning** | কিছু layer unfreeze করে **কম learning rate**-এ train |

**জনপ্রিয় pre-trained model:** ResNet, VGG, Inception, EfficientNet (vision) · BERT, GPT (NLP)

## Topic 4: Optimizer তুলনা
| Optimizer | বৈশিষ্ট্য |
|---|---|
| **SGD** | সরল, ধীর, অস্থির |
| **Momentum** | আগের দিক মনে রাখে, দোলা কমায় |
| **RMSprop** | প্রতিটি parameter-এর জন্য আলাদা learning rate |
| **Adam** ⭐ | Momentum + RMSprop — **বাস্তবে default পছন্দ** |

---
---

# MODULE 14 — NLP ও LLM BASICS 🟡

> ২০২৬-এ viva-তে এটা আসার সম্ভাবনা ভালোই। অন্তত terminology জেনে যাও।

## Topic 1: NLP Preprocessing ⭐

| ধাপ | কী করে |
|---|---|
| **Tokenization** | বাক্যকে শব্দ/token-এ ভাঙা |
| **Stop word removal** | "the", "is", "a" — অর্থহীন শব্দ বাদ |
| **Stemming** | শব্দের শেষ কেটে মূল আনা ("running" → "run") — **দ্রুত কিন্তু অগোছালো** |
| **Lemmatization** | অভিধান ধরে সঠিক মূল আনা ("better" → "good") — **ধীর কিন্তু নির্ভুল** |
| **POS Tagging** | প্রতিটি শব্দের পদ চিহ্নিত করা |

⭐ **Stemming vs Lemmatization** — এই পার্থক্যটা প্রায়ই জিজ্ঞেস করা হয়।

## Topic 2: Text → Number ⭐

| পদ্ধতি | কীভাবে |
|---|---|
| **Bag of Words (BoW)** | প্রতিটি শব্দ কতবার এসেছে গোনা — ক্রম হারিয়ে যায় |
| **TF-IDF** | **TF** (এই doc-এ কতবার) × **IDF** (কত doc-এ আছে, বিরল শব্দ বেশি গুরুত্ব) |
| **Word Embedding** | শব্দকে dense vector-এ রূপান্তর (**Word2Vec, GloVe**) — অর্থ ধরে রাখে |
| **Contextual Embedding** | একই শব্দ প্রসঙ্গভেদে ভিন্ন vector (**BERT**) |

⭐ **Embedding-এর জাদু:** `king − man + woman ≈ queen`

## Topic 3: Transformer & LLM ⭐

### Attention Mechanism
**ধারণা:** একটা শব্দ বোঝার জন্য বাক্যের **কোন কোন শব্দ বেশি গুরুত্বপূর্ণ** — model নিজেই ঠিক করে।

> "The animal didn't cross the street because **it** was too tired"
> — "it" বলতে কী বোঝাচ্ছে? Attention "animal"-এ বেশি ওজন দেবে।

### Transformer কেন RNN-এর চেয়ে ভালো?
| | RNN / LSTM | **Transformer** |
|---|---|---|
| Processing | **ক্রমানুসারে** (একটার পর একটা) | **সমান্তরালে (parallel)** ⭐ |
| দীর্ঘ নির্ভরতা | দুর্বল | **শক্তিশালী** (attention) |
| Training গতি | ধীর | দ্রুত (GPU-বান্ধব) |

⭐ মূল গবেষণাপত্র: **"Attention Is All You Need" (2017)**

### LLM Terminology
| Term | অর্থ |
|---|---|
| **Token** | Text-এর ক্ষুদ্রতম একক (শব্দ বা শব্দাংশ) |
| **Pre-training** | বিশাল text-এ সাধারণ ভাষাজ্ঞান শেখা |
| **Fine-tuning** | নির্দিষ্ট কাজের জন্য ছোট dataset-এ আরও train |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **Prompt Engineering** | ভালো নির্দেশ লিখে ভালো output পাওয়া |
| **Hallucination** | Model আত্মবিশ্বাসের সাথে ভুল তথ্য বলা ⚠️ |
| **RAG** | Retrieval-Augmented Generation — বাইরের document থেকে তথ্য এনে উত্তর দেওয়া |

---
---

# MODULE 15 — TOOLS & LIBRARIES 🔵

| Library | কাজ |
|---|---|
| **NumPy** | Numerical computing, array |
| **Pandas** | Data manipulation, DataFrame |
| **Matplotlib / Seaborn** | Visualization |
| **Scikit-learn** | **Classical ML** (regression, tree, SVM, K-Means) |
| **TensorFlow / Keras** | Deep Learning (Google) |
| **PyTorch** | Deep Learning (Meta) — **গবেষণায় সবচেয়ে জনপ্রিয়** |
| **OpenCV** | Computer Vision |
| **NLTK / spaCy** | NLP |
| **Hugging Face** | Pre-trained model ও Transformer |

---
---

# ★ PART 2 — REVISION (২০টা point)

1. **Parameter = model শেখে** (weight, bias) · **Hyperparameter = তুমি দাও** (lr, epoch, k)
2. **Normalization = [0,1]** · **Standardization = mean 0, std 1**
3. **Tree-based algorithm-এ scaling লাগে না**
4. **Nominal → One-Hot** · **Ordinal → Label Encoding**
5. **Bagging = parallel, variance কমায়, Random Forest**
6. **Boosting = sequential, bias কমায়, XGBoost/AdaBoost**
7. **Entropy 0 = বিশুদ্ধ, 1 = সম্পূর্ণ মিশ্র**
8. **Decision Tree সবচেয়ে বেশি Information Gain-এ split করে**
9. **Bayes:** `P(A|B) = P(B|A)·P(A) / P(B)`; "naive" = feature independence ধরে
10. **Sigmoid = binary** · **Softmax = multi-class (যোগফল 1)**
11. **Precision = TP/(TP+FP)** · **Recall = TP/(TP+FN)**
12. **ক্যান্সার → Recall জরুরি** · **Spam → Precision জরুরি**
13. **K-Means-এ k বাছতে Elbow Method**
14. **SVM-এ Kernel Trick** — উঁচু dimension-এ পাঠিয়ে ভাগ করা
15. **KNN = lazy learner**, k বিজোড় নাও
16. **CNN Output = (W − F + 2P)/S + 1**
17. **Transfer Learning** = pre-trained model + fine-tuning, কম data-তেও ভালো
18. **Batch Normalization** = training দ্রুত + vanishing gradient কমায়
19. **Stemming = দ্রুত/অগোছালো** · **Lemmatization = ধীর/নির্ভুল**
20. **Transformer parallel চলে, RNN sequential** — "Attention Is All You Need"

---

# 🎤 বাড়তি VIVA প্রশ্ন

| প্রশ্ন | উত্তরের কাঠামো |
|---|---|
| **Parameter ও Hyperparameter-এর পার্থক্য?** | Model শেখে vs তুমি ঠিক করো; উদাহরণ দাও |
| **Bagging ও Boosting-এর পার্থক্য?** | Parallel/variance vs Sequential/bias; RF vs XGBoost |
| **Normalization কেন দরকার?** | Age 20–60 vs Salary 20k–200k উদাহরণ দাও |
| **Decision Tree কীভাবে split করে?** | Information Gain / Gini — entropy কমানোর চেষ্টা |
| **Transfer Learning কী ও কেন?** | Pre-trained model, কম data + কম GPU-তে ভালো ফল |
| **Transformer কেন RNN-এর চেয়ে ভালো?** | Parallel processing + attention + দীর্ঘ নির্ভরতা |
| **তোমার dataset ছোট হলে কী করবে?** | Transfer learning, data augmentation, cross-validation, সরল model |

---

# ⚠️ এখন কি এটা পড়বে?

**না, যদি Networking/SQL/Programming এখনো বাকি থাকে।**

Sample paper-এ ML/DL-এর একটাও প্রশ্ন ছিল না। এই file-এর মূল্য **viva ও ভবিষ্যতের কাজে** — লিখিত পরীক্ষায় নয়।

**যদি ২০ মিনিট সময় থাকে, শুধু এই ৫টা:**
1. **Parameter vs Hyperparameter**
2. **Bagging vs Boosting**
3. **Precision vs Recall** (কখন কোনটা)
4. **Transfer Learning**
5. **Transformer vs RNN**
