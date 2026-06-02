# Train vs Test Preprocessing — What to Apply Where

A reference for which preprocessing steps get applied to the test set and which don't. The distinction is intentional and different for each stage — getting it wrong causes data leakage or inflated scores.

> **The rule:** transformations are *fit on train, applied to test* — **except row-removal steps, which are train-only.**

---

## Quick reference

| Stage | Applied to test? | Why |
|-------|:---:|-----|
| **EDA** | ❌ No | EDA is just looking at data (plots/stats) — there's nothing to "apply." You never explore the test set, so it stays unseen. |
| **Feature engineering** | ✅ Yes | `add_features()` runs on both `X_train` and `X_test`. Same row-wise rules, so no leakage. |
| **Encoding** | ✅ Yes | `get_dummies` on both, then `X_test` is reindexed to train's columns. Test must have the same features. |
| **Scaling** | ✅ Yes *(special)* | Scaler is **fit on train only**, then `transform` is applied to test using train's numbers (`fit_transform(X_train)` / `transform(X_test)`). |
| **Outlier handling** | ❌ No *(train only)* | Outliers are removed/capped only in train, never in test. |

---

## The two important "why"s

### 1. Scaling — fit on train, apply to test

Learn the mean / min / max from the **training** data, then use those same numbers to scale the test set.

```python
X_train_scaled = scaler.fit_transform(X_train)   # learn params from train
X_test_scaled  = scaler.transform(X_test)         # reuse train's params
```

If you fit the scaler on test too, the test set's values leak into the transformation — that's **data leakage**.

### 2. Outlier handling — train only, by design

This surprises beginners, but it's correct:

- **You can't delete test rows.** You're supposed to predict *every* test sample. Dropping them hides the hard cases and fakes a better score.
- **The test set should look like real future data,** which will contain outliers. The model needs to be judged on that reality.
- So outliers are removed/capped only from **training** (to help the model learn cleaner patterns), never from test.

---

## Summary

- **FE, encoding, scaling** → yes, test gets them (scaling via train-fitted parameters).
- **EDA, outlier removal** → no — and that's deliberate, not a mistake.

The mental model: anything that *transforms a row in place* applies to both sets (using parameters learned from train). Anything that *removes or explores rows* is train-only.
