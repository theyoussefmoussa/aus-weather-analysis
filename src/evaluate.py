import os
import joblib
import pandas as pd

from dotenv import load_dotenv
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    average_precision_score,
    roc_auc_score,
    confusion_matrix,
)


def load_test_data():
    """Load the final held-out test dataset."""
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")

    X_test = pd.read_parquet(
        f"{BASE_PATH}/data/final/X_test_final.parquet"
    )

    y_test = pd.read_parquet(
        f"{BASE_PATH}/data/final/y_test_final.parquet"
    )

    y_test = y_test.iloc[:, 0]

    return X_test, y_test


def load_model(filename):
    """Load a trained model from the models directory."""
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")

    return joblib.load(
        f"{BASE_PATH}/models/{filename}"
    )


def evaluate_model(model, X_test, y_test):
    """Evaluate a classification model on the held-out test set."""

    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = model.predict(X_test)

    results = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-Score": f1_score(y_test, y_pred),
        "PR-AUC": average_precision_score(y_test, y_proba),
        "ROC-AUC": roc_auc_score(y_test, y_proba),
    }

    return results


def get_confusion_matrix(model, X_test, y_test):
    """Return the confusion matrix for a classification model."""

    y_pred = model.predict(X_test)

    return confusion_matrix(y_test, y_pred)


def evaluate_saved_model(filename):
    """Load and evaluate a saved model."""

    X_test, y_test = load_test_data()
    model = load_model(filename)

    results = evaluate_model(
        model,
        X_test,
        y_test
    )

    return results


if __name__ == "__main__":
    baseline_results = evaluate_saved_model(
        "lgbm_baseline.pkl"
    )

    tuned_results = evaluate_saved_model(
        "lgbm_tuned.pkl"
    )

    print("\nBaseline Model:")
    for metric, value in baseline_results.items():
        print(f"{metric}: {value:.4f}")

    print("\nTuned Model:")
    for metric, value in tuned_results.items():
        print(f"{metric}: {value:.4f}")