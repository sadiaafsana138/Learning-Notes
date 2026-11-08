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

## GHG, CH₄, N₂O, CO₂e, GWP
*(page 01)*
- **সহজ মানে:** greenhouse gas। CO₂e = সব gas-কে CO₂-র সমান ধরে একক। GWP = Global Warming Potential, ১ kg gas কত kg CO₂-র সমান warming করে।
- **উদাহরণ (সংখ্যা):** 100-year GWP ধরলে CH₄ ≈ 28–34 × CO₂, N₂O ≈ 265–298 × CO₂ (AR5 range; এই paper কোন factor নিয়েছে তা **Not reported in the provided paper, Supporting Information, or available code**)।
- **এই paper-এ:** `Total_GWP` column (kg CO₂e/ha) — CCAFS-MOT থেকে।

## Hyperparameter
*(page 02)*
- **সহজ মানে:** যে setting আপনি train-এর আগে ঠিক করে দেন (tree-এর depth, learning rate)।
- **উদাহরণ:** max_depth = 5 বনাম 20।
- **এই paper-এ:** SI Table S2/S4।

## Model-agnostic
*(page 01)*
- **সহজ মানে:** যেকোনো model-এর ভেতর না দেখে শুধু input→output দেখে ব্যাখ্যা করা।

## PSU (Primary Sampling Unit)
*(page 02)*
- **সহজ মানে:** survey-র প্রথম ধাপে বাছাই করা ছোট এলাকা (গ্রাম/মহল্লা)। এখানে 325টা।
- **খেয়াল:** একই PSU-র ঘরগুলো একই মাটি/আবহাওয়া/আচরণ share করে → observations independent নয়।

## Resampling (250 m-এ)
*(page 02)*
- **সহজ মানে:** একটা raster-এর pixel-এর মাপ বদলে অন্য raster-এর সাথে মেলানো।
- **উদাহরণ:** 12 km pixel = ~(12000/250)² = 2304 টা 250 m pixel-এ ভাগ; সবকটায় প্রায় একই (smoothed) মান।
- **এই paper-এ:** ERA-Interim → 250 m (TPS)। **খেয়াল:** নতুন তথ্য তৈরি হয় না।

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

## XAI (Explainable AI)
*(page 01)*
- **সহজ মানে:** black-box model কেন এই উত্তর দিল তা বোঝার পদ্ধতি।
- **কীভাবে কাজ করে:** যেমন একটা feature-এর value এলোমেলো করে (shuffle) দেখি error কতটা বাড়ে — বাড়লে feature গুরুত্বপূর্ণ।
- **এই paper-এ:** PFI, PDP, ALE, breakdown (p5)।
- **খেয়াল রাখতে হবে:** XAI model-এর আচরণ বলে, বাস্তব জগতের কারণ-ফল নয়।

