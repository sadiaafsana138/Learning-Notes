# Geospatial & Explainable AI Analysis of Rice Yield (Aman, Aus, Boro)

This repository contains R Markdown analyses exploring **rice yield** across three major seasons in Bangladesh (or similar regions): **Aman**, **Aus**, and **Boro**. The project combines **geospatial correlation analysis**, **Automated Machine Learning (AutoML)** for yield prediction, and **local Explainable AI (XAI)** techniques.

## 📁 Project Structure

### Geospatial Correlation Analysis
- `gw_correlation_aman_01.Rmd` / `.html` — Geographically Weighted Correlation (Aman Season - Part 1)
- `gw_correlation_aman_02.Rmd` / `.html` — Geographically Weighted Correlation (Aman Season - Part 2)

### Local Explainable AI (XAI) Analysis
- `local_XAI_uniion_aman.Rmd` / `.html` — Local XAI for Aman season (Union level)
- `local_XAI_uniion_aus.Rmd` / `.html`  — Local XAI for Aus season (Union level)
- `local_XAI_uniion_boro.Rmd` / `.html` — Local XAI for Boro season (Union level)

### AutoML Yield Prediction Models
- `yield_aman_autoML.Rmd` / `.html` — AutoML modeling and prediction for Aman rice yield
- `yield_aus_autoML.Rmd` / `.html`  — AutoML modeling and prediction for Aus rice yield
- `yield_boro_autoML.Rmd` / `.html` — AutoML modeling and prediction for Boro rice yield

### Dataset
This dataset supports the study "AutoML and Explainable AI (XAI) for Rice Production Systems: Unraveling Yield Predictors and Greenhouse Gas Emissions in Bangladesh." It integrates plot-level rice production records with spatial environmental covariates to support machine-learning prediction of rice yield and modeled greenhouse gas (GHG) emissions across Bangladesh's three rice-growing seasons — Aus (winter–rainy transition), Aman (rainy), and Boro (irrigated winter).
The core agronomic data come from the Bangladesh Integrated Household Survey (BIHS, 2015), conducted by IFPRI and the PRSSP across all seven administrative divisions, covering roughly 6,500 households and 325 primary sampling units. Plot-level variables include rice yield, crop type and variety (local, high-yielding, or hybrid), field size and duration, transplanting and harvest dates, fertilizer (N, P, K) types and rates, organic matter and lime application, tillage, and irrigation practices, all converted to standard metric units.
Each survey location is matched to a harmonized set of spatial environmental layers resampled to a common 250 m × 250 m grid: national soil properties (pH, SOC, N, P, K, S, B, Zn) interpolated from a ~31,800-point SRDI dataset; SRTM-derived elevation; 16-day MODIS NDVI time series (2014–2015); and ERA-Interim temperature and rainfall. The dataset also includes modeled per-plot GHG emissions (CH₄, N₂O, CO₂, and total global warming potential) generated with the CCAFS Mitigation Options Tool (CCAFS-MOT).
In total it spans about 13,000 farmer records across the three seasons, providing a ready-to-model resource linking farm management, biophysical conditions, rice yield, and emissions for spatial and explainable-AI analyses.


## 📊 Project Overview

This repository focuses on:

- **Geographically Weighted Correlation** to understand spatial variation in relationships affecting rice yield.
- **AutoML** approaches for accurate yield prediction in different rice seasons.
- **Local Explainable AI (XAI)** to interpret model predictions at the union level, providing insights into which factors drive yield in specific locations.

The analyses are particularly relevant for **precision agriculture**, **food security**, and **climate-smart rice farming** in regions with distinct seasonal patterns (Aman, Aus, Boro).

## 🛠 Technologies Used

- **R** & **R Markdown**
- **Geographically Weighted Models** (GW correlation)
- **AutoML** frameworks (likely h2o, AutoML, or similar)
- **Explainable AI** techniques (SHAP, LIME, or local interpretability methods)
- HTML outputs for easy viewing and sharing of results

## 📖 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

   
