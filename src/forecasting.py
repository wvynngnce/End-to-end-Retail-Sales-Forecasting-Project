
import numpy as np
import pandas as pd


def recursive_forecast(model, train_data, forecast_dates):
    """
    Generate multi-step recursive forecasts.

    Predictions from previous forecast dates are used
    as lag features for subsequent predictions.
    """

    predictions = []

    families = train_data["family"].unique()

    for family in families:

        history = (
            train_data[train_data["family"] == family]
            .sort_values("date")["sales"]
            .tolist()
        )

        if len(history) < 28:
            raise ValueError(
                f"Insufficient history for family: {family}"
            )

        for forecast_date in forecast_dates:

            row = pd.DataFrame([{
                "family": family,
                "day_of_week": forecast_date.dayofweek,
                "day_of_month": forecast_date.day,
                "month": forecast_date.month,
                "year": forecast_date.year,
                "lag_1": history[-1],
                "lag_7": history[-7],
                "lag_14": history[-14],
                "lag_28": history[-28],
                "rolling_mean_7": np.mean(history[-7:]),
                "rolling_mean_28": np.mean(history[-28:])
            }])

            prediction = model.predict(row)[0]

            prediction = max(0, prediction)

            predictions.append({
                "date": forecast_date,
                "family": family,
                "prediction": prediction
            })

            history.append(prediction)

    return pd.DataFrame(predictions)
