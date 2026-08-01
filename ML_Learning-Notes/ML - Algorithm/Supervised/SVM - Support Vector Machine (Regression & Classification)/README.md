# Support Vector Machine (SVM) — The Widest-Street Algorithm

One algorithm, two jobs: **SVC** draws the widest possible street between classes; **SVR** fits the tightest tube around a curve. Same core idea (`margin`), opposite direction of use.

---

## 1. What Is It & Where Does It Sit

Support Vector Machine is a **supervised** learning algorithm. It handles **both**:

- **Classification → SVC** (Support Vector Classifier): predicts a discrete class label.
- **Regression → SVR** (Support Vector Regressor): predicts a continuous number.

Both live under `sklearn.svm` (`SVC`, `SVR`, plus linear-optimized variants `LinearSVC`/`LinearSVR`). Both share the same core object — a hyperplane defined by `w` and `b` — and the same core trick — the **kernel trick** — to bend that hyperplane around non-linear data without hand-engineering features.

**বাংলা ইনটুইশন:** SVM মূলত একটাই ধারণা — "সবচেয়ে কাছের পয়েন্টগুলোর থেকে যতটা সম্ভব দূরে থেকে একটা সীমারেখা টানো।" Classification-এ সীমারেখাটা দুটো ক্লাসকে আলাদা করে, Regression-এ সীমারেখাটা একটা tube হয়ে ডেটার মধ্যে দিয়ে যায়।

---

## 2. Where It Comes From & Why It Was Invented

SVM comes from **Vladimir Vapnik and Alexey Chervonenkis**, rooted in their **statistical learning theory** and the concept of **VC-dimension** (a measure of how complex/flexible a model class is, and hence how well it should be expected to generalize). The core theoretical insight: among all the boundaries that separate two classes perfectly, the one that **maximizes the margin** (the gap to the nearest points of each class) has the best theoretical bound on generalization error — it is the least likely to overfit to noise near the boundary.

This was a principled alternative to two things:

1. **Logistic regression's boundary** — logistic regression finds *a* separating boundary by maximizing likelihood/minimizing log-loss over *all* points, but nothing in its objective explicitly asks "is this the boundary with the most breathing room?" Two boundaries can achieve the same log-loss while one hugs the data much more tightly than the other. SVM asks for the margin-optimal one directly.
2. **Manual non-linear feature engineering** — before kernels, if your data wasn't linearly separable, you had to hand-craft polynomial/interaction features. The **kernel trick** (Aizerman, Braverman, Rozonoer; adopted into SVM by Boser, Guyon, Vapnik in 1992) let SVM implicitly work in an infinite-dimensional feature space without ever computing the transformation explicitly — non-linear boundaries "for free."

---

## 3. Intuition

**Classification (SVC):** imagine two neighborhoods of houses (two classes) with a street between them. SVM doesn't just draw *any* street that separates them — it finds the **widest possible street**, and that street's edges touch only the closest houses on each side. Those closest houses are the **support vectors** — every other house could be bulldozed and the street wouldn't move.

**বাংলা:** SVM দুই ক্লাসের মাঝে সবচেয়ে চওড়া রাস্তা (margin) খোঁজে, আর সেই রাস্তার কিনারা নির্ধারণ করে কেবল সবচেয়ে কাছের পয়েন্টগুলো (support vectors) — বাকি পয়েন্টগুলো গুরুত্বহীন।

**Regression (SVR):** instead of a street between classes, imagine a **tube of width epsilon (ε)** running through the data. Any point that falls *inside* the tube is "close enough" — zero penalty. Only points sticking out of the tube are penalized, and only those points shape the final curve.

**বাংলা:** SVR ডেটার উপর দিয়ে একটা epsilon-width tube বসায়। Tube-এর ভেতরে থাকা পয়েন্টদের কোনো শাস্তি (loss) নেই — শুধু tube থেকে বেরিয়ে থাকা পয়েন্টগুলোই মডেলকে প্রভাবিত করে।

---

## 4. Math & Formulas

### 4.1 The hyperplane

A hyperplane (line in 2D, plane in 3D, generalizes to `n` dimensions) is:

```
z = w·x + b        (w = weight vector, b = bias/intercept, x = feature vector)
```

Decision rule for classification:

```
z ≥ 0  →  predict class +1
z < 0  →  predict class -1
```

Compare to logistic regression, which squashes the same `z` through the sigmoid `σ(z) = 1 / (1 + e^-z)` to get a probability, with `σ(0) = 0.5` as the threshold. SVM instead reasons about `z` geometrically as a **signed distance**, not a probability.

### 4.2 Distance of a point from the hyperplane

```
distance = (w·x + b) / ||w||          where ||w|| = sqrt(w1² + w2² + ... + wn²)
```

`||w||` is just the magnitude (length) of the weight vector.

### 4.3 Margin

For the two support vectors closest to the boundary (one from each class), the canonical scaling of `w, b` sets their scores to exactly `+1` and `-1`:

```
d1 = distance of nearest +1 point = 1 / ||w||
d2 = distance of nearest -1 point = 1 / ||w||     (by symmetry, d1 = d2)

Margin M = d1 + d2 = 2 / ||w||
```

**Target: maximize M = 2/||w|| ⇔ minimize ||w|| ⇔ minimize (1/2)||w||²** (squaring + the 1/2 factor only makes the calculus cleaner — same optimum, and it turns the problem into a convex quadratic program).

### 4.4 Hard-margin optimization objective

```
minimize   (1/2) ||w||²
subject to  yᵢ (w·xᵢ + b) ≥ 1     for every training point i
```

where `yᵢ ∈ {+1, -1}` is the true label. This assumes the data is **perfectly linearly separable** — no misclassification allowed at all ("Hard Margin").

### 4.5 Soft margin, slack variables, and hinge loss

Real data is rarely perfectly separable. **Soft margin** SVM introduces slack variables `ξᵢ ≥ 0` (one per point) that allow controlled violations of the margin constraint:

```
minimize    (1/2)||w||² + C · Σ ξᵢ
subject to   yᵢ(w·xᵢ + b) ≥ 1 - ξᵢ,   ξᵢ ≥ 0
```

Folding the constraint into the objective directly gives the **hinge loss** formulation:

```
Hinge loss(xᵢ) = max(0, 1 - yᵢ(w·xᵢ + b))

J(w, b) = min [ ||w||²/2  +  C · Σᵢ Hinge loss(xᵢ) ]
```

Reading the hinge loss:
- If `yᵢ(w·xᵢ+b) ≥ 1` (correctly classified **and** outside/on the margin) → loss = 0. The point simply doesn't matter to the objective.
- If `0 ≤ yᵢ(w·xᵢ+b) < 1` (correctly classified but **inside** the margin) → small positive loss.
- If `yᵢ(w·xᵢ+b) < 0` (misclassified) → loss `> 1`, growing linearly with how wrong it is.

### 4.6 The role of `C`

`C` is the trade-off knob between **margin width** and **misclassification tolerance**:

- **`C` large** → hinge-loss term dominates → misclassification is punished heavily → narrower margin, closer to hard margin → risk of **overfitting**.
- **`C` small** → margin term dominates → the model tolerates more misclassified/inside-margin points → wider margin, softer boundary → risk of **underfitting**.

### 4.7 Dual / Lagrangian form and why only support vectors matter

The primal problem above is a constrained quadratic program (QP). Using Lagrange multipliers `αᵢ ≥ 0` (one per training point) and the KKT conditions, it can be rewritten as the **dual problem**:

```
maximize   Σᵢ αᵢ - (1/2) ΣᵢΣⱼ αᵢαⱼ yᵢyⱼ (xᵢ·xⱼ)
subject to  0 ≤ αᵢ ≤ C,   Σᵢ αᵢ yᵢ = 0
```

The KKT conditions force `αᵢ = 0` for every point that is correctly classified **and** strictly outside the margin. Only points *on* or *inside* the margin (or misclassified) get `αᵢ > 0` — these are exactly the **support vectors**. The final decision function only needs those points:

```
f(x) = sign( Σᵢ αᵢ yᵢ (xᵢ·x) + b )        (sum only over support vectors, since αᵢ = 0 elsewhere)
```

This dual form is also *why* the kernel trick works — the data only ever appears as a dot product `xᵢ·xⱼ`, so that dot product can be swapped for a kernel function without ever touching `w` explicitly.

### 4.8 The kernel trick

```
K(xᵢ, xⱼ) = φ(xᵢ) · φ(xⱼ)
```

`φ` is some (possibly very high- or infinite-dimensional) transformation of the input. The kernel trick's magic: `K` can be computed **directly from `xᵢ, xⱼ` in the original space**, without ever computing `φ(xᵢ)` and `φ(xⱼ)` explicitly. Classic illustration: points arranged as concentric circles in 2D (`(x1, x2)`) aren't linearly separable — but mapped to 3D via `(x1, x2, x1²+x2²)`, they become separable by a flat plane. The kernel computes the *effect* of that mapping's dot product without materializing the 3D coordinates.

Common kernels:

| Kernel | Formula | Use case |
|---|---|---|
| Linear | `K(x, x') = x · x'` | Data is already roughly linearly separable |
| Polynomial | `K(x, x') = (γ·x·x' + r)^d` | Curved boundaries, feature interactions up to degree `d` |
| RBF / Gaussian | `K(x, x') = exp(-γ ‖x - x'‖²)` | Default choice for unknown non-linear structure |

### 4.9 SVR: epsilon-insensitive loss and objective

SVR reuses the identical `(1/2)||w||²` margin term, but replaces hinge loss with the **epsilon-insensitive loss**:

```
L_ε(y, ŷ) = max(0, |y - ŷ| - ε)
```

i.e. zero loss as long as the prediction is within `ε` of the true value; loss grows linearly beyond that. With two slack variables (`ξᵢ` for points above the tube, `ξᵢ*` for points below):

```
minimize    (1/2)||w||² + C · Σᵢ (ξᵢ + ξᵢ*)
subject to   yᵢ - (w·xᵢ + b) ≤ ε + ξᵢ
             (w·xᵢ + b) - yᵢ ≤ ε + ξᵢ*
             ξᵢ, ξᵢ* ≥ 0
```

### 4.10 Hand-worked numeric example (hard margin, by inspection)

A tiny, linearly separable 2D dataset — 6 points, 3 per class:

| Point | (x1, x2) | Class y |
|---|---|---|
| A | (3, 3) | +1 |
| B | (4, 3) | +1 |
| C | (4, 4) | +1 |
| D | (2, 2) | -1 |
| E | (1, 2) | -1 |
| F | (1, 1) | -1 |

Assume (by inspection) the separating line `x1 + x2 = 5`, i.e. `w = (1, 1)`, `b = -5`, so `z = w·x + b = x1 + x2 - 5`.

Compute `z` for every point:

```
A (3,3): z = 3+3-5 = 1     →  y·z = (+1)(1)  = 1   → exactly on the +1 margin
B (4,3): z = 4+3-5 = 2     →  y·z = (+1)(2)  = 2   → beyond the margin (safe)
C (4,4): z = 4+4-5 = 3     →  y·z = (+1)(3)  = 3   → beyond the margin (safe)
D (2,2): z = 2+2-5 = -1    →  y·z = (-1)(-1) = 1   → exactly on the -1 margin
E (1,2): z = 1+2-5 = -2    →  y·z = (-1)(-2) = 2   → beyond the margin (safe)
F (1,1): z = 1+1-5 = -3    →  y·z = (-1)(-3) = 3   → beyond the margin (safe)
```

Every point satisfies `yᵢ(w·xᵢ+b) ≥ 1`, so this `w, b` is a valid separator. **A and D are the support vectors** (their score is exactly `1`, i.e. they sit right on the margin boundary); B, C, E, F are correctly classified with room to spare and could be deleted without changing the boundary at all.

Margin width:

```
||w|| = sqrt(1² + 1²) = √2 ≈ 1.414
Margin M = 2 / ||w|| = 2 / 1.414 ≈ 1.414
```

Sanity check geometrically: A(3,3) and D(2,2) are the two closest opposite-class points, and their Euclidean distance is `sqrt((3-2)²+(3-2)²) = sqrt(2) ≈ 1.414` — exactly the margin width, since the boundary sits exactly halfway between them, perpendicular to `w`.

For hinge loss, plugging in `C` and any point with `yᵢ(w·xᵢ+b) ≥ 1` gives `max(0, 1 - (≥1)) = 0` — confirming the objective's penalty term is zero for this perfectly-separated toy example (this is the hard-margin case; hinge loss only becomes positive once a point violates the margin, as shown by the PDF's own worked digression where a point with `y(wx+b) = 0.5` incurs hinge loss `max(0, 1-0.5) = 0.5`, and one with `y(wx+b) = -0.5` incurs `max(0, 1-(-0.5)) = 1.5`).

---

## 5. Algorithm Steps (Pseudocode)

```
INPUT: training data {(x1, y1), ..., (xn, yn)}, kernel choice, hyperparameters C (and gamma/degree/epsilon)

1. Choose a kernel K (linear / poly / rbf) — decides how similarity between points is computed.
2. Solve the constrained optimization problem:
      SVC:  minimize (1/2)||w||^2 + C * sum(hinge_loss(xi))
            subject to correct classification with allowed slack
      SVR:  minimize (1/2)||w||^2 + C * sum(xi_i + xi_i*)
            subject to predictions staying within the epsilon-tube, with allowed slack
   (In practice this is solved in its dual/Lagrangian form via quadratic programming —
    SMO (Sequential Minimal Optimization) is the classic algorithm libsvm/sklearn use.)
3. The solver returns Lagrange multipliers alpha_i for every training point.
   Points with alpha_i = 0 are discarded — they do not affect the model.
   Points with alpha_i > 0 are the SUPPORT VECTORS.
4. Recover b from any support vector using the margin condition.
5. PREDICT a new point x using only the support vectors:
      SVC:  y_hat = sign( sum_{i in SV} alpha_i * y_i * K(x_i, x) + b )
      SVR:  y_hat =        sum_{i in SV} alpha_i * K(x_i, x) + b
```

---

## 6. Key Hyperparameters

| Hyperparameter | Controls | Too high | Too low |
|---|---|---|---|
| `C` | Trade-off between margin width and misclassification penalty | Narrow margin, punishes every misclassification harshly → **overfitting**, sensitive to noise/outliers | Wide margin, tolerates many misclassifications → **underfitting**, boundary too loose |
| `kernel` | Shape of the decision boundary (`linear`, `poly`, `rbf`, `sigmoid`) | N/A (categorical choice) | Wrong kernel choice → boundary shape can't match the true data structure at all |
| `gamma` (for `rbf`, `poly`, `sigmoid`) | How far a single training point's influence reaches | Very localized influence, boundary hugs individual points tightly → **overfitting** | Influence reaches very far, boundary becomes overly smooth/almost linear → **underfitting** |
| `degree` (for `poly`) | Complexity/flexibility of the polynomial boundary | High-degree curves can wiggle excessively → **overfitting**, slow to compute | Degree 1-2 may be too rigid to capture real curvature → **underfitting** |
| `epsilon` (SVR only) | Width of the no-penalty tube around the regression line | Wide tube ignores real signal, too many points "don't matter" → **underfitting**, overly flat/insensitive model | Tube is razor-thin, almost every point is penalized → behaves like ordinary (non-margin) regression, can **overfit** noise |

---

## 7. Assumptions

- Works best when there is a genuine **margin/gap** between classes (or when a well-chosen kernel can create one in a transformed space).
- **Sensitive to feature scale** — features on wildly different scales distort distance-based margin computation (this is why `StandardScaler` before SVM is close to mandatory, not optional).
- Assumes the chosen kernel's implicit similarity notion (linear dot product, polynomial interaction, Gaussian similarity) is a reasonable match for the true relationship in the data.
- For SVR: assumes deviations of magnitude `≤ ε` are "noise" that shouldn't be modeled, and only larger deviations carry real signal.

---

## 8. Advantages

- Effective in **high-dimensional spaces**, even when the number of features exceeds the number of samples.
- Robust to overfitting, **especially** when there is a clear margin of separation between classes.
- **Kernel trick** captures non-linear boundaries without manual feature engineering.
- Works well even with relatively **few samples**, as long as there's a clean margin.
- Only a subset of points (support vectors) determine the model — memory-efficient at prediction time relative to the number of decision-relevant points.

---

## 9. Disadvantages

- **Slow to train on large datasets** — classic SVM training scales roughly quadratic-to-cubic in the number of samples; it doesn't comfortably scale past tens of thousands of rows.
- **Sensitive to kernel/hyperparameter choice** — needs deliberate tuning (`C`, `gamma`, `degree`, `epsilon`); a poor choice can silently underfit or overfit.
- **No direct probability output** — a raw decision function score isn't a calibrated probability; getting probabilities requires extra calibration (e.g. Platt scaling via `probability=True`, which itself adds training cost).
- **Less interpretable** than linear models — especially with non-linear kernels, there's no simple per-feature coefficient story.
- **Sensitive to feature scaling** — an unscaled feature with a large numeric range can dominate the margin computation.

---

## 10. Classification (SVC) vs Regression (SVR)

| Aspect | SVC (Classification) | SVR (Regression) |
|---|---|---|
| Loss function | Hinge loss: `max(0, 1 - yᵢ(w·xᵢ+b))` | Epsilon-insensitive loss: `max(0, |y-ŷ| - ε)` |
| What's controlled/maximized | **Margin width** between classes | **Tube width** (`ε`) with a flat-as-possible function inside it |
| Output | Discrete class label (`sign` of decision function); optionally a decision score / calibrated probability | Continuous numeric value |
| Evaluation metrics | Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC | MSE, RMSE, MAE, R² |
| Notebook section | `SVM_Complete.ipynb` → Part A (Titanic SVC) & Part B/C (kernel & C/gamma demos) | `SVM_Complete.ipynb` → Part D (SVR toy tube + `load_diabetes`) |

---

## 11. How It Compares to Related Algorithms

**vs Logistic Regression**
Both draw a linear boundary `w·x+b=0` in their base form (SVM bends it via kernels). Logistic regression minimizes **log-loss**, which keeps getting (slightly) smaller the further a correctly-classified point is from the boundary — every point always has *some* pull on the fit, and it naturally yields calibrated probabilities. SVM's **hinge loss** flatlines to zero the moment a point is safely outside the margin — points far from the boundary are completely ignored once correctly classified, so the fit is driven purely by the hardest, closest points. SVM is margin-maximizing; logistic regression is likelihood-maximizing.

**vs Decision Tree / Random Forest**
SVM produces a smooth, globally-optimized boundary (a hyperplane, possibly bent by a kernel). Trees/forests build **axis-aligned, piecewise** partitions (splitting one feature at a time). SVM tends to do well on small-to-medium, cleanly-scaled, clear-margin data. Trees/forests tend to win on messy real-world tabular data with mixed feature types, missing values, and non-smooth interactions — and they don't need feature scaling at all.

**vs KNN**
KNN makes each prediction by a **purely local** majority vote among the nearest neighbors at prediction time — there is no global training-time optimization, just memorized data. SVM instead solves a **global optimization problem once**, upfront, to find the single best-margin boundary, then discards everything except the support vectors. SVM front-loads the cost into training; KNN front-loads it into prediction.

---

## 12. Evaluation Metrics

### Classification (SVC)

```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)                      "Of predicted positives, how many were right?"
Recall    = TP / (TP + FN)                       "Of actual positives, how many did we find?"
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

- **Confusion Matrix**: a table of TP/FP/TN/FN counts — the raw material behind every metric above.
- **ROC-AUC**: area under the True-Positive-Rate vs False-Positive-Rate curve as the decision threshold sweeps; `SVC` needs `decision_function` (or `probability=True`) to compute this, since it has no native probability output.

### Regression (SVR)

```
MSE  = (1/n) * Σ (yᵢ - ŷᵢ)²
RMSE = sqrt(MSE)
MAE  = (1/n) * Σ |yᵢ - ŷᵢ|
R²   = 1 - [ Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)² ]        (ȳ = mean of true y)
```

---

## 13. When to Use / When NOT to Use

**Use SVM when:**
- The dataset is small-to-medium sized (roughly up to tens of thousands of rows).
- You expect (or can engineer via a kernel) a reasonably clear margin between classes, or a smooth underlying function for regression.
- The feature count is high relative to sample count (e.g. text/genomic data).
- You need a robust, well-regularized model and don't strictly need calibrated probabilities.

**Avoid SVM when:**
- The dataset is very large (hundreds of thousands+ rows) — training time/memory become impractical; prefer linear models, tree ensembles, or `LinearSVC`/`SGDClassifier` for the linear case.
- You need built-in, well-calibrated probability outputs out of the box.
- You need a highly interpretable model (coefficients, feature importances) — prefer linear/logistic regression or trees.
- Your data has heavily mixed types / lots of missing values and you don't want to build a careful preprocessing pipeline — tree ensembles handle this more gracefully.

---

## 14. Common Pitfalls & Practical Tips

- **Always scale features before SVM** (`StandardScaler` typically) — this is not optional, unlike for tree-based models.
- **Start with the RBF kernel + grid search over `C` and `gamma`** as a strong default before trying anything fancier.
- **Don't blindly throw SVM at huge datasets** — check training time on a subsample first; consider `LinearSVC`/`LinearSVR` (which scale much better) if the relationship looks roughly linear.
- **Use `class_weight='balanced'`** for imbalanced classification so the minority class's margin violations aren't drowned out by the majority class.
- **For SVR, consider scaling the target too** — `epsilon` is defined in the target's raw units, so an unscaled target with a huge numeric range can make the default `epsilon=0.1` meaningless (either always inside the tube, or always outside it).
- **Watch out for `gamma`/`C` interacting** — don't tune them independently; a grid/2D sweep (as done in this folder's notebook, Part C) shows their combined effect much better than tuning one at a time.

---

## 15. Notebook Map

`SVM_Complete.ipynb` (the merged, extended notebook — original backup lives untouched in `archive/Support_vector_Classifier_with_Scikit_Learn.ipynb`):

| Section | What It Demonstrates |
|---|---|
| Part A.0 – A.1 | Imports; loading & exploring the raw Titanic dataset |
| Part A.2 | Feature engineering: `Family_Size`, `Deck` |
| Part A.3 | Stratified train/test split |
| Part A.4 | Outlier handling: Z-score filter on `Age`, IQR clipping on `Fare` |
| Part A.5 | `ColumnTransformer` + `Pipeline` preprocessing (numeric scale, categorical encode) |
| Part A.6 | Target label encoding (`yes`/`no` → `1`/`0`) |
| Part A.7 | `GridSearchCV` over linear/rbf/poly kernels and their hyperparameters |
| Part A.8 | Full evaluation: accuracy, precision, recall, **F1**, confusion matrix, **ROC-AUC** (new vs the original notebook) |
| Part A.9 | Illustrative 2D decision-boundary plot (`Age` vs `Fare`) |
| Part B | Kernel trick demo: linear vs polynomial vs RBF on the same non-linear `make_moons` data |
| Part C | Effect of `C` and `gamma`: grid of decision boundaries + accuracy table, under-fit vs over-fit |
| Part D.0 | SVR theory recap (epsilon-insensitive loss, objective) |
| Part D.1 | 1D toy example visualizing the **epsilon tube** and support vectors, linear vs RBF |
| Part D.2 | Full SVR workflow on `load_diabetes`: scaling, linear vs RBF, MSE/RMSE/MAE/R² |
| Part D.3 | Small `C`/`epsilon` sweep for SVR, scored by R² |

---

## 16. One-Paragraph Exam-Ready Summary

SVM একটা margin-maximizing supervised algorithm যেটা classification-এ widest street (SVC) আর regression-এ epsilon-tube (SVR) হিসেবে কাজ করে; hyperplane হলো `w·x+b=0`, margin `= 2/||w||`, আর সেটা maximize করতে গিয়ে আমরা minimize করি `(1/2)||w||² + C·Σ hinge_loss` (SVC) বা `(1/2)||w||² + C·Σ(ξᵢ+ξᵢ*)` with epsilon-insensitive loss (SVR) — only the **support vectors** (points on/inside the margin, or on/outside the tube) actually matter, everything else has zero contribution via the dual `αᵢ=0`. `C` trades off margin width vs error tolerance; the **kernel trick** (`K(xᵢ,xⱼ)=φ(xᵢ)·φ(xⱼ)`, most commonly RBF `exp(-γ‖x-x'‖²)`) lets a linear-looking optimization bend around non-linear data without explicit feature engineering. SVM is scale-sensitive (always `StandardScaler` first), doesn't scale well to huge datasets, gives no native probabilities, but is strong on small/medium, high-dimensional, clear-margin problems — contrast with logistic regression (probability-maximizing log-loss, every point matters) and trees/forests (axis-aligned splits, no scaling needed, better on messy tabular data).
