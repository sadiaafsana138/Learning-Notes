# Linear Regression — Learning Notes

A complete, from-scratch walkthrough of **Linear Regression**, the foundational
algorithm of supervised machine learning. This folder takes you from the raw math
(`y = wx + b`) all the way to the industry-standard `scikit-learn` implementation —
building every piece by hand first so the intuition is rock solid.

---

## 📓 Main Notebook

| File | What's inside |
|------|---------------|
| **`Linear_Regression_Complete.ipynb`** | The full lesson, fully executed with all plots and outputs baked in. |

> This single notebook is the merge of three earlier notebooks (Simple LR – first
> part, Simple LR, and Multiple LR). Everything is now in one place.

### Notebook contents

**Part 0 — Setup**
- Imports: NumPy, Matplotlib, Seaborn.

**Part 1 — Simple Linear Regression (one feature)**
- Model: `f(x) = w·x + b` where `w` = slope (weight), `b` = intercept (bias).
- Dataset: *Years of Experience → Salary*.
- Build a prediction function from scratch.
- Manually tune `w` and `b` to build intuition for how each one moves the line.
- **Cost function** (Mean Squared Error) — a single number for "how wrong" the line is.
- Visualize the convex, U-shaped cost curve.
- **Gradient Descent** from scratch — automatically find the best `w` and `b`.
- Final best-fit line, a new prediction, and the learning curve.

**Part 2 — Multiple Linear Regression (many features)**
- Model: `f(x) = w₁x₁ + w₂x₂ + … + wₙxₙ + b` (dot product).
- Dataset with 4 features: *Experience, Problem-Solving Skill, Interview Pause Time, GPA → Salary*.
- Vectorized prediction, cost, and gradient functions using NumPy.
- Train with gradient descent and predict for a new person.

**Part 3 — Scikit-Learn (the practical tool)**
- `LinearRegression` — exact closed-form solution.
- `SGDRegressor` — Stochastic Gradient Descent, for very large datasets.
- Both compared against the from-scratch results.

**Part 4 — Real-World Uses & Hyperparameter Tuning**
- Where linear regression shows up in practice (pricing, forecasting, scoring, yield prediction, etc.) and why it's still worth knowing.
- **Parameters vs. hyperparameters** — the key distinction, explained using the notebook's own variables (`w`, `b` vs. `alpha`, `max_iter`).
- **Learning rate (α)** — a from-scratch demo comparing too-small / good / too-large, with a log-scale convergence plot showing exactly why Part 1 used `alpha=0.01`.
- **Number of iterations**, and scikit-learn's hyperparameters — `SGDRegressor`'s `alpha` (regularization strength), `penalty`, `learning_rate` schedule, `eta0`, `max_iter`, `tol`; and `LinearRegression`'s `fit_intercept`, `positive`, `n_jobs`.
- A live demo of regularization strength shrinking the weight vector, plus a quick-reference table of which hyperparameter matters most and why.
- **A complete reference table** of every remaining hyperparameter on both estimators (`loss`, `l1_ratio`, `shuffle`, `epsilon`, `random_state`, `power_t`, `early_stopping`, `validation_fraction`, `n_iter_no_change`, `warm_start`, `average`, `copy_X`, etc.) — pulled directly from the installed scikit-learn's own signatures, so nothing is left out.

---

## 🧠 The Core Idea (in one minute)

Linear regression just **draws the best straight line through your data points**.

| Term | Plain English |
|------|---------------|
| `y = wx + b` | the line (same as `y = mx + c`) |
| **weight (w)** | the slope — how steep the line is |
| **bias (b)** | the intercept — where the line starts |
| **cost (MSE)** | how wrong the line is (lower = better) |
| **gradient descent** | automatically searching for the best line |
| **learning rate (α)** | how big a step we take while searching |
| **hyperparameter** | a setting *you* choose before training (like α) — as opposed to `w`/`b`, which the model learns on its own |
| **scikit-learn** | does all of the above for you in ~3 lines |

The from-scratch parts teach you *what happens under the hood*; scikit-learn is
*what you actually use* in practice.

---

## 🚀 How to Run

1. Make sure the required libraries are installed:
   ```bash
   pip install numpy matplotlib seaborn scikit-learn
   ```
2. Open the notebook in Jupyter / VS Code:
   ```bash
   jupyter notebook Linear_Regression_Complete.ipynb
   ```
3. Run the cells top to bottom (**Kernel → Restart & Run All**). The notebook is
   self-contained — data and functions are defined before they're used.

---

## 🔗 Useful Links & Resources

### Interactive Visualization
- **Linear Regression Visualizer** — play with the slope/intercept and watch the fit change:
  <https://www.interactive-ml.com/linear-regression.html>

### Suggested Podcasts & Documentaries
Inspiring watches that connect this math to the bigger AI picture:

- **Andrew Ng & Fei-Fei Li — Human-Centered AI** (Stanford Online). Fei-Fei Li was
  one of the pioneers of image-related AI; a great discussion on where AI is headed:
  <https://www.youtube.com/watch?v=UNhC6Ox0T0o>
- **Protein Folding, Explained** *(must watch)* — how ML cracked a decades-old
  biology problem: <https://www.youtube.com/watch?v=KpedmJdrTpY>
- **The Thinking Game** — full documentary from Google DeepMind (Tribeca Film
  Festival official selection): <https://www.youtube.com/watch?v=d95J8yzvjbQ>

---

## 📂 Additional Material (`PPTx/` folder)

Background slides and reading on the history and structure of AI/ML:

- `The Beginning of Artificial Intelligence.pptx`
- `Paper on Dartmouth AI Summer Project.pdf` — the 1956 proposal that coined the term "Artificial Intelligence".
- `Types of ML .pptx`
- `The ML PipeLine.pptx`

---

## ✅ Key Takeaways

1. **The model** fits `f(x) = w·x + b`; `w` sets the slope, `b` shifts the line.
2. **The cost** (MSE) measures error — it forms a convex bowl with one lowest point.
3. **Gradient descent** rolls down that bowl to find the best parameters automatically.
4. **Simple → Multiple** changes almost nothing: the weight becomes a vector, the rest is identical.
5. **Scikit-learn** is the real-world shortcut — understand the hood, then use the library.
6. **Hyperparameters** (like the learning rate) are chosen by *you*, not learned by the model — the learning rate is the one to get right first; regularization strength is the one to reach for if a model overfits.
