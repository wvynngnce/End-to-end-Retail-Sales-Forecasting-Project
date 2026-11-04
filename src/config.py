
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Main directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORT_DIR / "figures"

# Data files
HISTORICAL_DATA_PATH = (
    PROCESSED_DATA_DIR / "forecasting_features.csv"
)

FORECAST_DATA_PATH = (
    PROCESSED_DATA_DIR / "final_forecast.csv"
)

# Model files
MODEL_PATH = MODEL_DIR / "random_forest_final.joblib"
BEST_PARAMS_PATH = MODEL_DIR / "best_rf_params.json"

# Forecast configuration
FORECAST_HORIZON = 7
RANDOM_STATE = 42

# Evaluation data files
ROLLING_METRICS_PATH = (
    PROCESSED_DATA_DIR / "rolling_validation_metrics.csv"
)

FAMILY_METRICS_PATH = (
    PROCESSED_DATA_DIR / "rolling_validation_metrics_by_family.csv"
)

FOLD_METRICS_PATH = (
    PROCESSED_DATA_DIR / "rolling_validation_metrics_by_fold.csv"
)

VALIDATION_PREDICTIONS_PATH = (
    PROCESSED_DATA_DIR / "validation_predictions.csv"
)
