import pandas as pd
import sys
from dotenv import load_dotenv
import os

project_root = os.path.abspath('..')
sys.path.insert(0, project_root)
from src.utils import save_dataset, diff, average, interaction, log_transform


def downcast(df):
    numeric_cols = df.select_dtypes(include='float64').columns
    df[numeric_cols] = df[numeric_cols].astype('float32')
    df['RainToday'] = df['RainToday'].astype('uint8')
    return df


def add_features(df):
    df = diff(df, "MaxTemp", "MinTemp", "TempRange")
    df = diff(df, "Temp3pm", "Temp9am", "TempChange")
    df = average(df, "Temp9am", "Temp3pm", "AverageTemp")

    df = diff(df, "Humidity3pm", "Humidity9am", "HumidityDiff")
    df = average(df, "Humidity9am", "Humidity3pm", "AverageHumidity")

    df = interaction(df, "AverageTemp", "AverageHumidity", "TempHumidityInteraction")

    df = diff(df, "Pressure3pm", "Pressure9am", "PressureDiff")
    df = average(df, "Pressure9am", "Pressure3pm", "AveragePressure")

    df = diff(df, "WindSpeed3pm", "WindSpeed9am", "WindSpeedDiff")
    df = average(df, "WindSpeed9am", "WindSpeed3pm", "AverageWindSpeed")

    df = interaction(df, "AveragePressure", "AverageWindSpeed", "PressureWindInteraction")

    df = log_transform(df, "Rainfall", "RainfallLog")

    df = downcast(df)
    return df


def feature_engineering():
    # Load Data
    BASE_PATH = os.getenv("BASE_PATH")
    OUTPUT_PATH = f"{BASE_PATH}/data/final"

    X_train = pd.read_parquet(f"{BASE_PATH}/data/processed/X_train.parquet")
    X_test = pd.read_parquet(f"{BASE_PATH}/data/processed/X_test.parquet")
    y_train = pd.read_parquet(f"{BASE_PATH}/data/processed/y_train.parquet")
    y_test = pd.read_parquet(f"{BASE_PATH}/data/processed/y_test.parquet")

    X_train = add_features(X_train)
    X_test = add_features(X_test)

    print(f"{X_train.memory_usage(deep=True).sum() / 1e6:.1f} MB")
    print(X_train.shape)
    print(X_test.shape)

    saved_datasets = {
        "X_train_final": X_train,
        "X_test_final": X_test,
        "y_train_final": y_train,
        "y_test_final": y_test,
    }
    for name, dataset in saved_datasets.items():
        save_dataset(dataset, output_path=OUTPUT_PATH, name=name)
    print("Datasets Saved in data/final")


if __name__ == "__main__":
    feature_engineering()