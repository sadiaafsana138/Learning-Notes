# Critical Review

**Paper:** Ahmed, Z.U., Sapkota, T.B., Hossain, M.K., Khanam, F., Timsina, J., Krupnik, T.J. (2026). *AutoML and explainable AI (XAI) for rice production systems: Unraveling yield predictors and greenhouse gas emissions in Bangladesh.* Ecological Informatics 97, 103885. https://doi.org/10.1016/j.ecoinf.2026.103885

**Materials examined:** the 16-page article; the 24-page Supporting Information (SI); the public repository (three season CSV files, eight R Markdown scripts and their rendered HTML outputs). R was not available in the review environment, so no script was executed; model outputs were read from the rendered HTML files. No AutoML model was retrained. Where we ran our own analyses (Python), they are labelled as such and are *not* reproductions of the authors' models.

**Conventions.** Locations are given as page / section / figure / table / SI item / `file:line`. Statements fall into three kinds: (A) acknowledged by the authors, (B) confirmed by us with evidence, (C) suspected. Where documentation is missing we write: "Not reported in the provided paper, Supporting Information, or available code."

---

## 1. Introduction & context

The study addresses an important question: which management, soil and climate factors are associated with rice yield in Bangladesh, and how do these associations relate to greenhouse-gas (GHG) emissions. The motivation (food security, mitigation) is well framed (p1–2).

**1.1 Citation–claim mismatches (B).**
- *Location:* p1 ¶1–2; p2 ¶3, ¶5; reference list p14, p16.
- *Evidence:* "IPCC, 2019" is titled "Annex IV: reviewers of the IPCC special report on climate change and land"; "Suarez-Gutierrez et al., 2018" is "Internal variability in European summer temperatures at 1.5 °C and 2 °C of global warming" (cited for net-negative emissions and rice mitigation); "Gaihre et al., 2015" concerns N₂O/NO emissions from urea deep placement (cited at p1 for CH₄); "Wang et al., 2018c" is "A cognitive vision method for insect pest image segmentation" (cited for stacking). The text cites "Ahmed et al., 2021a, 2021b" but the list holds one 2021 Ahmed entry; D'Orazio et al. (2019) appears twice. The "one-third" food-system claim is in fact supported by Crippa et al. (2021), cited alongside.
- *Why it matters:* readers cannot rely on the cited literature to support the stated premises.
- *Suggested fix:* verify each citation against its source; replace or remove mismatched ones; de-duplicate.

**1.2 Literature positioning (B).** Rudin (2019) argues for inherently interpretable models instead of post-hoc explanations of black boxes; the study adopts the opposite approach without discussing the argument (p2, p4). Song et al. (2020) concerns cross-site transportability, which the study does not examine (p2; refs p15).
- *Suggested fix:* discuss why a stacked ensemble with post-hoc XAI is preferred and compare with an interpretable model.

**1.3 Scope statements (B).** "One-third" (food systems) and "15%" (agricultural food system) are given without clarifying scope (p1). The novelty claim ("XAI has not yet been applied … in Bangladesh") sits beside the authors' own earlier AutoML+XAI maize study in Bangladesh (p2, p9) and should be narrowed to rice.

---

## 2. Objectives

The paper has no explicit research questions or hypotheses (p2). From the Methods the implicit aims are: (i) predict seasonal rice yield with AutoML; (ii) identify influential factors with XAI; (iii) map union-averaged local attributions; (iv) relate the key factors to modeled GHG. Prediction in unseen areas is not an objective, although the spatial framing of the title and abstract invites that reading.
- *Suggested fix:* state the research questions, and state explicitly that spatial transferability is outside scope (or test it).

---

## 3. Dataset & data quality

**3.1 Unit of observation (B).** The paper reports "6500 households" (p2), "13,137 farmers" (p5) and "plot-level" data. The released CSVs contain 13,150 rows (677 Aus, 6,664 Aman, 5,809 Boro; `*_data_all.csv`), each a unique `Index` record; no household or plot identifier column is documented. The number of unions is 78 / 246 / 224 in the data versus 78 / 247 / 224 in the text (p5).
- *Why it matters:* the independence structure of the data cannot be assessed.
- *Fix:* document the identifier scheme; reconcile row and union counts.

**3.2 Location assignment (A, B).** The authors acknowledge union-centroid assignment (p12). We confirm it: within every union, all 29–42 environmental columns (NDVI, climate, soil, DEM) are identical (`work/scripts/check01_07_data.py`). Consequently the stated 250 m grid precision (p2–3) carries no information beyond the union level, and resampling 12 km weather data to 250 m (a factor of (12000/250)² = 2304 in pixel count) adds smoothing rather than information.
- *Also:* the text states that NDVI (250 m) is the finest layer (p2) whereas Table 1 lists the DEM at 90 m (p3).

**3.3 Undefined or inconsistently reported variables (B).** Field duration is not defined (observed range 91–123, 91–146, 110–157 days; no date columns to reconstruct it). Water management is described as extracted (p2), excluded (p12), yet `Water_regime` is a model predictor (`yield_aus_autoML.Rmd:115`; Aman:128; Boro:131); its values are constant by season (Aus "Rainfed, wet season" 677/677; Boro "Continuous flooding" 5,809/5,809), i.e. a season class rather than farmer-reported irrigation, and its permutation importance is ≈ 0 (SI Tables S8–S9). The categorical predictors listed in the text (line sowing, balanced fertilization, lime; p4) differ from those in the code (land type, soil type, drainage class, temperature zone, texture, `Water_regime`, `Manure`). Unit-conversion factors, sampling weights, the number of rows removed as outliers (training sizes are 526 / 5,305 / 4,626, i.e. 77.7 / 79.6 / 79.6% of rows) and the origin of the land/soil/drainage/temperature-zone classes are not reported.

**3.4 Boro yield range (B).** The text gives ~2000–9000 kg/ha for Boro (p7); the CSV minimum is 0, with 12 zero-yield rows and 195 rows below 2000. Whether these are crop failures or data errors is not stated.

**3.5 Soil data (A, B).** The SRDI layers date from 1996–2014 (p3), the survey from 2015; kriging uncertainty is not propagated; 31,787 of 50,000 points were used without stated criteria; boron was interpolated but is absent from the models.

---

## 4. Methodology

**4.1 Data processing and scaling (B).** Features are standardised with `scale()` separately for the full, training and test frames (`yield_aus_autoML.Rmd:120,127-129`; Aman:133,140-142; Boro:136,143-145; local XAI: `local_XAI_uniion_aus.Rmd:108,115-117`). Test data are therefore not scaled with training statistics. *Why it matters:* it introduces a train/test inconsistency that matters most for GLM/DNN and for local explanations. *Fix:* fit scaling on training data only; its practical effect requires execution to quantify.

**4.2 AutoML configuration (B).** The paper reports `stopping_tolerance = 0.0001`, `stopping_rounds = 2`, and `max_runtime_secs = max_models = 0` (p4). The code uses 0.001 and 3, comments out `max_models`, and sets `max_runtime_secs_per_model = 0` (`yield_aus_autoML.Rmd:202-207`; Aman:215-220; Boro:218-223); SI Table S2 describes MAE-based early stopping over five rounds. We could not verify offline the default time limit applied by H2O when neither global limit is set; if a default applies, "no limit" would be inaccurate and the model counts (958 / 175 / 188) would reflect the time budget rather than search thoroughness. *Fix:* report the exact configuration and run log.

**4.3 Run provenance (B).** The local-XAI scripts load saved models different from those in the AutoML scripts' outputs (Aus `…AutoML_4_20211104_201857` vs `…AutoML_5_20211128_82339`; Aman `…AutoML_5_20211104_162457` vs `…AutoML_3_20211127_174647`; Boro `…AutoML_2_20211102_201704` vs `…AutoML_1_20211104_123317`; `local_XAI_uniion_*.Rmd:159/170/171` vs HTML). It is therefore unclear which run underlies Table 4, Figs. 5–7 versus Fig. 8.

**4.4 Season windows (B).** Feature windows are fixed calendar dates (SI Table S3): Aman ends 19 Dec 2014 while Boro starts 1 Nov 2014. In the Aman model `TEMP, DEC-19-2014` ranks eighth (15.6%, SI S8). Windows are not aligned to farmers' planting dates. *Fix:* use planting-date- or growth-stage-aligned features.

---

## 5. ML & validation

**5.1 Split and cross-validation design (B).** The 80/20 split and the 10-fold CV are row-level random; no `fold_column` or grouping by union/household is used (`yield_*_autoML.Rmd:200/213/216`), and the split files and the code that created them are absent from the repository. Because all rows within a union share identical environmental values, random splitting places rows from the same union in both training and test sets. This does not by itself prove leakage (the real split is unavailable), but in a simulation of the described procedure 97.0% / 99.8% / 99.7% of test rows (Aus/Aman/Boro) share a union with at least one training row (`work/check03_09_10.out`). *Our own check with a simpler model (random forest, defaults; not a reproduction):* R² falls from 0.461 to 0.129 (Aus), 0.574 to 0.276 (Aman) and 0.513 to 0.010 (Boro) when row-random 5-fold CV is replaced by leave-union-out CV. Reported R² (0.45–0.59) is therefore informative about interpolation among known unions, not about unseen areas. *Fix:* grouped/spatial CV and a test on unseen unions or districts.

**5.2 Baseline (B).** The GLM baseline has training R² = 0.000 in all seasons (SI S6). The rendered output shows a ridge GLM with λ = 14,082 (= λ_min), the last value of a 30-point path starting at λ_max = 50,164 (Aus; HTML), so the λ search never reached small penalties; the model is effectively intercept-only. A properly specified linear model on the same predictors (our own OLS, random 80/20 split, seed 42) reaches test R² of 0.284 / 0.378 / 0.197 versus 0.503 / 0.575 / 0.515 for a random forest. "Machine learning beats linear" survives, but with a smaller margin than an intercept-only comparison implies. *Fix:* report a tuned ridge/OLS/GAM baseline.

**5.3 Table 4 and metric stages (B).** Table 4 (p7) swaps Aus and Boro. Its "Boro" row (958 models; RMSE 816.01, MAE 622.31, RMSLE 0.35, R² 0.55) matches the Aus outputs (HTML: 958 base models; meta-learner level-one RMSE 816.68, MAE 622.46, R² 0.5448; SI S6 Aus CV 816.0/0.543); its "Aus" row (198; 1109.2, 773.47, 0.43, 0.51) matches Boro (HTML: 188 base models; CV RMSE 1112.41, MAE 772.56; SI S6 Boro CV 1109.2/0.510). Aman matches. The explanation that Aus performs worse because of the dry-to-wet transition (p5) rests on the swapped labels; per SI S6 the lowest CV R² is Boro (0.510). In addition, the Table 4 values correspond to the meta-learner's level-one metrics, not the stack's own 10-fold CV (Aus: 836.03 vs 816.68 RMSE). The text range for MAE ("637–773") conflicts with the table minimum (622.31), and the statement that MAE is below "the minimum observed yield" (p5) is not true of the data (minimum yields: 247, 112, 0 kg/ha). *Fix:* correct labels and state the metric stage for every number.

**5.4 Test metrics (B).** SI S6 test RMSE matches the rendered H2O test output (817.6 / 948.7 / 1122.7). However, the S6 test R² for Aman (0.590) and Boro (0.514) is inconsistent with the S6 test RMSEs and the GLM test statistics (implied 0.562 and 0.524), whereas the Fig. 5 R² values (0.561, 0.523) are consistent. For Aus, Fig. 5 reports RMSE 835 whereas the test output gives 817.6; the origin of 835 is unclear (the stack's CV RMSE is 836.03). *Fix:* regenerate all test metrics from one run and one test set.

**5.5 Stacking advantage (B).** The Discussion claims a 1–4% RMSE improvement over the best DRF (p9). From SI S6: test 1.47 / 1.08 / 0.91%; CV 6.23 / 1.81 / 1.07% (the Aus CV figure mixes stages); in Aus the best single model on test is XRT (820.8), 0.39% worse than the stack (817.6). With test sets of roughly 136–151 rows (Aus) and no repeated splits, differences of this size are within plausible noise. The authors themselves describe the improvement as "slight" (p6). *Fix:* repeated grouped CV with paired comparisons and intervals.

---

## 6. Spatial analysis

**6.1 Maps of union means (B).** Fig. 4 shows union-mean yield and GHG; the text states there is no distinct spatial pattern. Our own Moran's I (8 nearest neighbours, 999 permutations) shows none for Aus (I = 0.005, p = 0.93) but weak, significant positive autocorrelation for Aman (0.193, p = 0.001) and Boro (0.228, p = 0.001). The statement is therefore accurate for Aus and only loosely for the other seasons.

**6.2 Fig. 8 and breakdown maps (B, C).** Fig. 8 maps union means of local breakdown contributions. (i) The legends give no units, break method or per-union sample size, and classes differ by panel. (ii) A positive contribution of N-rate in X% of unions largely reflects whether a union's N-rate lies above the average rather than a spatially varying effect; as a naive proxy, the share of Aman unions with below-average local-variety share is 73.6%, close to the reported ">70%" for crop type (`work/check_breakdown_proxy.out`; not a reproduction of the method). (iii) The model used for Fig. 8 differs from that used for Table 4 (§4.3), and the input file `*_union_data_all.csv` is not provided. A spatial map of attributions, even a faithful one, does not establish spatial transferability.

---

## 7. XAI

**7.1 Data used (B).** PFI, PDP and ALE are computed on the training data (`explainer_train`; `yield_aus_autoML.Rmd:849-862,1016-1054`; Aman:862,875; Boro:865,878; no test explainer). The text (p5) leaves this open; it should be test or held-out data.

**7.2 Description of PFI (B).** The text describes the loss as "the factor by which the RMSE is increased" (p7); the code uses `type="difference"`, so the values (e.g. 361.5 for Aus N-rate) are differences in kg/ha; "importance %" is loss relative to the maximum (verified for Tables S7 and S9).

**7.3 Rank stability (B).** Importance gaps between adjacent top-five features are mostly within about 1–2 pooled permutation SDs (Aman crop type vs N: 11.2 / 25.3 = 0.44); only Aus N vs crop type is clearly separated (z ≈ 4.4). The set of five key features is robust; their order is not.

**7.4 Additivity (B).** The claim that the stack is additive rests on PD and ALE profiles being parallel (p8). Similar PD and ALE curves do not establish additivity (absence of interactions). `iml::Interaction` was computed and written to `Feature_Interaction.csv` (Aus:1066-1076; Aman:1089; Boro:1093), but no result is reported in the paper or SI, and the file is not in the repository. Moreover Fig. 7(o) (Boro crop type) shows PD and ALE differing by roughly 350–500 kg/ha. *Fix:* report H-statistics or remove the claim.

**7.5 Field duration (B, C).** Field duration has high PFI importance (61.3 / 70.0 / 47.7%) yet flat PD/ALE profiles (Fig. 7d,i,n). The authors note both but do not reconcile them; interaction with crop type or season, or acting as a proxy for variety, are possible explanations that can be tested with the unreported interaction output.

**7.6 Interpretation limits (A).** The authors state that post-hoc XAI does not explain causation and that PFI, PDP, ALE and breakdown have known limitations (p12). We agree; the Abstract and parts of the Discussion ("influencing", "impact", "critical role in increasing rice yield") use causal language that the Limitations paragraph does not support.

**7.7 Local XAI vs GW regression (C).** The Discussion proposes that local model-agnostic interpretation overcomes limitations of GW regression (p9). No comparison is presented, and the two approaches describe different objects (the model's behaviour vs local relationships in data).

---

## 8. GHG analysis

**8.1 Modeled emissions and circularity (A, B).** Emissions were modeled with CCAFS-MOT, whose inputs include fertilizer rates (p3 §2.2); this limitation is acknowledged in part. Because fertilizer rate is also the explanatory variable, correlations between N-rate and Total GWP (e.g. Aus r = 0.816; SI S5) are partly built in. The magnitude cannot be assessed because the CCAFS-MOT code, version and input list are not available. The Abstract does not state that GHG is modeled.

**8.2 Aggregation level (B).** SI Table S5 correlations are reproduced exactly (Aus, Boro) or approximately (Aman) by correlating *union means* (n = 78 / 246 / 224); row-level correlations are markedly lower (e.g. Aus P: 0.545 vs 0.385; Aman K: 0.223 vs 0.085). They are ecological correlations and should be labelled as such. The GW correlation bandwidth is chosen from a GWR AICc search; in the Aman scripts it is 144 nearest neighbours with `Crop_Types` and 69 without (HTML outputs of `gw_correlation_aman_01/02`), and it is not stated which version underlies Fig. 9. In `_01` a nominal variable (`Crop_Types`) enters a Pearson/GWR calculation (`gw_correlation_aman_01.Rmd:77`).

**8.3 Statements inconsistent with SI Table S5 (B).** (i) "Moderate to strongly positive across three rice-growing seasons" (p8) does not hold for Aman (N 0.201, P 0.108, K 0.223, FD 0.277; yield–GWP 0.061); the Discussion's "moderate to strong association" of P and K with GHG (p11) has the same problem. (ii) Section 3.6 (p9) states that Aus shows only a weak field-duration–GHG connection; S5 gives Aus 0.309, Aman 0.277, Boro 0.058, so Boro is the weak case — as the Discussion (p11) says — and Fig. 9(l) agrees. (iii) "The stacking ensemble model effectively captured these relationships" (p9) refers to an analysis in which no stacking model is used.

**8.4 P and K (B).** With N-rate partialled out, the association of GWP with P is near zero (Aus 0.116; Aman −0.070; Boro −0.016 at row level), supporting the authors' explanation that P/K associations arise from co-application with N (p11).

**8.5 Conclusion on nutrient management (B).** The Conclusion states that better nutrient management is linked to higher yield *and* lower GHG (p12). The results show that higher fertilizer rates accompany both higher yield and higher modeled emissions; no nutrient-use-efficiency or yield-scaled analysis is presented. In our exploratory check using the dataset's `Emission_Intensity` (≈ GWP/yield; definition not documented), intensity falls across N-rate quartiles in Aus (median 0.39 → 0.35) and Aman (1.82 → 1.31) but rises in Boro (0.72 → 0.83), so the claim is season-dependent and untested in the paper. The statement that hybrid area expansion "could help reduce GHG emissions" is not supported by the study's own results (hybrid modeled GWP exceeds HYV in Aus and Boro; row-level Welch tests p < 0.001; not significant in Aman), and the "no significant difference" statement holds only for Aman in our check.

**8.6 Fig. S7 (B).** The GHG permutation-importance figure is not cited in the main text, its caption is truncated, no code or performance metrics are available, and N-rate is absent from the top features for Aus despite the strong N–GWP correlation in S5.

---

## 9. Results & interpretation

- **Editorial inconsistencies (B).** Figure references: §3.4 cites Fig. 6 (and Figs. 6b, 6h) where Fig. 7 is meant; "P-rate (Fig. 7g)" in §3.5 should be Fig. 8g; "AL profiles (blue lines)" contradicts the legend (PD blue, AL orange); crop type is the rightmost, not leftmost, Fig. 7 panel. Tables 2 and 3 are missing (numbering jumps from 1 to 4). Hyperparameters are attributed to "Tables S2 and S3" (S3 holds MODIS dates; the grid is in S4, which is not cited). Fig. S6 panel letters do not match the caption or text (drainage is panel (d), temperature zones panel (e)). Fig. 9's first field-duration legend class reads "> 0.035". "Boro F-value" appears twice (the value 27.6 corresponds to Aus in our ANOVA; Aman 733.7 matches; Boro 116.6 vs the reported 123). Table 1 lists "Boro/Aman/Boro" and an ERA-Interim link to a MODIS archive. The Ethical statement refers to predicting wheat yield (p13).
- **Positive verification.** The crop-mix percentages (HYV 80.8, local 10.9, hybrid 8.4%; hybrid 3.1/3.6/14.4%), the ranking and counts of PFI features (17/19/18 features above 10%; orders in the text match SI Tables S7–S9) and several ANOVA F-values reproduce from the released data.
- **Discussion claims.** "N most important in all seasons" (p10) conflicts with Aman PFI (crop type first, SI S8) and with §3.5. Placement/timing recommendations and "balanced fertilization" are not testable with rate-only data. Several citations in the Discussion are only loosely related to the claims (Chen 2011, Luo 2013, Sutton-Grier 2011 for rice-yield soil processes; Craufurd & Wheeler 2009 for growth duration; Sapkota 2014 on wheat for rice N management).

---

## 10. Reproducibility

The repository releases the three feature tables and the R Markdown scripts, which is commendable. However, the Data-availability statement ("the code of all workflows and data") and §2.3.3 overstate completeness. Not in the repository: `train_data.csv`, `test_data.csv` and the splitting code; `*_union_data_all.csv`; GW shapefiles; saved H2O models and run logs; CCAFS-MOT code and outputs (the data hold only `Total_GWP` and `Emission_Intensity`, not separate CH₄/N₂O/CO₂); NDVI, weather and kriging pipelines; Aus/Boro GW code; the Fig. S7 code. Scripts contain hard-coded paths, a variable-name bug in the Aus script (`t.xy` at line 810 vs `test.xy` at line 800), mislabelled titles/outputs (the Aman XAI script is titled "Boro"; the Aus XAI script writes `Local_contribution_aman_union.csv`), and column-name inconsistencies (Aman `NDVI_205` vs `t2m_209` and SI S3 date 209; Boro `NDVI_001_2105`; S3 lacks the 1 Jan Boro date that the data and Table S9 include). Seeds are set only inside AutoML (`seed = 42`). *Fix:* release split files, saved models/seeds, environment, and all processing and GHG code.

---

## 11. Strengths

- A large, farm-level, three-season dataset with open tables and code.
- Transparent reporting of all algorithms' training, CV and test errors (SI S6).
- Use of both PDP and ALE, permutation SDs, and an explicit, honest Limitations section (causation, centroid assignment, sampling bias, water data, CCAFS-MOT, ordering dependence).
- Descriptive statistics that reproduce from the released data; a plausible and, in our check, supported explanation for the P/K–GHG association.
- Relevant policy motivation and good use of Bangladesh-specific literature.

---

## 12. Limitations & critical concerns

| Concern | Location | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| Row-level random validation; union leakage possible | p4 §2.3; `Rmd:200/213/216` | Simulation 97–99.8%; own RF: R² 0.461→0.129 etc. | Reported skill not indicative of unseen areas | Grouped/spatial CV; unseen-union test |
| Table 4 swapped; metric-stage mixing | p7 Table 4; SI S6; HTML | §5.3 | Wrong season attribution; incorrect explanation | Correct and state stage |
| S6/Fig. 5 test inconsistencies | SI S6; Fig. 5 | §5.4 | Unclear which run/metric | Single-run regeneration |
| Intercept-only baseline | SI S4/S6; HTML | λ path 50,164→14,082; R² 0.0001 | Overstates ML advantage | Tuned linear baseline |
| XAI on training data; different model for Fig. 8 | Rmd:849-862; XAI Rmd:159/170/171 | §7.1, §4.3 | Explanations may not describe reported model/held-out behaviour | Held-out XAI on the reported model |
| Additivity claim unsupported | p8; Rmd:1066-1076 | §7.4 | Misleading simplification | Report H-statistic |
| Circular fertilizer–GHG link; ecological correlations | p3; SI S5 | §8.1–8.2 | Weakens GHG conclusions | Remove/justify; use measured fluxes |
| Conclusion exceeds evidence | p12 | §8.5 | Policy risk | Yield-scaled analysis or temper |
| Causal wording vs Limitations; Limitations vs policy | p1, p10, p12 | §7.6 | Inconsistent message | Harmonise wording |
| Citation and editorial errors | various | §1.1, §9 | Credibility | Systematic check |
| Incomplete code/data release | p5, p13 | §10 | Not reproducible | Complete release |

---

## 13. Implications

For practitioners: the five predictors (N, P, K rates, variety, field duration) are consistently important *for within-sample prediction*, in line with agronomic expectation; the study does not demonstrate that changing them would change yield or emissions, or that the models would perform in new districts. Policy recommendations (subsidies, extension decision support) go beyond the evidence and the authors' own caution about validation through controlled trials (p12). For researchers: the released data are a useful benchmark for spatially grouped validation, season-aligned features, held-out XAI and fair interpretable baselines, and for studies of transferability to unseen areas.

---

## 14. Conclusion

The paper assembles valuable data and an openly shared workflow, and its limitations section is candid. Our verification supports many descriptive results but identifies issues that affect the central inferences: a mislabelled results table with mixed metric stages; test-metric inconsistencies; a random validation design that cannot indicate performance in unseen areas (and, in our simplified check, drops sharply under union-grouped validation); an intercept-only baseline; explanations computed on training data and, for the maps, from a different model run; an unsupported additivity claim with unreported interaction results; partly circular and aggregated GHG correlations; and a Conclusion that goes further than the analysis. Each is correctable, mostly by re-running existing pipelines with grouped validation, a single consistent run, held-out explanations and complete reporting. We recommend major revision with these specific actions: (1) correct Table 4 and regenerate all metrics from one run and one test set; (2) adopt grouped/spatial validation and report uncertainty across repeated splits; (3) add a tuned interpretable baseline; (4) compute XAI on held-out data for the reported model, and report interaction statistics; (5) clarify the GHG modeling inputs, treat fertilizer–GHG correlations as partly built-in, and add yield-scaled analysis or temper the Conclusion; (6) fix citations and editorial errors; (7) release split files, models, seeds and all missing code.
