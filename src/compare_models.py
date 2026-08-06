import joblib as job
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score
from dotenv import load_dotenv
import os
from src.utils import load_and_split_data


def compare_models(model_paths):
    """
    Compare multiple saved LightGBM models on the held-out test set.
    model_paths: dict of {display_name: filename_in_models_dir}
    """
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")

    _, _, _, _, _, _, X_test, y_test, _ = load_and_split_data()

    results = []
    for name, filename in model_paths.items():
        model = job.load(f"{BASE_PATH}/models/{filename}")
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        results.append({
            'Model': name,
            'PR-AUC': average_precision_score(y_test, y_pred_proba),
            'ROC-AUC': roc_auc_score(y_test, y_pred_proba),
            'Best Iteration': model.best_iteration_,
            'Non-zero Features': (model.feature_importances_ > 0).sum(),
        })

    comparison = pd.DataFrame(results)
    print(comparison.to_string(index=False))

    return comparison


if __name__ == "__main__":
    compare_models({
        'Baseline': 'lgbm_baseline.pkl',
        'Tuned': 'lgbm_tuned.pkl',
    })