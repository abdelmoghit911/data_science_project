# House Price Prediction --- Regression Capstone Project

**Module:** AI \& Data Science Basics --- Open Capstone Project  
**Institution:** EHTP --- MIG Department  
**Semester:** S4

## Team Members
- Abdelmoghit El Asraoui
- Mohamed Ben Mouh

## Problem Description
This project aims to predict the final sale price of residential homes in Ames, Iowa, using 79 property features (lot size, building quality, room counts, basement/fireplace/garage details, etc.). The target audience is real estate agents who need accurate price estimates to advise sellers on listing prices and buyers on fair offers. A mispriced listing means either lost money for the seller or a home sitting unsold for months.

## Dataset
**Source:** [Kaggle --- House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
**Size:** 1,460 rows × 81 columns (79 features + Id + SalePrice target)  
**Description:** Each row describes a residential home sold in Ames, Iowa between 2006 and 2010, with features spanning lot size, building type, quality ratings, basement/fireplace/garage details, and more.

### Dataset Justification (7 Criteria)
| # | Criterion | How the Dataset Meets It |
|---|-----------|--------------------------|
| 1 | Minimum size (1,000 rows, 8 features) | 1,460 rows, 79 features --- exceeds both |
| 2 | Public availability | Free on Kaggle with downloadable CSV |
| 3 | Real-world origin | Real residential sales records from Ames, Iowa (2006-2010) |
| 4 | Heterogeneous features | Mix of numerical, ordinal, and categorical |
| 5 | Imperfections | Missing values in ~20 columns |
| 6 | Clear target | Well-defined numerical target: SalePrice |
| 7 | Ethics check | No names, IDs, GPS, or sensitive personal data |

## Project Structure
```
/
├── data/
│   ├── raw/                    # train.csv, test.csv, data_description.txt
│   └── processed/              # train_cleaned.csv, housing.db (SQLite)
├── notebooks/
│   ├── 01_data_acquisition.ipynb   # Phase 1: Loading & audit
│   ├── 02_eda_wrangling.ipynb      # Phase 2: Cleaning, encoding, EDA
│   ├── 03_feature_engineering.ipynb # Phase 3: Features & SQLite
│   └── 04_modelling.ipynb          # Phase 4-5: Training & evaluation
├── src/
│   ├── load_data.py            # Data ingestion script
│   └── gen_pdf.py              # PDF report generation
├── reports/
│   ├── capstone_final_report.pdf   # Final written report
│   ├── presentation.pptx           # Oral presentation slides
│   └── figures/                    # 10 EDA & model figures
├── models/
│   ├── best_model.pkl          # Ridge Regression (α=10)
│   └── best_model_xgb.pkl      # XGBoost backup
├── README.md
├── requirements.txt
└── .gitignore
```

## Best Model Performance

| Model | RMSE (log) | R² | Training Time |
|-------|------------|-----|---------------|
| Linear Regression | 0.205 | 0.775 | <0.1s |
| Random Forest | 0.147 | 0.885 | ~2s |
| XGBoost | 0.144 | 0.889 | ~3s |
| **Ridge Regression (α=10)** | **0.135** | **0.902** | **<0.1s** |

### Final Metrics (Holdout Test Set, 292 Homes, Original Dollars)

| Metric | Value | Target | Met? |
|--------|-------|--------|------|
| RMSE | $25,298 | ≤ $30,000 | Yes |
| MAE | $16,365 | -- | -- |
| MAPE | 9.8% | ≤ 15% | Yes |
| R² | 0.917 | ≥ 0.85 | Yes |

All three project success criteria were exceeded with comfortable margins.

## How to Reproduce
1. Clone the repository:
   ```
   git clone https://github.com/abdelmoghit911/data_science_project.git
   cd data_science_project
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run notebooks in order:
   - `notebooks/01_data_acquisition.ipynb` --- Data loading and initial audit
   - `notebooks/02_eda_wrangling.ipynb` --- Cleaning, outlier detection, EDA visualizations
   - `notebooks/03_feature_engineering.ipynb` --- Feature creation, selection, SQLite storage
   - `notebooks/04_modelling.ipynb` --- Model training, hyperparameter tuning, evaluation
4. Outputs are saved to `models/` and `reports/`
