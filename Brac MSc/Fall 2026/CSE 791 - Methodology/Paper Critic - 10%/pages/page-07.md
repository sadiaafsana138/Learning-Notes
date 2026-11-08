# Page 07 — Bias discussion, Table 4, §3.3 PFI, Fig. 5 (obs vs pred), Fig. 6 (PFI)

← [page-06](page-06.md) | [page-08](page-08.md) →

## A. এই পেজে কী আছে
- §3.2-র শেষ অংশ (কেন extreme yield-এ model খারাপ; Boro-র RMSE বেশি কেন), **Table 4**, **§3.3 Permutation feature importance**, **Fig. 5** (1:1 plot, test), **Fig. 6** (PFI bar chart)।
- Main message: ensemble-এর performance আর কোন feature সবচেয়ে গুরুত্বপূর্ণ (N, P, K rate, crop type, field duration)।
- আগের পেজ: test metric ও bias-এর শুরু; পরের পেজ: PDP/ALE, breakdown।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ Extreme yield ও missing features (লাইন ১–১৫)
- **কী বলছে:** model গড়ের দিকে টানে, বিশেষ করে যেসব yield extreme training data-তে কম। Predictors (farmer-reported yield?, management, NDVI, climate) স্থানীয় agronomic/environmental condition (water management, pest, intensive management) ধরতে পারে না। Boro-র RMSE বেশি কারণ range বড় (~2000–9000 kg/ha)। ভবিষ্যতে spatially explicit ও management feature লাগবে।
- **খেয়াল রাখার মতো:**
  1. "**farmers' reported yield** … predictor variables employed" — yield তো **target**; target predictor হতে পারে না। সম্ভবত শব্দগত ভুল (বোঝাতে চেয়েছে "farmer-reported management info")। Code-এ YIELD feature-এ নেই (`FeatureData` শুধু YIELD target হিসেবে শেষ column)। **Confirmed issue** (wording)।
  2. Boro "range ~2000–9000": CSV-তে Boro yield min = **0**, 1st percentile 1,031, 99th 8,889, max 9,259; 195 row < 2000 (12 শূন্য) (আমাদের check)। তাই range ~0–9300। এই low tail-ই (শূন্য-yield outlier) Boro-র RMSE বাড়াতে পারে — নিশ্চিত নয় (**suspected**)।
  3. Boro-র RMSE বেশি হলেও R² সবচেয়ে কম (S6 CV 0.510) — RMSE-এর তুলনা season-জুড়ে অন্যায্য, কারণ yield-এর SD আলাদা (Aus ≈ 1,195, Aman ≈ 1,450, Boro ≈ 1,596 কেজি/হা; CSV)। Relative error (RMSE/mean): Aus ≈ 817.6/3105 = 26%, Aman ≈ 948.7/3557 = 27%, Boro ≈ 1122/5535 = 20%। অর্থাৎ **আপেক্ষিক ভুল Boro-তে কম**। (calculation: নিচে F)।

### B2. §3.3 Permutation-based feature importance (লাইন ১৬–৩৩)
- **কী বলছে:** Tables S7–S9 mean ও SD "RMSE loss (the factor by which RMSE increased)" ও relative importance (%)। Fig. 6-এ top 17/19/18 feature (importance > 10%)। সব season-এ top 5 = crop type, field duration, N, P, K rate; ক্রম: Aus — N > crop > FD > P > K; Aman — crop > N > K > P > FD; Boro — N > K > P > crop > FD। এছাড়া exTZONE সব season-এ, land type Aus-এ, soil type Aman-এ, early-stage NDVI ও rainfall Boro-তে।
- **আমাদের যাচাই (`work/scripts/check_pfi_tables.py`):** S7–S9-এর অর্ডার text-এর সাথে **মেলে**; importance > 10% এর সংখ্যা **17 / 19 / 18 ✓** (Aus/Aman/Boro)। Fig. 6 bar-order Table-এর সাথে মেলে। Aman S8-এর importance% কয়েক জায়গায় সামান্য অমিল (যেমন Soil Types 25.9 বনাম 85.95/328.57 = 26.2) — ছোট (≤ 0.3 percentage point)।
- **খেয়াল:**
  1. **"factor" ভুল** — code `type="difference"` (বিয়োগ, kg/ha)। (p5)।
  2. **Training data-য় PFI** (p5, `explainer_train`)।
  3. **Rank ঠিক কতটা স্পষ্ট?** SD = permutation-জুড়ে SD (data resampling নয়)। সংলগ্ন rank-এর পার্থক্য/pooled SD (`work/check_pfi_rankz.out`): Aman crop vs N: 11.2/25.3 = **0.44**; Aman K vs P: 26.9/26.2 = 1.03; Aus crop vs FD: 14.6/23.2 = 0.63; Boro K vs P: 1.02; Boro crop vs FD: 1.13। শুধু Aus-এ N vs crop (z = 4.43) স্পষ্ট। অর্থাৎ text-এ যে "ক্রম ভিন্ন ভিন্ন season-এ" বলা হয়েছে, তার বড় অংশ noise-এর মধ্যে — **শীর্ষ ৫টা feature-এর সেটই** নির্ভরযোগ্য, ক্রম নয়।
  4. **Correlated predictors:** N, P, K rate (Table S5: Aus yield~N 0.592, P 0.625, K 0.450; ফার্টিলাইজারগুলো নিজেরাও correlated) — একটা shuffle করলে অবাস্তব সংমিশ্রণ; আলাদা importance যোগফল-যোগ্য নয়।
  5. **Field duration** PFI-তে বড় (Aus 221.8 ±14.9; loss/SD ≈ 14.9; importance 61.3%) অথচ Fig. 7-এ PDP/ALE flat (p8) → Seed F9। এখানে শুধু নোট: field duration সম্ভবত crop type/season/variety-র proxy (hybrid/local-এর duration ভিন্ন) বা interaction-এর মাধ্যমে কাজ করছে — **suspected** (interaction/H-statistic ফাইলে আছে কিন্তু report হয়নি)।
  6. **Season window:** Aman PFI-তে `TEMP, DEC-19-2014` **৮ম** (S8: 52.30; 15.6%); অথচ SI S3-এ Aman window শেষ **353 (19 Dec 2014)** আর Boro শুরু **305 (1 Nov 2014)** — দুটো window ওভারল্যাপ (1 Nov–19 Dec)। Boro-র ফিচারে `TEMP DEC-19-2014` (12.8%) ও Nov/Dec NDVI/rain আছে (S9)। Aman-এ ডিসেম্বরের তাপমাত্রা গুরুত্বপূর্ণ হওয়া এই window-র calendar-নির্ভরতার লক্ষণ হতে পারে (Seed F8: **verified (windows overlap)**, ব্যাখ্যা "likely, not proven")।
  7. **Water_regime:** S8: loss 1.26 ± 9.49 (0.0%), S9: 0.00 ± 15.48 (0.0%) — model-এ ছিল, importance শূন্য; ফলে paper-এর "excluded" claim code-এর সাথে মেলে না, কিন্তু ফলাফলে ক্ষতি নেই (ধ্রুবক/কাছাকাছি ধ্রুবক feature)।

## C. নতুন শব্দগুলো

#### Relative importance (%)
- **সহজ মানে:** সবচেয়ে বড় loss-কে 100 ধরে বাকিগুলোর আনুপাতিক মান।
- **ছোট উদাহরণ:** 236.4/361.5 × 100 = **65.4%** (Aus crop type); 176.3/361.5 = **48.8%** (K-rate)।
- **এই paper-এ:** Table S7–S9, "> 10%" cut-off Fig. 6-এ feature বাছাইয়ের জন্য।
- **খেয়াল:** relative হওয়ায় season-জুড়ে তুলনা নেই; 10% cut-off arbitrary।

#### Drop-out loss
- **সহজ মানে:** feature বাদ/shuffle করলে model-এর error যতটা বাড়ে।
- **খেয়াল:** DALEX-এ default type="raw"; এখানে "difference" (loss − baseline loss)।

#### Observed vs predicted (1:1) plot
- **সহজ মানে:** x = আসল মান, y = prediction; আদর্শ হলে সব বিন্দু 45° রেখার উপর।
- **খেয়াল:** slope < 1 মানে shrinkage।

#### exTZONE
- **সহজ মানে:** extreme temperature zone (T1E1…T5E4) — একটা categorical code (SI Fig. S6e)।
- **খেয়াল:** উৎস/সংজ্ঞা paper-এ নেই ("Not reported…")।

## D. Equation / statistics
- **Eq. নেই।** দুই মেট্রিক:
  - **RMSE/mean (আপেক্ষিক):** Aus 817.6/3105 = **26.3%**; Aman 948.7/3557 = **26.7%**; Boro 1122/5535 = **20.3%** (calc: `python`; গড় yield CSV থেকে)।
  - **PFI "importance %"** সূত্র: 100 × loss_j / max_k loss_k (S7: verified)।

## E. Figures

**Table 4** → F।

**Fig. 5 — 1:1 plot, test set: (a) Aus, (b) Aman, (c) Boro**
- **Axes:** x = Observed yield (kg/ha) 0–10,000; y = Predicted 0–10,000; ধূসর বিন্দু = test row; কালো কঠিন লাইন = regression; ডট লাইন = 1:1। প্রতি panel-এ RMSE, R², EVar।
- **প্যাটার্ন:** Aus-এ বিন্দু খুব কম (ছোট test set) ও যথেষ্ট ছড়ানো; Aman ও Boro-য় ঘন মেঘ, কালো লাইন 1:1-এর চেয়ে flat — বেশি yield-এ কম অনুমান, কম yield-এ বেশি (✓ text)। Boro-তে observed ≈ 0–1000 অথচ predicted ≈ 3000–6000-র কিছু বিন্দু (সম্ভবত শূন্য-yield row)।
- **Authors' interpretation:** moderate skill + regression to the mean। **Figure supports:** shrinkage — হ্যাঁ। **R²/RMSE-র উৎস:** Aus 835 HTML test (817.6)-র সাথে মেলে না (p6)।
- **Visual/methodological problem:** (১) Axis 0–10,000 — সব বিন্দু দেখা যায়, কিন্তু আসল density ধূসর overplot-এ ঢাকা (transparency/hexbin নেই); (২) test n panel-এ নেই; (৩) confidence band নেই।

**Fig. 6 — Permutation-based feature importance (a) Aus, (b) Aman, (c) Boro**
- **Axes:** x = "RMSE Loss Per Permutation" 0–500; y = feature নাম (উপরে সবচেয়ে গুরুত্বপূর্ণ); error bar = SD।
- **প্যাটার্ন:** শীর্ষ ৫ (N, P, K, crop type, field duration) বাকিদের থেকে ২–৫ গুণ বড় loss (Aus: 361.5…176.3 বনাম exTZONE 69.9)। বাকি feature (soil, NDVI, rainfall, temp) ছোট ও প্রায় সমান।
- **Authors' interpretation:** এই ৫টা key factor। **Support?** হ্যাঁ — predictive importance হিসেবে; কিন্তু (১) train-data; (২) rank noise-এর মধ্যে (B2.3); (৩) feature-গুলো constant-within-union (union-identity proxy হতে পারে — soil/NDVI/climate-এ)।
- **Problem:** "Mannure application" (typo: Manure) Fig. 6a ও S7; Fig. 6-এ axis পুরো ০–৫০০ ফিক্সড বলে ছোট feature-এর পার্থক্য দেখা যায় না; x-axis-এর নামে "factor" নয়, kg/ha difference লেখা উচিত।

## F. Tables

**Table 4 — number of models and 10-fold CV statistics of best models (stack)**
| Season | No. of models | Best model | RMSE | MAE | RMSLE | R² |
|---|---|---|---|---|---|---|
| Boro | 958 | Stacked (ALL) | 816.01 | 622.31 | 0.35 | 0.55 |
| Aman | 175 | Stacked (ALL) | 926.20 | 647.44 | 0.34 | 0.59 |
| Aus | 198 | Stacked (ALL) | 1109.2 | 773.47 | 0.43 | 0.51 |
- **Max/min:** RMSE max = 1109.2 (labelled Aus), min = 816.01 (labelled Boro); R² max 0.59 (Aman), min 0.51।
- **Odd (Seed F1):** Row order **Boro, Aman, Aus** (উল্টো ক্রম); Boro-র সংখ্যা Aus-এর (S6 CV Aus 816.0/0.543, HTML Aus 958 base models); Aus-এর সংখ্যা Boro-র (S6 Boro CV 1109.2/0.510; HTML Boro 188 base models, paper "198")। **Table 4 swapped** (details: p5, `work/check_arith.out`)। Possible cause (**suspected**): উল্টো-ক্রমে সাজানো সারি-লেবেল।
- **Cross-check HTML:** Aus HTML: 958 base models (deeplearning 18, drf 2, gbm 769, glm 1, xgboost 168 — i.e., GBM-ই ৮০%); Aman 175 (dl 10, drf 2, gbm 130, glm 1, xgb 32); Boro 188। "no. of models" AutoML-এর time-budget-নির্ভর, কর্মক্ষমতার সূচক নয়। (HTML "Number of Base Models"; 'Boro 198' paper vs 188 HTML — সম্ভবত typo।)
- **Metric stage:** মানগুলো meta-learner level-one (HTML), সত্যিকারের stack-CV নয় (p5)।
- **Text vs table:** Text "(MAE) 637–773" বনাম Table 4 min 622.31 ✗।
- **Missing:** test-set metrics Table 4-এ নেই (আছে S6-এ); CV SD (HTML-এ আছে, যেমন Aus R² fold-wise ≈ 0.43–0.65, mean ± SD 0.518 ± 0.065) paper-এ নেই।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 7.1 | Table 4 Aus/Boro swapped (models count সহ); row order Boro/Aman/Aus | p7 Table 4; SI S6; HTML; `work/check_arith.out` | Confirmed issue |
| 7.2 | "farmers' reported yield" predictor বলা (yield = target; code-এ নেই) | p7 §3.2 শেষ; `FeatureData` | Confirmed issue (wording) |
| 7.3 | Boro yield "~2000–9000" বনাম CSV min 0, 195 row < 2000, 12 শূন্য | p7; `boro_data_all.csv` | Potential concern |
| 7.4 | RMSE season-জুড়ে তুলনা অন্যায্য; relative error Aus 26.3%, Aman 26.7%, Boro 20.3% | CSV means; S6 test RMSE | Potential concern |
| 7.5 | PFI ক্রম text ↔ S7–S9 ↔ Fig. 6 সামঞ্জস্যপূর্ণ; importance>10 সংখ্যা 17/19/18 ✓ | `work/check_pfi.out` | (লেখকদের পক্ষে — verified) |
| 7.6 | শীর্ষ-৫ feature-এর ভেতরে ক্রম noise-এর মধ্যে (Aman crop vs N z=0.44; Boro K vs P 1.02) | `work/check_pfi_rankz.out` | Potential concern |
| 7.7 | Aman PFI-তে `TEMP DEC-19-2014` ৮ম (15.6%) অথচ Aman window ওভারল্যাপ Boro-র সাথে (1 Nov–19 Dec) | SI S3; S8 | Confirmed issue (overlap); ব্যাখ্যা: Potential concern |
| 7.8 | Field duration PFI-তে বড় (61–70%) কিন্তু PDP/ALE flat (p8) | S7–S9; Fig. 7 | Unresolved question |
| 7.9 | "factor" বনাম code "difference"; PFI train data-য় | p7 §3.3; `Rmd:862` | Confirmed issue |
| 7.10 | `Water_regime` model-এ ছিল, importance 0 (S8: 1.26±9.49; S9: 0.00±15.48) | SI S8, S9 | Confirmed issue (inconsistent reporting) |
| 7.11 | "Mannure application" typo; Aman S8 importance% সামান্য অমিল | Fig. 6a; S7; S8 | Confirmed issue (minor) |
| 7.12 | Fig. 5 Aus RMSE 835 ≠ HTML test 817.6; test n/CI নেই | Fig. 5; HTML | Unresolved question |
| 7.13 | কোনো PFI-র সাথে repeated model run/seed variability নেই (AutoML-এর randomness) | p7 | Research opportunity |

**লেখকদের পক্ষে:** PFI SD দেখানো; Tables S7–S9-এ সব feature-এর পূর্ণ তালিকা; Fig. 6-এ সত্যিই শীর্ষ ৫টা আলাদাভাবে দেখা যায় — সংখ্যা text-এর সাথে মেলে।

**Reviewer-এর প্রশ্ন:** PFI test data-য় করলে শীর্ষ ৫ একই থাকবে? Correlated N-P-K-কে group করে permute (grouped PFI) করলে? Field duration-কে crop type/season-এর সাথে ভাঙলে?

## H. সারাংশ
- **Short summary:** Table 4 (Aus/Boro swapped), PFI শীর্ষ ৫ (N, P, K, crop type, field duration), Fig. 5–6।
- **৫ key terms:** Relative importance, Drop-out loss, 1:1 plot, exTZONE, Relative RMSE।
- **Takeaways:** (১) Table 4 সংশোধন দরকার; (২) PFI শীর্ষ ৫ সেট নির্ভরযোগ্য, ক্রম নয়; (৩) PFI train-data-র; (৪) Aman-এ ডিসেম্বর-তাপমাত্রা window-overlap-এর ইঙ্গিত।
- **Key numbers:** 816.01/622.31/0.35/0.55; 926.20/647.44/0.34/0.59; 1109.2/773.47/0.43/0.51; PFI Aus 361.5/236.4/221.8/201.8/176.3; Aman 328.57/317.36/299.44/272.58/230.46; Boro 440.62/370.32/340.16/237.78/210.03।
- **পরের পেজ-প্রশ্ন:** PDP/ALE কীভাবে field duration-কে flat দেখাল? AL ও PD কি সত্যিই parallel?

## Master Notes
- **Paragraph-wise:** extreme-yield bias; PFI (order, top 17/19/18)।
- **Exact numbers:** (H)।
- **Claims & evidence:** "top-5 all seasons" ✔; "factor" ✗ (difference); "Table 4 ten-fold CV" ✗ (level-one)।
- **Open checks:** PFI on test; grouped PFI; seed repeat।
- **MSc notes:** PFI-র বদলে/সাথে grouped/conditional PFI, held-out district-এ; relative error (MAPE/RMSE÷mean) report; table-label double-check।
