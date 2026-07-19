import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
def data_cleaning():
    # Load Data 
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")
    OUTPUT_PATH = f"{BASE_PATH}/data/processed/clean_weather_training_data.parquet"
    df = pd.read_csv(f"{BASE_PATH}/data/raw/weather_training_data.csv")

    # Drop Identifier Column 
    df.drop(columns=['row ID'], inplace=True)


    # Drop Duplicates
    df = df.drop_duplicates()

    # Range of Cloud According to Oktas from 0 to 8
    df.loc[df['Cloud3pm'] == 9.0, 'Cloud3pm'] = np.nan

    # Filling Missing Values With Median
    numerical_columns = ['MaxTemp', 'MinTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity3pm', 'Humidity9am', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']
    for col in numerical_columns: 
        df[col] = df.groupby('Location')[col].transform(
        lambda x: x.fillna(x.median())
    )
        df[col] = df[col].fillna(df[col].median())   # global fallback


    # Filling Wind Directions With Mode 
    df['WindGustDir'] = df.groupby('Location')['WindGustDir'].transform(
        lambda x: x.fillna(x.mode()[0] if not x.mode().empty else x)
    )

    global_mode = df['WindGustDir'].mode()[0]
    df['WindGustDir'] = df['WindGustDir'].fillna(global_mode)

    # Filling Columns with Mode
    categorical_columns = ['WindDir9am', 'WindDir3pm', 'RainToday']
    for col in categorical_columns: 
        df[col] = df.groupby('Location')[col].transform(
            lambda x: x.fillna(x.mode()[0] if not x.mode().empty else x)
    )

    cloud_columns = ['Cloud9am', 'Cloud3pm']
    for col in cloud_columns:
        df[col] = df.groupby('Location')[col].transform(
            lambda x: x.fillna(x.median())
        )
        df[col] = df[col].fillna(df[col].median()) # fallback for locations where all values were NaN (median() returns NaN too)

    # Must run after Rainfall is fully imputed above, since RainToday is derived from it
    df['RainToday'] = np.where(df['Rainfall'] > 1, 'Yes', 'No')


    # Downcasting Datatypes to Float32 for Continuous Value Columns
    continuous_columns = df.select_dtypes(include='float').columns
    df[continuous_columns] = df[continuous_columns].astype('float32')


    # Downcast Clouds to int8
    clouds_columns = ['Cloud9am', 'Cloud3pm']

    for cloud in clouds_columns:
        df[cloud] = df[cloud].round()  # round first: astype('Int8') truncates instead of rounding
        df[cloud] = df[cloud].astype('Int8')

    # Downcast Str to Category
    str_columns = df.select_dtypes(include='str').columns
    for col in str_columns: 
        df[col] = df[col].astype('category')

    # Downcast Rain Tomorrow to Boolean Value
    df['RainTomorrow'] = df['RainTomorrow'].astype('bool')

    # Save New Dataset
    df.to_parquet(OUTPUT_PATH, engine='pyarrow')
    print("Done: data_cleaning.py")
    print("New Dataset Saved in: data/processed/clean_weather_training_data.parquet")

if __name__ == "__main__": 
    data_cleaning()