# Australia Weather Analysis

Predicting next-day rainfall in Australia using historical weather data - a Classification project (Rain Tomorrow: Yes/No).

Collaborating with [Mohamed Farag](https://github.com/themohamedfarag)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-black?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-black?logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)

---

## Project Phases

| Phase | Status | Done By |
|------|:------:|------|
| Problem Definition | Done | Mohamed Farag |
| Data Understanding | Done | Mohamed Farag |
| Data Cleaning | Done | Youssef Moussa |
| Exploratory Data Analysis (Univariate Analysis) | Done | Youssef Moussa |
| Bivariate Analysis | Done | Youssef Moussa |
| Data Preprocessing | Done | Mohamed Farag |
| Feature Engineering | Done | Mohamed Farag |
| Modeling | Done | Youssef Moussa |
| Evaluation | Done | Mohamed Farag |
| Deployment | Done | Mohamed Farag |

---

## Project Structure

```text
my-project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
├── docs/
│   ├── problem_definition.md
│   ├── data_understanding.md
│   ├── data_cleaning.md
│   ├── univariate_analysis.md
│   ├── bivariate_analysis.md
│   ├── data_preprocessing.md
│   ├── feature_engineering.md
│   ├── model_train.md
│   └── evaluation.md
├── notebooks/
│   ├── 01_problem_definition.ipynb
│   ├── 02_data_understanding.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_univariate_analysis.ipynb
│   ├── 05_bivariate_analysis.ipynb
│   ├── 06_data_preprocessing.ipynb
│   ├── 07_feature_engineering.ipynb
│   ├── 08_modeling.ipynb
│   └── 09_evaluation.ipynb
├── src/
│   ├── bivariate_analysis.py
│   ├── compare_models.py
│   ├── data_cleaning.py
│   ├── data_preprocessing.py
│   ├── evaluate.py
│   ├── feature_engineering.py
│   ├── predict.py
│   ├── train_final_model.py
│   ├── train_model.py
│   ├── tune_model.py
│   ├── univariate_analysis.py
│   └── utils/
│       ├── constants.py
│       ├── core.py
│       ├── data_io.py
│       ├── feature_helpers.py
│       └── plotting.py
├── models/
│   ├── lgbm_baseline.pkl
│   └── lgbm_tuned.pkl
├── outputs/
│   ├── univariate_analysis/
│   └── bivariate_analysis/
├── app/
│   └── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

## Getting Started

Clone the repo:

```bash
git clone https://github.com/theyoussefmoussa/aus-weather-analysis.git
cd aus-weather-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up your environment variables (create a `.env` file):

```env
BASE_PATH=/path/to/your/data
```

Run the full pipeline:

```bash
python main.py
python3 main.py # if you are linux user like Moussa
```

Run the Streamlit application:

```bash
python -m streamlit run app/app.py
```

---

## Model Performance

Two LightGBM models were trained and evaluated: a **Baseline** model and a **Tuned** model.

Final test-set results:

| Metric | Baseline | Tuned |
|---|:---:|:---:|
| Accuracy | 0.813238 | 0.814645 |
| Precision | 0.556017 | 0.555304 |
| Recall | 0.838068 | 0.879222 |
| F1-Score | 0.668510 | 0.680693 |
| PR-AUC | 0.779255 | 0.807236 |
| ROC-AUC | 0.908311 | 0.922616 |
| Best Iteration | 302 | 730 |
| Non-zero Features | 124 | 126 |

The **Tuned LightGBM model** was selected as the final model, as it performed better overall — especially in PR-AUC, ROC-AUC, Recall, and F1-Score.

The final model artifact is:

```text
models/lgbm_tuned.pkl
```

---

## Evaluation

Evaluation was performed on the held-out test set and included:

- Accuracy
- Precision
- Recall
- F1-Score
- PR-AUC
- ROC-AUC
- Model comparison
- Feature importance analysis

The Tuned model has 126 non-zero features. The top important features include:

- PressureDiff
- Pressure3pm
- TempRange
- TempChange
- TempHumidityInteraction
- Sunshine
- HumidityDiff
- MinTemp
- WindGustSpeed
- Evaporation

---

## Deployment

The final Tuned LightGBM model was integrated into a prediction pipeline.

Prediction logic is implemented in:

```text
src/predict.py
```

The Streamlit application is:

```text
app/app.py
```

The prediction pipeline:

1. Receives weather input from the user.
2. Encodes categorical variables.
3. Encodes RainToday.
4. Creates the required engineered features.
5. Aligns the input with the model's 126 expected features.
6. Calculates the probability of rain tomorrow.
7. Returns a Yes/No prediction.

The application was tested locally and is working successfully.

Start the application with:

```bash
python -m streamlit run app/app.py
```

---

## Contact Us

**Youssef Moussa**

[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/theyoussefmoussa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa)
[![X](https://img.shields.io/badge/X-black?logo=x&logoColor=white)](https://x.com/theyosefmusa)

**Mohamed Farag**

[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/themohamedfarag)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-farag-37105134b/)