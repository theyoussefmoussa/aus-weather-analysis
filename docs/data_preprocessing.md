# Data Preprocessing

## Overview

This stage prepares the cleaned dataset for machine learning by converting it into a numerical format suitable for model training.

---

## Objectives

- Convert categorical variables into numerical representations.
- Split the dataset into training and testing sets.
- Save the processed datasets for the next stage of the pipeline.

---

## Steps Performed

### 1. Load Clean Dataset

Loaded the cleaned dataset from:

```
data/processed/clean_weather_training_data.parquet
```

---

### 2. Convert Categorical Columns

Converted categorical data types into strings before encoding.

Categorical columns include:

- Location
- WindGustDir
- WindDir9am
- WindDir3pm
- RainToday

---

### 3. One-Hot Encoding

Applied One-Hot Encoding to all categorical features.

Encoded features include:

- Location
- WindGustDir
- WindDir9am
- WindDir3pm

RainToday was encoded as a binary feature.

---

### 4. Train-Test Split

Split the dataset into:

- 80% Training Data
- 20% Testing Data

Random State:

```
42
```

Target variable:

```
RainTomorrow
```

---

### 5. Save Processed Data

Generated files:

- X_train.parquet
- X_test.parquet
- y_train.parquet
- y_test.parquet

These datasets are used in Feature Engineering and Model Training.

---

## Final Dataset

Training Samples:

```
79,587
```

Testing Samples:

```
19,897
```

Number of Features after preprocessing:

```
112 Features
```

*(before feature engineering)*