import pandas as pd
import joblib as job
import lightgbm as lgb
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, average_precision_score
from dotenv import load_dotenv
import os


def train_model():
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

    clf = LGBMClassifier(
        objective='binary',
        scale_pos_weight=scale_pos_weight,
        n_estimators=1000,
        metric='average_precision',
        verbose=-1,
        random_state=42
    )
    clf.fit(
        X_tr, y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric='average_precision',
        callbacks=[lgb.early_stopping(stopping_rounds=50), lgb.log_evaluation(period=50)]
    )

    # Evaluate on held-out test set
    y_pred_proba = clf.predict_proba(X_test)[:, 1]
    pr_auc = average_precision_score(y_test, y_pred_proba)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    print(f"PR-AUC: {pr_auc:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")

    job.dump(clf, f"{BASE_PATH}/models/lgbm_baseline.pkl")
    print("Model saved in models/lgbm_baseline.pkl")

    return clf


if __name__ == "__main__":
    train_model()