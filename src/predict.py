import os
import joblib
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

BASE_PATH = os.getenv("BASE_PATH")

MODEL_PATH = f"{BASE_PATH}/models/lgbm_tuned.pkl"


# Load trained model once
model = joblib.load(MODEL_PATH)

MODEL_FEATURES = model.feature_name_


def predict_weather(input_data):
    """
    Predict whether it will rain tomorrow.

    input_data:
        Dictionary containing weather features.

    Returns:
        prediction: "Yes" or "No"
        probability: probability of rain tomorrow
    """

    # Convert input dictionary to DataFrame
    df = pd.DataFrame([input_data])

    # One-hot encode categorical variables
    categorical_columns = [
        "Location",
        "WindGustDir",
        "WindDir9am",
        "WindDir3pm",
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns,
        dtype=int
    )

    # Encode RainToday
    if "RainToday" in df.columns:
        df["RainToday"] = df["RainToday"].map({
            "No": 0,
            "Yes": 1,
            0: 0,
            1: 1
        })

    # Create engineered features
    if "MinTemp" in df.columns and "MaxTemp" in df.columns:
        df["TempRange"] = df["MaxTemp"] - df["MinTemp"]

    if "Temp3pm" in df.columns and "Temp9am" in df.columns:
        df["TempChange"] = df["Temp3pm"] - df["Temp9am"]

    if "MinTemp" in df.columns and "MaxTemp" in df.columns:
        df["AverageTemp"] = (
            df["MinTemp"] + df["MaxTemp"]
        ) / 2

    if "Humidity9am" in df.columns and "Humidity3pm" in df.columns:
        df["HumidityDiff"] = (
            df["Humidity3pm"] - df["Humidity9am"]
        )

        df["AverageHumidity"] = (
            df["Humidity9am"] + df["Humidity3pm"]
        ) / 2

        df["TempHumidityInteraction"] = (
            df["Temp3pm"] * df["Humidity3pm"]
        )

    if "Pressure9am" in df.columns and "Pressure3pm" in df.columns:
        df["PressureDiff"] = (
            df["Pressure3pm"] - df["Pressure9am"]
        )

        df["AveragePressure"] = (
            df["Pressure9am"] + df["Pressure3pm"]
        ) / 2

    if "WindSpeed9am" in df.columns and "WindSpeed3pm" in df.columns:
        df["WindSpeedDiff"] = (
            df["WindSpeed3pm"] - df["WindSpeed9am"]
        )

        df["AverageWindSpeed"] = (
            df["WindSpeed9am"] + df["WindSpeed3pm"]
        ) / 2

    if "Pressure3pm" in df.columns and "WindSpeed3pm" in df.columns:
        df["PressureWindInteraction"] = (
            df["Pressure3pm"] * df["WindSpeed3pm"]
        )

    if "Rainfall" in df.columns:
        import numpy as np
        df["RainfallLog"] = np.log1p(df["Rainfall"])

    # Make sure every model feature exists
    for feature in MODEL_FEATURES:
        if feature not in df.columns:
            df[feature] = 0

    # Remove unexpected columns
    df = df[MODEL_FEATURES]

    # Predict probability
    probability = model.predict_proba(df)[0, 1]

    # Classification threshold
    prediction = "Yes" if probability >= 0.5 else "No"

    return prediction, probability