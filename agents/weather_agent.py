# agents/weather_agent.py

def check_planting_condition(temperature, rainfall):
    if temperature < 15:
        return "❄️ Too cold to plant. Wait for warmer days."
    elif rainfall < 40:
        return "💧 Not enough rain. Wait for better moisture."
    elif 20 <= temperature <= 30 and 50 <= rainfall <= 150:
        return "✅ Good weather! You can plant now."
    else:
        return "⚠️ Weather is okay, but keep monitoring."

# Optional: for testing only
if __name__ == "__main__":
    temp = float(input("Enter temperature (°C): "))
    rain = float(input("Enter rainfall (mm): "))
    msg = check_planting_condition(temp, rain)
    print("Planting Advice:", msg)
