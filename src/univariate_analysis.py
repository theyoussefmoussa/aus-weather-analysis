import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import sys

project_root = os.path.abspath("..")
sys.path.insert(0, project_root)

from src.utils import set_labels, highlight_max_bar, save_fig, HIST_COLOR, BAR_COLOR, PIE_COLORS


def univariate_analysis():
    """Run full univariate analysis and save all figures to output_dir."""
    load_dotenv()
    BASE_PATH = os.getenv("BASE_PATH")
    output_dir="outputs/univariate_analysis"
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/clean_weather_training_data.parquet")

    # Location counts
    location_counts = df['Location'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.barh(location_counts.index, location_counts.values, color=BAR_COLOR)  # type: ignore
    set_labels("Location Counts", "Counts", "City")
    plt.xticks(range(0, 2750, 250))
    ax.invert_yaxis()
    plt.grid()
    save_fig(fig, f"{output_dir}/location_counts.png")

    # MinTemp distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['MinTemp'], bins=30, edgecolor='black', color=HIST_COLOR)
    highlight_max_bar(ax)
    plt.xticks(range(-5, 35, 3))
    plt.xlim(-5, 30)
    set_labels("Minimum Temperature Distribution", "Temperature", "Frequency")
    plt.grid()
    save_fig(fig, f"{output_dir}/min_temp_distribution.png")

    # MaxTemp distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['MaxTemp'], bins=25, edgecolor='black', color=HIST_COLOR)
    plt.xlim(0, 45)
    plt.xticks(range(0, 45, 3))
    plt.yticks(range(0, 12000, 1000))
    highlight_max_bar(ax)
    set_labels("Maximum Temperature Distribution", "Temperature", "Frequency")
    save_fig(fig, f"{output_dir}/max_temp_distribution.png")

    # Rainfall distribution
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['Rainfall'], bins=40, edgecolor='black', color=HIST_COLOR)
    set_labels("Rainfall Distribution", "Amount", "Frequency")
    plt.xticks(range(0, 60, 5))
    plt.xlim(0, 60)
    save_fig(fig, f"{output_dir}/rainfall_distribution.png")

    # Evaporation distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Evaporation'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xticks(range(0, 30, 5))
    plt.xlim(0, 30)
    highlight_max_bar(ax)
    set_labels("Evaporation Distribution")
    save_fig(fig, f"{output_dir}/evaporation_distribution.png")

    # Sunshine distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Sunshine'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.yticks(range(0, 5500, 500))
    plt.xlim(0, 14)
    plt.xticks(range(0, 15, 1))
    highlight_max_bar(ax)
    set_labels("Sunshine Hours Per Day Distribution", "Hours", "Frequency")
    save_fig(fig, f"{output_dir}/sunshine_distribution.png")

    # WindGustDir
    wind_gust_dir = df['WindGustDir'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x=wind_gust_dir.index, height=wind_gust_dir.values, color=BAR_COLOR)  # type: ignore
    plt.yticks(range(0, 12750, 750))
    set_labels("Wind Gust Directions", "Direction", "Counts")
    highlight_max_bar(ax)
    plt.xticks(rotation=45)
    save_fig(fig, f"{output_dir}/wind_gust_directions.png")

    # WindGustSpeed
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['WindGustSpeed'], bins=20, edgecolor='black', color=HIST_COLOR)
    set_labels("Wind Gust Speed Distribution", "Speed", "Frequency")
    plt.xticks(range(5, 115, 10))
    plt.xlim(5, 110)
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/wind_gust_speed_distribution.png")

    # WindDir9am
    wind_dir_9am = df['WindDir9am'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x=wind_dir_9am.index, height=wind_dir_9am.values, color=BAR_COLOR)  # type: ignore
    set_labels('Wind Directions at 9 am', "Direction", "Frequency")
    plt.yticks(range(0, 10000, 1500))
    highlight_max_bar(ax)
    plt.xticks(rotation=45)
    save_fig(fig, f"{output_dir}/wind_dir_9am.png")

    # WindDir3pm
    wind_dir_3pm = df['WindDir3pm'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x=wind_dir_3pm.index, height=wind_dir_3pm.values, color=BAR_COLOR)  # type: ignore
    set_labels('Wind Directions at 3 pm', "Direction", "Frequency")
    highlight_max_bar(ax)
    plt.xticks(rotation=45)
    save_fig(fig, f"{output_dir}/wind_dir_3pm.png")

    # WindSpeed9am
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['WindSpeed9am'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(0, 60)
    plt.xticks(range(0, 60, 5))
    set_labels("Wind Speed at 9 am", 'Speed')
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/wind_speed_9am.png")

    # WindSpeed3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['WindSpeed3pm'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(0, 60)
    plt.xticks(range(0, 60, 5))
    plt.yticks(range(0, 25000, 2500))
    set_labels("Wind Speed at 3 pm", "Speed", 'Counts')
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/wind_speed_3pm.png")

    # Humidity9am
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df["Humidity9am"], bins=20, edgecolor='black', color=HIST_COLOR)
    set_labels("Humidity at 9 am", "Humidity Percentage", "Counts")
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/humidity_9am.png")

    # Humidity3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df["Humidity3pm"], bins=20, edgecolor='black', color=HIST_COLOR)
    set_labels("Humidity at 3 pm", "Humidity Percentage", "Counts")
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/humidity_3pm.png")

    # Pressure9am
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Pressure9am'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(990, 1040)
    plt.xticks(range(990, 1045, 5))
    set_labels("Atmospheric Pressure at 9 am", "HPA Range", "Frequency")
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/pressure_9am.png")

    # Pressure3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Pressure3pm'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(990, 1040)
    plt.xticks(range(990, 1045, 5))
    set_labels("Atmospheric Pressure at 3pm", "HPA Range", "Frequency")
    highlight_max_bar(ax)
    save_fig(fig, f"{output_dir}/pressure_3pm.png")

    # Cloud9am
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Cloud9am'], bins=20, edgecolor='black', color=HIST_COLOR)
    highlight_max_bar(ax)
    set_labels("Clouds at 9 am According to Oktas")
    plt.xlim(0, 8)
    save_fig(fig, f"{output_dir}/cloud_9am.png")

    # Cloud3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Cloud3pm'], bins=20, edgecolor='black', color=HIST_COLOR)
    highlight_max_bar(ax)
    set_labels("Clouds at 3 pm According to Oktas")
    plt.xlim(0, 8)
    save_fig(fig, f"{output_dir}/cloud_3pm.png")

    # Temp9am
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Temp9am'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(0, 40)
    plt.xticks(range(0, 45, 5))
    highlight_max_bar(ax)
    set_labels("Temperature Distribution at 9 am", "Temperature", "Frequency")
    save_fig(fig, f"{output_dir}/temp_9am.png")

    # Temp3pm
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Temp3pm'], bins=20, edgecolor='black', color=HIST_COLOR)
    plt.xlim(0, 40)
    plt.xticks(range(0, 45, 5))
    highlight_max_bar(ax)
    set_labels("Temperature Distribution at 3 pm", "Temperature", "Frequency")
    save_fig(fig, f"{output_dir}/temp_3pm.png")

    # RainToday
    rain_today_counts = df['RainToday'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(
        rain_today_counts.values,  # type: ignore
        labels=rain_today_counts.index,  # type: ignore
        autopct="%1.1f%%",
        colors=PIE_COLORS
    )
    plt.title("Rain Today Or Not")
    plt.legend()
    save_fig(fig, f"{output_dir}/rain_today_pie.png")

    # RainTomorrow
    rain_tomorrow_counts = df['RainTomorrow'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(
        rain_tomorrow_counts.values,  # type: ignore
        labels=rain_tomorrow_counts.index,  # type: ignore
        autopct="%1.1f%%",
        colors=PIE_COLORS
    )
    plt.title("Will It Rain Tomorrow?")
    plt.legend()
    save_fig(fig, f"{output_dir}/rain_tomorrow_pie.png")
    print("Done: univariate_analysis.py")
    print("Figures saved in: outputs/univariate_analysis")


if __name__ == "__main__":
    univariate_analysis()
