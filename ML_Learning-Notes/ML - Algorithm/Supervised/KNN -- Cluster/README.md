# K-Nearest Neighbors (KNN) — Learning Notes

A complete walkthrough of **K-Nearest Neighbors** classification with `scikit-learn` on
the Wine dataset (3-class chemical classification), closing with a hyperparameter
reference thorough enough to answer "is that really all of them?" KNN is the odd one
out among this repo's algorithm notes: it has no training phase and no learned
parameters at all — every single setting is a hyperparameter.

---

## 📓 Main Notebook

| File | What's inside |
|------|---------------|
| **`KNN_Complete.ipynb`** | The full lesson, fully executed with all outputs baked in. |

> This single notebook builds on one earlier notebook (`KNN.ipynb`, now organized into
> Part 1 with section headers), plus a new hyperparameter-tuning part written directly
> into the merge. Everything is now in one place.

### Notebook contents

**Part 1 — KNN with Scikit-Learn (Wine Dataset)**
- Dataset: `sklearn.datasets.load_wine` — 178 samples, 13 chemical measurements, 3 cultivar classes.
- **Data loading and exploration**: shape, `info()`, `describe()`, class-balance countplot.
- **Train/test split** with `stratify=y`.
- **Model training**: `StandardScaler` + `KNeighborsClassifier` combined in one `Pipeline` — scaling isn't optional here, since KNN's predictions depend directly on raw distances.
- **Evaluation**: accuracy, confusion matrix, classification report (perfect 1.00 on this clean, well-separated dataset at `n_neighbors=15`).
- **Choosing k**: two full sweeps of `n_neighbors` from 5–29, one with Euclidean distance (`p=2`), one with Manhattan (`p=1`) — both find a wide plateau of `k` values that reach 100% test accuracy.

**Part 2 — Real-World Uses & Hyperparameter Tuning**
- Where KNN is used in practice, and why it's worth knowing despite being one of the simplest ML algorithms.
- **Parameters vs. hyperparameters — a special case for KNN**: unlike the Logistic/Linear Regression notebooks, `.fit()` produces *nothing learned* — just stored data (and optionally a search tree). Every setting is a hyperparameter.
- **`n_neighbors` (k)** — a live train/test accuracy sweep (`k=1` to `k=100`) showing the bias/variance trade-off directly: severe underfitting by `k=100` (both train and test collapse together).
- **`weights`** (`'uniform'` vs. `'distance'`) — a live, honestly-reported comparison (made no difference on this clean dataset — with an explanation of when it would).
- **`metric` / `p`** — extends Part 1's Manhattan-vs-Euclidean sweep with `chebyshev` and `cosine` too.
- **`algorithm`** (`'auto'`, `'brute'`, `'kd_tree'`, `'ball_tree'`) — a live, best-of-3 timing benchmark on a larger synthetic dataset at two dimensionalities, directly demonstrating the *curse of dimensionality*: tree-based search is only modestly faster at 5 features, and roughly 15–20x **slower** than brute-force at 20 features. `'auto'` wins (or ties) in both regimes.
- **`leaf_size`** — confirmed empirically to change speed only, never predictions.
- **`metric_params` / `n_jobs`** — brief reference.
- **A quick-reference table** of which hyperparameter matters most, and why.
- **A complete reference table** of all 8 hyperparameters — pulled directly from the installed scikit-learn's own signature via `inspect.signature`, so nothing is left out.

---

## 🧠 The Core Idea (in one minute)

KNN classifies a new point by looking at its `k` closest neighbors in the training
data and taking a majority vote — there's no equation being fit, no cost function
being minimized, and no weights being learned.

| Term | Plain English |
|------|---------------|
| **k (`n_neighbors`)** | how many nearby training points get a vote |
| **distance metric** | how "nearby" is measured (Euclidean, Manhattan, ...) |
| **lazy learner** | `.fit()` just stores the data; all the work happens at prediction time |
| **scaling** | mandatory — distances are meaningless if features aren't on comparable scales |
| **bias/variance trade-off** | small `k` → follows noise (overfits); large `k` → oversmoothed (underfits) |
| **curse of dimensionality** | in high dimensions, "nearest" stops being meaningful, and even the search-tree speedups stop working |
| **hyperparameter** | for KNN, this is *everything* — there are no learned parameters to contrast it with |

Part 1 shows the practical workflow end-to-end; Part 2 explains every dial you can turn
and what actually happens when you turn it.

---

## 🚀 How to Run

1. Make sure the required libraries are installed:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
2. Open the notebook in Jupyter / VS Code:
   ```bash
   jupyter notebook KNN_Complete.ipynb
   ```
3. Run the cells top to bottom (**Kernel → Restart & Run All**). The notebook is
   fully self-contained — the Wine dataset loads directly from scikit-learn, no
   external CSV required. Part 2's `algorithm` timing demo builds its own larger
   synthetic dataset in-memory via `make_classification`.

---

## ✅ Key Takeaways

1. **The model**: KNN classifies a new point by majority vote among its `k` closest stored training points — no training phase, no learned weights.
2. **Scaling is mandatory**: `StandardScaler` must run before KNN, since it operates directly on distances between raw feature values.
3. **Parameters vs. hyperparameters**: KNN is a "lazy learner" — everything (`n_neighbors`, `weights`, `metric`, `algorithm`, ...) is a hyperparameter you choose; there's nothing analogous to a learned `coef_`/`intercept_`.
4. **Tuning priority**: `n_neighbors` first (the main bias/variance knob), then `metric` if the feature space calls for it, then `weights`/`algorithm` for the rest.
5. **The curse of dimensionality is real and measurable**: tree-based neighbor search (`kd_tree`/`ball_tree`) helps a little in low dimensions but can be over an order of magnitude *slower* than brute-force in higher dimensions — `algorithm='auto'` is a safe default because it checks this for you.
6. **Benchmark honestly**: a single timing measurement can be misleading (first-call overhead, system noise) — always take the best of a few repeats before trusting a "faster/slower" claim, on this dataset or your own.
