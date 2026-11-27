# Axlero Retail Churn: Customer Segmentation and Churn Prediction

Data Analytics internship project for **Axlero Solutions** (Project 1: Retail & E-commerce).

## Problem Statement

Direct-to-consumer retailers often face high customer acquisition costs and unpredictable retention. Without knowing which customers are valuable and which are about to leave, marketing budgets are wasted.

This project:

1. Segments customers using **RFM** (Recency, Frequency, Monetary) metrics and K-Means clustering.
2. Builds a **churn prediction model** to identify customers likely to stop buying.
3. Presents the results in a **BI dashboard** with actionable recommendations for each segment.

## Success Targets

| Area | Target |
|---|---|
| Data integrity | Handle missing values and outliers without dropping more than 5% of the data |
| Model performance | Churn model ROC-AUC of at least 0.75 |
| Actionability | At least 4 distinct customer segments, each with marketing recommendations |

## Tech Stack

- **Language:** Python 3.9+
- **Analysis:** Pandas, NumPy, SciPy
- **Machine learning:** Scikit-Learn
- **Database:** PostgreSQL (SQLAlchemy / Psycopg2)
- **Visualization:** Matplotlib, Seaborn, Power BI

## Project Structure

```
axlero-retail-churn/
├── data/
│   ├── raw/          # Original, immutable data
│   ├── interim/      # Cleaned / transformed data
│   └── processed/    # Final datasets for modeling
├── notebooks/        # Numbered Jupyter notebooks (1.0-eda, 2.0-rfm, ...)
├── src/              # Reusable Python code (dataset.py, features.py, modeling/)
├── models/           # Trained model files (joblib)
├── reports/          # Final report and figures/
├── requirements.txt  # Python dependencies
└── README.md
```

## Setup

```bash
git clone https://github.com/sonnnuuu/axlero-retail-churn.git
cd axlero-retail-churn
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Four-Week Plan

| Week | Focus | Main outputs |
|---|---|---|
| 1 | Data ingestion, SQL extraction, cleaning, EDA | Cleaned data in `data/interim/`, EDA notebook |
| 2 | RFM features and K-Means segmentation | `src/features.py`, segmented data in `data/processed/` |
| 3 | Churn modeling (Logistic Regression, Random Forest) | Trained models in `models/`, evaluation metrics |
| 4 | Power BI dashboard and final reporting | Dashboard file, final report in `reports/` |

## Progress

- [x] Repository and folder structure created
- [ ] Week 1: Data ingestion and EDA
- [ ] Week 2: RFM and segmentation
- [ ] Week 3: Churn prediction
- [ ] Week 4: Dashboard and report


## Data Quality Findings (Week 1)

- Total rows loaded into PostgreSQL: 1,067,371
- Rows with no customer_id: 243,007 (22.77% of rows, 15.40% of revenue). Kept and flagged; excluded only from customer-level RFM.
- Cancelled orders: 19,494
- Rows with quantity <= 0, price <= 0 or cancelled: 25,701 (2.41%). Dropped for sales analysis, within the 5% limit.

## Author

Devarakonda Sony, Data Analyst Intern, Axlero Solutions
