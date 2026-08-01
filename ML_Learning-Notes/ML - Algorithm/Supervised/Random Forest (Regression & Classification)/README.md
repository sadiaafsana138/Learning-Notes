# Random Forest (Classification & Regression) — Learning Notes

One weak, unstable Decision Tree becomes a strong, stable model the moment you grow **hundreds of slightly different versions of it and average their votes** — that single idea is Random Forest.

---

## 1. Title & One-Line Hook

**Random Forest = many Decision Trees + Bagging (bootstrap sampling) + random feature subsampling at every split, combined by majority vote (classification) or averaging (regression).**
It was invented to fix the one thing that makes a single Decision Tree unreliable: it memorizes whatever data you give it.

---

## 2. What Is It & Where Does It Sit

Random Forest is a **supervised ensemble learning** method built entirely out of Decision Trees. It handles **both**:

- **Classification** — `RandomForestClassifier` → predicts a class label (e.g. malignant/benign) by **majority vote** across all trees.
- **Regression** — `RandomForestRegressor` → predicts a number (e.g. disease-progression score) by **averaging** all trees' predictions.

It sits in the same family branch as Decision Trees (non-parametric, no distance/scaling needed) but one level up in the hierarchy: it is an **ensemble** — a "model of models" — not a single model.

বাংলায় বললে: একটা Decision Tree হলো একজন মানুষের মতামত, যেটা ভুলও হতে পারে; Random Forest হলো শত শত মানুষের মতামত নিয়ে ভোট করা — একজনের ভুল অন্যদের সঠিক উত্তরে চাপা পড়ে যায়।

---

## 3. Where It Comes From & Why It Was Invented

Random Forest did not appear out of nowhere — it is the endpoint of a very specific lineage, and understanding that lineage *is* understanding why it works.

**Decision Tree → Bagging → Random Forest**

1. **Decision Tree** — greedily splits data into purer and purer groups. Grown fully (no pruning), it fits the training set almost perfectly. That is exactly the problem: an unpruned tree has **low bias but very high variance** — it is extremely sensitive to the exact rows it was trained on. Change a handful of training examples and the whole tree structure can change. (See `../Decision Tree (Regression & Classification)/README.md` for the base algorithm.)
2. **Bagging (Bootstrap Aggregating)**, proposed by Leo Breiman in 1996 — the first fix. Train the *same* high-variance model (e.g. a Decision Tree) many times, each time on a different **bootstrap sample** (random sample of the data, drawn *with replacement*, same size as the original), then **average** the predictions (or vote, for classification). Averaging many noisy-but-unbiased estimators cancels out a lot of the noise, so variance drops.
3. **Random Forest**, proposed by Leo Breiman in **2001** — bagging alone still leaves the trees quite similar to each other, because bootstrap samples overlap heavily and the strongest feature usually wins the top split in almost every tree. Breiman added a second source of randomness: at **every split**, only a **random subset of the features** is even considered. This forces different trees to latch onto different features, making them genuinely different (decorrelated) from each other — and decorrelation is precisely what makes averaging effective (see the math in Section 5).

So: Random Forest = Bagging **+ extra randomness in feature selection**. That second ingredient is the entire reason it beats plain bagged trees.

বাংলায়: প্রথমে একটা গাছ বানানো শেখা হলো (Decision Tree), তারপর একই গাছ বহুবার আলাদা আলাদা স্যাম্পল দিয়ে বানিয়ে গড় করা শেখা হলো (Bagging), শেষে প্রতিটা গাছকে জোর করে আলাদা আলাদা ফিচার দিয়ে বানানো শেখা হলো (Random Forest) — যাতে গাছগুলো একরকম চিন্তা না করে।

---

## 4. Intuition

**"Ask a crowd of semi-independent experts and take the majority/average vote instead of trusting one opinion."** This is the **wisdom of the crowd** — the idea (straight from the handwritten notes) that large, diverse, independent groups often make better collective judgments than even individual experts, because individual errors are random and cancel out in the aggregate, while the true signal stays.

Classic medical analogy from the notes: if you ask one doctor "cancer or not?" you get one opinion, which might be wrong. Ask 100 independent doctors and take the majority vote — the chance that *more than half* are wrong at the same time is much lower than the chance that *one* is wrong. Random Forest does exactly this with trees instead of doctors: `y1, y2, ..., yn` → e.g. "Yes" = 60 votes, "No" = 40 votes → final prediction = **Yes**.

The catch (and the reason feature-randomness matters): this only works if the "doctors" are not all reading from the exact same notes and reaching the exact same conclusion. If every tree is nearly identical, their errors are *correlated* — they all get the same cases wrong together, and voting doesn't help at all.

বাংলায়: একজন ডাক্তারের মতের চেয়ে ১০০ জন স্বাধীন ডাক্তারের ভোট বেশি বিশ্বাসযোগ্য — কারণ সবার ভুল একসাথে হওয়ার সম্ভাবনা কম। কিন্তু ১০০ জনই যদি একই বই পড়ে একই রকম ভাবে, তাহলে ভোট করেও লাভ নেই — তাই প্রতিটা গাছকে আলাদা ফিচার দিয়ে "আলাদাভাবে চিন্তা" করানো হয়।

---

## 5. Math & Formula(s)

### 5.1 Bootstrap Sampling — why ~63.2% unique rows per tree

Each tree is trained on a **bootstrap sample**: draw `n` rows *with replacement* from an `n`-row dataset (so some rows appear multiple times, others not at all).

For one particular row, the probability it is **not** picked in a single draw is `1 - 1/n`. Since draws are independent and there are `n` draws:

```
P(row never chosen in n draws) = (1 - 1/n)^n
```

Taking the limit as `n → ∞` (this is one of the standard definitions of `e`):

```
lim(n→∞) (1 - 1/n)^n = 1/e ≈ 0.3679
```

So roughly **36.8%** of rows are left out of any given bootstrap sample (these are the **out-of-bag / OOB** rows for that tree — see Section 7 of the notebook), and therefore:

```
P(row included at least once) = 1 - 1/e ≈ 0.6321  →  ~63.2% unique rows per tree
```

Every tree effectively trains on a different ~63%-overlapping-but-not-identical view of the data. That alone (bagging) already reduces variance; Random Forest adds feature-randomness on top.

### 5.2 Random Feature Subsampling (`max_features`)

At **every single split** (not just once per tree), only a random subset of the `p` available features is considered as split candidates. Typical defaults:

- **Classification**: `max_features = sqrt(p)` — e.g. `p = 10` features → `sqrt(10) ≈ 3.16 → 3` (scikit-learn truncates via `int()`, it does not round up). Verified against a fitted `DecisionTreeClassifier(max_features='sqrt')` on 10 features: `max_features_` resolves to exactly `3`.
- **Regression**: traditionally `max_features = p / 3`. (Note: current scikit-learn defaults are `'sqrt'` for `RandomForestClassifier` and `1.0`, i.e. *all* features, for `RandomForestRegressor` — always check `model.get_params()['max_features']` for the version you're running; the `p/3` rule of thumb is still the classic textbook recommendation worth tuning around.)

### 5.3 Aggregation — the final prediction

```
Classification:  ŷ = mode(T1(x), T2(x), ..., TB(x))      (majority vote across B trees)
Regression:      ŷ = (1/B) * Σ Tb(x)   for b = 1..B      (mean across B trees)
```

### 5.4 Feature Importance

For each tree, every split gets credit for how much it decreased impurity (Gini/Entropy for classification, MSE/variance for regression), weighted by the fraction of samples that reached that node. A feature's importance in one tree = the sum of impurity decrease over every split that used it. The forest's importance = that value **averaged across all B trees**, then normalized so all importances sum to 1. This is exactly what `.feature_importances_` returns.

### 5.5 ⭐ The Key Formula — Why Averaging Correlated Trees Doesn't Fully Kill Variance

This is the mathematical heart of "why Random Forest works better than plain Bagging," and the reason feature-randomness exists at all.

Suppose we average `N` trees, each individually having variance `σ²` (same variance, since they are grown the same way), and every pair of trees has **average pairwise correlation `ρ`** between their predictions. The variance of the *average* prediction is:

```
Var(sum of N trees) = N·σ² + N(N-1)·ρ·σ²        (N variance terms + N(N-1) covariance terms, Cov(Ti,Tj) = ρσ²)

Var(mean of N trees) = Var(sum) / N²
                      = σ²/N + ((N-1)/N)·ρ·σ²
                      = ρσ² + (1-ρ)σ²/N            (exact algebraic identity, true for every N — just regroup the terms:
                                                     σ²/N + ((N-1)/N)ρσ² = σ²/N + ρσ² - ρσ²/N = ρσ² + (1-ρ)σ²/N)
```

**`Var(mean) = ρσ² + (1-ρ)σ²/N`**

Read this formula in two pieces:

- `(1-ρ)σ²/N` — the part that **shrinks as `N` grows**. More trees, less variance. This is what plain bagging already exploits.
- `ρσ²` — a **floor that never goes away**, no matter how many trees you add (as `N → ∞`, `Var(mean) → ρσ²`, not 0). If the trees are highly correlated (`ρ` close to 1), this floor is almost as high as a single tree's variance `σ²` — adding more trees barely helps.

**This is exactly why Random Forest forces random feature subsampling**: it exists purely to push `ρ` down. Lower `ρ` → lower floor → averaging actually pays off. Plain bagging (bootstrap only, no feature randomness) still leaves `ρ` fairly high because every tree still sees all features and tends to split on the same dominant feature first.

#### Numeric illustration (σ² = 1, N = 100)

| Pairwise correlation ρ | `Var(mean) = ρσ² + (1-ρ)σ²/N` | vs single tree (σ²=1) |
|---|---|---|
| ρ = 0.9 (highly correlated trees, weak decorrelation) | `0.9×1 + 0.1×1/100 = 0.9 + 0.001 = 0.901` | only ~10% variance reduction |
| ρ = 0.3 (well decorrelated trees, feature-randomness working) | `0.3×1 + 0.7×1/100 = 0.3 + 0.007 = 0.307` | ~69% variance reduction |

Same 100 trees, same per-tree variance — the *only* thing that changed is the correlation between trees, and the resulting variance is **~3x lower**. This single number is the entire justification for random feature subsampling: it is not a minor tweak, it is the mechanism that makes the forest work at all.

---

## 6. Algorithm Steps (Pseudocode)

```
Given: training data D of size n, number of trees B, features count p

for b = 1 to B:
    1. Bootstrap: draw a sample D_b of size n from D, with replacement
       (≈63.2% unique rows, ≈36.8% left out as "out-of-bag" for this tree)
    2. Grow a Decision Tree T_b on D_b:
           at every node, before choosing the best split:
               randomly select m features out of p available
               (m = sqrt(p) typical for classification, p/3 typical for regression)
               choose the best split using ONLY those m features
               (criterion = Gini/Entropy for classification, MSE/variance-reduction for regression)
       grow the tree fully / deep — NO pruning (each tree is allowed to overfit its own bootstrap sample)
    3. Store T_b

Prediction for a new point x:
    collect predictions T_1(x), T_2(x), ..., T_B(x)
    Classification -> return the majority class (mode)
    Regression     -> return the mean
```

The two random ingredients — step 1 (row bootstrap) and the inner loop of step 2 (feature subsampling) — are exactly the "(i) Random Sampling, (ii) Random Feature Sampling, (iii) Combined" from the handwritten notes.

---

## 7. Key Hyperparameters

| Hyperparameter | What it controls | Too low | Too high |
|---|---|---|---|
| `n_estimators` | Number of trees (`B`) in the forest | Few trees → high variance still, forest barely better than one tree, unstable score | Diminishing returns past a plateau; wastes training/prediction time and memory for no accuracy gain |
| `max_depth` | How deep each individual tree may grow | Shallow trees → each tree underfits (high bias); if all trees underfit similarly the forest underfits too | Fully deep trees (default) → each tree overfits its bootstrap sample, but that's usually fine *because* averaging cleans it up — main risk is only on small/noisy datasets |
| `max_features` | Size of the random feature subset considered at each split | Very small (e.g. 1) → trees become weak/very decorrelated, can underfit and need many more trees to compensate | Set to all features (no subsampling) → trees become correlated again, losing the whole decorrelation benefit (Section 5.5) |
| `min_samples_leaf` | Minimum samples required in a leaf node | Too small (e.g. 1) → leaves fit individual noisy points, more overfitting per tree | Too large → leaves get forced to average over dissimilar points, trees underfit |
| `bootstrap` | Whether trees are trained on bootstrap samples (`True`) or the full dataset (`False`) | `False` disables the row-sampling half of bagging → trees only differ via feature randomness, less diversity, and OOB scoring becomes unavailable | N/A |
| `oob_score` | Whether to compute the out-of-bag validation estimate (needs `bootstrap=True`) | `False` → no free validation signal, must rely purely on a held-out test set / CV | Slight extra computation, otherwise no downside — usually worth turning on |

---

## 8. Assumptions

Random Forest inherits a Decision Tree's very weak assumptions: it is **non-parametric** — no assumption about linear relationships, no assumption of feature independence, no distributional assumption on the target, no need for scaling (splits are threshold comparisons, not distances). It can model arbitrary non-linear boundaries and feature interactions automatically.

Its one real assumption is implicit: **the trees must actually be diverse enough that averaging helps.** If there are very few features, or the informative features are few and highly correlated with each other, `max_features` subsampling can't create much diversity — every random subset still contains "the same" signal, `ρ` stays high (Section 5.5), and the benefit over a single tree shrinks toward zero. Random Forest needs *some* redundancy/diversity in the feature space to exploit.

---

## 9. Advantages

- **Much lower variance / less overfitting** than a single Decision Tree — the direct consequence of the `Var(mean) = ρσ² + (1-ρ)σ²/N` math in Section 5.5.
- **Robust to noise and outliers** — a handful of mislabeled or extreme rows only heavily influence the bootstrap samples that happen to include them, not every tree.
- **Handles non-linear relationships and feature interactions** natively, same as a Decision Tree, without any manual feature engineering.
- **Free feature importance ranking** (`.feature_importances_`) with no extra modeling step.
- **Little preprocessing needed** — no scaling/normalization required, handles a mix of feature scales fine.
- **OOB score** — a "free" validation-like estimate computed during training itself, no separate validation split required (Section 5.1 explains the ~36.8% OOB rows this relies on).

---

## 10. Disadvantages

- **Much less interpretable than a single tree** — a fitted tree prints as a readable flowchart; a forest of hundreds of trees has no such simple summary, only aggregate statistics like feature importance.
- **Slower to train and predict** — training `B` trees costs roughly `B` times a single tree's cost; prediction requires querying every tree and aggregating.
- **Larger memory footprint** — hundreds of full tree structures must be stored, versus one tree.
- **Can still struggle with very high-dimensional sparse data** (e.g. bag-of-words text features), where random feature subsets rarely land on the informative ones.
- **Poor extrapolation in regression** — like any tree-based method, predictions are bounded by the range of leaf values seen in training; it cannot predict outside the training target range.
- **Feature importance can be biased toward high-cardinality / continuous features**, which get more opportunities to produce "good-looking" splits purely because they offer more possible threshold values, not necessarily because they are more informative.

---

## 11. Classification vs Regression Version

| Aspect | `RandomForestClassifier` | `RandomForestRegressor` |
|---|---|---|
| Aggregation rule | Majority vote across trees (or averaged class probabilities via `predict_proba`) | Mean of all trees' predicted values |
| Split criterion | Gini impurity or Entropy (information gain) | MSE / variance reduction (or MAE, Poisson deviance) |
| Base tree | `DecisionTreeClassifier` per tree | `DecisionTreeRegressor` per tree |
| Typical `max_features` | `sqrt(p)` | `p/3` (classic rule of thumb; check your sklearn version's actual default) |
| Evaluation metrics | Accuracy, Precision, Recall, F1, Confusion Matrix | MSE, RMSE, MAE, R² |
| Notebook section | Sections 1–7 (Breast Cancer dataset) | Section 8 (Diabetes dataset) |

---

## 12. Decision Tree → Random Forest: Exactly What Improved, and Why

This is the comparison this whole topic is built around — treat this table as the answer key.

| Aspect | Decision Tree (single) | Random Forest | Mechanism — *why* it changes |
|---|---|---|---|
| **Variance / overfitting** | High — an unpruned tree fits training noise almost perfectly (in this notebook: train R² = 1.000 on the Diabetes regression task) | Much lower — same forest scored train R² = 0.924, and the train−test *gap* shrank from **0.939** (single tree) to **0.490** (forest) | **Bagging averages out noise**: each tree overfits its *own* bootstrap sample's noise, but that noise is different per tree, so averaging cancels most of it out (Section 5.5's `(1-ρ)σ²/N` term shrinking with more trees) |
| **Stability to small data changes** | Low — changing a few rows or the random seed can restructure the whole tree (this is literally why it has high variance) | High — removing/changing a few rows barely changes the *forest's* aggregate vote, since it only perturbs a fraction of the bootstrap samples | Each tree only "sees" ~63.2% of rows (Section 5.1); a data change affects roughly that same fraction of trees, diluted by averaging over all `B` trees |
| **Interpretability** | High — a shallow tree is literally readable as a flowchart; `plot_tree`/`export_text` show the exact logic | Low — hundreds of trees, no single flowchart; must fall back on aggregate `feature_importances_` | There is no way to compress hundreds of trees back into one simple rule set; this is the direct cost of ensembling |
| **Training speed** | Fast — one tree, one pass | Slower — roughly `B`× the cost of training one tree (though trees train independently, so this parallelizes trivially across cores) | It is literally training `B` trees instead of 1 |
| **Accuracy (typical)** | Lower on unseen data due to overfitting | Equal or higher — in this notebook: classification test accuracy rose from 0.912 (single tree) to 0.956 (200-tree forest); regression test R² rose from 0.061 to 0.434 | Lower variance directly translates to better generalization, as long as bias doesn't rise too much (it barely does, since deep trees already have low bias) |
| **Handling of noise / outliers** | Poor — a single mislabeled/extreme row can force a split that misclassifies a whole region | Good — an outlier only appears in the ~63% of bootstrap samples that happen to include it, so at most a fraction of the trees are misled by it | Bootstrap sampling dilutes any single row's influence across the ensemble instead of letting it dominate one global model |

**The one-sentence mechanism**: bagging alone (bootstrap + averaging) already reduces variance because trees make *different* random mistakes that partly cancel; random feature subsampling pushes the inter-tree correlation `ρ` down further, which — per the `Var(mean) = ρσ² + (1-ρ)σ²/N` formula — is what lets the variance actually keep dropping toward `σ²/N` instead of getting stuck near a high `ρσ²` floor. **Without the feature-randomness step, trees on overlapping bootstrap samples still tend to agree on the strongest feature's split, stay correlated, and averaging buys much less than the numbers above show.**

> See the Decision Tree README (`../Decision Tree (Regression & Classification)/README.md`) for the base algorithm this builds on — entropy/Gini, information gain, pruning, and the exact overfitting behaviour Random Forest is designed to fix.

### Random Forest vs Gradient Boosting — the other major tree-ensemble family

Random Forest is **one of two** major ways to combine trees into an ensemble — it's worth knowing there's a second family with the opposite strategy:

| | Random Forest (Bagging) | Gradient Boosting |
|---|---|---|
| Trees built | **In parallel**, independently of each other | **Sequentially**, one at a time |
| What each new tree targets | Its own random bootstrap sample of the *original* target | The **residual errors** left over by all previous trees |
| Primary effect | Reduces **variance** (trees decorrelated, errors cancel on average) | Reduces **bias** (each tree explicitly corrects the previous ensemble's mistakes) |
| Overfitting risk | Low, and *decreases* as more trees are added | Higher — more boosting rounds can eventually overfit; needs `learning_rate`/early stopping |
| Typical individual tree | Deep, low-bias, high-variance trees | Shallow, high-bias, low-variance trees ("weak learners") |

In short: **bagging tames a strong-but-unstable learner by averaging; boosting builds up a strong learner out of many weak ones by correcting mistakes step by step.** Random Forest is the bagging family; XGBoost/LightGBM/CatBoost/`GradientBoostingClassifier` are the boosting family.

---

## 13. Evaluation Metrics

**Classification** (Section 4 & 7 of the notebook, breast cancer dataset):

```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)              — "of predicted positives, how many were right"
Recall    = TP / (TP + FN)               — "of actual positives, how many were caught"
F1        = 2 · (Precision · Recall) / (Precision + Recall)
```

Plus the **Confusion Matrix** — a 2×2 (or k×k) grid of actual vs predicted class counts, showing exactly which classes get confused with which.

**Regression** (Section 8 of the notebook, diabetes dataset):

```
MSE  = (1/n) · Σ (y_i - ŷ_i)²
RMSE = sqrt(MSE)                          — same units as the target, easier to interpret
MAE  = (1/n) · Σ |y_i - ŷ_i|              — less sensitive to large errors than MSE
R²   = 1 - (Σ (y_i - ŷ_i)²) / (Σ (y_i - ȳ)²)     — fraction of target variance explained (1.0 = perfect, 0 = no better than predicting the mean)
```

---

## 14. When to Use / When Not to Use

**Use Random Forest when:**
- You want strong out-of-the-box accuracy with minimal preprocessing and minimal tuning.
- The relationship between features and target is non-linear / involves interactions you don't want to hand-engineer.
- You need a reasonably fast, parallelizable baseline before trying boosting methods.
- You want built-in feature importance to understand which inputs matter.
- You need an internal validation estimate (OOB score) without sacrificing training data to a validation split.

**Avoid / reconsider when:**
- You need a genuinely interpretable model (a compliance/regulatory setting demanding "show me the exact rule") — use a single pruned Decision Tree or a linear model instead.
- The data is very high-dimensional and sparse (e.g. raw text/TF-IDF) — linear models or gradient boosting often do better.
- You need to extrapolate a regression target beyond the training range — tree-based models cannot predict outside observed leaf values; use a parametric model.
- Training/inference latency or memory is tightly constrained — hundreds of trees are heavier than one tree or a linear model.
- You have very few, highly correlated features — the decorrelation mechanism (Section 5.5) has little room to work, and gains over a single tuned tree may be small.

---

## 15. Common Pitfalls & Practical Tips

- **Tune `n_estimators` by watching the plateau, not by maximizing.** The notebook's Section 6 sweep (1 → 500 trees) shows test accuracy essentially flattening by ~20–50 trees; going to 500 costs far more compute for no measurable gain. Use the OOB score or a validation curve to find where it flattens, then stop.
- **Don't over-trust feature importance when features are correlated.** If two features carry the same information, impurity-based importance can split "credit" between them unevenly across trees, making both look individually less important than they really are jointly. Consider permutation importance for a more reliable check.
- **A forest can still overfit** if trees are allowed to be *too* flexible on a *small* dataset — very small `min_samples_leaf` (e.g. 1) combined with a small `n`, particularly with few, weak, or noisy features providing little diversity to exploit. Watch the train−test gap, exactly as demonstrated in Section 5 of the notebook, even for a forest.
- **Always compare against a single tree on the *same* split** (Section 5/8.1 in the notebook) — it's the cleanest way to *prove* to yourself the ensemble is actually helping and by how much, rather than assuming it.
- **Turn on `oob_score=True` for free** whenever `bootstrap=True` (the default) — it costs little and gives a sanity check against your test score without touching held-out data.

---

## 16. Notebook Map

| Notebook Section | What It Demonstrates |
|---|---|
| 1. Data Loading and Splitting | `load_breast_cancer`, 80/20 stratified train/test split |
| 2. Baseline Model & Grid Search | Default `DecisionTreeClassifier`, then `GridSearchCV` over `criterion` × `max_depth` |
| "Training on different depth" | `max_depth` = 2, 3, 4, 5 swept manually, train vs test accuracy at each — classic bias/variance walk |
| 3. Random Forest (Ensemble Learning) | `GridSearchCV` over `n_estimators` × `criterion` × `max_features` for `RandomForestClassifier`; train vs test accuracy of the best model |
| 4. Feature Importance & Confusion Matrix | Best RF's precision/recall/F1, confusion matrix plot, top-15 feature importance bar chart |
| 5. Decision Tree vs Random Forest — Side-by-Side | Single unrestricted tree vs 200-tree forest on the *same* split; train/test accuracy bar chart + explicit train−test gap comparison |
| 6. Effect of `n_estimators` | Accuracy vs number of trees (1 → 500), showing the diminishing-returns plateau |
| 7. Out-of-Bag (OOB) Score | `oob_score=True` demo, OOB score vs actual held-out test accuracy |
| 8. Random Forest Regression — Diabetes | Full regression walkthrough: DT vs RF R²/MSE/RMSE/MAE comparison (8.1), prediction-vs-actual scatter (8.2), feature importance (8.3), `n_estimators` sweep + OOB R² (8.4) |
| 9. Summary | Recap of every finding above in one cell |

---

## 17. One-Paragraph Exam-Ready Summary

Random Forest is a supervised ensemble that fixes a Decision Tree's core weakness — high variance, i.e. it overfits and becomes unstable to small data changes — by growing `B` trees on **bootstrap samples** (row sampling with replacement, giving each tree ~63.2% unique rows per the `1-(1-1/n)^n → 1-1/e` limit) and, at every split, restricting each tree to a **random subset of features** (`sqrt(p)` for classification, `p/3` traditionally for regression); predictions are combined by **majority vote** (classification) or **mean** (regression), and feature importance falls out as the impurity decrease averaged across all trees. The reason this actually reduces variance rather than just diluting it is captured by `Var(mean) = ρσ² + (1-ρ)σ²/N`: more trees (`N↑`) shrinks the second term, but only decorrelating the trees (`ρ↓`, achieved by the random feature step) lowers the unavoidable floor `ρσ²` — this notebook's own numbers show it working (classification train−test gap 0.088 → 0.044, regression train−test R² gap 0.939 → 0.490 going from one tree to a forest). The trade-off: you gain accuracy, stability, and a free OOB validation estimate, but lose the single tree's flowchart-level interpretability and pay more in training/prediction time — a cost/benefit that is usually well worth it, unless interpretability itself is the requirement (তখন single Decision Tree-ই ভালো), or you need Gradient Boosting's sequential error-correction instead of bagging's parallel averaging.
