# MSc comparison — Ahmed et al. (2026) বনাম আপনার MSc পরিকল্পনা

**আপনার topic:** "Season-Aware and Agroclimate-Informed Explainable Spatiotemporal Machine Learning for Crop Yield Prediction and Spatial Transferability Across Bangladesh"
**Scope:** maize + Aus/Aman/Boro rice; climate ও agroecological data; explainable ML; **district-level transferability — অদেখা district-এ**; বর্তমান সংস্করণে satellite data নেই।

> নিয়ম মেনে: নিচের প্রতিটি "gap" **এই paper-এর scope-এর বাইরে** — "paper ব্যর্থ" নয় — যতক্ষণ না সেটা সত্যিকারের ভুল (যা আলাদা করে লেখা আছে)। সংখ্যাগুলো আমাদের নিজস্ব সরল check থেকে (RF default; OLS) — **paper-এর reproduction নয়**।

## 1. এই paper ইতিমধ্যে কী করে?

- তিন season (Aus/Aman/Boro) আলাদা model, **BIHS 2015** farmer-level data (13,150 row) + soil, DEM, NDVI, ERA-Interim।
- H2O AutoML stack ensemble; **random 80/20 split** ও row-level 10-fold CV; PFI/PDP/ALE + local breakdown।
- Union-গড় attribution map (Fig. 8); modeled GHG-র সাথে GW correlation।
- **শুধু ধান** (maize নেই; আপনার scope বড়)।
- **Season-wise আলাদা model** — season-aware বলতে এটুকুই (আলাদা model, আলাদা feature-window); season-জুড়ে সম্পর্ক/শেয়ারিং নেই।

## 2. কোন প্রশ্ন খোলা থাকে?

- নতুন (অদেখা) জায়গায় model কেমন চলে?
- কোন source অঞ্চল কোন target অঞ্চলে ভালো "যায়" (agroclimate-মিলের ভিত্তিতে)?
- Season-জুড়ে (যেমন Aus↔Aman) শেখা কতটা স্থানান্তর হয়?
- Growth-stage-aligned feature (কৃষকের রোপণ-তারিখ ধরে) কি calendar-window-এর চেয়ে ভালো?
- XAI-ব্যাখ্যা held-out অঞ্চলে কতটা স্থিতিশীল?
- ভালো interpretable baseline-এর তুলনায় ML-এর আসল সুবিধা কত?

## 3. Unseen district-এ transfer কি পরীক্ষা করেছে?

**না।** Objectives-এ নেই (p2); validation = row-random (p4)। Limitations-এ "অন্য অঞ্চলে প্রযোজ্য নয়" বলা আছে (p12) কিন্তু পরীক্ষা নেই। Song 2020 (cross-site transportability) cite করা, আলোচিত নয় (2.5)।
**আমাদের সরল check:** Random 5-fold R² বনাম leave-union-out (grouped) R² — Aus 0.461→**0.129**; Aman 0.574→**0.276**; Boro 0.513→**0.010** (RF 150 trees)। এটাই আপনার gap-এর **প্রাথমিক প্রমাণ**: random split-এ ভালো স্কোর unseen-area-তে অনেক কমে। (সতর্কতা: Boro-তে প্রায় শূন্য — অংশত এই feature-সেটে union-নির্ভর environmental variable নতুন union-এ extrapolate করে।)

## 4. কাছাকাছি/climate-similar source district তুলনা কি করেছে?

**না।** সব union এক পুলে; source→target pair নেই; agroclimate similarity (AEZ, rainfall regime) ব্যবহৃত নয়। (এটা এই paper-এর scope-এর বাইরে — আপনার contribution।)

## 5. Season-এর ভিন্নতা কীভাবে সামলায়?

- আলাদা model + আলাদা feature-window (Aus 7 Apr–12 Jul; Aman 12 Jul–19 Dec; Boro 1 Nov–23 Apr)।
- **সমস্যা:** window **calendar-fixed** (কৃষকের রোপণ-তারিখ নয়); Aman ও Boro window ওভারল্যাপ (1 Nov–19 Dec); Aman PFI-তে TEMP DEC-19 ৮ম (15.6%) — phenology-অমিলের লক্ষণ (F8)।
- Season-জুড়ে শেয়ারিং/transfer-learning নেই।
- `Water_regime` season-ভিত্তিক শ্রেণি (Aus সব Rainfed; Boro সব Continuous flooding) — season-পরিচয়ের proxy।

## 6. কোন ধারণা নেবেন, কোনটা এড়াবেন?

**নিন (adopt):**
- Season-wise আলাদা model + S6-এর মতো **সব algorithm-এর train/CV/test একসাথে** report।
- AutoML-ধাঁচ নিয়ন্ত্রিত তুলনা (তবে settings এক জায়গায় config-এ)।
- Local attribution-কে geographic map-এ দেখানো (union/district-গড়) — **শর্তসাপেক্ষে** (নিচে)।
- Open CSV + code প্রকাশ।

**এড়ান (avoid):**
- Random row-level split/CV (4.1)।
- Intercept-only "GLM baseline" (4.13)।
- Train-data-য় XAI (5.3); ভিন্ন run-এর model-এ local XAI (5.5)।
- Scaling আলাদা প্রতি frame-এ (4.9)।
- "Additive" claim শুধু PD≈AL দিয়ে (8.3)।
- Union-centroid-এ 250 m-এর ভ্রান্ত precision (2.7)।
- Causal ভাষা ("influencing", "impact") (1.2, 12.5)।
- Modeled GHG-কে predictor-input-সহ correlation করা (circularity, 3.1)।
- "Which table row is which" ভুল (Table 4 swap) — কোড থেকে auto-generate করুন।

## 7. আসল gap কী থেকে যায়?

**Season-aware + agroclimate-informed + grouped-spatial validation + stability-tested XAI** — চারটি একসাথে, ধান ও maize-এ, district-level transfer সহ। (এই paper-এ কোনোটিই আংশিকও নেই — বিশেষত অদেখা-এলাকা validation ও transferability-র পরিমাপ; Rule: "outside this paper's scope"।)

## তুলনা-ছক

| Research dimension | Ahmed et al. (2026) | Proposed research | Remaining gap |
|---|---|---|---|
| Crops | ধান (Aus, Aman, Boro) | maize + ধান | Maize ও ধান একই framework-এ |
| Spatial unit | Union centroid (household-row; unions 78/246–247/224) | District | District-level aggregation; unit-এর স্পষ্ট সংজ্ঞা |
| Temporal | এক বছর (2014–15), season-wise 16-day window (calendar-fixed) | Season-aware spatiotemporal | বহু-বছর; growth-stage-aligned window |
| Predictors | Management + soil + NDVI + ERA-Interim (union-এ ধ্রুব) | Climate + agroecological; satellite নেই | Agroecological zone ও climate-regime features; ব্যবস্থাপনা-ডেটা ছাড়া কতটা? |
| Validation | Row-random 80/20, row 10-fold CV | **Leave-district-out** (grouped/spatial) | **এই paper-এ নেই** — আমাদের RF check: R² Aus 0.46→0.13; Aman 0.57→0.28; Boro 0.51→0.01 |
| Unseen-area transfer | পরীক্ষিত নয় | কেন্দ্রীয় লক্ষ্য | Transferability-র পরিমাণ ও কারণ |
| Source–target similarity | নেই | Climate-similar source district তুলনা | Similarity-ভিত্তিক transfer সুবিধা আছে কি |
| Season handling | আলাদা model; calendar window; ওভারল্যাপ (Aman/Boro) | Season-aware (শেয়ারিং/transfer) | Cross-season শেখা; phenology-aligned feature |
| Baseline | GLM কার্যত intercept-only | Interpretable + ML (Rudin 2019) | Fair OLS/ridge/GAM: আমাদের OLS R² 0.28/0.38/0.20 বনাম RF 0.50/0.58/0.52 |
| XAI | PFI/PDP/ALE (train-data); breakdown (ভিন্ন model) | Explainable; held-out | Held-out-এ XAI; stability (repeated splits); effect-heterogeneity বনাম feature-মান আলাদা করা |
| Uncertainty | SD (permutation); নেই (split-এ) | Repeated splits/CI | Split-জুড়ে uncertainty |
| GHG | Modeled (CCAFS-MOT), circular correlation | scope-এর বাইরে | — (এড়ানোর সুযোগ) |
| Reproducibility | CSV + আংশিক code; split/models নেই | সম্পূর্ণ pipeline | Split + seed + config প্রকাশ |

## Concrete lessons (আপনার design-এ)

1. **Grouped/spatial CV (leave-district-out) ব্যবহার করুন।** Random split-এ ফল অতিরিক্ত ভালো দেখায় (আমাদের check)। একই district-এর row দুই দিকে ভাগ করবেন না।
2. **Feature scaling শুধু source-domain (train) statistics দিয়ে।** Test/target-এ আলাদা `scale()` করবেন না (4.9)।
3. **Feature-কে growth stage-এ align করুন, calendar date-এ নয়।** Transplanting-তারিখ থাকলে সেটা ধরে window; নইলে stage-proxy (GDD)। Aman/Boro ওভারল্যাপ এড়ান (F8)।
4. **XAI চালান held-out (target) data-য়।** PFI/ALE/SHAP — train-এ নয়; একই run-এর model-এ।
5. **সঠিক linear/interpretable baseline রাখুন (Rudin 2019)।** OLS/ridge/GAM; paper-এর intercept-only GLM নয়। ML-এর সুবিধা: আমাদের check-এ RF > OLS (R² +0.20 থেকে +0.32), কিন্তু baseline দুর্বল হলে সুবিধা অতিরঞ্জিত হয়।
6. **Repeated splits-জুড়ে uncertainty report করুন।** একক split-এর 0.9–1.5% "improvement" (F3) noise-এর সীমায়; repeated grouped CV + paired comparison + CI।
7. **Local attribution-এ "effect heterogeneity" আর "feature-value difference" আলাদা করুন।** "N-contribution positive in 51% unions" মূলত "N গড়ের উপরে" — আমাদের proxy-তে Aman crop-type 73.6% ≈ paper ">70%"। করণীয়: একই feature-মানে (বা matched sample-এ) attribution তুলনা; ICE/conditional প্রভাব; union-n/uncertainty সহ।

## অতিরিক্ত ঝুঁকি/সুযোগ

- **Unit নির্ধারণ আগে:** row = household/plot হলে (BIHS) district-aggregation আনুমানিক; district-level target হলে district-yield data (BBS/DAE) লাগতে পারে — আপনার data-source আগে ঠিক করুন।
- **Satellite ছাড়া:** union-centroid + climate/AEZ-এর সীমা — আমাদের Check 2: union-এর ভেতর environmental ভিন্নতা শূন্য — district-এও একই সীমা আসবে; অর্থাৎ agroclimate variable-এর spatial resolution-ই মূল সীমা।
- **Moran's I (আমাদের check):** union-গড় yield-এ দুর্বল কিন্তু significant spatial autocorrelation (Aman I = 0.19, Boro 0.23) — spatial CV-এর যৌক্তিকতার আরেক প্রমাণ; এবং block-size/buffer বাছাইয়ের সময় autocorrelation-range মাপুন।
- **Song 2020** (cross-site transportability) আপনার lit-review-এর কেন্দ্র; **Rudin 2019** আপনার baseline-যুক্তি।
