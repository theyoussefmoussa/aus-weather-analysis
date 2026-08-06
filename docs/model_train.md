# Modeling Phase

## What's Actually Done

- Loaded preprocessed + feature-engineered data from `data/final/` (`X_train`, `X_test`, `y_train`, `y_test`)
- Converted `y_train`/`y_test` from single-column DataFrame to Series (`RainTomorrow`, bool)
- Refactored data loading + split into `load_and_split_data()` in `src/utils.py`, shared across baseline, tuning, and final model training
- Stratified train/validation split (80/20) on `X_train`/`y_train` for early stopping, `random_state=42`
- Computed `scale_pos_weight` (neg/pos ratio on `y_tr`) to correct for class imbalance
- Trained baseline LightGBM (`LGBMClassifier`, `objective='binary'`, `n_estimators=1000`, `metric='average_precision'`, early stopping at 50 rounds)
- Evaluated baseline on held-out test set using PR-AUC and ROC-AUC (probability-based, not the default 0.5-threshold classification report)
- Saved baseline model artifact via `joblib` to `models/lgbm_baseline.pkl`
- Ran hyperparameter tuning with Optuna (`TPESampler`, 75 trials, Bayesian optimization) over `num_leaves`, `learning_rate`, `max_depth`, `min_child_samples`, `subsample`, `colsample_bytree`, `reg_alpha`, `reg_lambda`; scored on validation PR-AUC, test set left untouched during tuning
- Reviewed hyperparameter importance and optimization history (see Key Findings)
- Trained final tuned LightGBM with best params from Optuna, evaluated once on held-out test set
- Saved tuned model artifact via `joblib` to `models/lgbm_tuned.pkl`
- Integrated baseline + tuned training into `main.py` pipeline (`src/train_model.py`, `src/train_final_model.py`), with `best_params` hardcoded from the tuning run
- Re-checked feature importance on the tuned model specifically for `RainToday`/`RainfallLog` (previously zero-importance on baseline) — confirmed they are **not** zero-importance under the tuned hyperparameters (see Key Findings)
- Built side-by-side comparison of baseline vs. tuned on the test set (PR-AUC, ROC-AUC, best iteration, non-zero feature count)

## Key Findings

- Baseline test set results:
  - PR-AUC: 0.7553
  - ROC-AUC: 0.8933
  - Best iteration: 302
  - Non-zero features: 124/126 (`RainToday`, `RainfallLog` at/near zero importance under default hyperparameters)
- Tuned test set results:
  - PR-AUC: 0.7613
  - ROC-AUC: 0.8962
  - Best iteration: 730
  - Non-zero features: 126/126 (all features contribute; `RainToday` importance 50, `RainfallLog` importance 625)
- Hyperparameter importance: `learning_rate` (0.64) and `num_leaves` (0.25) account for ~89% of tuning impact; `max_depth` (0.07) minor; `subsample`, `colsample_bytree`, `min_child_samples`, `reg_alpha`, `reg_lambda` all negligible (<0.01 each)
- Optimization history: most of the gain happened in the first ~20 trials (0.738 → 0.7536); remaining ~55 trials produced only marginal improvement (0.7536 → 0.7544) — future tuning runs could narrow the search space to `learning_rate`/`num_leaves` and cut trial count significantly
- **`RainToday`/`RainfallLog` importance is hyperparameter-dependent, not a fixed property of the features.** Under baseline defaults they contribute nothing; under the tuned config (lower `learning_rate`, higher `num_leaves`, ~2.4x more boosting rounds) they become meaningfully predictive. No features were dropped from either model — both baseline and tuned were trained on the full 126-feature set; the "zero importance" was an emergent property of the baseline's hyperparameters, not a deliberate exclusion.
- Tuned model outperforms baseline on both metrics; improvement is modest (~0.6% PR-AUC) but consistent across both metrics

## Not Done Yet

- Final model selection between baseline and tuned artifacts (pending discussion with Mohamed) — comparison table ready
- Evaluation and Deployment phases

## Notes

- Original modeling work was lost due to a fresh Ubuntu install without committing. Data pipeline (cleaning, feature engineering, preprocessing) was unaffected since it was already committed; only the modeling step had to be rebuilt.
- `early_stopping_rounds` as a direct `.fit()` argument is deprecated in the current LightGBM version — must use `callbacks=[lgb.early_stopping(...)]`.
- `eval_set` argument itself is also flagged as deprecated in favor of `eval_X`/`eval_y` (warning only, not yet migrated).
- `metric` should be set explicitly on `LGBMClassifier` (not just passed to `.fit()`), otherwise LightGBM also tracks its own default metric (`binary_logloss`) alongside the one specified in `.fit()`.
- `verbose=-1` added to suppress `[LightGBM] [Info]` startup logging, per project convention (minimal terminal output).
- `optuna.visualization` requires `plotly` as a separate dependency (not bundled); installed and added to `requirements.txt`.
- Tuning (`tune_model.py`) is intentionally excluded from `main.py` — it's an exploratory step run once to discover `best_params`, not part of the repeatable pipeline. Only the final training step with hardcoded `best_params` runs on every `main.py` execution.
- Earlier project notes (pre-data-loss) referenced dropping `RainToday`/`RainfallLog` as "confirmed not bugs" — this is superseded by the finding above; no drop was implemented in the rebuilt pipeline, and the current data shows the decision to drop would have been hyperparameter-specific, not a general property of these features.