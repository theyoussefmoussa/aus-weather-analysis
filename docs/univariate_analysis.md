# Univariate Analysis

## What's Actually Done In Univariate Analysis
- Plots used: histogram, bar chart, horizontal bar chart, pie chart
- Investigated each column individually to understand its distribution and value counts
- Highlighted the most frequent value (highest bar) in every plot for quick visual reference
- All figures saved to `output/univariate_analysis/` as `.png` files

---

## Key Findings Per Column

### Location
- `Canberra` has the highest number of records (**2,250+**), followed by `Sydney` and `Perth`
- Most locations fall between **1,750 and 2,250** observations
- Only 3 locations have between **1,000 and 1,750** observations
- The dataset is **reasonably balanced across locations**, no single city dominates overwhelmingly

### MinTemp / MaxTemp
- `MinTemp` peaks at **12°C** (8,000+ observations); most values fall between **7°C and 16°C**
- `MaxTemp` peaks at **20°C** (11,000+ observations); most values fall between **16°C and 27°C**
- Both distributions are **approximately bell-shaped**, with rare occurrences at extremes (sub-zero for MinTemp, above 31°C for MaxTemp)

### Rainfall
- **Highly right-skewed**, confirming the zero-inflation behavior discussed during cleaning
- The overwhelming majority of observations fall in the **0–25mm** bin (~100,000 records)
- Rainfall above **50mm** is extremely rare

### Evaporation
- Most values fall between **0–5mm** (25,000+ observations), declining sharply after **9mm**
- Values above **17mm** are extremely rare
- Distribution shape supports using **IterativeImputer** with related columns rather than a fixed value

### Sunshine
- Peaks at **11 hours/day** (~5,000 observations)
- **0 hours** is also common (~3,500 observations), reflecting fully overcast days
- Confirms this column has a genuine bimodal-leaning pattern (clear days vs overcast days), not just missing-data artifacts

### WindGustDir / WindDir9am / WindDir3pm
- `WindGustDir`: **West (W)** is the most frequent direction (~12,000 observations)
- `WindDir9am`: **North (N)** is most frequent (~9,000), followed by `NW`
- `WindDir3pm`: **Southeast (SE)** is most frequent (8,000+), followed by `W`
- All three show a **relatively balanced spread** across the 16 directions, with only minor skew toward dominant directions per time of day

### WindGustSpeed / WindSpeed9am / WindSpeed3pm
- `WindGustSpeed` peaks in the **37–45 km/h** range (~25,000 observations); sharp decline above 45 km/h, rare beyond 80 km/h
- `WindSpeed9am` peaks in the **13–20 km/h** range (~30,000 observations)
- `WindSpeed3pm` peaks in the **9–13 km/h** range (~22,500 observations)
- Wind speed is generally **higher at gust level than at fixed times of day**, as expected

### Humidity9am / Humidity3pm
- `Humidity9am` peaks between **65–75%** (10,000+ observations), left-skewed toward high humidity — mornings are typically humid
- `Humidity3pm` peaks between **50–65%** (~10,000 observations), slightly right-skewed
- Humidity is **consistently lower in the afternoon than in the morning**, matching expected diurnal patterns

### Pressure9am / Pressure3pm
- Both distributions are **approximately normal**, centered around **1017–1018 hPa**
- Values below 1005 hPa or above 1030 hPa are rare in both
- Afternoon pressure is **slightly shifted lower** compared to morning

### Cloud9am / Cloud3pm
- `Cloud9am` peaks at **6 oktas** (31,000+ observations) — moderate-to-heavy cloud cover dominates mornings
- `Cloud3pm` peaks at **5 oktas** (31,000+ observations), with **0 oktas (clear sky)** being the least common afternoon state
- Both confirm that fully clear skies are relatively uncommon in this dataset

### Temp9am / Temp3pm
- `Temp9am` peaks around **15°C** (~14,000 observations), concentrated in **10–22°C**
- `Temp3pm` peaks around **20°C** (14,000+ observations), concentrated in **15–28°C**, shifted higher than the morning reading — consistent with daytime warming

### RainToday / RainTomorrow
- Both are **imbalanced binary targets**: approximately **77.8% No / 22.2% Yes** (~3.5:1 ratio)
- This imbalance is consistent between `RainToday` and `RainTomorrow`, as expected since one is largely derived from the other

---

## Notes on Handling Imbalanced Data

> - The target variable is **moderately imbalanced**, with approximately **77.8%** of observations belonging to the **"No Rain"** class and **22.2%** to the **"Rain"** class (≈ 3.5:1 ratio).
> - Always use a **stratified train-test split** to preserve the original class distribution in both the training and testing sets.
> - **Accuracy alone is not a reliable evaluation metric** for imbalanced classification problems. Instead, evaluate models using:
>   - Precision
>   - Recall
>   - F1-Score
>   - ROC-AUC
>   - Confusion Matrix
> - Before applying any resampling technique, train a **baseline model** to establish a performance benchmark.
> - If the model performs poorly on the minority class (e.g., low recall for rainy days), consider using **class weights** (`class_weight='balanced'`) instead of modifying the dataset.
> - If class weighting is insufficient, apply **SMOTE (Synthetic Minority Over-sampling Technique)** to generate synthetic samples for the minority class.
> - **Random undersampling** should generally be avoided unless the dataset is very large, as it removes potentially useful information from the majority class.
> - Always compare model performance **before and after** applying imbalance-handling techniques to ensure that they provide a genuine improvement.

---

## Not Done Yet
- Bivariate analysis — relationship between each feature and `RainTomorrow`
- Correlation heatmap across numerical columns
- Geographic comparison — how distributions vary by `Location`
- Time-based patterns (seasonal trends), if any temporal signal becomes available

## Notes
- `highlight_max_bar()` is applied consistently across all histogram/bar plots to visually flag the most frequent value
- Color scheme: one fixed color for all histograms (`HIST_COLOR`), a separate fixed color for all categorical bar charts (`BAR_COLOR`), and a two-tone palette for binary pie charts (`PIE_COLORS`), replacing the previous Tokyo Night–styled visuals for a more neutral, presentation-ready look