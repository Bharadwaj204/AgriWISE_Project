# agents/farmer_advisor.py

def recommend_crop(soil_ph, soil_moisture, temperature, rainfall):
    """
    Recommend a crop based on simple environmental rules.
    You can replace this with an ML model later.
    """
    if soil_ph < 5.5:
        return "Rice"
    elif 6.0 <= soil_ph <= 7.0 and 40 <= soil_moisture <= 60:
        return "Wheat"
    elif soil_moisture < 30:
        return "Millet"
    elif temperature > 30 and rainfall > 100:
        return "Sugarcane"
    else:
        return "Maize"

# Example usage
if __name__ == "__main__":
    ph = float(input("Enter Soil pH: "))
    moisture = float(input("Enter Soil Moisture (%): "))
    temp = float(input("Enter Temperature (°C): "))
    rain = float(input("Enter Rainfall (mm): "))

    crop = recommend_crop(ph, moisture, temp, rain)
    print("✅ Recommended Crop:", crop)
