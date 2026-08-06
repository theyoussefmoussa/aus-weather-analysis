import joblib as job
import os
from dotenv import load_dotenv
import lightgbm as lgb
from lightgbm import LGBMClassifier
from sklearn.metrics import average_precision_score, roc_auc_score
from src.utils import load_and_split_data


def train_final_model(best_params):
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")

    X_tr, X_val, y_tr, y_val, X_train, y_train, X_test, y_test, scale_pos_weight = load_and_split_data()

    clf = LGBMClassifier(
        objective='binary',
        metric='average_precision',
        scale_pos_weight=scale_pos_weight,
        n_estimators=1000,
        random_state=42,
        verbose=-1,
        **best_params
    )

    clf.fit(
        X_tr, y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric='average_precision',
        callbacks=[lgb.early_stopping(stopping_rounds=50), lgb.log_evaluation(period=50)]
    )

    y_pred_proba = clf.predict_proba(X_test)[:, 1]
    pr_auc = average_precision_score(y_test, y_pred_proba)
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    print(f"Test PR-AUC: {pr_auc:.4f}")
    print(f"Test ROC-AUC: {roc_auc:.4f}")

    job.dump(clf, f"{BASE_PATH}/models/lgbm_tuned.pkl")
    print("Model saved in models/lgbm_tuned.pkl")

    return clf