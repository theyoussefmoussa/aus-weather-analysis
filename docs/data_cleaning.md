## What's Actually Done in Data Cleaning
--------------------------
1. Remove identifier column `row ID`
2. Drop duplicates — 30 rows
3. Fill `MinTemp` & `MaxTemp` with median based on `Location` (not every area has the same temperature)
4. Fill `Rainfall` with median based on `Location`
5. `Evaporation` has 42% missing values, so filling with median isn't the solution since this would break the natural variance in the data — this will be imputed from other related columns in the data preprocessing stage instead
6. `Sunshine` has 47% missing values, same reasoning as `Evaporation` — deferred to preprocessing
7. `WindGustDir` has 16 directions (North, South, West, East, West North, South North, West North West, etc.)
    - Filled with mode based on `Location`
    - Converted to `category` instead of `str`
8. `WindGustSpeed` ranges from 6.0 to 135.0, so datatype will be `float32`
    - Filled with median based on `Location`
9. `WindSpeed9am` & `WindSpeed3pm` filled with median based on `Location`
10. `Humidity9am` & `Humidity3pm` filled with median based on `Location`
11. `Pressure9am` & `Pressure3pm` filled with median based on `Location`
12. `Temp9am` & `Temp3pm` filled with median based on `Location`
13. `WindDir9am` missing value percentage is 7.01%, filled with mode based on `Location`
14. `WindDir3pm` missing value percentage is 2.63%, filled with mode based on `Location`
15. `Cloud3pm` missing values percentage is 40.78% — found a strange row with `Cloud3pm == 9`, but based on the Oktas scale valid values range from 0 to 8, so this value was converted to `NaN` before imputation
16. `Cloud9am` & `Cloud3pm` filled with median based on `Location`, then rounded to preserve valid integer Oktas values before downcasting
17. `RainToday` is derived directly from `Rainfall` (`Rainfall > 1mm` → `Yes`, else `No`) instead of being imputed independently, since `RainToday` is originally derived from `Rainfall` in the first place — this also resolves its missing values
18. For every `Location`-based median/mode fill, a global median/mode fallback is applied afterward, to handle locations where all values for a column were missing (in which case the group median/mode itself returns `NaN`)

### Missing Values Before & After Cleaning
#### Using median for continuous values, mode for categorical values
| ID | Column         | Before | After |
|----|----------------|-------:|------:|
| 0  | Location       | 0      | 0     |
| 1  | MinTemp        | 413    | 0     |
| 2  | MaxTemp        | 202    | 0     |
| 3  | Rainfall       | 977    | 0     |
| 4  | Evaporation    | 42501  | 42501 |
| 5  | Sunshine       | 47287  | 47287 |
| 6  | WindGustDir    | 6491   | 0     |
| 7  | WindGustSpeed  | 6450   | 0     |
| 8  | WindDir9am     | 6976   | 0     |
| 9  | WindDir3pm     | 2618   | 0     |
| 10 | WindSpeed9am   | 905    | 0     |
| 11 | WindSpeed3pm   | 1805   | 0     |
| 12 | Humidity9am    | 1203   | 0     |
| 13 | Humidity3pm    | 2476   | 0     |
| 14 | Pressure9am    | 9718   | 0     |
| 15 | Pressure3pm    | 9706   | 0     |
| 16 | Cloud9am       | 37542  | 0     |
| 17 | Cloud3pm       | 39972  | 0     |
| 18 | Temp9am        | 584    | 0     |
| 19 | Temp3pm        | 1874   | 0     |
| 20 | RainToday      | 977    | 0     |
| 21 | RainTomorrow   | 0      | 0     |

---

## Datatypes Optimization

| ID | Column         | Original Type | Optimized Type |
|----|----------------|---------------|-----------------|
| 0  | Location       | str           | category        |
| 1  | MinTemp        | float64       | float32         |
| 2  | MaxTemp        | float64       | float32         |
| 3  | Rainfall       | float64       | float32         |
| 4  | Evaporation    | float64       | float32         |
| 5  | Sunshine       | float64       | float32         |
| 6  | WindGustDir    | str           | category        |
| 7  | WindGustSpeed  | float64       | float32         |
| 8  | WindDir9am     | str           | category        |
| 9  | WindDir3pm     | str           | category        |
| 10 | WindSpeed9am   | float64       | float32         |
| 11 | WindSpeed3pm   | float64       | float32         |
| 12 | Humidity9am    | float64       | float32         |
| 13 | Humidity3pm    | float64       | float32         |
| 14 | Pressure9am    | float64       | float32         |
| 15 | Pressure3pm    | float64       | float32         |
| 16 | Cloud9am       | float64       | Int8            |
| 17 | Cloud3pm       | float64       | Int8            |
| 18 | Temp9am        | float64       | float32         |
| 19 | Temp3pm        | float64       | float32         |
| 20 | RainToday      | str           | category        |
| 21 | RainTomorrow   | int64         | bool            |

Memory usage before: 17.5 MB
Memory usage after: 7.0 MB

---

## Not Done Yet
- `Evaporation` & `Sunshine` (42% / 47% missing) — will be imputed using `IterativeImputer` in the preprocessing stage, using related columns (`MaxTemp`, `MinTemp`, `Humidity9am/3pm`, `WindSpeed9am/3pm`)
- Outlier handling — deferred; tree-based models (LightGBM) handle outliers natively, so this may not require explicit treatment

## Notes
- All `Location`-based fills use a two-step approach: group median/mode first, then a global fallback for locations where a column was missing entirely
- `RainToday` is fully derived from `Rainfall` rather than imputed independently, since it removes the missing values while staying logically consistent with the rainfall amount