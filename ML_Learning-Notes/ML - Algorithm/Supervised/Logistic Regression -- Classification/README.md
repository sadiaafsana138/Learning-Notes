# Logistic Regression — Learning Notes

A complete, from-scratch walkthrough of **Logistic Regression**, the foundational
algorithm of binary classification. This folder takes you from the raw math
(sigmoid → log loss → gradient descent) all the way to a full, tested
`scikit-learn` pipeline on the Titanic dataset — then closes with a hyperparameter
reference thorough enough to answer "is that really all of them?"

---

## 📓 Main Notebook

| File | What's inside |
|------|---------------|
| **`Logistic_Regression_Complete.ipynb`** | The full lesson, fully executed with all outputs baked in. |

> This single notebook is the merge of two earlier notebooks (*Logistic Regression
> from Scratch* and *Logistic Regression with Scikit-Learn*), plus a new
> hyperparameter-tuning part written directly into the merge. Everything is now in
> one place.

### Notebook contents

**Part 1 — Logistic Regression from Scratch (NumPy)**
- Toy dataset: `Age` and `Ticket Price` → survived / did not survive.
- The **sigmoid function** — squashes any real number into a `[0, 1]` probability.
- Making predictions: `z = W·X + b`, then `sigmoid(z)`, then threshold at `0.5`.
- **Cost function** — Binary Cross-Entropy (Log Loss), built by hand.
- **Gradient computation** — partial derivatives of the cost w.r.t. `W` and `b`.
- **Gradient Descent** — the training loop, run for 100,000 iterations.
- Final weights correctly reproduce the toy dataset's true labels.

**Part 2 — Logistic Regression with Scikit-Learn (End-to-End Pipeline)**
- Real dataset: the Titanic (`titanic_data_updated.csv`).
- **Feature engineering**: `Family_Size` (`SibSp + Parch + 1`), `Deck` (first letter of `Cabin`).
- **Train/test split** with `stratify=y` to preserve the survival ratio in both sets.
- **Outlier handling**: Z-score filtering on `Age`, IQR clipping on `Fare` — fit on `X_train` only.
- **Preprocessing pipelines** per column group, combined with `ColumnTransformer`:
  imputation + scaling for numerics, imputation + one-hot/ordinal encoding for categoricals.
  `Pclass` uses an explicit `OrdinalEncoder(categories=[['third','second','first']])` since it's ordered.
  `LabelEncoder` converts the target (`yes`/`no`) to `1`/`0`.
- **Model training**: preprocessor + `LogisticRegression(class_weight='balanced', max_iter=1000)`
  wrapped in one `Pipeline`, fit on the training data.
- **Evaluation**: accuracy (0.765), precision (0.675), recall (0.754) on the held-out test set.

**Part 3 — Real-World Uses & Hyperparameter Tuning**
- Where logistic regression is used in practice, and why it's still worth knowing.
- **Parameters vs. hyperparameters** — the key distinction, using this notebook's own variables (`W`, `b` vs. `alpha`, `max_iter`, `C`).
- **`C` (regularization strength)** — a live demo showing the weight vector grow as `C` increases.
- **`l1_ratio` / the deprecated `penalty`** — l1 vs. l2 vs. elasticnet, a live demo of `l1` zeroing out coefficients, and a captured `FutureWarning` showing scikit-learn's current migration path away from `penalty`.
- **`solver`** — a compatibility table (`lbfgs`, `liblinear`, `newton-cg`, `newton-cholesky`, `sag`, `saga`) plus a live accuracy comparison across all six.
- **`class_weight`** — `None` vs. `'balanced'` vs. a custom dict, with a live precision/recall trade-off table on Titanic's imbalanced classes (~62% / 38%).
- **`max_iter` / `tol`** — a live `ConvergenceWarning`, forced on purpose with `max_iter=1`, contrasted against a healthy budget.
- **A quick-reference table** of which hyperparameter matters most, and why.
- **A complete reference table** of every remaining hyperparameter (`dual`, `fit_intercept`, `intercept_scaling`, `random_state`, `verbose`, `warm_start`, `n_jobs`) — pulled directly from the installed scikit-learn's own signature via `inspect.signature`, so nothing is left out and it stays accurate as the library changes.

---

## 🧠 The Core Idea (in one minute)

Logistic regression draws a line (or hyperplane) through your data, then squashes
the result into a probability.

| Term | Plain English |
|------|---------------|
| `z = W·X + b` | same linear combination as linear regression |
| **sigmoid** | squashes `z` into a probability between `0` and `1` |
| **threshold (0.5)** | turns the probability into a `0`/`1` class label |
| **weight (W)** | how much each feature pushes the probability up or down |
| **bias (b)** | the baseline probability before any feature is considered |
| **cost (Log Loss)** | how wrong the predicted probabilities are — punishes confident *wrong* answers hardest |
| **gradient descent** | automatically searching for the `W`/`b` that minimize that cost |
| **hyperparameter** | a setting *you* choose before training (like `C` or `solver`) — as opposed to `W`/`b`, which the model learns on its own |
| **scikit-learn** | does all of the above for you in ~3 lines, plus a whole pipeline around it |

The from-scratch part teaches you *what happens under the hood*; the scikit-learn
part is *what you actually use* in practice; Part 3 teaches you *how to tune it*.

---

## 🚀 How to Run

1. Make sure the required libraries are installed:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
2. Open the notebook in Jupyter / VS Code:
   ```bash
   jupyter notebook Logistic_Regression_Complete.ipynb
   ```
3. Run the cells top to bottom (**Kernel → Restart & Run All**). The notebook is
   self-contained — `titanic_data_updated.csv` must stay in this same folder, since
   Part 2 reads it with a relative path.

---

## ✅ Key Takeaways

1. **The model** predicts a probability via `sigmoid(W·X + b)`, then thresholds it (usually at `0.5`) to get a class label.
2. **The cost** (Log Loss / Binary Cross-Entropy) heavily penalizes confident wrong predictions — it's what gradient descent minimizes.
3. **Gradient Descent** and scikit-learn's solvers do the same job: iteratively nudge `W`/`b` to shrink that cost.
4. **The full pipeline**: feature engineering → outlier handling → `ColumnTransformer` → `LogisticRegression`, all wrapped in one `Pipeline` fit on the training split only.
5. **Hyperparameters you actually tune, in priority order**: `C` (regularization strength) first, `class_weight` if your classes are imbalanced, `solver`/`max_iter` only if you hit a compatibility error or a convergence warning.
6. **One modern gotcha worth remembering**: `penalty` is deprecated in recent scikit-learn — use `l1_ratio` (`0`=l2, `1`=l1, in-between=elasticnet) together with `C` instead.
