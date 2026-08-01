# K-Means Clustering (Centroid-Based Clustering)

Group data into `k` clusters by repeatedly moving each cluster's "center" to the average of the points that belong to it — until nothing moves anymore.

## 1. What is it, and where does it sit

K-Means is an **unsupervised**, **centroid-based clustering** algorithm. It is *not* classification (no known class labels are used to train it) and *not* regression (there is no numeric target `y` being predicted). It belongs to the **Clustering** branch of unsupervised learning, alongside Dimensionality Reduction (e.g. PCA) and Anomaly Detection, which are the three broad tasks unsupervised learning is used for.

```
Machine Learning
├── Supervised          (X, y both known — True label given)
│    ├── Classification
│    └── Regression
└── Unsupervised        (only X known — no label/target)
     ├── Clustering            <-- K-Means lives here
     ├── Dimensionality Reduction
     └── Anomaly Detection
```

The core difference in the *dataset itself*: a supervised dataset has a label/target column (e.g. Pass/Fail); an unsupervised dataset has only feature columns, no answer column.

**বাংলা ইনটুইশন:** সুপারভাইজড লার্নিং-এ ডেটার সাথে "সঠিক উত্তর" (label) দেওয়া থাকে, কিন্তু আনসুপারভাইজড লার্নিং-এ কোনো উত্তর দেওয়া থাকে না — মডেলকে নিজে থেকেই ডেটার মধ্যে গোপন গঠন (hidden pattern) বা দলাদলি (grouping) খুঁজে বের করতে হয়। K-Means হলো সেই "নিজে থেকে দল খুঁজে বের করা"-র সবচেয়ে জনপ্রিয় পদ্ধতি।

## 2. Where it comes from & why it was invented

The algorithm behind K-Means — now called **Lloyd's algorithm** — was developed by Stuart Lloyd at Bell Labs in **1957** (for pulse-code modulation / signal quantization) but wasn't published until **1982**. Independently, related ideas were proposed around the same era (Forgy, MacQueen — who coined the term "k-means" in 1967). It was invented to solve a very practical problem: given a large collection of points, how do you partition them into `k` groups so that points inside each group are as close to each other as possible, using the least amount of computation possible?

It became one of the oldest and most widely used clustering algorithms because it is simple to explain, simple to implement, and computationally cheap — it scales to large datasets far better than many alternatives. It is the **foundational baseline** of clustering: almost every clustering method invented afterward (DBSCAN, Hierarchical Clustering, Gaussian Mixture Models) was designed specifically to fix one of K-Means's known weaknesses (fixed cluster shape, sensitivity to outliers, having to pre-specify `k`, etc.) while keeping its core simplicity where possible.

## 3. Intuition

**"Put k flags in a field. Everyone walks to their nearest flag. Move each flag to the average position of the people who walked to it. Repeat until nobody moves anymore."**

That's the entire algorithm. The "flags" are the centroids, the "people" are the data points, "walks to nearest flag" is the assignment step, "move flag to the average position" is the centroid-update step, and "repeat until nobody moves" is convergence.

**বাংলা ইনটুইশন:** মাঠে `k`-টা পতাকা (flag) পুঁতে দাও। প্রত্যেকে তার সবচেয়ে কাছের পতাকার দিকে হেঁটে যাক। এখন প্রতিটা পতাকাকে তার নিজের দলের মানুষদের গড় (average) পজিশনে নিয়ে যাও। যেহেতু পতাকা সরে গেছে, আবার সবাই দেখুক কোন পতাকা এখন কাছে — আবার হাঁটুক। এই প্রক্রিয়া বারবার চলবে যতক্ষণ না পতাকাগুলো একদম স্থির হয়ে যায় (আর কেউ দল বদলায় না)। সেটাই হলো K-Means-এর সম্পূর্ণ কাজ।

## 4. Math & Formula(s)

### 4.1 Objective function — WCSS / Inertia / SSE

K-Means minimizes the **Within-Cluster Sum of Squares** (WCSS), also called **inertia** in scikit-learn, or **SSE (Sum of Squared Errors)** in general statistics — all three names refer to the exact same quantity:

```
WCSS (= Inertia = SSE) = Σ_{k=1..K}  Σ_{x ∈ cluster_k}  ||x - μ_k||²
```

where `μ_k` is the centroid of cluster `k`, and `||x - μ_k||²` is the squared Euclidean distance from point `x` to its cluster's centroid. Smaller WCSS = tighter, more compact clusters.

### 4.2 Assignment rule

Each point is assigned to whichever centroid it is closest to:

```
assign x  to  argmin_k  ||x - μ_k||²
```

### 4.3 Centroid update rule

Each centroid is recomputed as the mean of all points currently assigned to it:

```
μ_k = (1 / |cluster_k|) · Σ_{x ∈ cluster_k} x
```

i.e. "the average member of the group." This is exactly why K-Means centroids are interpretable — a centroid is a real, meaningful point in feature space (e.g. "the average customer in this segment").

### 4.4 Why the cost never increases

- **Assignment step** (centroids fixed): every point is (re)assigned to the *closer* of the centroids — since it's always moving to something at least as close as before, the total squared distance cannot increase.
- **Update step** (assignments fixed): the arithmetic mean is the unique point that minimizes the sum of squared distances to a fixed set of points, so recentering on the mean cannot increase the cost either — it can only decrease it or leave it unchanged.

Both steps are individually cost-non-increasing, so the total WCSS forms a monotonically non-increasing sequence over iterations — this guarantees Lloyd's algorithm **converges** (though not necessarily to the *global* minimum — see Section 10).

### 4.5 Silhouette score

The Silhouette score measures, for each point `i`, how well it fits its own cluster compared to the next-best alternative cluster:

```
s(i) = ( b(i) - a(i) ) / max( a(i), b(i) )
```

- `a(i)` = mean distance from point `i` to every other point **in its own cluster** (cohesion — smaller is better)
- `b(i)` = mean distance from point `i` to every point in the **nearest neighboring cluster** it is *not* part of (separation — larger is better)

`s(i)` ranges from **-1 to +1**. Averaging `s(i)` over all points gives one silhouette score for a given clustering (a given choice of `k`): near **+1** = well-separated, tight clusters; near **0** = point sits on the border between two clusters; **negative** = the point is probably in the wrong cluster.

### 4.6 Fully worked numeric example (by hand)

**Dataset** (8 points, 2D — think of axes as "Study Hours" vs "IQ score", scaled down for easy arithmetic):

| Point | x (Study hrs) | y (IQ, scaled) |
|---|---|---|
| A | 1 | 1 |
| B | 1.5 | 2 |
| C | 3 | 4 |
| D | 5 | 7 |
| E | 3.5 | 5 |
| F | 4.5 | 5 |
| G | 3.5 | 4.5 |
| H | 1.2 | 1.8 |

**k = 2**, initial centroids chosen (arbitrarily, as K-Means normally does): `C1 = (1, 1)` and `C2 = (5, 7)`.

#### Iteration 1 — Assignment step

Compute squared Euclidean distance `d² = (x - cx)² + (y - cy)²` from every point to both centroids, assign to the smaller:

| Point | d² to C1=(1,1) | d² to C2=(5,7) | Assigned to |
|---|---|---|---|
| A (1, 1) | (0)²+(0)² = **0** | 16+36 = 52 | C1 |
| B (1.5, 2) | 0.25+1 = **1.25** | 12.25+25 = 37.25 | C1 |
| C (3, 4) | 4+9 = **13** | 4+9 = 13 (tie → C1 by convention, first-seen) | C1 |
| D (5, 7) | 16+36 = 52 | (0)²+(0)² = **0** | C2 |
| E (3.5, 5) | 6.25+16=22.25 | 2.25+4 = **6.25** | C2 |
| F (4.5, 5) | 12.25+16=28.25 | 0.25+4 = **4.25** | C2 |
| G (3.5, 4.5) | 6.25+12.25=18.5 | 2.25+6.25 = **8.5** | C2 |
| H (1.2, 1.8) | 0.04+0.64 = **0.68** | 14.44+27.04=41.48 | C1 |

Cluster 1 = {A, B, C, H}, Cluster 2 = {D, E, F, G}.

`SSE(iter 1) = (0 + 1.25 + 13 + 0.68) + (0 + 6.25 + 4.25 + 8.5) = 14.93 + 19.00 = 33.93`

#### Iteration 1 — Update step (recompute centroids as the mean of each cluster)

```
new C1 = mean of A(1,1), B(1.5,2), C(3,4), H(1.2,1.8)
       = ( (1+1.5+3+1.2)/4 , (1+2+4+1.8)/4 )
       = ( 6.7/4 , 8.8/4 )
       = ( 1.675 , 2.2 )

new C2 = mean of D(5,7), E(3.5,5), F(4.5,5), G(3.5,4.5)
       = ( (5+3.5+4.5+3.5)/4 , (7+5+5+4.5)/4 )
       = ( 16.5/4 , 21.5/4 )
       = ( 4.125 , 5.375 )
```

Centroids moved from `(1,1)→(1.675, 2.2)` and `(5,7)→(4.125, 5.375)`. They moved, so we must iterate again.

#### Iteration 2 — Assignment step (using the new centroids)

| Point | d² to C1=(1.675,2.2) | d² to C2=(4.125,5.375) | Assigned to |
|---|---|---|---|
| A (1,1) | (0.675)²+(1.2)² = 0.456+1.44 = **1.896** | (3.125)²+(4.375)² = 9.77+19.14=28.91 | C1 |
| B (1.5,2) | (0.175)²+(0.2)² = 0.031+0.04=**0.071** | (2.625)²+(3.375)²=6.89+11.39=18.28 | C1 |
| C (3,4) | (1.325)²+(1.8)² =1.756+3.24=**5.00** | (1.125)²+(1.375)²=1.266+1.89=**3.156** | C2 |
| D (5,7) | (3.325)²+(4.8)²=11.06+23.04=34.10 | (0.875)²+(1.625)²=0.766+2.64=**3.40** | C2 |
| E (3.5,5) | (1.825)²+(2.8)²=3.33+7.84=11.17 | (0.625)²+(0.375)²=0.39+0.14=**0.53** | C2 |
| F (4.5,5) | (2.825)²+(2.8)²=7.98+7.84=15.82 | (0.375)²+(0.375)²=0.14+0.14=**0.28** | C2 |
| G (3.5,4.5) | (1.825)²+(2.3)²=3.33+5.29=8.62 | (0.625)²+(0.875)²=0.39+0.766=**1.16** | C2 |
| H (1.2,1.8) | (0.475)²+(0.4)²=0.226+0.16=**0.386** | (2.925)²+(3.575)²=8.56+12.78=21.34 | C1 |

Note point **C** flipped from Cluster 1 (iteration 1) to Cluster 2 (iteration 2) — exactly the kind of re-assignment Lloyd's algorithm is designed to keep doing until stable. New clusters: Cluster 1 = {A, B, H}, Cluster 2 = {C, D, E, F, G}.

`SSE(iter 2) = (1.896+0.071+0.386) + (3.156+3.40+0.53+0.28+1.16) ≈ 2.353 + 8.526 ≈ 10.88`

*(The individual squared-distance terms above are rounded to 2-3 decimals for readability; adding the unrounded values gives the precise `SSE = 10.883125`, which is what "≈10.88" refers to.)*

SSE dropped from `33.93 → 10.88` — confirming the monotonic decrease proven in Section 4.4.

#### Iteration 2 — Update step

```
new C1 = mean of A(1,1), B(1.5,2), H(1.2,1.8)
       = ( (1+1.5+1.2)/3 , (1+2+1.8)/3 ) = (3.7/3, 4.8/3) = (1.233, 1.6)

new C2 = mean of C(3,4), D(5,7), E(3.5,5), F(4.5,5), G(3.5,4.5)
       = ( (3+5+3.5+4.5+3.5)/5 , (4+7+5+5+4.5)/5 )
       = (19.5/5, 25.5/5) = (3.9, 5.1)
```

Running a 3rd iteration with centroids `(1.233,1.6)` and `(3.9,5.1)` would reassign every point to the *same* cluster it's already in (A, B, H are clearly nearest to the tight bottom-left centroid; C, D, E, F, G are clearly nearest to the top-right centroid) — the centroids would stop moving. **The algorithm has converged**: final clusters are `{A, B, H}` and `{C, D, E, F, G}`, with final centroids `≈ (1.23, 1.6)` and `(3.9, 5.1)`.

## 5. Algorithm steps (pseudocode)

```
function KMeans(X, k, max_iter):
    # 1. Initialize
    centroids = pick k initial centroids       # random, or k-means++ (smarter spread-out picks)

    repeat:
        # 2. Assignment step
        for each point x in X:
            assign x to the cluster of the nearest centroid
                    (argmin_k ||x - centroid_k||²)

        # 3. Update step
        for each cluster k:
            centroid_k = mean of all points assigned to cluster k

    until centroids stop moving (converged)  OR  max_iter reached

    return cluster assignments, final centroids, final WCSS/inertia
```

## 6. Key hyperparameters

| Hyperparameter | What it controls | Effect if too high | Effect if too low |
|---|---|---|---|
| `n_clusters` (k) | How many clusters/centroids to find | Over-segments real groups into meaningless slices, WCSS trivially near 0 (at k = n, every point is its own cluster) | Under-segments — forces genuinely different groups to merge into one, high WCSS, poor separation |
| `init` | How initial centroids are chosen: `'random'` vs `'k-means++'` | N/A (categorical) | `'random'` risks poor starting points → more likely to land in a bad local minimum; `'k-means++'` (sklearn default) spreads initial centroids apart, converges faster and more reliably |
| `n_init` | How many independent times the whole algorithm is run (with different initial centroids); the best (lowest inertia) run is kept | Diminishing returns — more compute for very little extra reliability once already stable | `n_init=1` means you rely on a single lucky/unlucky initialization — much more likely to report a locally-optimal, sub-par clustering |
| `max_iter` | Max number of assign→update loop iterations before forcing a stop | Rarely a problem — K-Means usually converges quickly (few dozen iterations); a wastefully high cap just risks extra compute in edge cases that never converge | If too low, algorithm may be cut off before convergence, returning an unstable/unfinished clustering |
| `random_state` | Seed controlling the randomness of initial centroid placement | N/A | N/A — but leaving it unset makes results non-reproducible between runs |

## 7. Assumptions

- Clusters are roughly **spherical/convex** and of **similar size and density** (K-Means compares distance-to-a-single-center, so it implicitly assumes "round blobs").
- The chosen **distance metric** (almost always Euclidean) meaningfully reflects real similarity between points — features must be on comparable, well-scaled ranges for this to hold.
- The number of clusters `k` must be **chosen upfront** — the algorithm does not discover it on its own.

## 8. Advantages

- Simple to understand and implement.
- Fast and scales well even to large datasets (linear in the number of points per iteration).
- Easy to interpret — a centroid is a real, meaningful "average member" of its cluster.
- Works very well when clusters genuinely are roughly spherical and similarly sized — which covers a large fraction of real-world use cases (customer segmentation, color quantization, etc.).

## 9. Disadvantages

- Must choose `k` in advance (mitigated with the Elbow method / Silhouette score, Section 13).
- Sensitive to **initial centroid placement** — can converge to a **local minimum** of WCSS rather than the true global optimum. Mitigated by `k-means++` initialization and running multiple `n_init` restarts and keeping the best.
- Assumes **spherical/convex clusters** — fails badly on elongated, nested, or irregularly shaped clusters (see the `make_moons` demo in `K_Means_Complete.ipynb`, Section 6 of the notebook).
- Sensitive to **outliers** — because centroids are means, a single far-away outlier can pull a centroid noticeably away from the "real" center of its group.
- Sensitive to **feature scaling** — a feature on a larger numeric scale will dominate the Euclidean distance calculation unless features are standardized first.

## 10. Why no classification/regression version

Clustering is inherently **unsupervised**: there is no known/true target `y` to fit against, so there is no "K-Means classifier" or "K-Means regressor" in the way there's a "Random Forest Classifier" and "Random Forest Regressor." K-Means only ever sees `X`.

That said, cluster assignments **can be reused** as an engineered feature for a downstream supervised model — e.g. compute `cluster_id = kmeans.predict(X)` and feed that categorical feature into a classifier or regressor. This is a common practical trick (turning unsupervised structure into a supervised feature), but it does not turn K-Means itself into a supervised algorithm — it still never knew about any target when it formed the clusters.

## 11. How it compares to related algorithms

### K-Means vs DBSCAN

| Aspect | K-Means | DBSCAN |
|---|---|---|
| Number of clusters | Must specify `k` upfront | Does **not** need a predefined cluster count — discovers it from density |
| Cluster shape | Assumes roughly spherical/convex clusters | Handles **arbitrary shapes** (crescents, nested rings, elongated blobs) |
| Outliers | Sensitive — outliers pull centroids off-center; every point is forced into some cluster | Naturally robust — points in low-density regions are labeled **noise**, not force-fit into a cluster |
| Speed / simplicity | Faster, simpler, easier to reason about and tune | Slower on large data (needs neighborhood queries), needs tuning `eps`/`min_samples` |
| Best when | Clusters really are compact and similarly sized/dense — K-Means is often *better* here purely because it's simpler and faster | Clusters are irregular shapes, very different densities, or the data has genuine noise/outliers to be excluded rather than clustered |

**When to pick which:** if you can reasonably guess how many groups exist and expect them to look like round-ish blobs (e.g. customer segments by spend & frequency), reach for K-Means first — it's cheap and interpretable. If your data has odd shapes, unknown cluster count, or meaningful outliers/noise that should NOT be forced into a cluster, use DBSCAN instead. See `../DBSCAN (Density-Based Clustering)/README.md` in this repo for the full DBSCAN deep dive (density reachability, `eps`, `min_samples`, core/border/noise points, etc.) — this document only summarizes the comparison, not the full DBSCAN theory.

### Other alternatives (brief)

- **Hierarchical Clustering** — builds a full tree (dendrogram) of nested clusters rather than a single flat partition; useful when you want to inspect clustering at *every* possible `k` at once, without re-running the algorithm, at the cost of higher computational complexity on large datasets.
- **Gaussian Mixture Models (GMM)** — a probabilistic generalization of K-Means: instead of hard-assigning each point to exactly one nearest centroid, it models clusters as overlapping Gaussian distributions and gives each point a *probability* of belonging to each cluster (soft assignment), which also naturally supports elliptical (not just spherical) cluster shapes.

## 12. Evaluation metrics for clustering

Since clustering is unsupervised, there is **no ground-truth label** to compute accuracy, precision, or R² against. Instead, we use *internal* metrics that only look at the geometry of the clustering itself:

- **Elbow Method** — plot inertia (WCSS) against a range of `k` values. Inertia always decreases as `k` increases, but at some point the *rate* of decrease flattens sharply, forming a visual "elbow" — that bend is a good candidate for the true `k`.
- **Silhouette Score** — formula in Section 4.5, range **[-1, 1]**, higher is better. Unlike the Elbow method, it gives one clean number per `k` that can be directly compared and maximized, and it also works per-point (so you can spot which specific points are poorly clustered).

Both are demonstrated side-by-side in `K_Means_Complete.ipynb` (Section 4 of the notebook) on the same synthetic dataset, so you can see the elbow bend and the silhouette peak agree.

## 13. When to use / when NOT to use

**Use K-Means when:**
- You expect roughly round, similarly-sized/dense clusters.
- You have a rough idea of `k` (domain knowledge) or can afford to sweep `k` with Elbow/Silhouette.
- You need something fast, simple, and scalable to large `n`.
- You want directly interpretable "average member" centroids (e.g. customer segment profiles).

**Avoid K-Means when:**
- Clusters are non-convex / irregular shapes (crescents, rings, elongated arms) — use DBSCAN or spectral clustering instead.
- The data has many outliers that should be excluded rather than absorbed into a cluster — use DBSCAN.
- You have no idea how many clusters exist and can't afford to sweep `k` — DBSCAN or Hierarchical Clustering avoid pre-specifying a count.
- Features are categorical (not naturally numeric/distance-based) — K-Means needs a meaningful numeric distance metric; consider K-Modes/K-Prototypes instead.

## 14. Common pitfalls & practical tips

- **Always scale features first** (`StandardScaler` / `MinMaxScaler`) — K-Means is purely distance-based, so unscaled features silently dominate the clustering.
- **Always use `k-means++`** (scikit-learn's default `init`) with `n_init` > 1, rather than a single random initialization — this dramatically reduces the chance of reporting a bad local minimum.
- **Use the Elbow method AND the Silhouette score together**, not just one — the elbow bend can be ambiguous/subjective on real data, while silhouette gives a sharper, comparable number; agreement between the two is a much stronger signal than either alone.
- **K-Means can't handle categorical data directly** — one-hot encoding categorical features and feeding them straight into K-Means distorts the Euclidean distance; consider K-Modes/K-Prototypes or an embedding-based approach for mixed/categorical data.
- Remember that **inertia always decreases as `k` increases** — never pick `k` by minimizing inertia alone; that logic pushes you toward `k = n` (one cluster per point), which is meaningless.
- Watch out for **empty clusters** on pathological initializations (rare, but possible) — scikit-learn re-seeds empty clusters automatically, but it's worth knowing this edge case exists.

## 15. Notebook map

`K_Means_Complete.ipynb` sections:

| Notebook section | What it demonstrates |
|---|---|
| 1. Theory Recap | Supervised vs unsupervised, clustering as grouping, centroid concept, Lloyd's algorithm procedure, SSE/inertia objective, why cost monotonically decreases, choosing `k` via domain knowledge or Elbow |
| 2. Manual & Visual Intuition | Interactive slider widget computing a centroid by hand (sum/mean shown step by step); a button-driven step-through of Lloyd's algorithm on a small synthetic dataset showing assignment → SSE breakdown → centroid update → convergence |
| 3. Full scikit-learn Implementation | Iris dataset load, feature selection, `StandardScaler`, `KMeans(n_clusters=3, init='k-means++', max_iter=400)`, fitting, inspecting `labels_`, visualizing clusters with centroids plotted, reading `inertia_`, and confirming Inertia ≡ SSE |
| 4. Choosing k — Elbow + Silhouette | Sweeping `k` on `make_blobs` data, plotting inertia-vs-k and mean-silhouette-vs-k side by side, comparing where each suggests the right `k` |
| 5. Random-Init Sensitivity | Running `init='random', n_init=1` across multiple `random_state` values to show different inertia/cluster assignments (local-minima problem), then showing `init='k-means++', n_init=10` stabilizes the result |
| 6. Where K-Means Fails | `make_moons` non-spherical dataset — K-Means visibly cuts across both crescents; pointer to DBSCAN for arbitrary-shape clustering |

Original, unmodified source notebooks are preserved in `archive/` (`K_Means_Visualizer.ipynb`, `K_Means_Clustering_using_Scikit_Learn (1).ipynb`) as a backup snapshot. The theory PDF `K Means Clustering.pdf` remains in this folder unchanged.

## 16. Exam-ready summary

K-Means is an **unsupervised, centroid-based clustering** algorithm (Lloyd's algorithm, 1957/1982) that partitions `n` points into `k` groups by repeating two steps — **assign** each point to its nearest centroid (`argmin_k ||x-μ_k||²`), then **update** each centroid to the mean of its assigned points (`μ_k = mean(cluster_k)`) — until the centroids stop moving; the quantity it minimizes is **WCSS/inertia/SSE** `= Σ_k Σ_{x∈k} ||x-μ_k||²`, which is guaranteed to never increase during the loop but can still get stuck in a **local minimum** depending on the random initial centroids (fixed in practice with `k-means++` init and multiple `n_init` restarts). Since there's no ground-truth label, `k` is chosen and the clustering is judged using **internal metrics**: the **Elbow method** (inertia vs k, look for the bend) and the **Silhouette score** (`s(i)=(b(i)-a(i))/max(a(i),b(i))`, range -1 to 1, higher better) — used together for reliability. K-Means assumes roughly spherical, similarly-sized clusters and is sensitive to feature scale and outliers, which is exactly why **DBSCAN** (arbitrary shapes, naturally labels outliers as noise, no need to pre-specify `k`) exists as a complementary alternative — pick K-Means for speed/simplicity on compact round clusters, DBSCAN for irregular shapes and noisy data. মূল কথা: K-Means মানেই হলো "কেন্দ্রবিন্দুর দিকে হাঁটা আর কেন্দ্রবিন্দুকে গড়ে সরানো" — বারবার — যতক্ষণ না সবকিছু স্থির হয়ে যায়।
