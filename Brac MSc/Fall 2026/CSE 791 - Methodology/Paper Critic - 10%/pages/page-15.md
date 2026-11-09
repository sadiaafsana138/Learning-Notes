# Page 15 — References (Krupnik 2015 … Staniak 2018)

← [page-14](page-14.md) | [page-16](page-16.md) →

## A. এই পেজে কী আছে
- Reference-এর প্রায় ৬৫ entry: Krupnik 2015 → Staniak & Biecek 2018। এখানে আছে **Rudin 2019, Ribeiro 2016, Song 2020, Quiñones 2021, Hipp & Chalise 2015, Padarian 2020, Sapkota 2014/2021, Shahhosseini 2020, Shiragi 2017, SRDI, Staniak 2018, Le Mer 2001, Signor 2013 (পরিমাণে)**।
- Main message: নেই (list); আমাদের লক্ষ্য — MSc-র জন্য সবচেয়ে প্রাসঙ্গিক entry (Rudin, Song) ও সন্দেহজনক citation চিহ্নিত।

## B. Paragraph ধরে ধরে ব্যাখ্যা (reference-গুচ্ছ)

### B1. MSc-র জন্য গুরুত্বপূর্ণ entry
| Ref | Title | paper-এ ভূমিকা | আমাদের নোট |
|---|---|---|---|
| **Rudin, 2019** (Nat. Mach. Intell. 1, 206–215) | "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead" | p2: "black box … drawbacks for high-stakes decision-making" | Rudin interpretable model পরামর্শ দেন; paper উল্টো পথে; আলোচনা নেই (2.4) |
| **Song et al., 2020** (Nat. Commun. 11, 5668) | "Cross-site transportability of an explainable artificial intelligence model for acute kidney injury prediction" | p2: XAI স্বাস্থ্যখাতে | মূল বিষয় transportability — এই paper পরীক্ষা করেনি (2.5, **Research opportunity**) |
| **Ribeiro et al., 2016** (arXiv 1606.05386) | "Model-agnostic interpretability of machine learning" | p4–5: model-agnostic; breakdown-এর জন্যও | Breakdown-এর সঠিক সূত্র Staniak & Biecek 2018 (এই পেজেই) |
| **Staniak & Biecek, 2018** | "Explanations of model predictions with live and breakDown packages" | p5: breakdown | সঠিক |
| **Padarian et al., 2020** | "Game theory interpretation of digital soil mapping convolutional neural networks" (Soil 6) | p9: local interpretation | প্রাসঙ্গিক (SHAP-স্টাইল) |
| **Shahhosseini et al., 2020** | "Forecasting corn yield with machine learning ensembles" (সম্পূর্ণ title p15-এ) | p2: stacking in crop yield — "limited attention, few exceptions" | মেলে ✓ |

### B2. সন্দেহজনক/ঢিলা citation (title মিলিয়ে)
| Ref | Title | text-এ দাবি | মূল্যায়ন |
|---|---|---|---|
| **Quiñones, Goyal, Ahmed 2021** (Sci. Rep. 11, 6955) | "Geographically weighted machine learning model for untangling spatial heterogeneity of type 2 diabetes mellitus (T2D) prevalence in the USA" | p2: linear regression "require strong assumptions (normality, collinearity)"; p9: GW regression-এর সীমা | T2D-GW-ML paper (লেখকের সহ-গবেষণা); linear-regression-assumption-এর সূত্র হিসেবে অপ্রত্যক্ষ — **Potential concern** |
| **Hipp & Chalise 2015** | "Spatial analysis and correlates of county-level diabetes prevalence, 2009–2010" | p9: GW regression distance of influence অজানা | ডায়াবেটিস; সাধারণ spatial প্রসঙ্গ, সরাসরি পদ্ধতি-সূত্র নয় — **Potential concern** |
| **Sapkota et al., 2014** (Field Crops Res. 155) | "Precision nutrient management in conservation agriculture based **wheat** production of Northwest India: profitability, nutrient use efficiency and environmental footprint" | p10: precision N management NUE ও GHG ধান-এর জন্য | গম, উত্তর-পশ্চিম ভারত — **Potential concern** |
| **Shiragi et al., 2017** | "Pedotransfer Function of Bangladesh Soils" (journal/DOI নেই) | p3: SRDI soil dataset-এর সূত্র | ডেটাসেট-সূত্র হিসেবে পরোক্ষ — Potential concern |
| **SRDI, 1996–2014** | "Land and Soil Resources Utilization (in Bengali)" | p3: soil sample processing method | বাংলা, DOI নেই — যাচাইযোগ্যতা কম |
| **Le Mer & Roger 2001; Signor & Cerri 2013** | CH₄ ও N₂O-র review | p11: GHG প্রক্রিয়া | মেলে ✓ |

### B3. R/software citation
- ref list-এ **R Core Team, 2021** (একটি); text-এ 2020/2021a/2021b/Team 2021 (13.7)।
- Nychka 2017 (fields), Pebesma 2004 (gstat), Busetto 2016 (MODIStsp), Gollini 2015 (GWmodel), Ledell 2020 (h2o) ✓ — software-সূত্রগুলো উপস্থিত।

## C. নতুন শব্দগুলো

#### Interpretable model (inherently) vs Post-hoc explanation
- **সহজ মানে:** Interpretable = model নিজেই পড়ার মতো (linear regression, ছোট decision tree, GAM); Post-hoc = জটিল model-এর পরে ব্যাখ্যা।
- **ছোট উদাহরণ:** yield = 800 + 9·N + 5·P + 350·(hybrid) — প্রতিটি সংখ্যা সরাসরি পড়া যায়। Random forest-এ এমন সূত্র নেই।
- **এই paper-এ:** Rudin-কে cite করে post-hoc পথে গেছে।
- **খেয়াল:** আমাদের Check 9: OLS test R² Aus 0.284, Aman 0.378, Boro 0.197; RF 0.503/0.575/0.515 — interpretable baseline-এ accuracy কম, কিন্তু খুব কমও নয় (Aman)।

#### Transportability / Transferability
- **সহজ মানে:** এক site-এর data-য় train করা model অন্য site-এ প্রয়োগ।
- **ছোট উদাহরণ:** Aus-এর ৭০টা union-এ train করে বাকি ৮টা অদেখা union-এ পরীক্ষা (leave-union-out)।
- **এই paper-এ:** নেই; Song 2020-এ কেন্দ্রীয় প্রশ্ন।

#### Preprint (arXiv)
- **সহজ মানে:** peer-review ছাড়াই প্রকাশিত খসড়া।
- **খেয়াল:** Ribeiro 2016 = arXiv/ICML workshop; LIME-এর মূল paper নয়।

## D. Equation / statistics
এই পেজে নেই। (আমাদের check 9 সংখ্যা উপরে C-তে।)

## E. Figures
এই পেজে নেই।

## F. Tables
এই পেজে নেই (উপরের ছক নোট-হিসেবে)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 15.1 | Rudin 2019 = interpretable-model advocacy; paper আলোচনা করেনি | refs p15; p2 | Confirmed issue |
| 15.2 | Song 2020 = cross-site transportability; paper-এ অপরীক্ষিত | refs p15; p2 | Research opportunity |
| 15.3 | Quiñones 2021 ও Hipp & Chalise 2015 (diabetes) — linear-assumption/GW-limitation দাবির সরাসরি সূত্র নয় | refs p15; p2, p9 | Potential concern |
| 15.4 | Sapkota 2014 = গম (NW India), ধান-দাবির জন্য | refs p15; p10 | Potential concern |
| 15.5 | Shiragi 2017 "Pedotransfer Function of Bangladesh Soils" — SRDI 50,000-point dataset-এর সূত্র হিসেবে পরোক্ষ; SRDI report বাংলা/DOI-হীন | refs p15; p3 | Potential concern |
| 15.6 | Ribeiro 2016 breakdown-এর জন্য; সঠিক Staniak & Biecek 2018 (একই পেজে) | refs p15; p5 | Confirmed issue (minor) |
| 15.7 | OLS বনাম RF (নিজস্ব check): R² Aus 0.284/0.503, Aman 0.378/0.575, Boro 0.197/0.515 | `work/check03_09_10.out` | (আমাদের own check) Potential concern: "ML beats linear" টিকে যায়, কিন্তু gap paper-এর intercept-only তুলনার চেয়ে ছোট |

**লেখকদের পক্ষে:** Shahhosseini 2020, Padarian 2020, Staniak & Biecek 2018, Biecek & Burzykowski 2021 — পদ্ধতিগত সূত্র সঠিক ও প্রাসঙ্গিক; Rudin ও Song-কে অন্তত উল্লেখ করা তাদের সততা দেখায় (আলোচনা না করলেও)।

**Reviewer-এর প্রশ্ন:** Rudin-এর যুক্তির সামনে stacking-এর "black box" সিদ্ধান্ত কেন যুক্তিসঙ্গত? Transportability কেন পরীক্ষিত নয়?

## H. সারাংশ
- **Short summary:** p15 refs-এ MSc-র জন্য দু'টি মূল entry (Rudin, Song) ও কয়েকটি ঢিলা citation।
- **৫ key terms:** Interpretable model, Post-hoc, Transportability, Preprint, Pedotransfer function।
- **Takeaways:** (১) Rudin ≠ এই paper-এর পথ; (২) Song = আপনার gap; (৩) Sapkota 2014 গম।
- **Key numbers:** ~65 entries (এই পেজে); OLS vs RF R² (C-তে)।
- **পরের পেজ-প্রশ্ন:** p16-এ Suarez-Gutierrez, Wang 2018c, UNEP, Sutton-Grier কেমন?

## Master Notes
- **Paragraph-wise:** B1 (key refs), B2 (সন্দেহজনক), B3 (software)।
- **Exact numbers:** OLS/RF R²।
- **Claims & evidence:** Rudin/Song ছকে।
- **Open checks:** Quiñones 2021-এ linear-assumption আলোচনা আছে কি? (full text লাগবে)।
- **MSc notes:** Rudin 2019, Song 2020 আপনার literature review-এর কেন্দ্র; interpretable baseline + transportability test = আপনার contribution।
