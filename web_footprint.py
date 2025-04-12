import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/water_footprint_predictor.pkl')

st.set_page_config(page_title="Water Footprint Predictor", layout="centered")

st.title("🌿 Global Crop Water Footprint Predictor")
st.markdown("Predict the total water footprint (m³/tonne) of a crop based on its attributes.")

# Input fields
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load your trained model
with open("your_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌱 Crop Water Footprint Estimator")

st.markdown("Predict or calculate the total water footprint (m³/tonne) of a crop based on its attributes.")

# Toggle between Prediction and Manual Calculation
mode = st.radio("Choose Mode:", ["🔮 Predict using ML", "🧮 Calculate directly from water footprints"])

# User Inputs
crop_name = st.selectbox("Crop Name", ["Wheat", "Rice", "Maize", "Barley", "Soybean"])  # Extend as needed
crop_group = st.selectbox("Crop Group", ["Cereals", "Vegetables", "Fruits", "Fibres", "Oil crops", "Pulses"])
production = st.number_input("Production (tonnes)", min_value=0.0, value=10.0)

wfg = st.number_input("Green Water Footprint (m³/tonne)", min_value=0.0, value=100.0)
wfb_cr = st.number_input("Blue Water Footprint – Crop-Specific (m³/tonne)", min_value=0.0, value=50.0)
wfb_i = st.number_input("Blue Water Footprint – Infrastructure (m³/tonne)", min_value=0.0, value=25.0)

# Action Button
if st.button("🔍 Get Total Water Footprint"):
    if mode == "🧮 Calculate directly from water footprints":
        total = wfg + wfb_cr + wfb_i
        st.success(f"🧮 Calculated Total Water Footprint: **{total:.2f} m³/tonne**")
    else:
        # Create a DataFrame for model input
        input_df = pd.DataFrame({
            "crop_name": [crop_name],
            "crop_group": [crop_group],
            "production_t": [production]
        })

        try:
            prediction = model.predict(input_df)[0]
            st.success(f"🔮 Predicted Total Water Footprint: **{prediction:.2f} m³/tonne**")
        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
crop_name_categories= ['Maize (corn)', 'Soya beans', 'Wheat', 'Rice', 'Sorghum',
       'Seed cotton, unginned', 'Potatoes', 'Barley', 'Sunflower seed',
       'Millet', 'Rape or colza seed', 'Beans, dry', 'Cassava, fresh',
       'Groundnuts, excluding shelled', 'Sugar cane', 'Sugar beet',
       'Cow peas, dry', 'Peas, dry', 'Chick peas, dry', 'Tomatoes',
       'Sweet potatoes',
       'Onions and shallots, dry (excluding dehydrated)',
       'Chillies and peppers, green (Capsicum spp. and Pimenta spp.)',
       'Yams', 'Sesame seed', 'Oats', 'Grapes', 'Olives', 'Coffee, green',
       'Oil palm fruit', 'Natural rubber in primary forms', 'Cocoa beans',
       'Coconuts, in shell', 'Avocados', 'Cashew nuts, in shell',
       'Bananas', 'Tea leaves', 'Apples', 'Unmanufactured tobacco',
       'Oranges', 'Other vegetables, fresh n.e.c.',
       'Cucumbers and gherkins', 'Cabbages', 'Okra', 'Peas, green',
       'Watermelons', 'Eggplants (aubergines)', 'Other beans, green',
       'Green garlic', 'Asparagus', 'Pumpkins, squash and gourds',
       'Cauliflowers and broccoli', 'Lettuce and chicory',
       'Carrots and turnips', 'Cantaloupes and other melons',
       'Green corn (maize)', 'Spinach',
       'Broad beans and horse beans, green', 'Onions and shallots, green',
       'String beans', 'Leeks and other alliaceous vegetables',
       'Artichokes', 'Mushrooms and truffles', 'Chicory roots',
       'Cereals n.e.c.', 'Rye', 'Triticale', 'Buckwheat', 'Mixed grain',
       'Fonio', 'Canary seed', 'Quinoa', 'Other pulses n.e.c.',
       'Pigeon peas, dry', 'Lentils, dry',
       'Broad beans and horse beans, dry', 'Lupins', 'Vetches',
       'Bambara beans, dry', 'Taro',
       'Edible roots and tubers with high starch or inulin content, n.e.c., fresh',
       'Yautia', 'Linseed', 'Melonseed', 'Other oil seeds, n.e.c.',
       'Castor oil seeds', 'Mustard seed', 'Karite nuts (sheanuts)',
       'Safflower seed', 'Tallowtree seeds', 'Kapok fruit', 'Tung nuts',
       'Poppy seed', 'Hempseed', 'Jojoba seeds', 'Maté leaves',
       'Almonds, in shell', 'Walnuts, in shell', 'Areca nuts',
       'Pistachios, in shell', 'Hazelnuts, in shell',
       'Other nuts (excluding wild edible nuts and groundnuts), in shell, n.e.c.',
       'Kola nuts', 'Chestnuts, in shell', 'Brazil nuts, in shell',
       'Other fruits, n.e.c.', 'Plantains and cooking bananas',
       'Mangoes, guavas and mangosteens', 'Other tropical fruits, n.e.c.',
       'Tangerines, mandarins, clementines', 'Plums and sloes',
       'Peaches and nectarines', 'Other citrus fruit, n.e.c.', 'Dates',
       'Pears', 'Lemons and limes', 'Pineapples', 'Persimmons',
       'Apricots', 'Cashewapple', 'Papayas', 'Cherries', 'Strawberries',
       'Pomelos and grapefruits', 'Figs', 'Kiwi fruit', 'Sour cherries',
       'Currants',
       'Other berries and fruits of the genus vaccinium n.e.c.',
       'Raspberries', 'Blueberries', 'Quinces', 'Other stone fruits',
       'Cranberries', 'Other pome fruits', 'Gooseberries',
       'Locust beans (carobs)',
       'Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw',
       'Chillies and peppers, dry (Capsicum spp., Pimenta spp.), raw',
       'Other stimulant, spice and aromatic crops, n.e.c.',
       'Pepper (Piper spp.), raw', 'Cloves (whole stems), raw',
       'Nutmeg, mace, cardamoms, raw', 'Ginger, raw',
       'Cinnamon and cinnamon-tree flowers, raw', 'Vanilla, raw',
       'Hop cones', 'Peppermint, spearmint', 'Jute, raw or retted',
       'Other fibre crops, raw, n.e.c.', 'Flax, processed but not spun',
       'Sisal, raw', 'Abaca, manila hemp, raw',
       'Kenaf, and other textile bast fibres, raw or retted',
       'True hemp, raw or retted', 'Agave fibres, raw, n.e.c.',
       'Ramie, raw or retted', 'Pyrethrum, dried flowers',
       'Other sugar crops n.e.c.', 'Beets for fodder',
       'Swedes for fodder', 'Vegetables and roots fodder',
       'Clover for forage', 'Forage and silage, alfalfa',
       'Forage and silage, maize', 'Other forage products, n.e.c.',
       'Other grasses for forage', 'Other legumes for forage',
       'Turnips for forage', 'Forage and silage, rye grass',
       'Forage and silage, sorghum', 'Mixed Grasses and Legumes',
       'Forage and silage, green oilseeds', 'Cabbage for fodder',
       'Carrots for fodder']


crop_name = st.selectbox("Crop Name", crop_name_categories, help="Choose a crop (must be one present in the training dataset)")

crop_group = st.selectbox("Crop Group", ['Cereals', 'Oil crops', 'Fibres', 'Roots', 'Pulses', 'Sugar crops',
       'Vegetables', 'Fruits', 'Stimulants', 'Others', 'Nuts', 'Spices',
       'Fodder crops'], help="Choose the category of the crop")

production_t = st.number_input("Production (tonnes)", min_value=0.0, step=1000.0, format="%.2f")
wfg_m3_t = st.number_input("Green Water Footprint (m³/tonne)", min_value=0.0, step=10.0, format="%.2f")
wfb_cr_m3_t = st.number_input("Blue Water Footprint – Crop-Specific (m³/tonne)", min_value=0.0, step=10.0, format="%.2f")
wfb_i_m3_t = st.number_input("Blue Water Footprint – Infrastructure (m³/tonne)", min_value=0.0, step=10.0, format="%.2f")

# Submit
if st.button("Predict Total Water Footprint"):
    # Create input DataFrame
    input_data = pd.DataFrame([{
        'crop_code': 0,
        'crop_name': crop_name,
        'crop_group': crop_group,
        'production_t': production_t,
        'wfg_m3_t': wfg_m3_t,
        'wfb_cr_m3_t': wfb_cr_m3_t,
        'wfb_i_m3_t': wfb_i_m3_t
    }])

    # Predict
    prediction = model.predict(input_data)[0]

    st.success(f"🌊 Predicted Total Water Footprint: **{prediction:.2f} m³/tonne**")
