# Decision Trees — Classification & Regression

## 1. Title & One-Line Hook

*One yes/no question at a time, splitting the data into purer and purer groups, until each group is small and clean enough to just blurt out an answer. Decision Trees are what a flowchart looks like after it has eaten a dataset.*

---

## 2. What Is It & Where Does It Sit

A **Decision Tree** is a **supervised**, **non-parametric** learning algorithm that handles **both**:

- **Classification** — `DecisionTreeClassifier` — predicts a category (species, spam/not-spam, approved/denied).
- **Regression** — `DecisionTreeRegressor` — predicts a number (price, disease progression, temperature).

It sits in this repo's `Supervised/` family next to Logistic Regression, KNN, SVM, Linear Regression, and Random Forest. It is arguably the most important model in that family for a different reason than accuracy: it is the **building block**. Random Forest, Extra Trees, Gradient Boosting, XGBoost, LightGBM, and CatBoost are all, underneath, *many* Decision Trees combined. Understanding one tree deeply is a prerequisite for understanding all of them.

**বাংলায় বললে:** সহজ কথায়, Decision Tree হলো একগুচ্ছ yes/no প্রশ্নের সিরিজ — প্রতিটা প্রশ্নে ডেটা দুই ভাগে ভাগ হতে থাকে, আর শেষে একটা এমন ছোট গ্রুপে (leaf) গিয়ে থামে, যেখানে উত্তরটা almost নিশ্চিত হয়ে যায়। কোনো সমীকরণ নেই, কোনো দূরত্ব মাপা নেই — শুধু threshold-based প্রশ্ন।

---

## 3. Where It Comes From & Why It Was Invented

Decision trees as a *decision-analysis* tool predate machine learning — decision theorists used tree diagrams by hand to lay out choices, chance events, and expected payoffs. Machine learning's contribution was to make a computer **learn the splits from data** instead of a human drawing the tree from expert judgment. Three algorithms matter historically:

| Algorithm | Year / Author | Split criterion | Notes |
|---|---|---|---|
| **ID3** | Quinlan, 1986 | Information gain (entropy) | Categorical features only, multi-way splits, no pruning |
| **C4.5** | Quinlan, 1993 | Gain ratio (entropy normalized by split size) | Adds numeric features, pruning, handles missing values |
| **CART** | Breiman et al., 1984 | Gini (classification) / variance (regression) | **What scikit-learn implements** — always binary splits, does both classification *and* regression |

**Why it was invented / why it caught on:**

1. **Mimics human if-else reasoning.** A doctor's triage flowchart, a loan officer's approval checklist, a customer-support decision tree — these already existed as human artifacts. CART/ID3 simply asked: can a machine *learn* the same kind of flowchart directly from historical data instead of a human writing the rules?
2. **No linear assumption required.** Logistic Regression assumes a linear decision boundary (in the log-odds); Linear Regression assumes a linear relationship. Real-world data is full of thresholds, interactions and non-linear cutoffs ("approve the loan only if income > X **and** existing debt < Y") that a straight line simply cannot express. Recursive partitioning carves the feature space into axis-aligned boxes, which can approximate *any* shape given enough splits.
3. **One model for mixed data types.** A single tree can split on a numeric column (`age <= 30`) and a categorical column (encoded as an integer) side by side, with no separate treatment needed for either.
4. **The core idea — recursive partitioning:** repeatedly pick the single best yes/no question that splits the *current* subset of data into the two purest possible groups, then repeat that same procedure independently on each of the two resulting groups, and keep going until a stopping rule fires. This is a **greedy, top-down, divide-and-conquer** algorithm — simple enough to hand-execute on a small dataset (see Section 5 below), yet powerful enough to be the base learner of nearly every top Kaggle-winning tabular model today.

---

## 4. Intuition

Think of the children's game **20 Questions**: "Is it an animal?" → yes → "Does it have wings?" → no → "Is it bigger than a cat?" → ... Every answer eliminates roughly half of the remaining possibilities, and after a handful of well-chosen questions you can name the exact object. A Decision Tree does precisely this over a dataset instead of your imagination: every internal node is one yes/no question about **one feature**, every branch is an answer, and every leaf is the final guess.

```
                    [ petal length <= 2.45 ? ]        <- root node: the first, most informative question
                       /                \
                    yes                  no
                     /                     \
               ( setosa )         [ petal width <= 1.65 ? ]   <- decision node: a follow-up question
                leaf node             /              \
                                   yes                no
                                    /                  \
                           ( versicolor )         ( virginica )
                               leaf                    leaf
```

The tree always asks the question that separates the data best *right now* — it never plans two questions ahead. That greediness is both its biggest strength (fast, simple, tractable) and its biggest weakness (Section 10).

**বাংলায় বললে:** এটা ঠিক '২০ প্রশ্নের খেলা'র মতো — প্রতিটা প্রশ্নে ডেটাসেট দুই ভাগে ভাগ হয়ে যায়, আর সবচেয়ে ভালো প্রশ্নটাই (যেটা সবচেয়ে বেশি বিভ্রান্তি/অনিশ্চয়তা কমায়) সবার আগে করা হয়। Root node মানে প্রথম ও সবচেয়ে গুরুত্বপূর্ণ প্রশ্ন, আর leaf মানে যেখানে গিয়ে খেলা শেষ — এখানেই উত্তর পাওয়া যায়।

---

## 5. Math & Formula(s)

### 5.1 Impurity measures (classification)

**Entropy** — disorder of a node, measured in bits:

$$ H(S) = -\sum_{i=1}^{k} p_i \log_2 p_i $$

where $p_i$ is the proportion of class $i$ in node $S$. A pure node ($p=1$ for one class) has $H=0$; a binary 50/50 node has $H=1$ (maximum disorder for two classes).

**Gini impurity** — the probability of misclassifying a randomly drawn sample if it were labelled by randomly drawing a class from the node's own distribution:

$$ Gini(S) = 1 - \sum_{i=1}^{k} p_i^{2} $$

Pure node → $Gini=0$; binary 50/50 → $Gini=0.5$. Gini is scikit-learn's default `criterion` because it needs no logarithm (cheaper to compute); in practice it almost never disagrees with entropy about which split to take — same shape, different scale.

**Information Gain** — how much impurity a candidate split removes. Parent impurity minus the *weighted* impurity of the resulting children (weighted, because leaving 90% of the data still messy in one child is not much of a win):

$$ IG = I(\text{parent}) - \left( \frac{n_{\text{left}}}{n} I(\text{left}) + \frac{n_{\text{right}}}{n} I(\text{right}) \right) $$

Here $I$ is either $H$ (entropy) or $Gini$ — same formula, different impurity function underneath. At every node, the tree evaluates this for every feature and every candidate threshold, and keeps the split with the highest $IG$.

### 5.2 Impurity measure (regression) — variance / MSE reduction

A regression leaf predicts the **mean** of the training samples inside it, so impurity is the mean squared error of the node against its own mean (equivalently, the variance of the node):

$$ MSE(S) = \frac{1}{n}\sum_{i=1}^{n} \left( y_i - \bar{y}_S \right)^2 $$

and the split score — the regression mirror of information gain — is:

$$ \Delta_{\text{variance}} = MSE(\text{parent}) - \left( \frac{n_{\text{left}}}{n} MSE(\text{left}) + \frac{n_{\text{right}}}{n} MSE(\text{right}) \right) $$

This is exactly what `criterion='squared_error'` (the scikit-learn default for `DecisionTreeRegressor`) computes at every candidate split.

### 5.3 Worked example #1 — Classification: Gini and Entropy by hand

A tiny 8-row table: will a customer **buy** a product, given whether they are a **Student** and their **Income** level?

| # | Income | Student | Buys |
|---|--------|---------|------|
| 1 | High | Yes | Yes |
| 2 | High | Yes | Yes |
| 3 | Low  | Yes | Yes |
| 4 | Low  | Yes | Yes |
| 5 | High | No  | No |
| 6 | High | No  | No |
| 7 | Low  | No  | No |
| 8 | Low  | No  | Yes |

**Step 1 — impurity of the parent (all 8 rows).** `Buys`: 5 Yes, 3 No → $p_{yes}=5/8=0.625$, $p_{no}=3/8=0.375$.

$$ H(\text{parent}) = -(0.625\log_2 0.625 + 0.375\log_2 0.375) = -(0.625 \times (-0.678) + 0.375 \times (-1.415)) = 0.4238 + 0.5306 = 0.9544 $$

$$ Gini(\text{parent}) = 1-(0.625^2+0.375^2) = 1-(0.3906+0.1406) = 0.4688 $$

**Step 2 — candidate split on `Student`.** Two children, 4 rows each:

- `Student = Yes` (rows 1-4): 4 Yes, 0 No → **pure**. $H=0$, $Gini=0$.
- `Student = No` (rows 5-8): 1 Yes, 3 No → $p_{yes}=0.25$, $p_{no}=0.75$.

$$ H(\text{Student=No}) = -(0.25\log_2 0.25 + 0.75\log_2 0.75) = -(0.25\times(-2) + 0.75\times(-0.415)) = 0.5+0.3113 = 0.8113 $$

$$ Gini(\text{Student=No}) = 1-(0.25^2+0.75^2) = 1-(0.0625+0.5625)=0.375 $$

**Step 3 — weighted children impurity and gain** (each child holds $4/8=0.5$ of the data):

$$ \text{weighted } H = 0.5\times 0 + 0.5\times 0.8113 = 0.4057 \qquad IG_{\text{entropy}} = 0.9544-0.4057 = \mathbf{0.5488} $$

$$ \text{weighted } Gini = 0.5\times 0 + 0.5\times 0.375 = 0.1875 \qquad IG_{\text{gini}} = 0.4688-0.1875 = \mathbf{0.2813} $$

**For contrast — the losing split, on `Income`:** `Income=High` (rows 1,2,5,6) is 2 Yes/2 No ($H=1.0$); `Income=Low` (rows 3,4,7,8) is 3 Yes/1 No ($H=0.8113$). Weighted entropy $=0.5\times1.0+0.5\times0.8113=0.9057$, so $IG_{\text{entropy}}(\text{Income}) = 0.9544-0.9057=\mathbf{0.0487}$ — more than **10x smaller** than `Student`'s gain. The tree picks `Student` as the root split, exactly because $0.5488 \gg 0.0487$. This Income/Student/Buys table is a standalone hand-worked example for this README; `Decision_Tree_Complete.ipynb`, Part 0, Section 0.7 reproduces the identical entropy/Gini/Information-Gain mechanics in code on a different toy dataset (the classic 14-row "PlayTennis" Outlook/Humidity/Wind table) — the numbers won't match row-for-row, but the formulas and the split-picking logic are the same.

### 5.4 Worked example #2 — Regression: variance reduction by hand

A tiny 8-row table: predicted **exam score** from **hours studied**.

| Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|
| Score | 35 | 40 | 50 | 55 | 65 | 70 | 85 | 90 |

**Step 1 — MSE of the parent (all 8 rows).** Mean $=\frac{35+40+50+55+65+70+85+90}{8}=\frac{490}{8}=61.25$.

$$ MSE(\text{parent}) = \frac{1}{8}\left[(-26.25)^2+(-21.25)^2+(-11.25)^2+(-6.25)^2+3.75^2+8.75^2+23.75^2+28.75^2\right] = \frac{2787.5}{8} = \mathbf{348.4375} $$

**Step 2 — candidate split: `Hours <= 4`.**

- Left (`Hours` 1-4): scores $35,40,50,55$, mean $=45$. $MSE_{\text{left}}=\frac{100+25+25+100}{4}=\frac{250}{4}=62.5$
- Right (`Hours` 5-8): scores $65,70,85,90$, mean $=77.5$. $MSE_{\text{right}}=\frac{156.25+56.25+56.25+156.25}{4}=\frac{425}{4}=106.25$

**Step 3 — weighted children MSE and variance reduction** (4/8 = 0.5 each side):

$$ \text{weighted } MSE = 0.5\times62.5+0.5\times106.25 = 84.375 $$

$$ \Delta_{\text{variance}} = 348.4375 - 84.375 = \mathbf{264.0625} $$

A large positive number means this is a genuinely useful split — the tree keeps children whose scores are much more tightly clustered around their own mean than the whole parent was. This exact table and arithmetic is reproduced in code in `Decision_Tree_Complete.ipynb`, Part 0, Section 0.9 — the printed numbers match to the decimal.

---

## 6. Algorithm Steps (Pseudocode)

```text
function BUILD_TREE(D, depth):
    if STOPPING_CONDITION(D, depth):
        return MAKE_LEAF(D)      # classification: majority class in D
                                  # regression:     mean of targets in D

    best_score = -infinity
    best_split = None

    for feature in D.features:
        for threshold in CANDIDATE_THRESHOLDS(D, feature):
            D_left, D_right = SPLIT(D, feature, threshold)
            score = IMPURITY(D) - WEIGHTED_IMPURITY(D_left, D_right)   # info gain / variance reduction
            if score > best_score:
                best_score, best_split = score, (feature, threshold, D_left, D_right)

    if best_split is None or best_score <= min_impurity_decrease:
        return MAKE_LEAF(D)       # no split helps enough -> stop here

    feature, threshold, D_left, D_right = best_split
    left_child  = BUILD_TREE(D_left,  depth + 1)
    right_child = BUILD_TREE(D_right, depth + 1)
    return MAKE_INTERNAL_NODE(feature, threshold, left_child, right_child)
```

**Stopping criteria** (any one of these fires → make a leaf instead of splitting further):

- The node is already **pure** (impurity `= 0`).
- `max_depth` has been reached.
- The node holds fewer samples than `min_samples_split`.
- Splitting would create a child with fewer samples than `min_samples_leaf`.
- No candidate split improves impurity by at least `min_impurity_decrease`.
- The tree has already reached its `max_leaf_nodes` budget.

This is **greedy** — the best split *right now*, not the best split considering the whole future tree. Finding the provably-optimal decision tree is NP-complete, so every practical library (including scikit-learn's CART implementation) takes this greedy shortcut. Post-pruning (`ccp_alpha`, Section 7) is the usual way to partially compensate: grow the full greedy tree first, then cut back branches that don't earn their keep.

---

## 7. Key Hyperparameters

| Hyperparameter | Controls | Too low | Too high / unrestricted |
|---|---|---|---|
| `max_depth` | Maximum number of questions from root to any leaf — the primary overfitting control | Underfits: a shallow tree (e.g. depth 1, a "stump") can't separate more than a couple of groups | Overfits: default `None` grows until every leaf is pure, memorising individual training rows |
| `min_samples_split` | Minimum samples a node must hold before it's even allowed to split | Low value (e.g. `2`, the default) lets the tree split on tiny, unreliable groups | Very high value collapses the tree to just a few big, underfit leaves |
| `min_samples_leaf` | Minimum samples every resulting leaf must keep, or the split is rejected | Low value (default `1`) allows single-sample leaves — pure memorisation | Too high smooths away genuinely small-but-real subgroups, underfitting |
| `criterion` | Impurity function used to score a split — `'gini'`/`'entropy'`/`'log_loss'` (classification) or `'squared_error'`/`'friedman_mse'`/`'absolute_error'`/`'poisson'` (regression) | N/A — not a size knob | N/A — rarely changes the fitted tree's shape much; `'absolute_error'` is more robust to outliers but much slower to fit |
| `ccp_alpha` | Cost-complexity **post**-pruning penalty: $R_\alpha(T) = R(T) + \alpha \lvert T \rvert$, where $R(T)$ is the tree's error and $\lvert T \rvert$ its leaf count | `0.0` (default) = no post-pruning at all, full unrestricted tree | Very large `alpha` prunes the tree back to just the root — a single leaf that predicts one constant for everyone |
| `max_features` | How many features are considered at each split (`None`, an int, a float, `'sqrt'`, `'log2'`) | Restricting features weakens a *single* tree (worse splits are picked more often) | `None` (all features) gives the strongest single tree, but is also what makes every tree in a forest look alike (see Section 12) |

Other notable knobs covered in the notebook's hyperparameter deep-dive (Part 3): `splitter` (`'best'` vs `'random'`), `min_weight_fraction_leaf`, `max_leaf_nodes`, `min_impurity_decrease`, `class_weight` (essential for imbalanced classification — see Section 14), `random_state`, and `monotonic_cst` (scikit-learn 1.4+).

**Rule of thumb:** `max_depth`, `min_samples_leaf`/`min_samples_split`, `max_leaf_nodes`, `min_impurity_decrease` and `ccp_alpha` are all, mechanically, **the same knob wearing different clothes** — "how big is this tree allowed to get?" Tune one or two of them properly (ideally `ccp_alpha`, since scikit-learn computes its own candidate list from the data via `cost_complexity_pruning_path`) rather than all six badly.

---

## 8. Assumptions

Decision Trees are famously *non-parametric* — no equation form, no distributional assumption about the features, no linearity requirement. But "few assumptions" is not "no assumptions":

- **Axis-aligned splits are good enough.** Every split is `feature <= threshold` — a cut perpendicular to one axis. A true diagonal boundary ($x_1 = x_2$) has to be approximated with a staircase of many small axis-aligned splits, never drawn exactly.
- **Locally constant predictions are acceptable.** Every leaf predicts one constant (a class or a mean) for every sample that lands there — the model assumes the target doesn't vary meaningfully *within* a leaf.
- **Enough samples per leaf to estimate that constant reliably.** A leaf with 1-2 samples is not really "learning" a rule, it's memorising specific rows — this is exactly what `min_samples_leaf` guards against.
- **i.i.d. data**, like virtually all supervised learners — the training and test data are assumed to come from the same underlying distribution.

---

## 9. Advantages

| Advantage | Mechanism — *why* it's true |
|---|---|
| **Fully interpretable** | The fitted model is a literal flowchart (`plot_tree`, `export_text`) — every prediction is a short, readable path of threshold comparisons, not a black-box weight vector. |
| **No feature scaling needed** | A split only ever asks "is this value above or below a threshold?" — a monotonic transform of a feature's scale doesn't change which samples fall on which side, so `StandardScaler` changes nothing about the fitted tree. |
| **Handles mixed data types** | Numeric columns are split by threshold; encoded categorical columns are split the same way — no separate machinery needed for either. |
| **Captures non-linearity and interactions automatically** | Recursive partitioning can carve out any axis-aligned region, and because later splits happen *within* the subset created by earlier splits, the tree naturally encodes feature interactions ("if income is high **and** existing debt is low") without anyone specifying an interaction term by hand. |
| **Free feature importance** | `feature_importances_` falls out of the fitted tree — the total impurity reduction each feature contributed, summed across every split, at no extra computational or modelling cost. |
| **Fast at prediction time** | A prediction is a short walk down the tree (at most `max_depth` comparisons) — no distance computation against stored data (contrast with KNN) and no need to touch every feature. |

---

## 10. Disadvantages

| Disadvantage | Mechanism — *why* it's true |
|---|---|
| **High variance / overfits easily** | An unrestricted tree keeps splitting until every leaf is pure, which it can *always* achieve by isolating individual rows — that is memorisation, not generalisation. This is the single biggest weakness of a lone tree (see Section 12). |
| **Unstable** | Because every split is chosen greedily from the *current* data, changing even a handful of training rows can change which split looks "best" near the root — and a different root split cascades into a completely different tree below it. |
| **Greedy splits aren't globally optimal** | The algorithm always takes the best split *right now*; it never looks ahead to check whether a slightly worse split now would enable a much better one two levels down. Finding the truly optimal tree is NP-complete, so every practical implementation accepts this trade-off. |
| **Biased toward high-cardinality features** | A feature with many distinct values offers many more candidate thresholds to try, which mechanically raises its *chance* of stumbling on a split with high apparent information gain — even when that split doesn't generalise. (This is exactly why C4.5 introduced *gain ratio* instead of raw information gain.) |
| **Poor extrapolation in regression** | A regression leaf predicts a single constant (the training mean of the samples inside it) — a `DecisionTreeRegressor`'s output is a step function. For any input outside the range the training data covered, the tree still returns whichever boundary leaf's mean was closest — it can never extrapolate a trend beyond the data it saw. |

---

## 11. Classification vs Regression Version

| Aspect | Classification (`DecisionTreeClassifier`) | Regression (`DecisionTreeRegressor`) |
|---|---|---|
| Splitting criterion | Gini impurity (default) or entropy / log-loss | MSE / `'squared_error'` (default), or `'friedman_mse'`, `'absolute_error'`, `'poisson'` |
| Leaf prediction | **Majority class** of the training samples in that leaf | **Mean** of the training targets in that leaf |
| Split score formula | Information gain: $H(\text{parent}) - \sum \frac{n_c}{n}H(\text{child})$ | Variance reduction: $MSE(\text{parent}) - \sum \frac{n_c}{n}MSE(\text{child})$ |
| Typical evaluation metrics | Accuracy, precision, recall, F1, confusion matrix | MSE, RMSE, MAE, R² |
| `class_weight` support | Yes — crucial for imbalanced classes | Not applicable |
| Output shape | A discrete label | A step function (piecewise-constant surface) |
| Notebook section | `Decision_Tree_Complete.ipynb`, **Part 1** (Iris dataset) | `Decision_Tree_Complete.ipynb`, **Part 2** (Diabetes dataset) |

---

## 12. How It Compares to Related Algorithms

**The #1 weakness of a single Decision Tree is high variance / overfitting** (Section 10) — it is unstable, and it will memorise its training set if left unrestricted. This is not a minor footnote; it is *the* reason an entire family of algorithms exists.

**Random Forest** (`../Random Forest (Regression & Classification)/`) was built specifically to fix this. It trains **many** decision trees, each on a bootstrap-resampled subset of the rows (**bagging**) and each considering only a random subset of features at every split (**feature sub-sampling**, `max_features='sqrt'` by default for classification), then **averages** their predictions (majority vote for classification, mean for regression). Two mechanisms make this work:

1. **Bagging reduces variance** by averaging over many models trained on slightly different data — errors that are specific to one tree's training sample tend to cancel out across the ensemble.
2. **Feature sub-sampling decorrelates the trees.** If every tree in the forest were allowed to see every feature, they would tend to pick the same strong splits and end up highly correlated — averaging correlated models barely reduces variance at all. Forcing each split to consider only a random subset of features means different trees latch onto different features, so their individual errors are less alike, and averaging genuinely cancels out more of the noise.

Each individual tree inside a Random Forest is deliberately made *weaker* than the best possible single tree (that's exactly what `max_features='sqrt'` costs — see the seed-averaged experiment in this repo's own `Decision_Tree_Complete.ipynb`, Part 3, Section 7). The forest is stronger anyway, because it trades a little bias for a large reduction in variance. **See the Random Forest README for the full before/after comparison** — single-tree accuracy/R² vs. forest accuracy/R², and how the variance drops as more trees are added.

**vs. Logistic / Linear Regression:** these fit one global linear boundary (a straight line/hyperplane in the case of Logistic Regression's decision boundary, or a straight-line fit for Linear Regression). A Decision Tree instead partitions the space into **axis-aligned boxes**, each with its own constant prediction — no linearity assumption at all, but also no smooth boundary; the tree's boundary is a staircase, and a linear model's diagonal boundary needs many small tree-splits to approximate.

**vs. KNN:** KNN is a **lazy, local, non-parametric** model — `.fit()` does nothing but store the data, and every prediction re-scans the stored points to find the nearest neighbours at query time. A Decision Tree is **eager and global** — `.fit()` does real, upfront work to learn a structure (`model.tree_`) once, and prediction afterward is just a fast walk down that fixed structure, touching no stored training data at all. KNN also *requires* feature scaling (it compares distances); a tree does not (Section 9).

---

## 13. When to Use / When Not to Use

**Use a Decision Tree when:**

- The model **must be explainable** to a human (regulator, doctor, auditor) — "denied because income < X and existing debt > Y" is something a tree can produce directly and nothing else in this repo can match as literally.
- The data mixes numeric and categorical features and you don't want to build a scaling/encoding pipeline just to get a first baseline.
- You suspect strong **non-linear relationships or feature interactions** that a linear model would miss.
- You want a fast, zero-tuning **baseline** before reaching for Random Forest / Gradient Boosting.
- You specifically need the **tree structure itself** — e.g. as the base learner inside an ensemble.

**Avoid (or be very careful with) a single Decision Tree when:**

- **Accuracy/robustness matters more than explainability** and you can afford an ensemble — Random Forest or Gradient Boosting will almost always beat a single tuned tree.
- The **training set is small or noisy** — a single tree's instability (Section 10) means it can look wildly different after adding or removing a handful of rows.
- You need to **extrapolate in regression** beyond the range of the training data — a tree's step-function output cannot do this at all.
- The true decision boundary is **smooth and diagonal** rather than a set of thresholds — a linear/logistic model or SVM with the right kernel may fit that shape with far fewer parameters.

---

## 14. Common Pitfalls & Practical Tips

- **Always compare train vs. test score before trusting a tree.** A train score near `1.0` (accuracy or R²) alongside a much lower test score is the single most reliable overfitting signal — check it every time, on every dataset (this repo's own notebook, Part 1 Section 8 and Part 2 Section 2.8, shows exactly this gap opening up as `max_depth` grows).
- **Prune before deploying.** Don't ship the default, unrestricted tree. Either pre-prune (`max_depth`, `min_samples_leaf`) or post-prune with `ccp_alpha` — the latter is usually preferable because scikit-learn computes the *exact* candidate alphas from your data via `cost_complexity_pruning_path`, rather than you guessing a grid.
- **Don't forget `class_weight` on imbalanced classification.** A tree can score a deceptively high accuracy while quietly ignoring the minority class entirely — `class_weight='balanced'` forces each class to contribute equally to the impurity calculation regardless of how rare it is. Always check per-class recall, not just overall accuracy, on imbalanced data.
- **Set `random_state`.** Splits that tie on impurity are broken randomly by default — without a fixed seed, re-running the same cell can silently produce a different tree.
- **Benchmark anything involving randomness over multiple seeds**, not one run. `max_features`, `splitter='random'`, and `random_state` itself all make a single fit's score vary — a couple of percentage points of spread across seeds is normal and does not mean your first result was wrong (or right).
- **Treat impurity-based `feature_importances_` with a little suspicion.** It's known to inflate the apparent importance of high-cardinality features (Section 10) — `sklearn.inspection.permutation_importance` is the more trustworthy alternative when the ranking itself matters for a real decision.
- **Encode your categoricals yourself.** Unlike some other CART implementations, scikit-learn's trees do not accept raw strings — categorical columns need to be integer/one-hot encoded before fitting.

---

## 15. Notebook Map

`Decision_Tree_Complete.ipynb` (main notebook) — `archive/` holds the two original source notebooks, unchanged, as a backup.

| Section | What it demonstrates |
|---|---|
| Part 0 — The Theory Behind the Tree | Anatomy/terminology, how a split is chosen, entropy, Gini, information gain (with live code), variance/MSE reduction (with live code), ID3 vs C4.5 vs CART, regression trees, overfitting & pruning, advantages/disadvantages |
| Part 1 — Classification (Iris dataset) | Data exploration, train/test split, `DecisionTreeClassifier` fit, accuracy/precision/recall/F1/confusion matrix, `plot_tree`/`export_text`, feature importance, `GridSearchCV`, `max_depth` overfitting curve |
| Part 2 — Regression (Diabetes dataset) | Data exploration, train/test split, `DecisionTreeRegressor` fit, MSE/RMSE/MAE/R², predicted-vs-actual plot, tree visualization, feature importance, `max_depth` overfitting curve (R² version) |
| Part 3 — Real-World Uses & Hyperparameter Tuning | Where trees are used in practice, parameters vs. hyperparameters, every one of the 13 `DecisionTreeClassifier` hyperparameters individually demonstrated (including the full `ccp_alpha` cost-complexity pruning sweep and the imbalanced-data `class_weight` experiment), a priority-ordered quick-reference table |

---

## 16. One-Paragraph Exam-Ready Summary

A Decision Tree is a supervised, non-parametric model that learns a flowchart of threshold questions via **greedy, top-down recursive binary splitting**: at every node it picks the feature and threshold that most reduces impurity — **entropy** ($H=-\sum p_i\log_2 p_i$) or **Gini** ($1-\sum p_i^2$) for classification, **MSE/variance** for regression — scored as **information gain / variance reduction** (parent impurity minus the weighted impurity of the children), and it keeps splitting until a stopping rule fires (pure node, `max_depth`, `min_samples_leaf`, etc.). A classification leaf predicts the majority class; a regression leaf predicts the mean — that's the *only* structural difference between `DecisionTreeClassifier` and `DecisionTreeRegressor`. No scaling is ever needed (thresholds don't care about units), mixed data types are handled natively, and the fitted model can literally be read like a diagram — কিন্তু এই সুবিধার বিনিময়ে বড় মূল্য আছে: unrestricted রাখলে tree পুরো training set মুখস্থ করে ফেলে (overfitting), আর ডেটার একটু পরিবর্তনেও পুরো tree বদলে যেতে পারে (instability/high variance) — এটাই ঠিক সেই সমস্যা যেটা Random Forest বহু decorrelated tree-কে bagging + feature-subsampling দিয়ে গড় করে সমাধান করে। Prune it (`ccp_alpha` or `max_depth`/`min_samples_leaf`), always check train-vs-test score, set `class_weight` on imbalanced data, and remember: a single tree is a great *explainable baseline*, but an *ensemble of trees* is almost always the stronger production model.
