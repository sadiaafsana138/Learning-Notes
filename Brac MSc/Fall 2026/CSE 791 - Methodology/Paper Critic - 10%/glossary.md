# Glossary (alphabetical; প্রতিটা page-এর section C থেকে auto-generated)

## AutoML (Automated Machine Learning)
*(page 01)*
- **সহজ মানে:** অনেকগুলো model আর hyperparameter নিজে নিজে try করে সেরাটা বেছে দেওয়া একটা tool।
- **কীভাবে কাজ করে:** ধরুন আপনি ৬টা algorithm (GLM, DRF, GBM...) চালাবেন, প্রত্যেকটার ১০০ রকম setting। হাতে করলে ৬০০ বার। AutoML সেটা loop-এ চালায়, cross-validation RMSE দিয়ে rank করে leaderboard বানায়।
- **এই paper-এ:** H2O AutoML (R), p4 §2.3.1। সব season-এ stacked ensemble best।
- **খেয়াল রাখতে হবে:** AutoML মানে "ভালো validation" নয়; validation split ঠিক না হলে (p4 এ random row split) সব model-ই অতিরিক্ত ভালো দেখাতে পারে।

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

## CCAFS-MOT
*(page 03)*
- **সহজ মানে:** কৃষি-জমির GHG হিসাবের একটা tool/calculator (CGIAR); input দিলে emission estimate দেয়।
- **ছোট উদাহরণ:** N rate বেশি → N₂O emission factor ধরে বেশি N₂O (সরল ছবি; আসল সূত্র এই paper-এ নেই)।
- **এই paper-এ:** `Total_GWP` (kg CO₂e/ha) তৈরি।
- **খেয়াল:** Tool-এর input-ই যদি পরে "predictor" হিসেবে যায় → circular।

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

## Generalized Linear Model (GLM) / Ridge, λ
*(page 04)*
- **সহজ মানে:** linear regression-এর সাধারণ রূপ; regularization (Ridge) coefficient ছোট রাখে।
- **ছোট উদাহরণ:** λ বড় → coefficient প্রায় 0 → prediction ≈ গড়।
- **এই paper-এ:** baseline; SI S4: λ.max = λ.1se (Aus 50,164; Aman 52,782; Boro 21,265) ⇒ সব coefficient ≈ 0, **training R² = 0.000** (S6)।
- **খেয়াল:** এটা আসলে "intercept-only" মডেল; (Seed F4)।

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

## Kriging / Multi-Gaussian Kriging
*(page 03)*
- **সহজ মানে:** কাছের নমুনা-বিন্দুগুলোর ওজনযুক্ত গড় দিয়ে অজানা জায়গার মান অনুমান; ওজন ঠিক হয় distance + spatial correlation (variogram) দিয়ে।
- **ছোট উদাহরণ (সরল IDW দিয়ে বোঝানো; kriging-এ ওজন variogram থেকে আসে):** ১ km দূরে pH 6.0, ৩ km দূরে pH 7.0 → ওজন 1 ও 1/3 → 0.75, 0.25 → অনুমান 0.75×6+0.25×7 = **6.25** (`work/worked_examples.out`)।
- **এই paper-এ:** SRDI 31,787 point → 250 m soil map (pH, SOC, N, P, K, S, B, Zn)।
- **খেয়াল:** (১) kriging smooth করে; (২) variance বাদ দিয়ে শুধু গড় ব্যবহার; (৩) পুরোনো sample।

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

## XAI (Explainable AI)
*(page 01)*
- **সহজ মানে:** black-box model কেন এই উত্তর দিল তা বোঝার পদ্ধতি।
- **কীভাবে কাজ করে:** যেমন একটা feature-এর value এলোমেলো করে (shuffle) দেখি error কতটা বাড়ে — বাড়লে feature গুরুত্বপূর্ণ।
- **এই paper-এ:** PFI, PDP, ALE, breakdown (p5)।
- **খেয়াল রাখতে হবে:** XAI model-এর আচরণ বলে, বাস্তব জগতের কারণ-ফল নয়।

