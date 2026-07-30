## What's Actually Done

- **Train/test split** performed before any fitting step, using `stratify=y` (given the 77.8/22.2 class imbalance from EDA) and `train_size=0.8`, `random_state=42`
- **One-hot encoding** (`Location`, `WindGustDir`, `WindDir9am`, `WindDir3pm`) via `OneHotEncoder(handle_unknown='ignore')`, **fit on `X_train` only**, then `.transform()`-applied to both `X_train` and `X_test` using the same fitted encoder instance — no leakage from test into the fit
- **`RainToday`** mapped to binary (`No` → 0, `Yes` → 1), applied independently to `X_train` and `X_test`
- **Downcasting**: one-hot encoded columns (originally `float64` from `OneHotEncoder` output) cast to `uint8` on both splits
- All transformation logic (encode → map → downcast) consolidated into a single `transform()` helper, called once per split, so train/test always go through identical steps in identical order
- Output saved via shared `save_dataset()` utility in `src/utils.py`; `y_train`/`y_test` (pandas Series) converted to single-column DataFrames before saving, since `Series` has no native `.to_parquet()`

## Key Findings / Decisions

- **`Sunshine` and `Evaporation` are being kept**, not dropped, despite 42–47% missingness. Reasoning: bivariate analysis found real signal (`Sunshine` vs `Cloud3pm`: -0.65, `Sunshine` vs `Humidity3pm`: -0.63), and the target model (LightGBM) handles NaNs natively via learned split-direction, so imputing or dropping isn't necessary to make the columns usable
- **No scaling applied** — tree-based models are scale-invariant, so this step is intentionally skipped
- **No `IterativeImputer`** used anywhere in this phase — deferred/rejected in favor of letting LightGBM handle missingness natively, avoiding an extra fit-on-train/transform-on-test surface
- Model choice (LightGBM) is currently an **assumption carried from EDA**, not yet formally confirmed with the team — several preprocessing decisions (no scaling, no imputation, kept correlated features) depend on this holding

## Not Done Yet

- **Missing-indicator flags** for `Sunshine`/`Evaporation` (e.g. `Sunshine_missing`, `Evaporation_missing`) — discussed as a good addition alongside keeping the raw columns, not yet implemented in code
- **Domain validation checks** (`MinTemp > MaxTemp`, `Temp9am/3pm` outside `MinTemp`–`MaxTemp` range) — still pending from the Data Cleaning handoff,