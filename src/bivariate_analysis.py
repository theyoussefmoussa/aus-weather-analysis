import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from dotenv import load_dotenv
import sys
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)

from src.utils import set_labels, violinplot, save_fig, crosstab_barchart

def bivariate_analysis():
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")
    OUTPUT_PATH = f"{BASE_PATH}/outputs/bivariate_analysis"
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/clean_weather_training_data.parquet")


    # Heatmap correlation
    numeric_cols = df.select_dtypes(include=['float32', 'Int8']).columns
    corr_matrix = df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap='coolwarm',
        center=0,
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        square=True
    )
    set_labels("Feature Correlation Heatmap")
    plt.tight_layout()
    save_fig(fig, f"{OUTPUT_PATH}/heatmap_correlation.png")

    # Numerical vs Target
    # MinTemp vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'MinTemp')
    plt.yticks(range(-10,40,5))
    save_fig(fig, f"{OUTPUT_PATH}/min_temp_vs_rain_tomorrow.png")

    # MaxTemp vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'MaxTemp')
    plt.yticks(range(-5, 50, 5))
    save_fig(fig, f"{OUTPUT_PATH}/max_temp_vs_rain_tomorrow.png")

    # Rainfall vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Rainfall')
    plt.ylim(0, 20)
    plt.yticks(range(0, 20, 2))
    save_fig(fig, f"{OUTPUT_PATH}/rainfall_vs_rain_tomorrow.png")

    # Evaporation vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Evaporation')
    plt.ylim(0, 20)
    plt.yticks(range(0, 20, 2))
    save_fig(fig, f"{OUTPUT_PATH}/evaporations_vs_rain_tomorrow.png")

    # Sunshine vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Sunshine')
    save_fig(fig, f"{OUTPUT_PATH}/sunshine_vs_rain_tomorrow.png")

    # Wind Speed vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'WindGustSpeed')
    plt.yticks(range(0, 150, 10))
    save_fig(fig, f"{OUTPUT_PATH}/windspeed_vs_rain_tomorrow.png")

    # Wind Speed at 9am vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'WindSpeed9am')
    plt.ylim(0, 40)
    save_fig(fig, f"{OUTPUT_PATH}/windspeed_9am_vs_rain_tomorrow.png")


    # Wind Speed at 3pm vs Rain Tomorrow
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'WindSpeed3pm')
    plt.ylim(0, 45)
    save_fig(fig, f"{OUTPUT_PATH}/windspeed_3pm_vs_rain_tomorrow.png")

    # Humidity at 9 am 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Humidity9am')
    plt.yticks(range(0, 110, 10))
    save_fig(fig, f"{OUTPUT_PATH}/humidity_9am_vs_rain_tomorrow.png")


    # Humidity at 3 pm 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Humidity3pm')
    plt.yticks(range(0, 110, 10))
    save_fig(fig, f"{OUTPUT_PATH}/humidity_3pm_vs_rain_tomorrow.png")


    # Pressure at 9 am 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Pressure9am')
    save_fig(fig, f"{OUTPUT_PATH}/pressure_9am_vs_rain_tomorrow.png")


    # Pressure at 3 pm 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Pressure3pm')
    save_fig(fig, f"{OUTPUT_PATH}/pressure_3pm_vs_rain_tomorrow.png")


    # Clouds at 9 am 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Cloud9am')
    save_fig(fig, f"{OUTPUT_PATH}/cloud_9am_vs_rain_tomorrow.png")


    # Clouds at 3 pm 
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Cloud3pm')
    save_fig(fig, f"{OUTPUT_PATH}/cloud_3pm_vs_rain_tomorrow.png")

    # Temp at 9am
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Temp9am')
    save_fig(fig, f"{OUTPUT_PATH}/temp_9am_vs_rain_tomorrow.png")

    # Temp at 3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    violinplot(df, 'Temp3pm')
    save_fig(fig, f"{OUTPUT_PATH}/temp_3pm_vs_rain_tomorrow.png")


    # Categorical vs Target

    # Rain Today vs Rain Tomorrow
    fig = crosstab_barchart(df, 'RainToday')
    save_fig(fig, f"{OUTPUT_PATH}/rain_today_vs_rain_tomorrow.png")

    # Location vs Rain Tomorrow
    fig = crosstab_barchart(df, 'Location', 'barh', figsize=(12, 10))
    save_fig(fig, f"{OUTPUT_PATH}/location_vs_rain_tomorrow.png")

    # Wind Direction vs Rain Tomorrow
    fig = crosstab_barchart(df, 'WindGustDir')
    save_fig(fig, f"{OUTPUT_PATH}/wind_directions_vs_rain_tomorrow.png")


    # Wind Directionv at 9am vs Rain Tomorrow
    fig = crosstab_barchart(df, 'WindDir9am')
    save_fig(fig, f"{OUTPUT_PATH}/wind_directions_9am_vs_rain_tomorrow.png")

    fig = crosstab_barchart(df, 'WindDir3pm')
    save_fig(fig, f"{OUTPUT_PATH}/wind_directions_3pm_vs_rain_tomorrow.png")

    print("Done: Bivariate Analysis")
    print("All Graphs Saved to outputs/bivariate_analysis/")


if __name__ == "__main__": 
    bivariate_analysis()