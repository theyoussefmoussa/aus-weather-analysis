# Modeling Phase

## What's Actually Done

- Loaded preprocessed + feature-engineered data from `data/final/` (`X_train`, `X_test`, `y_train`, `y_test`)
- Converted `y_train`/`y_test` from single-column DataFrame to Series (`RainTomorrow`, bool)
- Stratified train/validation split (80/20) on `X_train`/`y_train` for early stopping, `random_state=42`
- Computed `scale_pos_weight` (neg/pos ratio on `y_tr`) to correct for class imbalance
- Trained baseline LightGBM (`LGBMClassifier`, `objective='binary'`, `n_estimators=1000`, `metric='average_precision'`, early stopping at 50 rounds)
- Evaluated on held-out test set using PR-AUC and ROC-AUC (probability-based, not the default 0.5-threshold classification report)
- Saved model artifact via `joblib` to `models/lgbm_baseline.pkl`

## Key Findings

- Best iteration: 302 (early stopped after 350, patience 50 rounds)
- Test set results:
  - PR-AUC: 0.7553
  - ROC-AUC: 0.8933
- Results are close to and slightly better than the original baseline run (PR-AUC 0.749, ROC-AUC 0.891) — treated as within normal run-to-run variance

## Not Done Yet

- Hyperparameter tuning
- Feature importance review and drop of zero-importance features (`RainToday`, `RainfallLog` — confirmed zero importance in earlier run, not yet re-verified on this rebuild)
- Final model selection (pending with Mohamed)
- Evaluation and Deployment phases

## Notes

- Original modeling work was lost due to a fresh Ubuntu install without committing. Data pipeline (cleaning, feature engineering, preprocessing) was unaffected since it was already committed; only the modeling step had to be rebuilt.
- `early_stopping_rounds` as a direct `.fit()` argument is deprecated in the current LightGBM version — must use `callbacks=[lgb.early_stopping(...)]`.
- `eval_set` argument itself is also flagged as deprecated in favor of `eval_X`/`eval_y` (warning only, not yet migrated).
- `metric` should be set explicitly on `LGBMClassifier` (not just passed to `.fit()`), otherwise LightGBM also tracks its own default metric (`binary_logloss`) alongside the one specified in `.fit()`.
- `verbose=-1` added to suppress `[LightGBM] [Info]` startup logging, per project convention (minimal terminal output).