# 00 — Document inventory (কোন ফাইল কোথায়, পড়া গেছে কি না)

Project root: `D:\Study\Phitron AI_ML Projects\Learning-Notes\Brac MSc\Fall 2026\CSE 791 - Methodology\Paper Critic - 10%`
(নিচের path-গুলো এই root থেকে relative। কোনো original ফাইল modify/move/delete করা হয়নি। লেখা হয়েছে শুধু `work/`, `pages/`, `registers/`, `synthesis/`, `review/` আর root-এর `.md` ফাইলে।)

## ১. Main paper আর SI

| ভূমিকা | Path | Pages | Readability |
|---|---|---|---|
| **Main paper** (Ecological Informatics 97, 103885) | `1-s2.0-S157495412600292X-main.pdf` | 16 | সব পেজে text আছে (PyMuPDF দিয়ে extract)। প্রতিটা পেজ PNG করে figure দেখা হয়েছে (p3, p4, p6, p7, p8, p9, p10)। |
| **Supporting Information (SI)** | `AutoML and XAI.pdf` ("Table S1" আছে) | 24 | Text আছে p1–7, p9–17 (Table S1–S9)। p8 খালি text (শুধু image/blank)। p18–24 মূলত figure (S1–S7): শুধু S6 (p23) আর S7 (p24) দেখা হয়েছে; S1–S5 (p18–22) পড়া/বোঝা হয়নি — figure হিসেবে unreadable নয়, শুধু দেখা হয়নি। |

Page numbering: PDF page N = journal page N (p1 = title/abstract, p16 = শেষ references)।
Body: p1–12 (শেষ হয় Conclusions + CRediT-এর শুরুতে), p12–16 = CRediT, ethics/funding, references।

## ২. Code ও data folder (`AutoML-and-Explainable-AI-XAI-for-Rice-main/`)

পুরো তালিকা (size, row count, column names, purpose) আছে `work/code-inventory.md`-তে (git-ignored)। সংক্ষেপে:

| ফাইল | কী |
|---|---|
| `aus_data_all.csv` | 677 rows × 68 cols |
| `aman_data_all.csv` | 6,664 rows × 76 cols |
| `boro_data_all.csv` | 5,809 rows × 82 cols |
| `yield_{aus,aman,boro}_autoML.Rmd/.html` | H2O AutoML + DALEX PFI/PDP/ALE + iml H-statistic |
| `local_XAI_uniion_{aus,aman,boro}.Rmd/.html` | break_down (local XAI) প্রতিটা row-এর জন্য |
| `gw_correlation_aman_01/02.Rmd/.html` | GW correlation (শুধু Aman) |
| `*.zip` (data, 3 yield Rmd, local_XAI aman) | zip copy |
| `README.md`, `test` | repo README; 1-byte stray ফাইল |

**Repo-তে নেই (Not reported in the provided paper, Supporting Information, or available code):** `train_data.csv`, `test_data.csv`, `aus/aman/boro_union_data_all.csv`, shapefile (`aman_GWM_01.shp` ইত্যাদি), saved H2O models, CCAFS-MOT code, GHG-PFI (Fig. S7) code, Aus/Boro GW-correlation code, train/test split বানানোর code।

## ৩. কী চালানো হয়েছে, কী চালানো যায়নি

- Python (pandas, scikit-learn, PyMuPDF, BeautifulSoup) দিয়ে সব check; scripts: `work/scripts/*.py`।
- R এই machine-এ নেই (`Rscript` পাওয়া যায়নি) → কোনো `.Rmd` **চালানো হয়নি**; H2O/DALEX output পড়া হয়েছে knit-করা `.html` থেকে।
- AutoML **retrain করা হয়নি** (নির্দেশ অনুযায়ী)।
- `pdftoppm` নেই; PyMuPDF দিয়ে PNG render করা হয়েছে (130 dpi main, 110 dpi SI)।

## ৪. Existing pages
`pages/page-01.md`, `pages/page-02.md` আগে থেকে ছিল না (শুরুতে `pages/` ফোল্ডার খালি ছিল), তাই সব ১৬টা page এই session-এ নতুন লেখা হয়েছে।
