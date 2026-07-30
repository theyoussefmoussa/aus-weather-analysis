## What's Actually Done

**Engineered features** (all built via generic helper functions parameterized by column name, applied identically to `X_train` and `X_test` through a single `add_features()` call per split — no per-split code duplication):

| Feature | Formula | Rationale |
|---|---|---|
| `TempRange` | `MaxTemp - MinTemp` | Daily temperature spread |
| `TempChange` | `Temp3pm - Temp9am` | How much temperature shifted through the day |
| `AverageTemp` | `(Temp9am + Temp3pm) / 2` | Single daily temperature summary |
| `HumidityDiff` | `Humidity3pm - Humidity9am` | Daily humidity shift |
| `AverageHumidity` | `(Humidity9am + Humidity3pm) / 2` | Single daily humidity summary |
| `TempHumidityInteraction` | `AverageTemp * AverageHumidity` | Exploratory interaction term — not physically motivated, left for the model to weigh |
| `PressureDiff` | `Pressure3pm - Pressure9am` | Pressure drop is a known precursor to rainfall |
| `AveragePressure` | `(Pressure9am + Pressure3pm) / 2` | Single daily pressure summary |
| `WindSpeedDiff` | `WindSpeed3pm - WindSpeed9am` | Daily wind speed shift |
| `AverageWindSpeed` | `(WindSpeed9am + WindSpeed3pm) / 2` | Single daily wind summary |
| `PressureWindInteraction` | `AveragePressure * AverageWindSpeed` | Exploratory interaction term — same caveat as `TempHumidityInteraction`, no confirmed physical basis |
| `RainfallLog` | `log1p(Rainfall)` | Compresses the long right tail from zero-inflated, skewed `Rainfall`; low-impact for LightGBM specifically (scale-invariant splits) but kept as a "why not" addition alongside the raw column |

**Downcasting:** all `float64` columns (newly engineered + any leftover from preprocessing) cast to `float32`; `RainToday` explicitly cast to `uint8` regardless of its incoming dtype, since it was found to persist as `int64` from `preprocessing.py`'s `.map()` output.

**Refactor note:** feature-creation logic was restructured from per-feature loops over `[X_train, X_test]` into generic, reusable functions (`diff`, `average`, `interaction`, `log_transform`) that take column names as parameters. These live in `src/utils.py` since they're generic; `downcast()` stays local to this script since it hardcodes dataset-specific column names (`RainToday`).

## Key Findings / Decisions

- `TempHumidityInteraction` and `PressureWindInteraction` are **not** based on a known meteorological relationship — they're generic interaction terms, included to let the model use them if useful, not as validated domain insights. Worth treating with skepticism relative to the diff/average features, which do have physical grounding.
- Checked `MinTemp == MaxTemp` rows: 7 out of 79,587 (~0.01%) — negligible, not investigated further.
- Confirmed no scaling applied at this stage either — consistent with the LightGBM assumption carried from preprocessing.

## Notes

- Output filenames changed from `X_train`/`X_test`/`y_train`/`y_test` to `X_train_final`/`X_test_final`/`y_train_final`/`y_test_final` in this phase's save step — **differs from Preprocessing's naming** (`data/processed/X_train.parquet`, no `_final` suffix). Flagging since downstream Modeling code will need to load the `_final`-suffixed names from `data/final/`, not the unsuffixed names — worth confirming this was intentional before Modeling starts, to avoid a path/name mismatch.