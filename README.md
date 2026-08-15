# Australia Weather Analysis

Predicting next-day rainfall in Australia using historical weather data — a binary classification project (Rain Tomorrow: Yes/No).

**[Live App](https://aus-weather-prediction.streamlit.app/)**

Collaborating with [Mohamed Farag](https://github.com/themohamedfarag)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-black?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

---

## Overview

| Phase | Done By |
|---|---|
| Problem Definition, Data Understanding, Feature Engineering, Evaluation, Deployment | Mohamed Farag |
| Data Cleaning, EDA, Preprocessing, Modeling | Youssef Moussa |

Full pipeline: `data/` → `notebooks/` → `src/` → `models/` → `app/app.py`

---

## Getting Started

```bash
git clone https://github.com/theyoussefmoussa/aus-weather-analysis.git
cd aus-weather-analysis
pip install -r requirements.txt
```

Create a `.env` file:

```env
BASE_PATH=/path/to/your/data
```

Run the pipeline:

```bash
python main.py
python3 main.py     # if You Are Linux User Like Moussa 
```

Run the app locally:

```bash
python -m streamlit run app/app.py
python3 -m streamlit run app/app.py     # For Linux
```

---

## Model Performance

Two LightGBM models were trained; the **Tuned** model was selected as final.

| Metric | Baseline | Tuned |
|---|:---:|:---:|
| Accuracy | 0.8132 | 0.8146 |
| Precision | 0.5560 | 0.5553 |
| Recall | 0.8381 | 0.8792 |
| F1-Score | 0.6685 | 0.6807 |
| PR-AUC | 0.7793 | 0.8072 |
| ROC-AUC | 0.9083 | 0.9226 |

Top features: `PressureDiff`, `Pressure3pm`, `TempRange`, `TempChange`, `TempHumidityInteraction`, `Sunshine`, `HumidityDiff`.

Final model artifact: `models/lgbm_tuned.pkl`

---

## Contact

**Youssef Moussa** — [GitHub](https://github.com/theyoussefmoussa) · [LinkedIn](https://linkedin.com/in/theyoussefmoussa) · [X](https://x.com/theyosefmusa)

**Mohamed Farag** — [GitHub](https://github.com/themohamedfarag) · [LinkedIn](https://www.linkedin.com/in/mohamed-farag-37105134b/)