
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def calculate_metrics(y_true, y_pred):
    """
    Calculate MAE, RMSE, and WAPE.

    WAPE is expressed as a percentage.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    mae = mean_absolute_error(y_true, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y_true, y_pred)
    )

    total_actual = np.sum(np.abs(y_true))

    if total_actual == 0:
        wape = np.nan
    else:
        wape = (
            np.sum(np.abs(y_true - y_pred))
            / total_actual
        ) * 100

    return {
        "MAE": mae,
        "RMSE": rmse,
        "WAPE (%)": wape
    }
