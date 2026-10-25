# Final Exam: TranslateAI (KMNIST) — Banglish e shompurno byakkha

Ei note ta `DL_Final_Exam_Solved.ipynb` er proti ongsho Banglish e bujhiye lekha, jate viva/review te atke na jao. Proti question er concept, code ar code er pechoner "keno" dhape dhape ache.

> `DL_Final_Exam_Question.ipynb` (original question) touch kora hoyni. Shob solve notun file `DL_Final_Exam_Solved.ipynb` e.

---

## Story ta ki bolche

Tumi **TranslateAI** e ML Engineer. Museum er prachin Japanese cursive (hater lekha) akkhor automatic chinte hobe.

- Dataset: **KMNIST** — 60,000 train + 10,000 test chobi, proti ta **28×28 grayscale**.
- 10 ta class: `o, ki, su, tsu, na, ha, ma, ya, re, wo` (label 0 theke 9).
- Eta **Multi-class Classification** (10 class), Midterm er moto, kintu ei bar extra jinish: **Batch Normalization** + **Adam optimizer** + **GPU/CPU device**.

---

## Question-wise Mod map (kon part kon mod theke)

| Exam part | Ki korte hobe | Kon mod/week theke | Kon file |
|---|---|---|---|
| **Q1.1** (5) Download | `KMNIST(..., download=True)` | Question er deya code | Midterm er `FashionMNIST` cell er moto |
| **Q1.2** (5) Sample chobi | 2x5 grid, `cmap='gray'` | wk4 | `Hand_Written_Digit_Classification` (imshow/subplots) |
| **Q1.3** (10) Scaling + split + tensor | MinMax, 50k/10k split, float32/long | Scaling: **mod 18**; split/tensor: wk4 | mod 18 `Normalization.ipynb`, `Normalization.pdf`; wk4 |
| **Q2** (15) DataLoader | batch 256, shuffle | wk4, **mod 13**, mod 15/16 | wk4; mod 13 `batch_vs_stochastic.ipynb`; mod 15 `All.pdf` (DataLoader parameters) |
| **Q3** (25) Model + BatchNorm | `Linear → BatchNorm1d → ReLU` | **mod 19**, mod 12, wk4 | mod 19 BatchNorm notebook + `What is Batch Norm..pdf`; mod 12 `nn_module.ipynb` |
| **Q4.1** (5) Loss + Adam | `CrossEntropyLoss`, `Adam(lr=0.001)` | **mod 20**, mod 18, mod 16 (device) | mod 20 `All Optimizers.pdf`, `optimizers_pytorch.pdf`; mod 18 `data_scaling_example_pytorch.ipynb`; mod 16 GPU notebook |
| **Q4.2** (20) Training loop | `train()`, loop, `eval()`, val loss/acc | **mod 16, 19**, mod 13, wk2_3 | mod 16 / 19 training + evaluation cell; mod 13 `train_model`; wk2_3 Part 3 |
| **Q5.1** (5) Test accuracy, `all_preds` | `no_grad`, `torch.max` | mod 16 / 19 evaluation cell, wk4 | mod 16 / 19 ("evaluation code" cell) |
| **Q5.2** (5) Learning curve | loss plot, legend, title | wk2_3, mod 18 | wk2_3 `plt.plot(losses)` |
| **Q5.3** (5) Confusion matrix + analysis | `ConfusionMatrixDisplay` + likha | Kono mod e code nai (wk4 te shudhu "HW" lekha) | Amar nijer (sklearn); analysis amar run theke |

> `student_email` cell: Assignment 1 er moto email string.

---

## Kon code kothay theke ashche (Source lookup)

Ekhane likha ache proti code-er ongsho **exact kon file er kon cell** theke, ar ta **hubohu mod er**, **mod er moto kore ami likhechi**, na **mod e nai (amar nijer)**. (Cell number = notebook er 0 theke gona cell index.)

| Final exam er code | Source (file + cell) | Status |
|---|---|---|
| Imports, `class_names`, `KMNIST(..., download=True)` | Question notebook er deya code (cell 5) | Question er deya |
| `.data.numpy()`, `.targets.numpy()` | Question hint ("extract as NumPy"); `FashionMNIST` e Midterm er deya cell 7 e same | Question er deya style |
| `plt.subplots(2,5)`, `flatten()`, `imshow(cmap='gray')`, `set_title`, `set_xticks([])` | wk4 `Hand_Written_Digit_Classification` cell 8 (`subplots(2,5)`, `flatten`, `imshow`, `set_title`, `axis('off')`) | Mod er moto, `set_xticks([])` question er instruction |
| `list(train_labels_all).index(i)` (class er prothom chobi) | Kono mod e nai | **Amar nijer** |
| MinMax `(x - x_min) / (x_max - x_min)` | mod 18 `Normalization.ipynb` cell 0 (manual min-max) | Formula mod er, code ta amar |
| `x_min`, `x_max` shudhu train theke, test e same | Kono mod e nai (data leakage er niyom) | **Amar nijer** |
| `train_test_split(..., test_size=10000, random_state=42)` | wk4 cell 9 (`test_size=0.1`), question e 10,000 bola | Mod er moto, number question er |
| `torch.tensor(..., dtype=torch.float32 / torch.long)` | wk4 cell 9 | Hubohu mod er moto |
| `TensorDataset` + `DataLoader(batch_size, shuffle)` | wk4 cell 11; mod 13 `batch_vs_stochastic.ipynb` cell 4 | Hubohu mod er moto (batch_size 256 question er) |
| `class ... (nn.Module)`, `self.network = nn.Sequential`, `forward(self, features)`, `input_size`/`num_classes` arguments | wk4 cell 12; mod 12 `nn_module.ipynb` cell 5 | Hubohu mod er moto |
| `nn.Linear → nn.BatchNorm1d → nn.ReLU` | mod 19 `ann_fashion_mnist_pytorch_gpu_optimized_with_batchNorm.ipynb` cell 14 (`Linear(128)`, `BatchNorm1d(128)`, `ReLU`) | Hubohu mod er pattern (size question er) |
| `torch.manual_seed(42)` | mod 16 / mod 19 cell 1 | Hubohu mod er |
| `device = torch.device('cuda' if ... else 'cpu')`, `model.to(device)` | mod 16 / mod 19 cell 2 ar cell 16 | Hubohu mod er |
| `nn.CrossEntropyLoss()` | wk4 cell 14; mod 16/19 cell 16 | Hubohu mod er |
| `optim.Adam(model.parameters(), lr=0.001)` | mod 18 `data_scaling_example_pytorch.ipynb` cell 6 (`optim.Adam(..., lr=0.001)`) | Hubohu mod er (mod 16/19 e SGD, Adam noy) |
| Training loop: `.to(device)`, forward, loss, `zero_grad`, `backward`, `step`, `loss.item()`, `total / len(train_loader)` | mod 16 / mod 19 cell 17 (training loop) | Hubohu mod er moto |
| `model.train()` | Kono mod e nai, question er step 1 e bola | Question er instruction |
| `model.eval()` | mod 16 / mod 19 cell 18 | Mod er |
| Validation: `with torch.no_grad()`, `torch.max(outputs, 1)`, `correct`/`total` | mod 16 / mod 19 cell 19 (evaluation code), wk4 cell 17 | Hubohu mod er moto |
| `val_loss` hisab ar `val_losses.append(...)` list | Loss list: wk2_3 `losses.append`; validation loss loop: wk4 cell 15 | Mod er moto, ami jorlam |
| `all_preds.extend(predicted.cpu().tolist())` | Kono mod e nai | **Amar nijer** |
| `plt.plot(train_losses)`, `legend`, `title`, `xlabel` | wk2_3 cell 18 / cell 34 (`plt.plot(losses)`) | Mod er moto |
| `confusion_matrix`, `ConfusionMatrixDisplay(...).plot()` | wk4 cell 18 e shudhu "HW: Accuracy Report, Confusion Matrix" lekha, **code nai** | **Amar nijer** (sklearn doc) |
| 5.3 analysis (kon class confuse) | Amar run er confusion matrix dekhe | **Amar nijer** (tomar run e alada hobe) |

**Theory er jonno ami ei note gulo poRe nichhe update korechi (niche "Mod note theke theory" section dekho):**
mod 17 `All.pdf` (loss function + vanishing gradient), mod 18 (`Why Scaling`, `Standardization`, `Normalization`, `Standardization vs Normalization`), mod 19 `What is Batch Norm..pdf`, mod 20 (`All Optimizers`, `EWMA`, `Previous optimizers`, `optimizers_types`, `optimizers_pytorch`).

**Ekhono poRini:** mod 19 `research_paper.pdf` (shudhu cover), mod 16 `All.pdf` / `cpu_to_gpu.pdf`, mod 16 `ann_project_with_cpu.ipynb`, mod 15 baki notebook, mod 17 `vanishing_gradient_problem.ipynb`, mod 18 `Standardization.ipynb`, mod 1–11 er scan PDF, `cs` wk1/5/6.

> Note: onek PDF handwritten (OneNote) scan, tai text search kora jay na — sheigulo directly khule dekhte hobe.

---

## Mod note theke theory (BatchNorm, Adam, Scaling, Vanishing Gradient)

### Mod 19 — Batch Normalization (`What is Batch Norm..pdf`)
- **Ki?** Training ke druto ar stable korar technique. Hidden layer er activation er value ke **current mini-batch er mean ar variance** diye normalize kore. Linear (Z) er pore, activation er age ba pore boshano hoy.
- **Internal Covariate Shift:** training cholar shomoy ager layer er weight bodlay, tai porer layer er input distribution bar bar bodlay → training dhimi ar osthir hoy, choto learning rate lage, deep network converge korte kosto hoy. BatchNorm eta kombay.
- **Note e dekha hoyechilo (hater lekha):** BatchNorm **mini-batch** ar **layer by layer** kaj kore. Normal flow: `Z → g(Z) → a`. BatchNorm flow: `Z → Z_norm → Z_BN → g(Z_BN) → a`.
- **Step 1 (normalize):** `Z_norm = (Z - μ_B) / (σ_B + ε)` — `μ_B` = batch er mean, `σ_B` = batch er std, `ε` = choto number (0 diye bhag na hoy).
- **Step 2 (scaling & shifting):** `Z_BN = γ · Z_norm + β` — `γ` (gamma) ar `β` (beta) **learnable parameter**. Shurute `γ = 1`, `β = 0`. Model nije shikhe normalize kora value ke kotota scale/shift korbe.
- **Shape example (note er):** input `(4, 2)` × weight `(2, 2)` + bias `(1, 2)` = `(4, 2)`; `m = 4` (batch size).
- PyTorch e: `nn.BatchNorm1d(features)` — `features` = ager Linear er output size.

### Mod 17 — Vanishing Gradient ar Loss Function (`All.pdf`)
- **Vanishing Gradient (note):** deep NN + sigmoid/tanh hole backprop e chhoto derivative gulo (jemon 0.1 × 0.1 × 0.1 ...) gun hoy, tai ager layer er gradient prai 0 hoye jay → weight update hoy na (`W_new = W_old - η ∂L/∂W`).
- **Samadhan (note e 3 ta):** (1) network er complexity komano, (2) **ReLU** use kora, (3) **Batch Normalization**.
- **Loss function (note):** Regression: MSE, MAE, Huber. Classification: Binary Cross Entropy, **Categorical Cross Entropy**, Hinge loss. Categorical CE formula: `L = - Σ y_j log(ŷ_j)` (one-hot label). Subidha: probability er shathe naturally kaj kore, multi-class e effective. Osubidha: bhul label ar class imbalance e sensitive.

### Mod 18 — Data Scaling (`Why Scaling`, `Standardization`, `Normalization`, `Standardization vs Normalization`)
- **Keno scaling?** Weight update formula `W_new = W_old - η ∂L/∂W`. Feature er scale alada hole (jemon Age vs Salary) loss er contour lomba/elomelo hoy (gradient descent zigzag kore), scale kore dile contour gol hoy ar gradient descent shoja minimum e jay (note er chobi: Unnormalized vs Normalized).
- **Standardization:** `z = (x - x̄) / σ` → mean = 0, std = 1. Neural network, Logistic/Linear Regression, SVM, PCA te use hoy; outlier beshi handle kore.
- **Normalization (MinMax):** `x' = (x - x_min) / (x_max - x_min)` → value `[0, 1]` er moddhe. Image data (pixel 0–255 → 0–1), KNN, K-means e use hoy. Outlier thakle baki value gulo chepe jay.
- **Final exam e:** question e "MinMax Scaling" bola, tai Normalization formula use korechi.

### Mod 20 — Optimizers (`All Optimizers`, `EWMA`, `optimizers_types`, `optimizers_pytorch`)
- **Basic update:** `W_new = W_old - η ∂L/∂W`. GD/SGD/Mini-batch er problem (note): convergence time ar local minima, ar SGD te noise/zigzag.
- **EWMA (Exponentially Weighted Moving Average):** `V_t = β V_{t-1} + (1 - β) θ_t` — purono data ke kom ar notun data ke beshi gurutto dey (smoothing). Time series (stock, temperature) e use hoy.
- **SGD with Momentum:** (1) momentum = smoothing, (2) dynamic learning rate. `V_dw_t = β V_dw_{t-1} + (1 - β) ∂L/∂w`, `w_t = w_{t-1} - η V_dw`. Zigzag (noise) kome, gorbi (rolling ball) shoja dike jay.
- **AdaGrad:** `W_new = W_old - η/√(α_t + ε) · ∂L/∂W`, `α_t = Σ (∂L/∂w)²`. Proti parameter er alada learning rate; kintu **learning rate kromagoto chhoto hoye jay** (core problem).
- **RMSProp:** AdaGrad er shrink hoy problem fix kore, shob gradient joma na kore **EWMA** use kore: `S_dw_t = β S_dw_{t-1} + (1 - β)(∂L/∂w)²`, `η' = η / √(S_dw + ε)`.
- **Adam:** **Momentum + RMSProp** ekshathe: `w_{t+1} = w_t - η / √(S_dw_t + ε) · V_dw_t` (ar bias er jonno `b` e eki rokom). Druto converge kore, beshirbhag problem e bhalo, practice e default choice.
- **PyTorch e:** `optim.SGD(model.parameters(), lr=0.01, momentum=0.9)`, `optim.Adam(model.parameters(), lr=0.001)`, `optim.RMSprop`, `optim.Adagrad`, `optim.AdamW` (Adam er better version). Training loop shob optimizer e ekoi: `zero_grad → forward → loss → backward → step`.
- **Final exam e:** `optim.Adam(model.parameters(), lr=0.001)` — mod 20 note er example er hubohu.

---

## Question 1 — Load, Explore, Preprocess (20 Marks)

### 1.1 Download (deya code)

```python
full_train_dataset = torchvision.datasets.KMNIST(root='./data', train=True, download=True)
test_dataset_raw  = torchvision.datasets.KMNIST(root='./data', train=False, download=True)
```

- `download=True` mane data na thakle nije download kore `./data` folder e rakhe. Tai ei cell **ek bar run korlei hobe**.
- Jodi `HTTP Error 403: Forbidden` ashe, mane KMNIST er official server (`codh.rois.ac.jp`) tomar network ke block korche. Tokhon alternative theke data nite hobe (instructor ke / amake bolo).

### 1.2 Protiti class er ekta kore chobi (2×5 grid)

```python
train_images_all = full_train_dataset.data.numpy()      # (60000, 28, 28)
train_labels_all = full_train_dataset.targets.numpy()   # (60000,)

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
axes = axes.flatten()

for i in range(10):
    index = list(train_labels_all).index(i)
    axes[i].imshow(train_images_all[index], cmap='gray')
    axes[i].set_title(class_names[i])
    axes[i].set_xticks([])
    axes[i].set_yticks([])
plt.show()
```

- `subplots(2, 5)` → 2 shari 5 column = 10 ta ghor. `flatten()` korle 2D grid ta 1D list hoy, tai `axes[i]` diye shohoje dhora jay.
- `list(train_labels_all).index(i)` → label list e `i` prothom jekhane ache oi position, mane oi class er **prothom chobi**.
- `cmap='gray'` grayscale e dekhay. `set_xticks([])` mane axis er dag bondho.

### 1.3 MinMax Scaling + Split + Tensor (10 Marks)

```python
x_min = train_images_all.min()
x_max = train_images_all.max()
train_images_scaled = (train_images_all - x_min) / (x_max - x_min)
test_images_scaled  = (test_images_all  - x_min) / (x_max - x_min)

X_train_np, X_val_np, y_train_np, y_val_np = train_test_split(
    train_images_scaled, train_labels_all, test_size=10000, random_state=42)

X_train = torch.tensor(X_train_np, dtype=torch.float32)
y_train = torch.tensor(y_train_np, dtype=torch.long)
```

- **MinMax Scaling formula** (mod 18): `(x - min) / (max - min)`. Pixel 0–255 hole formula `x / 255` er soman, ar value `[0, 1]` er moddhe ashe.
- **Keno scaling?** Boro value (0–255) hole gradient descent osthir/dhimi hoy. Choto value hole training druto ar stable.
- `x_min`, `x_max` **shudhu train data** theke nilam, test e **same value** use korlam. Test er data ke model "dekhe" felle seta data leakage hoto.
- `test_size=10000` → 60,000 theke thik 10,000 validation, baki 50,000 train. `random_state=42` → protibar ekei bhag.
- Image **float32** (model er weight float32), label **long** (`CrossEntropyLoss` integer class label chay).

---

## Question 2 — DataLoader (15 Marks)

```python
train_dataset = TensorDataset(X_train, y_train)
train_loader  = DataLoader(train_dataset, batch_size=256, shuffle=True)
val_loader    = DataLoader(val_dataset,   batch_size=256, shuffle=False)
test_loader   = DataLoader(test_dataset,  batch_size=256, shuffle=False)
```

- `TensorDataset` chobi ar label ke jora (pair) kore rakhe.
- `DataLoader` setake **256 ta kore batch** e bhange → eta **Mini-batch Gradient Descent** (mod 13).
- `shuffle=True` shudhu **train** e: protibar kromo elomelo korle model ekoi kromo mukhosto korte pare na. Validation/Test e shuffle lage na.
- Batch size 256 boro hole BatchNorm er jonno bhalo, karon batch er mean/std beshi stable hoy.

---

## Question 3 — Model with BatchNorm (25 Marks)

```python
class TranslateAIClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(input_size, 512), nn.BatchNorm1d(512), nn.ReLU(),
            nn.Linear(512, 256),        nn.BatchNorm1d(256), nn.ReLU(),
            nn.Linear(256, 128),        nn.BatchNorm1d(128), nn.ReLU(),
            nn.Linear(128, num_classes)
        )
    def forward(self, features):
        output = self.network(features)
        return output

model = TranslateAIClassifier(input_size=28*28, num_classes=10)
print(model)
```

- `Flatten` → `(batch, 28, 28)` ke `(batch, 784)` banay.
- Layer order: **Linear → BatchNorm1d → ReLU** (mod 19 er moto). `BatchNorm1d(512)` er `512` hocche **ager Linear er output size** (feature number), tai mile thakte hobe.
- **BatchNorm ki kore?** (mod 19 note) Step 1: `(Z - μ_B)/(σ_B + ε)` diye mean ≈ 0, std ≈ 1 kore. Step 2: `γ·Z_norm + β` (learnable, shurute γ=1, β=0) diye abar scale/shift kore.
- **BatchNorm er subidha** (mod 19 note + mod 17 note): (1) training druto o stable hoy (Internal Covariate Shift kombe), (2) boro learning rate use kora jay, (3) vanishing gradient er 3 ta samadhan er ekta (mod 17), (4) (amar byakkha) ektu regularization effect ache.
- **Shesh layer e Softmax nei** — `CrossEntropyLoss` nijei `log_softmax` kore, Softmax dile 2 bar hoye jay.
- `torch.manual_seed(42)` → protibar eki shuru-weight pabe, tai result mota-muti same thake.
- Test cell `model(test_input)` **CPU** tensor diye chalay, tai model ke `.to(device)` **Q3 er pore (4.1 e)** korechi. Age korle GPU te error ashto.

---

## Question 4 — Training Pipeline (25 Marks)

### 4.1 Setup

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 15
```

- `device` → GPU thakle GPU, na hole CPU. `model.to(device)` model ke oi device e pathay (mod 16).
- **Adam** (mod 20 note: **Momentum + RMSProp**; code mod 18 theke): SGD er theke onek druto converge kore. Eta **momentum** (ager gradient er EWMA) ar **adaptive learning rate** (proti parameter er alada step) duto ekshathe use kore. `lr=0.001` Adam er common default.
- `model.parameters()` → optimizer ke bole kon weight gulo update korte hobe.

### 4.2 Training Loop

```python
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for batch_features, batch_labels in train_loader:
        batch_features, batch_labels = batch_features.to(device), batch_labels.to(device)
        outputs = model(batch_features)               # 1. forward
        loss = criterion(outputs, batch_labels)       # 2. loss
        optimizer.zero_grad()                         # 3. ager gradient muche felo
        loss.backward()                               # 4. backward
        optimizer.step()                              # 5. weight update
        running_loss += loss.item()
    train_loss = running_loss / len(train_loader)

    model.eval()
    ...
    with torch.no_grad():
        for batch_features, batch_labels in val_loader:
            ...
```

- **`model.train()` vs `model.eval()` — BatchNorm er jonno khub joruri!**
  - `train()` mode e BatchNorm **current batch er** mean/std use kore ar ekta *running average* joma rakhe.
  - `eval()` mode e BatchNorm **training e joma kora running mean/std** use kore (batch er upor nirbhor kore na). Eta bhule gele validation/test er result ulta-palta hoy.
- `zero_grad()` keno? PyTorch gradient **joma** kore. Na muchle ager batch er gradient er shathe jog hoye bhul update hobe.
- `with torch.no_grad()` → validation e gradient track bondho (memory/somoy bachay, weight o bodlay na).
- `_, predicted = torch.max(outputs, 1)` → 10 ta score er moddhe sobcheye boro ta r index = predicted class.
- `train_losses`, `val_losses` e proti epoch er ekta kore value rakha (pore plot er jonno). Ami `val_accuracies` o rekhechi (question e "validation loss **and accuracy**" compute korte bolechilo).
- Print format question er moto: `Epoch {epoch+1}/{epochs} | Train Loss: ... | Val Loss: ...`.

---

## Question 5 — Evaluation (15 Marks)

### 5.1 Test Accuracy

```python
model.eval()
all_preds, all_labels = [], []
with torch.no_grad():
    for batch_features, batch_labels in test_loader:
        batch_features, batch_labels = batch_features.to(device), batch_labels.to(device)
        outputs = model(batch_features)
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().tolist())
        all_labels.extend(batch_labels.cpu().tolist())
        ...
test_accuracy = 100 * correct / total
```

- Test data model age kokhono dekheni, tai eta-i asol porikkha.
- `.cpu().tolist()` → GPU te thakle age CPU te ene tarpor list banano lage.
- Amar run e **Test Accuracy ≈ 91.5%** esechilo (weight random, tai ±1% hote pare).

### 5.2 Learning Curves
`plt.plot(train_losses, label=...)` + `plt.plot(val_losses, label=...)`, sathe `title`, `xlabel`, `ylabel`, `legend()`.

### 5.3 Confusion Matrix ar Analysis

```python
cm = confusion_matrix(all_labels, all_preds)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap='Blues')
```

- Shari (row) = asol class, column = model ja bolechilo. **Diagonal** = thik, **diagonal er baire** boro shongkha = bhul (confusion).
- Amar run e boro confusion: **su → tsu (~55)**, **ha → su (~44)**, **ki → ma (~39)**, **na → o (~36)**, **na → re (~30)**.
- **Keno?** Eigulo cursive (hater lekha) akkhor. `su` ar `tsu` du ta tei bokro/hook er moto shape, `ki`/`ma`/`ha` er stroke kaka-kaki, `na` er lombha lej `o`/`re` er moto. 28×28 pixel e chhoto parthokyo mushe jay, ar amader MLP shudhu pixel dekhe, stroke/shape bujhte pare na.
- **Learning curve theke:** train loss prai 0 hoye jay, kintu validation loss ~epoch 5 er por ar kome na (upor-nich kore). Mane model ektu **overfit** korche (training chobi mukhosto korche). BatchNorm + Adam training ke druto o stable koreche, kintu overfitting kombate Dropout, weight decay ba early stopping lagbe.

---

## Pura pipeline ek nojore (viva r jonno)

```
Download → numpy → MinMax scale → Train/Val split → Tensor → TensorDataset → DataLoader
   → Model (Linear → BatchNorm → ReLU ...) → .to(device)
   → Loss (CrossEntropy) + Optimizer (Adam)
   → Loop: model.train() → [forward → loss → zero_grad → backward → step]
           model.eval()  → [no_grad → val loss/acc]
   → Test → Confusion Matrix → Analysis
```

## Common bhul (Common Mistakes)

| Bhul | Fol |
|---|---|
| BatchNorm er size bhul (`BatchNorm1d(256)` ager Linear e 512 hole) | Shape error |
| `model.eval()` bhule jaoa | BatchNorm batch er stat use kore, validation/test result khub noisy |
| Shesh layer e `Softmax` dewa | Softmax 2 bar hoy, training kharap |
| Label `float` rakha | `CrossEntropyLoss` error, `long` lagbe |
| `zero_grad()` bhule jaoa | Gradient joma hoye bhul update |
| Test er jonno alada min/max (test theke) nea | Data leakage, train er min/max e use korte hobe |
| GPU te model, CPU te data (ba ulta) | Device mismatch error, data o `.to(device)` korte hobe |
| Validation e `no_grad()` na dewa | Memory nosto, dhimi |
