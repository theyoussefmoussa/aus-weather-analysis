# Feature Engineering

## Overview

This stage creates new informative features from the original weather variables to improve machine learning model performance.

---

## Objectives

- Increase predictive power.
- Capture hidden relationships between variables.
- Generate interaction features.

---

## Engineered Features

### Temperature Features

#### Temperature Range

```
TempRange = MaxTemp - MinTemp
```

Measures daily temperature variation.

---

#### Temperature Change

```
TempChange = Temp3pm - Temp9am
```

Measures temperature variation during the day.

---

#### Average Temperature

```
AverageTemp = (Temp9am + Temp3pm) / 2
```

Represents the average daytime temperature.

---

### Humidity Features

#### Humidity Difference

```
HumidityDiff = Humidity3pm - Humidity9am
```

Measures humidity variation throughout the day.

---

#### Average Humidity

```
AverageHumidity = (Humidity9am + Humidity3pm) / 2
```

---

### Pressure Features

#### Pressure Difference

```
PressureDiff = Pressure3pm - Pressure9am
```

---

#### Average Pressure

```
AveragePressure = (Pressure9am + Pressure3pm) / 2
```

---

### Wind Features

#### Wind Speed Difference

```
WindSpeedDiff = WindSpeed3pm - WindSpeed9am
```

---

#### Average Wind Speed

```
AverageWindSpeed = (WindSpeed9am + WindSpeed3pm) / 2
```

---

### Interaction Features

#### Temperature × Humidity

```
TempHumidityInteraction =
AverageTemp × AverageHumidity
```

Captures the combined effect of temperature and humidity.

---

#### Pressure × Wind

```
PressureWindInteraction =
AveragePressure × AverageWindSpeed
```

Captures the relationship between atmospheric pressure and wind speed.

---

### Rainfall Transformation

#### Log Transformation

```
RainfallLog = log(1 + Rainfall)
```

Reduces the skewness of rainfall values.

---

## Final Dataset

Number of Features after Feature Engineering:

```
124 Features
```

Training Shape:

```
(79,587, 124)
```

Testing Shape:

```
(19,897, 124)
```

---

## Summary

A total of **12 new engineered features** were created to enrich the dataset and provide additional information for the machine learning models.