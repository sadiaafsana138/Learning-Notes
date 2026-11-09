# Glossary (alphabetical; প্রতিটা page-এর section C থেকে auto-generated)

## Accumulated Local Effects (ALE)
*(page 05)*
- **সহজ মানে:** feature-কে ছোট ছোট bin-এ ভাগ করে প্রতি bin-এ শুধু ছোট পরিবর্তনে prediction-এর পার্থক্য জমা (accumulate) করা, তারপর center করা।
- **ছোট উদাহরণ (Python):** bin 1 (0–100): row-পার্থক্য 200, 300 → গড় 250; bin 2: 100, 60 → গড় 80। জমা: 250, 330 → ওজনযুক্ত গড় 290 → centered: **−40, +40**।
- **এই paper-এ:** Fig. 7-এ কমলা রেখা (AL)।
- **খেয়াল:** bin ছোট হলে অস্থির; local difference মানে model যেখানে data আছে সেখানেই দেখে।

## Additive model
*(page 08)*
- **সহজ মানে:** model যেখানে feature-এর প্রভাবগুলো যোগ হয়, একটা অন্যটার উপর নির্ভর করে না: f(x) = f₁(x₁) + f₂(x₂) + …।
- **ছোট উদাহরণ:** yield = 2000 + 8·N + 300·(HYV) → N বাড়ালে সবসময় +8, জাত-নির্বিশেষে। Non-additive: HYV-তে +10, local-এ +4 — **interaction**।
- **এই paper-এ:** "stack-ensemble is additive" claim।
- **খেয়াল:** PD ≈ AL additivity-র প্রমাণ নয়; H-statistic লাগে।

## Alternate Wetting and Drying (AWD)
*(page 11)*
- **সহজ মানে:** ধানের জমি সব সময় জলমগ্ন না রেখে মাঝে মাঝে শুকিয়ে দেওয়া — মিথেন কমে, জল বাঁচে।
- **ছোট উদাহরণ:** ১০০ দিনের মধ্যে ৭০ দিন জল বনাম ৪০ দিন জল ⇒ anaerobic সময় কম ⇒ CH₄ কম (সংখ্যাগুলো বোঝানোর কাল্পনিক)।
- **এই paper-এ:** Discussion-এ Boro ব্যাখ্যায়; data/মডেলে নেই।

## ANOVA (F-test)
*(page 05)*
- **সহজ মানে:** একাধিক group-এর গড় আলাদা কিনা পরীক্ষা: F = (group-এর মধ্যে variance)/(group-এর ভেতরের variance)।
- **ছোট উদাহরণ:** ৩ group (3000–3200, 3400–3600, 4000–4200), 3টা করে row → F = **76.0** (df 2,6)।
- **এই paper-এ:** season-ভেদে yield (F=3012), crop type-ভেদে।
- **খেয়াল:** independence ধরে নেয় — এখানে clustered।

## AutoML (Automated Machine Learning)
*(page 01)*
- **সহজ মানে:** অনেকগুলো model আর hyperparameter নিজে নিজে try করে সেরাটা বেছে দেওয়া একটা tool।
- **কীভাবে কাজ করে:** ধরুন আপনি ৬টা algorithm (GLM, DRF, GBM...) চালাবেন, প্রত্যেকটার ১০০ রকম setting। হাতে করলে ৬০০ বার। AutoML সেটা loop-এ চালায়, cross-validation RMSE দিয়ে rank করে leaderboard বানায়।
- **এই paper-এ:** H2O AutoML (R), p4 §2.3.1। সব season-এ stacked ensemble best।
- **খেয়াল রাখতে হবে:** AutoML মানে "ভালো validation" নয়; validation split ঠিক না হলে (p4 এ random row split) সব model-ই অতিরিক্ত ভালো দেখাতে পারে।

## Base learner vs meta-learner coefficient
*(page 09)*
- **সহজ মানে:** meta-learner প্রতিটি base model-এর prediction-কে ওজন দেয়; ওজন 0 মানে model-টি stack-এ অংশ নেয় না।
- **এই paper-এ:** HTML metalearner table (Aus: 958 model-এর মধ্যে বেশিরভাগ 0.0000)।

## BIHS (Bangladesh Integrated Household Survey)
*(page 02)*
- **সহজ মানে:** IFPRI-র নেওয়া ৬৫০০ ঘরের জাতীয় household survey (2015)।
- **খেয়াল:** এটা cross-section (এক বছর), তাই "temporal" ভিন্নতা নেই; season ভিন্নতা আছে।

## Black-box model
*(page 02)*
- **সহজ মানে:** যে model-এর ভেতরের হিসাব মানুষ সহজে পড়তে পারে না (deep net, ensemble)।
- **উদাহরণ:** ৫০০ গাছের forest — প্রতি গাছের সিদ্ধান্ত পড়া অসম্ভব।
- **এই paper-এ:** stacking-কেই black-box ধরে post-hoc XAI।
- **খেয়াল:** Rudin 2019 বলেন high-stakes-এ interpretable model ভালো।

## Boxplot
*(page 06)*
- **সহজ মানে:** বাক্সের ভেতরের দাগ = median; বাক্স = 25%–75%; গোঁফ = সাধারণ range; বিন্দু = outlier।
- **খেয়াল:** boxplot গড় দেখায় না; sample size দেখায় না (hybrid Aus-এ মাত্র 21 row)।

## Breakdown plot (iBreakDown)
*(page 05)*
- **সূত্র:** f(x*) = v₀ + Σ_j contribution_j (v₀ = গড় prediction)।
- **ছোট উদাহরণ:** গড় yield 3105 + N 250 + crop type 120 + field duration (−40) + P 60 + K 30 + বাকি 15 = **3540**।
- **এই paper-এ:** প্রতি row-এর contribution, union-গড় করে map (Fig. 8)।
- **খেয়াল:** order-নির্ভর; "contribution" ≠ causal effect; union-গড় feature-value-র পার্থক্য আর model-এর প্রকৃত "response"-এর পার্থক্য মিশিয়ে ফেলে।

## CCAFS-MOT
*(page 03)*
- **সহজ মানে:** কৃষি-জমির GHG হিসাবের একটা tool/calculator (CGIAR); input দিলে emission estimate দেয়।
- **ছোট উদাহরণ:** N rate বেশি → N₂O emission factor ধরে বেশি N₂O (সরল ছবি; আসল সূত্র এই paper-এ নেই)।
- **এই paper-এ:** `Total_GWP` (kg CO₂e/ha) তৈরি।
- **খেয়াল:** Tool-এর input-ই যদি পরে "predictor" হিসেবে যায় → circular।

## Collinearity / confounding
*(page 11)*
- **সহজ মানে:** দুটি predictor একসাথে ওঠানামা করে বলে আলাদা প্রভাব আলাদা করা যায় না। Confounding = অন্য একটি factor দুটি variable-কেই প্রভাবিত করে।
- **ছোট উদাহরণ:** যে কৃষক বেশি N দেয়, সে বেশি P-ও দেয় ⇒ P এবং GHG দুটোই বাড়ে; P নিজে দায়ী নয়।

## Cross-validation (10-fold)
*(page 04)*
- **সহজ মানে:** train data-কে ১০ ভাগ করে ৯ ভাগে train, ১ ভাগে validate — ১০ বার।
- **ছোট উদাহরণ:** 526 train row → প্রতি fold-এ প্রায় 52–53 row validate।
- **এই paper-এ:** H2O AutoML `nfolds=10`; model selection আর stacking-এর out-of-fold prediction।
- **খেয়াল:** random fold ≠ spatial fold; একই union-এর row দুই fold-এ ভাগ হয়ে যায়।

## Data leakage (এখানে: identity/spatial leakage)
*(page 04)*
- **সহজ মানে:** test-এর তথ্য আসলে train-এ আগে থেকে "চোখে পড়েছে" — তাই স্কোর বাড়াবাড়ি ভালো।
- **ছোট উদাহরণ:** একই union-এর ৫০টা row-এর ৪০টা train-এ, ১০টা test-এ; model union-এর NDVI/soil-সংমিশ্রণ দেখে ওই union-এর গড় yield জানে।
- **এই paper-এ:** প্রমাণ নয়, সম্ভাবনা; আমাদের simulation-এ ৯৭–৯৯.৮% test row-এর union train-এ আছে।
- **খেয়াল:** (Rule 6) leakage প্রমাণের জন্য আসল split লাগে।

## DEM / SRTM
*(page 03)*
- **সহজ মানে:** ভূমির উচ্চতার map; SRTM 90 m।
- **খেয়াল:** বাংলাদেশের floodplain-এ উচ্চতা ১–১০ m-এর মধ্যে — ছোট পার্থক্যই বড় (বন্যা/drainage)।

## DRF / XRT / GBM / XGBoost / DNN
*(page 04)*
- **DRF:** অনেক decision tree-র গড় (bootstrap + random feature)। **XRT:** DRF-এর চেয়েও random split। **GBM:** tree-গুলো ধাপে ধাপে আগের ভুল ঠিক করে। **XGBoost:** GBM-এর দ্রুত/regularized সংস্করণ। **DNN:** multi-layer neural net।
- **এই paper-এ:** Table S1; best-of-family S6-এ।
- **খেয়াল:** DRF-ই সাধারণত শক্ত baseline (S6-এ DRF সবচেয়ে ভালো single)।

## Drop-out loss
*(page 07)*
- **সহজ মানে:** feature বাদ/shuffle করলে model-এর error যতটা বাড়ে।
- **খেয়াল:** DALEX-এ default type="raw"; এখানে "difference" (loss − baseline loss)।

## Ecological (aggregate) correlation
*(page 05)*
- **সহজ মানে:** group-গড়ের (যেমন union-গড়) correlation, individual-এর নয়; সাধারণত বেশি দেখায়।
- **উদাহরণ:** Aus yield~P: union-গড়ে r = 0.625, row-level 0.402 (Check 7)।

## Explained variance (EVar)
*(page 06)*
- **সহজ মানে:** 1 − Var(error)/Var(y); R²-এর মতো, কিন্তু গড় ভুল (bias) বাদ দেয়।
- **উদাহরণ:** `work/worked_examples2.out`: R² 0.820, EVar 0.827 (bias −66.7 থাকায়)।

## exTZONE
*(page 07)*
- **সহজ মানে:** extreme temperature zone (T1E1…T5E4) — একটা categorical code (SI Fig. S6e)।
- **খেয়াল:** উৎস/সংজ্ঞা paper-এ নেই ("Not reported…")।

## Generalized Linear Model (GLM) / Ridge, λ
*(page 04)*
- **সহজ মানে:** linear regression-এর সাধারণ রূপ; regularization (Ridge) coefficient ছোট রাখে।
- **ছোট উদাহরণ:** λ বড় → coefficient প্রায় 0 → prediction ≈ গড়।
- **এই paper-এ:** baseline; SI S4: λ.max = λ.1se (Aus 50,164; Aman 52,782; Boro 21,265) ⇒ সব coefficient ≈ 0, **training R² = 0.000** (S6)।
- **খেয়াল:** এটা কার্যত "intercept-only"। HTML (Aus) দেখায় Ridge λ = 14,082 নির্বাচিত — এটা path-এর সবচেয়ে ছোট λ (λ.min), আর path শুরু λ.max = 50,164 থেকে; অর্থাৎ λ-search ছোট λ-তে যায়নি, ফলে training R² = 0.0001। (Seed F4: **revised** — "λ.1se = λ.max" সত্য, কিন্তু "Ridge λ = λ.min" বিরোধ নয়; সমস্যা হলো λ-path-এ ছোট λ না থাকা; তাই সত্যিকারের linear baseline নেই। আমাদের OLS check: p2/code-audit।)

## Geographically weighted (GW) correlation, bi-square kernel
*(page 05)*
- **সূত্র:** ওজন w(d) = (1 − (d/b)²)² যখন d < b, নাহলে 0; ওজনযুক্ত Pearson correlation।
- **ছোট উদাহরণ:** b = 10: d = 2 → 0.9216; d = 5 → 0.5625; d = 10 → 0।
- **এই paper-এ:** Total GWP বনাম N, P, K, GD; adaptive bandwidth (নিকটতম k প্রতিবেশী); Fig. 9।
- **খেয়াল:** local correlation অনেক কম sample-এ চলে → অস্থির; multiple-testing; spatial autocorrelation।

## Geographically Weighted Regression (GWR) / GW correlation
*(page 09)*
- **সহজ মানে:** একটা বিশ্বব্যাপী formula-র বদলে প্রতি জায়গার জন্য কাছের পয়েন্টগুলোকে বেশি ওজন দিয়ে আলাদা regression/correlation।
- **ছোট উদাহরণ:** ঢাকার union-এর জন্য ঢাকার কাছাকাছি ৪০টা union-কে ওজন (bi-square: 0.92, 0.56, 0), দূরেরগুলো 0।
- **এই paper-এ:** Total GWP ~ N/P/K/GD, adaptive bandwidth (AICc)।
- **খেয়াল:** bandwidth-সংবেদী; পুনঃপুনঃ test; কম local sample।

## GHG, CH₄, N₂O, CO₂e, GWP
*(page 01)*
- **সহজ মানে:** greenhouse gas। CO₂e = সব gas-কে CO₂-র সমান ধরে একক। GWP = Global Warming Potential, ১ kg gas কত kg CO₂-র সমান warming করে।
- **উদাহরণ (সংখ্যা):** 100-year GWP ধরলে CH₄ ≈ 28–34 × CO₂, N₂O ≈ 265–298 × CO₂ (AR5 range; এই paper কোন factor নিয়েছে তা **Not reported in the provided paper, Supporting Information, or available code**)।
- **এই paper-এ:** `Total_GWP` column (kg CO₂e/ha) — CCAFS-MOT থেকে।

## Global Warming Potential (GWP), CO₂e
*(page 03)*
- **সহজ মানে:** বিভিন্ন gas-কে CO₂-র সমান warming-এ রূপান্তর।
- **ছোট উদাহরণ (illustrative):** 10 kg CH₄ × 28 + 0.5 kg N₂O × 265 = **412.5 kg CO₂e** (AR5-style factor; এই paper কোন factor নিয়েছে তা Not reported…)।

## Hold-out test set
*(page 04)*
- **সহজ মানে:** train-এ ব্যবহার না করা, শেষে model-কে "পরীক্ষা"-য় বসানোর data।
- **ছোট উদাহরণ:** 677 row-এর 80% ≈ 541.6 train, 20% ≈ 135.4 test।
- **এই paper-এ:** 80/20 random।
- **খেয়াল:** "hold-out" তখনই সৎ, যখন test row-গুলো train row-র সাথে identity share করে না (এখানে union share করে)।

## Hybrid rice vs HYV vs Local
*(page 11)*
- **সহজ মানে:** Hybrid = F1 সংকর (বেশি ফলন, প্রতি মৌসুমে নতুন বীজ লাগে); HYV = আধুনিক উচ্চফলনশীল জাত (ইনব্রিড); Local = স্থানীয় ঐতিহ্যবাহী জাত।
- **এই paper-এ:** crop type (3 স্তর), Boro-তে local নেই।
- **খেয়াল:** জাতভেদ গড় yield-পার্থক্য আংশিক জমি-ব্যবস্থাপনার পার্থক্য (সেচযোগ্য ভালো জমিতে hybrid)।

## Hyperparameter
*(page 02)*
- **সহজ মানে:** যে setting আপনি train-এর আগে ঠিক করে দেন (tree-এর depth, learning rate)।
- **উদাহরণ:** max_depth = 5 বনাম 20।
- **এই paper-এ:** SI Table S2/S4।

## Hyperparameter tuning / Random grid search
*(page 04)*
- **সহজ মানে:** setting-এর অনেক সংমিশ্রণ এলোমেলোভাবে try করে সেরাটা বাছা।
- **উদাহরণ:** GBM-এ max_depth ∈ {3..17} (15 value) × min_rows ∈ 6 value = 90 সংমিশ্রণ থেকে random কয়েকটা (SI S4)।
- **এই paper-এ:** GBM, XGBoost, DNN।

## Interaction / H-statistic
*(page 08)*
- **সহজ মানে:** দুই feature একসাথে যে বাড়তি প্রভাব ফেলে যা আলাদা প্রভাবের যোগফল নয়।
- **সূত্র (সংক্ষেপে):** H²_j = (j-এর অংশবিশেষ-নির্ভর variance যা শুধু j-এর main effect ব্যাখ্যা করে না)/ (পুরো variance); 0 = interaction নেই, 1 = পুরোটাই interaction।
- **এই paper-এ:** `iml::Interaction` চালানো, ফল report নেই।
- **খেয়াল:** H-statistic ব্যয়বহুল ও correlated feature-এ বিভ্রান্তিকর হতে পারে।

## Kriging / Multi-Gaussian Kriging
*(page 03)*
- **সহজ মানে:** কাছের নমুনা-বিন্দুগুলোর ওজনযুক্ত গড় দিয়ে অজানা জায়গার মান অনুমান; ওজন ঠিক হয় distance + spatial correlation (variogram) দিয়ে।
- **ছোট উদাহরণ (সরল IDW দিয়ে বোঝানো; kriging-এ ওজন variogram থেকে আসে):** ১ km দূরে pH 6.0, ৩ km দূরে pH 7.0 → ওজন 1 ও 1/3 → 0.75, 0.25 → অনুমান 0.75×6+0.25×7 = **6.25** (`work/worked_examples.out`)।
- **এই paper-এ:** SRDI 31,787 point → 250 m soil map (pH, SOC, N, P, K, S, B, Zn)।
- **খেয়াল:** (১) kriging smooth করে; (২) variance বাদ দিয়ে শুধু গড় ব্যবহার; (৩) পুরোনো sample।

## Local attribution / contribution
*(page 08)*
- **সহজ মানে:** একটি specific row-এর prediction-এ কোন feature কতটা যোগ/বিয়োগ করল।
- **ছোট উদাহরণ:** গড় 3105 + N 250 + crop 120 + FD (−40) + P 60 + K 30 + বাকি 15 = 3540 (পরিমাণ বোঝানোর কাল্পনিক উদাহরণ)।
- **এই paper-এ:** break_down → union-গড়।
- **খেয়াল:** attribution = model-এর আচরণ; এটা "feature-মানের পার্থক্য" ও "প্রভাবের পার্থক্য" মেশায়।

## Local XAI বনাম GW regression
*(page 09)*
- **সহজ মানে:** GW regression = data-র local সম্পর্ক; Local XAI = model-এর local আচরণ। একটা model-কে ব্যাখ্যা করে, আরেকটা data-কে।
- **এই paper-এ:** Discussion বলছে XAI সীমা কাটায়; প্রমাণ নেই।

## Meta-learner (non-negative GLM)
*(page 04)*
- **সহজ মানে:** base model-এর prediction-কে input ধরে যে ছোট model চূড়ান্ত prediction বানায়; ওজন ≥ 0।
- **এই paper-এ:** H2O default (HTML "Metalearner algorithm: glm")।

## Model-agnostic
*(page 01)*
- **সহজ মানে:** যেকোনো model-এর ভেতর না দেখে শুধু input→output দেখে ব্যাখ্যা করা।

## MODIS NDVI (MOD13Q1)
*(page 03)*
- **সহজ মানে:** satellite দিয়ে গাছের "সবুজতা" মাপার সূচক; 16-day composite, 250 m।
- **উদাহরণ:** NDVI 0.2 = প্রায় খালি জমি/জল; 0.8 = ঘন সবুজ ধান।
- **এই paper-এ:** প্রতি season-এর 16-day সময়ে NDVI feature।
- **খেয়াল:** মেঘ, ছোট জমি (250 m pixel-এ মিশ্র ফসল), union-centroid-এ pixel।

## Nitrogen-use efficiency (NUE)
*(page 10)*
- **সহজ মানে:** দেওয়া N-এর কত অংশ ধান আসলে নিল (বা প্রতি kg N-এ কত kg grain)।
- **ছোট উদাহরণ:** 100 kg N/ha দিলে 4000 kg yield, N ছাড়া 2500 ⇒ agronomic efficiency = (4000 − 2500)/100 = **15 kg grain/kg N**।
- **এই paper-এ:** শুধু Discussion-এ উল্লেখ; মাপা হয়নি।
- **খেয়াল:** NUE না মেপে "efficiency" নিয়ে সুপারিশ করা দুর্বল।

## Non-stationarity (স্থানিক)
*(page 08)*
- **সহজ মানে:** একই সম্পর্ক (যেমন N→GHG) জায়গাভেদে আলাদা।
- **খেয়াল:** বাস্তব non-stationarity বনাম sample-কম থেকে আসা noise আলাদা করতে test দরকার।

## N₂O ও CH₄ উৎস (সংক্ষেপে)
*(page 10)*
- **CH₄:** জলমগ্ন (anaerobic) জমিতে জৈবিক বিয়োজন থেকে; **N₂O:** nitrification/denitrification থেকে, N-সারের পরিমাণের সাথে বাড়ে। দুটোর পদ্ধতি আলাদা, তাই Total GWP একটাই সংখ্যায় দুই ভিন্ন প্রক্রিয়া মিশিয়ে দেয়।

## Observed vs predicted (1:1) plot
*(page 07)*
- **সহজ মানে:** x = আসল মান, y = prediction; আদর্শ হলে সব বিন্দু 45° রেখার উপর।
- **খেয়াল:** slope < 1 মানে shrinkage।

## Partial correlation
*(page 11)*
- **সহজ মানে:** তৃতীয় কোনো variable-এর প্রভাব সরিয়ে দুই variable-এর সম্পর্ক।
- **ছোট উদাহরণ (আমাদের data, Boro row):** r(GWP, P) = 0.228, কিন্তু N-কে বাদ দিলে partial r = **−0.016** ⇒ P-র নিজস্ব ভূমিকা প্রায় নেই; আগের 0.228 ছিল N-এর ছায়া।
- **এই paper-এ:** ব্যবহৃত হয়নি; আমাদের check।
- **খেয়াল:** partial r-ও causal নয়; N-র সাথে সম্পর্ক রৈখিক ধরে।

## Partial Dependence Plot (PDP)
*(page 05)*
- **সূত্র:** ĝ_j(z) = (1/n) Σ_{i=1}^{n} f(z, x_{i,−j}) — j-তম feature-কে z-তে বসিয়ে বাকিগুলো যেমন আছে রেখে model-এর prediction গড়।
- **ছোট উদাহরণ:** ৪ row-এ N=100 বসালে prediction 3000, 3400, 3800, 4200 → PD = **3600**।
- **এই paper-এ:** Fig. 7 (নীল রেখা = PD)।
- **খেয়াল:** feature correlated হলে অবাস্তব combination; ICE দেখা হয়নি।

## Pearson correlation (local)
*(page 10)*
- **সূত্র:** r = Σ(xᵢ − x̄)(yᵢ − ȳ)/√(Σ(xᵢ − x̄)² Σ(yᵢ − ȳ)²); GW version-এ ওজনযুক্ত গড়/variance (bi-square)।
- **ছোট উদাহরণ:** x = [50,100,150,200], y = [900,1100,1250,1500] ⇒ **r = 0.995** (Python)।
- **এই paper-এ:** Total GWP vs N/P/K/GD; Aus global r (union-গড়) N = 0.816 ⇒ r² = **0.67** (variance-এর ~67%)।
- **খেয়াল:** r নির্দেশ করে সরলরেখীয় সম্পর্ক; r ≠ প্রভাব।

## Permutation Feature Importance (PFI) — গভীরে
*(page 05)*
- **সহজ মানে:** একটা feature-এর মান row-গুলোর মধ্যে এলোমেলো করে সাজাই; error কতটা বাড়ল সেটাই গুরুত্ব।
- **ছোট উদাহরণ (সংখ্যা):** train RMSE 404.8; N-rate shuffle → RMSE 766.3 → loss (difference) = 361.5; top feature-এর 100% ধরলে K-rate (176.3)-এর গুরুত্ব = 176.3/361.5 = **48.8%**।
- **এই paper-এ:** DALEX `variable_importance(type="difference")`, **train data-তে**; Table S7–S9, Fig. 6।
- **খেয়াল:** correlated feature (N, P, K rate) থাকলে এক feature shuffle করলে অসম্ভব combination তৈরি হয় → গুরুত্ব বিকৃত; test data-তে চালানো উচিত।

## PSU (Primary Sampling Unit)
*(page 02)*
- **সহজ মানে:** survey-র প্রথম ধাপে বাছাই করা ছোট এলাকা (গ্রাম/মহল্লা)। এখানে 325টা।
- **খেয়াল:** একই PSU-র ঘরগুলো একই মাটি/আবহাওয়া/আচরণ share করে → observations independent নয়।

## Reanalysis (ERA-Interim)
*(page 03)*
- **সহজ মানে:** অতীতের weather observation আর model মিলিয়ে বানানো গ্রিডেড আবহাওয়া-ডাটা (বাস্তব মাপ নয়)।
- **উদাহরণ:** একটা 12 km × 12 km cell-এ একটাই তাপমাত্রা; ওই cell-এর ভেতরে ৫ km দূরে দুই গ্রামের তফাত দেখা যায় না।
- **এই paper-এ:** rainfall ও temperature, 2014–2015।
- **খেয়াল:** Reanalysis rainfall সাধারণত স্থানীয় বৃষ্টির peak কম দেখায়।

## Regression to the mean / shrinkage
*(page 06)*
- **সহজ মানে:** model চরম মানের prediction কম চরম করে দেয় — কম yield-কে একটু বেশি, বেশি yield-কে একটু কম।
- **ছোট উদাহরণ:** observed 6000 → predicted 5200; observed 1500 → predicted 2300। Predicted-vs-observed লাইনের slope < 1।
- **এই paper-এ:** Fig. 5 সব season-এ।
- **খেয়াল:** এটা শুধু "ensemble-এর দোষ" নয়; noisy label (farmer-reported yield) থাকলেও হয়। Bias correction (isotonic/linear recalibration) আলোচনা নেই।

## Relative importance (%)
*(page 07)*
- **সহজ মানে:** সবচেয়ে বড় loss-কে 100 ধরে বাকিগুলোর আনুপাতিক মান।
- **ছোট উদাহরণ:** 236.4/361.5 × 100 = **65.4%** (Aus crop type); 176.3/361.5 = **48.8%** (K-rate)।
- **এই paper-এ:** Table S7–S9, "> 10%" cut-off Fig. 6-এ feature বাছাইয়ের জন্য।
- **খেয়াল:** relative হওয়ায় season-জুড়ে তুলনা নেই; 10% cut-off arbitrary।

## Resampling (250 m-এ)
*(page 02)*
- **সহজ মানে:** একটা raster-এর pixel-এর মাপ বদলে অন্য raster-এর সাথে মেলানো।
- **উদাহরণ:** 12 km pixel = ~(12000/250)² = 2304 টা 250 m pixel-এ ভাগ; সবকটায় প্রায় একই (smoothed) মান।
- **এই paper-এ:** ERA-Interim → 250 m (TPS)। **খেয়াল:** নতুন তথ্য তৈরি হয় না।

## RMSE, MAE, RMSLE, R²
*(page 04)*
- **RMSE:** বড় ভুলকে বেশি শাস্তি দেয়, kg/ha-এ। **MAE:** গড় পরম ভুল। **RMSLE:** log-scale ভুল; আপেক্ষিক ভুল বোঝায়। **R²:** variance-এর কত অংশ model ব্যাখ্যা করে।
- **ছোট উদাহরণ (D-তে পুরো হিসাব):** y = 3000/4000/5000, ŷ = 3200/3600/5400 → RMSE 346.4, MAE 333.3, R² 0.820।

## Stacked ensemble
*(page 01)*
- **সহজ মানে:** অনেক model-এর prediction আরেকটা model (meta-learner) দিয়ে জোড়া লাগানো।
- **ছোট উদাহরণ:** model A বলল 4000, B বলল 4400, meta-learner weights 0.6/0.4 → 0.6×4000+0.4×4400 = 4160।
- **এই paper-এ:** p4 §2.3.1; p9 Discussion-এ "১–৪% RMSE improvement vs DRF"।
- **খেয়াল রাখতে হবে:** Improvement ছোট হলে repeated split ছাড়া noise আর real gain আলাদা করা যায় না।

## Stacking / stacked generalization (গভীর)
*(page 02)*
- **সহজ মানে:** আলাদা ধরনের model-দের prediction-কে feature বানিয়ে আরেকটা model train করা।
- **ছোট উদাহরণ:** ধরুন ৩ model-এর out-of-fold prediction একটা row-এ 3000, 3600, 3300; meta weights 0.5, 0.2, 0.3 → 0.5×3000+0.2×3600+0.3×3300 = 3210।
- **এই paper-এ:** p4: দুটো stack (All models / Best of family); meta-learner = non-negative GLM।
- **খেয়াল রাখতে হবে:** Base model-গুলো যদি একই leakage-এ ভোগে, stack সেটা কমায় না।

## Thin Plate Spline (TPS)
*(page 03)*
- **সহজ মানে:** বিন্দুর মানের মধ্য দিয়ে একটা মসৃণ পৃষ্ঠ টানা — যেন পাতলা ধাতুর পাত বাঁকানো।
- **উদাহরণ:** 4টা weather cell-এর মাঝে একটা 250 m point-এর মান smooth interpolation-এ আসে।
- **এই paper-এ:** weather 12 km → 250 m, R `fields`।
- **খেয়াল:** Interpolation নতুন তথ্য আনে না।

## Urea broadcast / deep placement
*(page 10)*
- **সহজ মানে:** broadcast = জমিতে ছিটিয়ে দেওয়া (বন্যার জলে লোকসান বেশি); deep placement = ঢেলা (briquette) করে গাছের শিকড়ের কাছে মাটিতে গুঁজে দেওয়া।
- **খেয়াল:** এই data-তে এ তথ্য নেই।

## XAI (Explainable AI)
*(page 01)*
- **সহজ মানে:** black-box model কেন এই উত্তর দিল তা বোঝার পদ্ধতি।
- **কীভাবে কাজ করে:** যেমন একটা feature-এর value এলোমেলো করে (shuffle) দেখি error কতটা বাড়ে — বাড়লে feature গুরুত্বপূর্ণ।
- **এই paper-এ:** PFI, PDP, ALE, breakdown (p5)।
- **খেয়াল রাখতে হবে:** XAI model-এর আচরণ বলে, বাস্তব জগতের কারণ-ফল নয়।

## Yield-scaled emission (GHG intensity)
*(page 09)*
- **সহজ মানে:** প্রতি টন ফলনে কত CO₂e: Emission/Yield।
- **ছোট উদাহরণ:** 4000 kg CO₂e/ha ÷ 4000 kg yield = 1.00; 4400 ÷ 5000 = **0.88** — বেশি emission হলেও বেশি yield-এ intensity কম হতে পারে।
- **এই paper-এ:** CSV-তে `Emission_Intensity` column আছে (analysis-এ ব্যবহৃত নয়); text-এ নেই।
- **খেয়াল:** "ভালো nutrient management = বেশি yield + কম GHG" দাবির জন্য এটাই প্রয়োজনীয় মেট্রিক।

## Yield-scaled emission (পুনরাবৃত্তি, গভীরে)
*(page 11)*
- **ছোট উদাহরণ (Boro; CSV গড়, `python`):** HYV 3734.4 ÷ 5442.9 = **0.69**; Hybrid 3861.9 ÷ 6080.7 = **0.64** kg CO₂e/kg grain — hybrid-এ আনুমানিক ৭% কম intensity, যদিও total GWP বেশি।
- **খেয়াল:** গড়ের অনুপাত ≠ গড় অনুপাত; row-level `Emission_Intensity` column ব্যবহার করা উচিত।

