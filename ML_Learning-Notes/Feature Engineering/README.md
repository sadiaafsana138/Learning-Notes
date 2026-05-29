# Feature Engineering — Learning Notes

A complete, hands-on collection of Feature Engineering techniques for ML, with one consolidated cheatsheet plus topic-wise deep-dive folders.

---

## TL;DR — Just open this one file

**[`Feature_Engineering_FULL_Cheatsheet.ipynb`](./Feature_Engineering_FULL_Cheatsheet.ipynb)**

Everything below is merged into that single notebook in the correct execution order — load → split → impute → outlier-handle → encode → scale → ColumnTransformer pipeline.

---

## Folder structure

```
Feature Engineering/
├── Feature_Engineering_FULL_Cheatsheet.ipynb   <-- start here (everything merged)
├── README.md
│
├── 1. Data Distribution-splitting-missing values/
│   ├── Feature Engineering_1(Starter,_Train_Test_and_Handling_Missing_Values).ipynb
│   ├── Missing value handle.ipynb
│   ├── Missing values.pdf
│   ├── Understanding Data Distribution of a Dataset.pptx
│   ├── titanic_data_updated.csv                <-- used by the cheatsheet
│   └── science_job.csv                         <-- used in CCA demo
│
├── 2. Outlier(Z-score,IQR,Winsorization_Technique)/
│   ├── Feature_Engineering_2_Outlier_Handling_.ipynb
│   ├── Winsorization_Technique.ipynb
│   ├── Outlier Detection & Handling.pptx
│   └── marks_dataset.csv                       <-- used in Winsorization / Robust scaling demos
│
├── 3. Encoding(Ordinal,OneHot,Label)/
│   └── Feature_Engineering_3_Encoding.ipynb
│
├── 4. Scalling (Standard-zscore normal, MinMax , Robust)/
│   ├── Feature_Engineering_4_Scalling.ipynb
│   └── Robust_Scaler.ipynb
│
└── 5. ColumnTransformer/
    └── Titanic_Feature_Engineering_via columntransformer.ipynb
```

The cheatsheet reads its CSVs **directly from folders `1.` and `2.`** — no copies in the root.

---

## What's covered

### 1. Data Distribution + Train/Test Split
- Loading data, dropping irrelevant columns
- Checking missing-value percentages
- Why we split **before** doing anything else (avoid data leakage)

### 2. Missing Value Handling

| Technique | When to use |
|---|---|
| CCA (Complete Case Analysis) | Missing < 5% and random |
| Mean imputation | Numerical + roughly normal |
| Median imputation | Numerical + skewed / has outliers |
| Arbitrary value (-1, 99, 999) | Tree models, flag missingness |
| Random sample imputation | Preserve original distribution |
| Mode / most-frequent | Categorical with few missing |
| Constant `'Missing'` + indicator | Categorical with lots of missing (Cabin) |

Demonstrated with both **pandas** and **`sklearn.impute.SimpleImputer`**.

### 3. Outlier Detection & Handling

| Method | When to use |
|---|---|
| Z-Score (`abs(z) > 3`) | Data is approximately normal |
| IQR (`Q1 - 1.5*IQR`, `Q3 + 1.5*IQR`) | Data is skewed |
| Winsorization (percentile clip) | Custom percentile-based capping |

Two strategies shown: **trim** (drop rows) and **clip** (cap to bounds).

### 4. Encoding

| Encoder | Use for |
|---|---|
| `OrdinalEncoder` | Ordered categories (e.g. `third < second < first`) |
| `OneHotEncoder` | Nominal categories (Sex, Embarked, Cabin_Deck) |
| `LabelEncoder` | Target column `y` only |

Includes the feature-engineered `Cabin_Deck = Cabin.str[0]` trick.

### 5. Scaling

| Scaler | Formula | Use when |
|---|---|---|
| `StandardScaler` | `(x - mean) / std` | Data approximately normal |
| `MinMaxScaler` | `(x - min) / (max - min)` -> [0, 1] | Bounded range, no extreme outliers |
| `RobustScaler` | `(x - median) / IQR` | Data has outliers |

### 6. ColumnTransformer (Production Pattern)
End-to-end pipeline combining imputation + encoding + scaling in one place, applied **only after train/test split**.

---

## How to run

1. Make sure you have a Python environment with:
   ```
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
2. Open `Feature_Engineering_FULL_Cheatsheet.ipynb` in **Jupyter** or **VS Code**.
3. Run cells top-to-bottom — they execute sequentially (each section builds on the previous).
4. The required CSVs live inside the numbered subfolders (`1. Data Distribution-splitting-missing values/` and `2. Outlier(Z-score,IQR,Winsorization_Technique)/`). The cheatsheet uses relative paths to them, so just keep the folder structure intact.

---

## The golden order — follow this in every project

1. Load + drop irrelevant columns + check `isnull().mean()`
2. **`train_test_split` FIRST** (before anything else)
3. **Impute** missing values (fit on train, transform train + test)
4. **Handle outliers** (z-score / IQR / winsorization depending on distribution)
5. **Encode** categoricals (Ordinal / OneHot / Label-for-target)
6. **Scale** numerics (Standard / MinMax / Robust)
7. Wrap steps 3-6 into a **`ColumnTransformer`** for production

---

## Notes

- All sklearn transformers are **fit on `X_train` only**, then applied to both `X_train` and `X_test`. This is the single most important rule to avoid data leakage.
- For categorical imputation of high-missing-rate columns (like Cabin at ~77%), prefer `strategy='constant', fill_value='Missing', add_indicator=True` over mode imputation.
- Z-score outlier detection assumes a roughly normal distribution — use IQR for skewed data.
- `LabelEncoder` is for the **target only**. For features, use `OrdinalEncoder` (which accepts 2D input and supports an explicit `categories=` order).
