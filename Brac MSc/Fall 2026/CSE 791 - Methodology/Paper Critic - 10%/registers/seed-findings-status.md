# Seed findings status (verified / revised / rejected)

নিয়ম: প্রতিটি seed আমরা paper, SI, CSV ও HTML/Rmd-এর বিপরীতে যাচাই করেছি। "Verified" = সাক্ষ্য মেলে; "Revised" = মূল ধারণা আংশিক ঠিক, বিবরণ বদলেছে; "Rejected" = সাক্ষ্য মেলেনি। (R চালানো হয়নি — Rule 8; যেখানে execution লাগে তা লেখা আছে।)

## সারাংশ
- **Verified:** F1, F3, F5, F6, F7, F8 (overlap-অংশ), F9 (পর্যবেক্ষণ), F10 (সব কোড-পর্যায়ের উপ-দফা), সব editorial/citation (নিচে কয়েকটির nuance সহ), Page 1–2-এর অধিকাংশ।
- **Revised:** F2, F4, IPCC-2019 (one-third দাবি Crippa দ্বারা সমর্থিত), Gaihre-2015 (p1-এ ভুল, p10-এ ঠিক), F8 (Boro-র "before typical transplanting" অংশ), "Ridge λ = λ.min contradicts" অংশ।
- **Rejected:** কোনো seed সম্পূর্ণ rejected হয়নি (দুটি উপ-দাবি আংশিক ভুল পাঠ — F2-এর "Boro একই RMSE কিন্তু ভিন্ন R² ⇒ অন্য run"; F4-এর "S4 বিরোধ")।

## Results and models

| Seed | Status | সাক্ষ্য | Confidence | পেজ |
|---|---|---|---|---|
| **F1** Table 4 Aus/Boro swapped | **Verified** | Table 4 "Boro" 816.01/622.31/0.35/0.55 = S6 Aus CV (816.0/0.543) ≈ Aus HTML meta-learner (816.68/622.46/0.345/0.5448; 958 base models)। Table 4 "Aus" 1109.2/773.47/0.43/0.51 = S6 Boro CV (1109.2/0.510) ≈ Boro HTML (CV 1112.41/772.56/0.4316; 188 base models — paper 198)। Aman মেলে। S6-এ Boro-র CV R² সবচেয়ে কম (0.510) ⇒ "Aus lower due to transition" ব্যাখ্যা অসমর্থিত। **অতিরিক্ত:** Table 4-এর "CV" = meta-learner level-one metric; stack-এর true CV RMSE Aus 836.03 | উচ্চ | p5, p7 |
| **F2** Fig. 5 test ≠ S6 test | **Revised** | S6 test RMSE = HTML test (817.6/948.7/1122.7) ✔। **S6 R² কলাম অসঙ্গত** (Aman 0.590 ⇒ implied 0.562; Boro 0.514 ⇒ 0.524); Fig. 5 R² (0.561/0.523) নিজের RMSE-র সাথে সামঞ্জস্যপূর্ণ। শুধু Aus-এ Fig. 5 RMSE 835 ≠ HTML test 817.6 (উৎস অজানা; কাছাকাছি stack CV 836.03)। Seed-এর "Boro একই RMSE কিন্তু ভিন্ন R² ⇒ ভিন্ন run/test" — ধরনটা ঠিক (অসঙ্গতি আছে) কিন্তু outlier হলো S6-এর R², Fig. 5-এর নয় | উচ্চ (R² অসঙ্গতি); নিম্ন (Aus 835-এর উৎস) | p6 |
| **F3** "1–4% vs DRF" | **Verified** | (DRF−Stack)/DRF: test Aus 1.47%, Aman 1.08%, Boro 0.91%; CV 6.23%, 1.81%, 1.07% (CV stage-মিশ্রণ); Aus test: best single XRT 820.8 ⇒ stack মাত্র 0.39% ভালো | উচ্চ | p9 |
| **F4** GLM baseline R² 0.000 / λ.1se = λ.max / "Ridge λ = λ.min" বিরোধ | **Revised** | train R² 0.000 ✔ (HTML 0.0001); λ.1se = λ.max ✔ (Aus 50,164; Aman 52,782; Boro 21,265)। কিন্তু "S4 'Ridge λ = λ.min' এর সাথে বিরোধ" **ঠিক নয়**: HTML-এ Ridge λ = 14,082 = λ.min = λ-path-এর শেষ মান (nλ = 30, 50,164 → 14,082)। সমস্যা = λ-search ছোট λ-তে যায়নি ⇒ কার্যত intercept-only। **Our own check:** ঠিকমতো OLS test R² 0.284/0.378/0.197 (RF 0.503/0.575/0.515) | উচ্চ | p4, registers/code-audit §9 |

## GHG

| Seed | Status | সাক্ষ্য | Confidence | পেজ |
|---|---|---|---|---|
| **F5** S5 Aman দুর্বল বনাম "moderate to strongly positive"; FD claim | **Verified** | S5 Aman N 0.201, P 0.108, K 0.223, FD 0.277; yield~GWP 0.061 ✔। FD: Aus 0.309 > Aman 0.277 > Boro 0.058 ⇒ §3.6 "Aus weak" ভুল, Discussion (Boro weak) ঠিক। **অতিরিক্ত:** S5 = union-mean (ecological) correlation (আমাদের recompute); row-level কম | উচ্চ | p8, p9, p11 |
| **F6** fertiliser–GHG আংশিক circular | **Verified** (ধারণাগত); মাত্রা **Unresolved** | CCAFS-MOT-এর input-এ fertilizer rate (p3 §2.2); Aus GWP~N r = 0.816 (union-mean), R² (row) 0.69; CCAFS-MOT code/equation অনুপলব্ধ ⇒ circularity-র পরিমাণ জানা যায় না। P/K: N-কে নিয়ন্ত্রণে partial r ≈ 0 (Aus 0.116; Aman −0.070; Boro −0.016) | উচ্চ (ধারণা); নিম্ন (পরিমাণ) | p3, p10, p11 |
| **F7** Conclusion বেশি দাবি করে | **Verified** | fertilizer ↔ yield ও GWP দুটোই ধনাত্মক (S5); NUE/yield-scaled analysis নেই। **Extra (own check):** N-quartile Q1→Q4: intensity Aus 0.39→0.35, Aman 1.82→1.31 (কমে), Boro 0.72→0.83 (বাড়ে); total GWP সব season-এ বাড়ে | উচ্চ (দাবি-বনাম-সাক্ষ্য); মাঝারি (extra check; intensity সংজ্ঞা অজানা) | p12 |

## Features and XAI

| Seed | Status | সাক্ষ্য | Confidence | পেজ |
|---|---|---|---|---|
| **F8** season window overlap | **Verified** (overlap, calendar-fixed, Aman TEMP DEC-19 ৮ম 15.6%); "Boro Nov–Dec mostly before typical transplanting" **Revised (unverified)** | S3: Aman 193–353 (12 Jul–19 Dec), Boro 305 (1 Nov) শুরু ⇒ 1 Nov–19 Dec ওভারল্যাপ ✔; S8: `TEMP, DEC-19-2014` ৮ম (52.30; 15.6%) ✔; সব window ফিক্সড column (planting-date-aligned feature নেই) ✔। "Typical Boro transplanting" paper/CSV-তে নেই (transplanting-তারিখ column নেই) ⇒ domain-জ্ঞান, প্রমাণিত নয় | মাঝারি-উচ্চ | p7 |
| **F9** field duration: PFI বনাম flat PDP/ALE | **Verified** (পর্যবেক্ষণ); কারণ **Unresolved** | PFI importance 61.3% / 70.0% / 47.7% (Aus/Aman/Boro = "48–70%") ✔; Fig. 7 d, i, n flat ✔; ব্যাখ্যা paper-এ নেই। H-statistic (Interaction) কোডে আছে, ফল প্রকাশিত নয় ⇒ interaction/proxy-ব্যাখ্যা যাচাই-অযোগ্য | উচ্চ (পর্যবেক্ষণ) | p7, p8 |
| **F10a** split/CV row-level random; no `fold_column`/group; split code absent | **Verified** | `yield_*_autoML.Rmd:56-57/58-59/59-60` (CSV পড়া), `:200/213/216` (`nfolds=10`); repo-তে `train_data.csv`/`test_data.csv`/split code নেই। Simulation: test-row-এর union train-এ 97.0/99.8/99.7%; **Own check:** row-random→leave-union-out R² (RF) 0.461→0.129; 0.574→0.276; 0.513→0.010 | উচ্চ (design); মাঝারি (পরিমাণ) | p4 |
| **F10b** PFI/PDP/ALE on `explainer_train` | **Verified** | Aus:849-862,1016-1054; Aman:862,875; Boro:865,878; `explainer_test` নেই | উচ্চ | p5 |
| **F10c** scaling আলাদা all/train/test | **Verified** | Aus:120,127-129; Aman:133,140-142; Boro:136,143-145; local XAI aus:108,115-117 | উচ্চ (code); প্রভাব → execution | p4 |
| **F10d** AutoML settings অমিল | **Verified**; H2O default time-limit **Unresolved** | paper 0.0001/2 বনাম code 0.001/3 (Aus:203-204; Aman:216-217; Boro:219-220); `#max_models=20` commented; `max_runtime_secs_per_model=0`; SI S2 footnote MAE/5 rounds। H2O docs-এ time-limit default (যতদূর মনে — 3600 s) offline যাচাই করা যায়নি | উচ্চ (অমিল); নিম্ন (default) | p4 |
| **F10e** H-statistic computed, never reported | **Verified** (code); ফল অনুপলব্ধ | Aus:1066-1076; Aman:1089; Boro:1093; main text/SI-তে "interaction"/"H-statistic" নেই; HTML-এ সংখ্যা নেই (tiff), CSV repo-তে নেই | উচ্চ | p8 |
| **F10f** `Water_regime` predictor | **Verified** | Aus:115, Aman:128, Boro:131; S8/S9 importance 0.0%; CSV values: Aus সব Rainfed; Boro সব Continuous flooding | উচ্চ | p4, p12 |
| **F10g** GW `Crop_Types` numeric; শুধু Aman GW code; CCAFS-MOT ও GHG-PFI code নেই | **Verified** | `gw_correlation_aman_01.Rmd:77` (Crop_Types সহ), `_02` বাদ; file inventory | উচ্চ | p5 |
| **F10h** bugs/typos | **Verified** (সবকটি) | hard-coded paths (`*.Rmd:26-28`); Aus `t.xy` (`yield_aus_autoML.Rmd:810`) বনাম `test.xy` (`:800`); `local_XAI_uniion_aman.Rmd:2` title "Boro"; `local_XAI_uniion_aus.Rmd:231` `Local_contribution_aman_union.csv`; `NDVI_001_2105` (Boro Rmd:91); Aman `NDVI_205` (Rmd:87) বনাম `t2m_209` (:99)/S3 209 | উচ্চ | p3, code-audit |
| **F10i** একাধিক AutoML run; কোনটা paper-এ অজানা | **Verified** | Local XAI model IDs (Aus …AutoML_4_20211104_201857; Aman …AutoML_5_20211104_162457; Boro …AutoML_2_20211102_201704) ≠ AutoML HTML IDs (Aus …AutoML_5_20211128_82339; Aman …AutoML_3_20211127_174647; Boro …AutoML_1_20211104_123317) | উচ্চ | p5 |
| **F10j** local XAI on `*_union_data_all.csv` | **Verified** | `local_XAI_uniion_*.Rmd:47(46),152`; ফাইল repo-তে নেই | উচ্চ | p5 |

## Editorial and citations

| Seed | Status | সাক্ষ্য | পেজ |
|---|---|---|---|
| §3.4 "Fig. 6" (Figs. 6b, 6h) → Fig. 7 | **Verified** (+ নতুন: "P-rate (Fig. 7g)" in §3.5 → Fig. 8g; "leftmost panel" → rightmost) | p8 | p8 |
| "AL = blue lines" বনাম legend (blue = PD) | **Verified** | Fig. 7a legend | p8 |
| Tables 2, 3 নেই | **Verified** | grep: Table 1 → Table 4 | p7 |
| "Tables S2 and S3" hyperparameters (S3 = MOD13Q1; আসলে S4) | **Verified**; Table S4 text-এ অনুল্লিখিত | p4; SI | p4 |
| Fig. S6 panel letters ("S6d" আসলে (e); S6b আসলে (d)) | **Verified** | SI p23 | p5 |
| Fig. S7 caption truncated | **Verified** ("igure S7", "(a) aus, (b), and (c) boro"); Fig. S7 মূল text-এ cited নয় | SI p24 | SI log |
| "Boro F-value" দু'বার | **Verified** (27.6 = Aus; আমাদের ANOVA: Aus 27.6, Aman 733.7, Boro 116.6 (paper 123)) | p5 |
| MAE range "637–773" বনাম Table 4 min 622.31 | **Verified** | p5, p7 |
| Table 1 "Boro/Aman/Boro" | **Verified** | p3 |
| Ethics "predicting wheat yield" | **Verified** | p13 |
| Fig. 9 FD legend "> 0.035" | **Verified** (Fig. 9 j–l legend) | p10 |

## Page 1–2 issues

| Seed | Status | সাক্ষ্য |
|---|---|---|
| "IPCC 2019" = reviewer list | **Verified / Revised** | ref title "Annex IV: reviewers of the IPCC special report…" ✔; কিন্তু "one-third" দাবির আসল সূত্র Crippa 2021 ("Food systems are responsible for a third of global anthropogenic GHG emissions") একই বন্ধনীতে আছে ⇒ দাবি সমর্থিত, IPCC 2019 entry অপ্রাসঙ্গিক |
| Suarez-Gutierrez 2018 = European summer temperatures | **Verified** | "Internal variability in European summer temperatures at 1.5 °C and 2 °C of global warming" |
| Gaihre 2015 = N₂O/NO, not CH₄ | **Verified** (p1-এ CH₄ দাবিতে ভুল); p10-এ N₂O/deep placement প্রসঙ্গে ঠিক | |
| Wang 2018c = insect image segmentation | **Verified** | "A cognitive vision method for insect pest image segmentation" |
| Ahmed 2021a/b বনাম একটি entry | **Verified** | refs p13 (একটাই 2021 Ahmed: Sci. Rep. 11, 24090) |
| D'Orazio 2019 দু'বার | **Verified** | refs p14 (Prasad / Prasady) |
| Rudin 2019 — interpretable models; paper আলোচনা করে না | **Verified** | refs p15; p2 |
| Song 2020 — cross-site transportability; অপরীক্ষিত | **Verified** (Research opportunity) | refs p15; p2 |
| NDVI "finest 250 m" বনাম DEM 90 m | **Verified** | p2 §2.1.2; p3 Table 1 |
| Union-centroid ⇒ 250 m অর্থহীন | **Verified** | Check 2 (union-এ env value 100% অভিন্ন) |
| 12 km → 250 m false precision | **Verified** (ধারণাগত) | (12000/250)² = 2304 |
| "one-third" বনাম "15%" scope-ব্যাখ্যা নেই | **Verified** | p1 |
| Abstract-এ GHG modeled বলা নেই; causal ভাষা | **Verified** | p1 বনাম p3, p12 |
| Row unit 6,500 HH বনাম 13,137 farmers | **Verified** (+ data 13,150 row; Aman 246 বনাম 247 union) | Check 1, 4 |
| Irrigation extracted / excluded / `Water_regime` in code | **Verified** | p2, p12, Rmd |
| Field duration কখনো সংজ্ঞায়িত নয় | **Verified** | পুরো paper; raw date column নেই |
| Unit conversion factor, sampling weights অনুল্লিখিত | **Verified** — "Not reported in the provided paper, Supporting Information, or available code." | — |
| কোনো research question/hypothesis নেই; objectives-এ unseen-area prediction নেই | **Verified** | p2 |
