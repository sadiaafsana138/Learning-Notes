# DBSCAN — Density-Based Spatial Clustering of Applications with Noise

Find clusters of *any shape* by looking at local crowd density, and get outlier detection for free — no need to tell it how many clusters to look for.

## 1. What is it & where does it sit

- **Category:** Unsupervised Learning → **Clustering** (density-based).
- It is **not classification** (no predefined class labels exist to predict) and **not regression** (no continuous target to predict). DBSCAN only looks at the *feature space* `X` and groups rows based on how densely packed they are — there is no `y` anywhere in the algorithm.
- Full name: **D**ensity-**B**ased **S**patial **C**lustering of **A**pplications with **N**oise. Every word matters:
  - **Density-Based** — clusters are defined by density, not distance-to-center.
  - **Spatial Clustering** — it groups points in space.
  - **...of Applications with Noise** — it explicitly models "noise" (outlier) points as a first-class output, not an error case.

বাংলায় বললে: DBSCAN কোনো লেবেল ছাড়াই ডেটার মধ্যে **কে কোথায় ভিড় (density) করে আছে** তা দেখে নিজে থেকে গ্রুপ (cluster) বানায়, আর যারা একা/ফাঁকা জায়গায় আছে তাদের **noise/outlier** বলে চিহ্নিত করে দেয়।

## 2. Where it comes from & why it was invented

DBSCAN was introduced by **Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu** in their 1996 KDD paper *"A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise."*

It was invented directly to fix three core limitations of **K-Means** (the dominant clustering algorithm at the time):

| K-Means limitation | DBSCAN's fix |
|---|---|
| You must **specify the number of clusters `k`** in advance | DBSCAN discovers the number of clusters automatically from density structure — you only tune `eps` and `min_samples` |
| K-Means is **centroid-based**, so it is heavily **sensitive to outliers** (a single far-away point drags a centroid toward it) | DBSCAN is density-based: sparse/outlier points simply get **no cluster at all** (labeled noise) instead of distorting a cluster |
| K-Means **only works well with (roughly) spherical/convex clusters** because it minimizes distance-to-centroid | DBSCAN has no shape assumption — it can trace **arbitrarily shaped** (elongated, crescent, ring-shaped) clusters, because it only cares about local density connectivity, not distance to one center point |

বাংলায়: K-Means-কে আগে থেকেই বলে দিতে হয় কত ক্লাস্টার বানাবে, আর গোলাকার (spherical) শেপ ছাড়া অন্য শেপের ক্লাস্টার বুঝতে পারে না, আর একটা আউটলায়ার-ই পুরো centroid নষ্ট করে দিতে পারে। DBSCAN এই তিনটা সমস্যাই সমাধান করে — density দেখে cluster খুঁজে বের করে, শেপ যেকোনো হতে পারে, আর আউটলায়ার নিজে থেকেই আলাদা হয়ে যায়।

## 3. Intuition

Think of each data point as a person standing in a city:

- If you (a point) have **enough people standing close to you** (within radius `eps`, at least `min_samples` people including yourself) — you are in a **crowded neighborhood**. You are a **core point** — a genuine, certified member of "downtown."
- If you don't have enough people around *you*, but you are standing just at the edge of someone else's crowded neighborhood (within `eps` of a core point) — you're standing at the **edge of the crowd**. You are a **border point** — you belong to the cluster, but you didn't bring the crowd yourself.
- If you're standing alone, far from any crowd, and no core point's neighborhood reaches you — you're **isolated**. You are **noise**.

A cluster, then, is not "points near one center" — it's **a whole connected crowded region**: you can walk from core point to core point (each one within `eps` of the previous), like walking through a busy street from one crowded block to the next, and the whole connected chain (plus everyone standing at its edges) is one cluster.

বাংলায়: DBSCAN-এর ধারণাটা হলো — যদি তোমার আশেপাশে যথেষ্ট কাছের মানুষ (neighbor) থাকে, তুমি "ভিড়ের মূল অংশ" (**core point**)। যদি তুমি নিজে ভিড় না বানাতে পারো কিন্তু কোনো ভিড়ের পাশে দাঁড়িয়ে থাকো, তুমি "ভিড়ের কিনারা" (**border point**)। আর যদি তুমি একা, কোনো ভিড়ের ধারেকাছেও না থাকো, তুমি "noise" — বিচ্ছিন্ন বিন্দু।

## 4. Math & Formulas

### 4.1 Core definitions

Let `D` be the dataset, `dist(p, q)` a distance function (usually Euclidean), and fix two hyperparameters: `eps` (ε, a radius) and `minPts` (a minimum count).

**ε-neighborhood of a point p:**

```
N_eps(p) = { q ∈ D : dist(p, q) ≤ eps }
```

> **Convention (matches scikit-learn's implementation):** `N_eps(p)` includes `p` itself, since `dist(p, p) = 0 ≤ eps`. So when we say "a point needs `minPts` neighbors," that count **includes the point itself**.

**Core point:** `p` is a core point if its ε-neighborhood is dense enough:

```
p is CORE  ⟺  |N_eps(p)| ≥ minPts
```

**Directly density-reachable:** `q` is directly density-reachable from `p` if `q ∈ N_eps(p)` **and** `p` is a core point. (Note: this relation is *not symmetric* — reachability flows outward from core points.)

**Density-reachable:** `q` is density-reachable from `p` if there is a chain of points `p = p_0, p_1, ..., p_n = q` such that each `p_{i+1}` is directly density-reachable from `p_i`.

**Density-connected:** two points `p` and `q` are density-connected if there exists some point `o` such that **both** `p` and `q` are density-reachable from `o`. (This relation *is* symmetric — it's what lets border points on opposite edges of a cluster count as "the same cluster.")

**Cluster:** a maximal, non-empty set of points that are all mutually density-connected. Formally (Ester et al., 1996): a cluster `C` w.r.t. `eps` and `minPts` is a non-empty subset of `D` such that:
1. **Maximality:** ∀ p, q: if p ∈ C and q is density-reachable from p, then q ∈ C.
2. **Connectivity:** ∀ p, q ∈ C: p is density-connected to q.

**Border point:** a point that is *not* core (`|N_eps(p)| < minPts`) but lies in `N_eps(c)` for some core point `c`. It belongs to `c`'s cluster but cannot extend it further.

**Noise point:** any point that is not density-reachable from *any* core point — it belongs to no cluster. In scikit-learn's output this is the label `-1`.

### 4.2 Full worked-by-hand numeric example

Consider 10 points in 2D:

| Point | x | y |
|---|---|---|
| P1 | 1 | 2 |
| P2 | 2 | 2 |
| P3 | 2 | 3 |
| P4 | 3 | 2 |
| P5 | 3 | 3 |
| P6 | 4.2 | 3.6 |
| P7 | 8 | 8 |
| P8 | 8 | 9 |
| P9 | 9 | 8 |
| P10 | 25 | 25 |

Choose **`eps = 1.5`**, **`minPts = 3`** (counting the point itself, per the convention above), Euclidean distance.

**Step 1 — compute the relevant pairwise distances** (using `dist = sqrt(Δx² + Δy²)`):

*Inside the "left group" (P1–P5):*

| Pair | Δx,Δy | distance |
|---|---|---|
| P1–P2 | 1,0 | 1.000 |
| P1–P3 | 1,1 | 1.414 |
| P1–P4 | 2,0 | 2.000 |
| P1–P5 | 2,1 | 2.236 |
| P2–P3 | 0,1 | 1.000 |
| P2–P4 | 1,0 | 1.000 |
| P2–P5 | 1,1 | 1.414 |
| P3–P4 | 1,1 | 1.414 |
| P3–P5 | 1,0 | 1.000 |
| P4–P5 | 0,1 | 1.000 |

*P6 (candidate border point) to its closest neighbors:*

| Pair | Δx,Δy | distance |
|---|---|---|
| P5–P6 | 1.2,0.6 | 1.342 |
| P4–P6 | 1.2,1.6 | 2.000 |
| P3–P6 | 2.2,0.6 | 2.280 |

*Inside the "right group" (P7–P9):*

| Pair | Δx,Δy | distance |
|---|---|---|
| P7–P8 | 0,1 | 1.000 |
| P7–P9 | 1,0 | 1.000 |
| P8–P9 | 1,1 | 1.414 |

*Cross-group distances (to confirm the two groups never touch, and P10 is isolated):*

| Pair | distance |
|---|---|
| P6–P7 | 5.813 |
| P9–P10 | 23.345 |

**Step 2 — build each point's ε-neighborhood (distance ≤ 1.5, including itself) and classify:**

| Point | N_eps(p) (within 1.5) | \|N_eps(p)\| | ≥ minPts=3? | Classification |
|---|---|---|---|---|
| P1 | {P1, P2, P3} | 3 | Yes | **Core** |
| P2 | {P2, P1, P3, P4, P5} | 5 | Yes | **Core** |
| P3 | {P3, P1, P2, P4, P5} | 5 | Yes | **Core** |
| P4 | {P4, P2, P3, P5} | 4 | Yes | **Core** |
| P5 | {P5, P2, P3, P4, P6} | 5 | Yes | **Core** |
| P6 | {P6, P5} | 2 | No | Not core, but P6 ∈ N_eps(P5) and P5 is core → **Border** (of P5's cluster) |
| P7 | {P7, P8, P9} | 3 | Yes | **Core** |
| P8 | {P8, P7, P9} | 3 | Yes | **Core** |
| P9 | {P9, P7, P8} | 3 | Yes | **Core** |
| P10 | {P10} | 1 | No | Not core, and not in any core point's neighborhood → **Noise (-1)** |

**Step 3 — trace clusters via density-connectivity:**

- P1, P2, P3, P4, P5 are all core points and each is directly density-reachable from at least one other (e.g. P1 ∈ N_eps(P2), P2 is core ⇒ P1 is directly density-reachable from P2; similarly P4, P5 chain through P2/P3). They are mutually density-connected ⇒ **Cluster A = {P1, P2, P3, P4, P5}**.
- P6 is directly density-reachable from core point P5 (P6 ∈ N_eps(P5)) ⇒ P6 joins **Cluster A**. Final: **Cluster A = {P1, P2, P3, P4, P5, P6}**.
- P7, P8, P9 are mutually core and density-connected, and far (distance 5.8+) from Cluster A ⇒ separate **Cluster B = {P7, P8, P9}**.
- P10 is density-reachable from nobody ⇒ **Noise = {P10}**.

**Final result:** 2 clusters + 1 noise point — exactly the kind of output you'll see reproduced (with a bigger, messier dataset) in the accompanying notebook.

## 5. Algorithm steps (pseudocode)

```
DBSCAN(D, eps, minPts):
    label every point in D as UNVISITED
    cluster_id = 0

    for each point p in D:
        if p is already labeled (not UNVISITED):
            continue                       # already assigned to a cluster or noise

        neighbors = N_eps(p)                # find all points within eps of p

        if |neighbors| < minPts:
            label p as NOISE                # tentative — may be re-labeled BORDER later
            continue

        # p is a CORE point -> start a new cluster
        cluster_id += 1
        label p as cluster_id
        seed_set = neighbors \ {p}           # queue of points to expand from

        while seed_set is not empty:
            q = seed_set.pop()
            if q is labeled NOISE:
                label q as cluster_id         # noise -> becomes a border point of this cluster
            if q is already labeled (cluster_id or otherwise):
                continue
            label q as cluster_id

            q_neighbors = N_eps(q)
            if |q_neighbors| >= minPts:       # q is itself a core point -> expand further
                seed_set += q_neighbors \ {q}
    return labels
```

Key idea: **only core points can *expand* a cluster.** Border points get absorbed but don't recruit new members. A point first marked NOISE is not final — it only means "not reachable *yet*"; it can be relabeled the moment some later core point's search reaches it.

## 6. Key hyperparameters

| Hyperparameter | What it controls | Too small | Too large |
|---|---|---|---|
| `eps` (ε) | Radius of the neighborhood used to decide "closeness" | Almost nothing looks dense enough → most points become **noise**, or you get many tiny fragmented clusters | Everything looks reachable from everything → distinct clusters **merge into one giant blob** |
| `min_samples` / `minPts` | How many neighbors (density threshold) are needed to call a point "core" | Very easy to become core → algorithm becomes **overly sensitive**, treats small noisy clumps as real clusters | Very hard to become core → **few or no clusters form**, most points end up as noise/border |
| `metric` | The distance function used to measure "closeness" (default `'euclidean'`) | Wrong metric for the data geometry (e.g. Euclidean on cyclical/angular or high-cardinality categorical features) gives meaningless neighborhoods regardless of `eps` | — (not a magnitude knob, but choosing e.g. `'manhattan'`, `'cosine'`, or a custom metric changes what "close" means entirely) |

Practical starting points:
- Rule of thumb for `min_samples`: **≥ (number of features) + 1**; commonly `2 × n_features` as a starting guess, and larger for noisier data.
- Pick `eps` using the **k-distance / elbow method** (Section 15 below and demonstrated in the notebook) rather than guessing.

## 7. Assumptions

- Clusters are **regions of higher density separated by regions of lower density** — this is the *only* structural assumption DBSCAN makes about your data.
- It assumes a **single global density threshold** (one `eps`, one `minPts`) is meaningful across the *entire* dataset.
- Consequently, DBSCAN **struggles when clusters have very different densities** — one `eps` that correctly captures a sparse cluster will merge a dense cluster into a blob (or vice versa: one that fits the dense cluster will shred the sparse cluster into noise). This is DBSCAN's most well-known weakness (partially addressed by extensions like OPTICS / HDBSCAN, which use a range of densities instead of one fixed `eps`).

## 8. Advantages

- **No need to specify the number of clusters upfront** — it's discovered from the data via density.
- **Finds arbitrarily shaped clusters** — not restricted to spherical/convex shapes like K-Means.
- **Naturally identifies and labels outliers/noise** (`-1`) as part of the normal algorithm output, not as a separate step.
- **Robust to outliers skewing cluster shape** — since DBSCAN never averages points into a centroid, one far-away point cannot drag a whole cluster's "center" the way it does in K-Means.

## 9. Disadvantages

- **Sensitive to the choice of `eps` / `min_samples`** — there may be no single good value if different regions of the data have different densities.
- **Struggles with clusters of very different densities** (see Assumptions above).
- **Degrades in high-dimensional data** — in high dimensions, distances between points tend to concentrate (the curse of dimensionality), so "neighborhoods" stop being meaningful and `eps` becomes hard to tune.
- **Not great when clusters touch or overlap** — where density doesn't clearly dip between two groups, DBSCAN will merge them into one cluster (it has no notion of "two overlapping bells," unlike, say, a Gaussian Mixture Model).

## 10. Why no classification/regression version

Clustering is **inherently unsupervised**: DBSCAN never sees a target `y`. There is no "correct answer" to check predictions against during training, because there *is* no training in the supervised sense — DBSCAN just scans local density in `X`. That means:

- There is no "DBSCAN Classifier" that predicts a known class, and no "DBSCAN Regressor" that predicts a continuous value — the entire premise of classification/regression (learning a mapping `X → y` from labeled examples) doesn't apply.
- What DBSCAN *can* do is feed a downstream supervised model: its output — the cluster id (or `-1` for noise) assigned to each row — can be used as an **engineered feature** (e.g., "which customer-behavior cluster does this transaction fall into") in a later classification or regression pipeline. DBSCAN discovers structure; it doesn't predict a known target.

বাংলায়: DBSCAN কোনো label দেখেই না, তাই এর "classification version" বা "regression version" বলে কিছু নেই — এটা শুধু ডেটার গঠন (structure) খুঁজে বের করে। তবে এর আউটপুট (cluster id) পরবর্তীতে অন্য কোনো supervised মডেলের feature হিসেবে ব্যবহার করা যায়।

## 11. How it compares to related algorithms

### DBSCAN vs. K-Means (see `../K-Means (Centroid-Based Clustering)/README.md`)

| Aspect | K-Means | DBSCAN |
|---|---|---|
| Cluster model | **Centroid-based** — each cluster is defined by a center point; membership = nearest centroid | **Density-based** — a cluster is a connected region of high density |
| Cluster shape assumption | Roughly **spherical / convex**, similar size | **Arbitrary shape** — crescents, rings, elongated blobs, anything |
| Number of clusters | **Must specify `k`** in advance | **Not required** — emerges from `eps`/`min_samples` |
| Outlier handling | **Sensitive** — every point (including outliers) is forced into the nearest cluster, dragging centroids | **Robust** — outliers are explicitly labeled noise (`-1`) and excluded from clusters |
| Speed / scalability | **Fast**, scales well to large `n` and high dimensions (roughly `O(n·k·iterations)`) | Slower for large `n` with naive neighbor search (`O(n²)` without spatial indexing; `O(n log n)` with a KD-tree/Ball-tree for low dimensions) |
| Determinism | Depends on centroid initialization (mitigated by `k-means++` / multiple restarts) | Deterministic given `eps`/`min_samples`/point order (mostly — border points assigned to whichever core reaches them first can vary in edge cases) |
| Works well when... | Clusters really are roughly spherical, similarly sized, and you have a good estimate of `k` | Clusters have irregular shapes, contain noise, and you don't know `k` in advance |

**When to pick which:**
- Pick **K-Means** when you have a good idea of the number of clusters, clusters are expected to be roughly round/similarly sized, speed on large data matters, and there are few extreme outliers.
- Pick **DBSCAN** when clusters could be irregularly shaped, you don't know `k`, your data has real noise/outliers you want to *identify* (not force into a group), and dataset size is manageable for neighbor search (or you can use an indexed `metric` for speed).

### DBSCAN vs. other density-based methods (brief)
- **OPTICS** — generalizes DBSCAN by producing a "reachability plot" across a *range* of `eps` values instead of one fixed value, helping with the varying-density weakness.
- **HDBSCAN** — a hierarchical extension that automatically adapts to varying density and removes the need to hand-pick a single `eps`.
- **Gaussian Mixture Models (GMM)** — a *soft*, probabilistic clustering method that can model overlapping elliptical clusters (something DBSCAN can't), but requires specifying the number of components and assumes a Gaussian shape.

## 12. Evaluation metrics for clustering

Unlike classification/regression metrics (accuracy, RMSE, etc.), clustering metrics generally **don't require ground-truth labels** — they judge how good the clustering is using only the data and the discovered labels themselves.

**Silhouette Score** (most common):

For a point `i`, let:
- `a(i)` = mean distance from `i` to all other points **in its own cluster** (cohesion)
- `b(i)` = mean distance from `i` to all points in the **nearest other cluster** (separation)

```
s(i) = ( b(i) − a(i) ) / max( a(i), b(i) )
```

- `s(i)` ranges from **−1 to +1**.
- Close to **+1**: point is well matched to its own cluster and far from others (good).
- Close to **0**: point sits on/near the boundary between two clusters.
- Close to **−1**: point is likely in the wrong cluster.
- The overall **silhouette score** is the mean of `s(i)` over all points. For DBSCAN, **exclude noise points** (label `-1`) before computing it — they aren't a real cluster.

**Other options (mentioned briefly):**
- **Davies-Bouldin Index** — ratio of within-cluster scatter to between-cluster separation; **lower is better** (0 = best possible).
- **Calinski-Harabasz Index** (a.k.a. Variance Ratio Criterion) — ratio of between-cluster to within-cluster dispersion; **higher is better**.

> **Important caveat:** these metrics reward compact, convex, well-separated clusters — they don't know the *true* shape of your data. It is entirely possible (and demonstrated in the notebook) for K-Means to get a *higher* silhouette score than DBSCAN on the moons dataset, even though DBSCAN found the geometrically correct clusters and K-Means didn't. Always pair any metric with a visual check when clusters might be non-convex.

## 13. When to use / when NOT to use

**Use DBSCAN when:**
- You don't know the number of clusters in advance.
- Clusters may be irregularly shaped (not spherical).
- Your data has real outliers/noise you want explicitly identified, not forced into a group.
- Example real-world use case: **fraud/anomaly detection** — e.g. plotting customers by spending behavior (income vs. max transaction amount); the dense "normal behavior" region becomes a cluster, and sparse, isolated points naturally surface as anomalies/potential fraud, with zero need to pre-label any transaction as fraudulent.

**Avoid / be cautious with DBSCAN when:**
- Clusters have **very different densities** in the same dataset.
- Data is **high-dimensional** (curse of dimensionality hurts distance-based neighborhoods).
- Clusters genuinely **touch/overlap** with no density dip between them.
- You need **speed on very large datasets** without spatial indexing support for your metric.
- You actually know `k` and expect roughly spherical clusters — K-Means will likely be simpler and faster.

## 14. Common pitfalls & practical tips

- **Always scale your features first** (e.g. `StandardScaler`). `eps` is a raw distance threshold — if one feature has a much larger numeric range than another, it will dominate the distance calculation and `eps` will not mean the same thing along every axis.
- **Don't guess `eps`** — use the **k-distance graph / elbow method**: for a fixed `k = min_samples`, compute each point's distance to its k-th nearest neighbor, sort descending, plot, and pick `eps` at the "elbow" where the curve bends sharply from steep (sparse/noise points) to flat (dense cluster points). This is demonstrated step-by-step in the notebook.
- **Remember noise points (`-1`) need separate handling downstream** — they are not "cluster number -1", they are "no cluster." Don't feed them into per-cluster statistics, don't compute a "centroid of noise," and exclude them before computing silhouette score. If you need every point assigned somewhere (e.g., for a business report), decide explicitly how to handle noise (drop it, flag it, or assign it to the nearest cluster as a separate post-processing step) rather than silently including it in cluster math.
- Try a few `(eps, min_samples)` combinations and look at both the **cluster count** and the **noise count** — a good setting usually gives a stable, sensible number of clusters across a small neighborhood of parameter values (not wildly different at `eps=0.29` vs `eps=0.31`).

## 15. Notebook map

`DBSCAN_using_Scikit_Learn.ipynb`:

| Section in notebook | What it demonstrates |
|---|---|
| 1. Data Generation | Builds the classic **moons** dataset (non-globular, arbitrary-shaped clusters) and injects extra scattered **noise points** |
| 2. Feature Scaling | `StandardScaler` applied before any distance-based clustering |
| 3. k-distance Graph (Elbow Method) | Principled way to choose `eps` — plots sorted k-th-nearest-neighbor distances and identifies the elbow |
| 4. DBSCAN Clustering | Fits `DBSCAN(eps, min_samples)`, prints cluster/noise counts, and **visualizes clusters and noise (label -1) in distinct colors/markers** |
| 5. K-Means on the Same Data | Fits `KMeans(n_clusters=2)` on the identical scaled data, for a fair comparison |
| 6. Side-by-Side Comparison | Two subplots, same data/scale: DBSCAN correctly recovering the crescents + noise vs. K-Means cutting across them |
| 7. Silhouette Score | Computes silhouette score for DBSCAN (noise excluded) and K-Means (all points), with a caveat about what the metric can and can't tell you |
| 8. Key Takeaways | Recap, including why DBSCAN has no classification/regression counterpart |

## 16. One-paragraph exam-ready summary

**DBSCAN** হলো একটা **unsupervised, density-based clustering** অ্যালগরিদম যা কোনো label ছাড়াই ডেটাকে গ্রুপ করে — এটা classification বা regression কোনোটাই নয়, কারণ কোনো target `y` নেই। এটা দুইটা hyperparameter ব্যবহার করে: **`eps`** (কতটুকু এলাকার মধ্যে দুটি পয়েন্ট neighbor বলে গণ্য হবে) আর **`minPts`** (একটা পয়েন্টকে "core point" বলার জন্য কমপক্ষে কতজন neighbor লাগবে, `|N_eps(p)| ≥ minPts`)। যে পয়েন্টের যথেষ্ট neighbor আছে সে **core**, যে core-এর পাশে আছে কিন্তু নিজে dense না সে **border**, আর যে কোনো core-এর reach-এই পড়ে না সে **noise (-1)**। একটা cluster হলো density-connected পয়েন্টদের একটা maximal সেট — core points থেকে chain ধরে ধরে cluster expand হয়, border points শেষে যুক্त হয় কিন্তু নিজে expand করতে পারে না। K-Means-এর তুলনায় DBSCAN-এর সুবিধা: `k` আগে থেকে বলতে হয় না, arbitrary shape ধরতে পারে (K-Means পারে না, e.g. moons/crescent shape), আর outlier-এ robust (K-Means-এ outlier centroid নষ্ট করে দেয়)। অসুবিধা: বিভিন্ন density-র cluster থাকলে একটা single `eps` সবার জন্য কাজ করে না, high-dimensional data-য় distance-ভিত্তিক neighborhood অর্থহীন হয়ে যায় (curse of dimensionality), এবং touching/overlapping cluster আলাদা করতে পারে না। Evaluation-এর জন্য ground truth লাগে না — **Silhouette score** (`s(i) = (b(i)-a(i)) / max(a(i),b(i))`, range −1 থেকে +1) ব্যবহার করা হয়, noise point বাদ দিয়ে হিসাব করতে হয়; তবে এটা convex cluster-কে পছন্দ করে বলে সবসময় ভিজ্যুয়াল চেক-এর সাথে মিলিয়ে দেখা উচিত। Practical tip: distance-based algorithm বলে **feature scaling সবসময় আগে করতে হবে**, আর `eps` অনুমান না করে **k-distance elbow plot** দিয়ে বেছে নেওয়া উচিত।
