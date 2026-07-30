import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from src.utils import save_dataset
import sys
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)

def data_preprocessing():
    # Loading Data
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")
    OUTPUT_PATH = f"{BASE_PATH}/data/processed/"

    df = pd.read_parquet(
        f"{BASE_PATH}/data/processed/clean_weather_training_data.parquet"
    )

    # Drop columns that has missing values above 50% 
    # df.drop(columns=['Sunshine', 'Evaporation'], inplace=True)

    # Encoding Categorical Variables
    onehot_cols = ["Location", "WindGustDir", "WindDir9am", "WindDir3pm"]

    # Selecting Features and Target
    X = df.drop(columns=["RainTomorrow"])
    y = df["RainTomorrow"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y,
        stratify=y,
        train_size=0.8,
        random_state=42

    )

    # Fit encoder on train only
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoder.fit(X_train[onehot_cols])

    def transform(X, encoder, onehot_cols, rain_today_map):
        # Encode categorical columns (transform only - no fitting here)
        encoded = encoder.transform(X[onehot_cols])
        encoded_df = pd.DataFrame(
            encoded,
            columns=encoder.get_feature_names_out(onehot_cols),
            index=X.index
        )
        X = pd.concat([X, encoded_df], axis=1)
        X = X.drop(columns=onehot_cols)

        # Encode RainToday
        X['RainToday'] = X['RainToday'].map(rain_today_map)

        # Downcast encoded columns
        numeric_cols = X.select_dtypes(include='float64').columns
        X[numeric_cols] = X[numeric_cols].astype('uint8')

        return X

    rain_today_map = {"No": 0, "Yes": 1}

    X_train = transform(X_train, encoder, onehot_cols, rain_today_map)
    X_test = transform(X_test, encoder, onehot_cols, rain_today_map)


    # Saving New Dataset
    saved_datasets = {
    "X_train": X_train,
    "X_test": X_test,
    "y_train": y_train,
    "y_test": y_test,
}
    for name, dataset in saved_datasets.items():
        save_dataset(dataset, output_path=OUTPUT_PATH, name=name)
    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test :", y_test.shape)
    print("Proccessed Dataset Saved Successfully in data/processed")

if __name__ == "__main__":
    data_preprocessing()