
import pandas as pd

from src.config import (
    HISTORICAL_DATA_PATH,
    FORECAST_DATA_PATH,
    ROLLING_METRICS_PATH,
    FAMILY_METRICS_PATH,
    FOLD_METRICS_PATH,
    VALIDATION_PREDICTIONS_PATH
)


def load_historical_data(path=HISTORICAL_DATA_PATH):
    """Load historical sales and feature data."""

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])

    required_columns = {"date", "family", "sales"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Historical data is missing columns: {missing}"
        )

    return df


def load_forecast_data(path=FORECAST_DATA_PATH):
    """Load final sales forecasting results."""

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])

    required_columns = {"date", "family", "prediction"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Forecast data is missing columns: {missing}"
        )

    return df


def load_rolling_metrics(path=ROLLING_METRICS_PATH):
    """Load overall rolling validation metrics."""

    return pd.read_csv(path)


def load_family_metrics(path=FAMILY_METRICS_PATH):
    """Load rolling validation metrics by product family."""

    return pd.read_csv(path)


def load_fold_metrics(path=FOLD_METRICS_PATH):
    """Load rolling validation metrics by fold."""

    return pd.read_csv(path)


def load_validation_predictions(path=VALIDATION_PREDICTIONS_PATH):
    """Load actual and predicted sales during validation."""

    df = pd.read_csv(path)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df
