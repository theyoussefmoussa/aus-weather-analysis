from src.utils import separator
from src.data_cleaning import data_cleaning
from src.univariate_analysis import univariate_analysis
from src.bivariate_analysis import bivariate_analysis
from src.data_preprocessing import data_preprocessing
from src.feature_engineering import feature_engineering
from src.train_model import train_model
from src.train_final_model import train_final_model
from src.utils import BEST_PARAMS

if __name__ == "__main__":
    print("Starting Phases")
    separator(title="Data Cleaning")
    data_cleaning()
    separator("Univariate Analysis")
    univariate_analysis()
    separator(title="Bivariate Analysis")
    bivariate_analysis()
    separator("Data Preprocessing")
    data_preprocessing()
    separator(title="Feature Engineering")
    feature_engineering()
    separator(title="Model Training")
    train_model()
    separator(title="Final Model Training (Tuned)")
    train_final_model(best_params=BEST_PARAMS)