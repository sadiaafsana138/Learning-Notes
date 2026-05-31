# Time Series Forecasting — Beginner's Guide

A complete, from-scratch guide to time series forecasting, built around a real example: **forecasting maize price** (using BBS and DAM-style data). It covers two paths — **Classical (SARIMA)** and **Machine Learning (XGBoost)** — and ends with a one-page cheat sheet.

> If you know nothing about time series, read this top to bottom and you'll understand what it is and how to use it.

---

## Table of Contents

1. [What is a time series](#1-what-is-a-time-series)
2. [The three components](#2-the-three-components)
3. [Stationarity](#3-stationarity)
4. [Autocorrelation (ACF / PACF)](#4-autocorrelation-acf--pacf)
5. [ARIMA & SARIMA](#5-arima--sarima)
6. [Workflow — Classical (SARIMA)](#6-workflow--classical-sarima)
7. [Workflow — Machine Learning (XGBoost)](#7-workflow--machine-learning-xgboost)
8. [Python starter code](#8-python-starter-code)
9. [Cheat sheet](#9-cheat-sheet)

---

## 1. What is a time series

A **time series** is data collected at regular time intervals and ordered by time.

```
Jan 2023  ->  28 BDT/kg
Feb 2023  ->  30 BDT/kg
Mar 2023  ->  27 BDT/kg
Apr 2023  ->  25 BDT/kg
```

Each row has a **time** (month) and a **value** (price).

**Why it's different from ordinary data:** in ordinary data (e.g. heights of 100 people) every row is independent and order doesn't matter. In a time series, **order is everything** — this month's price is related to last month's. This is called **temporal dependency**, and it's why standard methods don't apply directly.

> **Key assumption:** past patterns will roughly continue into the future. Maize is harvested in the same season each year and prices fall — so forecasting is possible.

---

## 2. The three components

Any time series can be broken down (**decomposition**) into:

- **Trend** — the long-term direction (rising/falling). Maize price usually has a slow upward trend.
- **Seasonality** — a pattern that repeats every year. For maize this is the biggest factor: supply is high and price low during **harvest season**, higher off-season.
- **Noise** — random, unexplained movement (floods, transport issues, market swings).

```
actual price = trend + seasonality + noise
```

> 🔗 **ML link:** in ML you turn these into **features** — "which month" (seasonality), "row index over time" (trend), "last month's price" (lag). What classical methods capture automatically, ML asks you to build by hand.

---

## 3. Stationarity

The single most important concept — the foundation of ARIMA.

A series is **stationary** if its behavior doesn't change over time (mean and variance stay roughly constant).

- **Stationary** = a person standing in one place, swaying slightly.
- **Non-stationary** = a person walking steadily forward.

Maize price is almost certainly **non-stationary** (it has a trend and seasonality).

**Fix — differencing:** instead of the price values, take the **difference** between consecutive months.

```
price:        28, 30, 27, 25, 31
differenced:  +2, -3, -2, +6     <- often stationary
```

Even if price keeps rising, "how much it changed each month" can stay stable. This is the **"I"** in ARIMA. Check with a plot or the **ADF test** (Augmented Dickey-Fuller), which returns a p-value.

> 🔗 **ML link:** stationarity isn't mandatory for ML models — they handle trend somewhat on their own — but differencing often still helps. Required for classical, helpful for ML.

---

## 4. Autocorrelation (ACF / PACF)

**Correlation** = how much two things move together. **Autocorrelation** = how much a series correlates with **its own past values**.

**Lag** = how far back you look:

```
Lag 1   = correlation with 1 month ago
Lag 12  = correlation with 12 months ago   <- captures seasonality
```

For maize, **Lag 12** matters because last year's same month relates to this year's.

Two graphs help pick model parameters:

- **ACF** — total correlation at each lag (direct + indirect chain effects).
- **PACF** — only the **direct** correlation at each lag (indirect effects removed).

You read these graphs to choose ARIMA's `p` and `q`.

> 🔗 **ML link:** in ML you build **lag features** ("price 1 month ago", "price 12 months ago"). ACF/PACF tell you which lags are worth turning into features.

---

## 5. ARIMA & SARIMA

ARIMA = **AR + I + MA** — three common-sense ideas combined. Think of a shopkeeper guessing next month's price:

| Part | Idea | Parameter | Chosen from |
|------|------|-----------|-------------|
| **AR** (AutoRegressive) | "Last month was 30, before that 29, so this month is near 30." Guess from past values. | `p` = how many months back | PACF |
| **I** (Integrated) | Differencing to remove the rising trend. | `d` = how many times to difference | ADF test |
| **MA** (Moving Average) | "Last month I guessed 30, it was 33 — I was 3 low, adjust up." Correct using past **errors**. | `q` = how many past errors | ACF |

> ⚠️ This "Moving Average" is **not** the ordinary rolling average — it's the average of *errors*. Same name, different idea.

```
ARIMA( p , d , q )
```

**For maize you need SARIMA.** Plain ARIMA can't capture seasonality, which is the dominant effect for maize. SARIMA = ARIMA + a seasonal part:

```
SARIMA(p,d,q)(P,D,Q,s)      s = season length (12 for monthly)
```

Same idea, just applied twice (regular + seasonal). **SARIMA is your end goal.**

---

## 6. Workflow — Classical (SARIMA)

1. **Collect & merge** — BBS + DAM into one file (date, price); align units and date formats.
2. **Clean** — fix missing months, bad values, duplicate dates. The most important step.
3. **Plot** — always look first; spot trend, seasonality, outliers.
4. **Decompose** — split into trend + seasonality + noise.
5. **Stationarity check** — ADF test; decides `d`.
6. **ACF / PACF** — estimate `p`, `q`, and seasonal parameters.
7. **Train/test split** — keep order: old part = train, recent part = test. **Never random.**
8. **Fit model** — SARIMA, or `auto_arima` to search parameters.
9. **Validate** — forecast the test period, compare to actuals (MAE, RMSE, MAPE).
10. **Iterate** — if error is high, adjust parameters and retry.
11. **Final forecast** — refit on all data, forecast the future + confidence interval.

> ⚠️ **Golden rule:** in time series **never split randomly**. Always train on older data, test on recent data. Training on the future = cheating.

**Accuracy metrics:**

| Metric | Meaning |
|--------|---------|
| MAE | average error in BDT |
| RMSE | penalizes big errors more |
| MAPE | average % error (e.g. "5% off") — most intuitive |

---

## 7. Workflow — Machine Learning (XGBoost)

Steps 1–3 (collect, clean, plot) are identical. The real difference is feature engineering.

**Feature engineering ⭐ (the heart of the ML path)** — what ARIMA captures internally, you build as columns:

- **Lag features:** `price_lag_1`, `price_lag_2`, `price_lag_12` (← AR & seasonality)
- **Time features:** `month` (1–12), `year`, `quarter`, `is_harvest_season` (0/1)
- **Rolling means:** `roll_3`, `roll_6`
- **Trend:** `time_index` (1, 2, 3, ...)

Then:

5. **Stationarity** — optional, not mandatory.
6. **Train/test split** — same as classical, keep order. (Advanced: TimeSeriesSplit / walk-forward.)
7. **Fit model** — Random Forest (good baseline) or XGBoost/LightGBM (usually best).
8. **Validate** — same MAE/RMSE/MAPE.
9. **Feature importance ⭐** — the model tells you which features mattered most.
10. **Final forecast** — *recursive*: forecast one month, feed it in as input for the next, step by step.

> ⚠️ **The ML catch (recursive forecasting):** future forecasts need lag features ("last month's price"), but the future's "last month" hasn't happened yet. So you forecast one step, use it as input for the next, and walk forward. SARIMA handles this on its own.

**Two paths side by side:**

| Step | Classical (SARIMA) | ML (XGBoost) |
|------|--------------------|--------------|
| Data prep | differencing | feature engineering ⭐ |
| Parameters | ACF/PACF → p,d,q | feature selection + tuning |
| Split | keep order | keep order (same) |
| Model | SARIMA | RandomForest / XGBoost |
| Validation | MAE/RMSE/MAPE | same |
| Bonus | confidence interval | feature importance ⭐ |
| Future forecast | handles itself | recursive |

> **Advice:** run both and compare MAPE. Strong seasonality often makes SARIMA excellent for agricultural prices; adding many extra features (weather, imports) can push XGBoost ahead.

---

## 8. Python starter code

**Install**

```bash
pip install pandas matplotlib statsmodels pmdarima scikit-learn xgboost
```

**Load & plot**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('maize.csv', parse_dates=['date'], index_col='date')
df = df.asfreq('MS')              # monthly (month start)
df['price'].plot(figsize=(12, 5), title='Maize Price')
plt.show()
```

**Stationarity (ADF test)**

```python
from statsmodels.tsa.stattools import adfuller

result = adfuller(df['price'].dropna())
print('p-value:', result[1])
# p < 0.05 -> stationary; otherwise differencing needed
```

**SARIMA (auto)**

```python
import pmdarima as pm
from sklearn.metrics import mean_absolute_percentage_error as mape

train = df['price'][:-12]         # last 12 months = test
test  = df['price'][-12:]

model = pm.auto_arima(train, seasonal=True, m=12,
                      trace=True, suppress_warnings=True)
fc = model.predict(n_periods=12)
print('MAPE:', mape(test, fc) * 100, '%')
```

**ML (XGBoost) with engineered features**

```python
from xgboost import XGBRegressor

d = df.copy()
for lag in [1, 2, 3, 12]:
    d[f'lag_{lag}'] = d['price'].shift(lag)
d['month'] = d.index.month
d['roll3'] = d['price'].shift(1).rolling(3).mean()
d = d.dropna()

X, y = d.drop(columns='price'), d['price']
Xtr, Xte = X[:-12], X[-12:]
ytr, yte = y[:-12], y[-12:]

m = XGBRegressor(n_estimators=300, learning_rate=0.05)
m.fit(Xtr, ytr)
pred = m.predict(Xte)
```

---

## 9. Cheat sheet

**Glossary**

| Term | Meaning |
|------|---------|
| Trend | long-term direction (up/down) |
| Seasonality | pattern repeating each year (harvest) |
| Noise | random, unexplained movement |
| Stationary | behavior constant over time |
| Differencing | take differences of consecutive values → makes it stationary |
| Lag | value some steps back (lag 12 = 1 year ago) |
| ACF / PACF | which lags correlate — graphs for choosing parameters |

**ARIMA / SARIMA parameters**

| Symbol | What | From |
|--------|------|------|
| `p` | AR — months of past price | PACF |
| `d` | I — times differenced | ADF test |
| `q` | MA — past errors | ACF |
| `P,D,Q` | seasonal p,d,q | seasonal ACF/PACF |
| `s` | season length | 12 for monthly |

**Workflow in one line**

```
collect -> clean -> plot -> decompose -> stationarity (ADF)
  -> ACF/PACF -> train/test split (keep order!) -> fit
  -> validate (MAPE) -> iterate -> final forecast
```

**Golden rules**

- **Plot first** — never model blind.
- **Split by time** — never random.
- **Use SARIMA for maize** (seasonality dominates), not plain ARIMA.
- **Compare with MAPE** — "average % off".
- **Run both paths** — SARIMA vs XGBoost, keep whichever wins.

**Classical vs ML in one line**

| | Classical | ML |
|--|-----------|----|
| Prep | differencing | build features |
| Strength | works on small data, seasonality | many features, large data |
| Start with | this one ✅ | later |

---

*Start by plotting your maize data, then fit a SARIMA.*
