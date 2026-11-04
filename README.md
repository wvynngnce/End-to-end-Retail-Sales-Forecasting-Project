# End-to-End Retail Sales Forecasting

An end-to-end data science project focused on analyzing historical retail sales patterns and developing a machine learning model to forecast daily sales across selected product families. The project combines exploratory data analysis, time series forecasting, model evaluation, and business intelligence visualization using Python and Power BI.

---

## 1. Business Problem

Retail businesses operate in an environment where customer purchasing behavior, promotional activities, and seasonal patterns can cause daily sales to fluctuate.

Without reliable sales forecasts, business teams may struggle to:

- Anticipate changes in sales performance.
- Identify high-performing and underperforming product categories.
- Plan operational resources based on expected sales activity.
- Evaluate promotional activities and their relationship with sales.
- Make data-driven decisions using historical sales patterns.

Historical sales data provides valuable information, but understanding past performance alone is not sufficient. Businesses also need forward-looking insights to support operational and commercial planning.

### Business Questions

This project addresses the following questions:

1. How do daily sales evolve over time across different product families?
2. Which product families contribute the most to overall sales?
3. Are there recurring weekly sales patterns?
4. How are promotional activities associated with sales performance?
5. Can machine learning provide more reliable short-term sales forecasts than simple baseline methods?
6. How can forecasting results be translated into actionable business insights?

---

## 2. Project Objectives

The main objective is to develop a data-driven retail sales forecasting solution that supports short-term business planning.

Specific objectives:

- Perform exploratory data analysis to understand historical sales behavior.
- Identify temporal patterns and differences between product families.
- Develop baseline forecasting models for performance comparison.
- Build a Random Forest model using time-based features.
- Evaluate forecasting performance using chronological validation.
- Visualize historical sales, forecasts, and model performance through an interactive Power BI dashboard.
- Translate analytical findings into practical business recommendations.

---

## 3. Dataset

This project uses the **Store Sales – Time Series Forecasting** dataset provided by Corporación Favorita through Kaggle.

**Dataset source:** [Store Sales – Time Series Forecasting (Kaggle)](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)

The dataset contains historical daily sales information from Favorita grocery stores in Ecuador, along with supporting information such as store metadata, transactions, oil prices, and holiday events.

### Dataset Files

The original dataset includes:

| File | Description |
|---|---|
| `train.csv` | Historical daily sales records |
| `test.csv` | Test dataset |
| `stores.csv` | Store metadata |
| `transactions.csv` | Daily transaction records |
| `oil.csv` | Daily oil prices |
| `holidays_events.csv` | Holiday and event information |

### Project Dataset

For this project, historical sales were aggregated by date and product family.

The resulting analytical dataset contains:

- **8,420 observations**
- **3 columns:** `date`, `family`, and `sales`
- **5 selected product families:** GROCERY I, BEVERAGES, PRODUCE, CLEANING, and DAIRY.
- **Historical period:** January 2013 to August 2017.

The target variable, `sales`, represents monetary sales value in USD rather than the number of units sold.

**Note:** Original Kaggle dataset files are not included in this repository because of file size limitations. Download the dataset directly from Kaggle and place the required files in the appropriate local data directory before reproducing the project.

---

## 4. Project Workflow

The project follows an end-to-end data science workflow:

1. Data understanding and preparation.
2. Exploratory data analysis.
3. Feature engineering.
4. Baseline forecasting.
5. Random Forest model development.
6. Model evaluation and validation.
7. Forecast generation.
8. Power BI dashboard development.
9. Business insights and recommendations.

### 4.1 Exploratory Data Analysis (EDA)

EDA was conducted to understand historical sales behavior and identify potential patterns that could support forecasting.

The analysis covers:

- Overall daily sales trends.
- Sales distribution and variability.
- Sales contribution by product family.
- Average sales by day of the week.
- Weekly sales patterns.
- Promotional activity and its relationship with sales.

### 4.2 Feature Engineering

Time-based features were created to capture historical sales behavior and temporal patterns.

| Feature | Description |
|---|---|
| `day_of_week` | Day of the week |
| `day` | Day of the month |
| `month` | Month of the year |
| `year` | Calendar year |
| `lag_1` | Sales from the previous day |
| `lag_7` | Sales from seven days earlier |
| `lag_14` | Sales from fourteen days earlier |
| `lag_28` | Sales from twenty-eight days earlier |
| `rolling_mean_7` | Seven-day rolling average |
| `rolling_mean_28` | Twenty-eight-day rolling average |

These features enable the model to learn relationships between recent historical sales and future sales values.

### 4.3 Baseline Forecasting

Three baseline approaches were developed to establish reference forecasting performance:

- **Naive:** Uses the most recent observed sales value as the forecast.
- **Moving Average (7):** Uses the average of the previous seven days.
- **Seasonal Naive (7):** Uses sales from the corresponding day in the previous week.

### 4.4 Machine Learning Model

Random Forest Regressor was selected as the main machine learning approach.

The model uses engineered time-based features to estimate future daily sales for each selected product family.

A recursive forecasting strategy was applied to generate a seven-day forecast, where previously predicted values are incorporated into subsequent forecasting steps.

---

## 5. Model Evaluation

### Validation Strategy

A chronological expanding-window rolling-origin validation strategy was implemented.

The evaluation consists of eight validation folds, each covering seven consecutive days.

For every fold:

- The model is trained using historical observations available up to a specific cutoff date.
- The next seven days are used as the validation period.
- The training window expands as the evaluation progresses.

This approach preserves the chronological order of time series data and avoids random train-test splitting.

### Evaluation Metrics

Three metrics were used:

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute forecasting error |
| RMSE | Penalizes larger forecasting errors |
| WAPE | Measures total absolute error relative to total actual sales |

WAPE was selected as the primary comparison metric because the dataset contains many zero-sales observations, making MAPE unsuitable.

\[
WAPE = \frac{\sum |Actual - Forecast|}{\sum Actual} \times 100\%
\]

### Overall Model Performance

Results from the rolling validation evaluation:

| Model | MAE | RMSE | WAPE |
|---|---:|---:|---:|
| Random Forest | 9,278.69 | 13,687.81 | **6.80%** |
| Seasonal Naive (7) | 15,722.65 | 23,913.79 | 11.52% |
| Moving Average (7) | 23,174.78 | 32,021.76 | 16.98% |
| Naive | 24,563.75 | 38,205.27 | 18.00% |

### Key Evaluation Findings

- Random Forest achieved the lowest overall MAE, RMSE, and WAPE.
- Random Forest reduced WAPE by approximately **40.98%** compared with Seasonal Naive.
- Random Forest outperformed the other evaluated models in seven out of eight validation folds.
- Its performance was not consistently superior in every fold, indicating that forecasting reliability can vary across different periods.

These results suggest that incorporating historical and temporal features through Random Forest provides better forecasting performance than the evaluated baseline approaches.

---

## 6. Business Insights

Based on the exploratory analysis and model evaluation, several findings can be translated into business considerations.

### 6.1 Weekly Sales Patterns

Historical analysis indicates differences in average sales across days of the week:

- Sunday records the highest average daily sales.
- Thursday records the lowest average daily sales.

**Business implication:**

Operational teams can use recurring weekly patterns as an initial reference when planning staffing, store activities, and operational capacity.

However, these patterns should be monitored over time rather than assumed to remain constant.

### 6.2 Promotional Activities

Exploratory analysis indicates a positive relationship between promotional activities and sales.

**Business implication:**

Promotional activities may contribute to higher sales, but their effectiveness should be evaluated further by comparing sales performance across comparable periods and accounting for other factors such as seasonality and holidays.

Promotions should not automatically be considered the sole cause of increased sales.

### 6.3 Forecasting Performance Across Product Families

Random Forest performance differs across product families.

| Product Family | WAPE |
|---|---:|
| PRODUCE | 3.81% |
| DAIRY | 5.00% |
| BEVERAGES | 6.34% |
| GROCERY I | 6.64% |
| CLEANING | 15.27% |

**Business implication:**

- PRODUCE has the lowest forecasting error among the selected product families.
- CLEANING has the highest forecasting error and requires closer monitoring.
- Forecasting approaches may need to be evaluated separately for different product families rather than assuming one model performs equally well across all categories.

### 6.4 Model Reliability Over Time

Random Forest outperformed the evaluated alternatives in seven of eight validation folds. However, its performance weakened in later validation periods, and Naive performed better in the final fold.

**Business implication:**

Forecasting models should be monitored regularly. Model performance should be reassessed as new sales observations become available, particularly when actual sales begin to diverge from predicted values.

---

## 7. Business Recommendations

Based on the findings, the following recommendations are proposed:

| Area | Recommendation | Expected Business Value |
|---|---|---|
| Operational Planning | Use weekly sales patterns as an initial reference for staffing and operational capacity planning. | Better alignment between operations and expected sales activity. |
| Sales Planning | Use short-term forecasts to support daily and weekly sales planning. | More proactive planning based on expected sales performance. |
| Promotion Evaluation | Monitor sales changes during promotional periods and compare them with suitable non-promotional periods. | Better understanding of promotional effectiveness. |
| Product Family Monitoring | Prioritize forecasting error analysis for product families with higher WAPE, especially CLEANING. | Improved forecasting reliability across categories. |
| Model Monitoring | Periodically compare model forecasts with actual sales and reassess model performance. | Reduced risk of relying on outdated forecasting behavior. |

These recommendations are intended to support decision-making and should be evaluated alongside additional business information before implementation.

---

## 8. Power BI Dashboard

An interactive Power BI dashboard was developed to communicate analytical findings and make forecasting results easier to interpret.

The dashboard consists of four main pages:

### 8.1 Executive Overview

Provides a high-level summary of retail sales performance, including key performance indicators and overall sales trends.

### 8.2 Sales Analysis

Explores historical sales performance across product families and time periods, including weekly patterns and promotional analysis.

### 8.3 Sales Forecast

Displays historical actual sales alongside forecasted sales, allowing users to examine expected short-term sales behavior.

**Dashboard file:** `dashboard/power bi/retail-sales-forecasting_dashboard.pbix`
**Dashboard source:** https://docs.google.com/spreadsheets/d/1w0zjZTuxiwEv-IVWhKkjnXfDaaZ2Y9XlBl1DiJA6nJ4/edit?usp=sharing

---

## 9. Technology Stack

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Evaluation | MAE, RMSE, WAPE |
| Development Environment | VS Code, Jupyter Notebook |
| Business Intelligence | Microsoft Power BI |
| Version Control | Git, GitHub |

---

## 10. Project Structure

```text
End-to-end-Retail-Sales-Forecasting-Project/
│
├── dashboard/
│   └── power bi/
│       ├── README.txt
│       └── retail-sales-forecasting_dashboard.pbix
│
├── data/
│   ├── dashboard/
│   │   ├── demand_forecast.csv
│   │   ├── historical_sales.csv
│   │   └── validation_predictions.csv
│   │
│   └── processed/
│       ├── daily_family_sales.csv
│       ├── final_forecast.csv
│       ├── forecasting_features.csv
│       ├── rolling_validation_metrics.csv
│       ├── rolling_validation_metrics_by_family.csv
│       ├── rolling_validation_metrics_by_fold.csv
│       └── validation_predictions.csv
│
├── models/
│   ├── best_rf_params.json
│   ├── final_random_forest.joblib
│   └── model_metadata.json
│
├── notebooks/
│   ├── 01_data-understanding.ipynb
│   ├── 02_feature-engineering.ipynb
│   ├── 03_baseline-forecasting.ipynb
│   └── 04_random_forest_model.ipynb
│
├── reports/
│   ├── EDA/
│   └── baseline-forecasting/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── evaluation.py
│   └── forecasting.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

Note: Original raw Kaggle datasets are excluded from the repository. The structure above focuses on the files used for analysis, modeling, and dashboard development.

---

## 11. How to Run the Project

### Prerequisites

- Python 3.11
- Git
- Jupyter Notebook or VS Code
- Microsoft Power BI Desktop (for dashboard exploration)

### Installation

Clone the repository:

```bash
git clone https://github.com/wvynngnce/End-to-end-Retail-Sales-Forecasting-Project.git
cd End-to-end-Retail-Sales-Forecasting-Project
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Dataset Preparation

1. Download the original dataset from [Kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data).
2. Extract the required raw dataset files.
3. Place them in the local `data/` directory.
4. Run the notebooks in numerical order to understand the analysis and modeling workflow.

### Dashboard

Open the Power BI file:

```text
dashboard/power bi/retail-sales-forecasting_dashboard.pbix
```

If necessary, update the CSV data source paths in Power BI to match your local directory.

---

## 12. Limitations and Future Improvements

Although Random Forest achieved the best overall performance among the evaluated models, several improvements could be explored:

- **Advanced Time Series Models:** Compare Random Forest with XGBoost, LightGBM, Prophet, and other forecasting approaches.
- **External Variables:** Incorporate holiday, oil price, transaction, and store-level information into the forecasting pipeline.
- **Granular Forecasting:** Extend the analysis from aggregated product-family sales to store-level or product-level forecasting.
- **Model Monitoring:** Implement automated performance tracking and periodic model retraining.
- **Forecast Explainability:** Apply feature importance or SHAP to better understand the factors influencing predictions.
- **Advanced Optimization:** Connect sales forecasts with inventory planning and supply chain optimization in a future project.

---

## 13. Conclusion

This project demonstrates an end-to-end data science workflow for retail sales forecasting, from data exploration and feature engineering to machine learning evaluation and business intelligence visualization.

Random Forest achieved an overall WAPE of **6.80%**, outperforming the evaluated baseline models and providing a useful foundation for short-term sales planning.

Beyond model performance, the analysis highlights differences in weekly sales patterns, promotional activity, and forecasting reliability across product families.

The project illustrates how historical retail data can be transformed into predictive insights and communicated through an interactive dashboard to support more informed business decisions.

---

**Author:** Muhammad Arif Fadhillah  
**Field:** Industrial Engineering | Data Science | Machine Learning | Supply Chain Analytics
