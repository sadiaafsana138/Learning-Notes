# Code & data audit (registers/code-audit.md)

**নিয়ম:** R এই machine-এ নেই ⇒ কোনো `.Rmd` চালানো হয়নি; H2O/DALEX ফল পড়া হয়েছে knit-করা `.html` থেকে। AutoML retrain করা হয়নি। সব Python script `work/scripts/` এ (re-run করা যায়)। নিচের প্রতিটা output-block সেই script-এর হুবহু printed output।
**লেবেল:** "OUR OWN CHECK" = সরল model/পরিসংখ্যান দিয়ে আমাদের নিজস্ব যাচাই, paper-এর reproduction নয়।
**Scripts:** `check01_07_data.py` (checks 1,2,4,5,6,7), `check01b_household_id.py`, `check07b_s5_union_mean.py`, `check03_09_10_models.py` (3, 9, 10), `check_arith_F1_F4.py`, `check_anova_s31.py`, `check_moran.py`, `check_pfi_tables.py`, `check_breakdown_proxy.py`, `check_ghg_partial_ttest.py`, `check_intensity.py`। HTML সংখ্যা: `work/html_*.txt` (HTML থেকে extract, `check08_html.py`)।

## 0. Code finding table (file:line)

| # | ফাইল : লাইন | কোড কী করে | paper কী বলে | মেলে? | কেন গুরুত্বপূর্ণ | real error / execution লাগবে? |
|---|---|---|---|---|---|---|
| C1 | `yield_aus_autoML.Rmd:56-57,200`; `yield_aman_autoML.Rmd:58-59,213`; `yield_boro_autoML.Rmd:59-60,216` | `train_data.csv`/`test_data.csv` পড়ে; `h2o.automl(nfolds=10, …)` — `fold_column` নেই; split-তৈরির code নেই | "randomly split 80/20" (p4) | আংশিক (random ✔; group নেই, split code অনুপস্থিত) | union/household identity train ও test-এ ভাগ হয়ে যায় ⇒ "unseen area" নয়; CV-ও row-level | design issue (code পড়েই নিশ্চিত); leakage-এর পরিমাণ → আসল split লাগবে |
| C2 | `yield_aus_autoML.Rmd:849-862`; Aman:862-875; Boro:865-878 | `explainer_train` (data = `x_train`); `variable_importance(explainer_train, type="difference")`; কোনো `explainer_test` নেই | "training or test data" (p5); PFI "factor" (p7) | ✗ (train-only; difference ≠ factor) | train-এ PFI overfit-নির্ভর; test-এ ভিন্ন হতে পারে | real (code পড়েই); প্রভাবের মাত্রা → execution লাগবে |
| C3 | Aus:1016-1054 (`model_profile(explainer_train, type="partial"/"accumulated")`) | PD/ALE train-এ | Fig. 7 | train-only | extrapolation/sparse অঞ্চল | real |
| C4 | `yield_aus_autoML.Rmd:120,127-129`; Aman:133,140-142; Boro:136,143-145; `local_XAI_uniion_aus.Rmd:108,115-117,152`; `local_XAI_uniion_aman.Rmd:119,126-128` | `scale(fea[,1:33])` (Aman 1:45; Boro 1:46) প্রতিটি data-frame (all/train/test) আলাদা mean/SD-তে | scaling-এর উল্লেখ নেই | অনুপস্থিত | test/all-data train-এর scale-এ নয় ⇒ distribution shift (বিশেষত GLM/DNN, local XAI) | real design issue; প্রভাব → execution |
| C5 | Aus:202-207; Aman:215-220; Boro:218-223 | `stopping_tolerance=0.001`, `stopping_rounds=3`, `max_runtime_secs_per_model=0`, `#max_models=20` (commented) | 0.0001, 2, `max_runtime_secs`=`max_models`=0 (p4); SI S2: "MAE stable last five rounds" | ✗ | settings তিন উৎসে তিন রকম | real (reporting) |
| C6 | Aus:1066-1076; Aman:1089; Boro:1093 | `Interaction$new(Predictor)` (H-statistic); `Feature_Interaction.csv`, `FIGURE_Interaction.tif` লেখে | "AL parallel to PD ⇒ additive" (p8) — H-statistic report নেই | ✗ (চালানো, report নেই) | additivity claim-এর প্রমাণ অনুপস্থিত | real; ফল HTML-এ নেই (tiff-এ লেখা), CSV repo-তে নেই |
| C7 | Aus:115; Aman:128; Boro:131 (`"Water_regime"` feature); SI S8/S9 `Water Regime` | model predictor | "water data excluded" (p12) | ✗ | reporting অসঙ্গতি; importance ≈ 0 | real (reporting) |
| C8 | `gw_correlation_aman_01.Rmd:45-50,56,77`; `_02.Rmd` (Crop_Types বাদ) | `Crop_Types` (nominal) numeric Pearson/GWR-এ; `_02` বাদ | paper: GD, N, P, K | `_01` ✗, `_02` ✔ | nominal → numeric অর্থহীন | real (code-level); প্রকাশিত Fig. 9-এ crop type নেই |
| C9 | শুধু `gw_correlation_aman_*` আছে | Aman GW correlation | Aus, Aman, Boro (Fig. 9) | আংশিক | Aus/Boro অপুনরুৎপাদ্য | অনুপস্থিত code |
| C10 | CCAFS-MOT code নেই; GHG-PFI (Fig. S7) code নেই; NDVI/weather/kriging processing code নেই | — | "All relevant R code available" (p5); Data availability (p13) | ✗ | GHG ও feature-engineering অপুনরুৎপাদ্য | অনুপস্থিত |
| C11 | `yield_aus_autoML.Rmd:810` (`ggplot(data=t.xy …)`) বনাম `:800` (`test.xy<-…`) | object-নাম অমিল | — | ✗ | Aus Fig. 5 chunk error দেবে (Aman/Boro-তে `test.xy` ✔) | real bug (execution-এ error) |
| C12 | `local_XAI_uniion_aman.Rmd:2` title "Local_XAI: Boro Yield Prediction"; `local_XAI_uniion_aus.Rmd:231` লেখে `Local_contribution_aman_union.csv` | — | — | ✗ | copy-paste ঝুঁকি | real (naming); প্রভাব → execution |
| C13 | `yield_aman_autoML.Rmd:87` `NDVI_205` বনাম `:99` `t2m_209`; SI S3 Aman তারিখ 209; `yield_boro_autoML.Rmd:91` `NDVI_001_2105` | column নাম | S3 | ✗ (typo) | নামগত অসঙ্গতি | typo (data-মান যাচাই ছাড়া নিশ্চিত নয়) |
| C14 | `local_XAI_uniion_aus.Rmd:159`, `_aman.Rmd:170`, `_boro.Rmd:171` (`h2o.loadModel` …AutoML_4_20211104_201857 / …AutoML_5_20211104_162457 / …AutoML_2_20211102_201704) বনাম HTML model ID (Aus …AutoML_5_20211128_82339, Aman …AutoML_3_20211127_174647, Boro …AutoML_1_20211104_123317) | local XAI-এর model ≠ AutoML-script-এর best model | কোনটা paper-এ — অনুল্লেখ | ✗ | Fig. 8 ও Table 4/Fig. 6–7 ভিন্ন run | real (document-অনুপস্থিতি) |
| C15 | `local_XAI_uniion_*.Rmd:47,48,152` (`*_union_data_all.csv`) | local XAI সব union-row-এ, train file-এ নয় | "union-average attributions" | আংশিক | input file অজানা; repo-তে নেই | অনুপস্থিত |
| C16 | `*.Rmd:26-28` hard-coded `setwd("/home/zia207/Dropbox/…")`, `C:\\Users\\zahmed2\\…` | — | — | — | পুনরুৎপাদনযোগ্যতা | cosmetic |
| C17 | `yield_aus_autoML.Rmd:792` (commented `h2o.loadModel("…AutoML_1_20211102_184016")`); তিন Rmd-তেই একই | copy-paste অবশেষ | — | — | কোন model — অস্পষ্ট | cosmetic |

> "real" = কোড পড়ে নিশ্চিত; "execution লাগবে" = R চালিয়ে প্রভাব মাপতে হবে (আমরা পারিনি — Rule 8)।

## 1. Unit of a row (Check 1) ও household-like key
**কী পেলাম:** প্রতিটি `Index` অনন্য ⇒ row = একটি household-plot-season record। আলাদা household/plot ID column নেই। Union ID: `UNION_ID` (Aus, Boro), `UNION_CODE` (Aman)। Union-প্রতি row: Aus min 1 / median 3 / max 60 (78 union); Aman 1/18/200 (246); Boro 1/20/207 (224)।
`Index`-এর প্রথম দুই token (আমাদের **অনুমান**; documentation নেই) দিয়ে "household-like key": 307 / 2,241 / 2,103; token-2 আলাদাভাবে ~318 অনন্য (≈ 325 PSU?) — **suspected**।
**Confidence:** row-unit = মাঝারি-উচ্চ; household-key = নিম্ন। **Seed:** "row unit অস্পষ্ট" — verified।
```text
===== AUS (677, 68)
Index unique: 677 of 677
Index examples: ['1000_20194011771_2_2_TAus (HYV)', '1000_20194011771_5_3_TAus (HYV)', '102_1040913024_2_2_TAus (HYV)']
Index duplicates: 0
unions: 78 rows/union min/median/max: 1 3.0 60
household-like key (first two tokens) unique: 307 rows/hh min/med/max: 1 2.0 14
Crop_Types counts: {'HYV': 433, 'Local': 223, 'Hybrid': 21}
env cols: 29 | unions with >1 row: 65 | share of (union,env col) cells with exactly 1 unique value: 1.0000
max #unique env values within union: 1
Water regime values: {'Rainfed, wet season': 677}
Water regime unique within union (share of unions w/ 1 value): 1.0
GD describe: {'count': 677.0, 'mean': 103.1, 'std': 7.9, 'min': 91.0, '25%': 99.0, '50%': 103.0, '75%': 103.0, 'max': 123.0}
GHG-ish columns: ['Total_GWP', 'Emission_Intensity']
S5 recompute (n=677): r(GWP,N)=0.831 r(GWP,P)=0.385 r(GWP,K)=0.326 r(GWP,GD)=0.311 r(GWP,YIELD)=0.382
  also r(YIELD,N/P/K/GD) = 0.400 0.402 0.276 0.049
YIELD min/max: 247 5487 | missing per col top: {'Index': 0, 'Crop': 0, 'Seasons': 0, 'Crop_Types': 0}

===== AMAN (6664, 76)
Index unique: 6664 of 6664
Index examples: ['1000_20194011771_1_2_T Aman (HYV)', '1000_20194011771_4_3_T Aman (HYV)', '1009_20195425751_2_2_B Aman (local)']
Index duplicates: 0
unions: 246 rows/union min/median/max: 1 18.0 200
household-like key (first two tokens) unique: 2241 rows/hh min/med/max: 1 2.0 29
Crop_Types counts: {'HYV': 5213, 'Local': 1208, 'Hybrid': 243}
env cols: 41 | unions with >1 row: 234 | share of (union,env col) cells with exactly 1 unique value: 1.0000
max #unique env values within union: 1
Water regime values: {'Continuous flooding': 6614, 'Deepwater': 50}
Water regime unique within union (share of unions w/ 1 value): 0.874
GD describe: {'count': 6664.0, 'mean': 117.6, 'std': 12.9, 'min': 91.0, '25%': 109.0, '50%': 117.0, '75%': 123.0, 'max': 146.0}
GHG-ish columns: ['Total_GWP', 'Emission_Intensity']
S5 recompute (n=6664): r(GWP,N)=0.166 r(GWP,P)=0.001 r(GWP,K)=0.085 r(GWP,GD)=0.226 r(GWP,YIELD)=0.053
  also r(YIELD,N/P/K/GD) = 0.364 0.295 0.357 0.041
YIELD min/max: 112 8230 | missing per col top: {'Unnamed: 73': 6664, 'Index': 0, 'Seasons': 0, 'Crop': 0}

===== BORO (5809, 82)
Index unique: 5809 of 5809
Index examples: ['1_4010817010_1_3.1_Boro (HYV)', '10.2_4010817010_2_10.1_Boro (HYV)', '10.2_4010817010_3_7.1_Boro (HYV)']
Index duplicates: 0
unions: 224 rows/union min/median/max: 1 20.0 207
household-like key (first two tokens) unique: 2103 rows/hh min/med/max: 1 2.0 25
Crop_Types counts: {'HYV': 4973, 'Hybrid': 836}
env cols: 42 | unions with >1 row: 211 | share of (union,env col) cells with exactly 1 unique value: 1.0000
max #unique env values within union: 1
Water regime values: {'Continuous flooding': 5809}
Water regime unique within union (share of unions w/ 1 value): 1.0
GD describe: {'count': 5809.0, 'mean': 122.9, 'std': 7.5, 'min': 110.0, '25%': 120.0, '50%': 123.0, '75%': 123.0, 'max': 157.0}
GHG-ish columns: ['Total_GWP', 'Emission_Intensity']
S5 recompute (n=5809): r(GWP,N)=0.538 r(GWP,P)=0.228 r(GWP,K)=0.248 r(GWP,GD)=0.211 r(GWP,YIELD)=0.177
  also r(YIELD,N/P/K/GD) = 0.127 0.077 0.054 -0.001
YIELD min/max: 0 9259 | missing per col top: {'ID': 0, 'Index': 0, 'Crop': 0, 'Seasons': 0}

TOTAL rows 13150 vs paper 13,137; diff 13
Paper unions 78/247/224

aus token2 unique: 85 | rows/hh min/med/max: 1 4.0 60 | token2 startswith union id (%): 14.6 | token2 length counts: {11: 525, 10: 152}
aman token2 unique: 283 | rows/hh min/med/max: 1 18.0 133 | token2 startswith union id (%): 8.2 | token2 length counts: {11: 6024, 10: 640}
boro token2 unique: 261 | rows/hh min/med/max: 1 15.0 131 | token2 startswith union id (%): 10.0 | token2 length counts: {11: 5572, 10: 237}
unique household-like ids across 3 seasons: 318 (paper: 6500 households; 13,137 farmers)
```

## 2. Environmental duplication (Check 2)
উপরের output: প্রতি union-এর ভেতরে সব (union × env column) cell-এ unique value = **1** (share 1.0000)। **নিশ্চিত:** union-centroid assignment। Confidence উচ্চ।

## 3. Leakage size (Check 3) — **simulation**, আসল split reconstruct করা যায়নি
`train_data.csv`/`test_data.csv` নেই; বিকল্প: paper-এর পদ্ধতি অনুযায়ী 200× random 80/20 split-এ test-row-এর কত % union/household-like key train-এ আছে (নিচে Check 9-এর block-এর "CHECK 3" অংশ)।
**ফল:** union-share Aus 97.0%, Aman 99.8%, Boro 99.7%; household-like-key 73.9/85.1/82.6%। **এটা leakage "প্রমাণ" নয়** (Rule 6): confirm করতে আসল split ফাইল + union ID লাগবে। Confidence: মাঝারি।
**Seed:** F10 (split row-level) — verified (code-level); leakage-পরিমাণ — potential, unconfirmed।

## 4. Row counts (Check 4)
13,150 (677 + 6,664 + 5,809) বনাম paper 13,137 (পার্থক্য 13); unions Aus 78 ✔, Aman **246** (paper 247), Boro 224 ✔। কারণ অজানা। HTML train rows: Aus 526 (`Null D.o.F. 525`), Aman 5,305, Boro 4,626 ⇒ 77.7/79.6/79.6% (80% নয়)।

## 5. Water_regime (Check 5)
Aus: "Rainfed, wet season" (677/677); Aman: "Continuous flooding" 6,614 + "Deepwater" 50; Boro: "Continuous flooding" 5,809/5,809। ⇒ farmer-reported irrigation নয়; season-based class (উৎস অজানা — "Not reported in the provided paper, Supporting Information, or available code."); PFI importance ≈ 0 (S8: 1.26±9.49; S9: 0.00±15.48)। **Seed (Water_regime predictor despite exclusion claim): verified।**

## 6. Field duration (Check 6)
Harvest − transplanting তারিখ column data-তে নেই ⇒ **reproduce করা যায়নি**। Range (days): Aus 91–123 (mean 103.1, SD 7.9), Aman 91–146 (117.6, 12.9), Boro 110–157 (122.9, 7.5)।

## 7. GHG columns ও S5 recompute (Check 7)
Columns: `Total_GWP` (Aman-এ trailing space), `Emission_Intensity` — **CH₄/N₂O/CO₂ আলাদা নেই** (README-র দাবির বিপরীত)। `Emission_Intensity` ≈ `Total_GWP/YIELD` (corr ≥ 0.999; অনুপাত median 1.13/1.19/1.15 — সংজ্ঞা অজানা)।
```text
AUS union-mean (n unions=78) vs row-level vs S5
 GWP~GD: union-mean r=0.309 | row r=0.311 | S5(GWP col)=0.309
 GWP~N: union-mean r=0.816 | row r=0.831 | S5(GWP col)=0.816
 GWP~P: union-mean r=0.545 | row r=0.385 | S5(GWP col)=0.545
 GWP~K: union-mean r=0.483 | row r=0.326 | S5(GWP col)=0.483
 GWP~YIELD: union-mean r=0.559 | row r=0.382
 YIELD~GD: union-mean r=0.203 | row r=0.049 | S5(YIELD col)=0.203
 YIELD~N: union-mean r=0.592 | row r=0.400 | S5(YIELD col)=0.592
 YIELD~P: union-mean r=0.625 | row r=0.402 | S5(YIELD col)=0.625
 YIELD~K: union-mean r=0.450 | row r=0.276 | S5(YIELD col)=0.45

AMAN union-mean (n unions=246) vs row-level vs S5
 GWP~GD: union-mean r=0.256 | row r=0.226 | S5(GWP col)=0.277
 GWP~N: union-mean r=0.210 | row r=0.166 | S5(GWP col)=0.201
 GWP~P: union-mean r=0.103 | row r=0.001 | S5(GWP col)=0.108
 GWP~K: union-mean r=0.224 | row r=0.085 | S5(GWP col)=0.223
 GWP~YIELD: union-mean r=0.085 | row r=0.053
 YIELD~GD: union-mean r=0.015 | row r=0.041 | S5(YIELD col)=0.026
 YIELD~N: union-mean r=0.638 | row r=0.364 | S5(YIELD col)=0.632
 YIELD~P: union-mean r=0.549 | row r=0.295 | S5(YIELD col)=0.558
 YIELD~K: union-mean r=0.621 | row r=0.357 | S5(YIELD col)=0.595

BORO union-mean (n unions=224) vs row-level vs S5
 GWP~GD: union-mean r=0.058 | row r=0.211 | S5(GWP col)=0.058
 GWP~N: union-mean r=0.593 | row r=0.538 | S5(GWP col)=0.593
 GWP~P: union-mean r=0.343 | row r=0.228 | S5(GWP col)=0.343
 GWP~K: union-mean r=0.427 | row r=0.248 | S5(GWP col)=0.427
 GWP~YIELD: union-mean r=0.226 | row r=0.177
 YIELD~GD: union-mean r=-0.094 | row r=-0.001 | S5(YIELD col)=-0.094
 YIELD~N: union-mean r=0.256 | row r=0.127 | S5(YIELD col)=0.256
 YIELD~P: union-mean r=0.176 | row r=0.077 | S5(YIELD col)=0.176
 YIELD~K: union-mean r=0.147 | row r=0.054 | S5(YIELD col)=0.147
```
**ফল:** SI S5 = **union-mean (ecological) correlation** (Aus ও Boro হুবহু; Aman প্রায় — 246 বনাম 247 union); row-level অনেক কম। Section 3.6 "moderate to strongly positive" Aman-এ ভুল (S5 Aman N 0.201, P 0.108, K 0.223, FD 0.277; yield~GWP 0.061)। FD: Aus 0.309 > Aman 0.277 > Boro 0.058 ⇒ Section 3.6-এর "Aus weak" ভুল, Discussion ঠিক। **Seed F5: verified।** Confidence: উচ্চ।
**Circularity (F6) / collinearity:**
```text
aus row        n=  677 corr(N,P)=0.39 corr(N,K)=0.29 corr(P,K)=0.31 | r(GWP,P)=0.385 partial(P|N)=0.116 | r(GWP,K)=0.326 partial(K|N)=0.164 | R2 GWP~N=0.69
aus union-mean n=   78 corr(N,P)=0.56 corr(N,K)=0.41 corr(P,K)=0.46 | r(GWP,P)=0.545 partial(P|N)=0.181 | r(GWP,K)=0.483 partial(K|N)=0.283 | R2 GWP~N=0.67
              n     N     P     K     GD     GWP       Y
Crop_Types                                              
HYV         433  72.9  27.1  21.2  102.9   983.5  3299.5
Hybrid       21  88.0  30.1  33.6  109.3  1134.5  3855.0
Local       223  59.6  19.9   7.4  102.9   915.1  2656.4
  Welch t-test GWP HYV vs Hybrid: diff=151 t=-4.35 p=0.000253 (row-level, ignores clustering)
  Welch t-test GWP HYV vs Local: diff=-68 t=4.31 p=2.12e-05
aman row        n= 6664 corr(N,P)=0.39 corr(N,K)=0.44 corr(P,K)=0.39 | r(GWP,P)=0.001 partial(P|N)=-0.070 | r(GWP,K)=0.085 partial(K|N)=0.013 | R2 GWP~N=0.03
aman union-mean n=  246 corr(N,P)=0.57 corr(N,K)=0.61 corr(P,K)=0.63 | r(GWP,P)=0.103 partial(P|N)=-0.022 | r(GWP,K)=0.224 partial(K|N)=0.123 | R2 GWP~N=0.04
               n      N     P     K     GD     GWP       Y
Crop_Types                                                
HYV         5213   87.5  29.6  28.0  117.7  4655.2  3811.4
Hybrid       243  100.7  33.3  37.2  115.3  4621.6  4471.7
Local       1208   44.1  10.7   4.0  117.6  4040.5  2274.2
  Welch t-test GWP HYV vs Hybrid: diff=-34 t=0.31 p=0.76 (row-level, ignores clustering)
  Welch t-test GWP HYV vs Local: diff=-615 t=10.71 p=5.61e-26
boro row        n= 5809 corr(N,P)=0.45 corr(N,K)=0.25 corr(P,K)=0.23 | r(GWP,P)=0.228 partial(P|N)=-0.016 | r(GWP,K)=0.248 partial(K|N)=0.137 | R2 GWP~N=0.29
boro union-mean n=  224 corr(N,P)=0.55 corr(N,K)=0.47 corr(P,K)=0.39 | r(GWP,P)=0.343 partial(P|N)=0.024 | r(GWP,K)=0.427 partial(K|N)=0.210 | R2 GWP~N=0.35
               n      N     P     K     GD     GWP       Y
Crop_Types                                                
HYV         4973  132.8  65.7  42.9  122.7  3734.4  5442.9
Hybrid       836  119.4  58.0  40.6  123.7  3861.9  6080.7
  Welch t-test GWP HYV vs Hybrid: diff=127 t=-4.33 p=1.65e-05 (row-level, ignores clustering)
```

## 8. HTML outputs (Check 8) — F1 ও F2 নিষ্পত্তি
`work/html_{aus,aman,boro}.txt` থেকে প্রধান সংখ্যা:

| Season (HTML) | Model ID (best) | base models | stack TRAIN RMSE/MAE | stack 10-fold CV RMSE/MAE/RMSLE | meta-learner level-one RMSE/MAE/RMSLE/R² | test RMSE/MAE/RMSLE | train rows |
|---|---|---|---|---|---|---|---|
| Aus | `StackedEnsemble_AllModels_4_AutoML_5_20211128_82339` | **958** (DL 18, DRF 2, GBM 769, GLM 1, XGB 168); active 13 | 404.77 / 309.90 | 836.03 / 637.33 / 0.3523 | 816.68 / 622.46 / 0.3452 / **0.5448** | **817.64 / 652.09 / 0.3148** | 526 |
| Aman | `…_4_AutoML_3_20211127_174647` | **175** (DL 10, DRF 2, GBM 130, GLM 1, XGB 32); active 9 | 442.47 / 309.85 | 928.20 / 648.44 / 0.3421 | 926.23 / 647.33 / 0.3416 / 0.5942 | **948.71 / 668.71 / 0.3354** | 5,305 |
| Boro | `…_3_AutoML_1_20211104_123317` | **188**; active 9 | 495.38 / 351.14 | 1112.41 / 772.56 / 0.4316 | 1110.02 / 771.27 / 0.4311 / 0.5117 | **1122.67 / 786.52 / 0.5413** | 4,626 |

- **F1 (Table 4 swapped): VERIFIED.** Table 4 "Boro" (958 models; 816.01/622.31/0.35/0.55) ≈ Aus HTML level-one (816.68/622.46/0.345/0.545) = S6 Aus CV (816.0/0.543). Table 4 "Aus" (198; 1109.2/773.47/0.43/0.51) ≈ Boro HTML (CV 1112.41/772.56/0.4316; level-one R² 0.5117) = S6 Boro CV (1109.2/0.510)। Boro base-model সংখ্যা HTML-এ 188 (paper 198)। Aman মেলে। Confidence: উচ্চ। Table 4-এর "CV" আসলে meta-learner level-one metric; stack-এর true CV RMSE বেশি (Aus 836.03)।
- **F2 (Fig. 5 vs S6 test): REVISED।** S6 test RMSE = HTML test RMSE (817.6/948.7/1122.7) ✔। S6 test **R²** Aman (0.590) ও Boro (0.514) নিজের RMSE-র সাথে অসঙ্গত (implied 0.562, 0.524); Fig. 5 R² (0.451/0.561/0.523) সামঞ্জস্যপূর্ণ। শুধু Aus-এ Fig. 5 RMSE (835) HTML test (817.6) থেকে আলাদা; 835-এর উৎস অজানা (কাছাকাছি: stack CV RMSE 836.03)। (seed-এর "Boro RMSE একই, R² আলাদা ⇒ অন্য run" — আংশিক ভুল পাঠ: Boro-র Fig. 5 R² ঠিক, S6 R²-ই outlier।)
- **H-statistic:** code আছে; **HTML-এ সংখ্যা নেই** (`tiff()` দিয়ে file-এ লেখা), `Feature_Interaction.csv` repo-তে নেই ⇒ "Not reported in the provided paper, Supporting Information, or available code."
```text
F3: stacking improvement vs best DRF (RMSE %), (DRF-STK)/DRF
 Aus train: (396.1-404.8)/396.1 = -2.20%
 Aus CV: (870.2-816.0)/870.2 = 6.23%
 Aus test: (829.8-817.6)/829.8 = 1.47%
  best single on TEST = XRT 820.8; stack vs it = 0.39%
  best single on CV = GBM 857.3; stack vs it = 4.82%
 Aman train: (469.3-442.5)/469.3 = 5.71%
 Aman CV: (943.3-926.2)/943.3 = 1.81%
 Aman test: (959.1-948.7)/959.1 = 1.08%
  best single on TEST = DRF 959.1; stack vs it = 1.08%
  best single on CV = DRF 943.3; stack vs it = 1.81%
 Boro train: (575.6-499.1)/575.6 = 13.29%
 Boro CV: (1121.2-1109.2)/1121.2 = 1.07%
 Boro test: (1132.3-1122.0)/1132.3 = 0.91%
  best single on TEST = DRF 1132.3; stack vs it = 0.91%
  best single on CV = DRF 1121.2; stack vs it = 1.07%

F2: implied test R2 from S6 test RMSE and S6 GLM test RMSE/R2 (V = MSE_glm/(1-R2_glm)); R2 = 1 - RMSE^2/V
 Aus: implied test SD=1127.9
   S6 stack test RMSE 817.6 -> implied R2 = 0.475 | S6 printed R2 = 0.475 | Fig5 RMSE 835 -> implied R2 = 0.452 | Fig5 printed R2 = 0.451
 Aman: implied test SD=1433.7
   S6 stack test RMSE 948.7 -> implied R2 = 0.562 | S6 printed R2 = 0.59 | Fig5 RMSE 949 -> implied R2 = 0.562 | Fig5 printed R2 = 0.561
 Boro: implied test SD=1625.6
   S6 stack test RMSE 1122.0 -> implied R2 = 0.524 | S6 printed R2 = 0.514 | Fig5 RMSE 1122 -> implied R2 = 0.524 | Fig5 printed R2 = 0.523

F1: Table 4 vs S6 CV (stack) vs HTML
 Aus: Table4 RMSE,R2=(1109.2, 0.51) | S6 CV=816.0,0.543
 Aman: Table4 RMSE,R2=(926.2, 0.59) | S6 CV=926.2,0.592
 Boro: Table4 RMSE,R2=(816.01, 0.55) | S6 CV=1109.2,0.51
 HTML stack 10-fold CV RMSE: Aus 836.0281, Aman 928.2014, Boro 1112.412 ; HTML metalearner level-one 'training' RMSE: Aus 816.6753 (R2 .5448), Aman 926.2349 (R2 .594169), Boro 1110.015 (R2 .5117)
 (816.6753-816.01)/816.6753=0.08% ; Boro HTML CV MAE 772.5589 vs Table4 'Aus' MAE 773.47 diff 0.91
 Aus HTML 958 base models vs Table4 Boro 958; Boro HTML 188 base models vs Table4 Aus 198

F4: GLM lambda: S4 lambda.1se==lambda.max -> [('Aus', True), ('Aman', True), ('Boro', True)]

MAE range: paper text 637-773; Table4 MAE values 622.31, 647.44, 773.47; HTML stack CV MAE Aus 637.33 / Aman 648.44 / Boro 772.56; HTML test MAE 652.09/668.71/786.52

F9: PFI relative importance of field duration vs N: Aus 221.8/361.5=61.4%
Table S7 K check: 176.3/361.5 = 48.8%
Section 3.2: min Table-4 MAE 622.31 < 637 stated minimum: diff 14.690000000000055
Unions: (paper) 78+247+224 = 549 ; data rows 677+6664+5809 = 13150 ; vs 13137 diff 13
Aus train share: 526/677=77.7%, Aman 5305/6664=79.6%, Boro 4626/5809=79.6%

S7 Aus n features 41 | importance>10: 17 | top5: [('N-rate', 361.5, 100.0), ('Crop Types (Local/HYV/Hybrid)', 236.4, 65.4), ('Field Duration', 221.8, 61.3), ('P-rate', 201.8, 55.8), ('K-rate', 176.3, 48.8)]
  importance%% != loss/max*100 (tol .15): [] | window features (NDVI/TEMP/RAINFALL) in top 20: ['NDVI, MAY-09-2014', 'NDVI, MAY-26-2014', 'NDVI, JUN-10-2014', 'NDVI, JUL-12-2014', 'NDVI, JUN-26-2014', 'RAINFALL, JUL-12-2014']
  field duration loss/SD ratio: [('Field Duration', 14.9)] | Water Regime: [('Water Regime', 0.0, 0.0, 0.0)]
S8 Aman n features 53 | importance>10: 19 | top5: [('Crop Types (Local/HYV/Hybrid)', 328.57, 100.0), ('N-rate', 317.36, 96.6), ('K-rate', 299.44, 91.1), ('P-rate', 272.58, 82.9), ('Field  Duration', 230.46, 70.0)]
  importance%% != loss/max*100 (tol .15): [('Soil Types', 25.9, 26.2), ('exTZONE', 20.2, 20.5), ('TEMP, DEC-19-2014', 15.6, 15.9), ('NDVI, JUL-12-2014', 14.9, 15.3), ('Soil pH', 14.2, 14.5)] | window features (NDVI/TEMP/RAINFALL) in top 20: ['TEMP, DEC-19-2014', 'NDVI, JUL-12-2014', 'RAINFALL, JUL-12-2014', 'TEMP, JUL-24-2014', 'RAINFALL, SEP-30-2014', 'TEMP, AUG-13-2014', 'RAINFALL, JUL-24-2014', 'NDVI, JUL-24-2014', 'NDVI, AUG-13-2014']
  field duration loss/SD ratio: [('Field  Duration', 15.6)] | Water Regime: [('Water Regime', 1.26, 9.49, 0.0)]
S9 Boro n features 54 | importance>10: 18 | top5: [('N-rate', 440.62, 100.0), ('K-rate', 370.32, 84.0), ('P-rate', 340.16, 77.2), ('Crop Types (Local/HYV/Hybrid)', 237.78, 54.0), ('Field  Duration', 210.03, 47.7)]
  importance%% != loss/max*100 (tol .15): [] | window features (NDVI/TEMP/RAINFALL) in top 20: ['NDVI, FEB-02-2015', 'RAINFALL, MAR-06-2015', 'RAINFALL, FEB-02-2015', 'NDVI, JAN-17-2015', 'TEMP, DEC-19-2014', 'RAINFALL, APR-23-2015', 'NDVI, APR-07-2015', 'NDVI,  JAN-01-2015', 'TEMP, MAR-06-2015']
  field duration loss/SD ratio: [('Field  Duration', 13.8)] | Water Regime: [('Water Regime', 0.0, 15.48, 0.0)]

PFI rank gaps (diff, pooled SD of the two SDs, z) - SD is across permutations, not across data resamples; indicative only
Aman crop vs N: (11.20999999999998, 25.3, 0.44)
Aman K vs P: (26.860000000000014, 26.2, 1.03)
Aman P vs FD: (42.119999999999976, 25.4, 1.66)
Aus N vs crop: (125.1, 28.2, 4.43)
Aus crop vs FD: (14.599999999999994, 23.2, 0.63)
Aus P vs K: (25.5, 15.0, 1.7)
Boro N vs K: (70.30000000000001, 38.7, 1.82)
Boro K vs P: (30.159999999999968, 29.6, 1.02)
Boro crop vs FD: (27.75, 24.5, 1.13)
```

## 9 ও 10. Simple fair baseline + grouped evaluation — **OUR OWN CHECK with simpler models, not a reproduction of the paper**
সমান predictor set; আমাদের নিজস্ব random 80/20 split (seed 42); category one-hot; numeric median-fill; scaling শুধু train-statistics-এ। Paper-এর test ≠ আমাদের test, তাই সংখ্যা সরাসরি তুলনীয় নয়।
```text
OUR OWN CHECKS - simpler models, NOT a reproduction of the paper (no AutoML retraining).

== CHECK 3: simulated row-level random 80/20 split (the real split files train_data.csv/test_data.csv are NOT in the repo)
aus: test rows sharing a union with >=1 train row: mean 97.0% (min 89.6, max 100.0) | sharing a household-like key (first 2 tokens of Index): mean 73.9%
aman: test rows sharing a union with >=1 train row: mean 99.8% (min 99.1, max 100.0) | sharing a household-like key (first 2 tokens of Index): mean 85.1%
boro: test rows sharing a union with >=1 train row: mean 99.7% (min 99.2, max 100.0) | sharing a household-like key (first 2 tokens of Index): mean 82.6%

== CHECK 9 aus (n=677, train 541, test 136), our own random 80/20 split seed 42
  intercept-only     test RMSE=  1133.9  R2=-0.000
  OLS                test RMSE=   959.7  R2=0.284
  OLS + N_rate^2     test RMSE=   955.8  R2=0.290
  RidgeCV            test RMSE=   970.4  R2=0.268
  RandomForest(300)  test RMSE=   799.5  R2=0.503
== CHECK 10 aus RF(150, default) 5-fold: row-random R2=0.461 (sd 0.008) RMSE=877 | leave-union-out R2=0.129 (sd 0.018) RMSE=1115 | R2 drop=0.332

== CHECK 9 aman (n=6664, train 5331, test 1333), our own random 80/20 split seed 42
  intercept-only     test RMSE=  1472.0  R2=-0.003
  OLS                test RMSE=  1159.1  R2=0.378
  OLS + N_rate^2     test RMSE=  1159.0  R2=0.378
  RidgeCV            test RMSE=  1159.9  R2=0.377
  RandomForest(300)  test RMSE=   958.4  R2=0.575
== CHECK 10 aman RF(150, default) 5-fold: row-random R2=0.574 (sd 0.002) RMSE=946 | leave-union-out R2=0.276 (sd 0.007) RMSE=1234 | R2 drop=0.298

== CHECK 9 boro (n=5809, train 4647, test 1162), our own random 80/20 split seed 42
  intercept-only     test RMSE=  1662.4  R2=-0.000
  OLS                test RMSE=  1489.1  R2=0.197
  OLS + N_rate^2     test RMSE=  1483.9  R2=0.203
  RidgeCV            test RMSE=  1489.6  R2=0.197
  RandomForest(300)  test RMSE=  1157.5  R2=0.515
== CHECK 10 boro RF(150, default) 5-fold: row-random R2=0.513 (sd 0.003) RMSE=1114 | leave-union-out R2=0.010 (sd 0.022) RMSE=1588 | R2 drop=0.503
```
**Check 9 ফল:** OLS test R² Aus 0.284, Aman 0.378, Boro 0.197 (N² যোগ করলে 0.290/0.378/0.203); RF(300) 0.503/0.575/0.515। **"ML beats linear" ধরে রাখে**, কিন্তু gap paper-এর intercept-only GLM (R² ≈ 0) তুলনার চেয়ে ছোট। **Seed F4: REVISED** (GLM কার্যত intercept-only ✔; S4-এর "Ridge λ = λ.min" বিরোধ নয় — HTML-এ Ridge λ = 14,082 = λ.min = λ-path-এর শেষ; সমস্যা λ-path-এ ছোট λ-র অভাব)।

**Check 10 (RF 150 trees, default; 5-fold; 3 repeat গড়):**
| Season | row-random R² | leave-union-out R² | R² drop |
|---|---|---|---|
| Aus | 0.461 | 0.129 | 0.332 |
| Aman | 0.574 | 0.276 | 0.298 |
| Boro | 0.513 | 0.010 | 0.503 |

row-random ফল paper-এর R² (0.45–0.59)-এর কাছাকাছি; union-group করলে অনেক কমে। সতর্কতা: leave-union-out-এ union-নির্ভর feature নতুন union-এ নতুন মান — আংশিক "সঠিক spatial difficulty", আংশিক এই feature-সেটের সীমা; Rule 5: random split ≠ unseen-area test। **Seed F10: verified + পরিমাণ-সূচক।** Confidence: মাঝারি।

## 11. অতিরিক্ত যাচাই
**Moran's I (union-mean, 8-NN, 999 perm)** — Fig. 4 "no distinct spatial pattern":
```text
aus union-mean yield: n=78 Moran I (8-NN)=0.005 perm p=0.930 (E[I]=-1/(n-1)=-0.013)
aus union-mean Total_GWP: n=78 Moran I (8-NN)=0.047 perm p=0.345 (E[I]=-1/(n-1)=-0.013)
aman union-mean yield: n=246 Moran I (8-NN)=0.193 perm p=0.001 (E[I]=-1/(n-1)=-0.004)
aman union-mean Total_GWP: n=246 Moran I (8-NN)=0.115 perm p=0.002 (E[I]=-1/(n-1)=-0.004)
boro union-mean yield: n=224 Moran I (8-NN)=0.228 perm p=0.001 (E[I]=-1/(n-1)=-0.004)
boro union-mean Total_GWP: n=224 Moran I (8-NN)=0.161 perm p=0.001 (E[I]=-1/(n-1)=-0.004)
```
**§3.1 ANOVA পুনর্গণনা:**
```text
yield by season: F=2948.4 p=0 (paper: 3012)
Total_GWP by season: F=2365.9 p=0 (paper: 2364)
aus yield by crop type: F=27.6 p=3.06e-12 groups=['HYV', 'Local', 'Hybrid']
aman yield by crop type: F=733.7 p=1.07e-288 groups=['HYV', 'Local', 'Hybrid']
boro yield by crop type: F=116.6 p=6.46e-27 groups=['HYV', 'Hybrid']
GWP mean by season: {'aus': 966, 'aman': 4543, 'boro': 3753} yield mean: {'aus': 3105, 'aman': 3557, 'boro': 5535}
GWP by crop type per season (mean): {'aus': {'HYV': 983.0, 'Hybrid': 1135.0, 'Local': 915.0}, 'aman': {'HYV': 4655.0, 'Hybrid': 4622.0, 'Local': 4040.0}, 'boro': {'HYV': 3734.0, 'Hybrid': 3862.0}}
```
**Breakdown proxy (reproduction নয়):**
```text
Share of unions whose union-mean feature is ABOVE the all-row mean (a naive 'feature-value' proxy for sign of breakdown contribution); NOT a reproduction of break_down
aus paper %% unions positive: {'N': 51, 'P': 42, 'K': 41, 'GD': 30, 'crop': 51} | proxy (union mean > global mean): {'N': np.float64(50.0), 'P': np.float64(62.8), 'K': np.float64(50.0), 'GD': np.float64(48.7)} | unions with local share < overall local share (32.9%): 59.0% ; unions with hybrid share > overall (3.1%): 12.8% ; hybrid-majority unions: 3.8%
aman paper %% unions positive: {'N': 57, 'P': 53, 'K': 37, 'GD': 50, 'crop': 70} | proxy (union mean > global mean): {'N': np.float64(50.8), 'P': np.float64(54.5), 'K': np.float64(47.2), 'GD': np.float64(50.8)} | unions with local share < overall local share (18.1%): 73.6% ; unions with hybrid share > overall (3.6%): 18.7% ; hybrid-majority unions: 2.4%
boro paper %% unions positive: {'N': 74.6, 'P': 55.4, 'K': 55.8, 'GD': None, 'crop': 18} | proxy (union mean > global mean): {'N': np.float64(50.4), 'P': np.float64(44.2), 'K': np.float64(54.9), 'GD': np.float64(46.0)} | unions with local share < overall local share (0.0%): 0.0% ; unions with hybrid share > overall (14.4%): 25.9% ; hybrid-majority unions: 11.6%
```
**Emission intensity বনাম N (F7):**
```text
aus Emission_Intensity vs GWP/YIELD: corr=0.999 ratio median=1.129 IQR=(1.114,1.145) | EI mean 0.424
   corr(Emission_Intensity,N_rate)=-0.061 | corr(GWP/YIELD,N_rate)=-0.041
   corr(Emission_Intensity,P_rate)=-0.210 | corr(GWP/YIELD,P_rate)=-0.199
   corr(Emission_Intensity,K_rate)=-0.123 | corr(GWP/YIELD,K_rate)=-0.114
   corr(Emission_Intensity,GD)=0.050 | corr(GWP/YIELD,GD)=0.049
   corr(Emission_Intensity,YIELD)=-0.668 | corr(GWP/YIELD,YIELD)=-0.658
                N        Y      GWP  EIcalc    EI
N_rate                                           
Q1 low N    28.87  2385.76   752.59    0.34  0.39
Q2          58.21  3061.89   918.37    0.31  0.34
Q3          77.03  3291.86  1035.23    0.31  0.34
Q4 high N  112.09  3684.26  1157.61    0.31  0.35
aman Emission_Intensity vs GWP/YIELD: corr=1.000 ratio median=1.192 IQR=(1.182,1.200) | EI mean 1.978
   corr(Emission_Intensity,N_rate)=-0.123 | corr(GWP/YIELD,N_rate)=-0.118
   corr(Emission_Intensity,P_rate)=-0.164 | corr(GWP/YIELD,P_rate)=-0.162
   corr(Emission_Intensity,K_rate)=-0.143 | corr(GWP/YIELD,K_rate)=-0.141
   corr(Emission_Intensity,GD)=0.074 | corr(GWP/YIELD,GD)=0.073
   corr(Emission_Intensity,YIELD)=-0.531 | corr(GWP/YIELD,YIELD)=-0.532
                N        Y      GWP  EIcalc    EI
N_rate                                           
Q1 low N    28.35  2771.94  4247.18    1.51  1.82
Q2          65.27  3522.06  4401.24    1.19  1.42
Q3          92.31  3766.13  4622.08    1.15  1.37
Q4 high N  134.36  4167.03  4899.54    1.11  1.31
boro Emission_Intensity vs GWP/YIELD: corr=1.000 ratio median=1.148 IQR=(1.135,1.161) | EI mean 0.905
   corr(Emission_Intensity,N_rate)=0.034 | corr(GWP/YIELD,N_rate)=0.044
   corr(Emission_Intensity,P_rate)=-0.006 | corr(GWP/YIELD,P_rate)=0.002
   corr(Emission_Intensity,K_rate)=0.059 | corr(GWP/YIELD,K_rate)=0.063
   corr(Emission_Intensity,GD)=0.033 | corr(GWP/YIELD,GD)=0.029
   corr(Emission_Intensity,YIELD)=-0.583 | corr(GWP/YIELD,YIELD)=-0.578
                N        Y      GWP  EIcalc    EI
N_rate                                           
Q1 low N    67.23  5250.92  3270.52    0.61  0.72
Q2         113.35  5501.98  3633.48    0.65  0.75
Q3         145.76  5721.88  3903.11    0.67  0.76
Q4 high N  197.31  5709.90  4207.01    0.73  0.83
```
**স্টেটাস:** Check 1 ✔ (row-unit অস্পষ্ট), 2 ✔ (union-centroid নিশ্চিত), 3 ⚠ (simulation), 4 ✔ (13,150 বনাম 13,137), 5 ✔ (season-class), 6 ✘ (reproduce করা যায়নি), 7 ✔ (S5 = union-mean), 8 ✔ (F1 verified; F2 revised), 9 ✔, 10 ✔।
