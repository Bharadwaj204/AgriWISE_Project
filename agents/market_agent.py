# agents/market_agent.py
import pandas as pd
import os

def recommend_crops():
    # Load the market data from CSV
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "market_data.csv")
    
    if not os.path.exists(file_path):
        # If you're calling this inside a Streamlit app, you need to import streamlit
        import streamlit as st
        st.error("❌ Market data file not found!")
        return pd.DataFrame()  # Return empty DataFrame or handle as needed
    else:
        data = pd.read_csv(file_path)

        # Simple formula to check which crop is more profitable
        data["Profit_Score"] = (data["Market_Price_per_ton"] - data["Competitor_Price_per_ton"]) * data["Demand_Index"]

        # Sort and get top 2 profitable crops
        top = data.sort_values(by="Profit_Score", ascending=False).head(2)

        return top[["Product", "Market_Price_per_ton", "Demand_Index", "Profit_Score"]]
