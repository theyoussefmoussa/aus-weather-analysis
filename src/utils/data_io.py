import os
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split


def save_dataset(df, output_path, name, file_extension='parquet'):
    saving_path = f"{output_path}/{name}.{file_extension}"
    if isinstance(df, pd.Series):
        df = df.to_frame()
    if file_extension == "parquet":
        df.to_parquet(saving_path)


def load_and_split_data():
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")

    # Load preprocessed + feature-engineered data
    X_train = pd.read_parquet(f"{BASE_PATH}/data/final/X_train_final.parquet")
    X_test = pd.read_parquet(f"{BASE_PATH}/data/final/X_test_final.parquet")
    y_train = pd.read_parquet(f"{BASE_PATH}/data/final/y_train_final.parquet")
    y_test = pd.read_parquet(f"{BASE_PATH}/data/final/y_test_final.parquet")
    y_train = y_train.iloc[:, 0]
    y_test = y_test.iloc[:, 0]

    # Stratified split for early stopping validation
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.2, stratify=y_train, random_state=42
    )

    # Class imbalance correction
    neg, pos = y_tr.value_counts()[False], y_tr.value_counts()[True]
    scale_pos_weight = neg / pos

    return X_tr, X_val, y_tr, y_val, X_train, y_train, X_test, y_test, scale_pos_weight