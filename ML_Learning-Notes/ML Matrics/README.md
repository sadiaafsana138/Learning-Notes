# ML Metrics Cheatsheet

A beginner-friendly guide to picking the right model type and reading the numbers that tell you whether your model is good.

Companion file: `ml_metrics_cheatsheet.docx`

## What's inside

The cheatsheet walks through, in order:

1. **What kind of problem you have** — regression vs classification vs clustering
2. **Regression metrics** — MAE, MSE, RMSE, R²
3. **Classification metrics** — accuracy, precision, recall, F1, ROC-AUC (and the confusion matrix they come from)
4. **Why accuracy alone can lie**
5. **A quick decision guide** — your situation → which metric to watch
6. **Overfitting warning signs**

## Quick reference

### Which problem type?

| Type | You predict | Example |
|------|-------------|---------|
| Regression | A number | House price, temperature |
| Classification | A category | Spam / not spam, cat / dog |
| Clustering | Groups in unlabeled data | Customer segments |

If the answer is a **quantity**, it's regression. If it's a **bucket/label**, it's classification.

### Regression — is my model good?

| Metric | Want | Notes |
|--------|------|-------|
| MAE | Low | Average error, in original units |
| RMSE | Low | Like MAE but punishes big errors more |
| R² | High | 1.0 = perfect, 0 = no better than the average, negative = worse |

There is **no universal "good" RMSE** — compare it to the scale of what you're predicting.

### Classification — is my model good?

| Metric | Want | Use when |
|--------|------|----------|
| Accuracy | High | Classes are balanced |
| Precision | High | A false alarm is costly |
| Recall | High | Missing a real case is costly |
| F1 | High | You want one balanced score |
| ROC-AUC | High | Overall separation (0.5 = random) |

All of these are scored **0 → 1**, higher is better.

## Three things beginners get wrong

- **Accuracy can lie.** On imbalanced data (e.g. 99% not-spam), a lazy model looks 99% accurate but catches nothing. Check precision, recall, F1, ROC-AUC instead.
- **A metric only counts on unseen (test) data.** Great on training but bad on test = overfitting. Bad on both = underfitting.
- **Numbers need a baseline.** "RMSE = 5" or "R² = 0.7" means nothing until you compare it to the scale of the target and to a simple baseline.

## How to use it

Open `ml_metrics_cheatsheet.docx`, find your situation in Section 5 (the decision guide), then read the matching metric's "How to read them" notes. Keep it next to you while evaluating models.
