# Australia Weather Analysis

Predicting next-day rainfall in Australia using historical weather data — a Classification project (Rain Tomorrow: Yes/No).

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
|------|----:|------|
| Problem Definition | Done | Mohamed Farag |
| Data Understanding | Done | Mohamed Farag |
| Data Cleaning & Preprocessing | In Progress | Youssef Moussa |

---

## Project Structure

```text
my-project/
├── data/
│   ├── raw/
│   └── processed/
│   └── final/
├── docs/
│   └── data_understanding.md
│   └── problem_definition.md
├── notebooks/
│   └── 01_problem_definition.ipynb
│   └── 02_data_understanding.ipynb
│   └── 03_data_cleaning.ipynb
│   └── 04_data_preprocessing.ipynb
│   └── 05_feature_engineering.ipynb
│   └── 06_modeling.ipynb
│   └── 07_evaluation.ipynb
├── src/
│   ├── __init__.py
│   ├── evaluate.py
│   ├── feature_engineering.py
│   └── train.py
│   └── utils.py
├── models/
├── outputs/
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

Run the notebooks in order (`01` → `07`) inside `notebooks/`, or run the full pipeline:

```bash
python main.py
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