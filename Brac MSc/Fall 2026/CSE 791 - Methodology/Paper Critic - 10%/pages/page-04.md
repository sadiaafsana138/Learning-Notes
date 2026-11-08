# Page 04 — §2.3 Analyses: cleaning, split, AutoML, stacking, RMSE (Eq. 1), XAI শুরু, Fig. 2

← [page-03](page-03.md) | [page-05](page-05.md) →

## A. এই পেজে কী আছে
- §2.3 **data cleaning**, missing value/outlier, **80/20 random split**, §2.3.1 **AutoML** (H2O, algorithms, settings, stacking, meta-learner), **Equation (1) RMSE**, §2.3.2 **XAI**-এর শুরু, **Fig. 2** (workflow)।
- Main message: কীভাবে model train/validate হয়েছে — পুরো paper-এর validation design এখানে।
- এটা paper-এর সবচেয়ে গুরুত্বপূর্ণ পেজ ML-দৃষ্টিতে: split, CV, settings।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ Categorical handling (লাইন ৮–১৩)
- **কী বলছে:** h2o package categorical (rice variety type, crop type, line sowing, balanced fertilization, organic matter, lime) নিজে encode করে, one-hot লাগেনি।
- **খেয়াল:** কোড-এর feature list (Aus Rmd:109–116 অর্থাৎ `FeatureData`) যে categorical নেয়: `Crop_Types, LT_Class, General_Soil_type, DRC_Class, TZONE_Class, Soil_texture, Water_regime, Manure` — **text-এর list-এর সাথে মেলে না**: line sowing, balanced fertilization, lime কোডে নেই; উল্টে land type, soil type, drainage, temperature zone, texture, **Water_regime** আছে। **Confirmed issue** (text বনাম code)।

### B2. ¶ Missing values (লাইন ১৪–২৭)
- **কী বলছে:** GLM/DNN mean imputation; tree-based মডেল missing-কে আলাদা branch-এ পাঠায়। Soil data kriging থেকে তাই imputation দরকার নেই। Outlier boxplot + 3 SD rule; "clear data-entry error" বাদ, বাকি রাখা।
- **খেয়াল:**
  1. কত row বাদ গেল? Report নেই। HTML থেকে: Aus training rows = **526** (GLM "Null D.o.F. 525"), Aman **5,305**, Boro **4,626**; CSV total 677 / 6,664 / 5,809 → 80% = 541.6 / 5331.2 / 4647.2 (`work/worked_examples.out`)। অর্থাৎ Aus-তে প্রায় 15–16, Aman-এ ~26, Boro-তে ~21 row কম। আমরা বলতে পারি "train size 80%-এর চেয়ে কম" — কেন, "Not reported in the provided paper, Supporting Information, or available code" (হতে পারে outlier removal; **suspected**)।
  2. Boro CSV-তে **12টা row-এর yield = 0**; Boro < 2000 kg/ha: 195 row (`work` output)। Text বলে Boro range "~2000–9000" (p7)। শূন্য yield কি crop failure নাকি missing? "Not reported…"।
  3. "3 SD" rule outlier যাচাইয়ের জন্য — কিন্তু outlier test কি train/test split-এর আগে হয়েছে (পুরো data-য়) নাকি পরে? অজানা।
  4. `Total_GWP` আর `Emission_Intensity` — যেটা yield/emission-এর সাথে সম্পর্কিত — predictor list-এ নেই (ঠিক, leakage এড়ানো)। ✔

### B3. ¶ Train/test split (লাইন ২৮–৩৪) — **সবচেয়ে গুরুত্বপূর্ণ**
- **কী বলছে:** প্রতি crop-এর data **randomly** 80% train, 20% test। Test = hold-out।
- **খেয়াল:**
  1. **Row-level random split**; union/household/PSU group করা নেই। Code-এ `h2o.automl(... nfolds=10 ...)` (Aus Rmd:200; Aman:213; Boro:216) — `fold_column` **নেই**, `fold_assignment` default (Random/AUTO)। Train/test CSV পড়া হয় `train_data.csv`/`test_data.csv` (Aus Rmd:56–57), যেগুলো repo-তে **নেই**, আর split তৈরির code-ও নেই। ফলে split কীভাবে হয়েছে (seed, stratification) — "Not reported…"।
  2. **Leakage-সম্ভাবনার আকার (আমাদের simulation, `work/scripts/check03_09_10_models.py`):** একই size-এর random 80/20 split ২০০ বার করলে test row-এর কত % এর union train-এ আছে: Aus **97.0%**, Aman **99.8%**, Boro **99.7%**; household-like key (Index-এর প্রথম দুই token — আমাদের অনুমান) মেলে Aus 73.9%, Aman 85.1%, Boro 82.6%। অর্থাৎ test "unseen area" নয়। **আসল split reconstruct করা যায়নি** (ফাইল নেই) — এটা paper-এর পদ্ধতি অনুযায়ী simulation, "leakage প্রমাণ" নয়। কী হলে confirm হত: `train_data.csv`/`test_data.csv`।
  3. কারণ: প্রতিটা union-এর ভেতর সব environmental feature একই (Check 2); একই union-এর train row দেখে model union-এর "পরিচয়" (NDVI/soil/weather combination) মুখস্থ করে একই union-এর test row-এ yield অনুমান করতে পারে। এটা Rule 5 অনুযায়ী: "random split ≠ unseen area-তে test"।
  4. **আমাদের নিজস্ব check (Check 10)** — RF (default), 5-fold: row-random CV R² বনাম leave-union-out R²: Aus **0.461 → 0.129**; Aman **0.574 → 0.276**; Boro **0.513 → 0.010** (3 repeat গড়; "our own check with a simpler model, not a reproduction")। Row-random R² paper-এর stack R² (0.45–0.59)-এর কাছাকাছি, কিন্তু union-grouped করলে অনেক কমে। (Confidence: মাঝারি; RF-এ কোনো tuning নেই; তবু drop বড় ও consistent।)

### B4. Fig. 2 পরের অংশ — দেখুন E।

### B5. §2.3.1 AutoML (লাইন ৩৫–৭৭)
- **কী বলছে:** AutoML ম্যানুয়াল কাজ কমায়; H2O (`h2o`, R) দিয়ে GLM, DRF, XRT, GBM, XGBoost, DNN train+tune (Table S1); GLM/DRF/XRT default hyperparameter, GBM/XGBoost/DNN random grid (Table S2); **`max_runtime_secs` ও `max_models` = 0 (no limit)**, `stopping_tolerance = 0.0001`, `stopping_rounds = 2`; প্রতি family-র best **10-fold CV RMSE** দিয়ে; দুটো stack (All models / Best of family); meta-learner = **non-negative GLM** (Lasso/Elastic Net); base prediction = out-of-fold (10-fold)।
- **খেয়াল (code, SI ও paper-এর মিল):**
  | Setting | Paper (p4) | Code (Rmd) | SI |
  |---|---|---|---|
  | stopping_tolerance | **0.0001** | **0.001** (Aus:203, Aman:216, Boro:219) | — |
  | stopping_rounds | **2** | **3** (Aus:204, Aman:217, Boro:220) | S2 footnote: "MAE stable in last five training rounds" |
  | max_models | 0 (no limit) | `#max_models = 20` **commented out** (Aus:207) | — |
  | max_runtime_secs | 0 | `max_runtime_secs_per_model = 0` (Aus:205) — *per model*, মোট নয় | — |
  | stopping_metric | RMSE (primary) | `"RMSE"` (Aus:202) | MAE (S2 footnote) |
  - তিন source তিন রকম। **Confirmed issue** (reporting inconsistency)।
  - H2O AutoML-এ `max_runtime_secs` ও `max_models` কোনোটা না দিলে default time limit হয় (H2O docs অনুযায়ী আমার স্মৃতিতে 3600 সেকেন্ড = ১ ঘণ্টা; আমি offline এটা আবার যাচাই করতে পারিনি — **verify করুন**)। যদি তাই হয়, "no limit" claim সঠিক নয়, আর model count (958 / 175 / 188) time budget আর data size-এর ফল — সেরা model বাছাইয়ের মান নয়। (এটা suspected, কারণ run-এর `max_runtime_secs` log নেই।)
  - "**10-fold CV RMSE দিয়ে best-model**": ঠিক — কিন্তু CV fold row-level random।
  - **Meta-learner "Lasso/Elastic Net"**: HTML metalearner output "Metalearner algorithm: glm", `non_negative` — ঠিক; HTML দেখাচ্ছে Aus-এ 958 base model-এর মধ্যে বেশিরভাগ coefficient 0 (stack আসলে কয়েকটা model-ই ব্যবহার করে)।
  - Stack-এর "overfitting এড়াতে out-of-fold": ঠিক ধারণা, তবে **CV prediction-এর ওপর meta-learner fit করে সেই একই CV দিয়ে stack-এর CV RMSE জানালে** সামান্য optimistic — HTML-এ Aus: stack-এর "true" 10-fold CV RMSE **836.03** আর meta-learner-এর level-one metric **816.68** (পার্থক্য ~2.3%)। (পরের পেজে Table 4-এর সাথে যুক্ত)।
- **"Number of models"** নিয়ে: পরে p5/p7।

### B6. ¶ Evaluation + Eq (1) (লাইন ৭৮–৯১)
- **কী বলছে:** hold-out test; observed vs predicted plot; simple linear regression (obs vs pred) দিয়ে judge; metric RMSE (Eq. 1); "n = number of households"।
- **খেয়াল:** (১) Eq. (1) typo — নিচে D। (২) "n = households" কিন্তু row = farmer-plot-season (p2)। (৩) Test metric-এ R², MAE, RMSLE নেই text-এ (Fig. 5 ও S6-এ আছে)।

### B7. §2.3.2 XAI শুরু (লাইন ৯২–১১৮ প্রায়)
- **কী বলছে:** XAI black-box-কে ব্যাখ্যা করে; stack ensemble আরও কঠিন; তাই **model-agnostic** (Ribeiro 2016) approach; local = per-instance, global = পুরো আচরণ।
- **খেয়াল:** **Ribeiro 2016** ref-এর title = *"Model-agnostic interpretability of machine learning"* (arXiv 1606.05386) — "model-agnostic" claim-এ ঠিক; কিন্তু পরে p5-এ breakdown-এর জন্যও Ribeiro cite করা হয়েছে, যেখানে সঠিক source হতো Staniak & Biecek 2018 (যেটা p5-এ আছে)। ছোট citation অসঙ্গতি।

## C. নতুন শব্দগুলো

#### Hold-out test set
- **সহজ মানে:** train-এ ব্যবহার না করা, শেষে model-কে "পরীক্ষা"-য় বসানোর data।
- **ছোট উদাহরণ:** 677 row-এর 80% ≈ 541.6 train, 20% ≈ 135.4 test।
- **এই paper-এ:** 80/20 random।
- **খেয়াল:** "hold-out" তখনই সৎ, যখন test row-গুলো train row-র সাথে identity share করে না (এখানে union share করে)।

#### Cross-validation (10-fold)
- **সহজ মানে:** train data-কে ১০ ভাগ করে ৯ ভাগে train, ১ ভাগে validate — ১০ বার।
- **ছোট উদাহরণ:** 526 train row → প্রতি fold-এ প্রায় 52–53 row validate।
- **এই paper-এ:** H2O AutoML `nfolds=10`; model selection আর stacking-এর out-of-fold prediction।
- **খেয়াল:** random fold ≠ spatial fold; একই union-এর row দুই fold-এ ভাগ হয়ে যায়।

#### Data leakage (এখানে: identity/spatial leakage)
- **সহজ মানে:** test-এর তথ্য আসলে train-এ আগে থেকে "চোখে পড়েছে" — তাই স্কোর বাড়াবাড়ি ভালো।
- **ছোট উদাহরণ:** একই union-এর ৫০টা row-এর ৪০টা train-এ, ১০টা test-এ; model union-এর NDVI/soil-সংমিশ্রণ দেখে ওই union-এর গড় yield জানে।
- **এই paper-এ:** প্রমাণ নয়, সম্ভাবনা; আমাদের simulation-এ ৯৭–৯৯.৮% test row-এর union train-এ আছে।
- **খেয়াল:** (Rule 6) leakage প্রমাণের জন্য আসল split লাগে।

#### Hyperparameter tuning / Random grid search
- **সহজ মানে:** setting-এর অনেক সংমিশ্রণ এলোমেলোভাবে try করে সেরাটা বাছা।
- **উদাহরণ:** GBM-এ max_depth ∈ {3..17} (15 value) × min_rows ∈ 6 value = 90 সংমিশ্রণ থেকে random কয়েকটা (SI S4)।
- **এই paper-এ:** GBM, XGBoost, DNN।

#### Generalized Linear Model (GLM) / Ridge, λ
- **সহজ মানে:** linear regression-এর সাধারণ রূপ; regularization (Ridge) coefficient ছোট রাখে।
- **ছোট উদাহরণ:** λ বড় → coefficient প্রায় 0 → prediction ≈ গড়।
- **এই paper-এ:** baseline; SI S4: λ.max = λ.1se (Aus 50,164; Aman 52,782; Boro 21,265) ⇒ সব coefficient ≈ 0, **training R² = 0.000** (S6)।
- **খেয়াল:** এটা আসলে "intercept-only" মডেল; (Seed F4)।

#### DRF / XRT / GBM / XGBoost / DNN
- **DRF:** অনেক decision tree-র গড় (bootstrap + random feature)। **XRT:** DRF-এর চেয়েও random split। **GBM:** tree-গুলো ধাপে ধাপে আগের ভুল ঠিক করে। **XGBoost:** GBM-এর দ্রুত/regularized সংস্করণ। **DNN:** multi-layer neural net।
- **এই paper-এ:** Table S1; best-of-family S6-এ।
- **খেয়াল:** DRF-ই সাধারণত শক্ত baseline (S6-এ DRF সবচেয়ে ভালো single)।

#### Meta-learner (non-negative GLM)
- **সহজ মানে:** base model-এর prediction-কে input ধরে যে ছোট model চূড়ান্ত prediction বানায়; ওজন ≥ 0।
- **এই paper-এ:** H2O default (HTML "Metalearner algorithm: glm")।

#### RMSE, MAE, RMSLE, R²
- **RMSE:** বড় ভুলকে বেশি শাস্তি দেয়, kg/ha-এ। **MAE:** গড় পরম ভুল। **RMSLE:** log-scale ভুল; আপেক্ষিক ভুল বোঝায়। **R²:** variance-এর কত অংশ model ব্যাখ্যা করে।
- **ছোট উদাহরণ (D-তে পুরো হিসাব):** y = 3000/4000/5000, ŷ = 3200/3600/5400 → RMSE 346.4, MAE 333.3, R² 0.820।

## D. Equation / statistics

**Equation (1) — RMSE**
- Paper-এ লেখা: `RMSE = sqrt( (1/n) Σ_{i=1}^{n} [ y_i − ŷ ]² )` — "where n is number of households, y and ŷ are observed and predicted yield in household i"।
- **Typo:** ŷ-তে subscript **i** নেই (হওয়া উচিত ŷ_i)। আর "households" নয়, row/farmer-plot।
- **Symbols:** n = test row সংখ্যা; y_i = i-তম row-এর observed yield (kg/ha); ŷ_i = predicted।
- **কী মাপে:** গড় বর্গ ভুলের বর্গমূল, kg/ha-এ — বড় ভুলে সংবেদনশীল।
- **ছোট সংখ্যার উদাহরণ (Python):** ভুল = [−200, 400, −400]; MSE = (40,000+160,000+160,000)/3 = 120,000; RMSE = √120,000 = **346.4**; MAE = **333.3**; R² = **0.820**।
- **Interpret:** Aus test RMSE ≈ 818 kg/ha মানে typical ভুল ~৮০০ kg/ha; Aus গড় yield 3,105 (CSV) ⇒ ভুল ~26%।
- **Assumptions/limits:** outlier-সংবেদী; single number — test set ছোট হলে (Aus test ≈ 136–151 row) অনিশ্চিত; confidence interval/repeated split নেই।

**Simple linear regression (obs vs pred) "to judge performance"** — slope/intercept report নেই; শুধু Fig. 5-এর লাইন।

## E. Figures

**Fig. 2 — Steps used in automatic ML models for yield prediction**
- Flow: Data → Data Split (Training 80% / Test 20%) → AutoML → CV-Based Model Selection → The Best Model → Explainable AI → (1) PFI (2) Partial Dependency (3) Local Breakdown Plots; Best Model → Prediction → Predicted Yield।
- রঙ: নীল বাক্স = split/prediction; সবুজ = XAI।
- **Interpretation:** সরল workflow ঠিক; কিন্তু (১) "Partial Dependency" লেখা, ALE নেই অথচ text-এ ALE ব্যবহৃত; (২) কোনো group/spatial split বা GHG/GW correlation ধাপ নেই; (৩) split-এর আগে outlier removal/scaling-এর ধাপ নেই (code-এ scaling আলাদা)।

## F. Tables
এই পেজে নেই (Table S1, S2 SI-তে)।
- **SI cross-check (Table S1/S2):** S2 "Hyperparameter setting"-এ GLM/DRF/XRT = "pre-specified", GBM/XGBoost/DNN = pre-specified + random grid; ফুটনোটে MAE-ভিত্তিক early-stopping (paper বলে RMSE)। Table S1 GBM description "Friedman in 2011 (Friedman, 2001)" — সাল অমিল (ছোট)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 4.1 | Row-level random 80/20 split + row-level 10-fold CV; কোনো union/household group নেই | p4 §2.3; `yield_aus_autoML.Rmd:56-57,200`; Aman:213; Boro:216 | Confirmed issue |
| 4.2 | Split code ও `train_data.csv/test_data.csv` repo-তে নেই | file inventory | Unresolved question |
| 4.3 | Paper-এর পদ্ধতি অনুযায়ী simulation: test row-এর ৯৭–৯৯.৮% union train-এ আছে (Aus 97.0, Aman 99.8, Boro 99.7) | `work/check03_09_10.out` (Check 3) | Potential concern (leakage প্রমাণ নয়; আসল split দরকার) |
| 4.4 | নিজস্ব RF check: row-random R² → leave-union-out R²: Aus 0.461→0.129; Aman 0.574→0.276; Boro 0.513→0.010 | Check 10 (`work/check03_09_10.out`) | Potential concern |
| 4.5 | AutoML setting তিন জায়গায় তিন রকম: tolerance 0.0001 vs 0.001; rounds 2 vs 3; max_models "0" vs commented; MAE (S2) vs RMSE | p4; Rmd:202–207; SI S2 footnote | Confirmed issue |
| 4.6 | `max_runtime_secs`/`max_models` কোনোটাই না থাকলে H2O default time limit প্রযোজ্য কি না — যাচাই বাকি; "no limit" claim সন্দেহজনক | Rmd:205–207; H2O docs (verify) | Unresolved question |
| 4.7 | Categorical list (text) বনাম code: line sowing/balanced fert/lime নেই; land type, soil type, drainage, TZONE, texture, Water_regime আছে | p4 ¶1; Rmd `FeatureData` (Aus:109–116) | Confirmed issue |
| 4.8 | Train size 80%-এর চেয়ে কম: Aus 526/677=77.7%, Aman 5,305/6,664=79.6%, Boro 4,626/5,809=79.6%; কেন বাদ — অজানা | HTML "Null D.o.F." (Aus:525, Aman:5304, Boro:4625) | Unresolved question |
| 4.9 | Scaling আলাদাভাবে all/train/test-এ (`scale()` প্রতিবার নিজের mean/SD) — test-এ train-এর mean/SD নয় | `yield_aus_autoML.Rmd:120,127-129`; Aman:133,140-142; Boro:136,143-145 | Confirmed issue |
| 4.10 | Eq. (1): ŷ-এ subscript i নেই; "households" ভুল unit | p4 Eq.(1) | Confirmed issue |
| 4.11 | `Water_regime` model predictor (code), অথচ p12 "excluded" | Rmd:115 (Aus), 128 (Aman), 131 (Boro) | Confirmed issue |
| 4.12 | Fig. 2-তে ALE/স্থানিক correlation/grouped validation নেই; "Partial Dependency" | p4 Fig. 2 | Potential concern |
| 4.13 | GLM baseline intercept-only (λ.1se = λ.max; train R² = 0.000) — SI S4 আবার "Ridge λ = λ.min" লেখে | SI S4 (λ values); SI S6 | Confirmed issue |
| 4.14 | Stack-এর CV RMSE (HTML Aus 836.03) বনাম meta-learner level-one metric (816.68) আলাদা stage | HTML `yield_aus_autoML.html` (stacked ensemble CV vs glm training) | Potential concern |

**Scaling সম্পর্কে ব্যাখ্যা (4.9):** `scale(x)` প্রতিবার নিজের data-র mean/SD ব্যবহার করে। train-এ train-এর mean/SD, test-এ **test-এর** mean/SD — তাই একই feature-মান train ও test-এ আলাদা scaled value পায়। Tree-based model-এ প্রভাব কম (monotonic রূপান্তর, তবে train/test-এ ভিন্ন) কিন্তু threshold-কে ভুল জায়গায় ফেলতে পারে; GLM/DNN-এ বেশি ক্ষতি। এটা "standard practice" নয়। প্রভাব কতটা — execution ছাড়া নিশ্চিত নয় (Rule 8: R চালানো হয়নি)।

**লেখকদের পক্ষে:** Stack-এর out-of-fold ব্যবহার সঠিক; 10-fold CV-এর ফল table-এ; model count আর বিস্তারিত hyperparameter SI-তে; code public — যা প্রশংসনীয় (যদিও অসম্পূর্ণ)।

**Reviewer-এর প্রশ্ন:** Split কীভাবে? Group/spatial CV কেন নয়? Settings কোনটা সত্য? Linear baseline কেন intercept-only? Repeated random split-এ variability?

## H. সারাংশ
- **Short summary:** 80/20 random split, H2O AutoML (10-fold CV, RMSE), stacking (non-negative GLM meta-learner), RMSE (Eq.1), তারপর DALEX XAI।
- **৫ key terms:** Hold-out, Cross-validation, Leakage, Meta-learner, RMSE।
- **Takeaways:** (১) validation row-level random, union-leakage সম্ভাব্য; (২) settings তিন জায়গায় অমিল; (৩) GLM baseline আসলে নেই; (৪) per-frame scaling।
- **Key numbers:** 80/20; 10-fold; stopping_tolerance 0.0001 (paper)/0.001 (code); rounds 2/3; train rows 526/5,305/4,626; Eq.(1)।
- **পরের পেজ-প্রশ্ন:** PFI/PDP/ALE/breakdown কোন data-য় চলে (train না test)? GWC-র unit কী? Results-এ Table 4 মিলছে কি?

## Master Notes
- **Paragraph-wise:** categorical; missing/outlier; split; AutoML settings; stack; evaluation+Eq1; XAI intro।
- **Exact numbers:** 80/20; 10-fold; 0.0001/2 (paper); 0.001/3 (code); 526/5,305/4,626 train; Eq.(1)।
- **Claims & evidence:** "no limit" → code per-model; "automatically encodes" ✔; "replicable" → split missing।
- **Open checks:** H2O default `max_runtime_secs`; actual split files; outlier-removal count।
- **MSc notes:** (১) leave-district-out CV; (২) scaling শুধু source/train statistics দিয়ে; (৩) repeated splits + CI; (৪) linear baseline (OLS/Ridge ঠিকমতো) রাখুন; (৫) settings সব এক জায়গায় (config file) লিখুন।
