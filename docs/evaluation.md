# Evaluation Phase

## Objective

Evaluate and compare the Baseline and Tuned LightGBM models on the held-out test set.

The evaluation focuses on classification performance, ranking quality, and the effect of the tuning process.

---

## Evaluation Dataset

The models were evaluated using the held-out test dataset generated during the Data Preprocessing and Feature Engineering phases.

- Test samples: 19,897
- Features: 126
- Target: `RainTomorrow`
- Task: Binary Classification

The test set was kept separate from the hyperparameter tuning process to provide an unbiased final evaluation.

---

## Evaluation Metrics

The following metrics were used:

### Accuracy

Measures the overall percentage of correct predictions.

### Precision

Measures how many of the predicted rainy days were actually rainy.

### Recall

Measures how many of the actual rainy days were correctly identified.

### F1-Score

Provides a balance between Precision and Recall.

### PR-AUC

Measures the model's ability to distinguish the positive class across different classification thresholds.

PR-AUC is particularly useful for this project because the target variable is imbalanced.

### ROC-AUC

Measures the model's ability to rank positive examples above negative examples across different thresholds.

---

## Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | PR-AUC | ROC-AUC |
|------|---------:|---------:|--------:|---------:|--------:|--------:|
| Baseline | 0.813238 | 0.556017 | 0.838068 | 0.668510 | 0.779255 | 0.908311 |
| Tuned | 0.814645 | 0.555304 | 0.879222 | 0.680693 | 0.807236 | 0.922616 |

---

## Results

The Tuned LightGBM model achieved better overall performance than the Baseline model.

The most important improvements were:

- PR-AUC increased from `0.779255` to `0.807236`.
- ROC-AUC increased from `0.908311` to `0.922616`.
- Recall increased from `0.838068` to `0.879222`.
- F1-Score increased from `0.668510` to `0.680693`.
- Accuracy increased slightly from `0.813238` to `0.814645`.

Precision remained almost unchanged, with a small decrease from `0.556017` to `0.555304`.

---

## Feature Importance

Feature importance was analyzed using the tuned LightGBM model.

The top features included:

1. `PressureDiff`
2. `Pressure3pm`
3. `TempRange`
4. `TempChange`
5. `TempHumidityInteraction`
6. `Sunshine`
7. `HumidityDiff`
8. `MinTemp`
9. `WindGustSpeed`
10. `Evaporation`

The feature importance analysis helps identify which weather variables contribute most to the model's predictions.

---

## Final Model Selection

The Tuned LightGBM model was selected as the final model because it consistently outperformed the Baseline model on the main evaluation metrics.

The tuned model was saved as:

`models/lgbm_tuned.pkl`

It is used by the prediction module and the Streamlit deployment application.

---

## Deployment Validation

After evaluation, the final model was integrated into the prediction pipeline.

The Streamlit application was tested locally and successfully:

- Loaded the trained LightGBM model.
- Loaded the required environment variables.
- Prepared user input.
- Generated the required engineered features.
- Matched the input features with the model's 126 expected features.
- Generated a probability prediction.
- Returned a final `Rain Tomorrow: Yes/No` prediction.

---

## Conclusion

The evaluation results show that hyperparameter tuning improved the LightGBM model's ability to identify rainfall events.

The Tuned model achieved:

- PR-AUC: `0.807236`
- ROC-AUC: `0.922616`
- Recall: `0.879222`
- F1-Score: `0.680693`

Based on these results, the Tuned LightGBM model was selected for deployment.