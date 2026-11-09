# Page 01 — Title, Abstract, Introduction (শুরু)

← আগের পেজ: নেই (এটাই প্রথম) | পরের পেজ: [page-02](page-02.md) →

## A. এই পেজে কী আছে

- Title, authors, affiliation, keywords, **Abstract**, আর **Section 1 Introduction**-এর প্রথম অংশ।
- Main message: AutoML + XAI দিয়ে বাংলাদেশের Aus/Aman/Boro ধানের yield predict করা, কোন factor yield-কে "influence" করে তা বের করা, আর modeled GHG emission-এর সাথে ওই factor-গুলোর সম্পর্ক দেখা।
- লেখকরা কেন এটা রাখলেন: পাঠককে দ্রুত বলতে চান "stack ensemble সবচেয়ে ভালো", "PFI-তে ৫টা factor গুরুত্বপূর্ণ", আর "GHG কমানো কঠিন"।
- Research-এর কোন অংশ: পুরো paper-এর সারসংক্ষেপ + background/motivation।
- পরের পেজে (p2) Introduction চলতে থাকে: Bangladesh-এর context, ML/stacking/AutoML/XAI-এর gap।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. Abstract (লাইন ১–১৩ প্রায়)
- **কী বলছে:** AutoML models ধানের yield predict করতে পারে; XAI দেখায় কোন factor yield আর GHG-কে "influence" করে। Aus = winter→rainy transition, Aman = rainy season, Boro = irrigated winter season। Stack ensemble সব season-এ সব single model-কে হারিয়েছে। PFI বলেছে ৫টা key factor: rice type (local/HYV/hybrid), field duration, N, P, K rate। Breakdown plot দেখিয়েছে average effect-এর spatial variation। GHG-র সাথে এই factor-গুলোর সম্পর্ক positive আর spatially variable।
- **লেখকরা কী বোঝাতে চান:** এই পদ্ধতি দিয়ে "কী কারণে yield আর emission বদলায়" বোঝা যায়, তাই mitigation কঠিন।
- **কঠিন শব্দ:** *AutoML* = অনেক model নিজে নিজে try করে সেরাটা বেছে দেয় এমন tool; *XAI* = model-এর ভেতরের "কেন এই prediction" বোঝার পদ্ধতি; *model-agnostic* = যেকোনো model-এ চলে।
- **খেয়াল রাখার মতো:**
  1. Abstract-এ বলা নেই যে GHG **measure করা হয়নি, CCAFS-MOT model দিয়ে হিসাব করা** (p3 §2.2 এ বলা আছে)। শুধু "GHG emissions" পড়লে মনে হয় মাপা data।
  2. "factors **influencing** yields", "**impact** of these factors" — causal ভাষা। অথচ p12 Limitations বলছে XAI "do not explain why things happen" (causation নয়)। দুই জায়গায় মিল নেই।
  3. "stack ensemble outperformed all individual models in **all seasons**" — Table S6 test RMSE দেখলে gap অনেক ছোট (p9 ও registers দেখুন)। Aus test-এ XRT 820.8 vs stack 817.6।
  4. "PFI ... identified five key factors" — PFI **predictive importance**, causal effect নয়।
  5. Abstract-এ "spatial variations in average effects" — এটা Union-average **local attribution** (breakdown); spatial transferability test করা হয়নি।

### B2. Introduction ¶1 (লাইন ৩৩–৪৪): GHG, climate, food systems
- **কী বলছে:** GHG বাড়ার ফলে খাদ্য উৎপাদন ঝুঁকিতে (Lobell 2011)। CH₄, CO₂, N₂O প্রায় ১৫০, ৪০, ২০% বেড়েছে (IPCC 2014)। Food system global anthropogenic GHG-র **one-third** (Crippa 2021; IPCC 2019)। মোট নির্গমন 59.1 ± 5.9 GtCO₂e (2019); agricultural food system-এর অংশ **15%** (UNEP 2020)।
- **লেখকরা কী বোঝাতে চান:** সমস্যাটা বিশাল, তাই ধান নিয়ে কাজ জরুরি।
- **খেয়াল রাখার মতো:**
  1. **"one-third" বনাম "15%"** — একই paragraph-এ দুটো সংখ্যা, scope ব্যাখ্যা নেই (food system পুরো supply chain + land-use change ধরলে ~⅓; শুধু agriculture ধরলে কম)। পাঠক confuse হবে। "বড় সংখ্যা vs ছোট সংখ্যা" ব্যাখ্যা ছাড়া **Potential concern**।
  2. **Citation:** "IPCC, 2019" — reference list-এ এর title: *"Annex IV: reviewers of the IPCC special report on climate change and land"* (p13–14 refs)। অর্থাৎ reviewer-দের নামের তালিকা; "one-third" claim-এর source হতে পারে না। (একই বন্ধনীতে থাকা **Crippa et al. 2021** = "Food systems are responsible for a third of global anthropogenic GHG emissions" (p14 refs) — এটাই claim-কে সমর্থন করে; তাই claim ঠিক, কিন্তু IPCC 2019 entry অপ্রাসঙ্গিক।) **Confirmed issue** (citation mismatch)। (সঠিক source হতে পারে SRCCL-এর Chapter 5, কিন্তু সেটা paper-এ নেই — "Not reported in the provided paper".)
  3. "150, 40, 20%" IPCC 2014 (AR5 WGIII) — সংখ্যাটা আমরা AR5 থেকে যাচাই করিনি; **Unresolved**।

### B3. Introduction ¶2 (লাইন ৪৫–৫৮): rice importance, sustainability
- **কী বলছে:** ধান এশিয়ার smallholder-দের জন্য গুরুত্বপূর্ণ; জনসংখ্যা বাড়ছে তাই উৎপাদন বাড়াতে হবে কিন্তু sustainable-ভাবে; century-র শেষে net negative emissions লাগবে (IPCC 2014; **Suarez-Gutierrez et al., 2018**)। নতুন studies (Xu 2025, 2026) বলছে resource management দিয়ে GHG কমানো যায়। CH₄ কমানো সম্ভব yield না কমিয়ে, তবে trade-off আছে (**Gaihre et al., 2015**)।
- **খেয়াল রাখার মতো (citation check, ref list থেকে title quote):**
  1. Suarez-Gutierrez 2018 → *"Internal variability in European summer temperatures at 1.5°C and 2°C of global warming"* (Environ. Res. Lett. 13, 064026)। ইউরোপের গ্রীষ্মকালীন তাপমাত্রার internal variability নিয়ে; "net negative emissions by century end" বা ধান-mitigation claim-এর support নয়। **Confirmed issue**।
  2. Gaihre 2015 → *"Impacts of urea deep placement on nitrous oxide and nitric oxide emissions from rice fields in Bangladesh"* (Geoderma 259)। এটা **N₂O/NO** নিয়ে; text বলছে **CH₄** কমানোর কথা। Gas মেলেনি। **Confirmed issue**। (Gaihre-এর অন্য কাজ "Effects of irrigation regimes... methane" ref list-এ আছে 2023-এ; সম্ভবত সেটাই উদ্দেশ্য ছিল — এটা আমাদের অনুমান, **suspected**।)
  3. "Xu et al., 2025, 2026" — ref list-এ আলাদাভাবে যাচাই করা যায় (p16 refs); এখানে content check করিনি।

## C. নতুন শব্দগুলো

#### AutoML (Automated Machine Learning)
- **সহজ মানে:** অনেকগুলো model আর hyperparameter নিজে নিজে try করে সেরাটা বেছে দেওয়া একটা tool।
- **কীভাবে কাজ করে:** ধরুন আপনি ৬টা algorithm (GLM, DRF, GBM...) চালাবেন, প্রত্যেকটার ১০০ রকম setting। হাতে করলে ৬০০ বার। AutoML সেটা loop-এ চালায়, cross-validation RMSE দিয়ে rank করে leaderboard বানায়।
- **এই paper-এ:** H2O AutoML (R), p4 §2.3.1। সব season-এ stacked ensemble best।
- **খেয়াল রাখতে হবে:** AutoML মানে "ভালো validation" নয়; validation split ঠিক না হলে (p4 এ random row split) সব model-ই অতিরিক্ত ভালো দেখাতে পারে।

#### XAI (Explainable AI)
- **সহজ মানে:** black-box model কেন এই উত্তর দিল তা বোঝার পদ্ধতি।
- **কীভাবে কাজ করে:** যেমন একটা feature-এর value এলোমেলো করে (shuffle) দেখি error কতটা বাড়ে — বাড়লে feature গুরুত্বপূর্ণ।
- **এই paper-এ:** PFI, PDP, ALE, breakdown (p5)।
- **খেয়াল রাখতে হবে:** XAI model-এর আচরণ বলে, বাস্তব জগতের কারণ-ফল নয়।

#### Stacked ensemble
- **সহজ মানে:** অনেক model-এর prediction আরেকটা model (meta-learner) দিয়ে জোড়া লাগানো।
- **ছোট উদাহরণ:** model A বলল 4000, B বলল 4400, meta-learner weights 0.6/0.4 → 0.6×4000+0.4×4400 = 4160।
- **এই paper-এ:** p4 §2.3.1; p9 Discussion-এ "১–৪% RMSE improvement vs DRF"।
- **খেয়াল রাখতে হবে:** Improvement ছোট হলে repeated split ছাড়া noise আর real gain আলাদা করা যায় না।

#### GHG, CH₄, N₂O, CO₂e, GWP
- **সহজ মানে:** greenhouse gas। CO₂e = সব gas-কে CO₂-র সমান ধরে একক। GWP = Global Warming Potential, ১ kg gas কত kg CO₂-র সমান warming করে।
- **উদাহরণ (সংখ্যা):** 100-year GWP ধরলে CH₄ ≈ 28–34 × CO₂, N₂O ≈ 265–298 × CO₂ (AR5 range; এই paper কোন factor নিয়েছে তা **Not reported in the provided paper, Supporting Information, or available code**)।
- **এই paper-এ:** `Total_GWP` column (kg CO₂e/ha) — CCAFS-MOT থেকে।

#### Model-agnostic
- **সহজ মানে:** যেকোনো model-এর ভেতর না দেখে শুধু input→output দেখে ব্যাখ্যা করা।

## D. Equation / statistics
এই পেজে নেই।

## E. Figures
এই পেজে নেই।

## F. Tables
এই পেজে নেই।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 1.1 | Abstract-এ GHG যে **modeled (CCAFS-MOT)**, measured নয় — তা বলা নেই | p1 abstract; p3 §2.2 ("estimated emissions are based solely on modeled outputs") | Potential concern |
| 1.2 | Abstract-এর causal ভাষা ("influencing", "impact") vs p12 Limitation ("do not explain why things happen") | p1 abstract vs p12 | Potential concern |
| 1.3 | "IPCC, 2019" reference-এর title = "Annex IV: reviewers of the IPCC special report…" (reviewer list) — "one-third" claim-এর সূত্র হিসেবে অপ্রাসঙ্গিক (claim নিজে Crippa 2021 দ্বারা সমর্থিত) | p1 ¶1; ref list p14 | Confirmed issue |
| 1.4 | Suarez-Gutierrez 2018 = ইউরোপের গ্রীষ্মকালীন তাপমাত্রা; net-negative-emissions claim-এর সাথে মিল নেই | p1 ¶2; ref list p16 | Confirmed issue |
| 1.5 | Gaihre 2015 = N₂O/NO (urea deep placement); text-এ CH₄ কমানোর claim | p1 ¶2; ref list | Confirmed issue |
| 1.6 | "one-third" (food systems) vs "15%" (agri food system) — scope ব্যাখ্যা নেই | p1 ¶1 | Potential concern |
| 1.7 | Abstract-এ "outperformed all individual models" — S6 test gap ছোট (Aus: XRT 820.8 vs stack 817.6 = 0.39%); দেখুন p9 | Abstract; SI Table S6 (si.txt p12); script `work/scripts/check_arith_F1_F4.py` | Potential concern |
| 1.8 | Abstract-এ ৩টা season-এর মধ্যে Aus-কে "transition from winter to rainy season" বলা হয়েছে, কিন্তু p11 Discussion-এ Aus "rainfed", "pre-monsoon" বলা হয়েছে; Data-তে Aus `Water regime` = "Rainfed, wet season" (677/677) | p1; p11; `aus_data_all.csv` | Unresolved question (সংজ্ঞা সামান্য ঢিলে) |

**লেখকদের পক্ষে ন্যায্য কথা:** Abstract সংক্ষিপ্ত; লেখকরা Limitations-এ (p12) পরে causation-এর কথা স্বীকার করেছেন। ধান, GHG আর food security-র motivation যুক্তিসঙ্গত।

**Peer reviewer-এর প্রশ্ন:** (১) Abstract-এ কি GHG modeled তা লেখা যায় না? (২) "influencing" শব্দ কি "associated with" হবে না? (৩) IPCC 2019-এর সঠিক chapter কোনটা?

## H. সারাংশ
- **Short summary:** পেপারটা তিন season-এর ধানের yield-এ AutoML stack ensemble + XAI চালিয়ে N, P, K, field duration, crop type-কে প্রধান predictor বলছে, আর modeled GHG-এর সাথে spatial correlation দেখাচ্ছে।
- **৫টা key term:** AutoML, XAI, Stacked ensemble, GWP/CO₂e, Model-agnostic।
- **Takeaways:** (১) Abstract causal শোনায়, আসলে predictive association; (২) GHG modeled; (৩) p1-এর ৩টা citation (IPCC 2019, Suarez-Gutierrez, Gaihre) claim-এর সাথে মেলে না।
- **Key numbers (exact):** 59.1 ± 5.9 GtCO₂e (2019); 15% (agri food system); one-third (food systems); CH₄/CO₂/N₂O +150/40/20% (IPCC 2014)।
- **পরের পেজের প্রশ্ন:** Data row-এর unit কী? Stacking-এর gap কী যা paper দাবি করছে? XAI আগে ধানে হয়নি — সত্যি?

## Master Notes
- **Paragraph-wise:** Abstract → ৫ key factors, stack ensemble best, spatial attributions, positive spatially-variable GHG relation। Intro ¶1 GHG stats; ¶2 rice + sustainability।
- **Exact numbers:** 59.1 ± 5.9 GtCO₂e; 15%; 150/40/20%।
- **Claims & evidence:** "Food systems = ⅓" → Crippa 2021 সমর্থন করে; IPCC 2019 entry (reviewer list) অপ্রাসঙ্গিক। "Rice CH₄ কমানো যায়" → Gaihre 2015 N₂O নিয়ে।
- **Open checks:** IPCC 2014 percentages verify; Xu 2025/2026 content।
- **MSc notes:** নিজের proposal-এ citation-গুলো title পর্যন্ত যাচাই করুন; "influence/impact" না লিখে "associated with" লিখুন; GHG যদি না থাকে (আপনার scope-এ নেই) তবে এই অংশের দরকার নেই।
