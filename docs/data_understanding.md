# 🔍 Data Understanding

## Overview

In this phase, the Australian Weather dataset was inspected to understand its structure, features, and data quality before starting EDA and data preprocessing.

The analysis was performed in:

`notebooks/data_understanding.ipynb`

---

## Dataset Loading

The following datasets were loaded:

- Weather Training Data
- Weather Test Data

The training dataset contains the target variable:

`RainTomorrow`

while the test dataset is used for future predictions.

---

## Data Inspection

The following operations were performed:

- Displayed the first rows of the dataset using `head()` to understand the data format.
- Checked dataset size using `shape`.
- Checked columns, data types, and missing values using `info()`.
- Generated statistical summaries using `describe()`.

---

## Feature Analysis

The dataset contains:

### Numerical Features

Examples:

- Temperature values
- Rainfall
- Humidity
- Wind speed
- Atmospheric pressure

### Categorical Features

Examples:

- Location
- Wind direction
- Rain indicators

---

## Target Variable

The target variable:

`RainTomorrow`

represents whether it will rain the next day.

It is a binary variable:

- Yes
- No

The class distribution was checked to understand the prediction problem.

---

## Missing Values

Missing values were analyzed using:

`isnull().sum()`

The purpose was to identify incomplete features and understand the data quality.

Missing values handling was not performed in this phase and was left for the Data Cleaning stage.

---
## Data Understanding Findings

Based on the initial analysis, the following observations were identified:

- The dataset contains both numerical and categorical weather features.
- The target variable `RainTomorrow` makes the problem a binary classification task.
- Weather conditions are represented using different measurements such as temperature, rainfall, humidity, wind, and pressure.
- The dataset contains missing values in several features, which indicates that a data cleaning step is required before model training.
- Some features are categorical, such as `Location` and wind directions, which will require encoding during preprocessing.
- The dataset contains multiple weather observations collected from different locations across Australia.

These observations will guide the next phases, including Exploratory Data Analysis, Data Cleaning, and Preprocessing.


## Conclusion

The Data Understanding phase provided an overview of:

- Dataset structure
- Feature types
- Target variable
- Data quality issues

The dataset is ready for the next phase:

**Exploratory Data Analysis (EDA)**