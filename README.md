# Retail Sales Forecasting & Analytics

**Short-Term Retail Sales Forecasting Using Machine Learning and Power BI**

An end-to-end data science project that analyzes historical retail sales and predicts short-term sales across selected product families using a Random Forest Regressor.

The project covers data exploration, feature engineering, baseline forecasting, machine learning, rolling-origin validation, recursive forecasting, and interactive business intelligence visualization using Power BI.

## Project Overview

Accurate sales forecasting helps retail businesses understand sales patterns, anticipate future revenue, and support better operational and planning decisions.

This project uses historical sales data from the Corporación Favorita Grocery Sales Forecasting dataset to develop a machine learning model for predicting sales over a 7-day horizon.

The original dataset contains sales records across multiple stores and product families. For this project, store-level records are aggregated to create daily sales data for five selected product families.

## Objectives

- Explore historical retail sales patterns.
- Perform data cleaning and preprocessing.
- Develop time-based features for machine learning.
- Establish baseline forecasting models.
- Train and evaluate a Random Forest forecasting model.
- Compare model performance using rolling-origin validation.
- Generate recursive 7-day sales forecasts.
- Identify sales trends and product family performance.
- Present analytical results through an interactive Power BI dashboard.

## Dataset

**Source:** Corporación Favorita Grocery Sales Forecasting  
**Platform:** Kaggle  
**Dataset Period:** January 2013 – August 2017

Selected product families:

- GROCERY I
- BEVERAGES
- PRODUCE
- CLEANING
- DAIRY

The original transaction-level data is aggregated across stores to produce daily sales by product family.

The target variable is `sales`, representing the monetary value of sales in USD.

## Methodology

### 1. Data Preparation

- Load and inspect the original dataset.
- Aggregate store-level sales by date and product family.
- Handle missing values and duplicate records.
- Convert date columns into appropriate datetime formats.
- Prepare separate datasets for historical analysis and model development.

### 2. Exploratory Data Analysis

Analyze:

- Historical sales trends.
- Sales distribution by product family.
- Weekly sales patterns.
- Zero-sales observations.
- Promotional sales patterns.
- Product family contribution to total sales.

### 3. Feature Engineering

**Time-based features:**

- Day of week
- Day of month
- Month
- Year

**Lag features:**

- Lag 1
- Lag 7
- Lag 14
- Lag 28

**Rolling features:**

- 7-day rolling mean
- 28-day rolling mean

Rolling features are shifted by one period to prevent target leakage.

### 4. Baseline Models

Three baseline forecasting approaches are implemented:

- Naive Forecasting
- Moving Average Forecasting (7-day)
- Seasonal Naive Forecasting (7-day)

These models provide reference points for evaluating the performance of the machine learning model.

### 5. Machine Learning Model

A Random Forest Regressor is developed using:

- One-hot encoding for product family.
- Calendar features.
- Lag features.
- Rolling statistical features.

The model uses recursive forecasting for multi-step predictions, where each predicted value is incorporated into subsequent forecasting steps.

### 6. Model Evaluation

Model performance is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Weighted Absolute Percentage Error (WAPE)

WAPE is selected as the primary evaluation metric because the dataset contains zero-sales observations, making MAPE unsuitable.

An expanding-window rolling-origin validation approach is implemented with:

- 8 validation folds.
- 7 days per validation fold.
- Chronological training and validation periods.
- Expanding training windows.

This approach evaluates model performance across multiple historical periods while preserving temporal order.

## Results

### Overall Model Performance

| Model | MAE | RMSE | WAPE |
|---|---:|---:|---:|
| Random Forest | 9,278.69 | 13,687.81 | 6.80% |
| Seasonal Naive (7) | 15,722.65 | 23,913.79 | 11.52% |
| Moving Average (7) | 23,174.78 | 32,021.76 | 16.98% |
| Naive | 24,563.75 | 38,205.27 | 18.00% |

### Key Findings

- Random Forest achieved the lowest overall WAPE of **6.80%**.
- Random Forest reduced WAPE by approximately **40.98%** compared with Seasonal Naive.
- Random Forest outperformed the other models in **7 out of 8 validation folds**.
- PRODUCE achieved the lowest product-family WAPE at **3.81%**.
- CLEANING had the highest product-family WAPE at **15.27%**, indicating greater forecasting difficulty.

### Validation Considerations

The evaluation uses eight chronological validation windows, each covering seven days.

Model hyperparameters should be selected using training-only tuning windows, independently of the final validation folds. The reported metrics represent historical validation performance and should not be interpreted as a guarantee of future forecasting accuracy.

WAPE is calculated as the sum of absolute prediction errors divided by the sum of actual sales, multiplied by 100.

## Power BI Dashboard

The project uses Microsoft Power BI as the primary business intelligence and visualization platform.

The dashboard consists of four main pages:

### 1. Executive Overview

Provides a high-level summary of retail sales performance through:

- Total Historical Sales
- Average Daily Sales
- Total Forecast Sales
- Best-performing Product Family
- Historical Sales Trends
- Sales Contribution by Product Family
- Automated Business Insights

### 2. Sales Analysis

Explores historical sales patterns through:

- Daily and monthly sales trends.
- Sales distribution by product family.
- Weekly sales patterns.
- Promotion vs. non-promotion sales analysis.
- Product family contribution.
- Interactive date and product family filters.

### 3. Sales Forecast

Presents forecasting results through:

- Historical Actual vs. Forecast.
- 7-Day Sales Forecast.
- Forecast by Product Family.
- Forecast Trend Visualization.
- Forecast Summary.

### 4. Model Performance

Evaluates forecasting models through:

- Overall Model Comparison.
- MAE, RMSE, and WAPE.
- Validation Performance by Fold.
- Model Performance by Product Family.
- Actual vs. Predicted Sales.
- Model Evaluation Insights.

## Project Structure

```text
retail-sales-forecasting/
│
├── data/
│   ├── processed/
│   └── dashboard/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_baseline_modeling.ipynb
│   ├── 05_random_forest_modeling.ipynb
│   └── 06_model_evaluation_forecasting.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── forecasting.py
│   └── evaluation.py
│
├── models/
│
├── powerbi/
│   └── retail_sales_dashboard.pbix
│
├── reports/
│   └── figures/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd retail-sales-forecasting
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Dataset

Download the Corporación Favorita Grocery Sales Forecasting dataset from Kaggle.

Place the required source files in:

```text
data/raw/
```

Processed datasets and model outputs are stored in:

```text
data/processed/
```

### 5. Run the Analysis

Open the notebooks in the `notebooks/` directory using Jupyter Notebook or Visual Studio Code.

Execute the notebooks in sequential order to reproduce the data preparation, exploratory analysis, model development, evaluation, and forecasting workflow.

### 6. Open the Power BI Dashboard

Open the Power BI project:

```text
powerbi/retail_sales_dashboard.pbix
```

Update the data source paths if necessary to match your local repository directory.

## Limitations

- The analysis uses aggregated sales across stores rather than store-level forecasting.
- Only five product families are included.
- The dataset ends in August 2017 and does not represent current retail market conditions.
- External factors such as weather, economic conditions, and holidays are not fully incorporated.
- Recursive forecasting may accumulate prediction errors over longer horizons.
- Forecasts are point estimates and do not include prediction intervals.
- Sales value forecasts cannot be directly interpreted as physical inventory quantities.

## Future Improvements

- Incorporate additional external variables and holiday information.
- Evaluate additional machine learning and deep learning forecasting algorithms.
- Explore advanced time-series models.
- Develop prediction intervals to quantify forecasting uncertainty.
- Extend the analysis to store-level forecasting.
- Integrate inventory optimization and replenishment planning.
- Develop automated data pipelines and model monitoring.

## Author

**M. Arif Fadhillah**

Industrial Engineering Graduate  
Universitas Islam Indonesia

Interested in Data Science, Machine Learning, Optimization, and Supply Chain Analytics.#   E n d - t o - e n d - R e t a i l - S a l e s - F o r e c a s t i n g - P r o j e c t  
 