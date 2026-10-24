# Midterm Exam: StyleAI (Fashion-MNIST) — বাংলায় সম্পূর্ণ ব্যাখ্যা

এই নোটটা `Midterm_Exam_Solved.ipynb`-এর প্রতিটা অংশ বাংলায় বুঝিয়ে লেখা — যাতে ভাইভা বা রিভিউতে আটকে না যাও। প্রতিটা প্রশ্নের concept, code আর code-এর পেছনের "কেন" ধাপে ধাপে আছে।

> `Midterm_Exam.ipynb` (অরিজিনাল) touch করা হয়নি। সব সমাধান নতুন ফাইল `Midterm_Exam_Solved.ipynb`-এ।

---

## গল্পটা (Story) কী বলছে

তুমি **StyleAI** নামের একটা স্টার্টআপে কাজ করছো। অ্যাপে ইউজার কাপড়ের ছবি তুললে সেটা কোন ধরনের কাপড় (T-shirt, Trouser, Sneaker ইত্যাদি) তা বলে দিতে হবে।

- ডেটাসেট: **Fashion-MNIST** — ৬০,০০০ training ছবি + ১০,০০০ test ছবি, প্রতিটা **28×28 grayscale**।
- ১০টা class (0 = T-shirt/top ... 9 = Ankle boot)।
- এটা **Multi-class Classification** (২টার বেশি class)। আগের assignment ছিল binary (Forest/Urban)।

---

## কোন প্রশ্নের জন্য কোন Module / Week পড়বে

| প্রশ্ন | সম্পর্কিত Module / Week | ফাইল |
|---|---|---|
| Q1 Part A (Sigmoid vs ReLU) | Mod 5, Mod 8 | `Activation Funciton.pdf`, `Backpropagation.pdf` |
| Q1 Part B (Batch/SGD/Mini-batch) | Mod 13 | `Types of Gradient Descent.pdf`, `batch_vs_stochastic.ipynb` |
| Q1 Part C (CrossEntropy, `backward()`) | Mod 5, 9, 10 | `Binary Cross Entropy.pdf`, `pytorch_autograd.ipynb`, wk2_3 |
| Q2, Q3 (Data, DataLoader) | wk4 | `cs/Hand_Written_Digit_Classification---- wk4.ipynb` |
| Q4 (Model class) | Mod 11, 12, wk4 | `nn_module.ipynb`, wk4 notebook |
| Q5 (Training loop) | Mod 11, 12, wk2_3, wk4 | `pytorch_training_pipeline*.ipynb`, wk2_3 Part 3 |
| Q6 (Plot, Confusion Matrix) | wk4 (HW অংশ) | wk4 notebook-এর শেষে "HW: Accuracy Report, Confusion Matrix" |

### Code-er hint kothay pabe (Code → Mod/Week lookup)

Pore khujte subidha hobe bole, Midterm-er code-er proti ongsho kon mod/week-er kon file theke mille — tar list:

| Amar code | Kon mod/week e ache |
|---|---|
| `nn.Module` + `self.network = nn.Sequential(...)` + `forward(self, features)` | mod 12 `nn_module.ipynb` (Version 3), `Nn module.pdf`; wk4 `Hand_Written_Digit_Classification` |
| `optimizer.zero_grad()` → forward → `criterion` → `loss.backward()` → `optimizer.step()` | mod 12 `pytorch_training_pipeline_updated.ipynb`, mod 13 `batch_vs_stochastic.ipynb` (`train_model`), wk2_3 `Backprop_Autograd_PyTorch_Pipeline` Part 3 |
| `with torch.no_grad():` diye evaluation | mod 11 `pytorch_training_pipeline.ipynb`, mod 12 `pytorch_training_pipeline_updated.ipynb`, wk4 |
| `TensorDataset` + `DataLoader(batch_size, shuffle)` | mod 13 `batch_vs_stochastic.ipynb`, wk4 |
| `loss.item()` diye loss joma kora | mod 13 `batch_vs_stochastic.ipynb`, wk2_3 |
| `loss.backward()` er byakkha (graph, `.grad`, `zero_grad`) | mod 10 `pytorch_autograd.ipynb`, `Autograd for neural network.pdf`; wk2_3 Part 2 |
| Vanishing gradient ar sigmoid derivative `a*(1-a)` | mod 8 `Backpropagation.pdf` / `backpropagation_slide.pptx`, mod 9 `backprop_using_pytorch.ipynb`, wk2_3 (`sigmoid_derivative`) |
| `nn.CrossEntropyLoss`, `optim.SGD`, `model.parameters()` | mod 12 `Nn module.pdf` (built-in loss, optimizer), wk4 |
| Batch vs SGD vs Mini-batch (Q1 Part B) | mod 13 `Types of Gradient Descent.pdf`, `What is gradient descent.pdf`, `batch_vs_stochastic.ipynb` |
| Sigmoid, ReLU, BCE (Q1 Part A, C) | mod 5 `3_activation_functions.ipynb`, `Activation Funciton.pdf`, `Binary Cross Entropy.pdf` |
| Data load, split, tensor (`train_test_split`, `torch.tensor(..., dtype=...)`) | wk4 `Hand_Written_Digit_Classification` |
| `confusion_matrix`, `classification_report` (Q6) | wk4 notebook-er shesh-er "HW: Accuracy Report, Confusion Matrix" |

> Note: mod 8/9/10/11-er onek PDF handwritten (OneNote) scan, tai text search kora jay na — sheigulo directly khule dekhte hobe.

---

## Question 1 — Theory (10 Marks)

### Part A — Sigmoid vs ReLU

| | Sigmoid | ReLU |
|---|---|---|
| Formula | `1 / (1 + e^(-z))` | `max(0, z)` |
| Output | সবসময় (0, 1)-এর মধ্যে | negative হলে 0, positive হলে যা ছিল তাই |
| Gradient (derivative) | সর্বোচ্চ মাত্র **0.25**; z খুব বড়/ছোট হলে প্রায় **0** | z > 0 হলে ঠিক **1**, z < 0 হলে 0 |
| গতি | `exp()` লাগে, ধীর | শুধু compare, খুব দ্রুত |

**ReLU কেন hidden layer-এ ভালো?**
1. হিসাব খুব সহজ ও দ্রুত।
2. positive অংশে gradient = 1, তাই error signal পেছনে যেতে যেতে ছোট হয়ে যায় না।
3. deep network সহজে train হয়।

**Sigmoid-এর সমস্যা — Vanishing Gradient:**
Backpropagation-এ chain rule অনুযায়ী প্রতিটা layer-এর derivative গুণ হয়। Sigmoid-এর derivative ≤ 0.25। ধরো ১০টা layer — তাহলে `0.25 × 0.25 × ... (১০ বার)` ≈ প্রায় ০! মানে শুরুর দিকের layer-গুলো প্রায় কোনো gradient-ই পায় না, তাদের weight আপডেট হয় না, network শেখা বন্ধ করে দেয়। এটাকেই **vanishing gradient** বলে।

### Part B — Gradient Descent-এর তিন ধরন

ধরো ডেটা ৬০,০০০ টা ছবি।

| ধরন | কতগুলো sample দিয়ে gradient বের করে | প্রতি epoch-এ weight update |
|---|---|---|
| **Batch GD** | সব ৬০,০০০ | ১ বার |
| **SGD** | একটা মাত্র sample | ৬০,০০০ বার |
| **Mini-batch GD** | ছোট একটা batch (যেমন ৬৪) | ৬০,০০০ ÷ ৬৪ ≈ ৯৩৮ বার |

- **Batch GD** — সুবিধা: stable, smooth loss curve। অসুবিধা: খুব ধীর, সব ডেটা memory-তে লাগে।
- **SGD** — সুবিধা: দ্রুত update, noise-এর কারণে খারাপ local minimum থেকে বের হতে পারে। অসুবিধা: loss খুব এলোমেলো (zig-zag), GPU ভালোভাবে কাজে লাগে না।
- **Mini-batch GD** — সুবিধা: গতি আর stability-র ভালো ভারসাম্য, GPU-friendly। অসুবিধা: batch size নামে একটা বাড়তি hyperparameter ঠিক করতে হয়।

**Fashion-MNIST-এর জন্য সুপারিশ: Mini-batch GD** (আমরা `batch_size=64` ব্যবহার করেছি)। কারণ ৬০,০০০ ছবি একসাথে নেওয়া ভারী, আর একটা একটা করে নিলে অনেক ধীর ও noisy — mini-batch মাঝামাঝি সবচেয়ে ভালো।

### Part C

**১. `CrossEntropyLoss` কেন, `BCELoss` নয়?**
`BCELoss` শুধু **২ class** (একটা probability) এর জন্য। আমাদের ১০টা class, তাই `CrossEntropyLoss` লাগবে — এটা ১০টা raw score (logits) আর একটা integer label (যেমন 3) নিয়ে হিসাব করে।

**২. শেষে `nn.Softmax` কেন দেবো না?**
`CrossEntropyLoss`-এর ভেতরে **already** `log_softmax` চালানো হয়। আমরা model-এও Softmax দিলে Softmax **দুইবার** apply হবে → মান চ্যাপ্টা হয়ে যায়, gradient দুর্বল হয়, শেখা ধীর/ভুল হয়। তাই model-এর শেষ layer সরাসরি **raw logits** দেবে।

**৩. `loss.backward()` কী করে?**
Autograd দিয়ে computation graph-এ পেছন দিকে গিয়ে chain rule খাটিয়ে প্রতিটা weight/bias-এর জন্য `loss`-এর gradient বের করে `param.grad`-এ রাখে। এরপর `optimizer.step()` সেই gradient দিয়ে weight আপডেট করে। (wk2_3 নোটবুকের Part 2-এ এটাই দেখানো হয়েছে।)

---

## Question 2 — Data Load ও Explore (15 Marks)

### 2.1 Download (দেওয়া code)
`torchvision.datasets.FashionMNIST(..., download=True)` নিজে নিজে ডেটা নামিয়ে `./data` ফোল্ডারে রাখে। এরপর `.data.numpy()` আর `.targets.numpy()` দিয়ে ছবি ও label NumPy array হিসেবে নেওয়া হয়েছে:

```
train_images_all → (60000, 28, 28)     train_labels_all → (60000,)
```

### 2.2 প্রতি class-এর একটা করে ছবি (2×5 grid)

```python
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
axes = axes.flatten()
for i in range(10):
    index = list(train_labels_all).index(i)      # i number class er prothom chobir position
    axes[i].imshow(train_images_all[index], cmap='gray')
    axes[i].set_title(class_names[i])
    axes[i].set_xticks([]); axes[i].set_yticks([])
plt.show()
```

- `subplots(2, 5)` → ২ সারি ৫ কলাম = ১০টা ঘর। `flatten()` করলে 2D grid টা 1D list হয়ে যায়, তাই `axes[i]` দিয়ে সহজে ধরা যায় (wk4 নোটবুকেও একই করা হয়েছে)।
- `list(train_labels_all).index(i)` → label-এর list-এ `i` প্রথম যেখানে আছে সেই position, মানে ওই class-এর **প্রথম** ছবি।
- `cmap='gray'` → grayscale-এ দেখায়। `set_xticks([])` → অক্ষের দাগ বন্ধ।

### 2.3 Class Distribution (Bar chart)

```python
counts = []
for i in range(10):
    counts.append((train_labels_all == i).sum())   # কোন class-এ কয়টা ছবি
plt.bar(class_names, counts)
for i in range(10):
    plt.text(i, counts[i] + 50, str(counts[i]), ha='center')
```

- `(train_labels_all == i).sum()` → label `i`-এর সমান কয়টা আছে তা গুনে দেয়। Fashion-MNIST **balanced** — প্রতি class-এ ঠিক ৬০০০টা করে।
- `plt.text(...)` দিয়ে প্রতিটা bar-এর মাথায় সংখ্যা লেখা হয়েছে।

### 2.4 Tensor বানানো ও Split

```python
train_images_norm = train_images_all / 255.0        # pixel 0-255 → 0-1
X_train_np, X_val_np, y_train_np, y_val_np = train_test_split(train_images_norm, train_labels_all, test_size=10000, random_state=42)
X_train = torch.tensor(X_train_np, dtype=torch.float32)
y_train = torch.tensor(y_train_np, dtype=torch.long)
```

- **255.0 দিয়ে ভাগ কেন?** ছোট (0–1) মানে gradient descent দ্রুত ও stable converge করে। বড় মান (0–255) হলে training অস্থির হতো।
- `test_size=10000` → ৬০,০০০ থেকে ঠিক ১০,০০০ validation, বাকি ৫০,০০০ train। `random_state=42` → প্রতিবার একই ভাগ।
- **float32** কারণ model-এর weight float32; **long** কারণ `CrossEntropyLoss` class label হিসেবে integer (long) চায়।

---

## Question 3 — DataLoader (10 Marks)

```python
train_dataset = TensorDataset(X_train, y_train)
train_loader  = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader    = DataLoader(val_dataset,   batch_size=64, shuffle=False)
test_loader   = DataLoader(test_dataset,  batch_size=64, shuffle=False)
```

- `TensorDataset` ছবি আর label কে জোড়া (pair) করে রাখে।
- `DataLoader` সেটাকে ৬৪টা করে batch-এ ভেঙে দেয় — এটাই **Mini-batch GD**।
- `shuffle=True` শুধু **train**-এ: প্রতি epoch-এ ক্রম এলোমেলো করলে model একই ক্রম মুখস্থ করতে পারে না। Validation/Test-এ shuffle লাগে না (শুধু মাপছি, শিখছি না)।

---

## Question 4 — Model (15 Marks)

```python
class FashionClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(input_size, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 64),  nn.ReLU(),
            nn.Linear(64, num_classes)
        )
    def forward(self, features):
        output = self.network(features)
        return output

model = FashionClassifier(input_size=28*28, num_classes=10)
print(model)
```

- `nn.Module` — PyTorch-এর সব model-এর base class। `super().__init__()` ভুলে গেলে error!
- `nn.Flatten()` — `(batch, 28, 28)` কে `(batch, 784)` বানায়, কারণ `Linear` সমতল (flat) input চায়। 28×28 = 784।
- `nn.Linear(input_size, 256)` (`input_size = 28*28 = 784`, wk4-এর মতো argument হিসেবে দেওয়া) — ৭৮৪টা input থেকে ২৫৬টা neuron। এভাবে 256 → 128 → 64 → 10 করে size কমতে থাকে।
- `ReLU` — layer-গুলোর মাঝে non-linearity দেয় (না দিলে ১০ layer = ১ layer হয়ে যেত)।
- **শেষ layer-এ Softmax নেই** — কারণ Q1 Part C-তে বলা হয়েছে (CrossEntropyLoss নিজেই করে)।
- মোট parameter = 242,762 (টেস্ট সেলে দেখা যায়)।

---

## Question 5 — Training (25 Marks)

### 5.1 Setup
```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
epochs = 15
```
- `criterion` = loss কতটা ভুল হলো মাপার যন্ত্র।
- `optimizer` = ওই ভুল কমাতে weight কীভাবে বদলাবে (`SGD`, learning rate 0.01)।
- `model.parameters()` — এর মাধ্যমে optimizer জানে কোন কোন weight বদলাতে হবে।

### 5.2 Training Loop — ৫টা ধাপ (মুখস্থ রাখো!)

```python
for images, labels in train_loader:
    optimizer.zero_grad()              # 1. আগের gradient মুছো
    outputs = model(images)            # 2. forward pass
    loss = criterion(outputs, labels)  # 3. loss হিসাব
    loss.backward()                    # 4. backward pass (gradient বের করা)
    optimizer.step()                   # 5. weight update
```

- **কেন `zero_grad()` আগে?** PyTorch gradient **জমা (accumulate)** করে। মুছে না দিলে আগের batch-এর gradient এর সাথে যোগ হয়ে ভুল update হবে।
- **Validation-এ `torch.no_grad()`** — gradient track বন্ধ → memory ও সময় বাঁচে, আর validation-এ weight বদলানোর দরকারও নেই।
- **Accuracy:** `torch.argmax(outputs, dim=1)` প্রতিটা ছবির ১০টা score-এর মধ্যে সবচেয়ে বড়টার index (= predicted class) দেয়। `(preds == labels).sum()` দিয়ে সঠিক গুনে মোট দিয়ে ভাগ।
- `train_losses`, `val_losses`, `train_accuracies`, `val_accuracies` — প্রতি epoch-এ একটা করে মান list-এ রাখা হয়েছে (পরে plot করার জন্য)। Test cell `train_accuracies` ব্যবহার করে, তাই এটা না বানালে error আসতো।
- Loss = batch-গুলোর **average** (`running_loss / len(train_loader)`), যাতে মানটা পড়তে সহজ হয়।

### 5.3 Test Evaluation
```python
with torch.no_grad():
    y_pred_prob = model(X_test)          # wk4-এর মতো পুরো X_test একবারে

y_pred = torch.argmax(y_pred_prob, dim=1)
all_preds = y_pred.tolist()
all_labels = y_test.tolist()
test_accuracy = (y_pred == y_test).float().mean().item() * 100
```
- Test set model আগে কখনো দেখেনি — তাই এটাই আসল পরীক্ষা।
- আমার run-এ **test accuracy ≈ 82–84%** এসেছে (প্রতিবার weight random শুরু হয় বলে ±১–২% হতে পারে)। শর্ত ছিল > 40%।

---

## Question 6 — Visualize ও Analysis (25 Marks)

### 6.1 / 6.2 — Loss ও Accuracy Curve
`plt.plot(range(1, epochs+1), train_losses, label=...)` দিয়ে train আর validation এক গ্রাফে। `legend()`, `title`, `xlabel`, `ylabel` দিতে ভুলো না (marks আছে)।

### 6.3 — Confusion Matrix
```python
cm = confusion_matrix(all_labels, all_preds)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap='Blues', xticks_rotation=45)
```
- সারি (row) = আসল class, কলাম = model যা বলেছে।
- **Diagonal** = সঠিক। Diagonal-এর বাইরের বড় সংখ্যা = ভুল (confusion)।

### 6.4 — Classification Report
`classification_report(all_labels, all_preds, target_names=class_names)`
- **Precision** = model যতবার "এটা Shirt" বলেছে তার মধ্যে কতবার ঠিক।
- **Recall** = আসল Shirt-গুলোর মধ্যে কতগুলো model ধরতে পেরেছে।
- **F1** = precision ও recall-এর ভারসাম্যপূর্ণ গড়।

### 6.5 — Written Analysis

**১. কোন দুই class সবচেয়ে বেশি confuse হয়?**
উপরের অংশে পরার কাপড়গুলো নিজেদের মধ্যে confuse হয়: **Shirt, T-shirt/top, Pullover, Coat**। **Shirt** সবসময় সবচেয়ে দুর্বল (F1 ~০.৬)। আমার run-এর confusion matrix-এ diagonal-এর বাইরের সবচেয়ে বড় সংখ্যা: **Pullover → Coat (~৩৩০)**, **Shirt → Coat (~১৮৭)**, **T-shirt/top → Shirt (~১৩৭)**। তাই সবচেয়ে বেশি confused জোড়া **Pullover ↔ Coat** (সাথে Shirt ↔ Coat / T-shirt)। (weight প্রতিবার random শুরু হয়, তাই সংখ্যা একটু বদলাবে — নিজের matrix দেখে লিখো।)
**কারণ:** এগুলো সবই উপরের অংশে পরার কাপড় — আকৃতি প্রায় এক (শরীর + হাতা + গলা)। ছবি মাত্র 28×28 grayscale হওয়ায় কলার, বোতাম, জিপার, হাতার দৈর্ঘ্যের মতো ছোট পার্থক্য প্রায় মুছে যায়। আমাদের MLP শুধু raw pixel দেখে, আকৃতি/টেক্সচার বুঝতে পারে না। অন্যদিকে Trouser, Bag, Sandal, Sneaker, Ankle boot দেখতে একেবারে আলাদা, তাই এদের score ভালো (~০.৯২–০.৯৭)।

**২. Overfitting নাকি Underfitting?**
**Overfitting নয়** — বরং একটু **underfitting / এখনো শিখছে**।
- Overfitting হলে train loss কমতে থাকতো কিন্তু validation loss **বাড়তে** শুরু করতো, আর train accuracy অনেক বেশি হতো validation-এর চেয়ে। এখানে দুটোই একসাথে কমছে এবং শেষে কাছাকাছি (train ≈ ৮৫%, val ≈ ৮৩–৮৫%)।
- Test accuracy (~৮২–৮৪%) ও validation accuracy প্রায় সমান → model নতুন ডেটাতেও ভালো কাজ করছে (generalize করছে)।
- তবে curve এখনো পুরো সমান (flat) হয়নি, কারণ আমরা plain SGD, ছোট `lr=0.01`, momentum ছাড়া মাত্র ১৫ epoch চালিয়েছি। আরো epoch, বড় lr/momentum বা Adam দিলে আরো ভালো হবে। Validation loss-এর ছোট ওঠানামা mini-batch SGD-র noise, overfitting নয়।

---

## পুরো pipeline এক নজরে (ভাইভার জন্য)

```
Data load → Normalize (/255) → Train/Val split → Tensor → TensorDataset → DataLoader
   → Model (nn.Module) → Loss (CrossEntropy) + Optimizer (SGD)
   → Loop: zero_grad → forward → loss → backward → step
   → Validation (no_grad) → Test → Confusion Matrix / Report → Analysis
```

## সাধারণ ভুল (Common Mistakes)

| ভুল | ফল |
|---|---|
| Model-এর শেষে `Softmax` দেওয়া | Softmax দুইবার হয়, training খারাপ হয় |
| Label `float` রাখা | `CrossEntropyLoss` error দেয় — `long` লাগবে |
| `zero_grad()` ভুলে যাওয়া | gradient জমে ভুল update হয় |
| Validation-এ `no_grad()` না দেওয়া | memory নষ্ট, ধীর |
| Pixel normalize না করা | training ধীর ও অস্থির |
| Train loader-এ `shuffle=False` | model ক্রম মুখস্থ করে ফেলতে পারে |
