from src.utils import separator
from src.data_cleaning import data_cleaning
from src.univariate_analysis import univariate_analysis
from src.bivariate_analysis import bivariate_analysis
from src.data_preprocessing import data_preprocessing
from src.feature_engineering import feature_engineering
from src.model import train_model
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