# Paper Critic — Ahmed et al. (2026): AutoML + XAI for rice yield & GHG in Bangladesh

**Paper:** "AutoML and explainable AI (XAI) for rice production systems: Unraveling yield predictors and greenhouse gas emissions in Bangladesh" — Ecological Informatics 97, 103885 · DOI https://doi.org/10.1016/j.ecoinf.2026.103885 · Code: https://github.com/zia207/AutoML-and-Explainable-AI-XAI-for-Rice

এই notebook-টা MSc CSE (Data Science) ছাত্রের জন্য — সহজ চলিত বাংলায় পেপারটা পড়া, বোঝা আর critically review করার জন্য। English-এ আছে শুধু [`review/critical-review-en.md`](review/critical-review-en.md)।

## কীভাবে পড়বেন (How to read)

প্রথমে এই README-র "Top 10 findings" দেখুন, তারপর [`pages/page-01.md`](pages/page-01.md) থেকে ক্রমানুযায়ী পড়ুন — প্রতিটি page-file-এ একই কাঠামো: **A** কী আছে → **B** paragraph ধরে ধরে ব্যাখ্যা → **C** নতুন শব্দ (English → সহজ মানে → ছোট সংখ্যার উদাহরণ → paper-এ কোথায় → খেয়াল) → **D** equation/statistics → **E** figures → **F** tables → **G** critical পর্যবেক্ষণ (page.n নম্বর, প্রমাণ, ধরন) → **H** সারাংশ → **Master Notes**। "প্রমাণ" ঘরে exact page/figure/table/SI/`file:line` দেওয়া আছে। সব অঙ্ক Python দিয়ে হিসাব করা (`work/scripts/`, git-ignored; output [`registers/code-audit.md`](registers/code-audit.md)-এ)। তারপর registers, [`synthesis/A-to-M.md`](synthesis/A-to-M.md) (পুরো ছবি), [`msc-comparison.md`](msc-comparison.md) (আপনার MSc-র সাথে তুলনা) এবং শেষে English review। মনে রাখবেন: "our own check" লেখা সংখ্যা আমাদের সরল মডেল দিয়ে নেওয়া — paper-এর reproduction নয়; এবং R চালানো যায়নি, তাই `.Rmd` চালিয়ে মাপতে হবে এমন প্রভাব আলাদা করে চিহ্নিত।

## Index

| ফাইল | কী |
|---|---|
| [00-document-inventory.md](00-document-inventory.md) | input ফাইল, path, page count, readability |
| [pages/page-01.md](pages/page-01.md) … [page-16.md](pages/page-16.md) | main paper-এর প্রতিটি পেজ — [01](pages/page-01.md) · [02](pages/page-02.md) · [03](pages/page-03.md) · [04](pages/page-04.md) · [05](pages/page-05.md) · [06](pages/page-06.md) · [07](pages/page-07.md) · [08](pages/page-08.md) · [09](pages/page-09.md) · [10](pages/page-10.md) · [11](pages/page-11.md) · [12](pages/page-12.md) · [13](pages/page-13.md) · [14](pages/page-14.md) · [15](pages/page-15.md) · [16](pages/page-16.md) |
| [registers/observation-register.md](registers/observation-register.md) | সব page-এর সব observation এক table-এ (auto-generated) |
| [registers/si-verification-log.md](registers/si-verification-log.md) | প্রতিটি SI item main text/code/data-র সাথে মেলানো |
| [registers/seed-findings-status.md](registers/seed-findings-status.md) | seed F1–F10 + editorial + citation: verified/revised/rejected |
| [registers/code-audit.md](registers/code-audit.md) | code ও data audit, script output সহ |
| [glossary.md](glossary.md) | সব term, alphabetical (auto-generated) |
| [synthesis/A-to-M.md](synthesis/A-to-M.md) | চূড়ান্ত synthesis (A–M) |
| [msc-comparison.md](msc-comparison.md) | paper বনাম আপনার MSc plan |
| [review/critical-review-en.md](review/critical-review-en.md) | formal English critical review |

## Top 10 findings

1. **Table 4-এর Aus ও Boro অদলবদল** (model-count সহ); "Aus-এর কম performance = transition period" ব্যাখ্যা অসমর্থিত; Table 4-এর "CV" আসলে meta-learner level-one metric। → [p5](pages/page-05.md), [p7](pages/page-07.md), [code-audit §8](registers/code-audit.md)
2. **Row-level random split/CV; union-নির্ভর leakage-সম্ভাবনা।** Simulation: test row-এর 97–99.8% union train-এ আছে; আমাদের সরল RF-check: R² 0.461→0.129 (Aus), 0.574→0.276 (Aman), 0.513→0.010 (Boro) leave-union-out-এ। → [p4](pages/page-04.md), [code-audit §3, §10](registers/code-audit.md)
3. **Test-metric অসঙ্গতি:** S6 test R² (Aman 0.590, Boro 0.514) নিজের RMSE-র সাথে মেলে না; Fig. 5 Aus RMSE 835 ≠ HTML 817.6। → [p6](pages/page-06.md)
4. **GLM baseline কার্যত intercept-only** (λ-path 50,164→14,082); সত্যিকারের OLS R² 0.28/0.38/0.20 বনাম RF 0.50/0.58/0.52 (our own check)। → [p4](pages/page-04.md), [code-audit §9](registers/code-audit.md)
5. **XAI training data-য়; Fig. 8-এর model ভিন্ন run-এর; scaling আলাদা প্রতি frame-এ।** → [p5](pages/page-05.md), [p4](pages/page-04.md)
6. **"Additive" claim অপ্রমাণিত;** H-statistic চালানো হলেও report নেই; Fig. 7(o)-এ PD ≠ AL; field duration PFI বনাম flat PDP। → [p8](pages/page-08.md), [p7](pages/page-07.md)
7. **GHG বিশ্লেষণ:** CCAFS-MOT input-এ fertilizer ⇒ circular; S5 = union-mean (ecological) correlation; §3.6 "Aus weak FD" ভুল (Boro-ই weak); "moderate-strong" Aman-এ ভুল; P/K ≈ N-ছায়া (partial r ≈ 0)। → [p3](pages/page-03.md), [p8](pages/page-08.md), [p9](pages/page-09.md), [p11](pages/page-11.md)
8. **Conclusion ফলের চেয়ে বেশি দাবি করে:** "higher yield AND lower GHG" — fertilizer ↔ yield ও GHG দুটোই ধনাত্মক; yield-scaled emission বিশ্লেষণ নেই (our check: Aus/Aman-এ কমে, Boro-তে বাড়ে); Limitations বনাম policy অমিল। → [p12](pages/page-12.md)
9. **Stacking-এর সুবিধা ছোট:** "1–4%" ≠ test 0.9–1.5%; Aus-এ XRT-র তুলনায় মাত্র 0.39%। → [p9](pages/page-09.md)
10. **Citation/editorial/ethics ও reproducibility ত্রুটি:** IPCC 2019 (reviewer list), Suarez-Gutierrez, Gaihre@p1, Wang 2018c, Ahmed 2021a/b, D'Orazio duplicate; Fig./Table reference ভুল; Ethics "wheat"; "all code and data" দাবি বনাম split/models/CCAFS-MOT অনুপস্থিত। → [p1](pages/page-01.md), [p2](pages/page-02.md), [p8](pages/page-08.md), [p13](pages/page-13.md)–[p16](pages/page-16.md)

আপনার MSc-র জন্য সবচেয়ে কাজের: #2 (grouped/spatial CV-র যুক্তি), #4 (fair baseline), #5 (held-out XAI), এবং [msc-comparison.md](msc-comparison.md)।

## Progress

- Pages 01–16: ✅ সব লেখা ও commit করা (`page NN`)।
- Registers (observation, SI log, seed status, code audit), glossary: ✅
- Synthesis A–M, MSc comparison, English review: ✅
- যা করা **যায়নি:** R চালানো (এই machine-এ R নেই) ⇒ `.Rmd` execution-নির্ভর প্রভাব (scaling-অমিল, PFI on test, H-statistic) মাপা হয়নি; আসল train/test split না থাকায় leakage-এর পরিমাণ শুধু simulation; SI Fig. S1–S4 দেখা হয়নি; CCAFS-MOT-এর equation/input অনুপলব্ধ; H2O-র default time-limit offline যাচাই করা যায়নি।
