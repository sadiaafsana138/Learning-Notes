# Page 03 — Weather, Soil, DEM, GHG (CCAFS-MOT), Fig. 1, Table 1

← [page-02](page-02.md) | [page-04](page-04.md) →

## A. এই পেজে কী আছে
- §2.1.2.1 NDVI processing-এর শেষ অংশ, **§2.1.2.2 Weather (ERA-Interim)**, **§2.1.2.3 National soil database (kriging)**, **§2.1.2.4 DEM**, **§2.2 GHG emissions (CCAFS-MOT)**, **Fig. 1** (survey location map), **Table 1** (data sources + original resolution)।
- Main message: predictor-গুলো কোথা থেকে এল আর GHG কীভাবে "হিসাব" করা হলো।
- Research-এর অংশ: Methods — data preparation আর GHG।
- আগের পেজে BIHS + 250 m grid; পরের পেজে (p4) ML pipeline।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. §2.1.2.1 NDVI শেষ অংশ (লাইন ১–৭)
- **কী বলছে:** MODIS HDF → GeoTIFF mosaic `MODIStsp` (R) দিয়ে; extraction/re-projection/clipping/resampling ArcPython দিয়ে; সব raster 250 m grid-এ।
- **কঠিন শব্দ:** *HDF* = satellite data-র ফাইল ফরম্যাট; *mosaic* = অনেক tile জোড়া লাগানো; *re-projection* = coordinate system বদলানো।
- **খেয়াল:** Cloud masking / quality flag (MOD13Q1 pixel reliability) ব্যবহার হয়েছে কিনা — "Not reported in the provided paper, Supporting Information, or available code."। বাংলাদেশে বর্ষায় মেঘ বেশি, তাই এটা গুরুত্বপূর্ণ।

### B2. §2.1.2.2 Weather data (লাইন ৮–২০)
- **কী বলছে:** ERA-Interim reanalysis (ECMWF); 12 km grid, hourly → daily total rainfall + mean/min/max temp, 2014–2015; **MOD13Q1-এর 16-day reporting date অনুযায়ী** (Table S3) প্রতিটা interval-এর average; তারপর 250 m grid-এ **Thin Plate Spline** (`fields` package)।
- **বোঝাতে চান:** NDVI-এর সময়ের সাথে weather মেলানো।
- **খেয়াল:**
  1. **Dataset-এর নামে মিল:** ERA-Interim-কে ২০১৯ সালে ECMWF অবসর দিয়েছে (ERA5 এসেছে) — এই paper 2014–15 data ব্যবহার করছে বলে সমস্যা নয়, কিন্তু আমরা এটা যাচাই করিনি (**Unresolved**)।
  2. **Table 1-এ ERA-Interim-এর URL = `lpdaac.usgs.gov/get_data`** — এটা NASA LP DAAC (MODIS data)-র লিংক, ECMWF-এর নয়। **Confirmed issue** (সামান্য, reporting)।
  3. 12 km → 250 m: (12000/250)² = **2304** গুণ pixel; smoothing দিয়ে তৈরি, নতুন তথ্য নয় (code: `work/worked_examples.out`)।
  4. Text বলছে mean/min/max temperature তৈরি হয়েছে; কিন্তু model-এ শুধু `t2m_*` (একটা temperature) আর `tp_*` (rainfall) আছে (CSV column list); min/max temp কোথায় গেল? "Not reported…"। (`exTZONE` একটা আলাদা categorical, যা "extreme temperature zone")।
  5. Time-window: "16-day interval average" — কিন্তু `t2m_209` (Aman, Rmd) বনাম `NDVI_205` (CSV) — **column-নামে অমিল** (SI S3-তে Aman-এর তারিখ 209)। Code evidence: `yield_aman_autoML.Rmd` feature list এ `NDVI_205` ও `t2m_209`। ছোট কিন্তু typo/তারিখ-অমিল সম্ভাবনা; **Potential concern**।

### B3. §2.1.2.3 National soil database (লাইন ২১–২৯)
- **কী বলছে:** SRDI-র 50,000 point, topsoil 0–20 cm, 430 sub-district; **31,787 point** দিয়ে pH, SOC, N, P, K, S, B, Zn-এর 250 m raster; **Multi-Gaussian Kriging** (`gstat`)।
- **খেয়াল:**
  1. 50,000 → 31,787 (63.6%) কেন? বাদ দেওয়ার criterion: "Not reported…"।
  2. **B (Boron) raster বানানো হয়েছে কিন্তু model-এ B নেই** (CSV/Rmd feature list: pH, SOC, N, P, K, S, Zn) — কেন বাদ? "Not reported…"।
  3. **Kriging uncertainty (kriging variance) propagate হয়নি** — soil value-কে ধ্রুব মান ধরা হয়েছে। Soil sample-এর সময় ১৯৯৬–২০১৪ (SRDI 1996–2014), আর p12 নিজেই বলে "old, may not reflect current"।
  4. "Soil variables derived from kriging didn't need extra imputation" (p4) — ঠিক; কিন্তু kriging-এর smoothing-এর কারণে variability কম → PFI-তে soil-এর গুরুত্ব বাস্তবের চেয়ে কম দেখাতে পারে (**suspected**)।

### B4. §2.1.2.4 Terrain (লাইন ৩০–৩৪)
- **কী বলছে:** SRTM 90 m DEM → 250 m।
- **খেয়াল:** DEM 90 m — অর্থাৎ NDVI (250 m) "সবচেয়ে সূক্ষ্ম" নয় (p2 claim-এর সাথে অমিল; আগে লেখা 2.8)।

### B5. §2.2 GHG emissions (লাইন ৩৫–৫৬)
- **কী বলছে:** CCAFS-MOT দিয়ে CH₄, N₂O, CO₂ হিসাব; input = soil (pH, texture, SOC), climate, water management, **fertilizer rates**, অন্যান্য practice। South Asian rice-এ আগে ব্যবহার (Sapkota 2021)। **সরাসরি মাপা হয়নি**, তাই modeled output — limitation স্বীকার করা।
- **লেখকরা বোঝাতে চান:** tool ধান-এর জন্য উপযুক্ত।
- **খেয়াল (সবচেয়ে গুরুত্বপূর্ণ — Seed F6):**
  1. **Circularity:** CCAFS-MOT-এর input-এ fertilizer rate আছে (লেখকদেরই বর্ণনা, এই paper p3)। তাই N/P/K rate আর Total GWP-এর correlation **কিছুটা formula-র ভেতরেই "বসানো"**। এটা p9–p10-এ (Fig. 9) আসল সমস্যা হবে। Evidence: p3 §2.2 + SI S5 (Aus N r = 0.816) + আমাদের recompute (Check 7)।
  2. **CCAFS-MOT-এর কোনো code/output নেই** repo-তে (Check: file inventory)। CH₄/N₂O/CO₂ আলাদা column-ও নেই; শুধু `Total_GWP` আর `Emission_Intensity` (CSV columns)। README বলে per-plot CH₄, N₂O, CO₂ আছে, কিন্তু আমরা যে CSV দেখলাম তাতে নেই → "Not reported in the provided paper, Supporting Information, or available code."
  3. **"Water management practices" input:** p12 বলে water data exclude করা হয়েছে; তাহলে CCAFS-MOT কোন water regime ধরল? Data-তে `Water_regime` = Aus সবই "Rainfed, wet season", Boro সবই "Continuous flooding" — সম্ভবত এই class-ই CCAFS-MOT-এ গেছে (**suspected**)। এর মানে Boro-র AWD/intermittent irrigation (p11-এ লেখকরাই বলেন Boro-তে AWD common) GHG হিসাবে ধরা হয়নি।
  4. "widely recognized for accuracy" (p12) — কোনো validation নেই; এই paper-এ nothing against measured flux।
  5. CCAFS-MOT output-কে "GHG emissions" হিসেবে ধরে ML/GWC চালালে আসলে tool-এর equation-এর সাথে data-র সম্পর্ক পরীক্ষা হচ্ছে।

## C. নতুন শব্দগুলো

#### Reanalysis (ERA-Interim)
- **সহজ মানে:** অতীতের weather observation আর model মিলিয়ে বানানো গ্রিডেড আবহাওয়া-ডাটা (বাস্তব মাপ নয়)।
- **উদাহরণ:** একটা 12 km × 12 km cell-এ একটাই তাপমাত্রা; ওই cell-এর ভেতরে ৫ km দূরে দুই গ্রামের তফাত দেখা যায় না।
- **এই paper-এ:** rainfall ও temperature, 2014–2015।
- **খেয়াল:** Reanalysis rainfall সাধারণত স্থানীয় বৃষ্টির peak কম দেখায়।

#### Thin Plate Spline (TPS)
- **সহজ মানে:** বিন্দুর মানের মধ্য দিয়ে একটা মসৃণ পৃষ্ঠ টানা — যেন পাতলা ধাতুর পাত বাঁকানো।
- **উদাহরণ:** 4টা weather cell-এর মাঝে একটা 250 m point-এর মান smooth interpolation-এ আসে।
- **এই paper-এ:** weather 12 km → 250 m, R `fields`।
- **খেয়াল:** Interpolation নতুন তথ্য আনে না।

#### Kriging / Multi-Gaussian Kriging
- **সহজ মানে:** কাছের নমুনা-বিন্দুগুলোর ওজনযুক্ত গড় দিয়ে অজানা জায়গার মান অনুমান; ওজন ঠিক হয় distance + spatial correlation (variogram) দিয়ে।
- **ছোট উদাহরণ (সরল IDW দিয়ে বোঝানো; kriging-এ ওজন variogram থেকে আসে):** ১ km দূরে pH 6.0, ৩ km দূরে pH 7.0 → ওজন 1 ও 1/3 → 0.75, 0.25 → অনুমান 0.75×6+0.25×7 = **6.25** (`work/worked_examples.out`)।
- **এই paper-এ:** SRDI 31,787 point → 250 m soil map (pH, SOC, N, P, K, S, B, Zn)।
- **খেয়াল:** (১) kriging smooth করে; (২) variance বাদ দিয়ে শুধু গড় ব্যবহার; (৩) পুরোনো sample।

#### MODIS NDVI (MOD13Q1)
- **সহজ মানে:** satellite দিয়ে গাছের "সবুজতা" মাপার সূচক; 16-day composite, 250 m।
- **উদাহরণ:** NDVI 0.2 = প্রায় খালি জমি/জল; 0.8 = ঘন সবুজ ধান।
- **এই paper-এ:** প্রতি season-এর 16-day সময়ে NDVI feature।
- **খেয়াল:** মেঘ, ছোট জমি (250 m pixel-এ মিশ্র ফসল), union-centroid-এ pixel।

#### DEM / SRTM
- **সহজ মানে:** ভূমির উচ্চতার map; SRTM 90 m।
- **খেয়াল:** বাংলাদেশের floodplain-এ উচ্চতা ১–১০ m-এর মধ্যে — ছোট পার্থক্যই বড় (বন্যা/drainage)।

#### CCAFS-MOT
- **সহজ মানে:** কৃষি-জমির GHG হিসাবের একটা tool/calculator (CGIAR); input দিলে emission estimate দেয়।
- **ছোট উদাহরণ:** N rate বেশি → N₂O emission factor ধরে বেশি N₂O (সরল ছবি; আসল সূত্র এই paper-এ নেই)।
- **এই paper-এ:** `Total_GWP` (kg CO₂e/ha) তৈরি।
- **খেয়াল:** Tool-এর input-ই যদি পরে "predictor" হিসেবে যায় → circular।

#### Global Warming Potential (GWP), CO₂e
- **সহজ মানে:** বিভিন্ন gas-কে CO₂-র সমান warming-এ রূপান্তর।
- **ছোট উদাহরণ (illustrative):** 10 kg CH₄ × 28 + 0.5 kg N₂O × 265 = **412.5 kg CO₂e** (AR5-style factor; এই paper কোন factor নিয়েছে তা Not reported…)।

## D. Equation / statistics
- কোনো numbered equation নেই। পদ্ধতি দুটো: **Thin Plate Spline** আর **Multi-Gaussian Kriging** — equation paper-এ দেওয়া নেই, তাই reproduce করার কিছু নেই।
- **কী মাপে/কেন:** দুটোই interpolation — কম sample থেকে পুরো ভূমির map।
- **ছোট সংখ্যার উদাহরণ:** C-section-এ (IDW intuition)।
- **ব্যাখ্যা কীভাবে:** map-এর মান "অনুমান", measurement নয়।
- **Assumptions/limits:** stationarity (spatial pattern সব জায়গায় এক রকম), যথেষ্ট ঘন sample; বাংলাদেশের দ্রুত বদলানো soil-এ প্রশ্নসাপেক্ষ; কোনো cross-validation error report করা হয়নি ("Not reported…")।

## E. Figures

**Fig. 1 — "District map of Bangladesh showing the location of BIHS Unions…"**
- Axes: lat/long frame (87°44′30″E–92°15′15″E; 21°18′30″N–25°49′15″N)। Legend: "Semi-structured farmer survey location" (কালো ত্রিভুজ ▲)। Background: elevation (grayscale; পূর্বের পাহাড়ি অঞ্চল গাঢ়), scale bar 0–120 km।
- Pattern: বিন্দু সারা দেশে ছড়ানো; দক্ষিণ উপকূল ও উত্তর-পশ্চিম অংশে অপেক্ষাকৃত কম; পার্বত্য চট্টগ্রামে প্রায় নেই।
- **Caption বনাম ছবি:** Caption বলছে "**Circular points** indicate sampling locations" কিন্তু legend-এ **triangle**; আর caption "District map" বলছে কিন্তু বিন্দু Union-centroid (text অনুযায়ী); এটা ছোট inconsistency (**Potential concern**)।
- Figure কি claim support করে? শুধু coverage দেখায়; কত unions (78/247/224) বা কত row প্রতিটায় — figure থেকে বোঝা যায় না।

## F. Tables

**Table 1 — Data used in this study**
| Category | Variable | Source | Original resolution |
|---|---|---|---|
| BIHS survey | farm size, crop type (**Boro/Aman/Boro**), variety, line sowing, fertilizer, organic matter, lime | IFPRI 2016, Harvard Dataverse | Plot/household |
| National soil | soil type, pH, SOC, N, P, K, S, Zn | SRDI (Shiragi 2017) | Point (50,000) |
| Terrain | DEM | SRTM | **90 m** |
| Remote sensing | MODIS NDVI | NASA LP DAAC | 250 m |
| Weather | Temp, rainfall | ERA-Interim (URL = lpdaac.usgs.gov) | ~12 km (0.125°) |
- **Odd:** (১) "crop type (Boro/Aman/Boro)" — Boro দুবার; হওয়া উচিত Aus/Aman/Boro (Seed typo — **verified**)। (২) ERA-Interim-এর link ভুল সাইটের। (৩) "Plot/household level" আসল location precision-এর কথা বলে না (Union centroid)। (৪) Table 1-এ GHG/CCAFS-MOT input নেই। (৫) তালিকায় `Water_regime`, drainage class, land type, temperature zone, manure-এর উৎস (সম্ভবত SRDI/BARC class) নেই।
- Cross-check: soil variables CSV-তে `pH, SOC, N, P, K, S, Zn` — **B নেই** (text: B আছে)।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 3.1 | CCAFS-MOT input-এ fertilizer rate → N/P/K–GWP correlation আংশিক circular | p3 §2.2; SI S5 (Aus N r=0.816); `work/check07b.out` | Confirmed issue |
| 3.2 | Table 1: "crop type (Boro/Aman/Boro)" — Aus বাদ | p3 Table 1 | Confirmed issue |
| 3.3 | Table 1-এ ERA-Interim source URL = lpdaac.usgs.gov (MODIS DAAC) | p3 Table 1 | Confirmed issue |
| 3.4 | Fig. 1 caption "circular points"/"district map" বনাম legend triangle/union | p3 Fig. 1 | Potential concern |
| 3.5 | Soil B raster তৈরি, model-এ B নেই; 31,787 কেন বাছা — অজানা | p3 §2.1.2.3; CSV/Rmd features | Unresolved question |
| 3.6 | Kriging uncertainty ও soil sampling-year (1996–2014) propagate হয়নি | p3 §2.1.2.3; p12 | Potential concern |
| 3.7 | Text-এ min/max temp তৈরি, model-এ একটা `t2m` | p3 §2.1.2.2; CSV | Unresolved question |
| 3.8 | CCAFS-MOT code/CH₄/N₂O/CO₂ আলাদা column নেই — "Not reported in the provided paper, Supporting Information, or available code." | file inventory (`work/code-inventory.md`) | Unresolved question |
| 3.9 | Aman: CSV `NDVI_205` বনাম `t2m_209`/SI S3 "209" | `yield_aman_autoML.Rmd` feature list; SI S3 | Potential concern |
| 3.10 | Boro-তে AWD/intermittent irrigation CCAFS-MOT-এ ধরা হয়েছে কিনা অজানা; `Water_regime` Boro-তে সব "Continuous flooding" | `boro_data_all.csv` (Check 5); p11 | Potential concern |
| 3.11 | Cloud/quality masking of NDVI report নেই | p3 | Unresolved question |

**লেখকদের পক্ষে:** CCAFS-MOT-কে modeled বলে স্পষ্ট স্বীকার; geostatistical ও remote sensing tool-গুলো (MODIStsp, gstat, GWmodel) উল্লেখ করা।

**Reviewer প্রশ্ন:** Kriging cross-validation error? CCAFS-MOT-এর কোন version/equation? Fertilizer rate-কে predictor ও GHG-input দুটোই রাখা কি circular নয়?

## H. সারাংশ
- **Summary:** Predictor-এর উৎস (NDVI, ERA-Interim, SRDI soil, SRTM) আর GHG (CCAFS-MOT, modeled)।
- **৫ key terms:** Reanalysis, TPS, Kriging, NDVI, CCAFS-MOT।
- **Takeaways:** (১) GHG modeled + fertilizer input → circular; (২) সব environmental layer interpolated/smoothed; (৩) documentation-এ ছোট ভুল (Table 1)।
- **Key numbers:** 50,000 soil points; 31,787 used; 430 sub-districts; 12 km; 250 m; 90 m; 0–20 cm; 2014–2015।
- **পরের পেজ-প্রশ্ন:** Train/test split কীভাবে? CV কীভাবে? hyperparameter কোথায় (S2/S3/S4)?

## Master Notes
- **Paragraph-wise:** NDVI wrap-up; Weather; Soil; DEM; GHG।
- **Exact numbers:** 50,000/31,787/430; 12 km/250 m/90 m; 0–20 cm।
- **Claims→evidence:** "CCAFS-MOT accurate" → no validation here; "250 m alignment preserves detail" → location is union centroid।
- **Open checks:** CCAFS-MOT equations/version; ERA-Interim vs actual rainfall; NDVI quality masks।
- **MSc notes:** (১) আপনার scope-এ satellite নেই — তাহলে এই "NDVI at union centroid" সমস্যা এড়ানো যায়; (২) GHG বাদ দিলে circularity-ও যায়; (৩) climate data-র জন্য station/ERA5/CHIRPS-এর resolution + district-aggregation স্পষ্ট লিখুন; (৪) agro-ecological zone (AEZ) variables-এর source আগেই ঠিক করুন।
