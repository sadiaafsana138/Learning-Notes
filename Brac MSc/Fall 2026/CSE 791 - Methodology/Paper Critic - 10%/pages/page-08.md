# Page 08 — §3.4 PDP/ALE, §3.5 Breakdown maps, §3.6 GHG local correlation (শুরু), Fig. 7

← [page-07](page-07.md) | [page-09](page-09.md) →

## A. এই পেজে কী আছে
- **§3.4** PDP ও ALE (Fig. 7), **§3.5** Breakdown plot দিয়ে union-wise attribution (Fig. 8 → p9), **§3.6** GHG-র সাথে local correlation-এর শুরু (Fig. 9 → p10)।
- Main message: N, P, K ধনাত্মক ও nonlinear; field duration-এর marginal effect নগণ্য; hybrid/HYV > local; stack model "additive"; breakdown-এ prediction-এর স্থানিক contribution।
- এই পেজে অনেকগুলো figure-reference ভুল আছে (নিচে)।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. §3.4 ¶১ PDP/AL results (লাইন ১–১৫)
- **কী বলছে:** "Fig. 6 shows PDP and AL profile plots of the first five important factors…"; N-rate (Fig. 7a,f,k), P-rate (**Figs. 6b**, 7g,l), K-rate (Figs. 7c, **6h**, m) সব season-এ **positive (blue lines)**, তবে non-linear; field duration important কিন্তু marginal effect negligible (Fig. 7d,i,n); hybrid/HYV > local (Fig. 7 leftmost panel)।
- **খেয়াল:**
  1. **Figure reference ভুল (Seed verified):** "Fig. 6 shows PDP/AL" → হবে **Fig. 7**; "Figs. 6b", "6h" → Fig. 7b, 7h। (Fig. 6 = PFI।)
  2. **"leftmost panel" ভুল:** Crop type panel Fig. 7-এ **rightmost** (e, j, o)।
  3. **Colour ভুল:** "(blue lines)" ঠিক PD-র জন্য; কিন্তু §3.4 ¶২-এ "AL profiles (**blue-lines** in Fig. 7)" — legend (Fig. 7a): **PD = নীল, AL = কমলা**। **Confirmed issue**।
  4. **Field duration:** PFI-তে 61–70% (p7) অথচ PD/ALE flat — **Seed F9**। লেখকরা নিজেই দুটো উল্লেখ করেছেন (p8, p11: "effects … marginal") কিন্তু বিরোধের ব্যাখ্যা দেন না। সম্ভাব্য কারণ (সবই **suspected**): (a) interaction (field duration × crop type/season/N) — PFI interaction সহ গুরুত্ব ধরে, PDP/ALE গড় করে ফেলে; (b) field duration ≈ crop type-এর proxy (hybrid ও HYV/local-এর duration ভিন্ন) — তাই shuffle করলে variety-তথ্য নষ্ট হয়; (c) PFI train-data-য়, গড় PDP-ও train-এ — দুটোর পার্থক্য data-র ব্যবহারে নয়, পদ্ধতিতে। যাচাই-উপায়: `Feature_Interaction.csv` (H-statistic) — কোডে আছে, paper-এ report নেই (§B2)। (Code: `yield_aus_autoML.Rmd:1066–1076`; Aman:1089; Boro:1093।)
  5. Train data-য় PDP/ALE (`model_profile(explainer = explainer_train …)`, Aus Rmd:1016–1054)।
  6. কিছু feature-value range-এ (যেমন N-rate 200–400 kg/ha, Boro-তে ~400) data খুবই কম — curve-এর ডানপ্রান্ত অনির্ভরযোগ্য।

### B2. §3.4 ¶২ Additivity (লাইন ১৬–২০)
- **কী বলছে:** PDP additive model-এ ঠিক বর্ণনা দেয় না যখন feature correlated; AL ঠিক summary দেয়। "AL profiles (blue-lines) paralleled to PDP profiles for all five features suggest that the stack-ensemble model is **additive**।"
- **খেয়াল (সবচেয়ে গুরুত্বপূর্ণ):**
  1. **যুক্তিটা ঠিক নয়:** PD ও AL **কাছাকাছি** হওয়া মানে feature-গুলো correlation-এর কারণে PD-কে বিকৃত করছে না — এটা additivity-র প্রমাণ নয়। Additivity মানে f(x) = Σ f_j(x_j) (কোনো interaction নেই)। এটা পরীক্ষা করার সরঞ্জাম **H-statistic (Friedman & Popescu)**। কোডে `iml::Interaction$new(mod)` **চালানো হয়েছে** আর `Feature_Interaction.csv` লেখা হয়েছে (Aus Rmd:1068–1076; Aman:1089; Boro:1093) — কিন্তু paper/SI-তে **কোথাও report নেই** (grep: paper-এ "interaction", "H-statistic" নেই)। ফলে "additive" claim-এর প্রমাণ শুধু PD ≈ AL। **Confirmed issue** (claim ← evidence mismatch)।
  2. **"all five features parallel" ভুল:** Fig. 7(o) Boro crop type: PD (নীল) Hybrid ≈ 6000, HYV ≈ 5700; AL (কমলা) Hybrid ≈ 5650, HYV ≈ 5200 — পার্থক্য ~৩৫০–৫০০ kg/ha (বা ~৬–৯%) (ছবি থেকে আনুমানিক)। Fig. 7(d) Aus field duration-এও PD ও AL আলাদা (নিচে PD flat-down, AL slight slope)। অর্থাৎ "সব ৫টায় parallel" অতিসরলীকরণ।
  3. Stack ensemble-এ GBM/DRF/DNN (non-additive learners) — সাধারণ ধারণা: interaction **আছে**; তাই additive হওয়া প্রত্যাশিত নয়, বিশেষত field-duration/variety interaction।
  4. Local (breakdown) union-attribution-এ প্রায়শই feature-সংমিশ্রণ জড়িত; additivity ধরলে local attribution সারাংশ ভালো — কিন্তু প্রমাণিত নয়।

### B3. §3.5 Breakdown plots (লাইন ২১–৫৭ প্রায়)
- **কী বলছে:** Union-average attribution top-5 feature-এর (Fig. 8)। Aus: N, P, K, field duration, crop type-এ positive contribution **51, 42, 41, 30, 51%** unions-এ; "scattered all over"; crop type-এর বেশি positive contribution পশ্চিমে (Fig. 8e)। Aman: crop type **>70%** unions (Fig. 8j); N, P, K, FD: **57, 53, 37, 50%**; N (8f) ও crop type সারা দেশে; **P-rate (Fig. 7g)** ও K-rate (Fig. 8h) দক্ষিণ ও উত্তরে। Boro: **N 167, K 125, P 124** unions; crop type শুধু **18%** unions (উত্তর/উত্তর-পূর্ব, Fig. 8o)।
- **খেয়াল:**
  1. **Reference ভুল:** "P-rate (**Fig. 7g**)" → হবে **Fig. 8g**। **Confirmed issue**।
  2. **Unit mismatch (percent vs count):** Aus/Aman-এ **%**, Boro-তে **count** (167, 125, 124)। Boro: 167/224 = 74.6%, 125/224 = 55.8%, 124/224 = 55.4%; "18%" ⇒ ≈ 40 unions (0.18 × 224 = 40.3)। Aus: 78 union ⇒ 51% ≈ 39.8 (≈ 40), 42% ≈ 32.8, 41% ≈ 32.0, 30% ≈ 23.4। (calc: `work/worked_examples.out`)। একই বিবৃতি-শৈলীতে লেখা উচিত।
  3. **"positive contribution in X% of unions" মানে কী?** Breakdown-এ প্রতিটি contribution = (feature মান জানায় prediction কতটা গড় থেকে সরে)। কোনো union-এ N-rate-এর contribution **positive** মানে ওই union-এর N-rate model-এর হিসাবে গড়ের চেয়ে "yield-বাড়ানোর পক্ষে"। যেহেতু N ও yield positive-related, এটা প্রায় **"ওই union-এর N-rate গড়ের উপরে"** ধরনের তথ্য। মানে এই % ও map **feature-মানের পার্থক্য** দেখায়, "N-rate-এর **প্রভাবের** স্থানিক পার্থক্য (effect heterogeneity)" নয়। (সবচেয়ে বড় concept; MSc lesson।)
  4. **আমাদের naive proxy check (`work/scripts/check_breakdown_proxy.py`, breakdown reproduction নয়):** union-গড় feature > সব-row গড় — এমন union-এর শতাংশ: N-rate Aus 50.0% (paper 51%), Aman 50.8% (paper 57%), Boro 50.4% (paper 74.6%); crop type: Aman-এ local-share সর্বোচ্চ গড়ের কম এমন union **73.6%** (paper ">70%" ✓), Boro-তে hybrid-share-গড়ের উপরে **25.9%** / hybrid-majority **11.6%** (paper 18% — মাঝামাঝি), Aus 59.0% (paper 51%)। অর্থাৎ crop type-এর "স্থানিক pattern" মূলত **জাতের বণ্টনের map**; N-র ক্ষেত্রে Aus/Aman প্রায় মেলে, Boro-তে মেলে না। (Confidence: মাঝারি/সূচনামূলক।)
  5. **Boro crop type শুধু ১৮% positive:** Boro-য় local নেই (শুধু HYV/hybrid; hybrid 14.4%)। তাই "crop type negative in 82% unions" = HYV-heavy unions; paper-এ এর ব্যাখ্যা নেই ("কম positive" ≠ "কম গুরুত্ব")।
  6. Map শুধু **union-average** — union-এর ভেতরে row-গুলোর বণ্টন, uncertainty (SD/n) নেই; 1-row-এর union আর 207-row-এর union একই ওজনে।
  7. **কোন model/data:** local XAI = ভিন্ন saved model + `*_union_data_all.csv` (p5, 5.5–5.6); **Fig. 8 ≠ Table 4/Fig. 6–7-এর model**।
  8. **Interpretation overreach:** Abstract "spatial variations in average effects" — আসলে "union-average local attribution"; Rule 5: spatial map ≠ spatial transferability।

### B4. §3.6 শুরু (লাইন ৫৮–৬৯)
- **কী বলছে:** GHG আর চারটি feature (N, P, K rate, FD)-এর local correlation (Fig. 9); global correlation "moderate to strongly positive across three seasons (Table S5)"।
- **খেয়াল (Seed F5 — আমাদের যাচাই):** S5 (GWP কলাম): Aus N 0.816, P 0.545, K 0.483, FD 0.309; **Aman N 0.201, P 0.108, K 0.223, FD 0.277**; Boro N 0.593, P 0.343, K 0.427, FD 0.058। yield~GWP: Aus 0.559, Aman **0.061**, Boro 0.226।
  - "moderate to strongly positive across three seasons" — Aus ✓ (N 0.816 strong), Boro N 0.593 moderate; **Aman সব ≤ 0.277 = weak**। তাই বাক্যটা Aman-এর জন্য অতিরঞ্জিত। **Confirmed issue**।
  - **Section 3.6-এর FD-claim ভুল:** পরের page-এ (p9) "Aus season shows only a weak connection between field duration and emissions" — S5: **Aus FD 0.309** (সবচেয়ে বেশি), Aman 0.277, **Boro 0.058** (সবচেয়ে কম)। সুতরাং Section 3.6 ভুল (Aus নয়, Boro-ই weak); Discussion (p11) ঠিক ("only a weak correlation in the Boro season")। **Confirmed** (Seed F5 অংশ verified); p9 দেখুন।

## C. নতুন শব্দগুলো

#### Additive model
- **সহজ মানে:** model যেখানে feature-এর প্রভাবগুলো যোগ হয়, একটা অন্যটার উপর নির্ভর করে না: f(x) = f₁(x₁) + f₂(x₂) + …।
- **ছোট উদাহরণ:** yield = 2000 + 8·N + 300·(HYV) → N বাড়ালে সবসময় +8, জাত-নির্বিশেষে। Non-additive: HYV-তে +10, local-এ +4 — **interaction**।
- **এই paper-এ:** "stack-ensemble is additive" claim।
- **খেয়াল:** PD ≈ AL additivity-র প্রমাণ নয়; H-statistic লাগে।

#### Interaction / H-statistic
- **সহজ মানে:** দুই feature একসাথে যে বাড়তি প্রভাব ফেলে যা আলাদা প্রভাবের যোগফল নয়।
- **সূত্র (সংক্ষেপে):** H²_j = (j-এর অংশবিশেষ-নির্ভর variance যা শুধু j-এর main effect ব্যাখ্যা করে না)/ (পুরো variance); 0 = interaction নেই, 1 = পুরোটাই interaction।
- **এই paper-এ:** `iml::Interaction` চালানো, ফল report নেই।
- **খেয়াল:** H-statistic ব্যয়বহুল ও correlated feature-এ বিভ্রান্তিকর হতে পারে।

#### Local attribution / contribution
- **সহজ মানে:** একটি specific row-এর prediction-এ কোন feature কতটা যোগ/বিয়োগ করল।
- **ছোট উদাহরণ:** গড় 3105 + N 250 + crop 120 + FD (−40) + P 60 + K 30 + বাকি 15 = 3540 (পরিমাণ বোঝানোর কাল্পনিক উদাহরণ)।
- **এই paper-এ:** break_down → union-গড়।
- **খেয়াল:** attribution = model-এর আচরণ; এটা "feature-মানের পার্থক্য" ও "প্রভাবের পার্থক্য" মেশায়।

#### Non-stationarity (স্থানিক)
- **সহজ মানে:** একই সম্পর্ক (যেমন N→GHG) জায়গাভেদে আলাদা।
- **খেয়াল:** বাস্তব non-stationarity বনাম sample-কম থেকে আসা noise আলাদা করতে test দরকার।

## D. Equation / statistics
- কোনো numbered equation নেই। PDP, ALE, break-down সূত্র + সংখ্যার উদাহরণ p5-এ।
- **Percent→count (calc):** Aus 78 × 0.51 = 39.8 ≈ 40 ইত্যাদি (উপরে)।

## E. Figures

**Fig. 7 — Marginal effects (PD, ALE) of N-rate, P-rate, K-rate, field duration, crop type for Aus (a–e), Aman (f–j), Boro (k–o)**
- **Axes:** x = feature (kg/ha; দিন; categorical); y = "Expected yield response (kg/ha)" ("Respone" typo)। **Legend:** নীল = Partial Dependence (PD), কমলা = Accumulated-local (AL)। y-অক্ষের range season-ভেদে আলাদা (Aus ~2000–4000; Aman ~2000–4500; Boro ~4500–6500)।
- **প্যাটার্ন (আনুমানিক):** N-rate: দ্রুত বাড়ে ~100–150 kg/ha পর্যন্ত, তারপর প্রায় সমতল (saturating); Aus N: ~2300 → ~3400 (≈ +1100 kg/ha); P ও K: ছোট ধনাত্মক ঢাল ও সমতলতা; Boro K (m) ~120-এ PD বনাম AL ভাগ হয়ে যায়। Field duration (d, i, n): সমতল বা হালকা নিম্নমুখী। Crop type (e, j, o): Aus/Aman-এ hybrid, HYV > local; Boro-তে PD ও AL-এর মধ্যে বড় ফারাক।
- **Authors' interpretation:** non-linear positive fertilizer response; FD negligible; stack additive।
- **Support?** (১) positive ও saturating N-response — হ্যাঁ, agronomic ভাবে বিশ্বাসযোগ্য (কিন্তু কার্যকারণ নয়; N-rate অন্য management-এর সাথে correlated); (২) FD negligible — PDP/ALE-তে হ্যাঁ, PFI-র সাথে বিরোধ; (৩) additivity — না (B2)।
- **Visual/methodological সমস্যা:** (১) রেখা-রেখে uncertainty band নেই; (২) rug/density plot নেই (data-sparse অঞ্চল বোঝা যায় না); (৩) PD/AL train-data-য়; (৪) y-range আলাদা ⇒ cross-season তুলনা কঠিন; (৫) subpanel-এর label ছোট ও (e) থেকে (o)-তে legend নেই; (৬) text-ref ভুল (B1); (৭) crop-type panel-এ bar দুটো রঙ legend ছাড়া।

(Fig. 8, Fig. 9 → p9, p10-এ বিশ্লেষণ।)

## F. Tables
এই পেজে নেই। **SI cross-check:** S5 (B4-এ); S7–S9 PFI (p7)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 8.1 | Fig. reference ভুল: "Fig. 6 shows PDP/AL"(→Fig. 7), "Figs. 6b, 6h"(→7b, 7h), "leftmost panel"(→rightmost), "P-rate (Fig. 7g)"(→Fig. 8g) | p8 §3.4–3.5; Fig. 6/7/8 | Confirmed issue |
| 8.2 | "AL = blue lines" ভুল; legend: PD নীল, AL কমলা | p8 §3.4 ¶২; Fig. 7a legend | Confirmed issue |
| 8.3 | "Additive" claim শুধু PD≈AL-এর ভিত্তিতে; `iml::Interaction` চালিয়ে `Feature_Interaction.csv` লিখলেও কোথাও report নেই | p8 §3.4; `yield_aus_autoML.Rmd:1066-1076`; Aman:1089; Boro:1093 | Confirmed issue |
| 8.4 | "All five features parallel" — Fig. 7(o) Boro crop type-এ PD vs AL ৩৫০–৫০০ kg/ha ফারাক (আনুমানিক) | Fig. 7(o) | Confirmed issue |
| 8.5 | Field duration: PFI 61–70% বনাম PDP/ALE flat — লেখকরা উল্লেখ করেন, ব্যাখ্যা করেন না | p7; p8; Fig. 7d,i,n | Unresolved question |
| 8.6 | PDP/ALE train data-য়; sparse high-N অংশ অনির্ভরযোগ্য; uncertainty/rug নেই | `Rmd:1016-1054`; Fig. 7 | Potential concern |
| 8.7 | §3.5: Aus/Aman % বনাম Boro count (167/125/124) — শৈলী মেলে না (167/224 = 74.6%) | p8 §3.5 | Confirmed issue (reporting) |
| 8.8 | "Positive contribution in X% of unions" ≈ feature-মান গড়ের উপরে কি না; effect heterogeneity নয় — আমাদের proxy: Aman crop type 73.6% ≈ ">70%" | `work/check_breakdown_proxy.out` | Potential concern |
| 8.9 | Union-average-এ union-প্রতি n/uncertainty নেই (n = 1–207) | Fig. 8; CSV | Potential concern |
| 8.10 | **F5:** S5 Aman GWP~N/P/K/FD = 0.201/0.108/0.223/0.277 (weak) বনাম "moderate to strongly positive across three seasons" | p8 §3.6; SI S5; আমাদের recompute `work/check07b.out` | Confirmed issue |
| 8.11 | Fig. 7 y-label "Respone" typo; Fig. 7 e/j/o legend নেই | Fig. 7 | Confirmed issue (minor) |
| 8.12 | Abstract "spatial variations in average effects" বনাম আসলে union-average local attribution | p1; p8 | Potential concern |

**লেখকদের পক্ষে:** PDP-র সীমা বুঝে ALE-ও দিয়েছেন; field duration-এর flat PDP-র কথা লুকাননি; local contribution-কে union-গড়ে map করে সারা দেশ-এর ছবি আনার চেষ্টা সৃজনশীল (GW regression-এর বিকল্প)।

**Reviewer-এর প্রশ্ন:** H-statistic-এর ফল কী? Boro crop-type PD vs AL-এর ফারাক কেন? Attribution-map কি শুধু জাতের map? Test-data-য় PD/ALE?

## H. সারাংশ
- **Short summary:** PD/AL N, P, K ধনাত্মক ও saturating; FD flat; stack-কে "additive" বলা অপ্রমাণিত; breakdown union-গড় map; F5 verify।
- **৫ key terms:** Additive, Interaction/H-statistic, Local attribution, Non-stationarity, PD vs AL।
- **Takeaways:** (১) অন্তত ৪টা figure-ref ভুল; (২) additivity অপ্রমাণিত, H-statistic লুকানো; (৩) "% unions positive" feature-মান-নির্ভর; (৪) S5 Aman দুর্বল।
- **Key numbers:** Aus 51/42/41/30/51%; Aman 57/53/37/50% (+crop >70%); Boro 167/125/124 + crop 18%; S5 Aman 0.201/0.108/0.223/0.277।
- **পরের পেজ-প্রশ্ন:** Fig. 8 কী দেখায়? Discussion-এ stacking "১–৪%" মেলে?

## Master Notes
- **Paragraph-wise:** PD/AL results; additivity argument; breakdown; §3.6 intro।
- **Exact numbers:** (H)।
- **Claims & evidence:** additive → PD≈AL (অপর্যাপ্ত); positive contribution % → feature-value-ই।
- **Open checks:** `Feature_Interaction.csv` (output নেই repo-তে — Rmd execution লাগবে); test-data PDP।
- **MSc notes:** SHAP + interaction; effect heterogeneity vs feature-value — একই feature-মানে "contribution" তুলনা (ICE/CATE-ধাঁচ); uncertainty band; rug plot।
