# Page 10 — Fig. 9 (GW correlation maps), Discussion: PFI বনাম Breakdown, N fertilizer ও GHG

← [page-09](page-09.md) | [page-11](page-11.md) →

## A. এই পেজে কী আছে
- **Fig. 9**: Total GHG-র সাথে N, P, K rate ও field duration-এর **local (geographically weighted) Pearson correlation** — Aus/Aman/Boro, ১২টি panel।
- Discussion-এর ¶৪–৫: PFI বনাম breakdown-এর ফল, **N fertilizer-এর গুরুত্ব**, urea-র ব্যবহার, N-use efficiency (NUE) ও GHG-র সম্পর্ক, deep placement।
- এই পেজে text খুব কম (দুই কলাম, শেষ বাক্য p11-এ চলে যায়); বেশিরভাগ জায়গা Fig. 9।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. ¶ "of local model-agnostic … showed spatial variation" (p9 থেকে চলমান, লাইন ১–১৮)
- **কী বলছে:** breakdown দেখিয়েছে feature contribution-এর স্থানিক ভিন্নতা। "Of these, the **N-fertilizer application rate was the most important factor in all seasons in many unions**, indicating its critical role in increasing rice yield in Bangladesh।"
- **লেখকরা বোঝাতে চান:** সব season-এ N-ই মূল চালক, তাই N management জরুরি।
- **খেয়াল রাখার মতো:**
  1. **নিজেদের ফলের সাথে মিল নেই:** Aman-এ PFI-র শীর্ষ **crop type** (S8: 328.57 > N-rate 317.36), আর p8 §3.5-এ লেখা "**In Aman, crop type (variety) was the most critical factor … positively contributing to more than 70% unions**"। অর্থাৎ Aman-এ N প্রথম নয়। Aus-এ N প্রথম (PFI + 51% unions), Boro-তে N প্রথম (PFI; 167 unions)। **"all seasons"** অতিসরলীকরণ। **Confirmed issue** (text বনাম text/S8)। (যদিও Aman-এ crop type ও N-এর PFI-gap z = 0.44 — পরিসংখ্যানগতভাবে আলাদা নয় (p7); তবে লেখকদের নিজেদের ভাষা সংগতিপূর্ণ হওয়া উচিত।)
  2. **"critical role in increasing rice yield" — causal:** PFI predictive importance; observational data; N-rate সম্ভবত অন্য management-এর proxy (সেচ, উন্নত জাত, আর্থিক সামর্থ্য)। Limitations-এ (p12) লেখকরাই এটা স্বীকার করেন।
  3. "In many unions" — কত? Aus 51% ও Aman 57% ≈ অর্ধেক, "many" ঢিলা।

### B2. ¶ N management ও GHG (লাইন ১৯–৩২; p11-তে চলে)
- **কী বলছে:** অদক্ষ N management (যেমন বন্যার জলে urea broadcast) বাংলাদেশে N-use efficiency খারাপ (Coggins 2025; Islam 2018, 2022), যা GHG বাড়ায় (Banger 2012)। বার্ষিক ~2.9 MT urea, 60% ধানে (BBS 2020), CH₄ ও N₂O বাড়ার ঝুঁকি (Islam 2022)। Precision N management ও NUE ধান-উৎপাদন বাড়াতে ও GHG কমাতে ভূমিকা রাখতে পারে (Sapkota 2014)। Broadcast থেকে sub-surface/deep placement-এ গেলে N-loss ও GHG কমে (Chakraborty 2025; Emran 2019; Gaihre 2015; Liu 2020 — p11-এ)।
- **সংখ্যা (গণনা):** 2.9 MT × 60% = **1.74 MT** urea ধানে (`work/worked_examples.out`)।
- **খেয়াল:**
  1. **এই সব সাহিত্য-ভিত্তিক, এই study-র ফল নয়।** Data-তে শুধু **rate** (kg/ha: `N_rate`, `Urea Amount`, `MP`, `TSP`, `DAP`) আছে; **placement, timing, split application, NUE** নেই। অর্থাৎ placement/deep-placement সুপারিশ study-র বিশ্লেষণ দিয়ে সমর্থিত নয় — literature-support মাত্র।
  2. **Gaihre 2015** আবার (N₂O/NO, urea deep placement — এখানে সঠিক প্রসঙ্গে! p1-এ CH₄ দাবিতে ভুল ছিল)। এখানে N₂O/deep-placement-এর সাথে মেলে — ✓।
  3. **Liu et al. 2020** = "Advantages of nitrogen fertilizer deep placement in GHG emissions … no-tillage paddy fields" (J. Clean. Prod.; চীন) — প্রসঙ্গ (deep placement) ঠিক; কোন দেশ/মাটিতে — আমরা যাচাই করিনি।
  4. "poor NUE → GHG বাড়ে" ঠিক সাধারণভাবে; কিন্তু **এই paper-এ NUE ও yield-scaled emission মাপা নেই** ⇒ "N rate কমালে yield ও GHG দুটোই ভালো" বলা যায় না (Seed F7)।
  5. **Circularity (F6):** N rate ↔ Total GWP correlation (Aus r = 0.816) CCAFS-MOT-এর input থেকে। তাই "N বাড়লে GHG বাড়ে" মডেল-নির্মিত।

## C. নতুন শব্দগুলো

#### Nitrogen-use efficiency (NUE)
- **সহজ মানে:** দেওয়া N-এর কত অংশ ধান আসলে নিল (বা প্রতি kg N-এ কত kg grain)।
- **ছোট উদাহরণ:** 100 kg N/ha দিলে 4000 kg yield, N ছাড়া 2500 ⇒ agronomic efficiency = (4000 − 2500)/100 = **15 kg grain/kg N**।
- **এই paper-এ:** শুধু Discussion-এ উল্লেখ; মাপা হয়নি।
- **খেয়াল:** NUE না মেপে "efficiency" নিয়ে সুপারিশ করা দুর্বল।

#### Urea broadcast / deep placement
- **সহজ মানে:** broadcast = জমিতে ছিটিয়ে দেওয়া (বন্যার জলে লোকসান বেশি); deep placement = ঢেলা (briquette) করে গাছের শিকড়ের কাছে মাটিতে গুঁজে দেওয়া।
- **খেয়াল:** এই data-তে এ তথ্য নেই।

#### N₂O ও CH₄ উৎস (সংক্ষেপে)
- **CH₄:** জলমগ্ন (anaerobic) জমিতে জৈবিক বিয়োজন থেকে; **N₂O:** nitrification/denitrification থেকে, N-সারের পরিমাণের সাথে বাড়ে। দুটোর পদ্ধতি আলাদা, তাই Total GWP একটাই সংখ্যায় দুই ভিন্ন প্রক্রিয়া মিশিয়ে দেয়।

#### Pearson correlation (local)
- **সূত্র:** r = Σ(xᵢ − x̄)(yᵢ − ȳ)/√(Σ(xᵢ − x̄)² Σ(yᵢ − ȳ)²); GW version-এ ওজনযুক্ত গড়/variance (bi-square)।
- **ছোট উদাহরণ:** x = [50,100,150,200], y = [900,1100,1250,1500] ⇒ **r = 0.995** (Python)।
- **এই paper-এ:** Total GWP vs N/P/K/GD; Aus global r (union-গড়) N = 0.816 ⇒ r² = **0.67** (variance-এর ~67%)।
- **খেয়াল:** r নির্দেশ করে সরলরেখীয় সম্পর্ক; r ≠ প্রভাব।

## D. Equation / statistics
- **Pearson r** (উপরে), **GW weights** (p5)। কোনো numbered equation নেই।
- **Interpret (Fig. 9):** r > 0.436 "moderate-strong" (লেখকদের cut); GW-র কোনো p-value/CI map নেই।
- **Assumptions/limits:** local sample (adaptive bandwidth) — HTML থেকে: Aman `_01` bandwidth = **144 nearest neighbours** (AICc 4175.355), `_02` = **69** (AICc 4152.714) (`gw_correlation_aman_01.html`, `_02.html`)। অর্থাৎ নির্বাচিত neighbourhood-এর আকার covariate-সেটের উপর নির্ভরশীল (Crop_Types সহ/ছাড়া) এবং Fig. 9-এর Aman map কোনটার (144 না 69) — paper বলেনি। (`bw.gwr` GWR regression-এর AICc দিয়ে; correlation-এর জন্য নয়।) Search-এর প্রথম ধাপ 160 — golden-section অনুপাত হিসাব করলে ~246–247 point (union-level) অনুমান করা যায় (**suspected**; shapefile নেই)।

## E. Figures

**Fig. 9 — Local Pearson correlation (r) between Total GHG and N-, P-, K-rate, field duration: Aus (left), Aman (middle), Boro (right)**
- **Layout:** ১২ panel; সারি = N, P, K, Field duration (a–c, d–f, g–i, j–l); কলাম = Aus, Aman, Boro। প্রতি সারিতে একটি **shared legend** (৫ শ্রেণি), তাই season-জুড়ে তুলনা সম্ভব (এটা ভালো)।
- **Legend (ছবি থেকে):** N: <0.144 | 0.145–0.435 | 0.436–0.581 | 0.582–0.617 | >0.618। P: <0.083 | 0.084–0.301 | 0.302–0.323 | 0.324–0.356 | >0.357। K: <0.189 | 0.190–0.399 | 0.400–0.408 | 0.409–0.441 | >0.442। FD: "**> 0.035**" | 0.036–0.080 | 0.081–0.217 | 0.218–0.306 | >0.307।
- **প্যাটার্ন (গুণগত):** N: Aus (a) মাঝারি-বড় বিন্দু; Aman (b) ছোট বিন্দু বেশিরভাগ (দুর্বল), দক্ষিণে কিছু বড়; Boro (c) ঘন ও বড় বিন্দু (শক্তিশালী) — text "particularly Boro" সমর্থিত। P: (e) Aman-এ দক্ষিণ-মধ্যে বড় বিন্দুর গুচ্ছ। K: (h) Aman-এ দক্ষিণে গুচ্ছ। FD: (k) Aman গাঢ়, (l) Boro ফ্যাকাশে/ছোট (**দুর্বল ✓ S5 0.058**), (j) Aus মাঝারি।
- **Authors' interpretation:** N-GHG শক্তিশালী (বিশেষত Boro), P/K দুর্বল ও বিচিত্র, FD Aman-এ ধনাত্মক।
- **Figure কি সমর্থন করে?** গুণগত প্যাটার্ন — হ্যাঁ। তবে:
  1. **Legend-এর প্রথম শ্রেণি FD-তে "> 0.035"** — হওয়া উচিত "< 0.035" (সর্বনিম্ন শ্রেণি)। **Confirmed issue** (typo; Seed verified)।
  2. N-র Aus global r = 0.816 (S5) বনাম Fig. 9-এ সর্বোচ্চ শ্রেণি শুধু ">0.618" (ঊর্ধ্বসীমা অজানা) — Aus-এর সব পয়েন্ট একই শ্রেণিতে? দেখা যায় না। Aus-এ global শক্তিশালী কিন্তু Fig. 9(a)-এ "particularly Boro" বলা — S5 অনুযায়ী Aus বেশি। দ্বন্দ্ব নয় (local ≠ global, n আলাদা) — কিন্তু ব্যাখ্যা দরকার। **Unresolved**।
  3. **পদ্ধতিগত:** union-গড় data; local r-এ significance/CI নেই; multiple-testing (শত শত local test); spatial autocorrelation।
  4. **Circularity:** N/P/K-rate ↔ CCAFS-MOT GHG (p3)।
  5. Map-এর বিন্দু = union (Aus-এ কম, Boro-তে বেশি) — বিন্দু-সংখ্যার পার্থক্য চোখে "শক্তি"-র ধারণা দেয়।

## F. Tables
এই পেজে নেই। **Cross-check:** S5 (global r) — N: Aus 0.816, Aman 0.201, Boro 0.593; P: 0.545/0.108/0.343; K: 0.483/0.223/0.427; FD: 0.309/0.277/0.058। আমাদের recompute: union-mean দিয়ে Aus/Boro **হুবহু**, Aman প্রায় (±0.03); row-level অনেক কম (`work/check07b.out`)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 10.1 | "N most important in all seasons" — Aman-এ PFI শীর্ষ crop type (S8) ও p8 নিজেই "crop type most critical in Aman" | p10 §4; p8 §3.5; SI S8 | Confirmed issue |
| 10.2 | "critical role in increasing rice yield" — causal ভাষা; PFI/attribution predictive | p10; p12 limitations | Potential concern |
| 10.3 | Fig. 9 FD legend "> 0.035" → হবে "< 0.035" | p10 Fig. 9(j–l) legend | Confirmed issue |
| 10.4 | Placement/deep-placement/NUE সুপারিশ data দিয়ে সমর্থিত নয় (data-তে শুধু rate) | p10–p11; CSV columns | Confirmed issue (claim ← evidence) |
| 10.5 | Fig. 9: significance/CI নেই; local sample ছোট; bandwidth: Aman `_01` = 144, `_02` = 69 neighbours — কোনটা Fig. 9-এ? | `gw_correlation_aman_01.html`, `_02.html` | Unresolved question |
| 10.6 | N/P/K–GHG correlation আংশিক circular (CCAFS-MOT input) | p3 §2.2; Fig. 9 | Confirmed issue (conceptual) / পরিমাণ: Unresolved |
| 10.7 | "Particularly Boro" (N) বনাম S5 global Aus 0.816 > Boro 0.593 — ব্যাখ্যা নেই | Fig. 9; SI S5 | Unresolved question |
| 10.8 | NUE/yield-scaled emission বিশ্লেষণে নেই | p10 Discussion | Potential concern |
| 10.9 | Gaihre 2015 এখানে সঠিক প্রসঙ্গে (N₂O, deep placement); p1-এ ভুল ছিল | p10; p1 | (লেখকদের পক্ষে) |
| 10.10 | Aman GW code দুই version (`_01`, `_02`) ও ভিন্ন bandwidth; কোনটা প্রকাশিত অজানা | `gw_correlation_aman_01/02.Rmd` | Unresolved question |

**লেখকদের পক্ষে:** Fig. 9-এ shared legend (season-তুলনা সম্ভব); GW correlation দুটো Rmd-তে প্রকাশ; literature-সংযোগ ভালো (Sapkota 2021 mitigation estimates) — বাংলাদেশের নীতি-প্রসঙ্গের সাথে প্রাসঙ্গিক।

**Reviewer-এর প্রশ্ন:** Fig. 9 কোন bandwidth/shapefile থেকে? Local correlation-এর significance? N-GHG-র circularity কতটা?

## H. সারাংশ
- **Short summary:** Fig. 9 local correlation maps; Discussion N-কে সব season-এ প্রধান বলছে (Aman-এ নিজের ফলের সাথে অমিল) ও literature-ভিত্তিক N management।
- **৫ key terms:** NUE, Urea broadcast/deep placement, CH₄ vs N₂O, Pearson r (GW), Shared legend।
- **Takeaways:** (১) "N all seasons" ভুল; (২) FD legend typo; (৩) placement/NUE claim data-বহির্ভূত; (৪) bandwidth অস্পষ্ট।
- **Key numbers:** 2.9 MT urea; 60% (≈ 1.74 MT); r > 0.436; bandwidth 144/69; S5 N: 0.816/0.201/0.593।
- **পরের পেজ-প্রশ্ন:** P ও K GHG-র সাথে "moderate-strong" — S5 বলে? Aus FD মন্তব্য আবার?

## Master Notes
- **Paragraph-wise:** breakdown বনাম PFI; N management/NUE/urea।
- **Exact numbers:** (H)।
- **Claims & evidence:** "N প্রধান সব season-এ" ✗ (Aman); "deep placement" literature-only।
- **Open checks:** Fig. 9-এর bandwidth; S5 vs shapefile n।
- **MSc notes:** GHG/N circularity এড়াতে measured data বা না-রাখা; local correlation-এ significance map।
