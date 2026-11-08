# Observation register (সব page-এর section G একসাথে; `work/scripts/build_registers.py` দিয়ে auto-generated)

মোট observation: 20 | Potential concern: 5, Confirmed issue: 11, Unresolved question: 2, Research opportunity: 2

| # (page.n) | কী পেলাম | প্রমাণ | ধরন | page |
|---|---|---|---|---|
| 1.1 | Abstract-এ GHG যে **modeled (CCAFS-MOT)**, measured নয় — তা বলা নেই | p1 abstract; p3 §2.2 ("estimated emissions are based solely on modeled outputs") | Potential concern  | [p01](../pages/page-01.md) |
| 1.2 | Abstract-এর causal ভাষা ("influencing", "impact") vs p12 Limitation ("do not explain why things happen") | p1 abstract vs p12 | Potential concern  | [p01](../pages/page-01.md) |
| 1.3 | "IPCC, 2019" reference-এর title = "Annex IV: reviewers of the IPCC special report…" (reviewer list); "one-third" claim support করে না | p1 ¶1; ref list p14 | Confirmed issue  | [p01](../pages/page-01.md) |
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
