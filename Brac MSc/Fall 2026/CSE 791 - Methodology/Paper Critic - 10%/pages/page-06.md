# Page 06 — Hold-out test result (Fig. 5 text), Fig. 3 (boxplots), Fig. 4 (maps)

← [page-05](page-05.md) | [page-07](page-07.md) →

## A. এই পেজে কী আছে
- §3.2-এর বাকি অংশ: test-set R²/RMSE, "regression toward the mean" bias (text, Fig. 5 p7-এ)।
- **Fig. 3** (yield ও GHG-র boxplot, crop type × season) আর **Fig. 4** (union-গড় yield ও GHG-র map)।
- এই পেজ Results-এর ছবি-ভরা পেজ; paragraph মাত্র একটা।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ Test performance + bias (লাইন ১–১৪; p5 শেষ থেকে চলছে)
- **কী বলছে:** hold-out test-এ stack ensemble "only slightly improved" অন্য model-এর চেয়ে (Table S6); R² = 0.451, 0.561, 0.523, RMSE = 835, 949, 1122 kg/ha (Aus, Aman, Boro; Fig. 5)। Model **under-estimate high yields, over-estimate low yields** — regression line 1:1 লাইনের চেয়ে flat। কারণ: MSE-minimizing ensemble গড়ের দিকে টানে।
- **লেখকরা বোঝাতে চান:** performance "moderate", bias সাধারণ ও ব্যাখ্যাযোগ্য।
- **কঠিন শব্দ:** *regression to the mean* = চরম মানের prediction গড়ের কাছে চলে আসা।
- **খেয়াল রাখার মতো:**
  1. **Seed F2 — Fig. 5 বনাম S6 test:** 
     | Season | Fig. 5 (RMSE / R²) | S6 test (RMSE / R²) | HTML test RMSE |
     |---|---|---|---|
     | Aus | 835 / 0.451 | 817.6 / 0.475 | 817.6381 |
     | Aman | 949 / 0.561 | 948.7 / 0.590 | 948.7078 |
     | Boro | 1122 / 0.523 | 1122.0 / 0.514 | 1122.671 |
     Test RMSE-এর HTML (h2o.performance on test) S6-এর সাথে প্রায় হুবহু মেলে (Aus 817.6; Aman 948.7; Boro 1122.7)।
  2. **R² একই test set + একই RMSE-তে আলাদা হতে পারে না।** আমাদের গণনা (`work/scripts/check_arith_F1_F4.py`): S6-এর GLM (≈ intercept-only) test RMSE ও R² থেকে test-set variance V = MSE_GLM/(1 − R²_GLM) বের করে R² = 1 − RMSE²/V:
     - Aus: V-র SD ≈ 1127.9 → S6 RMSE 817.6 ⇒ R² = **0.475** (S6 printed 0.475 ✓); Fig. 5 RMSE 835 ⇒ **0.452** (Fig. 5 printed 0.451 ✓)।
     - Aman: SD ≈ 1433.7 → S6 RMSE 948.7 ⇒ **0.562** (S6 printed **0.590 ✗**; Fig. 5 printed 0.561 ✓)।
     - Boro: SD ≈ 1625.6 → S6 RMSE 1122.0 ⇒ **0.524** (S6 printed **0.514 ✗**; Fig. 5 printed 0.523 ✓)।
     অর্থাৎ **Fig. 5-এর R² ও RMSE নিজেদের মধ্যে সামঞ্জস্যপূর্ণ**, আর S6-এর **R² কলাম (Aman 0.590, Boro 0.514) নিজের RMSE-র সাথে অসঙ্গত**। Seed-এ ধারণা ছিল "Fig. 5 অন্য run"; আমাদের revised সিদ্ধান্ত: **Boro-য় Fig. 5 (0.523) আসলে S6-এর RMSE-র সাথে মেলে, S6 R² 0.514 সম্ভবত typo/অন্য মান**; **Aus-এ Fig. 5 RMSE 835 HTML test (817.6) থেকে আলাদা** — 835 কোনো test output-এ নেই (সবচেয়ে কাছে Aus stack-এর CV RMSE **836.03**, যা ভিন্ন stage)। (Confidence: Aman/Boro-র R² অসঙ্গতি — উচ্চ; Aus 835-এর উৎস — অজানা।)
  3. "stack **only slightly** improved" — লেখকরা নিজেরাই বলছেন (p6)। কিন্তু Abstract/Discussion-এ "outperformed" — tone-এ ফারাক; দেখুন p9 (F3)।
  4. "regression line flatter" — ঠিক; কিন্তু slope, CI কত? Report নেই। EVar ≈ R² (0.453 vs 0.451) ⇒ গড় error ≈ 0, তবে slope < 1 মানে conditional bias (high-y under-predict)।
  5. "Overfit দেখা যায় না?" — S6: stack train RMSE 404.8 বনাম test 817.6 (Aus) — train/test অনুপাত ~2×; "R² train 0.888 বনাম test 0.475"। বড় generalization gap কিন্তু random split-এ gap স্বাভাবিক (ensemble tree overfit)।

## C. নতুন শব্দগুলো

#### Regression to the mean / shrinkage
- **সহজ মানে:** model চরম মানের prediction কম চরম করে দেয় — কম yield-কে একটু বেশি, বেশি yield-কে একটু কম।
- **ছোট উদাহরণ:** observed 6000 → predicted 5200; observed 1500 → predicted 2300। Predicted-vs-observed লাইনের slope < 1।
- **এই paper-এ:** Fig. 5 সব season-এ।
- **খেয়াল:** এটা শুধু "ensemble-এর দোষ" নয়; noisy label (farmer-reported yield) থাকলেও হয়। Bias correction (isotonic/linear recalibration) আলোচনা নেই।

#### Explained variance (EVar)
- **সহজ মানে:** 1 − Var(error)/Var(y); R²-এর মতো, কিন্তু গড় ভুল (bias) বাদ দেয়।
- **উদাহরণ:** `work/worked_examples2.out`: R² 0.820, EVar 0.827 (bias −66.7 থাকায়)।

#### Boxplot
- **সহজ মানে:** বাক্সের ভেতরের দাগ = median; বাক্স = 25%–75%; গোঁফ = সাধারণ range; বিন্দু = outlier।
- **খেয়াল:** boxplot গড় দেখায় না; sample size দেখায় না (hybrid Aus-এ মাত্র 21 row)।

## D. Equation / statistics
এই পেজে নেই। (R² ↔ RMSE সম্পর্ক: R² = 1 − RMSE²/Var(y) — সংখ্যাসহ উপরে B1-এ।)

## E. Figures

**Fig. 3 — Boxplots of (a) yield and (b) total GHG emission of local, HYV, hybrid rice in Aus, Aman, Boro**
- **Axes:** (a) x = Yield (kg ha⁻¹) 0–~9000; (b) x = Total emissions (kg CO₂e ha⁻¹) 0–12,500। y = season (উপর থেকে নিচে Boro, Aus, Aman)। **Legend:** Hybrid = লাল, HYV = সবুজ, Local = নীল।
- **প্যাটার্ন (ছবি থেকে আনুমানিক):** (a) Boro-তে শুধু HYV ও Hybrid (local নেই ✓ text); Boro hybrid-এর median (~6000) HYV (~5600)-এর চেয়ে বেশি; Boro-তে অনেক নিচু outlier (0–2000) — CSV-তে Boro-য় 12 row yield = 0, 195 row < 2000 (আমাদের check)। Aus ও Aman-এ local < HYV < hybrid (median ~2300 < ~3000 < ~3800 Aus; Aman ~2300 < ~3800 < ~4700)। (b) Aus-এ GHG ছোট ও সংকীর্ণ (~800–1100); Aman সবচেয়ে বেশি ও বিস্তৃত (local box চওড়া, উপরে অনেক outlier 8000–12,500); Boro মাঝারি।
- **Interpretation বনাম প্রমাণ:** লেখকরা বলেন hybrid yield বেশি ও local-এর emission কম (কম fertilizer-এর কারণে)। ছবি এটা দেখায় — তবে "কম fertilizer-এর কারণে" একটা অনুমান (Fig. S5 দেখায় rate কম, কিন্তু অন্য কারণ নিয়ন্ত্রিত নয়)। Aman-এ local-এর GHG box বেশ চওড়া — text "local-এর emission significantly lower" Aman-এ আমাদের গড় (local 4040 < HYV 4655 ≈ hybrid 4622; `work/check_anova.out`) মেলে।
- **সমস্যা:** (১) sample size (n) box-এ নেই — Aus hybrid মাত্র 21 row; (২) Boro-তে local নেই বলে Boro-র তুলনা সীমিত; (৩) GHG একটা modeled quantity (পরের কথা p3); (৪) colour legend শুধু ডানে — panel (a)-এও প্রযোজ্য কি না বোঝা কঠিন।

**Fig. 4 — Spatial distribution of average yield (উপরে) ও Total GHG (নিচে): (a) Aus, (b) Aman, (c) Boro**
- **Axes/legend:** প্রতি বিন্দু = union (সম্ভবত union-গড়); বিন্দুর আকার = মান (বড় = বেশি)। 10টা bin। Yield legend (kg ha⁻¹): Aus 576–5213; Aman 200–6584; Boro 1170–8548। GHG legend (kg CO₂ eq ha⁻¹): Aus 578–1374; Aman 2037–9827; Boro 2475–5285। ধূসর background = DEM।
- **Caption সমস্যা:** panel লেবেল (a)–(f) কিন্তু caption "(a) Aus, (b) Aman, (c) Boro (upper row … lower row)" — চেনা যায়, তবে ছোট mismatch। Legend-এ "Aus yield" max 5213 বনাম CSV union-mean? (আমরা union-mean max যাচাই করিনি)।
- **Interpretation:** লেখকরা: "কোনো স্পষ্ট spatial pattern নেই; high/low yield scattered"।
  - **আমাদের check (Moran's I, 8-nearest neighbours, 999 permutation; `work/check_moran.out`):** union-mean yield: Aus I = 0.005 (p = 0.93, কোনো autocorrelation নেই ✓); Aman I = **0.193** (p = 0.001); Boro I = **0.228** (p = 0.001)। GHG: Aus 0.047 (p=0.345); Aman 0.115 (p=0.002); Boro 0.161 (p=0.001)। অর্থাৎ Aman ও Boro-য় **দুর্বল কিন্তু statistically significant positive spatial clustering** আছে; "no distinct spatial pattern" Aus-এর জন্য ঠিক, Aman/Boro-র জন্য আংশিক সঠিক (pattern ছোট, চোখে ধরা কঠিন)। (Confidence: মাঝারি — weights পছন্দ (8-NN) আর union-centroid নির্ভর; "our own check, not a reproduction"।)
  - **Map-এর বিন্দু = union centroid** — plot নয়। সব union একই size-এ দেখানো নয় (আকার = মান)।
- **Methodological সমস্যা:** (১) quantile/natural-break bin-এর পদ্ধতি লেখা নেই; (২) প্রতি union-এ কত row (1–207) — গড় নির্ভরযোগ্যতা ভিন্ন, বিন্দুতে দেখানো নেই; (৩) 78 Aus union-এ gaps বড় — পশ্চিম-দক্ষিণে sample কম।

## F. Tables
এই পেজে নেই।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 6.1 | S6 test RMSE ≈ HTML test RMSE (817.6/948.7/1122.7); কিন্তু S6 R² কলাম (Aman 0.590, Boro 0.514) নিজের RMSE-র সাথে অসঙ্গত (implied 0.562, 0.524) | SI S6; HTML `h2o.performance(test)`; `work/check_arith.out` | Confirmed issue |
| 6.2 | Fig. 5 R² (0.561, 0.523) S6 RMSE-র সাথে সামঞ্জস্যপূর্ণ; Aus-এ Fig. 5 RMSE 835 কোনো test output-এ নেই (HTML test 817.6; কাছাকাছি 836.03 = CV, ভিন্ন stage) | p7 Fig. 5; `work/check_arith.out` | Unresolved question |
| 6.3 | "Stack only slightly improved" (p6) বনাম Abstract "outperformed all" — tone-অমিল | p1; p6 | Potential concern |
| 6.4 | Fig. 5 flat-slope bias স্বীকৃত; slope/CI/recalibration report নেই | p6 §3.2; Fig. 5 | Potential concern |
| 6.5 | Fig. 3: sample size (n) দেখানো নেই; Aus hybrid মাত্র 21 row; Boro-য় 12 শূন্য-yield row | Fig. 3; CSV | Potential concern |
| 6.6 | "No distinct spatial pattern" — Aman/Boro-য় Moran's I 0.19/0.23 (p≈0.001) দুর্বল clustering দেখায় | `work/check_moran.out` (আমাদের own check) | Potential concern |
| 6.7 | Fig. 4: bin-পদ্ধতি/union-প্রতি n অজানা; caption-label সামান্য অমিল | Fig. 4 | Potential concern |
| 6.8 | Fig. 3 hybrid>HYV yield correlation, causation নয় (nutrient/district নিয়ন্ত্রিত নয়) | p5 §3.1; Fig. 3 | Potential concern |

**লেখকদের পক্ষে:** Fig. 5 ও text bias খোলাখুলি স্বীকার করে; R², RMSE, EVar একসাথে দেখায়। Fig. 3 crop-type গ্রুপ ভিত্তিক তুলনা সুন্দরভাবে ব্যবহার করে।

**Reviewer প্রশ্ন:** Fig. 5 কোন run/test-set থেকে? Test-set R² কীভাবে হিসাব (H2O নিজে R² দেয় কি)? Spatial autocorrelation পরিমাপ?

## H. সারাংশ
- **Short summary:** Test RMSE 835/949/1122, R² 0.451/0.561/0.523; model high yield under-predict করে; Fig. 3 crop-type পার্থক্য; Fig. 4 yield/GHG scattered map।
- **৫ key terms:** Regression to the mean, EVar, R², Boxplot, Spatial autocorrelation (Moran's I)।
- **Takeaways:** (১) S6 R² কলাম অসঙ্গত, Fig. 5 R² সামঞ্জস্যপূর্ণ; (২) Aus 835-এর উৎস অজানা; (৩) "no spatial pattern" Aus-এ ঠিক, Aman/Boro-য় দুর্বল pattern আছে।
- **Key numbers:** 0.451/0.561/0.523; 835/949/1122; EVar 0.453/0.562/0.524; Moran's I Aman 0.193, Boro 0.228।
- **পরের পেজ-প্রশ্ন:** PFI order কী? PDP flat কেন?

## Master Notes
- **Paragraph-wise:** test result + bias।
- **Exact numbers:** (H)।
- **Claims & evidence:** "stack only slightly improved" ✔ (S6); "no spatial pattern" → আংশিক।
- **Open checks:** Fig. 5 data source; test n।
- **MSc notes:** R² ও RMSE একই stage থেকে রিপোর্ট; bias/slope report; spatial autocorrelation পরীক্ষা (Moran's I) আপনার district-level target-এ।
