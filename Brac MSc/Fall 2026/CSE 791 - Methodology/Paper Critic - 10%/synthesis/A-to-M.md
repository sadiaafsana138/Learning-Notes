# Synthesis A–M — Ahmed et al. (2026), *AutoML and XAI for rice production systems* (Ecol. Inform. 97, 103885)

> সব সংখ্যা paper, SI, CSV বা HTML থেকে নেওয়া অথবা `work/scripts/` দিয়ে হিসাব-করা (বিস্তারিত: [code-audit](../registers/code-audit.md)). "Our own check" = আমাদের সরল model/পরিসংখ্যান, paper-এর reproduction নয়।

## A. Research overview

- **সমস্যা:** বাংলাদেশে ধানের (Aus/Aman/Boro) yield খামারে খামারে ও মৌসুমে মৌসুমে অনেক বদলায়; কোন factor কতটা জড়িত এবং কোথায় — তা পরিষ্কার নয়। সাথে ধান-জমির GHG নির্গমন।
- **Motivation:** yield gap কমানো, খাদ্য-নিরাপত্তা, GHG mitigation (p1–2)।
- **Gap (লেখকদের দাবি):** stacking ensemble ফসল-yield-এ কম ব্যবহৃত; XAI বাংলাদেশের ধানে প্রয়োগ হয়নি; আগের কাজ replicable নয় (p2)।
- **Objectives (আমাদের পাঠে — লিখিত নেই):** (১) AutoML দিয়ে তিন season-এর yield predict; (২) PFI/PDP/ALE/breakdown দিয়ে factor ব্যাখ্যা; (৩) union-গড় breakdown map; (৪) modeled GHG-র সাথে factor-গুলোর GW correlation। **কোনো স্পষ্ট research question/hypothesis নেই; unseen-area prediction objective নয়** (2.12)।
- **Implicit research questions:** RQ1 কোন model সবচেয়ে ভালো? RQ2 কোন factor yield-এর জন্য গুরুত্বপূর্ণ? RQ3 factor-এর প্রভাব জায়গাভেদে কেমন? RQ4 GHG-র সাথে factor-এর সম্পর্ক জায়গাভেদে কেমন?
- **Contributions (দাবি):** H2O AutoML stack + DALEX XAI pipeline বাংলাদেশের ধানে; union-গড় local attribution map; GHG-factor GW correlation; GitHub code।

## B. Dataset inventory table

| Variable | Category | Source | Spatial scale | Temporal scale | Role in model |
|---|---|---|---|---|---|
| `YIELD` (kg/ha) | Target | BIHS 2015 (farmer-reported; IFPRI Dataverse) | plot/household → **union-centroid** | 2014–15 season | **Target** (রেঞ্জ: Aus 247–5,487; Aman 112–8,230; Boro 0–9,259) |
| `Total_GWP` (kg CO₂e/ha), `Emission_Intensity` | GHG (modeled) | CCAFS-MOT (R version) | union-centroid | season | Yield-model-এ নয়; GW correlation-এ; Fig. S7 PFI (code নেই) |
| `GD` (field duration, দিন) | Management | BIHS (সংজ্ঞা অজানা) | household | season | Predictor; PFI শীর্ষ ৫ |
| `N_rate`, `P_rate`, `K_rate` (kg/ha) | Management | BIHS (self-report; local→metric conversion অজানা) | household | season | Predictor; PFI শীর্ষ ৫ |
| `Crop_Types` (Local/HYV/Hybrid) | Management | BIHS | household | season | Predictor (categorical) |
| `Manure` | Management | BIHS | household | season | Predictor |
| `pH, SOC, N, P, K, S, Zn` | Soil | SRDI 31,787/50,000 point → kriging (gstat) | 250 m (union-এ ধ্রুব) | সংগ্রহ 1996–2014 | Predictor |
| `DEM` | Terrain | SRTM 90 m → 250 m | 250 m | স্থির | Predictor |
| `NDVI_*` (Aus 7; Aman 11; Boro 12 তারিখ) | Remote sensing | MODIS MOD13Q1 16-day | 250 m (union-এ ধ্রুব) | 16-day, 2014–15 | Predictor |
| `t2m_*`, `tp_*` (7/11/11 তারিখ) | Climate | ERA-Interim 12 km → TPS 250 m | 12 km → 250 m | 16-day average | Predictor |
| `LT_Class`, `General_Soil_type`, `DRC_Class`, `TZONE_Class` (exTZONE), `Soil_texture` | Land/soil classes | উৎস paper-এ নেই ("Not reported…") | অজানা | স্থির | Predictor (categorical) |
| `Water_regime` | Class | উৎস অজানা (Aus সব Rainfed; Boro সব Continuous flooding; Aman 6,614 + 50) | — | season | Predictor; importance ≈ 0% |

## C. Full workflow (raw data → conclusions)

1. **Raw data:** BIHS 2015 (≈6,500 HH, 325 PSU) + SRDI soil + SRTM + MODIS NDVI + ERA-Interim।
2. **Processing:** 250 m grid-এ resample (TPS, kriging); union-centroid-এ extraction; unit conversion; outlier removal (3 SD + domain) — কত row বাদ: অজানা (Aus train 526/677)।
3. **Features:** numeric 33/45/46 + categorical 8; `scale()` আলাদা প্রতি data-frame-এ।
4. **Models:** H2O AutoML (10-fold CV, RMSE), GLM/DRF/XRT/GBM/XGB/DNN → stacked ensemble (All models), meta = non-negative GLM।
5. **Evaluation:** random 80/20 split; Table 4 (CV), Fig. 5 (test), SI S6।
6. **XAI:** PFI + PDP/ALE (train data); local breakdown (ভিন্ন saved model, union data) → union-গড় map।
7. **Spatial:** Fig. 4 maps, Fig. 8 maps।
8. **GHG:** CCAFS-MOT → Total_GWP → GW Pearson correlation (union-mean) → Fig. 9; Fig. S7 PFI।
9. **Conclusions:** N/P/K/variety/FD গুরুত্বপূর্ণ; "better nutrient management → higher yield, lower GHG"; policy সুপারিশ।

## D. Model performance table (Aus / Aman / Boro)

**সূত্র: SI Table S6 (train / CV / test)।** CV = H2O stack-এর meta-learner level-one metric (stack-এর নিজস্ব CV আলাদা — নিচে)। MAE: শুধু stack-এর জন্য HTML থেকে।

| Season | Model | Train RMSE | CV RMSE | Test RMSE | Train R² | CV R² | Test R² |
|---|---|---|---|---|---|---|---|
| **Aus** | GLM | 1210.4 | 1211.7 | 1133.5 | 0.000 | −0.002 | −0.010 |
| | DRF | 396.1 | 870.2 | 829.8 | 0.893 | 0.483 | 0.459 |
| | XRT | 424.7 | 883.7 | 820.8 | 0.877 | 0.467 | 0.471 |
| | GBM | 437.6 | 857.3 | 824.5 | 0.869 | 0.498 | 0.466 |
| | XGBoost | 397.6 | 885.1 | 840.2 | 0.892 | 0.465 | 0.445 |
| | DNN | 452.5 | 899.3 | 961.6 | 0.860 | 0.456 | 0.273 |
| | **Stack** | 404.8 | 816.0 | 817.6 | 0.888 | 0.543 | 0.475 |
| **Aman** | GLM | 1453.9 | 1454.0 | 1433.7 | 0.000 | 0.000 | 0.000 |
| | DRF | 469.3 | 943.3 | 959.1 | 0.896 | 0.579 | 0.553 |
| | XRT | 493.2 | 945.1 | 966.4 | 0.885 | 0.577 | 0.546 |
| | GBM | 463.8 | 946.5 | 970.4 | 0.898 | 0.576 | 0.542 |
| | XGBoost | 452.5 | 955.4 | 998.3 | 0.903 | 0.568 | 0.515 |
| | DNN | 834.8 | 1014.2 | 1009.2 | 0.670 | 0.513 | 0.505 |
| | **Stack** | 442.5 | 926.2 | 948.7 | 0.907 | 0.592 | **0.590 ⚠** |
| **Boro** | GLM | 1588.5 | 1588.9 | 1625.6 | 0.000 | 0.000 | 0.000 |
| | DRF | 575.6 | 1121.2 | 1132.3 | 0.869 | 0.502 | 0.515 |
| | XRT | 619.2 | 1130.3 | 1137.4 | 0.848 | 0.494 | 0.510 |
| | GBM | 386.7 | 1131.4 | 1147.0 | 0.941 | 0.493 | 0.502 |
| | XGBoost | 481.1 | 1145.7 | 1174.1 | 0.908 | 0.480 | 0.478 |
| | DNN | 987.8 | 1241.5 | 1188.2 | 0.613 | 0.389 | 0.466 |
| | **Stack** | 499.1 | 1109.2 | 1122.0 | 0.901 | 0.510 | **0.514 ⚠** |

⚠ = S6 test R² নিজের RMSE-র সাথে অসঙ্গত (implied: Aman 0.562, Boro 0.524) — F2।

**Stack-এর অন্যান্য সূত্র (HTML = AutoML script-এর output):**

| Season | Table 4 (paper) | HTML stack 10-fold CV RMSE/MAE/RMSLE | HTML meta-learner level-one RMSE/R² | HTML test RMSE/MAE | Fig. 5 (RMSE/R²/EVar) |
|---|---|---|---|---|---|
| Aus | "Boro" 816.01/622.31/0.35/0.55 (**Aus-এর মান**) | 836.03/637.33/0.352 | 816.68/0.545 | 817.64/652.09 | 835/0.451/0.453 |
| Aman | 926.20/647.44/0.34/0.59 | 928.20/648.44/0.342 | 926.23/0.594 | 948.71/668.71 | 949/0.561/0.562 |
| Boro | "Aus" 1109.2/773.47/0.43/0.51 (**Boro-র মান**) | 1112.41/772.56/0.432 | 1110.02/0.512 | 1122.67/786.52 | 1122/0.523/0.524 |

**Our own checks (সরল মডেল; নিজস্ব random 80/20, seed 42; paper-এর test ≠ আমাদের test):**

| Season | n | Intercept-only R² | OLS R² (RMSE) | OLS+N² R² | RidgeCV R² | RF(300) R² (RMSE) | **RF row-random 5-fold R²** | **RF leave-union-out R²** |
|---|---|---|---|---|---|---|---|---|
| Aus | 677 | −0.000 | 0.284 (959.7) | 0.290 | 0.268 | 0.503 (799.5) | 0.461 | **0.129** |
| Aman | 6,664 | −0.003 | 0.378 (1159.1) | 0.378 | 0.377 | 0.575 (958.4) | 0.574 | **0.276** |
| Boro | 5,809 | −0.000 | 0.197 (1489.1) | 0.203 | 0.197 | 0.515 (1157.5) | 0.513 | **0.010** |

**মূল পাঠ:** (১) stack বনাম DRF test gap 0.9–1.5% (F3); (২) intercept-only GLM বাদ দিলে সত্যিকারের linear baseline R² 0.20–0.38, RF 0.50–0.58 — "ML beats linear" ধরে রাখে, gap ছোট; (৩) union-group করলে R² অনেক কমে (Boro ≈ 0)।

## E. XAI findings — এবং কতটা justified

| Finding | লেখকদের দাবি | Justified? | কারণ |
|---|---|---|---|
| শীর্ষ-৫ predictor: N, P, K rate, crop type, field duration (PFI) | সব season-এ | **আংশিক ✔** — সেট ঠিক (S7–S9, 17/19/18 >10%); ক্রম নড়বড়ে (Aman crop vs N z=0.44) | PFI train-data-য়; correlated feature; predictive importance ≠ causal |
| "N সব season-এ most important" (p10) | N প্রধান | **✘ Aman-এ** | Aman PFI শীর্ষ crop type; p8 নিজেই "crop type most critical in Aman" |
| PD/ALE: N, P, K ধনাত্মক, non-linear | Fig. 7 | **✔ (গুণগত)** | train-data; sparse উচ্চ-N; CI নেই |
| Field duration-এর marginal effect negligible | Fig. 7 | **✔ (PDP-তে)** কিন্তু PFI 48–70% — **অমীমাংসিত** | interaction/proxy; H-statistic অপ্রকাশিত |
| "Stack model additive" | PD ≈ AL | **✘ অপ্রমাণিত** | PD≈AL ≠ additivity; Boro crop type-এ PD vs AL ফারাক; `iml::Interaction` চালিয়েও report নেই |
| Breakdown: union-wise %-positive contribution | Fig. 8 | **আংশিক** | মূলত feature-মানের পার্থক্য (Aman crop type: local-কম union 73.6% ≈ ">70%"); effect-heterogeneity নয়; ভিন্ন saved model |
| "Local XAI overcomes GW regression limits" | Discussion | **✘ অসমর্থিত** | তুলনা নেই; ভিন্ন জিনিস মাপে |

## F. GHG findings এবং validity

| Finding | Validity |
|---|---|
| GWP ঋতুভেদে ভিন্ন, Aus সবচেয়ে কম (966 বনাম Aman 4,543, Boro 3,753; ANOVA F = 2365.9 ≈ paper 2364) | ✔ (ডেটায় মেলে); **কিন্তু modeled** |
| Local < HYV GWP কারণ কম fertilizer | ✔ (Aman local N 44.1 vs HYV 87.5; GWP 4,040 vs 4,655, t = 10.7) |
| N/P/K ধনাত্মক GHG-র সাথে (GW correlation) | ধারণাগতভাবে **circular** (CCAFS-MOT input); union-mean ecological r (S5); P/K ≈ N-ছায়া (partial r ≈ 0) |
| "moderate to strongly positive across seasons" | **✘ Aman-এ** (S5 Aman ≤ 0.277) |
| FD–GHG: Aus weak (§3.6) | **✘** — Boro weak (S5: 0.058) |
| HYV ও hybrid-এর GHG-তে significant পার্থক্য নেই | **আংশিক** — শুধু Aman (Aus +151, Boro +127, row-level p < 0.001) |
| "Better nutrient management → higher yield, lower GHG" | **✘ বিশ্লেষিত নয়**; intensity: Aus/Aman কমে, Boro বাড়ে (our check) |
| GHG-model PFI (Fig. S7) | **অনুপলব্ধ** — text-এ উল্লিখিত নয়, code/performance নেই; Aus-এ N-rate শীর্ষে নেই (S5-এর সাথে প্রশ্ন) |

## G. Real contributions বনাম standard application

- **Real (মাঝারি):** (১) তিন season জুড়ে বড় (13k) BIHS-ভিত্তিক integrated dataset ও open CSV; (২) AutoML-এর সব model-এর train/CV/test একসাথে দেখানো (S6); (৩) union-গড় local attribution দিয়ে spatial map করার ধারণা (যদিও প্রমাণ দুর্বল); (৪) GitHub-এ code।
- **Standard application:** H2O AutoML; PFI/PDP/ALE/breakdown (DALEX); GW correlation (GWmodel); CCAFS-MOT — সবই বিদ্যমান tool।
- **নতুন বিজ্ঞান-দাবি:** "XAI দিয়ে spatial heterogeneity" — প্রমাণ দুর্বল (union-leakage, ভিন্ন model, feature-মান-নির্ভর attribution)।

## H. Strengths

1. বাস্তব, বড় ও বৈচিত্র্যময় খামার-স্তরের data; তিন season আলাদা।
2. S6-এ সব model-এর train/CV/test স্বচ্ছভাবে দেওয়া; HTML ও CSV প্রকাশিত।
3. Limitations অংশ সৎ ও বিস্তৃত (causation, centroid, sampling bias, water data, CCAFS-MOT, post-hoc)।
4. PFI SD report; PDP + ALE দুটোই; shared legend Fig. 9-এ।
5. EDA-র crop-mix/ANOVA সংখ্যা আমাদের recompute-এ মেলে (HYV 80.8%, local 10.9%, hybrid 8.4%; F = 733.7 Aman)।
6. P/K–GHG সম্পর্কের ব্যাখ্যা (N-এর সাথে একত্রে ব্যবহার) আমাদের partial correlation সমর্থন করে।

## I. Limitations — তিন গ্রুপে

**(১) লেখকদের স্বীকৃত:** BIHS sampling bias; union centroid; water data দুর্বল/বাদ; CCAFS-MOT modeled; post-hoc XAI ≠ causal (PFI inflated, PDP unrealistic, ALE unstable, breakdown order-dependent); soil data পুরোনো; microclimate; Bangladesh-নির্দিষ্ট।

**(২) আমরা প্রমাণসহ যোগ করছি:**
- Row-level random split/CV; union-সংক্রান্ত leakage-সম্ভাবনা (simulation: 97–99.8% test row-এর union train-এ; leave-union-out R² Aus 0.129, Aman 0.276, Boro 0.010)।
- Table 4 Aus/Boro swapped; "CV" = meta-learner level-one metric।
- S6 test R² অসঙ্গত; Fig. 5 Aus RMSE-র উৎস অজানা।
- GLM baseline কার্যত intercept-only।
- PFI/PDP/ALE train-data-য়; per-frame scaling; local XAI ভিন্ন model।
- "Additive" claim অপ্রমাণিত; H-statistic লুকানো।
- Circularity (CCAFS-MOT input); S5 ecological correlation; "Aus weak FD" text-ভুল।
- Conclusion-এর "lower GHG" বিশ্লেষণহীন; policy ↔ limitation অমিল।
- Citation সমস্যা (Suarez-Gutierrez, Wang 2018c, Gaihre@p1, Chen 2011, Sutton-Grier, Sapkota 2014…)।
- Documentation: `Water_regime`, field duration, conversion factors, sampling weights, split, train rows।

**(৩) সন্দেহ (প্রমাণের জন্য আরও তথ্য লাগবে):** আসল split-এ leakage-এর মাত্রা; scaling-অমিলের প্রভাব; H2O default time-limit; CCAFS-MOT-এ P/K input; Boro-র AWD CCAFS-MOT-এ ধরা হয়েছে কিনা; Fig. 8-এর break-পদ্ধতি; 13 row ও 1 union-এর পার্থক্যের কারণ।

## J. Reproducibility assessment

| উপাদান | আছে? | মন্তব্য |
|---|---|---|
| Final feature CSV (3 season) | ✔ | 13,150 row; কিন্তু paper 13,137 |
| Train/test split ফাইল ও code | ✘ | `train_data.csv`, `test_data.csv` নেই |
| AutoML code | ✔ (Rmd) | settings paper-এর সাথে অমিল; hard-coded path; Aus `t.xy` bug |
| Saved models / seeds / H2O version | ✘ | seed=42 শুধু AutoML-এ; model files নেই; কোন run প্রকাশিত অজানা |
| XAI code | ✔ (Rmd) | train-explainer; local XAI ভিন্ন model + `*_union_data_all.csv` অনুপস্থিত |
| GW correlation | আংশিক | শুধু Aman; shapefile নেই |
| CCAFS-MOT code/output | ✘ | CH₄/N₂O/CO₂ আলাদা নেই |
| Feature-processing code (NDVI, kriging, TPS) | ✘ | |
| Fig. S7 (GHG PFI) | ✘ | |
| Raw BIHS ↔ Index mapping | ✘ | household/plot id নথিভুক্ত নয় |
| **মূল্যায়ন:** CSV থেকে modeling আংশিক পুনরায় করা যায় (আমরা সরল মডেলে করেছি), কিন্তু paper-এর সংখ্যা exactly পুনরুৎপাদনযোগ্য নয়। |

## K. Critical observation matrix

| No. | Page/Section | Observation | Evidence | Classification | Why it matters |
|---|---|---|---|---|---|
| 1 | p7 Table 4 / p5 §3.2 | Aus ও Boro row-label অদলবদল (models count সহ) | S6; HTML (958 → Aus; 188 → Boro) | Confirmed issue | Aus "transition" ব্যাখ্যা অসমর্থিত; Table 4 ভুল |
| 2 | p7 Table 4 | "CV" আসলে meta-learner level-one metric | HTML Aus 836.03 vs 816.68 | Potential concern | stage-মিশ্রণ; আশাবাদী |
| 3 | p6 Fig. 5 / S6 | S6 test R² (Aman, Boro) নিজের RMSE-র সাথে অসঙ্গত; Fig. 5 Aus RMSE 835 ≠ HTML 817.6 | `check_arith.out` | Confirmed issue / Unresolved | কোন run/metric — স্পষ্ট নয় |
| 4 | p9 §4 | "1–4% vs DRF": test 0.9–1.5%; Aus XRT-র তুলনায় 0.39% | S6 | Confirmed issue | noise-সীমায় |
| 5 | p4 §2.3 | Row-level random split/CV, union-group নেই; split code নেই | Rmd:56-57,200 | Confirmed issue | "unseen area" নয়; overstated performance |
| 6 | p4 | Simulation: 97–99.8% test row-এর union train-এ | Check 3 | Potential concern | leakage-সম্ভাবনা (প্রমাণ নয়) |
| 7 | p4 | Own RF: R² row-random→leave-union-out: 0.461→0.129; 0.574→0.276; 0.513→0.010 | Check 10 | Potential concern | spatial generalization-এর বাস্তব দুর্বলতা |
| 8 | p4 | GLM baseline কার্যত intercept-only (λ-path) | S4/S6/HTML | Confirmed issue | "ML beats linear" তুলনা অন্যায্য |
| 9 | p5, p7 | PFI/PDP/ALE train-data-য়; "factor" ভুল (difference) | Rmd:849-862 | Confirmed issue | gold-standard নয়; বর্ণনা ভুল |
| 10 | p4 | `scale()` আলাদা প্রতি frame-এ | Rmd:120,127-129 | Confirmed issue | train/test মিল নেই |
| 11 | p4 | AutoML settings তিন উৎসে অমিল | p4, Rmd, S2 | Confirmed issue | reporting |
| 12 | p8 §3.4 | "Additive" claim শুধু PD≈AL; H-statistic computed কিন্তু অপ্রকাশিত | Rmd:1066-1076 | Confirmed issue | claim-সাক্ষ্য অমিল |
| 13 | p8 | Figure-ref ভুল (Fig. 6→7; 7g→8g), "AL = blue" ভুল | text, Fig. 7 | Confirmed issue | পাঠযোগ্যতা |
| 14 | p7–p8 | Field duration: PFI 48–70% কিন্তু PDP/ALE flat | S7–S9; Fig. 7 | Unresolved question | variable-এর ভূমিকা অস্পষ্ট |
| 15 | p7 | Aman TEMP DEC-19 ৮ম; season window ওভারল্যাপ/calendar-fixed | S3; S8 | Confirmed issue / Potential concern | phenology-অমিল |
| 16 | p5 | Local XAI model ≠ AutoML-script model (3 run) | Rmd vs HTML IDs | Confirmed issue | Fig. 8 ↔ Table 4/Fig. 6–7 অসংলগ্ন |
| 17 | p5, p8 | Breakdown "%-positive" ≈ feature-মান; Aman crop type 73.6% proxy | `check_breakdown_proxy.out` | Potential concern | "spatial effect"-এর ভুল ব্যাখ্যা |
| 18 | p3 §2.2, p10 | CCAFS-MOT input-এ fertilizer ⇒ N/P/K–GHG circular | p3; S5 | Confirmed issue (ধারণাগত) | GHG-সিদ্ধান্তের ভিত্তি দুর্বল |
| 19 | p5 | S5 = union-mean (ecological) r | `check07b.out` | Confirmed issue | row-level দুর্বলতর |
| 20 | p9 §3.6 | "Aus weak FD" ভুল; Boro weak (0.058) | S5; Fig. 9 | Confirmed issue | text-text বিরোধ |
| 21 | p8 §3.6, p11 | "moderate to strong" P/K Aman-এ ভুল (≤ 0.277) | S5 | Confirmed issue | অতিরঞ্জন |
| 22 | p11 | P/K–GHG ≈ N-ছায়া (partial r ≈ 0); hybrid-GHG দাবি Aus/Boro-তে বেমানান | `check_ghg_partial.out` | Potential concern | কারণ-ব্যাখ্যা |
| 23 | p12 | Conclusion "higher yield AND lower GHG" — বিশ্লেষণ নেই; intensity Boro-তে বাড়ে | S5; `check_intensity.out` | Confirmed issue | বেশি দাবি |
| 24 | p12 | Limitations ("controlled trials ছাড়া নয়") ↔ Policy (subsidy) অমিল; Abstract causal | p1, p12 | Potential concern | নীতি-ঝুঁকি |
| 25 | p2, p12 | `Water_regime` predictor বনাম "excluded"; Aus/Boro-তে ধ্রুবক | Rmd:115 | Confirmed issue | reporting |
| 26 | p2 | Union-centroid প্রমাণিত; 250 m অর্থহীন; 12 km→250 m | Check 2 | Confirmed issue | spatial claim-সীমা |
| 27 | p2 | Row-unit: 6,500 HH / 13,137 / 13,150; Aman 246 বনাম 247 | Check 4 | Unresolved question | data-identity |
| 28 | p1,p2,p11,p16 | Citation mismatch: IPCC 2019, Suarez-Gutierrez, Gaihre@p1, Wang 2018c, Chen 2011, Sutton-Grier, Sapkota 2014, Ahmed 2021a/b, D'Orazio duplicate | refs | Confirmed issue | বৈধতা |
| 29 | p13 | Ethics "wheat"; "all code and data" অতিরঞ্জিত | p13; inventory | Confirmed issue | বিশ্বাসযোগ্যতা |
| 30 | p2, p15 | Rudin 2019 অনালোচিত; Song 2020 transportability অপরীক্ষিত | refs | Research opportunity | আপনার MSc-র gap |
| 31 | p6 Fig. 4 | "no distinct spatial pattern" — Aman/Boro-তে Moran's I 0.19/0.23 (p≈0.001) | `check_moran.out` | Potential concern | spatial structure আছে |
| 32 | p5 §3.1 | ANOVA "Boro F-value" দু'বার; 27.6 = Aus; Boro F 116.6 vs 123 | `check_anova.out` | Confirmed issue | reporting |

## L. Unresolved questions — কীসে উত্তর মিলবে

- **Repo (GitHub) — যা যোগ হলে মিলবে:** train/test ফাইল ও split code (leakage-সীমা); saved H2O models ও run-log (কোন run paper-এ); `*_union_data_all.csv`, shapefile; CCAFS-MOT code/output; Fig. S7 code; Aus/Boro GW code।
- **Raw data (BIHS Dataverse):** `Index` ↔ household/plot id; 13,137 বনাম 13,150; Aman 246 বনাম 247 union; field duration (harvest − transplanting); unit conversion; Boro-র 12টি শূন্য-yield row।
- **Rmd (R চালিয়ে):** scaling-অমিলের প্রভাব; PFI test-data-য়; H-statistic (`Feature_Interaction.csv`); H2O default `max_runtime_secs`; Aus `t.xy` bug।
- **HTML:** (ইতিমধ্যে ব্যবহৃত) — বাকি: Fig. 5-এর Aus RMSE 835-এর উৎস; H-statistic সংখ্যা (tiff-এ)।
- **SI:** Fig. S1–S4 (আমরা দেখিনি); Fig. S7-এর model/metric; S6 test R² কীভাবে হিসাব।
- **BIHS source/CCAFS-MOT docs:** CCAFS-MOT-এর সূত্র ও input (P/K ঢোকে কি?); BIHS sampling weights; `Emission_Intensity` সংজ্ঞা; `Water_regime`/`TZONE`/`LT`/`DRC` ক্লাসের উৎস।

## M. Peer-review style comments

### Major
1. **Validation design (Data & validation)।** Random row-level split ও CV union/household পরিচয় আলাদা করে না; test-row-এর প্রায় সবটার union train-এ (simulation)। *সহজ কথা:* একই এলাকার ঘর train ও test দু'দিকেই থাকলে model এলাকা "চেনে"; নতুন এলাকার পারফরম্যান্স বোঝা যায় না। Grouped/spatial CV দিন; আমাদের সরল check-এ R² 0.46→0.13 (Aus) পর্যন্ত নামে।
2. **Table 4 ও টেস্ট-মেট্রিক অসঙ্গতি (Reporting/Statistical)।** Aus/Boro label অদলবদল; CV মান আসলে meta-learner level-one; S6 test R² ও Fig. 5 অমিল। *সহজ কথা:* এক সংখ্যা কোন ধাপ (train/CV/test) থেকে — সেটা না মিললে "model কতটা ভালো" বলা যায় না। সব সংখ্যা এক run ও এক stage থেকে দিন।
3. **Causal ভাষা ও Conclusion (Major)।** "Influencing/impact", "better nutrient management → higher yield, lower GHG" — ফল শুধু predictive association এবং fertilizer ↔ GHG ধনাত্মক। *সহজ কথা:* "সম্পর্ক আছে" ≠ "কারণ"। yield-scaled emission/NUE দিয়ে দাবি যাচাই করুন বা দাবি নামান।

### Minor
4. **Figure/Table references (Reporting)।** Fig. 6→7, Fig. 7g→8g, "AL blue", Tables 2–3 নেই, Fig. S6 labels, Fig. 9 legend "> 0.035"। *সহজ কথা:* পাঠক ভুল ছবি দেখবেন; সংশোধন সহজ।
5. **Citations (Reporting)।** Suarez-Gutierrez, Wang 2018c, Gaihre@p1, Chen 2011, Sutton-Grier, Sapkota 2014, IPCC 2019; Ahmed 2021a/b ও D'Orazio duplicate। *সহজ কথা:* citation-এর title দাবির সাথে মিলুক।
6. **Ethics/Declaration typo।** "wheat", "Spkota", "Hosssin"।

### Methodological
7. **Linear baseline।** GLM কার্যত intercept-only (λ-path)। *সহজ কথা:* "ML linear-কে হারিয়েছে" বলার আগে ন্যায্য linear/ridge দিন; আমাদের OLS R² 0.20–0.38 বনাম RF 0.50–0.58।
8. **XAI data ও run।** PFI/PDP/ALE train-data-য়; local XAI ভিন্ন model। *সহজ কথা:* ব্যাখ্যা সেই model-এর হওয়া চাই যা রিপোর্ট করছেন, এবং hold-out data-য়।
9. **Additivity ও interaction।** PD≈AL ≠ additive; H-statistic report করুন।
10. **Scaling।** শুধু train statistics ব্যবহার করুন।

### Statistical
11. **Stack-এর সুবিধা।** 0.9–1.5% test gap; repeated splits/CI/paired test দিন।
12. **Ecological correlation ও GWC।** S5 union-mean; local r-এ significance/multiple testing; bandwidth (144 বনাম 69) স্পষ্ট করুন।
13. **ANOVA clustering।** Hybrid-বনাম-HYV "no difference" claim-এর test বলুন; clustering ধরে mixed model।

### Data & validation
14. **Union-centroid, 250 m resample।** 100% অভিন্ন environmental মান union-এর ভেতরে — তাই "250 m" ভ্রান্ত precision।
15. **Row unit/sample size।** 6,500 HH / 13,137 / 13,150; train rows 77.7–79.6%; outlier-removal count; Boro শূন্য yield।
16. **`Water_regime` ও field duration সংজ্ঞা।**

### Reproducibility
17. Split, saved models, seeds, shapefile, CCAFS-MOT, feature-processing, Fig. S7 code প্রকাশ করুন; data availability statement ঠিক করুন।

### Reporting
18. Abstract-এ GHG modeled বলুন; research questions/hypotheses; Limitations ↔ Policy সঙ্গতি; "all code and data" দাবি সংশোধন।
