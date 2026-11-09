# Page 13 — CRediT (শেষ), Ethics, Declarations, Acknowledgment, Data availability, References (A–Chakraborty)

← [page-12](page-12.md) | [page-14](page-14.md) →

## A. এই পেজে কী আছে
- CRediT-এর শেষ অংশ, **Ethical statement**, **Declaration of competing interest**, **Acknowledgment**, **Appendix A (Supplementary data link)**, **Data availability**, তারপর **References** শুরু (Ahmed 2021 … Chakraborty 2025)।
- Main message: নৈতিকতা, তহবিল, data/code availability — "কেন বিশ্বাস করা যায়" অংশ।
- Research-এর অংশ: back-matter। (কোনো নতুন ফল নেই।)
- Reference list (p13–p16) প্রায় ১৬০টি entry (regex অনুমান; `work/scripts` ও `work/refs.txt`)।

## B. Paragraph ধরে ধরে ব্যাখ্যা

### B1. CRediT (লাইন ১–১০)
- **কী বলছে:** Fahmida Khanam, Jagadish Timsina, Timothy Krupnik-এর ভূমিকা (writing, methodology, data curation, supervision, funding…)।
- **খেয়াল:** তথ্যমূলক; যাচাইযোগ্য কিছু নেই। (Data curation Md. K. Hossain ও F. Khanam-এর — BIHS/CCAFS-MOT কে হিসাব করেছেন, অজানা।)

### B2. Ethical statement (লাইন ১১–৩৯)
- **কী বলছে:** CIMMYT/CGIAR/Ecological Informatics-এর নৈতিক মান মেনে; (১) "**This study used machine learning techniques to analyze agricultural data for predicting wheat yield in Bangladesh.** IRB লাগেনি, কারণ human/animal subject নেই"; (২) data "publicly available datasets or provided by CIMMYT and partners with permission"; (৩) authorship; (৪) তহবিল CIMMYT, Bangladesh ও CGIAR; (৫) COPE।
- **খেয়াল:**
  1. **"predicting wheat yield" — ভুল ফসল।** এই paper ধান (Aus/Aman/Boro) নিয়ে। সম্ভবত অন্য (গম) paper-এর template থেকে কপি (Ahmed 2025 wheat paper আছে)। **Confirmed issue** (Seed verified)।
  2. "**No human subjects**" — data আসলে household survey (BIHS); secondary/public data বলে IRB লাগেনি — যুক্তিসঙ্গত। তবে "no human subjects" বাক্যটা কিছুটা বিভ্রান্তিকর; BIHS নিজে IFPRI-র ethical clearance নিয়েছিল কি না, উল্লেখ নেই (Not reported…)।
  3. "provided by CIMMYT and partners with permission" — কোন data (soil SRDI? CCAFS-MOT outputs?) non-public তা বলা নেই।
  4. তহবিল বিবরণ: Ethical statement বলে "CIMMYT, Bangladesh, and the CGIAR Research Program"; Acknowledgment বলে CCAFS, CSRD/USAID, BMGF/CSISA — তালিকা ভিন্ন (আংশিক overlap)। ছোট অসঙ্গতি।

### B3. Declaration of competing interest (লাইন ৪০–৫৩)
- **কী বলছে:** সব লেখক "no conflicts"; তহবিলদাতা design/analysis-এ role রাখেনি।
- **খেয়াল:** নামের বানান ভুল: "Dr, Tek B. **Spkota**" (→ Sapkota), "Md. Khaled **Hosssin**" (→ Hossain)। proofreading। ছোট কিন্তু বিশ্বাসযোগ্যতায় প্রভাব ফেলে।

### B4. Acknowledgment ও Appendix (লাইন ৫৪–৭৫)
- **কী বলছে:** CIMMYT, University at Buffalo; CCAFS, CSRD, USAID, BMGF, CSISA-এর সহায়তা। Supplementary data: DOI লিংক।
- **খেয়াল:** তথ্যমূলক; Acknowledgment-এ "CSISA" কিন্তু main text-এ BIHS (IFPRI) ছাড়া অন্য data-প্রকল্প উল্লেখিত নয়।

### B5. Data availability (লাইন ৭৬–৮০)
- **কী বলছে:** "The code of all workflows and data used in this study is available on GitHub at https://github.com/zia207/AutoML-and-Explainable-AI-XAI-…"
- **আমাদের যাচাই (repo inventory, `work/code-inventory.md`):** Repo-তে আছে: তিনটি `*_data_all.csv` (13,150 row), 8টি Rmd + HTML, README। **নেই:** `train_data.csv`, `test_data.csv`, split code; `*_union_data_all.csv`; GW shapefiles; saved H2O models; CCAFS-MOT code/output (CH₄/N₂O/CO₂ আলাদা); NDVI/weather/kriging processing code; Aus/Boro GW code; GHG-PFI (Fig. S7) code। তাই "code of **all** workflows and data" — অতিরঞ্জিত। **Confirmed issue**। (সূত্র: p5 §2.3.3-এর অনুরূপ দাবি — 5.8।)
- Raw BIHS: Harvard Dataverse DOI 10.7910/DVN/BXSYEL (p14 refs) — অংশত সার্বজনীন। কিন্তু `Index` ↔ BIHS household/plot id-র mapping নথিভুক্ত নয় (Not reported…)।

### B6. References শুরু (A → Chakraborty)
- **কী পরীক্ষা করেছি (title quote):**
  - Ahmed, Z.U., Sun, K., Shelly, M., et al., 2021 — *"Explainable artificial intelligence (XAI) for exploring spatial variability of lung and bronchus cancer (LBC) mortality rates in the contiguous USA"* (Sci. Rep. 11, 24090) — text-এ "Ahmed 2021a" ও "2021b" দুটোই; entry একটি ⇒ 2.2/13.1।
  - Ahmed 2024 (maize, Artif. Intell. Agric. 13), Ahmed 2025 (wheat, Smart Agric. Technol. 10, 101693) — Discussion-এ উল্লেখিত ✓।
  - Aiello 2016 — *"Machine Learning with R, H2O"* ✓ (AutoML-এর সূত্র); Apley & Zhu 2020 — ALE ✓।
  - Banger 2012 — *"Do nitrogen fertilizers stimulate or inhibit methane emissions from rice fields?"* — p10 ¶-এ N→CH₄ প্রসঙ্গে ✓ মেলে।
  - Biecek 2018 (DALEX) ✓; Biecek & Burzykowski 2021 ✓; Brunsdon 2002 (GW) ✓।
  - Cai 2019, Chakraborty 2025 (*Global insights into nitrogen losses and efficiency in rice, wheat, and maize*) ✓ প্রসঙ্গ মেলে।
- **Reference-list বনাম in-text মিল:** R Core Team — text-এ "R Core Team, 2021a", "R Core Team, 2021b", "R-core-Team, 2020", "(Team, 2021)"; list-এ একটি "R Core Team, 2021"। **Confirmed issue** (ছোট)। অন্য অনেক in-text citation heuristic-এ "missing" দেখা গেলেও manual grep-এ পাওয়া গেছে (Cai, Lauritsen, Ledell, Kunhikrishnan, Flint, Liimatainen ইত্যাদি) — তাই regex-এর ফল আমরা claim করছি না।
- Formatting অসামঞ্জস্য: "Fisher, Aaron, Cynthia Rudin, Francesca, Dominici, 2019" ও "Gollini, Isabella, Binbin Lu, …" — নামের ফরম্যাট ভিন্ন।

## C. নতুন শব্দগুলো

#### DOI (Digital Object Identifier)
- **সহজ মানে:** একটা paper/dataset-এর স্থায়ী ইন্টারনেট ঠিকানা (যেমন 10.1016/j.ecoinf.2026.103885)।
- **এই paper-এ:** reference list-এ ~105টি DOI (regex গণনা); BIHS Dataverse DOI 10.7910/DVN/BXSYEL।
- **খেয়াল:** DOI দিয়ে title মিলিয়ে দেখলে citation-mismatch ধরা যায় (আমরা title দিয়ে করেছি)।

#### Citation–claim mismatch
- **সহজ মানে:** text-এ যে কথা বলা, সেই cited paper-এ আসলে সেই কথা নেই।
- **ছোট উদাহরণ:** "stacking ভালো (Wang 2018c)" কিন্তু Wang 2018c = insect pest image segmentation।
- **খেয়াল:** মনে রাখুন — mismatch বলার আগে title দেখা; abstract না পড়লে "প্রমাণ নেই" না বলে "title মেলে না" বলুন।

#### Data/Code availability statement
- **সহজ মানে:** paper-এ লিখে জানানো কোথায় data ও code পাওয়া যাবে।
- **খেয়াল:** "available" মানে "reproducible" নয় — split, saved model, seed, environment লাগে।

## D. Equation / statistics
এই পেজে নেই।

## E. Figures
এই পেজে নেই।

## F. Tables
এই পেজে নেই।

## G. Critical পর্যবেক্ষণ

| # (page.n) | কী পেলাম | প্রমাণ | ধরন |
|---|---|---|---|
| 13.1 | Ethical statement: "predicting **wheat** yield in Bangladesh" — paper ধান নিয়ে | p13 Ethical statement | Confirmed issue |
| 13.2 | Data availability: "code of all workflows and data" — train/test CSV, split code, union CSV, shapefile, models, CCAFS-MOT, processing code, Aus/Boro GW, Fig. S7 code নেই | p13; `work/code-inventory.md` | Confirmed issue |
| 13.3 | লেখকের নামে typo: "Spkota", "Hosssin" | p13 Declaration | Confirmed issue (minor) |
| 13.4 | তহবিল-বিবরণ ভিন্ন (Ethics: CIMMYT/CGIAR; Ack: + USAID, BMGF, CSISA) | p13 | Potential concern (minor) |
| 13.5 | "No human subjects" — household-survey data; BIHS-এর ethics clearance উল্লেখ নেই | p13 | Potential concern |
| 13.6 | "provided by CIMMYT and partners with permission" — কোন data non-public তা বলা নেই | p13 | Unresolved question |
| 13.7 | R Core Team 2020/2021a/2021b/Team 2021 in-text, list-এ একটি | p13–p16 refs; p3–p5 | Confirmed issue (minor) |
| 13.8 | Reference-name formatting অসামঞ্জস্য (Fisher, Gollini) | refs p15 | Confirmed issue (minor) |

**লেখকদের পক্ষে:** Code ও data GitHub-এ প্রকাশ — অনেক paper-এর চেয়ে ভালো অনুশীলন; BIHS Dataverse DOI দেওয়া; competing-interest ও COPE statement স্পষ্ট।

**Reviewer-এর প্রশ্ন:** Ethics statement কি অন্য paper-এর template? Data availability-তে কী কী বাদ? BIHS-এর unit-id mapping কোথায়?

## H. সারাংশ
- **Short summary:** Ethics/Declaration/Data availability-তে কয়েকটা ছোট-বড় ভুল (wheat, নামের বানান, "all code and data")।
- **৫ key terms:** DOI, Citation–claim mismatch, Data availability, IRB, CRediT।
- **Takeaways:** (১) "wheat" ভুল; (২) "all code and data" অতিরঞ্জিত; (৩) R Core Team in-text মিল নেই।
- **Key numbers:** ~160 refs (অনুমান); ~105 DOI; BIHS DOI 10.7910/DVN/BXSYEL।
- **পরের পেজ-প্রশ্ন:** p14 refs-এ আর কোন citation মিলছে না (Chen 2011, D'Orazio, IPCC 2019)?

## Master Notes
- **Paragraph-wise:** CRediT; ethics; declaration; acknowledgment; data availability; refs A–C।
- **Exact numbers:** (H)।
- **Claims & evidence:** "all code and data available" ✗।
- **Open checks:** BIHS ethics; non-public data।
- **MSc notes:** নিজের thesis-এ ethics/data statement-এ ফসল/অঞ্চল ঠিক লিখুন; data+code+split+seed একসাথে release করুন।
