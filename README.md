# Lunaris
__Not just an AI-Powered Water Footprint Calculator for Sustainable Agriculture__

## Tech Stack
### Backend (Core Brain of the System)
- AI/ML Model:
    - Language: Python 
    Libraries:
        - scikit-learn or XGBoost for **initial regression models**
        - pandas, NumPy for **data manipulation**
        - joblib or pickle to **serialize models** for deployment
- API Framework: FastAPI OR Flask
- Data Integration: OpenWeatherMap and NASA POWER API
- Database: PostgreSQL with PostGIS or Firebase

### Frontend (User Dashboard)
- Framework:
        React OR Streamlit
  
- Charting/Maps:
        Plotly / Chart.js for water trends
        Leaflet.js or Mapbox for regional visualizations

### Report Generation
- PDF/CSV:
  reportlab or pdfkit for PDF
  pandas.to_csv() for CSV export

# Demo Videos
- [Crop Prediction](https://youtu.be/i9wpE1C-MpA)
 
## App Details
- Crop Prediction: uses Decision Tree for prediction of crop based on nitrogetn, potassium, phosphorus, rainfall and temperature parameters


## Feature List 
- [x] Regression model for water blueprint for water blueprint prediction
- [x] Irrigation Prediction
- [x] Water Footprint
- [ ] Random forest for water blueprint for water blueprint pridiction
- [ ] Gradient Boosting / XGBoost for water blueprint prediction
- [ ] Dashboard with Water Blueprint

## Additional Features
- [x] Crop prediction model prototype on streamlit
- [ ] Personalized Crop Advisory prototype on streamlit
- [ ] Farm Record Management prototype on streamlit

## Demo Videos
- [Crop Pridiction](https://youtu.be/i9wpE1C-MpA)
- [Irrigation Prediction](#)
- [Water Footprint](#)

## Setting up and developing applications
1. clone repo
    ```
    git clone https://github.com/thatsyogeshjjr/Lunaris
    ```
2. Go into directory
    ```
    cd Lunaris
    ```
3. Install required packages
    ```
    pip install -r requirements.txt
    ```
4. Run streamlit applications
    ```
    streamlit run [app_name].py
    ``` 


## Making application accessible
1. Making app accessible to low literacy users to improve adoption rates
    - [ ] **Visual Interfaces**: using more icons to convey information
    - [ ] **Voice Assistant**: T2S features (in local languages if possible)
    - [ ] **Simplified Navigation**: design intuitive user flows
    - [ ] **Offline Functionality**: ensuring tool usage w/o constant internet access
 



