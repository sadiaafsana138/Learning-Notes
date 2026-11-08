# Observation register (সব page-এর section G একসাথে; `work/scripts/build_registers.py` দিয়ে auto-generated)

মোট observation: 45 | Potential concern: 13, Confirmed issue: 21, Unresolved question: 9, Research opportunity: 2

| # (page.n) | কী পেলাম | প্রমাণ | ধরন | page |
|---|---|---|---|---|
| 1.1 | Abstract-এ GHG যে **modeled (CCAFS-MOT)**, measured নয় — তা বলা নেই | p1 abstract; p3 §2.2 ("estimated emissions are based solely on modeled outputs") | Potential concern  | [p01](../pages/page-01.md) |
| 1.2 | Abstract-এর causal ভাষা ("influencing", "impact") vs p12 Limitation ("do not explain why things happen") | p1 abstract vs p12 | Potential concern  | [p01](../pages/page-01.md) |
| 1.3 | "IPCC, 2019" reference-এর title = "Annex IV: reviewers of the IPCC special report…" (reviewer list); "one-third" claim support করে না | p1 ¶1; ref list p14 | Confirmed issue  | [p01](../pages/page-01.md) |
| 1.4 | Suarez-Gutierrez 2018 = ইউরোপের গ্রীষ্মকালীন তাপমাত্রা; net-negative-emissions claim-এর সাথে মিল নেই | p1 ¶2; ref list p16 | Confirmed issue  | [p01](../pages/page-01.md) |
| 1.5 | Gaihre 2015 = N₂O/NO (urea deep placement); text-এ CH₄ কমানোর claim | p1 ¶2; ref list | Confirmed issue  | [p01](../pages/page-01.md) |
| 1.6 | "one-third" (food systems) vs "15%" (agri food system) — scope ব্যাখ্যা নেই | p1 ¶1 | Potential concern  | [p01](../pages/page-01.md) |
| 1.7 | Abstract-এ "outperformed all individual models" — S6 test gap ছোট (Aus: XRT 820.8 vs stack 817.6 = 0.39%); দেখুন p9 | Abstract; SI Table S6 (si.txt p12); script `work/scripts/check_arith_F1_F4.py` | Potential concern  | [p01](../pages/page-01.md) |
| 1.8 | Abstract-এ ৩টা season-এর মধ্যে Aus-কে "transition from winter to rainy season" বলা হয়েছে, কিন্তু p11 Discussion-এ Aus "rainfed", "pre-monsoon" বলা হয়েছে; Data-তে Aus `Water regime` = "Rainfed, wet season" (677/677) | p1; p11; `aus_data_all.csv` | Unresolved question (সংজ্ঞা সামান্য ঢিলে)  | [p01](../pages/page-01.md) |
| 2.1 | Wang et al. 2018c = "cognitive vision method for insect pest image segmentation", stacking-এর support নয় | p2 ¶stacking; refs p16 | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.2 | "Ahmed et al. 2021a/2021b" text-এ; ref list-এ ২০২১-এর একটাই Ahmed entry | p2 ¶XAI; p9; refs p14 | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.3 | D'Orazio et al. 2019 ref list-এ দু'বার (Prasad/Prasady) | refs p14 | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.4 | Rudin 2019 interpretable-model argue করে; paper উল্টো পথে, আলোচনা নেই | p2 ¶XAI; refs | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.5 | Song 2020 = cross-site transportability; paper কখনো test করেনি | p2; refs; পুরো paper | Research opportunity  | [p02](../pages/page-02.md) |
| 2.6 | Row-unit অস্পষ্ট: 6500 households (p2) vs 13,137 farmers (p5) vs data 13,150 rows | p2 §2.1.1; p5 §3.1; `work/check01_07.out` (Check 1,4) | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.7 | Union-এর ভেতরে সব environmental value 100% একই → union-centroid assignment | `work/scripts/check01_07_data.py` output (Check 2) | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.8 | NDVI "finest (250 m)" বনাম Table 1 DEM 90 m | p2 §2.1.2; p3 Table 1 | Confirmed issue  | [p02](../pages/page-02.md) |
| 2.9 | 12 km → 250 m resample = false precision | p2; p3 §2.1.2.2 | Potential concern  | [p02](../pages/page-02.md) |
| 2.10 | Irrigation: p2 "extracted", p12 "excluded", code-এ `Water_regime` predictor (Check 5: Aus/Boro-তে প্রায় ধ্রুবক) | p2; p12; `yield_aus_autoML.Rmd:115`; SI S8/S9 | Confirmed issue (inconsistent reporting)  | [p02](../pages/page-02.md) |
| 2.11 | Field duration, unit conversion, sampling weights, research question — কোথাও নেই | p2, পুরো paper | Unresolved question  | [p02](../pages/page-02.md) |
| 2.12 | No hypotheses / objectives-এ unseen-area prediction নেই | p2 ¶study | Research opportunity  | [p02](../pages/page-02.md) |
| 3.1 | CCAFS-MOT input-এ fertilizer rate → N/P/K–GWP correlation আংশিক circular | p3 §2.2; SI S5 (Aus N r=0.816); `work/check07b.out` | Confirmed issue  | [p03](../pages/page-03.md) |
| 3.2 | Table 1: "crop type (Boro/Aman/Boro)" — Aus বাদ | p3 Table 1 | Confirmed issue  | [p03](../pages/page-03.md) |
| 3.3 | Table 1-এ ERA-Interim source URL = lpdaac.usgs.gov (MODIS DAAC) | p3 Table 1 | Confirmed issue  | [p03](../pages/page-03.md) |
| 3.4 | Fig. 1 caption "circular points"/"district map" বনাম legend triangle/union | p3 Fig. 1 | Potential concern  | [p03](../pages/page-03.md) |
| 3.5 | Soil B raster তৈরি, model-এ B নেই; 31,787 কেন বাছা — অজানা | p3 §2.1.2.3; CSV/Rmd features | Unresolved question  | [p03](../pages/page-03.md) |
| 3.6 | Kriging uncertainty ও soil sampling-year (1996–2014) propagate হয়নি | p3 §2.1.2.3; p12 | Potential concern  | [p03](../pages/page-03.md) |
| 3.7 | Text-এ min/max temp তৈরি, model-এ একটা `t2m` | p3 §2.1.2.2; CSV | Unresolved question  | [p03](../pages/page-03.md) |
| 3.8 | CCAFS-MOT code/CH₄/N₂O/CO₂ আলাদা column নেই — "Not reported in the provided paper, Supporting Information, or available code." | file inventory (`work/code-inventory.md`) | Unresolved question  | [p03](../pages/page-03.md) |
| 3.9 | Aman: CSV `NDVI_205` বনাম `t2m_209`/SI S3 "209" | `yield_aman_autoML.Rmd` feature list; SI S3 | Potential concern  | [p03](../pages/page-03.md) |
| 3.10 | Boro-তে AWD/intermittent irrigation CCAFS-MOT-এ ধরা হয়েছে কিনা অজানা; `Water_regime` Boro-তে সব "Continuous flooding" | `boro_data_all.csv` (Check 5); p11 | Potential concern  | [p03](../pages/page-03.md) |
| 3.11 | Cloud/quality masking of NDVI report নেই | p3 | Unresolved question  | [p03](../pages/page-03.md) |
| 4.1 | Row-level random 80/20 split + row-level 10-fold CV; কোনো union/household group নেই | p4 §2.3; `yield_aus_autoML.Rmd:56-57,200`; Aman:213; Boro:216 | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.2 | Split code ও `train_data.csv/test_data.csv` repo-তে নেই | file inventory | Unresolved question  | [p04](../pages/page-04.md) |
| 4.3 | Paper-এর পদ্ধতি অনুযায়ী simulation: test row-এর ৯৭–৯৯.৮% union train-এ আছে (Aus 97.0, Aman 99.8, Boro 99.7) | `work/check03_09_10.out` (Check 3) | Potential concern (leakage প্রমাণ নয়; আসল split দরকার)  | [p04](../pages/page-04.md) |
| 4.4 | নিজস্ব RF check: row-random R² → leave-union-out R²: Aus 0.461→0.129; Aman 0.574→0.276; Boro 0.513→0.010 | Check 10 (`work/check03_09_10.out`) | Potential concern  | [p04](../pages/page-04.md) |
| 4.5 | AutoML setting তিন জায়গায় তিন রকম: tolerance 0.0001 vs 0.001; rounds 2 vs 3; max_models "0" vs commented; MAE (S2) vs RMSE | p4; Rmd:202–207; SI S2 footnote | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.6 | `max_runtime_secs`/`max_models` কোনোটাই না থাকলে H2O default time limit প্রযোজ্য কি না — যাচাই বাকি; "no limit" claim সন্দেহজনক | Rmd:205–207; H2O docs (verify) | Unresolved question  | [p04](../pages/page-04.md) |
| 4.7 | Categorical list (text) বনাম code: line sowing/balanced fert/lime নেই; land type, soil type, drainage, TZONE, texture, Water_regime আছে | p4 ¶1; Rmd `FeatureData` (Aus:109–116) | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.8 | Train size 80%-এর চেয়ে কম: Aus 526/677=77.7%, Aman 5,305/6,664=79.6%, Boro 4,626/5,809=79.6%; কেন বাদ — অজানা | HTML "Null D.o.F." (Aus:525, Aman:5304, Boro:4625) | Unresolved question  | [p04](../pages/page-04.md) |
| 4.9 | Scaling আলাদাভাবে all/train/test-এ (`scale()` প্রতিবার নিজের mean/SD) — test-এ train-এর mean/SD নয় | `yield_aus_autoML.Rmd:120,127-129`; Aman:133,140-142; Boro:136,143-145 | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.10 | Eq. (1): ŷ-এ subscript i নেই; "households" ভুল unit | p4 Eq.(1) | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.11 | `Water_regime` model predictor (code), অথচ p12 "excluded" | Rmd:115 (Aus), 128 (Aman), 131 (Boro) | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.12 | Fig. 2-তে ALE/স্থানিক correlation/grouped validation নেই; "Partial Dependency" | p4 Fig. 2 | Potential concern  | [p04](../pages/page-04.md) |
| 4.13 | GLM baseline intercept-only (λ.1se = λ.max; train R² = 0.000) — SI S4 আবার "Ridge λ = λ.min" লেখে | SI S4 (λ values); SI S6 | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.14 | Stack-এর CV RMSE (HTML Aus 836.03) বনাম meta-learner level-one metric (816.68) আলাদা stage | HTML `yield_aus_autoML.html` (stacked ensemble CV vs glm training) | Potential concern  | [p04](../pages/page-04.md) |
