# Logistic Regression — Complete Learning Notes

Logistic Regression predicts a **probability** (0 to 1) that something belongs to a class — it draws a boundary through your data and squashes the result into a valid probability with the sigmoid function.

---

## 1. What Is It & Where Does It Sit

- **Type**: Supervised Learning.
- **Task**: **Classification only** — binary (2 classes, e.g. survived / did not survive) and multiclass (3+ classes, e.g. setosa / versicolor / virginica).
- **Family**: Linear model (same `w·x + b` DNA as Linear Regression), but with a non-linear "link function" (sigmoid/softmax) on top and a different cost function (log-loss instead of squared error).
- **Not**: a regression algorithm for continuous targets, despite the name "regression" in it (historical naming — see Section 11).

**বাংলা ইনটুইশন:** নামে "Regression" থাকলেও এটা আসলে **Classification** অ্যালগরিদম — এটা কোনো continuous সংখ্যা প্রেডিক্ট করে না, বরং "এটা কোন ক্লাসে পড়বে" তার **সম্ভাবনা (probability)** বলে দেয়।

---

## 2. Where It Comes From & Why It Was Invented

Linear Regression fits `z = w·x + b` and predicts `z` directly. Early statisticians tried to reuse this for classification by fitting `y ∈ {0, 1}` directly with a straight line. That fails in three concrete ways:

1. **Unbounded output** — a straight line can predict `z = -3.7` or `z = 8.2`, but a class label / probability must live in `[0, 1]`. Nothing stops linear regression from predicting nonsense values.
2. **Meaningless "probability"** — even where the line's output happens to land in `[0, 1]`, there is no mathematical reason to interpret it as a probability; it is just wherever the least-squares line happens to be.
3. **Poor fit to 0/1 targets** — squared-error loss (used by Linear Regression) is the wrong penalty for a yes/no outcome; it doesn't punish confidently-wrong predictions the way a classification problem needs.

Logistic Regression was invented (statistics, early-to-mid 20th century; the logistic function itself dates to 1830s population-growth models) to fix exactly this: keep the familiar linear combination `z = w·x + b`, but

- pass `z` through the **sigmoid function** to force the output into `[0, 1]` — now it's a valid probability, and
- replace squared-error with **log-loss (binary cross-entropy)**, a cost function specifically shaped for probabilistic 0/1 targets.

In short: **Logistic Regression = Linear Regression's linear combination + a squashing function + a probability-shaped cost function.**

---

## 3. Intuition

Think of predicting "will a student pass?" from hours studied. Zero hours → very low chance of passing. Twelve hours → very high chance. Somewhere in the middle, the chance rises steeply — but it can never go below 0% or above 100%. Plotted, this looks like a flattened "S" — the **sigmoid curve**.

**বাংলা ইনটুইশন:** ধরো, স্টাডি আওয়ারের উপর ভিত্তি করে পাস/ফেল-এর সম্ভাবনা বের করতে চাইছ। খুব কম পড়লে পাসের সম্ভাবনা কম, বেশি পড়লে সম্ভাবনা বেশি — কিন্তু সম্ভাবনা কখনো ০%-এর নিচে বা ১০০%-এর উপরে যাবে না। এই "S" আকৃতির কার্ভটাই সিগময়েড (sigmoid) — এটাই Logistic Regression-এর মূল হাতিয়ার।

---

## 4. Math & Formula(s)

### 4.1 Linear combination
$$z = w \cdot x + b = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b$$

### 4.2 Sigmoid function (binary case)
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
Maps any real number `z` into the open interval `(0, 1)`. This is exactly `sigmoid()` in Part 1 of the notebook and the S-curve plotted there.

### 4.3 Log-odds / logit (the inverse view)
$$\ln\left(\frac{p}{1-p}\right) = z$$
This is the other way to say the same thing: logistic regression models the **log of the odds** of the positive class as a linear function of the features. This is *why* the decision boundary is linear in log-odds space (Section 10).

### 4.4 Softmax (multiclass generalization)
For `K` classes with per-class scores `z_1, …, z_K`:
$$P(y=k \mid x) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$
Binary sigmoid is the special case `K = 2`.

### 4.5 Cost function — Binary Cross-Entropy (Log Loss)
For `n` training examples, with `ŷ_i = σ(z_i)` the predicted probability and `y_i ∈ {0,1}` the true label:
$$J(w,b) = -\frac{1}{n} \sum_{i=1}^{n} \Big[ y_i \ln(\hat{y}_i) + (1-y_i)\ln(1-\hat{y}_i) \Big]$$
Intuition: if `y=1` and the model predicted `ŷ ≈ 0` (confidently wrong), `-ln(ŷ)` blows up toward infinity — the cost punishes confident wrong answers far harder than timid wrong answers.

### 4.6 Gradient descent update rule
$$w_j \leftarrow w_j - \alpha \cdot \frac{\partial J}{\partial w_j}, \qquad b \leftarrow b - \alpha \cdot \frac{\partial J}{\partial b}$$
where the gradients have a beautifully simple closed form (identical in structure to linear regression's, only `ŷ` now comes from the sigmoid):
$$\frac{\partial J}{\partial w_j} = \frac{1}{n}\sum_{i=1}^n (\hat{y}_i - y_i)\, x_{ij}, \qquad \frac{\partial J}{\partial b} = \frac{1}{n}\sum_{i=1}^n (\hat{y}_i - y_i)$$
`α` (alpha) is the learning rate. This exact loop is implemented by hand in Part 1's `calculate_gradient()` and `gradient_descent()`.

### 4.7 Decision threshold
$$\hat{class} = \begin{cases} 1 & \text{if } \hat{y} \ge 0.5 \\ 0 & \text{if } \hat{y} < 0.5 \end{cases}$$
`0.5` is the *default* threshold, not a law of nature — Section 15 discusses moving it.

### 4.8 Worked-by-hand numeric example

**Setup.** One feature, `x` = hours studied; target `y` = 1 (pass) or 0 (fail). Toy dataset:

| x (hours) | y (pass?) |
|---|---|
| 1 | 0 |
| 2 | 0 |
| 3 | 1 |
| 4 | 1 |

Assume the model has already learned (for this illustration) `w = 1.2`, `b = -3`. Let's hand-compute everything for the third data point, `x = 3, y = 1`.

**Step 1 — linear combination:**
$$z = w \cdot x + b = 1.2 \times 3 + (-3) = 3.6 - 3 = 0.6$$

**Step 2 — sigmoid:**
$$\sigma(0.6) = \frac{1}{1+e^{-0.6}} = \frac{1}{1 + 0.548812} = \frac{1}{1.548812} \approx 0.6457$$

**Step 3 — predicted probability:** `ŷ ≈ 0.6457` → "64.57% chance of passing."

**Step 4 — predicted class:** since `0.6457 ≥ 0.5`, predicted class = **1 (pass)**. This matches the true label `y = 1` — a correct prediction.

**Step 5 — log-loss contribution for this one point:**
$$-\big[y\ln(\hat y) + (1-y)\ln(1-\hat y)\big] = -\big[1 \times \ln(0.6457) + 0\big] = -\ln(0.6457) \approx 0.4372$$

So this single correctly-classified-but-not-fully-confident point still contributes `≈0.437` to the total cost — it would contribute exactly `0` only if `ŷ` had been `1.0`. Repeat Steps 1–5 for every row and average to get the full `J(w,b)`; repeat the whole thing with updated `w, b` every gradient-descent iteration. This is the identical arithmetic Part 1's `compute_cost()` performs across its 4-row toy dataset.

---

## 5. Algorithm Steps (Pseudocode)

```
1. Initialize weights W = 0 (or small random values) and bias b = 0
2. Repeat until convergence (or for max_iter steps):
     a. For each example i:
          z_i      = W·x_i + b
          y_hat_i  = sigmoid(z_i)               # or softmax for multiclass
     b. Compute cost J using Binary Cross-Entropy (log-loss) over all examples
     c. Compute gradients dJ/dW and dJ/db
     d. Update:  W = W - alpha * dJ/dW
                 b = b - alpha * dJ/db
3. Output final W, b as the learned model
4. Predict: y_hat = sigmoid(W·x_new + b); class = 1 if y_hat >= threshold else 0
```
This is exactly Part 1's `sigmoid()` → `make_prediction()` → `compute_cost()` → `calculate_gradient()` → `gradient_descent()` chain, in order.

---

## 6. Key Hyperparameters

| Hyperparameter | What it controls | Effect if too high | Effect if too low |
|---|---|---|---|
| `C` | **Inverse** of regularization strength (small `C` = strong regularization). Controls the fit-vs-simplicity trade-off. | Weak regularization → model fits training noise → **overfitting**, large coefficients. | Strong regularization → model too constrained → **underfitting**, coefficients pushed toward 0. |
| `penalty` (deprecated in newer sklearn; use `l1_ratio`) | Type of regularization: `l2` (shrink smoothly), `l1` (can zero out coefficients — feature selection), `elasticnet` (mix), `None`. | N/A (categorical) | N/A (categorical) — wrong choice just means suboptimal sparsity/shrinkage behavior. |
| `solver` | Which optimization algorithm finds `W`/`b` (`lbfgs`, `liblinear`, `newton-cg`, `newton-cholesky`, `sag`, `saga`). | N/A — mostly a speed/compatibility choice, not an accuracy lever. | Wrong solver for the job (e.g. no `l1` support) → errors or forced fallback. |
| `max_iter` | Cap on how many iterations the solver is allowed. | Wastes compute once already converged (harmless beyond a point). | Solver stops before convergence → underfit / `ConvergenceWarning`. |
| `class_weight` | Re-weights the cost function per class (`None`, `'balanced'`, or a custom dict) — crucial for imbalanced data. | Over-correcting for the minority class → recall up, precision down (more false alarms). | Ignoring imbalance (`None`) → majority-class bias, poor recall on the minority class. |
| `multi_class` | *(Removed in scikit-learn ≥ 1.9 — see Section 12 of the notebook.)* Historically chose `'ovr'` vs `'multinomial'` (softmax) for 3+ classes. Now softmax-style fitting is the default; explicit OvR needs `OneVsRestClassifier`. | — | — |

**Priority order to tune, in practice:** `C` first → `class_weight` if classes are imbalanced → `solver`/`max_iter` only if you hit an error or a `ConvergenceWarning`.

---

## 7. Assumptions

- **Linearity in log-odds**: the log-odds of the outcome is assumed to be a *linear* function of the features (`ln(p/(1-p)) = w·x + b`), not the raw probability itself, which is why the sigmoid curve is non-linear even though the boundary is linear.
- **Independent observations**: each row is assumed independent of the others (no repeated-measures / time-series autocorrelation baked in).
- **Little/no multicollinearity**: highly correlated features make coefficients unstable and hard to interpret (check with VIF — Variance Inflation Factor).
- **Sufficient sample size per class**: logistic regression's coefficient estimates get unreliable with very few examples of a class — a common rule of thumb is at least ~10 events per predictor per class.

---

## 8. Advantages

- Outputs **calibrated-ish probabilities** (`predict_proba`), not just hard labels — you can rank, threshold, or feed the probability into a downstream decision.
- **Fast to train** even on large datasets; no expensive search like tree ensembles.
- **Interpretable**: each coefficient has a direct odds-ratio interpretation (`e^{w_j}` = multiplicative change in odds per unit increase in `x_j`).
- **Strong, cheap baseline** — before reaching for a random forest or a neural net, fit logistic regression; if a fancier model can't clearly beat it, the added complexity isn't earning its keep.
- **Naturally extends to multiclass** via softmax, with no separate algorithm needed (Section 4 of the notebook's Part 4).

---

## 9. Disadvantages

- **Linear decision boundary only** (in log-odds space) — struggles with genuinely non-linear class boundaries unless you manually engineer polynomial/interaction features.
- **Sensitive to outliers and multicollinearity** — extreme feature values or redundant correlated features can distort the learned coefficients.
- Needs **reasonably balanced classes** or careful `class_weight` tuning — severe imbalance biases the model toward the majority class.
- Like any linear model, it **can't automatically discover feature interactions** the way tree-based models can.

---

## 10. Why NOT Used for Regression

Logistic Regression's entire architecture is built around producing a **bounded probability**:

- The sigmoid forces every output into `[0, 1]` — mathematically incapable of representing a continuous, unbounded target like "house price" or "temperature."
- The optimizer minimizes **log-loss**, a cost function shaped specifically around 0/1 (or one-hot multiclass) labels — it has no meaning for a continuous target.

For predicting a continuous number, the correct tool is **Linear Regression** (see the sibling folder: `Supervised/Linear Regression - Simple & Multiple (Regression)`), which keeps the raw, unbounded `z = w·x + b` as the final prediction and minimizes squared error instead.

**সহজ কথায়:** Logistic Regression-এর আউটপুট সবসময় ০ থেকে ১-এর মধ্যে বাঁধা (probability), তাই এটা continuous সংখ্যা প্রেডিক্ট করতে পারে না। Continuous সংখ্যার জন্য পাশের ফোল্ডারে থাকা **Linear Regression** ব্যবহার করো।

---

## 11. How It Compares to Related Algorithms

| vs. | Key difference |
|---|---|
| **Linear Regression** | Same linear-model DNA (`w·x + b`) and literally sibling folders — but Linear Regression predicts a continuous value directly with squared-error loss; Logistic Regression squashes that same linear combination through sigmoid/softmax and optimizes log-loss to predict class probabilities. |
| **Decision Tree** | Logistic Regression draws one *global*, linear (in log-odds) boundary across the whole feature space. A Decision Tree carves the space into axis-aligned rectangular regions and can capture non-linear, interacting patterns natively — at the cost of being more prone to overfitting without pruning. |
| **KNN** | KNN is a *local*, non-parametric method with no fitted boundary at all — it just looks at nearby points at prediction time. Logistic Regression is *global* and parametric — it learns one fixed `W`/`b` for the whole space, which is far cheaper to predict with, but rigid. |
| **SVM (Support Vector Machine)** | Both fit a linear boundary (with a kernel, SVM can go non-linear too). The difference is the objective: Logistic Regression minimizes log-loss and yields a probability for every point; SVM (in its classic form) minimizes hinge loss and only cares about maximizing the margin around the boundary, generally without a native probability output. |

---

## 12. Evaluation Metrics

Let `TP`, `TN`, `FP`, `FN` be true/false positives/negatives from the confusion matrix:

|  | Predicted: No | Predicted: Yes |
|---|---|---|
| **Actual: No**  | TN | FP |
| **Actual: Yes** | FN | TP |

- **Accuracy** = `(TP + TN) / (TP + TN + FP + FN)` — overall fraction correct.
- **Precision** = `TP / (TP + FP)` — of everything predicted positive, how much was actually positive.
- **Recall (Sensitivity)** = `TP / (TP + FN)` — of everything actually positive, how much did we catch.
- **F1-score** = `2 · (Precision · Recall) / (Precision + Recall)` — harmonic mean; one number that balances both.
- **ROC curve** — plots True Positive Rate (`Recall`) vs. False Positive Rate (`FP/(FP+TN)`) as the decision threshold sweeps across all values.
- **AUC (Area Under the ROC Curve)** — a single number in `[0, 1]` (0.5 = random guessing, 1.0 = perfect separation) summarizing ranking quality *independent of any one threshold*.

**When accuracy is misleading:** with imbalanced classes (e.g. 95% negative / 5% positive), a model that always predicts "negative" scores 95% accuracy while being useless. In that situation, **prefer precision, recall, F1, and AUC** over raw accuracy — exactly the reasoning behind the notebook's Titanic evaluation (Part 4, Section 1) and its use of `class_weight='balanced'`.

---

## 13. When to Use / When NOT to Use

**Use it when:**
- The target is binary or multiclass (categorical), not continuous.
- You need calibrated probabilities, not just hard labels.
- You want a fast, interpretable baseline before trying anything fancier.
- The relationship between features and log-odds is roughly linear (or can be made so with feature engineering).

**Avoid / be cautious when:**
- The true decision boundary is highly non-linear and you're not willing to engineer polynomial/interaction features (consider trees, SVM with a kernel, or neural nets instead).
- Classes are severely imbalanced and you haven't addressed it via `class_weight`, resampling, or threshold tuning.
- Features are highly collinear and interpretability of individual coefficients matters (address multicollinearity first).
- The target is actually continuous — use Linear Regression (Section 10).

---

## 14. Common Pitfalls & Practical Tips

- **Check class balance first** (`value_counts()` / `class_weight` decision) — imbalance quietly wrecks recall while accuracy looks fine.
- **Don't trust accuracy alone** — always look at the confusion matrix, F1, and AUC together (Section 12).
- **Scale your features** (`StandardScaler`/`MinMaxScaler`) — gradient-based solvers converge faster and more reliably on similarly-scaled features; unscaled features can also distort regularization (`C` penalizes all coefficients equally regardless of the feature's natural scale).
- **Check for multicollinearity** with **VIF (Variance Inflation Factor)** — a VIF above ~5–10 on a feature is a red flag that its coefficient is unstable.
- **The 0.5 threshold isn't sacred** — if false positives and false negatives have very different real-world costs, calibrate/move the threshold (using the ROC curve or a precision-recall trade-off) instead of always defaulting to 0.5.
- **Watch for `ConvergenceWarning`** — it means `max_iter` was hit before the solver settled; raise it rather than trusting an unconverged fit.
- **Prefer `l1_ratio` over `penalty`** in recent scikit-learn — `penalty` is deprecated (see Part 3, Section 5 of the notebook).

---

## 15. Notebook Map

`Logistic_Regression_Complete.ipynb` — every section, what it demonstrates:

| Part | Section | Demonstrates |
|---|---|---|
| Part 1 | Data Preparation | Toy 4-row dataset: Age & Ticket Price → survived/not, used to hand-build the algorithm. |
| Part 1 | The Sigmoid Function | `sigmoid(z)` implemented by hand and **plotted explicitly** as the S-curve. |
| Part 1 | Making Predictions | `z = W·X + b` → `sigmoid(z)` → threshold at 0.5, via `make_prediction()`. |
| Part 1 | Cost Function | Binary Cross-Entropy / Log Loss implemented by hand in `compute_cost()`. |
| Part 1 | Gradient Computation | Partial derivatives `dJ/dW`, `dJ/db` in `calculate_gradient()`. |
| Part 1 | Gradient Descent | Full training loop, 100,000 iterations, cost decreasing, final weights recover the true labels. |
| Part 2 | Data Loading & EDA | Real Titanic dataset (`titanic_data_updated.csv`) — sampling, `.info()`, missing-value inspection. |
| Part 2 | Feature Engineering | `Family_Size = SibSp + Parch + 1`; `Deck` extracted from `Cabin`'s first letter. |
| Part 2 | Data Splitting | `train_test_split(..., stratify=y)` — 80/20 split preserving the survival ratio. |
| Part 2 | Outlier Handling | Z-score filtering (`|z| ≤ 3`) on `Age`; IQR clipping on `Fare` — fit on `X_train` only. |
| Part 2 | Preprocessing Pipelines | `ColumnTransformer` combining imputers, `StandardScaler`/`MinMaxScaler`, `OneHotEncoder`, and an ordered `OrdinalEncoder` for `Pclass`. |
| Part 2 | Label Encoding | `yes`/`no` target → `1`/`0` via `LabelEncoder`. |
| Part 2 | Model Training | `LogisticRegression(class_weight='balanced', max_iter=1000)` wrapped in one `Pipeline`. |
| Part 2 | Evaluation | Accuracy (0.765), precision (0.675), recall (0.754) on the held-out test set. |
| Part 3 | Real-world uses | Table of industries/use-cases where logistic regression is the standard first model. |
| Part 3 | Parameters vs. hyperparameters | The key distinction, grounded in this notebook's own variables. |
| Part 3 | `C` (regularization strength) | Live demo: `||w||` growing as `C` increases from 0.01 → 100. |
| Part 3 | `penalty` / `l1_ratio` | l1 vs l2 vs elasticnet; coefficients zeroed out by `l1`; captured `FutureWarning` for the deprecated `penalty`. |
| Part 3 | `solver` | Compatibility table + live accuracy comparison across 6 solvers. |
| Part 3 | `class_weight` | `None` vs `'balanced'` vs custom dict — live precision/recall trade-off table. |
| Part 3 | `max_iter` / `tol` | Forced `ConvergenceWarning` at `max_iter=1`, contrasted with a healthy budget. |
| Part 3 | Complete hyperparameter list | Every remaining `LogisticRegression` parameter, pulled live via `inspect.signature`. |
| **Part 4** | **Full evaluation suite** | **F1-score, confusion matrix (+ heatmap), ROC curve, and AUC (~0.84)** on the Part 2 Titanic model. |
| **Part 4** | **Decision boundary** | 2D decision boundary plotted on raw `Age` & `Fare`, with the 0.5-probability contour shown as the boundary line. |
| **Part 4** | **`C` trade-off, isolated** | Train **vs.** test accuracy plotted together across 15 values of `C` (`1e-4` → `1e4`) — the direct under-fitting/over-fitting picture. |
| **Part 4** | **Multiclass logistic regression** | Iris dataset (3 classes): softmax/multinomial `LogisticRegression` vs. explicit `OneVsRestClassifier`, plus a 3-region decision-boundary plot. |

---

## 16. One-Paragraph Exam-Ready Summary

Logistic Regression is a **classification** algorithm (never regression on a continuous target) that takes the familiar linear combination `z = w·x + b`, squashes it through the **sigmoid** function `σ(z) = 1/(1+e^{-z})` (or **softmax** for 3+ classes) to get a probability in `[0, 1]`, and is trained by minimizing **log-loss / binary cross-entropy** via **gradient descent** — updating `w` and `b` in the direction `(ŷ - y)·x` until the cost stops shrinking. A `0.5` threshold (adjustable) turns that probability into a hard class label. The most important hyperparameter is `C` (inverse regularization strength: small `C` → simpler/underfit, large `C` → closer training fit, risk of overfit), followed by `class_weight` for imbalanced classes. It assumes a linear relationship between features and **log-odds**, is fast, interpretable via odds ratios, and makes an excellent baseline — but it cannot bend into non-linear boundaries on its own and is not the tool for continuous targets (that's Linear Regression's job, its regression sibling in DNA but not in task). Evaluate it with **accuracy, precision, recall, F1, the confusion matrix, and ROC-AUC** together — never accuracy alone, especially under class imbalance. **সংক্ষেপে: Logistic Regression একটা probability বের করে sigmoid দিয়ে, log-loss মিনিমাইজ করে গ্র্যাডিয়েন্ট ডিসেন্ট দিয়ে ট্রেইন হয়, এবং এটা শুধু classification-এর জন্য — continuous ভ্যালুর জন্য Linear Regression ব্যবহার করতে হয়।**
