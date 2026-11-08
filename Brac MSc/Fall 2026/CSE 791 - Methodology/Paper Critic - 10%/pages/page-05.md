# Page 05 — XAI methods (PFI, PDP/ALE, Breakdown), GW correlation, §3.1 EDA, §3.2 AutoML results (শুরু)

← [page-04](page-04.md) | [page-06](page-06.md) →

## A. এই পেজে কী আছে
- §2.3.2 XAI-র তিন পদ্ধতি (**PFI**, **PDP/ALE**, **Breakdown**), §2.3.3 **Geographically weighted (GW) correlation**, code availability।
- **§3.1 Exploratory data analysis**, **§3.2 AutoML results**-এর শুরু (model count, Table 4-এর বিবরণ, hold-out test R² 0.451/0.561/0.523)।
- Main message: XAI কোন data-য় চলল, কী মাপা হলো; EDA-র তথ্য (কত % HYV, F-test)।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ DALEX explainer (লাইন ১–১৫)
- **কী বলছে:** DALEX package (Biecek 2018)-এ "explainer" বানানো হয়েছে যা model + data (train বা test) জুড়ে দেয়; PFI, PDP/ALE গ্লোবাল; breakdown লোকাল।
- **খেয়াল:** কোন data-র সাথে explainer জুড়ল? Text বলে "training or test data"। **Code বলছে training**: `explainer_train <- DALEX::explain(model=best_ML, data=x_train, y=y_train …)` (Aus Rmd:849–858; Aman:862; Boro:865) এবং `variable_importance(explainer_train, type="difference")` (Aus:862; Aman:875; Boro:878); PDP/ALE `model_profile(explainer = explainer_train, …)` (Aus:1016–1054)। **কোনো test-data explainer নেই** (grep `explainer_test`: নেই)। অর্থাৎ PFI/PDP/ALE **training data-তে** — যেখানে stack-এর RMSE ≈ 404.8 (Aus, S6) আর test 817.6। **Confirmed issue** (Seed F10)।
- কেন গুরুত্বপূর্ণ: PFI training-এ মাপলে model যা "মুখস্থ" করেছে (overfit) সেই feature-ও গুরুত্ব পায়; test-এ গুরুত্ব ভিন্ন হতে পারে।

### B2. ¶ PFI (লাইন ১৬–২৬ প্রায়)
- **কী বলছে:** Fisher et al. 2019-এর model-agnostic PFI: feature shuffle করলে prediction error (drop-out loss = RMSE) কতটা বাড়ে।
- **খেয়াল (p7 §3.3-এর সাথে):** Text বলে loss হলো "the factor by which the RMSE is increased"। কিন্তু code `type="difference"` — মানে **বিয়োগফল (kg/ha)**, গুণক নয়। Table S7 Aus N-rate "Mean loss = 361.5" → যদি train RMSE ≈ 404.8 হয় তবে permute করলে ≈ 404.8 + 361.5 = **766.3** (difference); "factor" হলে 1.89× হত (`work/worked_examples.out`)। তাই বর্ণনা ভুল (**Confirmed issue**)। আর "Importance (%)" = loss/(সর্বোচ্চ loss) × 100 (যেমন 236.4/361.5 = 65.4%) — relative-to-top, কোনো absolute নয়।
- **আরও:** permutation-সংখ্যা (B) ও random seed report নেই ("Not reported…")। SD loss (21.9 ইত্যাদি) থেকে বোঝা যায় একাধিক permutation — কিন্তু কয়টা?
- **Rule 4:** PFI predictive importance, causal effect নয়।

### B3. ¶ PDP ও ALE (লাইন ২৭–৪২ প্রায়)
- **কী বলছে:** PDP = অন্য সব feature "control" করে feature-এর গড় প্রভাব; correlated feature-এ PDP ভুল হতে পারে; ALE (Apley & Zhu 2020) এর বিকল্প — unbiased, extrapolation লাগে না।
- **খেয়াল:**
  1. "PDP other predictors **controlled**" — আসলে PDP বাকি feature-গুলোর **observed value-র উপর গড়** করে; "controlled/fixed" বলা ভুল শোনায়।
  2. "ALE is unbiased" — ALE correlated feature-এ ভালো, তবে bin-সংখ্যা ও sparse region-এ অস্থির (লেখকরাই p12-তে বলেন)।
  3. **Train data-য় চলে** (B1)।

### B4. ¶ Breakdown (লাইন ৪৩–৬৪ প্রায়)
- **কী বলছে:** "Model agnostic greedy explanations" (Biecek & Burzykowski 2021; Staniak & Biecek 2018): ভবিষ্যদ্বাণীকে feature-wise contribution-এ ভাঙে। **Union-average attributions for top five features** calculate ও map করা।
- **খেয়াল (Seed F10, code):**
  1. Local XAI code `local_XAI_uniion_*.Rmd` `break_down()` চালায় **সব row-তে** (for-loop, Aus Rmd:193–196) — ফাইল `*_union_data_all.csv` থেকে (**repo-তে নেই**, `aus_data_all.csv` নয়)।
  2. **ভিন্ন saved model:** XAI Rmd `h2o.loadModel(...)`: Aus `StackedEnsemble_AllModels_3_AutoML_4_20211104_201857` (Aus XAI Rmd:159); Aman `…_4_AutoML_5_20211104_162457` (Aman XAI:170); Boro `…_3_AutoML_2_20211102_201704` (Boro XAI:171)। অথচ AutoML HTML-এ model ID: Aus `…_4_AutoML_5_20211128_82339`; Aman `…_4_AutoML_3_20211127_174647`; Boro `…_3_AutoML_1_20211104_123317`। অর্থাৎ **Fig. 8 (local) আর Table 4/Fig. 6–7 (AutoML run) একই run-এর model নয়** — কোনটা paper-এ গেছে, documented নয়।
  3. **Scaling mismatch:** local XAI-এ `df<-FeatureData(mf)` (পুরো union data নিজের mean/SD-তে scale) আর model train হয়েছে train-data-র নিজস্ব scale-এ (Aus XAI:108,115–117)। তাই model যে scale-এ train হয়েছে, explanation-এর input সেই scale-এ নয় — execution ছাড়া প্রভাব মাপা যায় না (Rule 8)।
  4. "**Union-average attribution**": row-এর attribution union ধরে গড় — সেটা কি attribution-এর spatial pattern, নাকি শুধু union-এর feature value-র পার্থক্য? (B ও notes: "effect heterogeneity vs feature-value differences" আলাদা করা দরকার; MSc lesson।)
  5. Breakdown-এর order নির্ভরতা (লেখকরা স্বীকার করেছেন p12); কোডে `break_down` default greedy order — order fix/average (shap) করা হয়নি।
  6. Breakdown-এর জন্য Ribeiro 2016 cite; সঠিক হতো Staniak & Biecek 2018 (যেটা আছে)।

### B5. §2.3.3 Geographically weighted correlation (লাইন ৬৫–৭৪)
- **কী বলছে:** GW Pearson correlation (Brunsdon 2002) — Total GWP বনাম সবচেয়ে গুরুত্বপূর্ণ factor; bi-square adaptive kernel; GWmodel (Gollini 2015)।
- **খেয়াল (code):**
  1. কোড আছে **শুধু Aman** (`gw_correlation_aman_01/02.Rmd`); Aus/Boro-র GW code নেই। `_01`: `gwss(vars=c("Total_GWP","Crop_Types","GD","N_rate","P_rate","K_rate"))` — **`Crop_Types` (nominal, local/HYV/hybrid) numeric ধরে Pearson** (Rmd:77, `_01`); `_02` তা বাদ দেয়। Nominal-কে numeric করা অর্থহীন (codes-এর order নেই)। **Confirmed issue** (code-level); Fig. 9-এ crop type নেই, তাই প্রকাশিত ফলে প্রভাব সম্ভবত নেই (**suspected** যে `_02` ব্যবহার হয়েছে)।
  2. Bandwidth `bw.gwr(Total_GWP ~ Crop_Types+GD+K_rate+N_rate+P_rate, approach="AICc", kernel="bisquare", adaptive=TRUE)` — GWR (regression)-এর জন্য নির্বাচিত bandwidth, সেটা `gwss` correlation-এ ব্যবহার: বিকল্প নয়, কিন্তু correlation-এর জন্য আলাদা বাছাই নয়; paper "optimum neighbour size" বলে।
  3. Input data: `aman_GWM_01.shp` — union-level (প্রতি union একটা point) বলে মনে হয়; shapefile repo-তে নেই → "Not reported…"।
  4. **Fertilizer → GWP correlation আংশিক circular** (CCAFS-MOT input; p3)।
  5. Union-level aggregate (ecological) correlation: আমাদের recompute দেখায় SI S5 **union-mean** correlation (Aus/Boro exact; Aman প্রায়)। Row-level correlation অনেক কম (যেমন Aus P: 0.545 → 0.385)। Check 7।

### B6. ¶ Code availability (লাইন ৭৫–৭৯)
- **কী বলছে:** "All relevant R code … available in our GitHub repository।"
- **খেয়াল:** Repo-তে কী **নেই**: train/test CSV, split code, union_data_all CSV, shapefile, saved models, CCAFS-MOT code, kriging/NDVI processing code, Aus/Boro GW code, GHG-PFI (Fig. S7) code। "All relevant" অতিরঞ্জিত। **Confirmed issue** (inventory-ভিত্তিক)।

### B7. §3.1 Exploratory data analysis (লাইন ৮১–১০৯)
- **কী বলছে:** মোট 13,137 farmer; >80% HYV, ~11% local, ~8% hybrid; Aus-Aman-এ hybrid 3–4%, Boro-তে 14%; local Aus-এ ~33%, Aman-এ 18%, Boro-তে 0। Boxplot (Fig. 3a)। **Boro গড় yield Aus/Aman-এর চেয়ে বেশি (F = 3012, p<0.001)**। Hybrid সব season-এ বেশি yield "(Boro F = 27.6**, Aman F = 733.6**, Boro F = 123)"। Total GHG season-ভেদে ভিন্ন (F = 2364), Aus-এ সবচেয়ে কম; local-এর emission কম, কারণ কম fertilizer (Fig. S5)। N, P, K ধনাত্মক correlation (Table S5)। **Highland-এ yield বেশি, কিন্তু significant নয় (Fig. S6a, S6b)**; Aman ও Boro-তে medium texture-এ বেশি (S6c); extreme temp শুধু Boro-তে প্রভাব (S6d); spatial variability "no distinct pattern" (Fig. 4)।
- **আমাদের যাচাই (CSV, `work/scripts/check_anova_s31.py`):**
  - Row সংখ্যা 13,150 (677+6,664+5,809) বনাম paper 13,137: পার্থক্য **13** (কারণ অজানা)। Union: Aus 78 ✓, Aman **246** (paper 247), Boro 224 ✓।
  - Crop mix: HYV 80.8%, Local 10.9%, Hybrid 8.4% ✓; Aus hybrid 3.1%, Aman 3.6%, Boro 14.4% ✓; Local Aus 32.9%, Aman 18.1% ✓; Boro local 0 ✓। (paper-এর সংখ্যা মেলে।)
  - Season-ভেদে yield ANOVA: **F = 2948.4** (paper 3012) — একই order, মান সামান্য আলাদা (row সংখ্যা/কিছু বাদ?)। GWP ANOVA F = **2365.9** (paper 2364 ✓)।
  - Hybrid vs others (crop type ANOVA): Aus **F = 27.6**; Aman **F = 733.7** (paper 733.6 ✓); Boro **F = 116.6** (paper "123")। অর্থাৎ paper-এর "**Boro F = 27.6**" আসলে **Aus**-এর F — "Boro" দু'বার লেখা (Seed: verified), আর Boro-র F paper-এ 123, আমাদের 116.6 (পার্থক্য ব্যাখ্যাহীন)।
  - ANOVA-র সীমা: row-গুলো independent নয় (একই PSU/union); post-hoc/multiple comparison উল্লেখ নেই; "significantly higher" মানে hybrid-এর গড় বেশি, আলাদা nutrient/district-এর প্রভাব নিয়ন্ত্রণ করা নেই (confounding)।
- **Fig. S6 labels:** Text "(Fig. S6a and S6b)" highland/drainage, "(S6c)" texture, "(S6d)" extreme temp। SI Fig. S6-এ panel: (a) Land types, (**d**) Drainage class, (c) Soil texture, (**e**) Extreme temp zones; caption বলে "(a), (b), (c) and (e)"। অর্থাৎ text-এর S6b = আসলে (d) drainage; S6d (extreme temp) = আসলে (e)। **Confirmed issue** (labels)।
- "Highland-এ বেশি yield, কিন্তু significant নয়" — Fig. S6a দেখলে Aus-এ Very Lowland/Highland ভিন্ন, test result (p-value) report নেই।

### B8. §3.2 AutoML শুরু (লাইন ১১০–১৩৮; পরের অংশ p6)
- **কী বলছে:** AutoML "958, 175, 198 models" train করেছে "Boro, Aman, Aus-এ" (Table 4)। Stack (all models) সব season-এ best। MAE "637–773 kg/ha" যা minimum observed yield-এর চেয়ে কম। Boro (958 model): RMSE 816.01, MAE 622.31, RMSLE 0.35, R² 0.55; Aman (175): 926.20, 647.44, 0.34, 0.59; Aus (198): 1109.2, 773.47, 0.43, 0.51; "51–59% variance"; Aus-এ কম performance "greater variability… dry to wet transition"।
- **খেয়াল — Seed F1 (সবচেয়ে গুরুত্বপূর্ণ):** তিন সূত্রে মিলিয়ে দেখলে **Table 4-এ Aus ও Boro অদলবদল**:
  | | Table 4 (p7) | SI S6 stack CV | AutoML HTML (stack 10-fold CV / meta-learner level-one) |
  |---|---|---|---|
  | "Boro" | 958 models; 816.01 / 622.31 / 0.35 / **0.55** | Aus CV **816.0 / 0.543** | **Aus** HTML: 958 base models; stack CV RMSE 836.03; MAE 637.33; meta-learner (level-one) RMSE **816.68**, MAE **622.46**, R² **0.5448** |
  | "Aus" | 198; 1109.2 / 773.47 / 0.43 / **0.51** | Boro CV **1109.2 / 0.510** | **Boro** HTML: 188 base models; stack CV RMSE **1112.41**, MAE **772.56**, RMSLE 0.4316; meta-learner R² 0.5117 |
  | Aman | 175; 926.20 / 647.44 / 0.34 / 0.59 | Aman CV 926.2 / 0.592 ✓ | Aman HTML: 175 base models; level-one RMSE 926.23, MAE 647.33, R² 0.594 ✓ |
  - (গণনা: (816.6753 − 816.01)/816.6753 = 0.08% — Table 4-এর "Boro" মান Aus HTML-এর meta-learner মানের প্রায় সমান; `work/check_arith.out`।)
  - **Verdict:** Table 4-এ **Aus ও Boro row-label swapped** — models count (958 → Aus; Boro-র আসলে 188 ≠ paper "198") সহ। এর উপর ভিত্তি করে লেখা "Aus-এর কম performance = transition period" ব্যাখ্যা (p5 শেষ) **অসমর্থিত**; S6-এ **Boro-র CV R² সবচেয়ে কম (0.510)**, Aus 0.543 (RMSE-এর দিক থেকে Boro সবচেয়ে বেশি 1109.2 কারণ yield-এর variance বেশি)। (Confidence: উচ্চ।)
  - **দ্বিতীয় সূক্ষ্মতা:** Table 4-এর caption "10-fold cross-validation statistics" — কিন্তু মানগুলো (816.68, R² 0.5448 ইত্যাদি) আসলে **meta-learner-এর level-one metrics** (HTML-এ `glm` "reported on training data" ব্লক), যেখানে stack-এর নিজস্ব CV RMSE Aus-এ 836.03 (S6 CV-তে 816.0 = meta-learner মান)। অর্থাৎ **stage মেশানো**: কিছু "CV" মান সম্ভবত meta-learner-এর out-of-fold prediction-এ গণনা; সত্যিকারের 10-fold CV of the stack আরও বড়: Aus 836.03 (মান ~2.4% বেশি: (836.03−816.68)/816.68), Boro 1112.41 (vs 1110.02), Aman 928.20 (vs 926.23)। (Check 8; Rule 3.)
  - "MAE 637–773" — Table 4-এ minimum MAE 622.31; "637" মিলছে Aus HTML stack CV MAE 637.33; "773" Table 4-এর Aus MAE 773.47। তাই text range "table-এর সাথে মেলে না" (622.31 < 637)। **Confirmed issue**।
  - "MAE … lower than the minimum observed yield values": min yield CSV: Aus 247, Aman 112, Boro 0 — **MAE ≥ 622 > 247/112/0**; তাই বাক্যটা ভুল (শুধু 5th percentile Aus ~1235-এর সাথে তুলনা করলে ঠিক হত)। **Confirmed issue** (data-নির্ভর)।
  - R² 0.51–0.59 = "explaining 51–59% variance": S6 CV R² 0.510–0.592 ✓ (মূল label-swap বাদে)।

## C. নতুন শব্দগুলো

#### Permutation Feature Importance (PFI) — গভীরে
- **সহজ মানে:** একটা feature-এর মান row-গুলোর মধ্যে এলোমেলো করে সাজাই; error কতটা বাড়ল সেটাই গুরুত্ব।
- **ছোট উদাহরণ (সংখ্যা):** train RMSE 404.8; N-rate shuffle → RMSE 766.3 → loss (difference) = 361.5; top feature-এর 100% ধরলে K-rate (176.3)-এর গুরুত্ব = 176.3/361.5 = **48.8%**।
- **এই paper-এ:** DALEX `variable_importance(type="difference")`, **train data-তে**; Table S7–S9, Fig. 6।
- **খেয়াল:** correlated feature (N, P, K rate) থাকলে এক feature shuffle করলে অসম্ভব combination তৈরি হয় → গুরুত্ব বিকৃত; test data-তে চালানো উচিত।

#### Partial Dependence Plot (PDP)
- **সূত্র:** ĝ_j(z) = (1/n) Σ_{i=1}^{n} f(z, x_{i,−j}) — j-তম feature-কে z-তে বসিয়ে বাকিগুলো যেমন আছে রেখে model-এর prediction গড়।
- **ছোট উদাহরণ:** ৪ row-এ N=100 বসালে prediction 3000, 3400, 3800, 4200 → PD = **3600**।
- **এই paper-এ:** Fig. 7 (নীল রেখা = PD)।
- **খেয়াল:** feature correlated হলে অবাস্তব combination; ICE দেখা হয়নি।

#### Accumulated Local Effects (ALE)
- **সহজ মানে:** feature-কে ছোট ছোট bin-এ ভাগ করে প্রতি bin-এ শুধু ছোট পরিবর্তনে prediction-এর পার্থক্য জমা (accumulate) করা, তারপর center করা।
- **ছোট উদাহরণ (Python):** bin 1 (0–100): row-পার্থক্য 200, 300 → গড় 250; bin 2: 100, 60 → গড় 80। জমা: 250, 330 → ওজনযুক্ত গড় 290 → centered: **−40, +40**।
- **এই paper-এ:** Fig. 7-এ কমলা রেখা (AL)।
- **খেয়াল:** bin ছোট হলে অস্থির; local difference মানে model যেখানে data আছে সেখানেই দেখে।

#### Breakdown plot (iBreakDown)
- **সূত্র:** f(x*) = v₀ + Σ_j contribution_j (v₀ = গড় prediction)।
- **ছোট উদাহরণ:** গড় yield 3105 + N 250 + crop type 120 + field duration (−40) + P 60 + K 30 + বাকি 15 = **3540**।
- **এই paper-এ:** প্রতি row-এর contribution, union-গড় করে map (Fig. 8)।
- **খেয়াল:** order-নির্ভর; "contribution" ≠ causal effect; union-গড় feature-value-র পার্থক্য আর model-এর প্রকৃত "response"-এর পার্থক্য মিশিয়ে ফেলে।

#### Geographically weighted (GW) correlation, bi-square kernel
- **সূত্র:** ওজন w(d) = (1 − (d/b)²)² যখন d < b, নাহলে 0; ওজনযুক্ত Pearson correlation।
- **ছোট উদাহরণ:** b = 10: d = 2 → 0.9216; d = 5 → 0.5625; d = 10 → 0।
- **এই paper-এ:** Total GWP বনাম N, P, K, GD; adaptive bandwidth (নিকটতম k প্রতিবেশী); Fig. 9।
- **খেয়াল:** local correlation অনেক কম sample-এ চলে → অস্থির; multiple-testing; spatial autocorrelation।

#### Ecological (aggregate) correlation
- **সহজ মানে:** group-গড়ের (যেমন union-গড়) correlation, individual-এর নয়; সাধারণত বেশি দেখায়।
- **উদাহরণ:** Aus yield~P: union-গড়ে r = 0.625, row-level 0.402 (Check 7)।

#### ANOVA (F-test)
- **সহজ মানে:** একাধিক group-এর গড় আলাদা কিনা পরীক্ষা: F = (group-এর মধ্যে variance)/(group-এর ভেতরের variance)।
- **ছোট উদাহরণ:** ৩ group (3000–3200, 3400–3600, 4000–4200), 3টা করে row → F = **76.0** (df 2,6)।
- **এই paper-এ:** season-ভেদে yield (F=3012), crop type-ভেদে।
- **খেয়াল:** independence ধরে নেয় — এখানে clustered।

## D. Equation / statistics
এই পেজে numbered equation নেই। পদ্ধতি-সূত্র (PFI, PDP, ALE, breakdown, GW correlation, ANOVA) section C-তে symbol, উদাহরণসহ দেওয়া। সীমা সংক্ষেপে:
- **PFI:** feature correlated → বিকৃত; train data → overfit-ভিত্তিক।
- **PDP:** feature independence ধরে।
- **ALE:** bin-নির্ভর, sparse region-এ নড়বড়ে।
- **Breakdown:** order-নির্ভর, instance-নির্ভর।
- **GW correlation:** bandwidth-নির্ভর; local sample ছোট।
- **ANOVA:** independence, normality, equal variance।
- **R² বনাম EVar (Fig. 5):** EVar (explained variance) = 1 − Var(error)/Var(y); R² = 1 − MSE/Var(y)। **bias থাকলে EVar > R²** (খেলনা-উদাহরণে R² 0.820, EVar 0.827)। Fig. 5-এ EVar − R² মাত্র 0.002 ⇒ গড় ভুল ≈ 0 (bias নগণ্য), যদিও regression লাইন "flatter" (slope < 1)।

## E. Figures
এই পেজে নেই (Fig. 3, 4 → p6; Fig. 5, 6 → p7)।

## F. Tables
- **Table 4** p7-এ; এই পেজের text তার বর্ণনা — বিশ্লেষণ B8-এ (Aus/Boro swap)।
- **Cross-check SI Table S5 (r values):** text "N, P, K positively correlated with yield and GHG in all seasons" — S5: Boro yield~N 0.256, P 0.176, K 0.147 (দুর্বল), Aman GWP~N 0.201, P 0.108, K 0.223 (দুর্বল)। "সব season-এ positive" ঠিক (চিহ্নে), কিন্তু শক্তি season-ভেদে ভীষণ ভিন্ন (দেখুন p9 আলোচনা)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 5.1 | **Table 4-এ Aus ও Boro অদলবদল** (958 models = Aus HTML; 198 বনাম Boro HTML 188) — Aus "transition period" ব্যাখ্যা অসমর্থিত | p5 §3.2; p7 Table 4; SI S6; HTML (aus: 958 base models, level-one RMSE 816.68; boro: 188 base models, CV RMSE 1112.41) | Confirmed issue |
| 5.2 | Table 4 "CV" মান আসলে meta-learner level-one metrics; stack-এর নিজস্ব CV RMSE (Aus 836.03, Aman 928.20, Boro 1112.41) আলাদা stage | `work/html_{aus,aman,boro}.txt` (extract of the HTMLs): stack CV block vs `glm` level-one block (Aus lines 426 vs 512; Aman 443 vs 529; Boro 447 vs 533) | Potential concern |
| 5.3 | PFI/PDP/ALE **training data-য়** (`explainer_train`), test-এ নয় | `yield_aus_autoML.Rmd:849-862,1016-1054`; Aman:862,875; Boro:865,878 | Confirmed issue |
| 5.4 | Paper "RMSE-এর factor" বলে, code `type="difference"` (kg/ha বিয়োগ) | p7 §3.3; Rmd:862 | Confirmed issue |
| 5.5 | Local XAI-এর saved model ≠ AutoML-HTML-এর model (Aus: 20211104_201857 vs 20211128_82339; Aman: …162457 vs …174647; Boro: …201704 vs …123317) | `local_XAI_uniion_*.Rmd:159/170/171` vs HTML model IDs | Confirmed issue |
| 5.6 | Local XAI চলেছে `*_union_data_all.csv`-এ (repo-তে নেই), train ফাইলে নয়; scaling mismatch | `local_XAI_uniion_aus.Rmd:47,108,115-117,152` | Confirmed issue (scaling-প্রভাব: execution লাগবে) |
| 5.7 | GW code শুধু Aman; `_01`-এ nominal `Crop_Types` numeric Pearson-এ | `gw_correlation_aman_01.Rmd:77`; `_02` তা বাদ দেয় | Confirmed issue (code-level) |
| 5.8 | "All relevant R code available" — CCAFS-MOT, split, kriging, GHG-PFI, Aus/Boro GW নেই | file inventory | Confirmed issue |
| 5.9 | S5 correlations = union-mean (ecological); row-level কম | `work/check07b.out` | Confirmed issue (reporting) / Potential concern (interpretation) |
| 5.10 | "Boro F-value" দু'বার; 27.6 আসলে Aus (আমাদের ANOVA); Boro F আমাদের 116.6 vs paper 123 | p5 §3.1; `work/check_anova.out` | Confirmed issue |
| 5.11 | MAE range "637–773" বনাম Table 4 min 622.31; "MAE < minimum observed yield" ভুল (min yield: 247/112/0) | p5 §3.2; Table 4; CSV | Confirmed issue |
| 5.12 | Row 13,150 বনাম 13,137; Aman unions 246 বনাম 247 | CSV (Check 4) | Unresolved question |
| 5.13 | Fig. S6 panel/label মিল নেই (text S6b→(d), S6d→(e)) | p5 §3.1; SI p23 | Confirmed issue |
| 5.14 | Train rows 80% নয় (77.7–79.6%) | HTML Null D.o.F. | Unresolved question |
| 5.15 | ANOVA-তে clustering/confounding উপেক্ষিত; hybrid-এ "significantly higher yield" মানে causal নয় | p5 §3.1 | Potential concern |

**লেখকদের পক্ষে:** Crop-mix (HYV/local/hybrid %) আমাদের CSV-র সাথে মেলে — data description সৎ। PFI-র SD report করা, PDP-র সাথে ALE ব্যবহার, breakdown-এর order-সীমা স্বীকার — চমৎকার।

**Reviewer প্রশ্ন:** PFI test data-য় করলে ranking একই থাকবে? Table 4 সংশোধন কী? কোন model run Fig. 8-এ গেছে?

## H. সারাংশ
- **Short summary:** XAI-র তিন পদ্ধতি train data-য়, local breakdown ভিন্ন saved model-এ; GWC union-গড়ে; EDA-র সংখ্যা মূলত CSV-র সাথে মেলে; Table 4 Aus/Boro অদলবদল।
- **৫ key terms:** PFI, PDP, ALE, Breakdown, GW correlation (সাথে ANOVA)।
- **Takeaways:** (১) Table 4 swapped (F1 verified); (২) XAI train data-য়; (৩) XAI ও AutoML আলাদা run; (৪) S5 ecological correlation।
- **Key numbers:** 13,137; 958/175/198 (paper); Table 4 values; F = 3012, 27.6, 733.6, 123, 2364; 637–773; test R² 0.451/0.561/0.523 (p6 শুরুতে)।
- **পরের পেজ-প্রশ্ন:** Fig. 3–5 কী দেখায়? Fig. 5 vs S6 test মেলে?

## Master Notes
- **Paragraph-wise:** DALEX; PFI; PDP/ALE; breakdown; GWC; code; EDA; AutoML results।
- **Exact numbers:** (উপরে H)।
- **Claims & evidence:** "Aus lower performance due to transition" → data উল্টো; "all code available" → নয়; "PFI factor" → difference।
- **Open checks:** কোন run Fig. 8/6/7-এর? PFI on test; permutation B।
- **MSc notes:** XAI held-out data-তে; একই run-এর model; local attribution-এ "effect heterogeneity বনাম feature-value difference" আলাদা করুন; group-CV; code+split file publish।
