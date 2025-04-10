# ml/crop_predictor.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 🚜 Train and save the models
def get_model():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "farm_data.csv"))

    # Features and targets
    X = df[["Soil_pH", "Soil_Moisture", "Temperature_C", "Rainfall_mm", "Fertilizer_Usage_kg", "Pesticide_Usage_kg"]]
    y_yield = df["Crop_Yield_ton"]
    y_sustain = df["Sustainability_Score"]

    # Train/Test split
    X_train, _, y_yield_train, _ = train_test_split(X, y_yield, test_size=0.2, random_state=42)
    _, _, y_sustain_train, _ = train_test_split(X, y_sustain, test_size=0.2, random_state=42)

    # Models
    yield_model = RandomForestRegressor(n_estimators=100, random_state=42)
    yield_model.fit(X_train, y_yield_train)

    sustain_model = RandomForestRegressor(n_estimators=100, random_state=42)
    sustain_model.fit(X_train, y_sustain_train)

    # Save models
    os.makedirs("models", exist_ok=True)
    joblib.dump(yield_model, "models/yield_model.pkl")
    joblib.dump(sustain_model, "models/sustain_model.pkl")

    print("✅ Models trained and saved successfully.")

# 🌾 Predict Yield and Sustainability
def predict_yield(input_data):
    try:
        yield_model = joblib.load("models/yield_model.pkl")
        prediction_input = np.array(input_data).reshape(1, -1)
        predicted_yield = yield_model.predict(prediction_input)[0]
        return round(predicted_yield, 2)
    except:
        return "Model not found or input error!"

# 🌱 Predict both (if needed in backend/logic)
def predict_yield_and_sustainability(input_data):
    try:
        yield_model = joblib.load("models/yield_model.pkl")
        sustain_model = joblib.load("models/sustain_model.pkl")
        prediction_input = np.array(input_data).reshape(1, -1)
        predicted_yield = yield_model.predict(prediction_input)[0]
        predicted_sustain = sustain_model.predict(prediction_input)[0]
        return round(predicted_yield, 2), round(predicted_sustain, 2)
    except:
        return None, None

# 🔧 For testing only
if __name__ == "__main__":
    get_model()
    sample = [6.5, 45, 27, 90, 30, 5]
    yld, sus = predict_yield_and_sustainability(sample)
    print("Predicted Yield:", yld, "tons")
    print("Predicted Sustainability Score:", sus)
