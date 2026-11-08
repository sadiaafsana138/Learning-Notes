# Page 02 — Introduction (বাকি অংশ) + §2.1 Data (BIHS, spatial data)

← আগের: [page-01](page-01.md) | পরের: [page-03](page-03.md) →

## A. এই পেজে কী আছে
- Bangladesh-এর ধান/GHG context, "linear model-এর সীমাবদ্ধতা", stacking আর AutoML-এর যুক্তি, XAI-এর gap, তারপর **§2.1.1 BIHS data**, **§2.1.2 spatial data** (250 m grid), MODIS NDVI শুরু।
- Main message: "ML + stacking + AutoML + XAI একসাথে ধানে হয়নি, আমরা করছি"; data = BIHS 2015 + NDVI/weather/soil/DEM।
- Research-এর অংশ: Introduction (gap) + Methods (Data)।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ "Agriculture in Bangladesh…" (লাইন ৮০–৯১)
- **কী বলছে:** ধান ~11.4 Mha, 36.6 MT (2019–20); কৃষির GHG 76.79 MT CO₂e (2014–15), crop production 65%; 70–75% technical mitigation nutrient/water management আর short-duration variety দিয়ে সম্ভব (Sapkota 2021)।
- **বোঝাতে চান:** mitigation option আর ধান চাষের link কম বোঝা — তাই গবেষণা দরকার।
- **খেয়াল রাখার মতো:** "11.4 Mha agriculture" বনাম "rice produced 36.6 MT" — বাক্যটা grammar-এ গোলমেলে (agriculture-ই 11.4 Mha নেয়, নাকি ধান?)। সংখ্যা BBS 2020 থেকে; আমরা মূল source দেখিনি → **Unresolved**।

### B2. ¶ "Conventionally, data-driven statistical models…" (লাইন ৯২–১০৫)
- **কী বলছে:** আগে linear regression ইত্যাদি; এগুলো outlier-এ sensitive আর normality/collinearity assumption লাগে; ML এই সীমা কাটায়।
- **খেয়াল রাখার মতো:** (১) Linear regression-এর "normality assumption" শুধু inference-এ দরকার, prediction-এ নয়; (২) "ML সব সময় ভালো" — আসলে Table S6 অনুযায়ী এই paper-এর **GLM baseline-এর training R² = 0.000** (সব season) — অর্থাৎ GLM আসলে intercept-only; কোনো সত্যিকারের linear baseline তুলনায় নেই (**Confirmed issue**, পরে p4/p11-এ বিস্তারিত)। আমাদের নিজস্ব OLS check: [code-audit](../registers/code-audit.md) Check 9।

### B3. ¶ Stacking (লাইন ১০৬–১১৬)
- **কী বলছে:** Stacking দুই stage; heterogeneous base learners + meta-learner; bias ও variance দুটোই কমায় (Ma 2018; Wang 2018c; Zhai & Chen 2018)।
- **খেয়াল রাখার মতো (ref list থেকে title):**
  - **Wang et al., 2018c** = *"A cognitive vision method for insect pest image segmentation"* (IFAC-PapersOnLine 51) — stacking নিয়ে নয়, image segmentation। **Confirmed issue**।
  - Ma 2018 = warfarin dose, Zhai & Chen 2018 = PM2.5 Beijing — stacking-এর উদাহরণ হিসেবে ঠিক আছে, কিন্তু ফসলের নয়।
  - "bias ও variance **দুটোই** কমায়" — theoretical claim; এই paper নিজে সেটা পরীক্ষা করেনি (bias-variance decomposition নেই)।

### B4. ¶ AutoML (লাইন ১১৭–১৩০)
- **কী বলছে:** AutoML model selection ও tuning automate করে (Feurer 2015; Liu 2021; D'Orazio 2019)। Stacking ফসল-yield-এ কম ব্যবহৃত (Shahhosseini 2020)। অনেক application replicable নয়; তাই এই study "comprehensive architectural description" দেয়।
- **খেয়াল রাখার মতো:** (১) D'Orazio 2019 ref list-এ **দুইবার** আছে (p14, একটায় "Prasad", আরেকটায় "Prasady"); (২) "provides a comprehensive architectural description … reproducibility" — কিন্তু repo-তে `train_data.csv`, `test_data.csv`, saved models, split code নেই (p5 §2.3.3 বলে code GitHub-এ); (৩) AutoML settings paper/code/SI-তে ভিন্ন (দেখুন p4)।

### B5. ¶ XAI gap (লাইন ১৩১–১৪২)
- **কী বলছে:** ML দিয়ে ধানের yield factor বের করা হয়েছে (Chen 2016; Delerce 2016); কিন্তু ব্যাখ্যা দরকার; Black-box high-stakes-এ সমস্যা (**Rudin 2019**); XAI স্বাস্থ্য (Lauritsen; **Song 2020**), exposure, cancer mortality (Ahmed 2021a)-এ হয়েছে; ধানের yield-এ "has not yet been applied"।
- **খেয়াল রাখার মতো:**
  1. **Rudin 2019** ref = *"Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead"*। অর্থাৎ Rudin বলছেন black-box + post-hoc explanation **না করে** interpretable model ব্যবহার করুন। এই paper ঠিক উল্টোটা করছে (black-box stack + post-hoc XAI) আর Rudin-কে আলোচনা করে না। **Confirmed issue** (citation সঠিক পড়া হয়নি/সম্পর্ক আলোচিত নয়)। MSc-র জন্য: simple interpretable baseline রাখুন।
  2. **Song 2020** = *"Cross-site transportability of an explainable AI model for acute kidney injury prediction"* — মূল বিষয় **transportability (এক site থেকে অন্য site-এ model যাওয়া)**। এই paper কখনো transferability test করেনি। **Research opportunity** (আপনার MSc-র সরাসরি gap)।
  3. **Ahmed 2021a / 2021b:** text-এ দুটো; ref list-এ ২০২১-এর **একটাই** Ahmed entry (Sci. Rep. 11, 24090, lung cancer)। **Confirmed issue** (p13 refs)।
  4. "XAI has not yet been applied to understand factors influencing rice yield in Bangladesh" — একটা novelty claim; literature search আমরা করিনি → **Unresolved** (claim-টা "Bangladesh-specific" করে সংকীর্ণ; আলাদা yield XAI studies অন্য দেশে আছে, নিজেদের Intro-ই Chen 2016/Delerce 2016 উল্লেখ করে)।

### B6. ¶ Study summary (লাইন ১৪৩–১৫২)
- **কী বলছে:** BIHS (PRSSP + IFPRI) data + remote sensing + climate + soil দিয়ে yield predict, factors identify, GHG-র সাথে spatial সম্পর্ক। "three model-agnostic methods"।
- **খেয়াল রাখার মতো:** (১) **কোনো research question/hypothesis স্পষ্ট নেই**; (২) objective-এ **unseen area-এ prediction** নেই; (৩) GHG আবারো "emissions" বলা হচ্ছে যদিও modeled (পরের লাইনে "modeled GHG emissions" আছে — ভালো)।

### B7. §2.1.1 BIHS (লাইন ১৫৫–১৭০)
- **কী বলছে:** ৭ division, **6500 households, 325 primary sampling units**; plot-এর geolocation "derived from a Union shapefile"; yield, transplanting date, variety, fertilizer, organic matter, tillage, **irrigation practices**, harvest date extract; local unit → metric।
- **খেয়াল রাখার মতো:**
  1. **Row-এর unit অস্পষ্ট:** 6500 households (এখানে) বনাম 13,137 farmers (p5 §3.1)। আমরা data-তে পেয়েছি 13,150 row (677 + 6,664 + 5,809) — Aus 677, Aman 6,664, Boro 5,809। Index দেখলে এটা **household-plot-season record**; household id আলাদা column নেই (Check 1: `work/check01_07.out`)।
  2. **Location = Union centroid:** "geolocation of each plot was derived from a Union shapefile" — অর্থাৎ plot GPS নয়। আমাদের Check 2: প্রতিটা union-এর ভেতরে সব row-এর সব environmental column (NDVI/t2m/tp/soil/DEM, ২৯–৪২টা) **১০০% একই** (unique value = 1)। এটা union-centroid assignment-এর সরাসরি প্রমাণ — **Confirmed**। ফলে 250 m precision অর্থহীন।
  3. **Irrigation:** এখানে "irrigation practices extracted" বলা, কিন্তু p12-এ "water management data… excluded due to inconsistencies"। অথচ code-এ `Water_regime` model predictor (দেখুন নিচে/ p4)। Check 5: `Water_regime` = Aus সবই "Rainfed, wet season" (677/677), Aman "Continuous flooding" 6,614 + "Deepwater" 50, Boro সবই "Continuous flooding" (5,809/5,809)। এটা farmer-reported irrigation নয়, **season-based class** মনে হচ্ছে (**suspected**, কারণ column-এর উৎস documented নয়)। PFI Table S8/S9-এ importance ≈ 0%।
  4. **Field duration** কোথাও সংজ্ঞায়িত নেই (harvest − transplanting?)। Check 6: GD range Aus 91–123, Aman 91–146, Boro 110–157 days। Raw date column data-তে নেই → reproduce করা **যায়নি**: "Not reported in the provided paper, Supporting Information, or available code."
  5. Local unit conversion factor কত? "Not reported…"।
  6. BIHS sampling weight ব্যবহার হয়েছে কিনা — "Not reported…" (p12 শুধু বলে sample country-representative)।

### B8. §2.1.2 Spatial environmental data (লাইন ১৭১–১৮৯)
- **কী বলছে:** সব raster 250 m × 250 m grid-এ আনা হয়েছে, কারণ MODIS NDVI-এর resolution 250 m (সবচেয়ে সূক্ষ্ম)। ERA-Interim (~12 km) আর soil point data 250 m-এ resample।
- **খেয়াল রাখার মতো:**
  1. **Inconsistency:** "NDVI (250 m) is the highest among all layers" কিন্তু Table 1 (p3)-এ DEM = **90 m** (SRTM) — অর্থাৎ DEM আরও সূক্ষ্ম। **Confirmed issue** (সামান্য)।
  2. **False precision:** 12 km weather → 250 m (thin plate spline) মানে নতুন তথ্য আসে না; আর location আবার union centroid। তাই "250 m grid-এ align" একটা প্রযুক্তিগত ধাপ, বৈজ্ঞানিক রেজোলিউশন নয়।
  3. "We did not use a higher resolution due to computational limits and the risk of noise" — যুক্তি গ্রহণযোগ্য, কিন্তু যেহেতু household location centroid, আসল bottleneck এটাই।

## C. নতুন শব্দগুলো

#### Stacking / stacked generalization (গভীর)
- **সহজ মানে:** আলাদা ধরনের model-দের prediction-কে feature বানিয়ে আরেকটা model train করা।
- **ছোট উদাহরণ:** ধরুন ৩ model-এর out-of-fold prediction একটা row-এ 3000, 3600, 3300; meta weights 0.5, 0.2, 0.3 → 0.5×3000+0.2×3600+0.3×3300 = 3210।
- **এই paper-এ:** p4: দুটো stack (All models / Best of family); meta-learner = non-negative GLM।
- **খেয়াল রাখতে হবে:** Base model-গুলো যদি একই leakage-এ ভোগে, stack সেটা কমায় না।

#### Black-box model
- **সহজ মানে:** যে model-এর ভেতরের হিসাব মানুষ সহজে পড়তে পারে না (deep net, ensemble)।
- **উদাহরণ:** ৫০০ গাছের forest — প্রতি গাছের সিদ্ধান্ত পড়া অসম্ভব।
- **এই paper-এ:** stacking-কেই black-box ধরে post-hoc XAI।
- **খেয়াল:** Rudin 2019 বলেন high-stakes-এ interpretable model ভালো।

#### Hyperparameter
- **সহজ মানে:** যে setting আপনি train-এর আগে ঠিক করে দেন (tree-এর depth, learning rate)।
- **উদাহরণ:** max_depth = 5 বনাম 20।
- **এই paper-এ:** SI Table S2/S4।

#### BIHS (Bangladesh Integrated Household Survey)
- **সহজ মানে:** IFPRI-র নেওয়া ৬৫০০ ঘরের জাতীয় household survey (2015)।
- **খেয়াল:** এটা cross-section (এক বছর), তাই "temporal" ভিন্নতা নেই; season ভিন্নতা আছে।

#### PSU (Primary Sampling Unit)
- **সহজ মানে:** survey-র প্রথম ধাপে বাছাই করা ছোট এলাকা (গ্রাম/মহল্লা)। এখানে 325টা।
- **খেয়াল:** একই PSU-র ঘরগুলো একই মাটি/আবহাওয়া/আচরণ share করে → observations independent নয়।

#### Resampling (250 m-এ)
- **সহজ মানে:** একটা raster-এর pixel-এর মাপ বদলে অন্য raster-এর সাথে মেলানো।
- **উদাহরণ:** 12 km pixel = ~(12000/250)² = 2304 টা 250 m pixel-এ ভাগ; সবকটায় প্রায় একই (smoothed) মান।
- **এই paper-এ:** ERA-Interim → 250 m (TPS)। **খেয়াল:** নতুন তথ্য তৈরি হয় না।

## D. Equation / statistics
এই পেজে নেই।

## E. Figures
এই পেজে নেই (Fig. 1 p3-এ)।

## F. Tables
এই পেজে নেই (Table 1 p3-এ)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 2.1 | Wang et al. 2018c = "cognitive vision method for insect pest image segmentation", stacking-এর support নয় | p2 ¶stacking; refs p16 | Confirmed issue |
| 2.2 | "Ahmed et al. 2021a/2021b" text-এ; ref list-এ ২০২১-এর একটাই Ahmed entry | p2 ¶XAI; p9; refs p14 | Confirmed issue |
| 2.3 | D'Orazio et al. 2019 ref list-এ দু'বার (Prasad/Prasady) | refs p14 | Confirmed issue |
| 2.4 | Rudin 2019 interpretable-model argue করে; paper উল্টো পথে, আলোচনা নেই | p2 ¶XAI; refs | Confirmed issue |
| 2.5 | Song 2020 = cross-site transportability; paper কখনো test করেনি | p2; refs; পুরো paper | Research opportunity |
| 2.6 | Row-unit অস্পষ্ট: 6500 households (p2) vs 13,137 farmers (p5) vs data 13,150 rows | p2 §2.1.1; p5 §3.1; `work/check01_07.out` (Check 1,4) | Confirmed issue |
| 2.7 | Union-এর ভেতরে সব environmental value 100% একই → union-centroid assignment | `work/scripts/check01_07_data.py` output (Check 2) | Confirmed issue |
| 2.8 | NDVI "finest (250 m)" বনাম Table 1 DEM 90 m | p2 §2.1.2; p3 Table 1 | Confirmed issue |
| 2.9 | 12 km → 250 m resample = false precision | p2; p3 §2.1.2.2 | Potential concern |
| 2.10 | Irrigation: p2 "extracted", p12 "excluded", code-এ `Water_regime` predictor (Check 5: Aus/Boro-তে প্রায় ধ্রুবক) | p2; p12; `yield_aus_autoML.Rmd:115`; SI S8/S9 | Confirmed issue (inconsistent reporting) |
| 2.11 | Field duration, unit conversion, sampling weights, research question — কোথাও নেই | p2, পুরো paper | Unresolved question |
| 2.12 | No hypotheses / objectives-এ unseen-area prediction নেই | p2 ¶study | Research opportunity |

**লেখকদের পক্ষে:** Stacking কেন, AutoML কেন — যুক্তি পরিষ্কারভাবে দেওয়া। Resolution-এর trade-off নিজেরা উল্লেখ করেছেন (p2) আর union-centroid limitation p12-তে স্বীকার করেছেন।

**Peer-reviewer প্রশ্ন:** Row-এর unit কী? Household ID সহ data share করা যাবে? Linear baseline কোথায়? "XAI not applied" claim-এর systematic search?

## H. সারাংশ
- **Short summary:** Intro-তে ML/stacking/AutoML/XAI-এর পক্ষে যুক্তি; Data = BIHS + ৫ ধরনের spatial layer, সব 250 m-এ resample।
- **৫ key terms:** Stacking, Black-box, PSU, Resampling, BIHS।
- **Takeaways:** (১) ৫টা citation সমস্যা p1–2-এ; (২) union-centroid প্রমাণিত; (৩) row-unit/irrigation/field-duration অস্পষ্ট।
- **Key numbers:** 11.4 Mha; 36.6 MT; 76.79 MT CO₂e (2014–15); 65%; 70–75%; 6500 households; 325 PSUs; 250 m; ~12 km; 31,787 (p3)।
- **পরের পেজ-প্রশ্ন:** NDVI/weather/soil কীভাবে বানানো? GHG কীভাবে হিসাব? CCAFS-MOT-এর input কী?

## Master Notes
- **Paragraph-wise:** ¶BD context; ¶linear বনাম ML; ¶stacking; ¶AutoML; ¶XAI gap; ¶study; §2.1.1; §2.1.2।
- **Exact numbers:** 11.4 Mha, 36.6 MT, 76.79 MT CO₂e, 65%, 70–75%, 6500 HH, 325 PSU, 250 m, 12 km, 90 m (DEM)।
- **Claims & evidence:** stacking bias+variance কমায় → cited paper ভুল (insect image); XAI gap → unsearched; "replicable" → split/ models নেই।
- **Open checks:** BBS 2020 numbers; BIHS Dataverse-এ household ID পাওয়া যায় কি?
- **MSc notes:** (১) Row-unit আগে নির্ধারণ করুন (household/plot/district); (২) district-level aggregation করলে centroid-সমস্যা কমে; (৩) Rudin 2019 পড়ে interpretable baseline রাখুন; (৪) Song 2020-এর transportability সরাসরি আপনার topic।
