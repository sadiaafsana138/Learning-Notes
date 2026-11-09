# Observation register (সব page-এর section G একসাথে; `work/scripts/build_registers.py` দিয়ে auto-generated)

মোট observation: 164 | Potential concern: 55, Confirmed issue: 78, Unresolved question: 23, Research opportunity: 6

| # (page.n) | কী পেলাম | প্রমাণ | ধরন | page |
|---|---|---|---|---|
| 1.1 | Abstract-এ GHG যে **modeled (CCAFS-MOT)**, measured নয় — তা বলা নেই | p1 abstract; p3 §2.2 ("estimated emissions are based solely on modeled outputs") | Potential concern  | [p01](../pages/page-01.md) |
| 1.2 | Abstract-এর causal ভাষা ("influencing", "impact") vs p12 Limitation ("do not explain why things happen") | p1 abstract vs p12 | Potential concern  | [p01](../pages/page-01.md) |
| 1.3 | "IPCC, 2019" reference-এর title = "Annex IV: reviewers of the IPCC special report…" (reviewer list) — "one-third" claim-এর সূত্র হিসেবে অপ্রাসঙ্গিক (claim নিজে Crippa 2021 দ্বারা সমর্থিত) | p1 ¶1; ref list p14 | Confirmed issue  | [p01](../pages/page-01.md) |
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
| 4.13 | GLM baseline কার্যত intercept-only: HTML-এ "Ridge (lambda = 14082.0)", nlambda = 30, λ.max = λ.1se = 50164, λ.min = 14082 (= λ-path-এর শেষ মান), training R² = 0.0001 (Aus), Aman 0.0001, Boro ≈ 0 — λ-path কখনো ছোট λ-তে পৌঁছায়নি; (S4-এর "Ridge λ = λ.min" ও "λ.1se = λ.max" দুটোই সত্য, বিরোধ নেই) | `work/html_aus.txt:770-772,809`; SI S4; SI S6 | Confirmed issue  | [p04](../pages/page-04.md) |
| 4.14 | Stack-এর CV RMSE (HTML Aus 836.03) বনাম meta-learner level-one metric (816.68) আলাদা stage | HTML `yield_aus_autoML.html` (stacked ensemble CV vs glm training) | Potential concern  | [p04](../pages/page-04.md) |
| 5.1 | **Table 4-এ Aus ও Boro অদলবদল** (958 models = Aus HTML; 198 বনাম Boro HTML 188) — Aus "transition period" ব্যাখ্যা অসমর্থিত | p5 §3.2; p7 Table 4; SI S6; HTML (aus: 958 base models, level-one RMSE 816.68; boro: 188 base models, CV RMSE 1112.41) | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.2 | Table 4 "CV" মান আসলে meta-learner level-one metrics; stack-এর নিজস্ব CV RMSE (Aus 836.03, Aman 928.20, Boro 1112.41) আলাদা stage | `work/html_{aus,aman,boro}.txt` (extract of the HTMLs): stack CV block vs `glm` level-one block (Aus lines 426 vs 512; Aman 443 vs 529; Boro 447 vs 533) | Potential concern  | [p05](../pages/page-05.md) |
| 5.3 | PFI/PDP/ALE **training data-য়** (`explainer_train`), test-এ নয় | `yield_aus_autoML.Rmd:849-862,1016-1054`; Aman:862,875; Boro:865,878 | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.4 | Paper "RMSE-এর factor" বলে, code `type="difference"` (kg/ha বিয়োগ) | p7 §3.3; Rmd:862 | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.5 | Local XAI-এর saved model ≠ AutoML-HTML-এর model (Aus: 20211104_201857 vs 20211128_82339; Aman: …162457 vs …174647; Boro: …201704 vs …123317) | `local_XAI_uniion_*.Rmd:159/170/171` vs HTML model IDs | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.6 | Local XAI চলেছে `*_union_data_all.csv`-এ (repo-তে নেই), train ফাইলে নয়; scaling mismatch | `local_XAI_uniion_aus.Rmd:47,108,115-117,152` | Confirmed issue (scaling-প্রভাব: execution লাগবে)  | [p05](../pages/page-05.md) |
| 5.7 | GW code শুধু Aman; `_01`-এ nominal `Crop_Types` numeric Pearson-এ | `gw_correlation_aman_01.Rmd:77`; `_02` তা বাদ দেয় | Confirmed issue (code-level)  | [p05](../pages/page-05.md) |
| 5.8 | "All relevant R code available" — CCAFS-MOT, split, kriging, GHG-PFI, Aus/Boro GW নেই | file inventory | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.9 | S5 correlations = union-mean (ecological); row-level কম | `work/check07b.out` | Confirmed issue (reporting) / Potential concern (interpretation)  | [p05](../pages/page-05.md) |
| 5.10 | "Boro F-value" দু'বার; 27.6 আসলে Aus (আমাদের ANOVA); Boro F আমাদের 116.6 vs paper 123 | p5 §3.1; `work/check_anova.out` | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.11 | MAE range "637–773" বনাম Table 4 min 622.31; "MAE < minimum observed yield" ভুল (min yield: 247/112/0) | p5 §3.2; Table 4; CSV | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.12 | Row 13,150 বনাম 13,137; Aman unions 246 বনাম 247 | CSV (Check 4) | Unresolved question  | [p05](../pages/page-05.md) |
| 5.13 | Fig. S6 panel/label মিল নেই (text S6b→(d), S6d→(e)) | p5 §3.1; SI p23 | Confirmed issue  | [p05](../pages/page-05.md) |
| 5.14 | Train rows 80% নয় (77.7–79.6%) | HTML Null D.o.F. | Unresolved question  | [p05](../pages/page-05.md) |
| 5.15 | ANOVA-তে clustering/confounding উপেক্ষিত; hybrid-এ "significantly higher yield" মানে causal নয় | p5 §3.1 | Potential concern  | [p05](../pages/page-05.md) |
| 6.1 | S6 test RMSE ≈ HTML test RMSE (817.6/948.7/1122.7); কিন্তু S6 R² কলাম (Aman 0.590, Boro 0.514) নিজের RMSE-র সাথে অসঙ্গত (implied 0.562, 0.524) | SI S6; HTML `h2o.performance(test)`; `work/check_arith.out` | Confirmed issue  | [p06](../pages/page-06.md) |
| 6.2 | Fig. 5 R² (0.561, 0.523) S6 RMSE-র সাথে সামঞ্জস্যপূর্ণ; Aus-এ Fig. 5 RMSE 835 কোনো test output-এ নেই (HTML test 817.6; কাছাকাছি 836.03 = CV, ভিন্ন stage) | p7 Fig. 5; `work/check_arith.out` | Unresolved question  | [p06](../pages/page-06.md) |
| 6.3 | "Stack only slightly improved" (p6) বনাম Abstract "outperformed all" — tone-অমিল | p1; p6 | Potential concern  | [p06](../pages/page-06.md) |
| 6.4 | Fig. 5 flat-slope bias স্বীকৃত; slope/CI/recalibration report নেই | p6 §3.2; Fig. 5 | Potential concern  | [p06](../pages/page-06.md) |
| 6.5 | Fig. 3: sample size (n) দেখানো নেই; Aus hybrid মাত্র 21 row; Boro-য় 12 শূন্য-yield row | Fig. 3; CSV | Potential concern  | [p06](../pages/page-06.md) |
| 6.6 | "No distinct spatial pattern" — Aman/Boro-য় Moran's I 0.19/0.23 (p≈0.001) দুর্বল clustering দেখায় | `work/check_moran.out` (আমাদের own check) | Potential concern  | [p06](../pages/page-06.md) |
| 6.7 | Fig. 4: bin-পদ্ধতি/union-প্রতি n অজানা; caption-label সামান্য অমিল | Fig. 4 | Potential concern  | [p06](../pages/page-06.md) |
| 6.8 | Fig. 3 hybrid>HYV yield correlation, causation নয় (nutrient/district নিয়ন্ত্রিত নয়) | p5 §3.1; Fig. 3 | Potential concern  | [p06](../pages/page-06.md) |
| 7.1 | Table 4 Aus/Boro swapped (models count সহ); row order Boro/Aman/Aus | p7 Table 4; SI S6; HTML; `work/check_arith.out` | Confirmed issue  | [p07](../pages/page-07.md) |
| 7.2 | "farmers' reported yield" predictor বলা (yield = target; code-এ নেই) | p7 §3.2 শেষ; `FeatureData` | Confirmed issue (wording)  | [p07](../pages/page-07.md) |
| 7.3 | Boro yield "~2000–9000" বনাম CSV min 0, 195 row < 2000, 12 শূন্য | p7; `boro_data_all.csv` | Potential concern  | [p07](../pages/page-07.md) |
| 7.4 | RMSE season-জুড়ে তুলনা অন্যায্য; relative error Aus 26.3%, Aman 26.7%, Boro 20.3% | CSV means; S6 test RMSE | Potential concern  | [p07](../pages/page-07.md) |
| 7.5 | PFI ক্রম text ↔ S7–S9 ↔ Fig. 6 সামঞ্জস্যপূর্ণ; importance>10 সংখ্যা 17/19/18 ✓ | `work/check_pfi.out` | (লেখকদের পক্ষে — verified)  | [p07](../pages/page-07.md) |
| 7.6 | শীর্ষ-৫ feature-এর ভেতরে ক্রম noise-এর মধ্যে (Aman crop vs N z=0.44; Boro K vs P 1.02) | `work/check_pfi_rankz.out` | Potential concern  | [p07](../pages/page-07.md) |
| 7.7 | Aman PFI-তে `TEMP DEC-19-2014` ৮ম (15.6%) অথচ Aman window ওভারল্যাপ Boro-র সাথে (1 Nov–19 Dec) | SI S3; S8 | Confirmed issue (overlap); ব্যাখ্যা: Potential concern  | [p07](../pages/page-07.md) |
| 7.8 | Field duration PFI-তে বড় (61–70%) কিন্তু PDP/ALE flat (p8) | S7–S9; Fig. 7 | Unresolved question  | [p07](../pages/page-07.md) |
| 7.9 | "factor" বনাম code "difference"; PFI train data-য় | p7 §3.3; `Rmd:862` | Confirmed issue  | [p07](../pages/page-07.md) |
| 7.10 | `Water_regime` model-এ ছিল, importance 0 (S8: 1.26±9.49; S9: 0.00±15.48) | SI S8, S9 | Confirmed issue (inconsistent reporting)  | [p07](../pages/page-07.md) |
| 7.11 | "Mannure application" typo; Aman S8 importance% সামান্য অমিল | Fig. 6a; S7; S8 | Confirmed issue (minor)  | [p07](../pages/page-07.md) |
| 7.12 | Fig. 5 Aus RMSE 835 ≠ HTML test 817.6; test n/CI নেই | Fig. 5; HTML | Unresolved question  | [p07](../pages/page-07.md) |
| 7.13 | কোনো PFI-র সাথে repeated model run/seed variability নেই (AutoML-এর randomness) | p7 | Research opportunity  | [p07](../pages/page-07.md) |
| 8.1 | Fig. reference ভুল: "Fig. 6 shows PDP/AL"(→Fig. 7), "Figs. 6b, 6h"(→7b, 7h), "leftmost panel"(→rightmost), "P-rate (Fig. 7g)"(→Fig. 8g) | p8 §3.4–3.5; Fig. 6/7/8 | Confirmed issue  | [p08](../pages/page-08.md) |
| 8.2 | "AL = blue lines" ভুল; legend: PD নীল, AL কমলা | p8 §3.4 ¶২; Fig. 7a legend | Confirmed issue  | [p08](../pages/page-08.md) |
| 8.3 | "Additive" claim শুধু PD≈AL-এর ভিত্তিতে; `iml::Interaction` চালিয়ে `Feature_Interaction.csv` লিখলেও কোথাও report নেই | p8 §3.4; `yield_aus_autoML.Rmd:1066-1076`; Aman:1089; Boro:1093 | Confirmed issue  | [p08](../pages/page-08.md) |
| 8.4 | "All five features parallel" — Fig. 7(o) Boro crop type-এ PD vs AL ৩৫০–৫০০ kg/ha ফারাক (আনুমানিক) | Fig. 7(o) | Confirmed issue  | [p08](../pages/page-08.md) |
| 8.5 | Field duration: PFI 61–70% বনাম PDP/ALE flat — লেখকরা উল্লেখ করেন, ব্যাখ্যা করেন না | p7; p8; Fig. 7d,i,n | Unresolved question  | [p08](../pages/page-08.md) |
| 8.6 | PDP/ALE train data-য়; sparse high-N অংশ অনির্ভরযোগ্য; uncertainty/rug নেই | `Rmd:1016-1054`; Fig. 7 | Potential concern  | [p08](../pages/page-08.md) |
| 8.7 | §3.5: Aus/Aman % বনাম Boro count (167/125/124) — শৈলী মেলে না (167/224 = 74.6%) | p8 §3.5 | Confirmed issue (reporting)  | [p08](../pages/page-08.md) |
| 8.8 | "Positive contribution in X% of unions" ≈ feature-মান গড়ের উপরে কি না; effect heterogeneity নয় — আমাদের proxy: Aman crop type 73.6% ≈ ">70%" | `work/check_breakdown_proxy.out` | Potential concern  | [p08](../pages/page-08.md) |
| 8.9 | Union-average-এ union-প্রতি n/uncertainty নেই (n = 1–207) | Fig. 8; CSV | Potential concern  | [p08](../pages/page-08.md) |
| 8.10 | **F5:** S5 Aman GWP~N/P/K/FD = 0.201/0.108/0.223/0.277 (weak) বনাম "moderate to strongly positive across three seasons" | p8 §3.6; SI S5; আমাদের recompute `work/check07b.out` | Confirmed issue  | [p08](../pages/page-08.md) |
| 8.11 | Fig. 7 y-label "Respone" typo; Fig. 7 e/j/o legend নেই | Fig. 7 | Confirmed issue (minor)  | [p08](../pages/page-08.md) |
| 8.12 | Abstract "spatial variations in average effects" বনাম আসলে union-average local attribution | p1; p8 | Potential concern  | [p08](../pages/page-08.md) |
| 9.1 | §3.6: "Aus weak FD" ভুল; S5 Aus 0.309, Aman 0.277, Boro 0.058; Fig. 9(l) Boro দুর্বল; Discussion p11 সঠিক | p9 §3.6; SI S5; `work/check07b.out`; Fig. 9 | Confirmed issue  | [p09](../pages/page-09.md) |
| 9.2 | "Stacking ensemble effectively captured these relationships" — GW correlation-এ stack ব্যবহৃত হয়নি | p9 §3.6; `gw_correlation_aman_01.Rmd:76-80` | Confirmed issue  | [p09](../pages/page-09.md) |
| 9.3 | "water-saving practices" ও "maintaining productivity" — water/yield-scaled emission বিশ্লেষণে নেই | p9 §3.6; p12 | Confirmed issue (claim ← evidence)  | [p09](../pages/page-09.md) |
| 9.4 | "1–4% vs DRF": test 0.91–1.47%, CV 1.07–6.23% (stage ভিন্ন), Aus test best single XRT 820.8 থেকে মাত্র 0.39% | SI S6; `work/check_arith.out` | Confirmed issue  | [p09](../pages/page-09.md) |
| 9.5 | Stack-এর "bias+variance কমায়" — এই data-য় পরীক্ষা নেই; 958-এর 769 GBM; অধিকাংশ coefficient 0 | p9 §4; HTML metalearner | Potential concern  | [p09](../pages/page-09.md) |
| 9.6 | "Local XAI overcomes GW regression constraints" — তুলনা নেই; ভিন্ন জিনিস মাপে | p9 §4 ¶১ | Potential concern  | [p09](../pages/page-09.md) |
| 9.7 | Fig. 8: legend-এ unit নেই, break-পদ্ধতি অজানা, প্রতি panel আলাদা scale; "%-positive" ও legend-এর মিল অনিশ্চিত | Fig. 8 | Unresolved question  | [p09](../pages/page-09.md) |
| 9.8 | "Fertilizer effects on GHG" causal ভাষা + CCAFS-MOT circularity | p9 §3.6; p3 §2.2 | Potential concern  | [p09](../pages/page-09.md) |
| 9.9 | Local correlation-এ union-গড় (ecological), row-level কম | `work/check07b.out` | Potential concern  | [p09](../pages/page-09.md) |
| 9.10 | Novelty claim (p2) বনাম Discussion-এ Ahmed 2024 (maize AutoML+XAI Bangladesh) | p2; p9 | Potential concern  | [p09](../pages/page-09.md) |
| 9.11 | "crop duration" ও "field duration" — একই কি না অস্পষ্ট; কোথাও সংজ্ঞা নেই | p9; p2 | Unresolved question  | [p09](../pages/page-09.md) |
| 9.12 | Stack vs single model-এর gap-এর জন্য repeated split/CI নেই | S6 | Research opportunity  | [p09](../pages/page-09.md) |
| 10.1 | "N most important in all seasons" — Aman-এ PFI শীর্ষ crop type (S8) ও p8 নিজেই "crop type most critical in Aman" | p10 §4; p8 §3.5; SI S8 | Confirmed issue  | [p10](../pages/page-10.md) |
| 10.2 | "critical role in increasing rice yield" — causal ভাষা; PFI/attribution predictive | p10; p12 limitations | Potential concern  | [p10](../pages/page-10.md) |
| 10.3 | Fig. 9 FD legend "> 0.035" → হবে "< 0.035" | p10 Fig. 9(j–l) legend | Confirmed issue  | [p10](../pages/page-10.md) |
| 10.4 | Placement/deep-placement/NUE সুপারিশ data দিয়ে সমর্থিত নয় (data-তে শুধু rate) | p10–p11; CSV columns | Confirmed issue (claim ← evidence)  | [p10](../pages/page-10.md) |
| 10.5 | Fig. 9: significance/CI নেই; local sample ছোট; bandwidth: Aman `_01` = 144, `_02` = 69 neighbours — কোনটা Fig. 9-এ? | `gw_correlation_aman_01.html`, `_02.html` | Unresolved question  | [p10](../pages/page-10.md) |
| 10.6 | N/P/K–GHG correlation আংশিক circular (CCAFS-MOT input) | p3 §2.2; Fig. 9 | Confirmed issue (conceptual) / পরিমাণ: Unresolved  | [p10](../pages/page-10.md) |
| 10.7 | "Particularly Boro" (N) বনাম S5 global Aus 0.816 > Boro 0.593 — ব্যাখ্যা নেই | Fig. 9; SI S5 | Unresolved question  | [p10](../pages/page-10.md) |
| 10.8 | NUE/yield-scaled emission বিশ্লেষণে নেই | p10 Discussion | Potential concern  | [p10](../pages/page-10.md) |
| 10.9 | Gaihre 2015 এখানে সঠিক প্রসঙ্গে (N₂O, deep placement); p1-এ ভুল ছিল | p10; p1 | (লেখকদের পক্ষে)  | [p10](../pages/page-10.md) |
| 10.10 | Aman GW code দুই version (`_01`, `_02`) ও ভিন্ন bandwidth; কোনটা প্রকাশিত অজানা | `gw_correlation_aman_01/02.Rmd` | Unresolved question  | [p10](../pages/page-10.md) |
| 11.1 | "P ও K moderate-strong association all seasons" ভুল — S5 Aman P 0.108, K 0.223 (weak) | p11; SI S5; `work/check07b.out` | Confirmed issue  | [p11](../pages/page-11.md) |
| 11.2 | N-কে নিয়ন্ত্রণে P-GHG partial r ≈ 0 (Aus 0.116; Aman −0.070; Boro −0.016) ⇒ লেখকদের "N-এর সাথে একত্রে ব্যবহার" ব্যাখ্যা সমর্থিত | `work/check_ghg_partial.out` (আমাদের own check) | (লেখকদের পক্ষে — verified)  | [p11](../pages/page-11.md) |
| 11.3 | "HYV vs hybrid emission-এ significant পার্থক্য নেই" — শুধু Aman-এ; Aus +151 (p=0.0003), Boro +127 (p<0.0001), row-level Welch | `work/check_ghg_partial.out` | Potential concern  | [p11](../pages/page-11.md) |
| 11.4 | "Hybrid area বাড়ালে GHG কমবে" — নিজের ফল উল্টো/নিরপেক্ষ; সাহিত্য (Islam 2025) নির্ভর; yield-scaled emission অগণিত | p11; CSV; calc | Confirmed issue (claim ← evidence)  | [p11](../pages/page-11.md) |
| 11.5 | Boro-তে hybrid-এর N/P/K কম কিন্তু GWP বেশি ⇒ GWP-র নির্ধারক অন্যত্র (CCAFS-MOT input অজানা) | `work/check_ghg_partial.out` | Unresolved question  | [p11](../pages/page-11.md) |
| 11.6 | "Our study captured these complex interactions" — কোনো interaction/GHG-model/H-statistic report নেই; Fig. S7 text-এ উল্লিখিত নয় | p11; (grep "S7"/"interaction") | Confirmed issue  | [p11](../pages/page-11.md) |
| 11.7 | "marginal PDP … Indeed positive in many unions" — যুক্তি-সংযোগ ভুল (feature-value vs effect) | p11 §4 | Potential concern  | [p11](../pages/page-11.md) |
| 11.8 | Boro AWD ব্যাখ্যা বনাম data (`Water_regime` Boro = সবাই "Continuous flooding"); GD range সংকীর্ণ (SD 7.5 দিন) | `boro_data_all.csv`; p11 | Potential concern  | [p11](../pages/page-11.md) |
| 11.9 | Citation mismatch: Chen 2011 (steppe CH₄ uptake), Luo 2013 (3 ecosystems), Sutton-Grier 2011 (wetland CH₄), Craufurd & Wheeler 2009 (flowering time), Sapkota 2014 (wheat NW India) | refs p14, p15, p13 | Confirmed issue  | [p11](../pages/page-11.md) |
| 11.10 | "Balanced NPK + water management" সুপারিশ — balanced fertilization/water ফলে নেই | p11; p12; p4 | Confirmed issue (claim ← evidence)  | [p11](../pages/page-11.md) |
| 11.11 | §3.6 (p9) বনাম p11 FD-কথা পরস্পরবিরোধী (Aus বনাম Boro weak) | p9; p11; S5 | Confirmed issue  | [p11](../pages/page-11.md) |
| 11.12 | Self-reported fertilizer data-র error প্রভাব মাপা নেই (স্বীকৃত) | p11 | Potential concern (acknowledged)  | [p11](../pages/page-11.md) |
| 12.1 | **F7:** Conclusion "better nutrient management → higher yield AND lower GHG" — ফল: fertilizer ↔ yield ও GHG দুটোই ধনাত্মক; NUE/yield-scaled analysis নেই | p12 §5; SI S5 | Confirmed issue  | [p12](../pages/page-12.md) |
| 12.2 | আমাদের extra evidence: total GWP N-এর সাথে বাড়ে; intensity Aus 0.39→0.35, Aman 1.82→1.31 (কমে), Boro 0.72→0.83 (বাড়ে) | `work/check_intensity.out` (own check) | Potential concern  | [p12](../pages/page-12.md) |
| 12.3 | "Water data excluded" বনাম `Water_regime` predictor (importance 0%) | p12; `Rmd:115/128/131`; S8–S9 | Confirmed issue  | [p12](../pages/page-12.md) |
| 12.4 | "CCAFS-MOT widely recognized for accuracy" — এই paper-এ validation নেই; একই ¶-এ অনিশ্চয়তা স্বীকার | p12 | Potential concern  | [p12](../pages/page-12.md) |
| 12.5 | Limitations (post-hoc ≠ causal) বনাম Abstract (influencing/impact) | p1; p12 | Potential concern  | [p12](../pages/page-12.md) |
| 12.6 | Limitations ("controlled trials ছাড়া decision-এ নয়") বনাম Policy (subsidy, extension decision-support) | p12 | Confirmed issue (internal inconsistency)  | [p12](../pages/page-12.md) |
| 12.7 | স্বীকৃত নয়: random-split/leakage সম্ভাবনা, linear baseline অভাব, ভিন্ন-run XAI, transferability অপরীক্ষিত | p12 বনাম 4.1–4.13, 5.5 | Potential concern  | [p12](../pages/page-12.md) |
| 12.8 | "Balanced fertilizer use" অসংজ্ঞায়িত; balanced-fertilization feature code-এ নেই | p12; p4; `FeatureData` | Confirmed issue  | [p12](../pages/page-12.md) |
| 12.9 | `Emission_Intensity` column আছে (≈ GWP/YIELD) অথচ ব্যবহৃত নয়; Krupnik 2022 yield-scaled উল্লেখ | CSV; p12 | Research opportunity  | [p12](../pages/page-12.md) |
| 12.10 | Soil data সময়-অমিল (SRDI 1996–2014 বনাম BIHS 2015) | p3; p12 | Potential concern  | [p12](../pages/page-12.md) |
| 13.1 | Ethical statement: "predicting **wheat** yield in Bangladesh" — paper ধান নিয়ে | p13 Ethical statement | Confirmed issue  | [p13](../pages/page-13.md) |
| 13.2 | Data availability: "code of all workflows and data" — train/test CSV, split code, union CSV, shapefile, models, CCAFS-MOT, processing code, Aus/Boro GW, Fig. S7 code নেই | p13; `work/code-inventory.md` | Confirmed issue  | [p13](../pages/page-13.md) |
| 13.3 | লেখকের নামে typo: "Spkota", "Hosssin" | p13 Declaration | Confirmed issue (minor)  | [p13](../pages/page-13.md) |
| 13.4 | তহবিল-বিবরণ ভিন্ন (Ethics: CIMMYT/CGIAR; Ack: + USAID, BMGF, CSISA) | p13 | Potential concern (minor)  | [p13](../pages/page-13.md) |
| 13.5 | "No human subjects" — household-survey data; BIHS-এর ethics clearance উল্লেখ নেই | p13 | Potential concern  | [p13](../pages/page-13.md) |
| 13.6 | "provided by CIMMYT and partners with permission" — কোন data non-public তা বলা নেই | p13 | Unresolved question  | [p13](../pages/page-13.md) |
| 13.7 | R Core Team 2020/2021a/2021b/Team 2021 in-text, list-এ একটি | p13–p16 refs; p3–p5 | Confirmed issue (minor)  | [p13](../pages/page-13.md) |
| 13.8 | Reference-name formatting অসামঞ্জস্য (Fisher, Gollini) | refs p15 | Confirmed issue (minor)  | [p13](../pages/page-13.md) |
| 14.1 | IPCC 2019 entry = reviewer তালিকা (দাবি Crippa 2021 দ্বারা সমর্থিত) | refs p14 (IPCC 2019; Crippa 2021) | Confirmed issue  | [p14](../pages/page-14.md) |
| 14.2 | Gaihre 2015 = N₂O/NO (p1-এ CH₄ দাবিতে ভুল; p10-এ ঠিক) | refs p14; p1; p10 | Confirmed issue  | [p14](../pages/page-14.md) |
| 14.3 | Chen 2011 = steppe CH₄ uptake; p11-এ "rice yield" প্রসঙ্গে | refs p14; p11 | Confirmed issue  | [p14](../pages/page-14.md) |
| 14.4 | D'Orazio 2019 duplicate (Prasad/Prasady) | refs p14 | Confirmed issue  | [p14](../pages/page-14.md) |
| 14.5 | কিছু entry-র traceability দুর্বল (SRDI Bengali report, UNEP শুধু URL, কয়েকটায় DOI নেই) | refs p14–p16 | Potential concern  | [p14](../pages/page-14.md) |
| 14.6 | Crippa 2021, Datta 2013, Emran 2019, Coggins 2025 title দাবির সাথে মেলে | refs p14 | (লেখকদের পক্ষে — verified)  | [p14](../pages/page-14.md) |
| 15.1 | Rudin 2019 = interpretable-model advocacy; paper আলোচনা করেনি | refs p15; p2 | Confirmed issue  | [p15](../pages/page-15.md) |
| 15.2 | Song 2020 = cross-site transportability; paper-এ অপরীক্ষিত | refs p15; p2 | Research opportunity  | [p15](../pages/page-15.md) |
| 15.3 | Quiñones 2021 ও Hipp & Chalise 2015 (diabetes) — linear-assumption/GW-limitation দাবির সরাসরি সূত্র নয় | refs p15; p2, p9 | Potential concern  | [p15](../pages/page-15.md) |
| 15.4 | Sapkota 2014 = গম (NW India), ধান-দাবির জন্য | refs p15; p10 | Potential concern  | [p15](../pages/page-15.md) |
| 15.5 | Shiragi 2017 "Pedotransfer Function of Bangladesh Soils" — SRDI 50,000-point dataset-এর সূত্র হিসেবে পরোক্ষ; SRDI report বাংলা/DOI-হীন | refs p15; p3 | Potential concern  | [p15](../pages/page-15.md) |
| 15.6 | Ribeiro 2016 breakdown-এর জন্য; সঠিক Staniak & Biecek 2018 (একই পেজে) | refs p15; p5 | Confirmed issue (minor)  | [p15](../pages/page-15.md) |
| 15.7 | OLS বনাম RF (নিজস্ব check): R² Aus 0.284/0.503, Aman 0.378/0.575, Boro 0.197/0.515 | `work/check03_09_10.out` | (আমাদের own check) Potential concern: "ML beats linear" টিকে যায়, কিন্তু gap paper-এর intercept-only তুলনার চেয়ে ছোট  | [p15](../pages/page-15.md) |
| 16.1 | Suarez-Gutierrez 2018 = ইউরোপের গ্রীষ্মকালীন তাপমাত্রা (p1 ¶২ দাবির সাথে অমিল) | refs p16; p1 | Confirmed issue  | [p16](../pages/page-16.md) |
| 16.2 | Wang et al. 2018c = insect pest image segmentation (p2 stacking দাবির সাথে অমিল) | refs p16; p2 | Confirmed issue  | [p16](../pages/page-16.md) |
| 16.3 | Sutton-Grier 2011 (wetland CH₄) — p11-এ rice yield প্রসঙ্গে | refs p16; p11 | Potential concern  | [p16](../pages/page-16.md) |
| 16.4 | La Puma 2007 (CO₂, Alaska), Guo 2013 (GHG concentration) — p12-এ "regional methane" দাবির জন্য | refs p15–16; p12 | Potential concern  | [p16](../pages/page-16.md) |
| 16.5 | UNEP 2020 শুধু URL; 59.1 GtCO₂e/15% সংখ্যা অযাচাইকৃত | refs p16; p1 | Unresolved question  | [p16](../pages/page-16.md) |
| 16.6 | Reference list: D'Orazio duplicate; Ahmed 2021a/b ও R Core Team a/b-এর জন্য একটি entry | refs p13–p14; p2–p5 | Confirmed issue  | [p16](../pages/page-16.md) |
