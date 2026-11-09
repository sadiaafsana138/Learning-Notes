# Page 09 — Fig. 8 (breakdown maps), §3.6 শেষ অংশ, §4 Discussion (শুরু)

← [page-08](page-08.md) | [page-10](page-10.md) →

## A. এই পেজে কী আছে
- **Fig. 8** (Aus, Aman, Boro-র union-wise local contribution map)।
- **§3.6**-এর বাকি অংশ (P, K, field duration ও GHG-র GW correlation-এর বর্ণনা, সমাপনী মন্তব্য)।
- **§4 Discussion**-এর শুরু: অন্য কাজের সাথে সম্পর্ক, local XAI বনাম GW regression, AutoML ও stacking-এর "১–৪% improvement", stacking কেন ভালো, PFI vs breakdown শুরু।
- Research-এর অংশ: Results-এর শেষ + Discussion-এর প্রথম অংশ।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. §3.6 শেষ অংশ (লাইন ১–১৪)
- **কী বলছে:** P (panels d–f) ও K (g–i)-এর সাথে GHG-র correlation "generally weaker ও more variable"; **field duration (panels j–l)** "several regions-এ notable positive correlations (especially darker areas in panel k)", মনে করায় দীর্ঘ জলমগ্নতা/বৃদ্ধিকাল ⇒ বেশি মিথেন; "**however, the Aus season shows only a weak connection between field duration and emissions compared to Boro and Aman**"; map "substantial spatial heterogeneity"; "**The stacking ensemble model effectively captured these relationships**"; "site-specific nutrient management and water-saving practices … mitigating GHG while maintaining productivity"।
- **লেখকরা বোঝাতে চান:** local correlation দেখায় কোথায় কোন factor GHG-র সাথে জড়িত, তাই site-specific management দরকার।
- **খেয়াল রাখার মতো:**
  1. **Seed F5 (FD) — verified:** S5: field duration~GWP: **Aus 0.309**, Aman 0.277, **Boro 0.058**। তাই Aus **দুর্বল নয়**; **Boro-ই দুর্বল**। Fig. 9-এর (l) panel (Boro) ছোট/ফ্যাকাশে বিন্দু (দুর্বল), (j) Aus মাঝারি, (k) Aman গাঢ়। অর্থাৎ **figure ও SI Table S5 একমত, §3.6-এর text ভুল**; Discussion (p11) সঠিক ("only a weak correlation in the Boro season")। **Confirmed issue** (text-বনাম-text)।
  2. **"The stacking ensemble model effectively captured these relationships" — ভুল প্রসঙ্গ:** GW correlation GHG ও input-এর সরাসরি Pearson (union-গড়ে); কোথাও stack model/XAI ব্যবহৃত হয়নি (Aman GW code: `gw_correlation_aman_01.Rmd:76-80` — `gwss(vars=…)` শুধু shapefile column)। Yield-model GHG ব্যাখ্যা করে না। **Confirmed issue** (logical)।
  3. **"effects of fertilizer … on GHG"** — causal ভাষা; আসলে modeled GHG-র সাথে input-এর correlation, আর input-ই CCAFS-MOT-এ ঢোকে (p3) ⇒ আংশিক circular (F6, 3.1)। কত % circular — জানতে CCAFS-MOT সূত্র লাগে (অনুপলব্ধ)।
  4. **"water-saving practices"** — paper-এ water management/AWD বিশ্লেষণে নেই (data excluded, p12)। এটা সুপারিশ-ভিত্তিক নয়, কল্পনা/সাহিত্য-ভিত্তিক।
  5. **"while maintaining productivity"** — yield vs GHG trade-off (yield-scaled emission) বিশ্লেষণ নেই (আমাদের S5: Aman yield~GWP r = 0.061; Aus 0.559; Boro 0.226 — union-গড়)। Seed F7।
  6. **Spatial effect heterogeneity:** আমাদের recompute — S5-এর মতো union-গড় correlation (ecological), row-level দুর্বলতর (Aus P: 0.545 → 0.385; Aman K 0.223 → 0.085)।

### B2. §4 ¶১ Discussion — অন্য studies ও local XAI (লাইন ১৫–৩৯)
- **কী বলছে:** study ML/AutoML চালিয়ে best model বের করে, model-agnostic XAI-তে "how soil, climate, management **appear to influence** yields"। সম্পর্কিত কাজ: Krupnik 2015 (wheat, non-parametric), Ahmed 2024 (maize, AutoML + XAI, nutrient-limited), Ahmed 2025 (wheat ensemble)। Local interpretation cancer mortality (Ahmed 2021b) ও digital soil mapping (Padarian 2020)-এ; "alternative approach to GW regression (Ahmed 2021b)"। GW regression-এর সীমা: local coefficient ঘনিষ্ঠ এলাকার উপর নির্ভর, "distance of influence" তাত্ত্বিকভাবে অজানা (Hipp & Chalise 2015; Quiñones 2021)। "local model-agnostic interpretability **helps to overcome these constraints**"।
- **খেয়াল:**
  1. **"appear to influence"** — এখানে modest ভাষা (ভালো), Abstract-এর "influencing/impact"-এর চেয়ে সতর্ক।
  2. **Novelty vs p2:** p2 বলে "XAI not yet applied to understand factors influencing rice yield … in Bangladesh"; Discussion-এ Ahmed 2024 (maize, Bangladesh, AutoML + XAI) উল্লেখ — একই লেখকের সম্পর্কিত কাজ; novelty শুধু ধান-নির্দিষ্ট। নিজেই স্বীকৃত; তবে claim-এর scope সংকীর্ণ করা উচিত।
  3. **"Local XAI overcomes GW regression limitations" — অসমর্থিত:** (ক) কোনো তুলনা/experiment নেই; (খ) breakdown/SHAP-ধরনের local attribution model-নির্ভর (এই model random split-এ train, union-leakage-সম্ভাব্য) আর spatial weighting/bandwidth-এর মতো "spatial unknown" না থাকলেও spatial smoothness-এর কোনো assumption নেই — অর্থাৎ spatial pattern map করা হয় union-গড় করার পরে; (গ) এই paper নিজেই GW correlation (bandwidth-নির্ভর) ব্যবহার করে। **Potential concern** (Rule 10: কেন গুরুত্বপূর্ণ — GW regression coefficients ও XAI attributions ভিন্ন জিনিস মাপে: প্রথমটি data-র local সম্পর্ক; দ্বিতীয়টি model-এর local আচরণ। একটাকে অপরটির বিকল্প বলা পদ্ধতিগত ঝুঁকি)।
  4. Ahmed 2021b — ref list-এ সেই entry নেই (p2 আলোচনা, 2.2)।

### B3. §4 ¶২ AutoML ও "১–৪% improvement" (লাইন ৪০–৫১)
- **কী বলছে:** "Without prior knowledge of which model would perform best, AutoML proved an excellent choice … stacking ensemble optimal … The stacking ensemble achieved a **1–4% improvement in RMSE compared to the best-performing DRF**।"
- **আমাদের গণনা (S6, `work/scripts/check_arith_F1_F4.py`; সূত্র (DRF−Stack)/DRF):**
  | Season | Train | CV | Test | Test: best single | Stack vs best single (test) |
  |---|---|---|---|---|---|
  | Aus | (396.1−404.8)/396.1 = −2.20% | (870.2−816.0)/870.2 = **6.23%** | (829.8−817.6)/829.8 = **1.47%** | XRT 820.8 | (820.8−817.6)/820.8 = **0.39%** |
  | Aman | (469.3−442.5)/469.3 = 5.71% | (943.3−926.2)/943.3 = **1.81%** | (959.1−948.7)/959.1 = **1.08%** | DRF 959.1 | 1.08% |
  | Boro | (575.6−499.1)/575.6 = 13.29% | (1121.2−1109.2)/1121.2 = **1.07%** | (1132.3−1122.0)/1132.3 = **0.91%** | DRF 1132.3 | 0.91% |
  - **Verdict (Seed F3):** "1–4%" test-এ **0.9–1.5%**; CV-তে **1.1–6.2%** (Aus-এর 6.2% সম্ভবত meta-learner-এর level-one metric বনাম DRF-এর true CV — ভিন্ন stage; পরের টীকা দেখুন)। কোনো একক stage-এ "1–4%" মেলে না; stage উল্লেখ নেই। Aus test-এ best single (XRT) থেকে stack মাত্র **0.39%** ভালো। ফলে "outperformed all individual models" সত্য, কিন্তু gap নগণ্য — repeated split/CI ছাড়া noise-এর সীমায়। (Rule 3: এখানে CV মান S6 CV = meta-learner level-one-এর কাছাকাছি, তাই DRF-এর সাথে like-for-like নয়; দেখুন p5।)
  - "Without prior knowledge… AutoML excellent choice" — AutoML বনাম "ভালোভাবে tune করা একক RF/GBM" তুলনা নেই; এখানে DRF (default params) প্রায় সমান।
  - **Fair point:** S6-তে সব model-এর train/CV/test একসাথে দেওয়া — স্বচ্ছ।

### B4. §4 ¶৩ Stacking কেন ভালো (লাইন ৫২–৬১)
- **কী বলছে:** দুই-ধাপ stacking, বিভিন্ন ধরনের base model ভিন্ন ভুল করে, meta-learner জুড়ে bias+variance কমায়; ensemble-এর সঙ্গতি (Ahmed 2021a, 2025; Liu 2021; Ma 2018; Zhai & Chen 2018)।
- **খেয়াল:** (১) Mechanism ব্যাখ্যা ঠিক, কিন্তু এই data-য় প্রমাণ নেই — bias-variance decomposition, base-model residual correlation, meta-weights বিশ্লেষণ নেই। HTML meta-learner summary (`number_of_active_predictors`): Aus — 958 base model-এর মধ্যে মাত্র **13** active (≈1.4%); Aman — 175-এর মধ্যে **9** active; Boro — নিচে দেখুন। অর্থাৎ stack কার্যত অল্প কয়েকটা model-এর ওজনযুক্ত গড়। (২) 958 base model GBM-ই 769 — "heterogeneous" কম, বেশিরভাগ GBM। (৩) Citation (Ma 2018 warfarin, Zhai & Chen PM2.5) অন্য domain — ঠিক আছে "সঙ্গতি" হিসেবে, কিন্তু Wang 2018c ভুল (p2)।

### B5. §4 ¶৪ শুরু (লাইন ৬২–৬৮; p10 শেষে চলে)
- **কী বলছে:** PFI-তে crop type, duration, N, P, K ৫টা শীর্ষ; "However, breakdown plots … showed spatial variation in feature contributions"।
- **খেয়াল:** "crop duration" এখানে, "field duration" অন্যত্র — একই variable? সংজ্ঞা paper-এ নেই (p2)।

## C. নতুন শব্দগুলো

#### Geographically Weighted Regression (GWR) / GW correlation
- **সহজ মানে:** একটা বিশ্বব্যাপী formula-র বদলে প্রতি জায়গার জন্য কাছের পয়েন্টগুলোকে বেশি ওজন দিয়ে আলাদা regression/correlation।
- **ছোট উদাহরণ:** ঢাকার union-এর জন্য ঢাকার কাছাকাছি ৪০টা union-কে ওজন (bi-square: 0.92, 0.56, 0), দূরেরগুলো 0।
- **এই paper-এ:** Total GWP ~ N/P/K/GD, adaptive bandwidth (AICc)।
- **খেয়াল:** bandwidth-সংবেদী; পুনঃপুনঃ test; কম local sample।

#### Local XAI বনাম GW regression
- **সহজ মানে:** GW regression = data-র local সম্পর্ক; Local XAI = model-এর local আচরণ। একটা model-কে ব্যাখ্যা করে, আরেকটা data-কে।
- **এই paper-এ:** Discussion বলছে XAI সীমা কাটায়; প্রমাণ নেই।

#### Yield-scaled emission (GHG intensity)
- **সহজ মানে:** প্রতি টন ফলনে কত CO₂e: Emission/Yield।
- **ছোট উদাহরণ:** 4000 kg CO₂e/ha ÷ 4000 kg yield = 1.00; 4400 ÷ 5000 = **0.88** — বেশি emission হলেও বেশি yield-এ intensity কম হতে পারে।
- **এই paper-এ:** CSV-তে `Emission_Intensity` column আছে (analysis-এ ব্যবহৃত নয়); text-এ নেই।
- **খেয়াল:** "ভালো nutrient management = বেশি yield + কম GHG" দাবির জন্য এটাই প্রয়োজনীয় মেট্রিক।

#### Base learner vs meta-learner coefficient
- **সহজ মানে:** meta-learner প্রতিটি base model-এর prediction-কে ওজন দেয়; ওজন 0 মানে model-টি stack-এ অংশ নেয় না।
- **এই paper-এ:** HTML metalearner table (Aus: 958 model-এর মধ্যে বেশিরভাগ 0.0000)।

## D. Equation / statistics
- কোনো equation নেই। **Improvement %** সূত্র: (RMSE_DRF − RMSE_Stack)/RMSE_DRF × 100 — সংখ্যাসহ B3 table-এ (Python)।
- **ব্যাখ্যা:** 0.9–1.5% test improvement = ~৮–১২ kg/ha, test RMSE ৮০০–১১০০-র তুলনায় ক্ষুদ্র; test n ছোট (Aus ≈ 136–151) ⇒ standard error-ও বড়।
- **সীমা:** একক split; pairing/bootstrapping নেই।

## E. Figures

**Fig. 8 — Union-mean local contribution (breakdown) of top-5 variables: Aus (a–e), Aman (f–j), Boro (k–o)**
- **Layout/axes:** ধূসর DEM background; বিন্দু = union; বিন্দুর আকার = মান; প্রতিটি panel-এর নিজস্ব legend (৫–৬ শ্রেণি, প্রতি panel-এ আলাদা break; একক নেই)। কলাম: N-rates, P-rates, K-rates, Field duration, Crop types।
- **Legend values (ছবি থেকে):** Aus N-rates: <55.6, 55.7–88.0, 88.1–132.4, 132.5–170.3, 170.4–226.4, >226.4। Aus crop types: <27.2 … >192.0। Aman crop types: <104.4 … >159.9। Boro crop types (o): <−71.5, −71.4…−60.2, −60.1…−40.8, −40.5…−21.1, −21.0…4.9, >5.0 (বেশিরভাগ negative)।
- **প্যাটার্ন:** Aus-এ কম বিন্দু (78 union) ও বিচ্ছিন্ন; Aman/Boro-য় ঘন। Aman crop-type (j)-এর বিন্দু বড় ও বহুল (জাতের সর্বব্যাপী ভূমিকা)। Boro crop-type (o) legend-এর বেশিরভাগ মান negative — (HYV vs hybrid; local নেই)।
- **Authors' interpretation:** "scattered all over", কিছু অঞ্চলে বেশি (পশ্চিমে crop type Aus; দক্ষিণে P, উত্তরে K Aman)। **Support?** আংশিক — গুণগত; কোনো spatial statistic (Moran's I, cluster test) নেই; "দক্ষিণে/উত্তরে" দাবির জন্য কোনো test নেই।
- **Visual/methodological সমস্যা:**
  1. **Unit লেখা নেই** legend-এ (মনে হয় kg/ha)।
  2. **Break পদ্ধতি অজানা**, প্রতি panel-এ আলাদা break ⇒ প্যানেলগুলো সরাসরি তুলনা করা যায় না (N-rate-এর "বেশি" Aus-এর 226 বনাম Boro-র 127 — ভিন্ন scale)।
  3. **Legend বনাম "%-positive" text:** Aus N-rate legend-এর সর্বনিম্ন শ্রেণি "<55.6" (সব ধনাত্মক মান) — যদি শ্রেণি সমান-সংখ্যক (quantile) হত, বেশিরভাগ union-এর contribution > 0 — text-এর "51% positive"-এর সাথে মেলে না। Break-পদ্ধতি (natural breaks?) না জেনে সমাধান অসম্ভব — **Unresolved**।
  4. বিন্দুর আকার ছোট/বড় ধূসর/কালো, overplotting; union-প্রতি n নেই।
  5. Fig. 8-এর model = ভিন্ন saved model (5.5)।

## F. Tables
এই পেজে নেই। **SI/code cross-check:** S6 (F3), S5 (F5), HTML metalearner।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 9.1 | §3.6: "Aus weak FD" ভুল; S5 Aus 0.309, Aman 0.277, Boro 0.058; Fig. 9(l) Boro দুর্বল; Discussion p11 সঠিক | p9 §3.6; SI S5; `work/check07b.out`; Fig. 9 | Confirmed issue |
| 9.2 | "Stacking ensemble effectively captured these relationships" — GW correlation-এ stack ব্যবহৃত হয়নি | p9 §3.6; `gw_correlation_aman_01.Rmd:76-80` | Confirmed issue |
| 9.3 | "water-saving practices" ও "maintaining productivity" — water/yield-scaled emission বিশ্লেষণে নেই | p9 §3.6; p12 | Confirmed issue (claim ← evidence) |
| 9.4 | "1–4% vs DRF": test 0.91–1.47%, CV 1.07–6.23% (stage ভিন্ন), Aus test best single XRT 820.8 থেকে মাত্র 0.39% | SI S6; `work/check_arith.out` | Confirmed issue |
| 9.5 | Stack-এর "bias+variance কমায়" — এই data-য় পরীক্ষা নেই; 958-এর 769 GBM; অধিকাংশ coefficient 0 | p9 §4; HTML metalearner | Potential concern |
| 9.6 | "Local XAI overcomes GW regression constraints" — তুলনা নেই; ভিন্ন জিনিস মাপে | p9 §4 ¶১ | Potential concern |
| 9.7 | Fig. 8: legend-এ unit নেই, break-পদ্ধতি অজানা, প্রতি panel আলাদা scale; "%-positive" ও legend-এর মিল অনিশ্চিত | Fig. 8 | Unresolved question |
| 9.8 | "Fertilizer effects on GHG" causal ভাষা + CCAFS-MOT circularity | p9 §3.6; p3 §2.2 | Potential concern |
| 9.9 | Local correlation-এ union-গড় (ecological), row-level কম | `work/check07b.out` | Potential concern |
| 9.10 | Novelty claim (p2) বনাম Discussion-এ Ahmed 2024 (maize AutoML+XAI Bangladesh) | p2; p9 | Potential concern |
| 9.11 | "crop duration" ও "field duration" — একই কি না অস্পষ্ট; কোথাও সংজ্ঞা নেই | p9; p2 | Unresolved question |
| 9.12 | Stack vs single model-এর gap-এর জন্য repeated split/CI নেই | S6 | Research opportunity |

**লেখকদের পক্ষে:** Discussion-এ "appear to influence" বলা সতর্ক ভাষা; S6-এ সব model-এর সব stage; সম্পর্কিত কাজের সাথে নিজের কাজ যুক্ত করার চেষ্টা।

**Reviewer-এর প্রশ্ন:** কোন stage-এ "1–4%"? Local XAI vs GWR তুলনা কোথায়? GW correlation-এ stack-এর ভূমিকা কী? Fig. 8-এর unit ও break?

## H. সারাংশ
- **Short summary:** Fig. 8 union-গড় attribution; §3.6 শেষে FD-claim ভুল ও stack-সংক্রান্ত অযৌক্তিক বাক্য; Discussion-এ "১–৪%" ও stacking-যুক্তি।
- **৫ key terms:** GW correlation, Local XAI vs GWR, Yield-scaled emission, Meta-learner coefficient, Improvement %।
- **Takeaways:** (১) F3 — improvement 0.9–1.5% (test); (২) F5 — Boro-ই FD-দুর্বল; (৩) GWC-তে stack-এর ভূমিকা নেই; (৪) Fig. 8-এর unit/break অজানা।
- **Key numbers:** 1–4% (paper); 1.47/1.08/0.91% test; 6.23/1.81/1.07% CV; 0.39% (Aus vs XRT); S5 FD 0.309/0.277/0.058।
- **পরের পেজ-প্রশ্ন:** Fig. 9 legend-এর ">0.035" ঠিক? N-rate দাবি বাস্তবে কী?

## Master Notes
- **Paragraph-wise:** §3.6 শেষ; Discussion ¶১–৪ শুরু।
- **Exact numbers:** (H)।
- **Claims & evidence:** "Aus weak FD" ✗; "stack captured relations" ✗; "1–4%" ✗ (0.9–1.5% test)।
- **Open checks:** break-method Fig. 8; CCAFS-MOT circularity মাত্রা।
- **MSc notes:** XAI vs spatial-statistics-এর তুলনা নিজের মতো করে বলবেন না; GHG বাদ রাখলে এই সমস্যা নেই; improvement-এর CI।
