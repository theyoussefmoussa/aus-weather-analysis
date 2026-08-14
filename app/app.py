import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from src.predict import predict_weather


st.set_page_config(
    page_title="Australia Weather Prediction",
    page_icon="🌦️",
    layout="wide"
)


st.title("🇦🇺 Australia Weather Prediction")
st.write("Predict whether it will rain tomorrow based on today's weather conditions.")

st.divider()


st.subheader("📍 Location")

location = st.selectbox(
    "Location",
    [
        "Adelaide", "Albany", "Albury", "AliceSprings",
        "BadgerysCreek", "Ballarat", "Bendigo", "Brisbane",
        "Cairns", "Canberra", "Cobar", "CoffsHarbour",
        "Dartmoor", "Darwin", "GoldCoast", "Hobart",
        "Katherine", "Launceston", "Melbourne",
        "MelbourneAirport", "Mildura", "Moree", "MountGambier",
        "MountGinini", "Newcastle", "Nhil", "NorahHead",
        "NorfolkIsland", "Nuriootpa", "PearceRAAF", "Penrith",
        "Perth", "PerthAirport", "Portland", "Richmond",
        "Sale", "SalmonGums", "Sydney", "SydneyAirport",
        "Townsville", "Tuggeranong", "Uluru", "WaggaWagga",
        "Walpole", "Watsonia", "Williamtown", "Witchcliffe",
        "Wollongong", "Woomera"
    ]
)


st.subheader("🌡️ Temperature")

col1, col2, col3, col4 = st.columns(4)

with col1:
    min_temp = st.number_input("MinTemp", value=15.0)

with col2:
    max_temp = st.number_input("MaxTemp", value=25.0)

with col3:
    temp_9am = st.number_input("Temp9am", value=20.0)

with col4:
    temp_3pm = st.number_input("Temp3pm", value=24.0)


st.subheader("🌧️ Rain")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.number_input(
        "Rainfall",
        min_value=0.0,
        value=0.0
    )

with col2:
    evaporation = st.number_input(
        "Evaporation",
        min_value=0.0,
        value=5.0
    )

with col3:
    sunshine = st.number_input(
        "Sunshine",
        min_value=0.0,
        value=7.0
    )


rain_today = st.selectbox(
    "RainToday",
    ["No", "Yes"]
)


st.subheader("💧 Humidity & Pressure")

col1, col2, col3, col4 = st.columns(4)

with col1:
    humidity_9am = st.number_input(
        "Humidity9am",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col2:
    humidity_3pm = st.number_input(
        "Humidity3pm",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

with col3:
    pressure_9am = st.number_input(
        "Pressure9am",
        value=1015.0
    )

with col4:
    pressure_3pm = st.number_input(
        "Pressure3pm",
        value=1010.0
    )


st.subheader("☁️ Clouds")

col1, col2 = st.columns(2)

with col1:
    cloud_9am = st.number_input(
        "Cloud9am",
        min_value=0,
        max_value=8,
        value=4
    )

with col2:
    cloud_3pm = st.number_input(
        "Cloud3pm",
        min_value=0,
        max_value=8,
        value=4
    )


st.subheader("💨 Wind")

col1, col2, col3 = st.columns(3)

wind_directions = [
    "N", "NNE", "NE", "ENE",
    "E", "ESE", "SE", "SSE",
    "S", "SSW", "SW", "WSW",
    "W", "WNW", "NW", "NNW"
]

with col1:
    wind_gust_speed = st.number_input(
        "WindGustSpeed",
        min_value=0.0,
        value=40.0
    )

with col2:
    wind_speed_9am = st.number_input(
        "WindSpeed9am",
        min_value=0.0,
        value=15.0
    )

with col3:
    wind_speed_3pm = st.number_input(
        "WindSpeed3pm",
        min_value=0.0,
        value=20.0
    )


col1, col2, col3 = st.columns(3)

with col1:
    wind_gust_dir = st.selectbox(
        "WindGustDir",
        wind_directions
    )

with col2:
    wind_dir_9am = st.selectbox(
        "WindDir9am",
        wind_directions
    )

with col3:
    wind_dir_3pm = st.selectbox(
        "WindDir3pm",
        wind_directions
    )


st.divider()


if st.button(
    "🔮 Predict Rain Tomorrow",
    type="primary",
    use_container_width=True
):

    input_data = {
        "Location": location,
        "MinTemp": min_temp,
        "MaxTemp": max_temp,
        "Rainfall": rainfall,
        "Evaporation": evaporation,
        "Sunshine": sunshine,
        "WindGustDir": wind_gust_dir,
        "WindGustSpeed": wind_gust_speed,
        "WindDir9am": wind_dir_9am,
        "WindDir3pm": wind_dir_3pm,
        "WindSpeed9am": wind_speed_9am,
        "WindSpeed3pm": wind_speed_3pm,
        "Humidity9am": humidity_9am,
        "Humidity3pm": humidity_3pm,
        "Pressure9am": pressure_9am,
        "Pressure3pm": pressure_3pm,
        "Cloud9am": cloud_9am,
        "Cloud3pm": cloud_3pm,
        "Temp9am": temp_9am,
        "Temp3pm": temp_3pm,
        "RainToday": rain_today,
    }

    try:
        prediction, probability = predict_weather(input_data)

        st.subheader("Prediction Result")

        if prediction == "Yes":
            st.error("🌧️ Rain Tomorrow: YES")
        else:
            st.success("☀️ Rain Tomorrow: NO")

        st.metric(
            "Rain Probability",
            f"{probability * 100:.2f}%"
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")