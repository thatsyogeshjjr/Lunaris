import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Page Config
st.set_page_config(page_title="Water Blueprint Estimator", page_icon="💧", layout="centered")

# Title & Subtitle
st.markdown("# 💧 Smart Water Blueprint Estimator")
st.markdown("Estimate sustainable water usage based on crop & climate inputs.")

# ------------------------ MODEL TRAINING AND LOADING ------------------------
@st.cache_resource
def load_model():
    np.random.seed(42)
    n_samples = 1000
    
    # Generate synthetic data
    X = pd.DataFrame({
        'temperature': np.random.uniform(10, 45, n_samples),
        'humidity': np.random.uniform(10, 100, n_samples),
        'soil_moisture': np.random.uniform(0, 100, n_samples),
        'crop_type_Corn': np.random.randint(0, 2, n_samples),
        'crop_type_Rice': np.random.randint(0, 2, n_samples),
        'crop_type_Soybean': np.random.randint(0, 2, n_samples),
        'crop_type_Wheat': np.random.randint(0, 2, n_samples),
    })
    
    # Generate target (Water Blueprint) with realistic relationships
    y = (
        2.5 * X['temperature'] +
        -1.5 * X['humidity'] +
        -2.0 * X['soil_moisture'] +
        50 * X['crop_type_Corn'] +
        100 * X['crop_type_Rice'] +
        30 * X['crop_type_Soybean'] +
        40 * X['crop_type_Wheat'] +
        np.random.normal(0, 10, n_samples)
    )
    y = np.maximum(y, 10)  # ensure non-negative usage
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/water_blueprint_model.pkl')
    return model

# ------------------------ DATA PREP FUNCTIONS ------------------------
def prepare_input(temperature, humidity, soil_moisture, crop_type):
    crop_types = ['Corn', 'Rice', 'Soybean', 'Wheat']
    crop_encoded = [1 if crop == crop_type else 0 for crop in crop_types]

    input_data = np.array([temperature, humidity, soil_moisture] + crop_encoded).reshape(1, -1)
    input_df = pd.DataFrame(
        input_data, 
        columns=['temperature', 'humidity', 'soil_moisture', 
                'crop_type_Corn', 'crop_type_Rice', 'crop_type_Soybean', 'crop_type_Wheat']
    )
    return input_df

def predict_water_blueprint(temperature, humidity, soil_moisture, crop_type):
    model = joblib.load('models/water_blueprint_model.pkl')
    input_df = prepare_input(temperature, humidity, soil_moisture, crop_type)
    prediction = model.predict(input_df)[0]
    return round(prediction, 1)

# ------------------------ INPUT UI ------------------------
st.markdown("### 🌱 Input Environmental Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    temperature = st.number_input("🌡 Temperature (°C)", 10.0, 45.0, 25.0, step=0.1)
with col2:
    humidity = st.number_input("💦 Humidity (%)", 10.0, 100.0, 50.0, step=0.1)
with col3:
    soil_moisture = st.number_input("🌱 Soil Moisture (%)", 0.0, 100.0, 20.0, step=0.1)

st.markdown("### 🌾 Select Crop Type")
crop_type = st.selectbox("", ["Wheat", "Rice", "Corn", "Soybean"])

# ------------------------ MANUAL MODE TOGGLE ------------------------
manual_mode = st.toggle("🔧 Manually Calculate Water Blueprint")

if manual_mode:
    st.markdown("### ✍️ Manual Calculation Inputs")
    
    # Default water usage values
    crop_defaults = {
        "Wheat": 4500,
        "Rice": 7000,
        "Corn": 4000,
        "Soybean": 3500
    }

    base_usage = st.number_input(
        f"💧 Base Water Usage for {crop_type} (liters/acre)",
        1000, 10000, crop_defaults[crop_type], step=100
    )

    st.markdown("#### ⚙️ Adjustments for Conditions")
    temp_adj = st.slider("🌡 Temperature Impact (%)", -50, 50, 0, step=5)
    humidity_adj = st.slider("💦 Humidity Impact (%)", -50, 50, 0, step=5)
    soil_adj = st.slider("🌱 Soil Moisture Impact (%)", -50, 50, 0, step=5)

    total_adjustment = temp_adj + humidity_adj + soil_adj
    adjusted_water = base_usage * (1 + total_adjustment / 100)

    st.markdown("---")
    st.success("🧮 Manual Calculation Complete")
    st.markdown(f"### 💧 Estimated Water Blueprint: `{round(adjusted_water, 1)} liters/acre`")

else:
    # Predict using AI model
    if st.button("🚀 Predict Water Blueprint"):
        with st.spinner("🔍 Calculating... Please wait"):
            load_model()  # Train if not trained
            water_blueprint = predict_water_blueprint(temperature, humidity, soil_moisture, crop_type)
            st.success("🎯 Prediction Successful!")
            st.markdown("## 💧 Predicted Water Blueprint")
            st.markdown(f"### 🔹 `{water_blueprint} liters/acre`")

            # Optional Explanation
            factors = {
                "Temperature": ["High 🔥" if temperature > 30 else "Moderate 🌤" if temperature > 20 else "Low ❄",
                               "Higher temperatures increase transpiration"],
                "Humidity": ["High 💦" if humidity > 70 else "Moderate 💧" if humidity > 40 else "Low 🏜",
                            "Lower humidity increases evaporation"],
                "Soil Moisture": ["High 💦" if soil_moisture > 70 else "Moderate 💧" if soil_moisture > 30 else "Low 🏜",
                                 "Lower soil moisture requires more irrigation"]
            }

            st.markdown("### 🔍 Factors Considered:")
            for factor, (level, explanation) in factors.items():
                st.markdown(f"- **{factor}**: {level} – _{explanation}_")
