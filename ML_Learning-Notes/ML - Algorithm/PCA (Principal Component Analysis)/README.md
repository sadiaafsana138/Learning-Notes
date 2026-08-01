# Principal Component Analysis (PCA)

**One-line hook:** PCA takes a pile of correlated, high-dimensional features and hands you back a small set of new, uncorrelated "super-features" that capture almost all the original spread (variance) in the data — no labels required.

---

## 1. What is it & where does it sit

PCA is an **unsupervised dimensionality-reduction / feature-extraction** technique. It is *not* a classifier and *not* a regressor — it never looks at a target `y`. It only looks at `X` and re-expresses it in a new coordinate system.

- Family: Unsupervised learning → Dimensionality reduction → Linear feature extraction.
- It sits **before** a supervised model in a pipeline, not instead of one. You still need a classifier (e.g. Logistic Regression) or regressor (e.g. Linear Regression) *after* PCA if you want predictions.
- Bengali intuition: **PCA কোনো "answer" শেখায় না — ও শুধু data-র shape/spread বুঝে সেটাকে ছোট আকারে, কম feature-এ, প্রায় same information নিয়ে ঘুরিয়ে দেয়।**

## 2. Where it comes from & why it was invented

PCA was introduced by Karl Pearson (1901) and later formalized by Harold Hotelling (1933). It solves several very practical problems that show up constantly in real datasets:

- **Curse of dimensionality**: every extra feature = an extra dimension in the feature space. As dimensions grow, data points become sparse and "distance" stops being meaningful — models need exponentially more data to generalize well. (This is literally the first topic in the source lecture notes for this folder — see "Notebook map / source notes" below.)
- **Redundant / correlated features**: real-world tabular data (like `mean radius`, `mean perimeter`, `mean area` in a tumor dataset) often has many columns that are just different measurements of the *same* underlying signal. Feeding all of them raw wastes capacity and can destabilize linear models (multicollinearity).
- **Visualization of high-dimensional data**: humans can only plot 2D/3D. PCA compresses 30+ dimensions down to 2-3 axes that still preserve as much "spread" (information) as mathematically possible, so you can actually *see* your data's structure.
- **Noise reduction**: small-variance directions are often dominated by measurement noise; dropping them denoises the data.
- **Speeding up downstream models**: fewer input features → faster training, less memory, less overfitting risk (fewer parameters to estimate relative to samples).

The linear-algebra idea it's built on: PCA finds the direction (a unit vector) along which the **projected data has maximum variance**. It turns out this is mathematically equivalent to finding the **eigenvectors of the covariance matrix**, sorted by their eigenvalues (each eigenvalue = variance captured along that eigenvector's direction). It is also equivalent to finding the linear projection that **minimizes reconstruction error** (squared distance between original points and their projections back from the reduced space) — maximizing variance and minimizing reconstruction error are two views of the exact same optimization problem.

## 3. Intuition

Imagine a 3D wireframe object (say, a spinning wireframe globe) casting a shadow on a wall. Depending on the angle you shine the light, the shadow (a 2D projection) can look like a tiny circle (most of the object's "spread" is hidden — bad projection) or a large, detailed silhouette that captures the object's real shape (most of the "spread" is visible — good projection). PCA is the math that finds the *best possible angle* to shine the light from, so the shadow keeps the maximum possible spread/information about the original 3D object.

Bengali intuition: **৩D object-এর shadow ২D wall-এ ফেললে, সব angle থেকে shadow same information দেয় না — PCA সেই angle খুঁজে দেয় যেখানে shadow-টা সবচেয়ে বেশি "স্প্রেড" (variance) ধরে রাখে, মানে আসল object-টা বোঝা সবচেয়ে সহজ হয়।**

## 4. Math & Formula(s)

### 4.1 Mean-centering

For a data matrix `X` with `n` samples and `d` features, first subtract the mean of each column:

```
X_centered = X - mean(X, axis=0)
```

This is mandatory — PCA is defined around variance/covariance, which is inherently about deviations from the mean. Skipping this shifts the "origin" and corrupts the covariance computation.

### 4.2 Covariance matrix

```
Σ = (1 / (n - 1)) · X_centeredᵀ · X_centered
```

`Σ` is a `d × d` symmetric matrix. Diagonal entries = variance of each feature; off-diagonal entries = covariance between feature pairs (how much two features vary together).

### 4.3 Eigenvalue / eigenvector equation

PCA solves the eigen-decomposition of the covariance matrix:

```
Σ v = λ v
```

- `v` = eigenvector (a direction in feature space) → becomes a **principal component**.
- `λ` = eigenvalue (a scalar) → the variance of the data **along that direction**.
- Sort all `(λ, v)` pairs by `λ` descending. `v₁` (largest `λ`) is PC1 (captures the most variance), `v₂` is PC2 (captures the most *remaining* variance orthogonal to PC1), and so on. All eigenvectors of a symmetric matrix are mutually orthogonal, so the principal components are automatically uncorrelated with each other.

### 4.4 Explained variance ratio

```
explained_variance_ratio_i = λ_i / Σ_j λ_j
```

Fraction of total variance captured by component `i`. Cumulative sum across the first `k` components tells you how much information you keep if you retain only `k` components.

### 4.5 Projection formula

Once you pick the top `k` eigenvectors and stack them as columns of a matrix `V` (`d × k`), the reduced representation is:

```
X_reduced = X_centered · V        # shape (n, k)
```

Each row of `X_reduced` is a sample's coordinates in the new, lower-dimensional "principal component space". To reconstruct an approximation of the original data: `X_reconstructed ≈ X_reduced · Vᵀ + mean(X)`.

### 4.6 Full worked-by-hand numeric example

Toy dataset (10 points, 2 features `x, y` — this is the same array used in `PCA.ipynb` Section 3, so you can re-run every number below yourself):

```
X = [[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0],
     [2.3, 2.7], [2.0, 1.6], [1.0, 1.1], [1.5, 1.6], [1.1, 0.9]]
```

**Step 1 — Mean:**

```
mean = [1.81, 1.91]
```

**Step 2 — Mean-center** (subtract mean from every row), then compute covariance:

```
Σ = (1/(n-1)) XᵀX  =  [[0.616556, 0.615444],
                       [0.615444, 0.716556]]
```

(Both features have similar variance ~0.62–0.72, and a large positive covariance ~0.615 — meaning `x` and `y` increase together, which matches the raw data visually.)

**Step 3 — Eigenvalues and eigenvectors of Σ** (solved via `Σv = λv`, then sorted descending by `λ`):

```
λ₁ = 1.284028      v₁ = [-0.677873, -0.735179]   (PC1)
λ₂ = 0.049083      v₂ = [-0.735179,  0.677873]   (PC2)
```

**Step 4 — Explained variance ratio:**

```
λ₁ / (λ₁ + λ₂) = 1.284028 / 1.333111 = 0.963181   → PC1 keeps 96.32% of the variance
λ₂ / (λ₁ + λ₂) = 0.049083 / 1.333111 = 0.036819   → PC2 keeps only 3.68%
```

This already tells us: for this toy dataset, one component (PC1) is basically enough — the data is almost perfectly a 1D line with a bit of noise around it.

**Step 5 — Project the centered data onto `[v₁, v₂]`** to get PCA scores (first 3 rows shown, all 10 are in the notebook):

```
centered point (2.5,2.4) -> mean (1.81,1.91) -> centered (0.69, 0.49)  -> score = (-0.827970, -0.175115)
centered point (0.5,0.7) -> centered (-1.31, -1.21)                     -> score = ( 1.777580,  0.142857)
centered point (2.2,2.9) -> centered (0.39, 0.99)                       -> score = (-0.992197,  0.384375)
```

If you only keep PC1 (drop PC2 — a 2D → 1D reduction), the reduced dataset is just the first number of each score: `[-0.828, 1.778, -0.992, -0.274, -1.676, -0.913, 0.099, 1.145, 0.438, 1.224]` — one number per point instead of two, while retaining 96.32% of the original variance.

`PCA.ipynb` Section 3 reproduces every one of these numbers with `np.linalg.eig` **and** cross-checks them against `sklearn.decomposition.PCA.fit_transform` on the same array (they match exactly, up to an arbitrary sign flip on the eigenvectors — `v` and `-v` are equally valid eigenvectors of the same eigenvalue).

## 5. Algorithm steps (pseudocode)

```
function PCA(X, k):
    1. X_centered = X - mean(X, axis=0)                 # mean-center every feature
    2. (optional but usually required) scale features   # e.g. StandardScaler
    3. Σ = (1/(n-1)) * X_centeredᵀ * X_centered          # covariance matrix, d x d
    4. eigvals, eigvecs = eig(Σ)                         # solve Σv = λv
    5. sort (eigval, eigvec) pairs by eigval descending
    6. V = first k eigvecs, stacked as columns           # top-k principal components
    7. X_reduced = X_centered · V                         # project -> shape (n, k)
    return X_reduced, V, eigvals
```

In practice `sklearn.decomposition.PCA` does this via SVD (Singular Value Decomposition) of the centered data matrix directly, rather than explicitly forming and eigen-decomposing the covariance matrix — it's mathematically equivalent but numerically more stable, especially when `d` is large.

## 6. Key hyperparameters

| Hyperparameter | What it controls | Effect if too high / too low |
|---|---|---|
| `n_components` | How many principal components to keep. Can be an int (exact count), a float in `(0,1)` (keep enough components to reach that much cumulative explained variance, e.g. `0.95`), or `None` (keep all). | **Too high** (close to original `d`): little/no dimensionality reduction benefit, keeps noise components, defeats the purpose. **Too low**: throws away real signal, downstream model underfits, reconstruction error grows, visual separability can collapse. |
| `svd_solver` | Which numerical algorithm computes the decomposition: `'full'` (exact, standard SVD — good for small/medium data), `'randomized'` (approximate, much faster for large `n_features` when `n_components` is small), `'arpack'` (for sparse/truncated SVD), `'auto'` (sklearn picks based on data size). | Wrong choice mostly affects **speed/memory**, not correctness for well-conditioned data — but `'randomized'` on very small `n_components` relative to `d` trades a small amount of accuracy for large speed gains; `'full'` on huge datasets can be slow/memory-heavy. |
| Whether to scale (`StandardScaler` before PCA) | Whether all features contribute to variance on equal footing. | **No scaling** when features have different units/ranges: PCA is dominated by whichever feature has the largest raw numeric scale (misleading components — see notebook Section 2 demo). **Scaling** when features are already comparable/meaningfully on the same scale: usually harmless, and is the safe default. |

## 7. Assumptions

- **Linearity**: PCA only finds *linear* combinations of the original features. If the true structure in the data is curved/nonlinear, PCA will need many more components to capture it than a nonlinear method would (see PCA vs t-SNE/UMAP below).
- **High variance ⇒ high importance**: PCA assumes directions with more spread are more "interesting". This is often true but not guaranteed — a low-variance direction can still be exactly the direction that matters for your target (see Disadvantages).
- **Features are roughly on comparable scales** (or you scale them first): otherwise "variance" is really just measuring units, not information.
- Implicitly assumes the mean and covariance structure are stable/representative of the data (sensitive to outliers — a few extreme points can massively distort the covariance matrix and hence the components).

## 8. Advantages (why good)

- **Dimensionality reduction**: fewer features to store, process, and feed into models.
- **Removes multicollinearity**: principal components are mathematically guaranteed to be uncorrelated with each other, which stabilizes linear models like linear/logistic regression.
- **Speeds up training**: fewer input dimensions → faster fitting, less memory, especially valuable before slower models (SVM, k-NN, deep nets on tabular data).
- **Denoising**: dropping low-variance components often drops mostly noise, leaving a cleaner signal.
- **Visualization**: makes 2D/3D plots of otherwise-unplottable high-dimensional data possible, revealing clusters/structure/outliers.

## 9. Disadvantages (why bad)

- **Components are hard to interpret**: each principal component is a linear combination of *all* original features (a weighted mix), so "PC1 = 0.68·mean_radius + 0.71·mean_perimeter + ..." doesn't have an intuitive real-world name the way a raw feature does.
- **Assumes linearity**: fails to capture genuinely nonlinear structure efficiently.
- **Sensitive to scaling**: as shown in the notebook, skipping `StandardScaler` can make results meaningless.
- **Variance ≠ relevance**: PCA can discard a low-variance direction that was actually crucial for predicting `y` (since it never looks at `y`), hurting downstream supervised performance. This is the single biggest risk of using PCA carelessly before a classifier/regressor.
- **Sensitive to outliers**: a few extreme points inflate variance/covariance in their direction, and PCA can chase those outliers instead of the "real" structure.

## 10. How PCA relates to classification/regression pipelines

PCA is a **preprocessing / transform** step — it is completely agnostic to whatever supervised task comes after it. The exact same `PCA` object, fit with the exact same API (`fit`, `transform`, `fit_transform`), can sit in front of:

- a **classifier** (e.g. `LogisticRegression`, SVM, k-NN) predicting a discrete label, or
- a **regressor** (e.g. `LinearRegression`, Ridge, Random Forest Regressor) predicting a continuous value.

`PCA.ipynb` makes this literal, not just a claim:
- **Section 7** builds `Pipeline([StandardScaler, PCA(n_components=10), LogisticRegression])` on the Breast Cancer dataset and compares accuracy with/without PCA.
- **Section 8** builds `Pipeline([StandardScaler, PCA(n_components=0.95), LinearRegression])` on the Diabetes regression dataset and compares R²/MSE with/without PCA.

Both pipelines use the *same* `PCA` transform logic; only the final estimator and the target type differ. This is the concrete proof that PCA "feeds both classification and regression pipelines" rather than being tied to one.

**Critical practical rule**: always `fit` the scaler and the PCA transform **only on the training data**, then `transform` (not `fit_transform`) the test data. Using `sklearn.pipeline.Pipeline` (as done throughout the notebook) makes this automatic and prevents train/test leakage.

## 11. How it compares to related techniques

| Technique | Type | Key difference from PCA |
|---|---|---|
| **Feature selection** (e.g. `SelectKBest`, forward/backward selection) | Selects a subset of *original* columns | PCA **transforms** features into new combined axes; feature selection **picks** a subset of existing columns, keeping them interpretable but potentially throwing away useful information spread across the dropped columns. |
| **LDA (Linear Discriminant Analysis)** | Supervised dimensionality reduction | LDA **uses the class labels** — it finds directions that maximize *separation between classes* (between-class variance / within-class variance), not just overall variance. PCA is blind to labels; LDA is not. Use LDA when you specifically want axes that help classification; use PCA when you have no labels or want a task-agnostic reduction. |
| **t-SNE / UMAP** | Nonlinear dimensionality reduction, mainly for visualization | These preserve **local neighborhood structure** (nonlinear, good for revealing tight clusters) rather than global linear variance. They are typically **not invertible**, not meant for feeding into a downstream model as reusable features, and are primarily 2D/3D visualization tools — unlike PCA, which is a general-purpose, reusable, invertible (approximately) linear transform usable anywhere in a pipeline. |

## 12. When to use / when NOT to use

**Use PCA when:**
- You have many correlated/redundant numeric features.
- You need to visualize high-dimensional data in 2D/3D.
- You want to speed up or stabilize a downstream model (fewer, decorrelated inputs).
- You suspect noise in low-variance directions and want a cheap denoising step.

**Avoid / be careful with PCA when:**
- The relationship between features and the target is strongly nonlinear and you actually need interpretability of that nonlinearity (consider nonlinear methods, or feature engineering, or tree-based models that handle raw features natively).
- You need to explain predictions in terms of the *original* business features (components are linear mixes — hard to explain to stakeholders).
- Your dataset has severe outliers you haven't handled (they'll distort the covariance matrix).
- The very low-variance features are actually the informative ones for your specific target (rare but possible — always validate downstream performance with and without PCA, as done in the notebook).

## 13. Common pitfalls & practical tips

- **Forgetting to scale**: the #1 mistake. Always `StandardScaler` (or similar) before PCA unless features are already comparably scaled.
- **Data leakage**: fitting PCA (or the scaler) on the *entire* dataset before train/test split leaks test-set statistics (mean, variance, covariance) into training. Always `fit` on train only, then `transform` test — use `sklearn.pipeline.Pipeline` to make this automatic and foolproof.
- **Picking `n_components` arbitrarily**: use the scree plot + cumulative variance (e.g. ≥95% rule) instead of guessing a round number.
- **Assuming PCA always helps supervised performance**: it doesn't always — always compare a pipeline with PCA against one without, on a held-out test set, before committing to it (exactly what Sections 7 and 8 of the notebook do).
- **Ignoring sign/direction ambiguity**: eigenvectors are only defined up to a sign flip (`v` and `-v` are both valid) — don't be alarmed if a re-run or a different library flips the sign of a component; the magnitudes and the geometry are identical.
- **Outliers**: consider robust scaling or outlier removal before PCA if your data has extreme points, since covariance is sensitive to them.

## 14. Notebook map

| Notebook section | What it demonstrates |
|---|---|
| 0. Imports | All libraries needed for the rest of the notebook. |
| 1. Load the dataset | Loads `load_breast_cancer` as a DataFrame; shows feature scale differences. |
| 2. Why scaling matters before PCA | PCA fit on raw `X` vs `StandardScaler`-transformed `X`; compares `explained_variance_ratio_` and top PC1 loadings to show unscaled PCA is misleading. |
| 3. Covariance & eigen-decomposition by hand | Manual mean-centering, covariance (`(1/(n-1))XᵀX` vs `np.cov`), `np.linalg.eig`, sorted eigenvectors, manual projection — all cross-checked against `sklearn.decomposition.PCA` on the same 10-point toy dataset (same numbers as README Section 4.6). |
| 4. Full PCA + scree plot | `explained_variance_ratio_`, cumulative variance, and a dual-axis scree plot (bars + cumulative line + 95% threshold line) on the scaled Breast Cancer data. |
| 5. Choosing n_components (≥95% rule) | Finds the smallest component count crossing 95% cumulative variance; confirms `PCA(n_components=0.95)` picks the same count automatically. |
| 6. 2D / 3D visualization | Scatter plots of PC1–PC2 and PC1–PC2–PC3, colored by malignant/benign label, showing visual separability after dimensionality reduction. |
| 7. Downstream classification demo | `StandardScaler → PCA(10) → LogisticRegression` vs no-PCA baseline; compares accuracy. |
| 8. Downstream regression demo | `StandardScaler → PCA(0.95) → LinearRegression` on `load_diabetes` vs no-PCA baseline; compares R²/MSE. |
| 9. Overall summary | Recaps every finding from the notebook in one place. |

**Note on `PCA.pdf`**: the source PDF in this folder is a scanned handwritten lecture note. Only its first two pages are actually about PCA — page 1 is a topic outline (Feature Extraction → Curse of dimensionality, Feature Selection, PCA Intuition, Geometrical Interpretation, Scikit-learn, Dataset Implementation) and page 2 works through the **curse of dimensionality** (each column = one dimension; more features/columns = higher-dimensional space; example: a feature table with columns `Age, Height, Weight, IQ` → 4 dimensions; sketches showing points along a single axis vs. scattered across a 2D plane, illustrating how added dimensions spread points out and make them harder to work with). Pages 3–8 of that PDF are unrelated SVM (Support Vector Machine) notes — margin/hinge-loss derivation, hard vs soft margin, kernel trick — that appear to be misfiled into this folder; their content is **not** PCA and has intentionally not been folded into this README so the PCA topic stays accurate. (If you find the correct PCA slides later, this README's structure has room to absorb any extra intuition/geometry diagrams under Sections 3-4.)

## 15. One-paragraph exam-ready summary

PCA হলো একটা **unsupervised, linear dimensionality-reduction** technique — no `y` involved। Problem: বেশি feature/dimension থাকলে data redundant, correlated, আর curse-of-dimensionality-এর শিকার হয়; visualize করাও কঠিন হয়ে যায়। Fix: **mean-center** করে **covariance matrix Σ = (1/(n-1))XᵀX** বানাও, তারপর **Σv = λv** সমাধান করে eigenvalues/eigenvectors বের করো — eigenvector = principal component (নতুন axis), eigenvalue = ওই axis-এ কতটা variance আছে। Eigenvalue অনুযায়ী descending sort করে top-k নেও, data-কে ওই k-টা vector-এ project করলেই dimensionality reduction হয়ে যায় (`X_reduced = X_centered · V`), আর `explained_variance_ratio_ = λᵢ/Σλ` দিয়ে বুঝবে কত % information রাখা হলো (scree plot + ≥95% rule দিয়ে k বেছে নেও)। **Scaling must** — না হলে বড় scale-এর feature (যেমন area vs smoothness) ভুলভাবে PC1 দখল করে নেয়। PCA কোনো classifier/regressor না — এটা শুধু preprocessing; একই PCA object Logistic Regression (classification) আর Linear Regression (regression) — দুটোর সামনেই বসতে পারে, কারণ ও label দেখেই না। Compare করলে: feature selection = column বাছাই (transform না), LDA = supervised (label ব্যবহার করে class-separation maximize করে), t-SNE/UMAP = nonlinear, local-structure, শুধু visualization-এর জন্য, reusable transform না। Advantage: dimensionality কমে, multicollinearity যায়, training fast হয়, noise কমে, visualization সহজ হয়। Disadvantage: component-গুলো interpret করা কঠিন (সব feature-এর mixture), linearity assume করে, scaling-sensitive, outlier-sensitive, আর variance বেশি মানেই target-এর জন্য relevant না-ও হতে পারে — তাই সবসময় train-only fit করো (leakage এড়াতে) আর PCA-সহ/ছাড়া downstream performance compare করে decide করো।
