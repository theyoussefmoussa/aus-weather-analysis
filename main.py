from src.utils import separator
from src.data_cleaning import data_cleaning
from src.univariate_analysis import univariate_analysis
from src.bivariate_analysis import bivariate_analysis
from data_preprocessing import preprocessing
if __name__ == "__main__": 
    print("Starting Phases")
    separator(title="Data Cleaning")
    data_cleaning()
    separator("Univariate Analysis")
    univariate_analysis()
    separator(title="Bivariate Analysis")
    bivariate_analysis()
    separator("Data Preprocessing")
    preprocessing()