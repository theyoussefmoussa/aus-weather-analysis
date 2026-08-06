import optuna
from lightgbm import LGBMClassifier
from sklearn.metrics import average_precision_score
import lightgbm as lgb


def objective(trial, X_tr, y_tr, X_val, y_val, scale_pos_weight):
    params = {
        'objective': 'binary',
        'metric': 'average_precision',
        'scale_pos_weight': scale_pos_weight,
        'n_estimators': 1000,
        'random_state': 42,
        'verbose': -1,
        'num_leaves': trial.suggest_int('num_leaves', 15, 255),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'max_depth': trial.suggest_int('max_depth', 3, 12),
        'min_child_samples': trial.suggest_int('min_child_samples', 5, 100),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True),
    }

    clf = LGBMClassifier(**params)
    clf.fit(
        X_tr, y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric='average_precision',
        callbacks=[lgb.early_stopping(stopping_rounds=50, verbose=False)]
    )

    y_pred_proba = clf.predict_proba(X_val)[:, 1]
    return average_precision_score(y_val, y_pred_proba)


def tune_model(X_tr, y_tr, X_val, y_val, scale_pos_weight, n_trials=75):
    study = optuna.create_study(direction='maximize', sampler=optuna.samplers.TPESampler(seed=42))
    study.optimize(
        lambda trial: objective(trial, X_tr, y_tr, X_val, y_val, scale_pos_weight),
        n_trials=n_trials,
        show_progress_bar=True
    )

    print(f"Best PR-AUC (validation): {study.best_value:.4f}")
    print(f"Best params: {study.best_params}")

    return study