import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Page Config
st.set_page_config(page_title="Smart Water Usage Predictor", page_icon="💧", layout="centered")

# Title & Subtitle
st.markdown("# Predict Water Usage", unsafe_allow_html=True)

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
    
    # Generate target with some realistic relationships
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
    
    # Ensure water usage is always positive
    y = np.maximum(y, 10)
    
    # Train a Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    model_filename = 'models/irrigation_predictor.pkl'
    joblib.dump(model, model_filename)
    print(f'Model saved to {model_filename}')
    
    return model

# Function to prepare data for prediction
def prepare_input(temperature, humidity, soil_moisture, crop_type):
    # One-hot encode crop type
    crop_types = ['Corn', 'Rice', 'Soybean', 'Wheat']
    crop_encoded = [1 if crop == crop_type else 0 for crop in crop_types]
    
    # Create input array
    input_data = np.array([temperature, humidity, soil_moisture] + crop_encoded).reshape(1, -1)
    
    # Create DataFrame with correct column names
    input_df = pd.DataFrame(
        input_data, 
        columns=['temperature', 'humidity', 'soil_moisture', 
                'crop_type_Corn', 'crop_type_Rice', 'crop_type_Soybean', 'crop_type_Wheat']
    )
    
    return input_df

# Function to predict water usage
def predict_water_usage(temperature, humidity, soil_moisture, crop_type):
    # to make model 
    # model = load_model()
    model = joblib.load('models/irrigation_predictor.pkl')
    input_df = prepare_input(temperature, humidity, soil_moisture, crop_type)
    prediction = model.predict(input_df)[0]
    
    # Round to 1 decimal place
    return round(prediction, 1)

# Input Section
st.markdown("### 🌱 Enter Environmental & Soil Parameters")
col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input("🌡 Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0, step=0.1)
with col2:
    humidity = st.number_input("💦 Humidity (%)", min_value=10.0, max_value=100.0, value=50.0, step=0.1)
with col3:
    soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

st.markdown("### 🌾 Select Crop Type")
crop_type = st.selectbox("", ["Wheat", "Rice", "Corn", "Soybean"])

st.markdown("---")

# Predict Button
if st.button("🚀 Predict Irrigation Need"):
    with st.spinner("🔍 Predicting... Please wait"):
        # Calculate prediction
        water_usage = predict_water_usage(temperature, humidity, soil_moisture, crop_type)
        
        # Display result
        st.success("🎯 Prediction Successful!")
        st.markdown("## 💧 Recommended Water Usage")
        st.markdown(f"### 🔹 {water_usage} liters/acre")
        
        # Optional: Add visualization or additional context
        factors = {
            "Temperature": ["High 🔥" if temperature > 30 else "Moderate 🌤" if temperature > 20 else "Low ❄", 
                           "Higher temperatures increase water needs"],
            "Humidity": ["High 💦" if humidity > 70 else "Moderate 💧" if humidity > 40 else "Low 🏜",
                        "Lower humidity increases evaporation"],
            "Soil Moisture": ["High 💦" if soil_moisture > 70 else "Moderate 💧" if soil_moisture > 30 else "Low 🏜",
                             "Lower soil moisture indicates immediate watering need"]
        }
        
        st.markdown("### Factors Affecting Recommendation:")
        for factor, (level, desc) in factors.items():
            st.markdown(f"{factor}: {level} - {desc}")
