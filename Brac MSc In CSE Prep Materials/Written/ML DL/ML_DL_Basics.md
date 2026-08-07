# 🤖 MACHINE LEARNING & DEEP LEARNING — BASICS
### BRAC MSc CSE Admission + Viva প্রস্তুতি

> **কতটা পড়বে:** ৪৫ মিনিট। Sample paper-এ ML ছিল না, তাই **depth নয়, coverage** দরকার।
> **কেন পড়বে:** (১) নতুন প্রশ্নপত্রে AI/ML আসছে (২) **Viva-তে প্রায় নিশ্চিত** — "MSc-তে কী নিয়ে কাজ করতে চাও?" বললেই ML প্রসঙ্গ আসবে।

---
---

# MODULE 1 — AI, ML, DL সম্পর্ক

## Topic 1: AI vs ML vs DL ⭐⭐⭐

### Definitions (English)

| Term | Definition |
|---|---|
| **AI (Artificial Intelligence)** | The broad field of making machines perform tasks that normally require **human intelligence**. |
| **ML (Machine Learning)** | A **subset of AI** where systems **learn patterns from data** without being explicitly programmed. |
| **DL (Deep Learning)** | A **subset of ML** that uses **multi-layered neural networks** to learn features automatically. |

### Concept (বাংলায়)
```
┌─────────────────────────────────┐
│  AI (সবচেয়ে বড় গণ্ডি)             │
│  ┌───────────────────────────┐  │
│  │  ML                        │  │
│  │  ┌─────────────────────┐  │  │
│  │  │  DL                  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

**পার্থক্যটা এভাবে বোঝো:**
- **Traditional Programming:** নিয়ম + data → **ফলাফল**
- **Machine Learning:** data + ফলাফল → **নিয়ম** ⭐

**Real Example:**
- **AI** = দাবা খেলার program (rule-based-ও হতে পারে)
- **ML** = spam email চেনা (হাজারো email দেখে নিজে শিখেছে)
- **DL** = ছবিতে মুখ চেনা, ChatGPT, Google Translate

### Key Points
1. **AI ⊃ ML ⊃ DL** — এই ক্রম মুখস্থ
2. ML-এ **feature manually** বের করতে হয়; DL-এ model **নিজেই feature শেখে** ⭐
3. DL-এর জন্য **অনেক বেশি data + GPU** লাগে
4. ML ছোট dataset-এও চলে, DL-এর জন্য সাধারণত হাজার-লক্ষ sample লাগে

### ML vs DL Comparison ⭐⭐⭐

| Feature | **Machine Learning** | **Deep Learning** |
|---|---|---|
| Data প্রয়োজন | কম (হাজার) | **অনেক বেশি (লক্ষ)** |
| Feature extraction | **Manual** (হাতে করতে হয়) | **Automatic** (নিজে শেখে) |
| Hardware | CPU-তেই চলে | **GPU লাগে** |
| Training সময় | কম (মিনিট-ঘণ্টা) | বেশি (ঘণ্টা-দিন) |
| Interpretability | **ভালো** (কেন সিদ্ধান্ত বোঝা যায়) | খারাপ (**Black Box**) |
| উদাহরণ | Decision Tree, SVM, KNN | CNN, RNN, Transformer |

### 🔁 Revision Box
**AI ⊃ ML ⊃ DL**। Traditional programming: rules+data → output; **ML: data+output → rules**। ML-এ **feature manual**, DL-এ **automatic**। DL-এর জন্য বেশি data + GPU লাগে, কিন্তু **black box**।

---
---

# MODULE 2 — TYPES OF MACHINE LEARNING ⭐⭐⭐

## Topic 1: চার ধরনের ML

### 1. Supervised Learning
**Definition:** Learning from **labeled data**, where each input has a known correct output.

**Concept:** শিক্ষক যেভাবে উত্তরসহ প্রশ্ন দিয়ে শেখান। Model input-output জোড়া দেখে সম্পর্ক শেখে।

**দুই ভাগ:**
| Type | কী predict করে | উদাহরণ |
|---|---|---|
| **Classification** | **Category / Class** (discrete) | Spam না Not-spam, রোগ আছে/নেই |
| **Regression** | **Continuous মান** | বাড়ির দাম, তাপমাত্রা, বিক্রির পরিমাণ |

⭐ **মনে রাখার নিয়ম:** উত্তর যদি "কোনটা?" → **Classification**। উত্তর যদি "কত?" → **Regression**।

### 2. Unsupervised Learning
**Definition:** Learning from **unlabeled data** to discover hidden patterns or groupings.

**Concept:** কোনো উত্তর দেওয়া নেই। Model নিজেই data-র মধ্যে গঠন খুঁজে বের করে।

**দুই প্রধান কাজ:**
| Type | কাজ | উদাহরণ |
|---|---|---|
| **Clustering** | একই রকম data একসাথে গ্রুপ করা | Customer segmentation |
| **Dimensionality Reduction** | Feature কমানো | PCA দিয়ে ১০০ column → ১০ column |

### 3. Semi-Supervised Learning
কিছু data labeled, বেশিরভাগ unlabeled। বাস্তবে labeling ব্যয়বহুল বলে এটা কাজে লাগে।

### 4. Reinforcement Learning
**Definition:** An **agent** learns by interacting with an **environment**, receiving **rewards** or **penalties** for its actions.

**Concept:** চেষ্টা-ভুল-পুরস্কার। ভালো কাজে reward, খারাপ কাজে penalty — এভাবে নীতি (policy) শেখে।

**উপাদান:** Agent · Environment · State · Action · **Reward** · Policy
**উদাহরণ:** Self-driving car, AlphaGo, Game AI, Robot navigation

### Comparison Table ⭐⭐⭐

| Type | Data | লক্ষ্য | উদাহরণ Algorithm |
|---|---|---|---|
| **Supervised** | **Labeled** | Predict করা | Linear/Logistic Regression, SVM, KNN, Decision Tree |
| **Unsupervised** | **Unlabeled** | Pattern খোঁজা | **K-Means**, Hierarchical, **PCA** |
| **Semi-supervised** | মিশ্র | কম label দিয়ে বেশি কাজ | Self-training |
| **Reinforcement** | Reward signal | সর্বোচ্চ reward | Q-Learning, DQN |

### ⚠️ Common MCQ Traps
- **K-Means = Unsupervised** ✅ (অনেকে supervised ভাবে)
- **KNN = Supervised** ✅ — নাম মিললেও K-Means-এর সাথে গুলিয়ে ফেলবে না ⭐⭐⭐
- **PCA = Unsupervised** (dimensionality reduction)
- **Logistic Regression = Classification**, নাম "regression" হলেও ⭐ Classic trap

### 🔁 Revision Box
**Supervised** = labeled data → Classification ("কোনটা?") ও Regression ("কত?")। **Unsupervised** = unlabeled → Clustering (K-Means) ও Dimensionality Reduction (PCA)। **Reinforcement** = agent + environment + **reward**। ⚠️ **KNN = supervised, K-Means = unsupervised**; **Logistic Regression = classification**।

---
---

# MODULE 3 — COMMON ML ALGORITHMS

## এক লাইনে প্রতিটি ⭐

| Algorithm | Type | কীভাবে কাজ করে |
|---|---|---|
| **Linear Regression** | Supervised (Regression) | Data-র মধ্যে দিয়ে **সেরা সরলরেখা** টানে (`y = mx + c`) |
| **Logistic Regression** | Supervised (**Classification**) | **Sigmoid** দিয়ে probability বের করে, 0.5-এর উপরে হলে class 1 |
| **KNN** (K-Nearest Neighbors) | Supervised | নতুন point-এর **k সবচেয়ে কাছের প্রতিবেশী**-র majority vote |
| **Decision Tree** | Supervised | প্রশ্নের গাছ — প্রতিটি node-এ একটা শর্ত, leaf-এ উত্তর |
| **Random Forest** | Supervised | **অনেক Decision Tree**-র ভোট (**Ensemble**) — overfitting কমায় |
| **SVM** (Support Vector Machine) | Supervised | দুই class-এর মাঝে **সবচেয়ে চওড়া margin**-এর hyperplane আঁকে |
| **Naive Bayes** | Supervised | **Bayes Theorem** + feature গুলো স্বাধীন ("naive") ধরে নেয় |
| **K-Means** | **Unsupervised** | Data-কে **k টি cluster**-এ ভাগ করে, centroid বারবার আপডেট করে |
| **PCA** | **Unsupervised** | সবচেয়ে বেশি variance-এর দিক ধরে **dimension কমায়** |

### K-Means — কীভাবে চলে (Steps) ⭐
1. **k** টি random centroid বেছে নাও।
2. প্রতিটি data point-কে **সবচেয়ে কাছের centroid**-এর cluster-এ দাও।
3. প্রতিটি cluster-এর **গড় বের করে নতুন centroid** বসাও।
4. Centroid আর না বদলানো পর্যন্ত ধাপ 2–3 পুনরাবৃত্তি করো।

### Decision Tree — কীভাবে split করে
সবচেয়ে ভালো প্রশ্ন বেছে নেয় **Information Gain** (Entropy কমানো) বা **Gini Index** দিয়ে।

### 🔁 Revision Box
**Linear Reg** = সরলরেখা; **Logistic Reg** = sigmoid, classification; **KNN** = k প্রতিবেশীর ভোট; **Decision Tree** = শর্তের গাছ (Entropy/Gini); **Random Forest** = অনেক tree-র ensemble; **SVM** = সর্বোচ্চ margin hyperplane; **Naive Bayes** = Bayes + independence ধরে; **K-Means** = k cluster, centroid update; **PCA** = dimension কমানো।

---
---

# MODULE 4 — MODEL TRAINING & EVALUATION ⭐⭐⭐

## Topic 1: Data Split
| Set | কাজ | সাধারণ অনুপাত |
|---|---|---|
| **Training set** | Model শেখে | 70–80% |
| **Validation set** | Hyperparameter tune করা | 10–15% |
| **Test set** | চূড়ান্ত performance মাপা (**একবারই**) | 10–20% |

**Cross-Validation (k-fold):** Data-কে k ভাগে ভাগ করে, প্রতিবার একটা ভাগ test, বাকিগুলো train — k বার চালিয়ে গড় নেওয়া। ছোট dataset-এ খুব কাজে লাগে।

## Topic 2: Overfitting vs Underfitting ⭐⭐⭐

| | **Underfitting** | **Overfitting** |
|---|---|---|
| সমস্যা | Model **খুব সরল** | Model **খুব জটিল** |
| Training accuracy | **কম** | **খুব বেশি** |
| Test accuracy | **কম** | **কম** ⚠️ |
| কারণ | কম feature, কম training | বেশি feature, কম data, বেশি training |
| **Bias / Variance** | **High Bias** | **High Variance** |
| সমাধান | জটিল model, বেশি feature | **Regularization, Dropout, বেশি data, Early Stopping** |

**Concept (বাংলায়):**
**Overfitting** = model training data **মুখস্থ** করে ফেলেছে, নতুন data-তে পারে না।
**Underfitting** = model কিছুই ঠিকমতো শেখেনি।

⭐ **Bias-Variance Tradeoff:** Bias কমালে Variance বাড়ে, উল্টোটাও। মাঝামাঝি একটা balance-ই সেরা model।

**Regularization:**
- **L1 (Lasso)** — কিছু weight একদম **0** করে দেয় → feature selection
- **L2 (Ridge)** — weight ছোট করে, কিন্তু 0 করে না

## Topic 3: Evaluation Metrics ⭐⭐⭐

### Confusion Matrix
```
                 Predicted
              Positive  Negative
Actual Pos      TP        FN
       Neg      FP        TN
```

| Metric | Formula | কখন ব্যবহার |
|---|---|---|
| **Accuracy** | (TP+TN) / Total | Balanced dataset-এ |
| **Precision** | **TP / (TP + FP)** | False alarm ব্যয়বহুল হলে (spam filter) |
| **Recall (Sensitivity)** | **TP / (TP + FN)** | Miss করা ব্যয়বহুল হলে (**ক্যান্সার detection**) |
| **F1-Score** | **2 × (P×R) / (P+R)** | Precision ও Recall-এর ভারসাম্য (harmonic mean) |
| **ROC-AUC** | Curve-এর নিচের ক্ষেত্রফল | Threshold-independent তুলনা |

⭐ **Precision vs Recall মনে রাখার উপায়:**
- **Precision** = "যেগুলো positive বলেছি, তার কতটা সত্যি?" (**P**redicted-এর মধ্যে)
- **Recall** = "যত সত্যি positive ছিল, তার কতটা ধরতে পেরেছি?" (**A**ctual-এর মধ্যে)

### Regression Metrics
| Metric | পূর্ণরূপ |
|---|---|
| **MSE** | Mean Squared Error |
| **RMSE** | Root Mean Squared Error |
| **MAE** | Mean Absolute Error |
| **R²** | Coefficient of Determination (1-এর কাছে ভালো) |

### ⚠️ Common MCQ Trap — Imbalanced Data
১০০০ email-এর ৯৯০টা normal, ১০টা spam। সব "normal" বললেই **Accuracy 99%** — কিন্তু model সম্পূর্ণ অকেজো।
➡️ **Imbalanced dataset-এ Accuracy বিভ্রান্তিকর; Precision/Recall/F1 দেখতে হয়।** ⭐⭐⭐

### 🔁 Revision Box
Data → **Train / Validation / Test**। **Overfitting** = train ভালো test খারাপ = **High Variance** → Regularization/Dropout/বেশি data। **Underfitting** = দুটোই খারাপ = **High Bias**। **Precision = TP/(TP+FP)**, **Recall = TP/(TP+FN)**, **F1 = harmonic mean**। **Imbalanced data-তে Accuracy বিভ্রান্তিকর**।

---
---

# MODULE 5 — DEEP LEARNING BASICS ⭐⭐⭐

## Topic 1: Artificial Neural Network (ANN)

### Definition (English)
An **Artificial Neural Network** is a computing model inspired by the human brain, consisting of interconnected **neurons** organized in **layers**, where each connection has a **weight**.

### Structure
```
Input Layer      Hidden Layer(s)      Output Layer
   x1 ──┐         ┌───┐
        ├────────►│ h │──┐
   x2 ──┤         └───┘  ├──────►  ŷ (prediction)
        ├────────►┌───┐  │
   x3 ──┘         │ h │──┘
                  └───┘
```

**একটি Neuron-এর কাজ:**
```
output = Activation( Σ(weight × input) + bias )
```

| উপাদান | কাজ |
|---|---|
| **Weight (w)** | কোন input কতটা গুরুত্বপূর্ণ |
| **Bias (b)** | Threshold সরানোর জন্য |
| **Activation Function** | **Non-linearity** যোগ করে ⭐ |

⭐ **Activation না থাকলে** পুরো network যত layer-ই হোক, শেষ পর্যন্ত একটা **linear function**-এই দাঁড়াবে। এজন্যই activation অপরিহার্য।

## Topic 2: Activation Functions ⭐⭐⭐

| Function | Range | কোথায় ব্যবহার | সমস্যা |
|---|---|---|---|
| **Sigmoid** | 0 to 1 | Binary classification (output layer) | **Vanishing gradient** |
| **Tanh** | −1 to 1 | Sigmoid-এর চেয়ে ভালো (zero-centered) | Vanishing gradient |
| **ReLU** | 0 to ∞ | **Hidden layer-এর default** ⭐ | Dying ReLU (negative-এ 0) |
| **Leaky ReLU** | −∞ to ∞ | Dying ReLU-র সমাধান | — |
| **Softmax** | 0 to 1, যোগফল = 1 | **Multi-class** output layer ⭐ | — |

⭐ **মুখস্থ:** Hidden layer → **ReLU** · Binary output → **Sigmoid** · Multi-class output → **Softmax**

## Topic 3: Training একটা Neural Network — Steps ⭐⭐⭐

1. **Forward Propagation** — input থেকে layer ধরে ধরে সামনে এগিয়ে **prediction (ŷ)** বের করা
2. **Loss Calculation** — prediction ও আসল উত্তরের **পার্থক্য** মাপা (Loss Function দিয়ে)
3. **Backpropagation** — loss থেকে **পিছনের দিকে** গিয়ে প্রতিটি weight-এর **gradient** (derivative) বের করা
4. **Weight Update** — **Gradient Descent** দিয়ে weight সংশোধন:
   `w_new = w_old − (learning_rate × gradient)`
5. **Repeat** — Loss যথেষ্ট কমা পর্যন্ত ধাপ 1–4 পুনরাবৃত্তি (প্রতিবার = ১ **epoch**)

### Loss Functions
| কাজ | Loss Function |
|---|---|
| Regression | **MSE** (Mean Squared Error) |
| Binary Classification | **Binary Cross-Entropy** |
| Multi-class Classification | **Categorical Cross-Entropy** |

### Gradient Descent-এর ধরন ⭐

| Type | কতটা data দিয়ে একবার update |
|---|---|
| **Batch GD** | পুরো dataset — সঠিক কিন্তু ধীর |
| **Stochastic GD (SGD)** | **একটা sample** — দ্রুত কিন্তু অস্থির |
| **Mini-batch GD** | **ছোট batch (32/64/128)** — বাস্তবে সবচেয়ে ব্যবহৃত ⭐ |

**Optimizer:** SGD, Momentum, RMSprop, **Adam** (সবচেয়ে জনপ্রিয়)

### গুরুত্বপূর্ণ Terms ⭐

| Term | অর্থ |
|---|---|
| **Epoch** | পুরো dataset একবার সম্পূর্ণ ঘুরে আসা |
| **Batch Size** | একবারে কতগুলো sample দিয়ে weight update |
| **Iteration** | একটা batch process করা |
| **Learning Rate** | প্রতিবার weight কতটা বদলাবে ⭐ |

**Formula:** `Iterations per epoch = Total samples / Batch size`
*উদাহরণ:* 1000 sample, batch size 100 → **10 iteration = 1 epoch**

⚠️ **Learning Rate:**
- **খুব বড়** → minimum-এর উপর দিয়ে লাফিয়ে যাবে, converge হবে না
- **খুব ছোট** → খুব ধীরে শিখবে, আটকে যেতে পারে

## Topic 4: DL-এর সাধারণ সমস্যা ও সমাধান

| সমস্যা | কী হয় | সমাধান |
|---|---|---|
| **Vanishing Gradient** | Gradient এত ছোট হয়ে যায় যে শুরুর layer শেখেই না | **ReLU**, Batch Norm, **LSTM**, ResNet |
| **Exploding Gradient** | Gradient বিশাল হয়ে যায় | Gradient Clipping |
| **Overfitting** | মুখস্থ করে ফেলে | **Dropout**, Regularization, Data Augmentation, Early Stopping |

**Dropout:** Training-এর সময় randomly কিছু neuron **বন্ধ** করে দেওয়া (যেমন 20%) — যাতে model কোনো একটা neuron-এর উপর অতিনির্ভর না হয়।

### 🔁 Revision Box
Neuron: `output = Activation(Σwx + b)`। **Activation না থাকলে পুরো network linear**। Hidden → **ReLU**, Binary → **Sigmoid**, Multi-class → **Softmax**। Training: **Forward → Loss → Backpropagation → Gradient Descent**। `w_new = w − lr × gradient`। **Epoch** = পুরো data একবার; **Mini-batch GD** সবচেয়ে ব্যবহৃত; **Adam** জনপ্রিয় optimizer। **Vanishing gradient → ReLU/LSTM**, **Overfitting → Dropout**।

---
---

# MODULE 6 — DL ARCHITECTURES (শুধু নাম ও কাজ) ⭐

| Architecture | কীসের জন্য | মূল ধারণা |
|---|---|---|
| **ANN / MLP** | সাধারণ tabular data | Fully connected layers |
| **CNN** (Convolutional NN) | **Image, Video** ⭐ | **Convolution** (filter দিয়ে feature বের করা) + **Pooling** (size কমানো) |
| **RNN** (Recurrent NN) | **Sequence, Time series** | পূর্বের output পরের input-এ ফিরে আসে (memory) |
| **LSTM / GRU** | দীর্ঘ sequence | **Gate** দিয়ে vanishing gradient সমাধান |
| **Transformer** | **NLP, LLM (ChatGPT)** ⭐ | **Attention mechanism** — "Attention Is All You Need" |
| **GAN** | ছবি/data তৈরি করা | **Generator vs Discriminator** — দুইজনের প্রতিযোগিতা |
| **Autoencoder** | Compression, Anomaly detection | Encoder → ছোট representation → Decoder |

### CNN-এর তিন স্তর ⭐
1. **Convolution Layer** — filter/kernel চালিয়ে feature map বানায় (edge, texture)
2. **Pooling Layer** — dimension কমায় (**Max Pooling** সবচেয়ে common)
3. **Fully Connected Layer** — শেষে classification করে

### 🔁 Revision Box
**CNN → Image** (Convolution + Pooling + FC)। **RNN/LSTM → Sequence/Time series** (LSTM-এর gate vanishing gradient সমাধান করে)। **Transformer → NLP/LLM** (**Attention**)। **GAN → Generator vs Discriminator**, নতুন data তৈরি। **Autoencoder → compression/anomaly**।

---
---

# ★ FINAL REVISION — ২০টা নিশ্চিত-ধরনের প্রশ্ন

1. **AI ⊃ ML ⊃ DL**
2. **ML = data + output → rules** (traditional programming-এর উল্টো)
3. **Supervised = labeled**, **Unsupervised = unlabeled**, **RL = reward**
4. **Classification = "কোনটা?"**, **Regression = "কত?"**
5. ⚠️ **KNN = Supervised, K-Means = Unsupervised**
6. ⚠️ **Logistic Regression = Classification** (নাম regression হলেও)
7. **PCA = Dimensionality Reduction, Unsupervised**
8. **Random Forest = অনেক Decision Tree-র ensemble**
9. **SVM = সর্বোচ্চ margin-এর hyperplane**
10. **Overfitting = High Variance** (train ভালো, test খারাপ)
11. **Underfitting = High Bias** (দুটোই খারাপ)
12. **Overfitting-এর সমাধান = Dropout, Regularization, বেশি data, Early Stopping**
13. **Precision = TP/(TP+FP)**, **Recall = TP/(TP+FN)**, **F1 = harmonic mean**
14. ⚠️ **Imbalanced data-তে Accuracy বিভ্রান্তিকর**
15. **Activation না থাকলে network পুরোটাই linear**
16. **Hidden → ReLU, Binary output → Sigmoid, Multi-class → Softmax**
17. **Backpropagation = পিছন দিকে gradient হিসাব**
18. `w_new = w_old − (learning_rate × gradient)`
19. **CNN → Image, RNN/LSTM → Sequence, Transformer → NLP**
20. **Vanishing Gradient → ReLU / LSTM দিয়ে সমাধান**

---

# 🎤 Viva-তে যা জিজ্ঞেস করতে পারে (প্রস্তুতি নিয়ে যাও)

| প্রশ্ন | সংক্ষিপ্ত উত্তরের কাঠামো |
|---|---|
| **AI, ML, DL-এর পার্থক্য কী?** | AI সবচেয়ে বড় গণ্ডি → ML হলো data থেকে শেখা → DL হলো multi-layer neural network |
| **Supervised ও Unsupervised-এর পার্থক্য?** | Label আছে কি নেই; উদাহরণ দাও (spam detection vs customer segmentation) |
| **Overfitting কী, কীভাবে ঠেকাবে?** | মুখস্থ করে ফেলা; Dropout, Regularization, বেশি data, Cross-validation |
| **Accuracy যথেষ্ট নয় কেন?** | Imbalanced data-র উদাহরণ দাও (৯৯০ normal, ১০ spam) |
| **Neural network কীভাবে শেখে?** | Forward → Loss → Backpropagation → Gradient Descent |
| **CNN কেন image-এর জন্য?** | Convolution spatial feature (edge, shape) ধরে, parameter কম লাগে |
| **তুমি MSc-তে কী নিয়ে কাজ করতে চাও?** | একটা নির্দিষ্ট area বলো (যেমন CV বা NLP) + কেন + কোন সমস্যায় প্রয়োগ করতে চাও |

⭐ **শেষ প্রশ্নটার উত্তর আগে থেকে ভেবে রাখো** — এটাই সবচেয়ে বেশি জিজ্ঞেস করা হয়, আর এখানেই তোমাকে আলাদা করে চেনা যায়। BRAC-এ **CVIS Lab** (Computer Vision & Intelligent Systems) আছে — সেটার নাম জানা থাকলে ভালো লাগবে।
