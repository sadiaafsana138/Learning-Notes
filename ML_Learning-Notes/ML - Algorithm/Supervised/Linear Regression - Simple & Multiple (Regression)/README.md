# Linear Regression (Simple & Multiple)

**Draw the best straight line through your data, and use it to predict a number.** সবচেয়ে পুরনো এবং সবচেয়ে গুরুত্বপূর্ণ ML অ্যালগরিদম — বাকি সব কিছু এখান থেকেই শুরু।

---

## 1. What is it & where does it sit

Linear Regression is a **supervised, REGRESSION-only** algorithm — it predicts a **continuous numeric value** (price, salary, temperature, disease progression score, etc.), never a class label.

```
Machine Learning
└── Supervised Learning
    ├── Regression (continuous target)   ← Linear Regression lives HERE
    │     Linear Regression, Ridge, Lasso, Decision Tree Regressor, ...
    └── Classification (discrete target)  ← NOT Linear Regression
          Logistic Regression, SVM, Decision Tree Classifier, ...
```

There is no meaningful "classification version" of plain linear regression — that job belongs to its sibling, **Logistic Regression** (`Supervised/Logistic Regression (Classification)`), which wraps this same linear formula in a sigmoid function to squeeze the output into a `[0, 1]` probability. More on that in §11.

**বাংলা ইন্টুইশন:** ধরো তোমার কাছে কিছু পয়েন্ট আছে একটা গ্রাফে (যেমন Experience বনাম Salary)। Linear Regression সেই পয়েন্টগুলোর মধ্য দিয়ে এমন একটা সরলরেখা টানে যেটা সবচেয়ে কম "ভুল" করে — মানে রেখা থেকে পয়েন্টগুলোর দূরত্ব সবচেয়ে কম হয়।

---

## 2. Where it comes from & why it was invented

Linear Regression is one of the **oldest formal statistical techniques**, predating "machine learning" as a field by roughly two centuries:

- **~1805** — Adrien-Marie **Legendre** published the **method of least squares** while studying orbital paths of comets.
- **~1809** — Carl Friedrich **Gauss** claimed to have used the same method since 1795 (for predicting the orbit of the asteroid Ceres) and gave it a rigorous probabilistic justification (linking it to the Normal/Gaussian distribution of errors — which is *why* the distribution is named after him, and why "normality of residuals" shows up as an assumption later in this document).
- **1886** — Francis **Galton** coined the term "**regression**" itself, while studying how the heights of children "regressed" toward the average height of the population, relative to their (taller or shorter) parents.

The core idea has stayed unchanged for over 200 years: **model a target as a weighted linear sum of inputs, and choose the weights that minimize total squared error.** This simple idea turned out to be the seed for a huge amount of modern ML:

- **Logistic Regression** = Linear Regression + a sigmoid squashing function (§11).
- **Ridge / Lasso / ElasticNet** = Linear Regression + a penalty term on the weights (§12).
- **A single neuron in a neural network** = Linear Regression (`w·x + b`) + a non-linear activation function. Stack thousands of these neurons in layers, and you get deep learning.

Understanding linear regression deeply is therefore not just "one more algorithm" — it's the literal mathematical foundation that a huge fraction of ML builds on.

---

## 3. Intuition

**One-line intuition:** find the straight line that minimizes the total squared "miss-distance" between the line and every data point.

Picture a scatter plot of points. For any candidate line, drop a vertical line from each data point down (or up) to the line you drew — that vertical gap is the point's **error** (residual). Square each gap (so positive and negative errors don't cancel, and big misses are punished disproportionately), add them all up. That sum is the **cost**. Linear regression is the search for the one line that makes that sum as small as possible.

**বাংলা:** কল্পনা করো, প্রতিটা ডেটা পয়েন্ট থেকে তোমার আঁকা রেখা পর্যন্ত একটা লম্ব রেখা টানলে। ওই লম্ব রেখার দৈর্ঘ্যটাই হলো "ভুল" (error)। সেই ভুলগুলোকে বর্গ (square) করে যোগ করলে একটা সংখ্যা পাওয়া যায় — এই সংখ্যাটাকেই যত সম্ভব ছোট করাই Linear Regression-এর কাজ।

---

## 4. Math & Formula(s)

### 4.1 Simple linear regression (one feature)

$$ \hat{y} = mx + c \qquad (\text{equivalently: } f(x) = wx + b) $$

- `m` (or `w`) — **slope**: how much `ŷ` changes per +1 unit of `x`.
- `c` (or `b`) — **intercept**: the value of `ŷ` when `x = 0`.

### 4.2 Cost function — Sum of Squared Residuals

$$ J(m, c) = \sum_{i=1}^{n} \left( y_i - \hat{y}_i \right)^2 = \sum_{i=1}^{n} \left( y_i - (mx_i + c) \right)^2 $$

This is the total squared "miss-distance" from §3. It is a **convex, bowl-shaped** function of `(m, c)` — one unique lowest point, no other local minima to get stuck in. (Some texts use $\frac{1}{2n}\sum(\cdot)^2$ instead — the constant is purely a convenience for calculus and doesn't change *where* the minimum is; the notebook uses this $\frac{1}{2m}$ form.)

### 4.3 Deriving the OLS estimates by calculus

To find the `m` and `c` that minimize `J`, set both partial derivatives to zero (calculus rule: at a minimum of a smooth convex function, the slope is zero in every direction).

**Step 1 — solve for `c`:**

$$ \frac{\partial J}{\partial c} = -2\sum_{i=1}^n \left( y_i - mx_i - c \right) = 0 $$

$$ \Rightarrow \sum y_i - m\sum x_i - nc = 0 \quad\Rightarrow\quad c = \bar{y} - m\bar{x} $$

where $\bar{x}, \bar{y}$ are the means of `x` and `y`.

**Step 2 — solve for `m`:**

$$ \frac{\partial J}{\partial m} = -2\sum_{i=1}^n x_i\left( y_i - mx_i - c \right) = 0 $$

$$ \Rightarrow \sum x_iy_i - m\sum x_i^2 - c\sum x_i = 0 $$

Substitute $c = \bar{y} - m\bar{x}$ from Step 1 and simplify:

$$ m = \frac{\sum x_iy_i - n\bar{x}\bar{y}}{\sum x_i^2 - n\bar{x}^2} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)} $$

**This is the closed-form OLS solution**: the slope is *covariance of x and y, divided by variance of x*; the intercept follows from the slope and the two means. No iteration, no guessing — one formula, exact answer.

### 4.4 A full worked-by-hand numeric example

Tiny dataset (5 points, 1 feature):

| $x_i$ | $y_i$ |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 4 |
| 5 | 5 |

**Step 1 — means:**
$$ \bar{x} = \frac{1+2+3+4+5}{5} = 3 \qquad \bar{y} = \frac{2+4+5+4+5}{5} = 4 $$

**Step 2 — deviations from the mean:**

| $x_i-\bar{x}$ | $y_i-\bar{y}$ | $(x_i-\bar{x})(y_i-\bar{y})$ | $(x_i-\bar{x})^2$ |
|---|---|---|---|
| −2 | −2 | 4 | 4 |
| −1 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 2 | 1 | 2 | 4 |
| **Σ = 0** | **Σ = 0** | **Σ = 6** | **Σ = 10** |

**Step 3 — slope and intercept:**
$$ m = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} = \frac{6}{10} = 0.6 $$
$$ c = \bar{y} - m\bar{x} = 4 - (0.6)(3) = 4 - 1.8 = 2.2 $$

**So the fitted line is:** $\hat{y} = 0.6x + 2.2$

**Step 4 — predictions and residuals:**

| $x_i$ | $y_i$ | $\hat{y}_i = 0.6x_i+2.2$ | Residual $y_i-\hat{y}_i$ | $(y_i-\hat{y}_i)^2$ | $(y_i-\bar{y})^2$ |
|---|---|---|---|---|---|
| 1 | 2 | 2.8 | −0.8 | 0.64 | 4 |
| 2 | 4 | 3.4 | 0.6 | 0.36 | 0 |
| 3 | 5 | 4.0 | 1.0 | 1.00 | 1 |
| 4 | 4 | 4.6 | −0.6 | 0.36 | 0 |
| 5 | 5 | 5.2 | −0.2 | 0.04 | 1 |
| | | | **Σ = SS_res = 2.4** | | **Σ = SS_tot = 6** |

**Step 5 — R² by hand:**
$$ R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{2.4}{6} = 1 - 0.4 = 0.6 $$

**Interpretation:** this line explains **60% of the variance** in `y`; the remaining 40% is unexplained (noise, or missing features). This exact worked example (same style, different numbers) is echoed in the notebook's Part 5 using a real dataset instead of 5 hand-picked points.

### 4.5 Multiple linear regression — matrix form

With `p` features and `n` samples, stack everything into matrices. Let `X` be `n × (p+1)` — a column of `1`s prepended for the intercept, plus the `p` feature columns — and $\boldsymbol\beta$ be the `(p+1)`-length vector `[b, w_1, w_2, ..., w_p]`:

$$ \hat{\mathbf{y}} = X\boldsymbol\beta $$

### 4.6 The Normal Equation (closed-form solution for multiple regression)

Minimizing $J(\boldsymbol\beta) = \| \mathbf{y} - X\boldsymbol\beta \|^2$ with matrix calculus (same zero-derivative idea as §4.3, generalized) gives:

$$ \boldsymbol\beta = (X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}\mathbf{y} $$

This is *exactly* the `np.linalg.inv(X.T @ X) @ X.T @ y` line used in the notebook's Part 7 — and it reproduces scikit-learn's `LinearRegression` output exactly, because that's essentially what scikit-learn computes internally (via a numerically stabler routine).

### 4.7 Gradient Descent — the iterative alternative

For very large datasets, inverting $X^{\mathsf{T}}X$ can be too expensive. Gradient descent finds the same minimum step by step:

$$ \boldsymbol\beta := \boldsymbol\beta - \alpha \cdot \frac{1}{n} X^{\mathsf{T}}(X\boldsymbol\beta - \mathbf{y}) $$

repeated until the cost stops shrinking meaningfully. `α` (**learning rate**) controls the step size. For simple regression this is the same pair of updates:

$$ w := w - \alpha\frac{\partial J}{\partial w}, \qquad b := b - \alpha\frac{\partial J}{\partial b} $$

### 4.8 R² and Adjusted R²

$$ R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum_i(y_i-\hat{y}_i)^2}{\sum_i(y_i-\bar{y})^2} $$

$$ R^2_{adj} = 1 - (1-R^2)\frac{n-1}{n-p-1} $$

where `n` = number of samples, `p` = number of features. Adjusted R² penalizes adding features that don't actually help (plain `R²` can only go up or stay flat as you add features, even useless random ones — Adjusted R² can go *down* if a feature isn't worth its complexity cost).

---

## 5. Algorithm steps (pseudocode)

**Option A — Closed-form (Normal Equation).** Exact, one-shot, best for small/medium data:

```
1. Collect data into X (n x p feature matrix) and y (n x 1 target vector)
2. Prepend a column of 1s to X  ->  X_design (n x (p+1))
3. Compute beta = inverse(X_design^T @ X_design) @ X_design^T @ y
4. beta[0] is the intercept b; beta[1:] are the feature weights w
5. Predict new points with:  y_hat = X_new_design @ beta
```

**Option B — Gradient Descent (iterative).** Scales to huge data; needed when `X^T X` is too big/expensive to invert:

```
1. Initialize w, b (commonly to zero)
2. Choose a learning rate alpha and number of iterations (or a stopping tolerance)
3. Repeat until convergence:
     a. Compute predictions:  y_hat = X @ w + b
     b. Compute the gradient of the cost w.r.t. w and b
     c. Update:  w := w - alpha * dJ/dw
                 b := b - alpha * dJ/db
4. Stop when the cost stops decreasing meaningfully (or after max_iter steps)
```

Both converge to the **same** answer for ordinary least squares, because the cost surface is convex with a single global minimum (verified directly in the notebook's Part 7).

---

## 6. Key hyperparameters / knobs

| Knob | Applies to | What it controls | Notes |
|---|---|---|---|
| **Learning rate (`α` / `eta0`)** | Gradient descent variant | Step size per update | Too small → slow crawl to the minimum. Too large → overshoots, cost diverges. Most important knob for GD-based training. |
| **Number of iterations (`max_iter`)** | Gradient descent variant | How many update steps to take | Too few → stops before converging (underfit-like). Too many → wasted compute (harmless for this convex problem, unlike neural nets). |
| **`fit_intercept`** | scikit-learn's `LinearRegression` (closed-form solver) | Whether to learn a bias `b` at all | Leave `True` unless you know the line must pass through the origin. |
| **`alpha`** (regularization strength) | Ridge / Lasso / ElasticNet — the natural extension of plain linear regression | How strongly to shrink the weight vector | `alpha=0` recovers plain linear regression; larger `alpha` → smaller, more stable, more biased coefficients. See §12. |

`LinearRegression`'s closed-form solver barely needs tuning — that's a *feature*, not a limitation: there's no search happening, so there's nothing to tune.

---

## 7. Assumptions (very important for this algorithm)

Linear regression's coefficients, confidence intervals, and p-values are only trustworthy if these hold:

| Assumption | What it means | How to check | If violated |
|---|---|---|---|
| **Linearity** | The true relationship between `X` and `y` is (approximately) a straight line / weighted sum | Plot residuals vs fitted values — should show no curve/pattern | Predictions systematically biased in some regions; consider polynomial features (§ notebook Part 9) or a non-linear model |
| **Independence of errors** | One data point's error doesn't predict another's (no autocorrelation) | **Durbin-Watson test** (~2 = independent; toward 0 or 4 = strong positive/negative autocorrelation) — common with time-series data | Standard errors become unreliable; use time-series-aware models instead |
| **Homoscedasticity** | Residual spread is roughly constant across all predicted values (no "funnel" shape) | Residuals vs fitted plot (notebook Part 6.3) | Coefficient estimates stay unbiased but their standard errors/p-values become unreliable; consider transforming `y` (e.g. log) or weighted least squares |
| **Normality of residuals** | Errors are approximately normally distributed | Histogram / Q-Q plot of residuals (notebook Part 6.3) | Confidence intervals and hypothesis tests on coefficients lose validity (point predictions are usually still fine) |
| **Little/no multicollinearity** | Features aren't strongly linearly correlated with each other | Correlation matrix + **Variance Inflation Factor (VIF)**; `VIF > 5–10` is concerning (notebook Part 8) | Coefficients become unstable, sign can flip, hard to interpret which feature "really" matters — even though overall predictions may still be fine |

**বাংলা:** এই assumption গুলো ভাঙলেও মডেল predict করতে থাকবে, কিন্তু coefficient-এর ব্যাখ্যা (interpretation) এবং confidence interval-এর উপর বিশ্বাস করা যাবে না।

---

## 8. Advantages

- **Simple and highly interpretable** — each coefficient has a direct, plain-English meaning ("+1 year experience → +5k salary").
- **Fast** — training is close to instant even on the closed-form solution.
- **Closed-form solution exists** — no iterative hyperparameter tuning required for small/medium datasets (§4.6).
- **Low data hunger** — works reasonably even with a handful of points.
- **A great baseline** — if a fancy model can't clearly beat plain linear regression, the extra complexity isn't earning its keep.
- **Statistically well-understood** — over 200 years of theory give confidence intervals and significance tests, not just point predictions.

## 9. Disadvantages

- **Only captures linear relationships** — unless you manually engineer polynomial/interaction terms (§ notebook Part 9), curved relationships are missed.
- **Sensitive to outliers** — squared-error loss amplifies large errors, so a single extreme point can drag the whole line toward it.
- **Sensitive to multicollinearity** — correlated features make individual coefficients unstable (§7).
- **Extrapolates poorly** — predictions far outside the range of training data can be wildly wrong; the line only "knows" the range it was fit on.

---

## 10. Why NOT used for classification

Plain linear regression's output $\hat y = w\cdot x + b$ is **unbounded** — it can be any real number (−∞ to +∞). That's a poor match for classification, where the target is a class label (like `0`/`1`):

- An unbounded number doesn't map cleanly to a **probability** (which must sit in `[0, 1]`) or to a discrete class.
- The **squared-error loss** used to fit linear regression is a poor fit for 0/1 targets — it penalizes confidently-correct predictions almost as much as wrong ones in some ranges, and doesn't produce the sharp probability-style boundary classification needs.

**The fix (bridge to the sibling folder):** wrap the same linear formula $z = w\cdot x + b$ in the **sigmoid function** $\sigma(z) = \frac{1}{1+e^{-z}}$, which squashes any real number into `(0, 1)`, interpretable as a probability. That's precisely **Logistic Regression** — see `Supervised/Logistic Regression (Classification)`. Same linear core, different output layer and loss function (log-loss instead of squared error).

---

## 11. How it compares to related algorithms

| vs. | Key difference |
|---|---|
| **Logistic Regression** | Sibling algorithm: same linear combination $w\cdot x+b$, but passed through a sigmoid and trained with log-loss to predict class **probabilities**, not continuous values. Regression vs. classification. |
| **Ridge Regression** | Adds an L2 penalty $\lambda\sum w_j^2$ to the cost function. Shrinks all coefficients smoothly toward (but not exactly to) zero — directly fixes the multicollinearity/instability problem from §7/§9. |
| **Lasso Regression** | Adds an L1 penalty $\lambda\sum |w_j|$. Can push some coefficients to *exactly* zero — effectively automatic feature selection, on top of the same shrinkage benefit as Ridge. |
| **ElasticNet** | Blends L1 and L2 penalties — gets Lasso's feature-selection behavior and Ridge's stability at the same time. |
| **Decision Tree / Random Forest Regressor** | Linear regression fits one **global** straight-line (or hyperplane) function; trees/forests fit **non-linear, piecewise** partitions of the feature space. Linear regression wins decisively when the true relationship really is (close to) linear — fewer parameters, better extrapolation, cleaner interpretation. It loses badly when the relationship is highly non-linear/interactive, where trees/forests adapt automatically without manual feature engineering. |

---

## 12. Evaluation metrics

| Metric | Formula | What it tells you |
|---|---|---|
| **MSE** (Mean Squared Error) | $\frac{1}{n}\sum(y_i-\hat y_i)^2$ | Average squared error; punishes large errors heavily; not in original units. |
| **RMSE** (Root MSE) | $\sqrt{MSE}$ | Same scale as `y` (e.g. "dollars," "kg") — the most intuitive "typical error size" metric. |
| **MAE** (Mean Absolute Error) | $\frac{1}{n}\sum\lvert y_i-\hat y_i\rvert$ | Average absolute error; more robust to outliers than MSE/RMSE (no squaring). |
| **R²** | $1 - \frac{SS_{res}}{SS_{tot}}$ | Fraction of variance in `y` explained by the model. `1` = perfect, `0` = no better than predicting the mean. |
| **Adjusted R²** | $1-(1-R^2)\frac{n-1}{n-p-1}$ | Like R², but penalizes useless extra features — the right metric when **comparing models with different numbers of features**. |

---

## 13. When to use / when NOT to use

**Use it when:**
- The target is continuous, and the relationship with the features is roughly linear (check with scatter plots / residual plots).
- You need **interpretability** — stakeholders need to know *why* the model predicts what it predicts.
- You want a fast, low-cost **baseline** before trying anything fancier.
- The dataset is small-to-medium, or features are limited and reasonably independent of each other.

**Avoid / be cautious when:**
- The true relationship is strongly non-linear and you're not willing to engineer polynomial/interaction features.
- Data has significant outliers that aren't handled/cleaned first.
- Features are heavily multicollinear and you need trustworthy individual coefficients (use Ridge, or drop/combine features).
- You need class probabilities/labels — use Logistic Regression (or another classifier) instead.

---

## 14. Common pitfalls & practical tips

- **Always plot residuals** (vs. fitted values) — this single plot catches non-linearity and heteroscedasticity at a glance (notebook Part 6.3).
- **Check VIF for multicollinearity** before trusting any individual coefficient's sign or size (notebook Part 8).
- **Don't trust R² alone** — when comparing models with different numbers of features, use **Adjusted R²**; plain R² can only go up as you add features, even useless ones.
- **Watch for outliers** — because the loss is squared error, a handful of extreme points can meaningfully tilt the whole line. Visualize the data first.
- **Scale your features** if you're using gradient descent (features on very different scales make some directions of the cost bowl much steeper than others, slowing convergence) or any regularized variant (Ridge/Lasso penalize raw coefficient size, so unscaled features get unfairly penalized more/less just because of their units).
- **Coefficient magnitude ≠ importance** unless features are standardized first — a coefficient of `5` on a feature ranging 0–1 is not comparable to a coefficient of `5` on a feature ranging 0–1000.

---

## 15. Notebook map

| Notebook section | What it demonstrates |
|---|---|
| Part 0 — Setup | Imports (NumPy, Matplotlib, Seaborn). |
| Part 1 — Simple Linear Regression (from scratch) | `f(x)=wx+b` prediction function, manual parameter tuning, MSE cost function, cost-curve visualization, gradient descent from scratch, best-fit line + learning curve on a 5-point toy dataset. |
| Part 2 — Multiple Linear Regression (from scratch) | Vectorized prediction/cost/gradient for `n` features, gradient descent on a 4-feature synthetic dataset, prediction for a new example. |
| Part 3 — Scikit-Learn | `LinearRegression` (closed-form) and `SGDRegressor` (stochastic gradient descent) fit on the same data, compared against the from-scratch results. |
| Part 4 — Real-world uses & hyperparameters | Where linear regression is used in practice; parameters vs. hyperparameters; learning-rate demo (too small/good/too large); iteration count; full hyperparameter reference tables for `SGDRegressor` and `LinearRegression`. |
| **Part 5 — Simple regression on a real dataset** | scikit-learn's Diabetes dataset, single feature (BMI), `LinearRegression` fit, coefficients, best-fit line vs. scatter, R² computed three ways (manual, `.score()`, `r2_score`), RMSE/MAE. |
| **Part 6 — Multiple regression on a real dataset** | All 10 Diabetes features, coefficient table, R² and Adjusted R² (with the multicollinearity caveat on comparing raw coefficient sizes), residuals-vs-fitted plot, residual distribution plot. |
| **Part 7 — Manual OLS via the Normal Equation** | `beta = inv(X.T @ X) @ X.T @ y` computed by hand with NumPy on a small example, verified to match scikit-learn's `LinearRegression` exactly. |
| **Part 8 — Multicollinearity check** | Correlation-matrix heatmap and hand-computed Variance Inflation Factor (VIF) for every feature in the Diabetes dataset. |
| **Part 9 — Polynomial regression extension** | Non-linear synthetic data fit with plain `LinearRegression` (underfits) vs. `PolynomialFeatures(degree=2)` + `LinearRegression` (fits the curve), R² comparison. |
| Summary & Key Takeaways | Dense recap of every part above. |

---

## 16. One-paragraph exam-ready summary

Linear Regression models a continuous target as a weighted linear sum of input features, $\hat y = w\cdot x + b$, and finds the weights that minimize the **sum of squared residuals** — either exactly via the **Normal Equation** $\beta=(X^TX)^{-1}X^Ty$ or iteratively via **Gradient Descent**; both reach the same unique minimum because the cost surface is convex. Model quality is judged with **MSE/RMSE/MAE** (error size) and **R²/Adjusted R²** (variance explained, with Adjusted R² correcting for feature count). It rests on the assumptions of linearity, independent/homoscedastic/normal errors, and low multicollinearity — always sanity-check these with residual plots and VIF (Part 6, 8 of the notebook) rather than trusting the coefficients blindly. It only works for **regression**, not classification (§10) — its unbounded, squared-error-fit output doesn't suit probabilities/labels, which is exactly the gap **Logistic Regression** fills using a sigmoid link function. It's fast, interpretable, and a mandatory baseline — but it only sees straight lines unless you engineer curved features (Part 9), and it's the mathematical ancestor of Logistic Regression, Ridge/Lasso, and even a single neuron in a neural network. **সংক্ষেপে:** Linear Regression হলো ডেটার মধ্য দিয়ে সবচেয়ে কম ভুল করা সরলরেখা টানার সবচেয়ে পুরনো, দ্রুত ও ব্যাখ্যাযোগ্য (interpretable) পদ্ধতি — এবং আধুনিক ML-এর অনেক অ্যালগরিদমের ভিত্তি।
