# agents/sustainability_agent.py

def calculate_sustainability(fertilizer, pesticide, rainfall, yield_ton):
    """
    Calculates a sustainability score based on inputs.
    Lower usage of chemicals and good yield improve the score.
    """
    score = 100  # Start with perfect sustainability

    # Penalize overuse of fertilizer
    if fertilizer > 50:
        score -= 20
    elif fertilizer > 30:
        score -= 10

    # Penalize overuse of pesticide
    if pesticide > 10:
        score -= 20
    elif pesticide > 5:
        score -= 10

    # Penalize abnormal rainfall
    if rainfall < 40 or rainfall > 200:
        score -= 10

    # Reward high yield
    if yield_ton >= 4:
        score += 10
    elif yield_ton < 2:
        score -= 10

    # Ensure score remains between 0 and 100
    score = max(0, min(100, score))

    return score

# Example usage
if __name__ == "__main__":
    fert = float(input("Fertilizer used (kg): "))
    pest = float(input("Pesticide used (kg): "))
    rain = float(input("Rainfall (mm): "))
    yield_ton = float(input("Crop Yield (tons): "))

    final_score = calculate_sustainability(fert, pest, rain, yield_ton)
    print("🌱 Sustainability Score:", final_score)
