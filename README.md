# Lunaris
__Not just an AI-Powered Water Footprint Calculator for Sustainable Agriculture__

## Tentative user interfaces
<img src="https://github.com/user-attachments/assets/224e3350-cf70-4f2b-b786-ae991b12a1a1" height=360>
<img src="https://github.com/user-attachments/assets/7c7dce33-c6a1-4e13-bfcd-c308d857e33a" height=360>
<br>

## Screenshots for user Interfaces and results in streamlit
<img src="https://github.com/user-attachments/assets/64878038-274c-4d5c-8037-3c9f41413cae" height=240>
<img src="https://github.com/user-attachments/assets/5a00f6dd-694f-4199-8da9-9e6e495dfd34" height=240>
<img src="https://github.com/user-attachments/assets/0ba6d387-83ab-4b37-95ed-27ef254f5bad" height=240>



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
 
## App Details
- Crop Prediction: uses Decision Tree for prediction of crop based on nitrogetn, potassium, phosphorus, rainfall and temperature parameters
- Irrigation Prediction: uses Random Forest for predicting irrigation need of crops (in development)
- Water Footprint: uses Random Forest for predicting water footprint of the crops (in development)

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
 



