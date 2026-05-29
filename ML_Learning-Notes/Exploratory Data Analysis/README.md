# Exploratory Data Analysis (EDA) — Learning Notes

Hands-on EDA notes on two classic datasets (Titanic + Heart Disease), plus one consolidated cheatsheet that merges everything.

---

## TL;DR — Just open this one file

**[`EDA_FULL_Cheatsheet.ipynb`](./EDA_FULL_Cheatsheet.ipynb)**

Everything below is merged into that single notebook in the standard EDA order:
load -> screen -> profile -> univariate -> outliers/skew -> multivariate -> correlation -> automated report.

---

## Folder structure

```
Exploratory Data Analysis/
├── EDA_FULL_Cheatsheet.ipynb        <-- start here (Titanic + Heart Disease merged)
│
├── Titanic/
│   ├── EDA_Part 1.ipynb             <-- dataset understanding -> univariate
│   ├── EDA_Part 2.ipynb             <-- multivariate + ydata_profiling
│   ├── titanic_data_updated.csv
│   └── report.html                  <-- pre-generated ydata_profiling report
│
└── Heart Disease/
    ├── heart_disease.ipynb          <-- full EDA on heart disease dataset
    ├── heart.csv
    └── report.html
```

---

## What's covered

### 1. Dataset Understanding
- `df.shape`, `df.head()`, `df.sample()`
- Feature reference table for Heart Disease columns
- Auto-categorize features into `cat_cols` / `num_cols`

### 2. Feature Screening & Cleaning
- Missing values count + heatmap
- Duplicate detection + `drop_duplicates()`

### 3. Statistical Profiling
- `df.info()` — dtypes + non-null counts
- `df.describe()` — five-number summary for numerical columns
- `df.describe(include='object')` — for categorical columns

### 4. Univariate Analysis

| Type | Plots |
|---|---|
| Categorical | `countplot`, `value_counts(normalize=True)`, pie chart |
| Numerical | `histplot`, `kdeplot`, `boxplot` |

### 5. Outlier & Skewness
- Boxplot for visual outlier detection
- **IQR rule**: `Q1 - 1.5*IQR  <=  value  <=  Q3 + 1.5*IQR`
- `df[col].skew()` — sign tells you direction of skew

### 6. Multivariate Analysis

| Combination | Plot |
|---|---|
| Cat-Cat | `countplot(hue=...)` + `groupby().value_counts(normalize=True)` |
| Cat-Num | `barplot`, `kdeplot(hue=...)` |
| Num-Num | `scatterplot` |

### 7. Big-Picture Relationships
- `sns.pairplot(...)` — scatter matrix for a small subset of features
- `sns.heatmap(df.corr())` — correlation heatmap

### 8. Automated EDA
- `ydata_profiling.ProfileReport` — generates a full HTML report
- Pre-generated reports in both `Titanic/report.html` and `Heart Disease/report.html`

---

## How to run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib seaborn ydata-profiling
   ```
2. Open `EDA_FULL_Cheatsheet.ipynb` in **Jupyter** or **VS Code**.
3. Run cells top-to-bottom. The notebook expects to be run from this folder, with both `Titanic/` and `Heart Disease/` subfolders present.

---

## The standard EDA workflow

1. **Load & shape** — `read_csv`, `df.shape`, `df.head()`, `df.sample()`
2. **Screen** — missing values + duplicates
3. **Categorize** — `select_dtypes` to split categorical / numerical
4. **Profile** — `df.info()`, `df.describe()`
5. **Univariate** — per-column plots (categorical vs numerical)
6. **Outlier / skew** — IQR bounds + `.skew()`
7. **Multivariate** — relationship plots (Cat-Cat / Cat-Num / Num-Num)
8. **Big-picture** — `pairplot`, correlation heatmap
9. **Automate** — `ydata_profiling` for a one-shot HTML report

---

## Datasets

- **Titanic** — classification problem: did the passenger survive?
  Source: classic Kaggle Titanic dataset.
- **Heart Disease** — classification problem: is heart disease present?
  Source: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

---

## Notes

- **Always check distributions** before deciding on imputation / scaling later. Skewed columns (like Fare, Cholesterol) often need median imputation + RobustScaler or log transforms.
- **`countplot` with `hue`** is the single most useful plot for classification EDA — it shows class imbalance and feature-target relationship in one shot.
- **`groupby(col)[target].value_counts(normalize=True)`** gives the within-group survival/disease *rate*, which is often more informative than raw counts.
- The HTML profiling reports (`report.html`) are pre-generated — open them in a browser for an instant overview without running any code.
