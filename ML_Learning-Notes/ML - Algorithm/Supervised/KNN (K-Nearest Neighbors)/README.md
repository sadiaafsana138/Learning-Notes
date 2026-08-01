# K-Nearest Neighbors (KNN)

**One-line hook:** KNN predicts by looking at the `k` training points closest to a new point and copying them — majority vote for a class, average for a number — with no training step at all.

> **⚠️ Naming history / common misconception.** This folder used to be misleadingly named **"KNN — Cluster"**. That name is wrong and has been fixed. **KNN is a SUPERVISED algorithm** (it needs labeled/target data to learn from) used for **classification and regression**. It is **NOT a clustering algorithm**. The confusion happens because KNN and **K-Means** share the letter "K" and the word "nearest/distance" — but they are from two completely different families of ML (see Section 12 for a full side-by-side). If you're looking for clustering, that's a different folder, different algorithm, different math. Do not mix them up in an exam or interview.

---

## 1. What Is It & Where Does It Sit

KNN (K-Nearest Neighbors) is a **supervised, instance-based, non-parametric** algorithm that can do **both**:

- **Classification** — predict a category/label (e.g., wine cultivar, spam/not-spam).
- **Regression** — predict a continuous number (e.g., disease-progression score, house price).

It sits in the **Supervised Learning** branch of ML, alongside Linear Regression, Logistic Regression, Decision Trees, etc. — all of these need a labeled target column (`y`) during "training." KNN's twist is *how* it uses that label: instead of fitting an equation, it just **memorizes the data** and, for every new prediction, searches for the most similar stored examples.

| | KNN | K-Means (different folder!) |
|---|---|---|
| Learning type | **Supervised** | **Unsupervised** |
| Needs labels (`y`)? | Yes | No |
| What it does | Classification / Regression | Clustering (grouping unlabeled points) |
| What "k" means | Number of *neighbors* to consult per prediction | Number of *clusters/centroids* to discover |

বাংলায় বললে — KNN আর K-Means দুটো সম্পূর্ণ আলাদা জিনিস, শুধু নামে "K" আর "distance" শব্দটা মিলে যায় বলে অনেকে গুলিয়ে ফেলে। KNN-কে label (উত্তর) দেখিয়ে শেখানো হয় (supervised), আর K-Means কোনো label ছাড়াই ডেটাকে নিজে থেকে দলে ভাগ করে (unsupervised) — এই দুটো এক পরিবারের অ্যালগরিদম না।

---

## 2. Where It Comes From & Why It Was Invented

The "nearest-neighbor rule" is one of the **oldest ideas in pattern recognition** — it was formally described by **Evelyn Fix and Joseph Hodges in 1951** (a US Air Force technical report on discriminant analysis), later popularized and extended by **Thomas Cover and Peter Hart (1967)**, who proved bounds on its error rate. This predates almost every "modern" parametric ML algorithm — Logistic Regression's practical popularization, SVMs, neural network backprop — by decades.

The reasoning behind it is almost embarrassingly simple, which is exactly why it's still taught and used today:

> **"You are similar to the people (points) around you."** If something behaved a certain way in the past, and a new thing looks a lot like it, it will probably behave the same way.

This is called **instance-based learning** (or a **lazy learner**): instead of compressing the training data into a fixed set of parameters (like Linear Regression's `coef_`/`intercept_`), KNN keeps the *entire* dataset around and defers all computation to prediction time. There is no "training" in the optimization sense — `.fit()` for `KNeighborsClassifier`/`KNeighborsRegressor` just stores the data (and optionally builds a search tree).

---

## 3. Intuition

**Analogy:** Imagine judging a stranger's personality by asking "who are their 5 closest friends, and what are *those 5 people* like?" If 4 out of 5 of their closest friends are runners, you'd guess the stranger is probably a runner too (classification). If you wanted to guess the stranger's age instead, you might just average the ages of those 5 friends (regression).

That's the entire algorithm. Formally:

1. Pick how many "friends" to consult — this is `k`.
2. Measure "closeness" with a distance formula.
3. Look at the `k` closest points' labels/values.
4. Aggregate them: **vote** (classification) or **average** (regression).

তুমি তোমার আশেপাশের `k`-জন মানুষের মতোই — এই এক লাইনেই পুরো অ্যালগরিদম। নতুন কোনো ডেটা পয়েন্ট এলে, তার সবচেয়ে কাছের `k`-টা পুরনো পয়েন্ট খুঁজে বের করে তাদের answer-টাই ধার নেওয়া হয়।

---

## 4. Math & Formulas

### 4.1 Distance metrics

**Euclidean distance** (straight-line distance — the default, `p=2`):

```
d(x, y) = sqrt( Σ (xi - yi)² )      for i = 1..n features
```

**Manhattan distance** (sum of absolute differences — "city block" distance, `p=1`):

```
d(x, y) = Σ |xi - yi|
```

**Minkowski distance** (the general form both of the above are special cases of):

```
d(x, y) = ( Σ |xi - yi|^p )^(1/p)
```

- `p = 1` → Manhattan
- `p = 2` → Euclidean
- `p → ∞` → Chebyshev (distance = the single largest coordinate difference)

### 4.2 Aggregation

**Classification (majority vote):**

```
ŷ = mode( y₁, y₂, ..., y_k )     (the most frequent label among the k nearest neighbors)
```

**Regression (mean):**

```
ŷ = (1/k) · Σ yᵢ                  for the k nearest neighbors
```

**Weighted KNN** (`weights='distance'`) — closer neighbors get more say, using `1/distance` as a weight:

```
weight_i = 1 / d(query, xᵢ)

ŷ_classification = the label with the highest total weight (weighted vote)
ŷ_regression      = Σ(weight_i · yᵢ) / Σ(weight_i)          (weighted average)
```

### 4.3 Full worked-by-hand example

Six students, two features (`Study_Hours`, `Attendance_%`), a classification target (`Result`: Pass/Fail) and a regression target (`Exam_Score`), exactly as computed in the notebook (Part 0):

| Point | Study_Hours | Attendance_% | Result | Exam_Score |
|---|---|---|---|---|
| P1 | 2 | 40 | Fail | 35 |
| P2 | 3 | 50 | Fail | 42 |
| P3 | 5 | 60 | Pass | 58 |
| P4 | 7 | 80 | Pass | 75 |
| P5 | 8 | 90 | Pass | 82 |
| P6 | 1 | 30 | Fail | 28 |

**New query point:** `(Study_Hours=6, Attendance_%=70)` — what's the prediction?

**Step 1 — compute distances to every stored point:**

Euclidean example for P3: `d = sqrt((6-5)² + (70-60)²) = sqrt(1 + 100) = sqrt(101) ≈ 10.05`

| Point | Euclidean dist | Manhattan dist |
|---|---|---|
| P1 | 30.27 | 34 |
| P2 | 20.22 | 23 |
| **P3** | **10.05** | **11** |
| **P4** | **10.05** | **11** |
| P5 | 20.10 | 22 |
| P6 | 40.31 | 45 |

**Step 2 — sort ascending and take `k=3` nearest:** P3 (10.05), P4 (10.05), P5 (20.10) — the same three points win under either distance metric here.

**Step 3a — Classification (majority vote):** labels are `Pass, Pass, Pass` → **predicted `Result = Pass`** (3/3 unanimous).

**Step 3b — Regression (mean):** scores are `58, 75, 82` → **predicted `Exam_Score = (58+75+82)/3 = 71.67`**.

**Bonus — weighted regression** (`weights='distance'`, weight = `1/d`):

```
weight(P3) = 1/10.05 = 0.0995
weight(P4) = 1/10.05 = 0.0995
weight(P5) = 1/20.10 = 0.0498

ŷ_weighted = (0.0995·58 + 0.0995·75 + 0.0498·82) / (0.0995+0.0995+0.0498) ≈ 69.60
```

Because P3/P4 are closer than P5, the weighted average (`69.60`) pulls slightly away from P5's higher score (`82`) compared to the plain average (`71.67`). This exact example is executed cell-by-cell in **Part 0** of `KNN_Complete.ipynb`.

---

## 5. Algorithm Steps (Pseudocode)

KNN has no real "training" — everything happens at prediction time.

```
TRAINING ("fit"):
    store X_train, y_train as-is
    (optionally: build a kd_tree / ball_tree index for faster lookup later)
    → nothing is learned, nothing is optimized

PREDICTION, for each new query point x_new:
    1. Compute distance(x_new, xi) for every stored training point xi
    2. Sort all training points by distance, ascending
    3. Take the first k points → these are the "k nearest neighbors"
    4. Aggregate their labels/values:
           if classification: ŷ = majority_vote(labels of k neighbors)
           if regression:      ŷ = average(values of k neighbors)
    5. Return ŷ
```

Because step 4 is the *only* difference between classification and regression, `KNeighborsClassifier` and `KNeighborsRegressor` in scikit-learn share almost the entire implementation.

---

## 6. Key Hyperparameters

| Hyperparameter | Controls | Too low | Too high |
|---|---|---|---|
| `n_neighbors` (**k**) | How many neighbors vote/average | **Overfits** — follows every quirk/noise in training data (high variance); `k=1` = pure memorization | **Underfits** — predictions wash out toward the overall majority class / global mean (high bias) |
| `weights` | How much each of the `k` neighbors counts | `'uniform'`: every neighbor counts equally, even a neighbor that's barely inside the top-k | `'distance'`: very close neighbors can dominate completely, making it sensitive to single close points |
| `metric` / `p` | How "distance" is defined (Euclidean, Manhattan, Minkowski, cosine, chebyshev, ...) | Wrong metric for the data shape → "closest" stops matching real similarity | N/A — it's a choice, not a magnitude |
| `algorithm` | *How* the search is carried out: `'brute'`, `'kd_tree'`, `'ball_tree'`, `'auto'` | N/A — never changes predictions, only speed | Tree methods (`kd_tree`/`ball_tree`) can become **slower** than brute-force in high dimensions (see Section 10) |

**Tuning priority (from the notebook's own findings):** `n_neighbors` first — it's the main bias/variance knob and always matters. Then `metric` if the feature space calls for it. Then `weights`, which mattered little on the clean Wine dataset but is worth checking on noisier data. `algorithm`/`leaf_size` are pure speed knobs — tune them only once your dataset is large enough for prediction latency to actually matter.

---

## 7. Assumptions

KNN makes *fewer* assumptions than almost any other algorithm in this repo, but it isn't assumption-free:

- **Similar inputs → similar outputs.** The core assumption is that points close together in feature space have similar labels/values. If that's not true for your data, KNN has nothing to work with.
- **All features are on comparable, meaningful scales.** Distance is a sum across all features — if one feature's scale dwarfs the others, the "closeness" it measures becomes meaningless (see Section 14 and the notebook's live demonstration).
- **The stored training data is representative.** Since there's no model being fit, KNN can only be as good as the neighbors it has to draw from — sparse or unrepresentative regions of feature space get bad predictions.

---

## 8. Advantages

- **Simple to understand and explain** — "look at your closest neighbors" needs no calculus to justify.
- **Zero training cost** — `.fit()` is instant; there's no optimization loop to converge.
- **Naturally handles multi-class problems** — no one-vs-rest tricks needed (see the 3-class Wine example).
- **Non-parametric** — makes no assumption about the shape of the decision boundary (unlike Logistic Regression's inherently linear one), so it can capture non-linear patterns for free.
- **One core idea, two jobs** — classification and regression use the *exact* same neighbor-finding machinery; only the aggregation step (vote vs. average) changes.

---

## 9. Disadvantages

- **Slow at prediction time** — every single prediction must compare against (some or all of) the stored training set; the opposite of a model like Logistic Regression, whose prediction is one cheap dot product.
- **Curse of dimensionality** — in high-dimensional feature spaces, almost every point ends up roughly equidistant from the query, so "nearest" stops being a meaningful concept, and even tree-based search speedups (`kd_tree`/`ball_tree`) stop helping (the notebook measures this directly — see Section 10).
- **Sensitive to feature scaling** — a single large-magnitude feature can dominate the distance calculation and silently wreck accuracy (measured directly in the notebook: **0.806 unscaled vs. 1.000 scaled** on Wine).
- **Sensitive to irrelevant/noisy features** — every feature counts toward distance whether or not it's actually useful.
- **Sensitive to class imbalance** — if one class vastly outnumbers others in the training set, it can dominate the vote even for query points that are only "sort of" nearby.
- **Memory-heavy** — the entire training set must be kept in memory (and possibly a search tree on top of it), unlike a parametric model that only needs to store a handful of learned numbers.

---

## 10. Classification vs. Regression Version

| | `KNeighborsClassifier` | `KNeighborsRegressor` |
|---|---|---|
| Predicts | A category/label | A continuous number |
| Aggregation of the `k` neighbors | **Majority vote** (mode) | **Mean** (or weighted mean) |
| Distance/`k`/scaling machinery | Identical | Identical |
| Notebook dataset used | `load_wine` (178 rows, 13 features, 3 classes) | `load_diabetes` (442 rows, 10 features, continuous target) |
| Notebook section | Part 1 (+ Part 2 hyperparameters) | Part 3 |
| Evaluation metrics used | Accuracy, precision, recall, F1, confusion matrix | MSE, RMSE, MAE, R² |

The two estimators are, under the hood, the same neighbor search with a different last step — see Section 5's pseudocode and Section 4.3's worked example, where the *same three nearest neighbors* produce both a classification answer (`Pass`) and a regression answer (`71.67`).

---

## 11. How It Compares to Related Algorithms

| | **KNN** | **Decision Tree** | **Logistic / Linear Regression** |
|---|---|---|---|
| Learner type | **Lazy** (no training) | Eager (builds a tree) | Eager (fits weights via optimization) |
| Parametric? | **Non-parametric** | Non-parametric | **Parametric** (fixed number of weights) |
| Decision boundary shape | Local, can be very irregular/non-linear | Axis-aligned, rectangular splits | Linear (or linear in transformed features) |
| What `.fit()` produces | Nothing — stored data (+ optional tree index) | A tree of if/else split rules | Learned `coef_` / `intercept_` |
| Prediction cost | Expensive — scans/searches neighbors every time | Cheap — walk down the tree | Cheap — one dot product |
| Interpretability | Medium ("here are the neighbors that drove this") | High (readable rules) | High (readable weights) |

### KNN vs. K-Means — the classic mix-up

This is the single most common beginner confusion with KNN, and it's exactly why this folder's old name ("KNN — Cluster") was wrong and has been corrected:

| | **KNN** | **K-Means** |
|---|---|---|
| Category | Supervised — **classification & regression** | Unsupervised — **clustering** |
| Needs labels? | Yes, always | No, never |
| What "k" means | Number of **neighbors** consulted per prediction | Number of **clusters** to discover |
| What "distance" is used for | Finding the closest *labeled* training points | Assigning points to the closest *centroid* and moving centroids |
| Output | A predicted label or number for a new point | A cluster assignment (1..k) for every point, no "correct answer" involved |

They share vocabulary ("k", "nearest", "distance") purely by coincidence of naming — they solve different problems, from different branches of ML, and are not variations of each other.

---

## 12. When to Use / When NOT to Use

**Good fit when:**
- The dataset is small-to-medium sized (predictions stay fast enough).
- The feature space is low-to-moderate dimensional.
- Features are on comparable scales (or you're willing to scale them).
- You want a strong, assumption-free **baseline** before trying something fancier.
- The relationship between features and target is genuinely "local" (similar inputs really do have similar outputs).

**Poor fit when:**
- The dataset is huge — prediction-time search over millions of points is slow (even with `kd_tree`/`ball_tree`, see Section 10).
- The feature space is high-dimensional (curse of dimensionality erodes the whole notion of "nearest").
- You need very low-latency predictions in production (e.g., real-time systems) — every prediction is a search, not a lookup.
- Many features are irrelevant or noisy, and you haven't filtered/reduced them first.
- Classes are heavily imbalanced without any correction.

---

## 13. Common Pitfalls & Practical Tips

- **Always scale your features first.** `StandardScaler` (or `MinMaxScaler`) inside a `Pipeline`, every time — this is not optional for a distance-based model. The notebook shows accuracy dropping from `1.000` to `0.806` on Wine from skipping this one step.
- **Never pick `k` by guessing — sweep it.** Try a range of `k` values with cross-validation (or at least a clean train/test split) and look at the accuracy/error curve's elbow, as done throughout Parts 1-3 of the notebook.
- **Watch for imbalanced classes.** A rare class can get outvoted by a common one even among genuinely close neighbors — consider `weights='distance'`, resampling, or a larger `k` with care.
- **Consider dimensionality reduction (PCA) before KNN** if you have many features — this both fights the curse of dimensionality and can speed up neighbor search.
- **Use `algorithm='auto'`** unless you have a specific reason not to — it inspects your data and picks the fastest correct search strategy (see the notebook's own timing benchmarks in Part 2).
- **Remember there's no `coef_`/`intercept_` to inspect** — if you need to explain *why* a prediction was made, the honest answer is "these were the nearest neighbors," not "these were the important features."

---

## 14. Notebook Map

`KNN_Complete.ipynb` — everything below is fully executed with outputs baked in.

| Notebook section | What it demonstrates |
|---|---|
| **Part 0** — Distance Metrics, By Hand | Manual Euclidean & Manhattan distance calculations on a 6-point toy dataset with real numbers; manual `k=3` majority-vote classification *and* mean/weighted-mean regression on the same neighbors, before any library is used |
| **Part 1, Sections 1-4** — Wine Classification | `load_wine` (178 rows, 13 features, 3 classes), train/test split, `StandardScaler` + `KNeighborsClassifier` in a `Pipeline`, accuracy/confusion matrix/classification report |
| **Part 1, Sections 5-6** — Choosing k | Accuracy vs. `k` sweeps (`k=5..29`) for both Euclidean (`p=2`) and Manhattan (`p=1`) distance, plotted as elbow-style curves |
| **Part 1, Section 7** — Why Scaling Matters | Direct with-vs-without-`StandardScaler` comparison on Wine: **0.806 (unscaled) vs. 1.000 (scaled)** |
| **Part 2** — Real-World Uses & Hyperparameters | Applications table; parameters-vs-hyperparameters explanation; live experiments for `n_neighbors` (bias/variance via train/test gap, `k=1..100`), `weights`, `metric`/`p`, `algorithm` (timing benchmark showing the curse of dimensionality), `leaf_size`, `metric_params`/`n_jobs`; full hyperparameter reference pulled from the installed scikit-learn |
| **Part 3** — Diabetes Regression | `load_diabetes` (442 rows, 10 features), `StandardScaler` + `KNeighborsRegressor`, an MSE-vs-`k` elbow plot (best `k=6`, MSE=2891.34), final evaluation (RMSE=53.77, MAE=42.03, R²=0.454), a predicted-vs-actual scatter plot, and a `weights='uniform'` vs. `'distance'` comparison |

---

## 15. Exam-Ready Summary

KNN হলো একটা **supervised, lazy, non-parametric** algorithm যেটা classification আর regression দুটোতেই কাজ করে — `.fit()` কিছুই শেখে না (learn করে না), শুধু ডেটা মনে রাখে (store করে), আর আসল কাজ হয় prediction-এর সময়: নতুন point-এর সবচেয়ে কাছের `k`-টা neighbor খুঁজে বের করা হয় (Euclidean `d=√Σ(xi-yi)²` বা Manhattan `d=Σ|xi-yi|` distance দিয়ে), তারপর classification-এ majority vote আর regression-এ average (বা `1/distance`-weighted average) নেওয়া হয়। `k` ছোট হলে overfit করে (noise-কে follow করে), বড় হলে underfit করে (সব prediction গড়পড়তার দিকে চলে যায়) — এটাই bias-variance trade-off। Feature scaling (`StandardScaler`) **বাধ্যতামূলক**, কারণ distance calculation raw সংখ্যার উপর নির্ভর করে (notebook-এ scaling ছাড়া accuracy `1.000` থেকে `0.806`-এ নেমে যাওয়া প্রমাণ করে এটা)। উচ্চ-dimension-এ এই অ্যালগরিদম দুর্বল হয়ে পড়ে (curse of dimensionality) এবং প্রতিটা prediction-এর জন্য পুরো training data স্ক্যান করতে হয় বলে ধীরগতির। সবচেয়ে গুরুত্বপূর্ণ: **KNN ≠ K-Means** — KNN supervised classification/regression, আর K-Means unsupervised clustering; নাম আর "k"/"distance" শব্দ মিললেও এই দুটো সম্পূর্ণ ভিন্ন পরিবারের অ্যালগরিদম।
