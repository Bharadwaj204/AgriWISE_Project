import sys
import os
from datetime import date
import streamlit as st
import pandas as pd

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.farmer_advisor import recommend_crop
from agents.market_agent import recommend_crops
from agents.weather_agent import check_planting_condition
from agents.sustainability_agent import calculate_sustainability
from db_helper import insert_result, create_database
from ml.crop_predictor import get_model, predict_yield

# Create the database if it doesn't exist
create_database()

# 🌱 Streamlit Web UI setup
st.set_page_config(page_title="AgriWISE AI", page_icon="🌾", layout="centered")

st.title("🌾 AgriWISE AI - Smart Sustainable Farming")
st.markdown("Empowering Farmers with AI: Smarter Crops, Smarter Future 🚜")

# 👨‍🌾 Input Section
st.subheader("📋 Enter Farm Details")

farm_id = st.text_input("Farm ID")
soil_ph = st.slider("Soil pH", 3.0, 9.0, step=0.1)
moisture = st.slider("Soil Moisture (%)", 0, 100)
temperature = st.slider("Temperature (°C)", 0, 50)
rainfall = st.slider("Rainfall (mm)", 0, 500)
fertilizer = st.slider("Fertilizer Usage (kg)", 0, 100)
pesticide = st.slider("Pesticide Usage (kg)", 0, 50)

# 🔍 Run AI Prediction
if st.button("Run AgriWISE AI") and farm_id:
    # Ensure model exists (train if needed)
    get_model()

    # Input as list
    input_list = [soil_ph, moisture, temperature, rainfall, fertilizer, pesticide]

    # ML Prediction
    predicted_yield = predict_yield(input_list)

    # Agent 1: Crop Recommendation
    recommended_crop = recommend_crop(soil_ph, moisture, temperature, rainfall)

    # Agent 2: Market Suggestion
    market_df = recommend_crops()
    market_crop = market_df.iloc[0]['Product'] if not market_df.empty else "N/A"

    # Agent 3: Weather Status
    weather_status = check_planting_condition(temperature, rainfall)

    # Agent 4: Sustainability Score
    score = calculate_sustainability(fertilizer, pesticide, rainfall, predicted_yield)

    # Save to DB
    today = str(date.today())
    insert_result(farm_id, recommended_crop, market_crop, weather_status, score, today)

    # Display Results
    st.metric(label="🌾 Predicted Crop Yield (tons)", value=predicted_yield)
    st.success(f"✅ Recommended Crop: **{recommended_crop}**")
    st.info(f"📈 Market Preferred Crop: **{market_crop}**")
    st.warning(f"🌦️ Weather Advice: **{weather_status}**")
    st.metric(label="♻️ Sustainability Score", value=score)

    st.markdown("---")
    st.subheader("📊 Market Insights")
    st.dataframe(market_df)

else:
    st.info("👈 Fill in the details and click **Run AgriWISE AI** to get suggestions.")
