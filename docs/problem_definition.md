# 🌦️ Australian Weather Prediction

## Problem Definition

The goal of this project is to predict whether it will rain tomorrow in Australia using historical weather observations and Machine Learning techniques.

This project follows the CRISP-DM methodology, starting from understanding the problem and preparing the data for the modeling phase.

## Business Problem

Accurate rainfall prediction can support decision-making in different fields:

- Agriculture
- Transportation
- Disaster Management
- Water Resource Planning

## Machine Learning Problem

This project is a Binary Classification problem.

### Target Variable:
- `RainTomorrow`

### Input Features:
Weather observations such as:

- Temperature
- Rainfall
- Humidity
- Wind conditions
- Atmospheric pressure
- Location

### Output:

- Yes → Rain tomorrow
- No → No rain tomorrow

## Dataset

The dataset contains two files:

- `Weather Training Data.csv`
  - Contains historical weather data with the target variable `RainTomorrow`.

- `Weather Test Data.csv`
  - Contains weather data without the target variable and is used for prediction.