# Question 8: Forest Fire Risk by District and Province

districts = [
    ("Chitwan", "Bagmati", 36, 18, 25, 40),
    ("Kaski", "Gandaki", 27, 55, 10, 5),
    ("Dang", "Lumbini", 33, 30, 35, 20),
    ("Bardiya", "Lumbini", 38, 15, 32, 35),
    ("Ilam", "Koshi", 24, 70, 8, 3),
    ("Makwanpur", "Bagmati", 31, 40, 18, 12)
]

# Initialize risk groups
risk_groups = {
    "Low": [],
    "Moderate": [],
    "High": [],
    "Extreme": []
}

alert_provinces = set()

# Process districts
for district, province, temp, humidity, wind, days in districts:

    score = 0

    # Temperature scoring
    if temp > 35:
        score += 3

    elif temp > 30:
        score += 2

    elif temp > 25:
        score += 1

    # Humidity scoring
    if humidity < 20:
        score += 3

    elif humidity < 35:
        score += 2

    elif humidity < 50:
        score += 1

    # Wind speed scoring
    if wind > 30:
        score += 2

    elif wind > 15:
        score += 1

    # Days since rain scoring
    if days > 30:
        score += 3

    elif days > 14:
        score += 2

    elif days > 7:
        score += 1

    # Determine risk level
    if score >= 9:
        risk = "Extreme"

    elif score >= 7:
        risk = "High"

    elif score >= 4:
        risk = "Moderate"

    else:
        risk = "Low"

    # Group district and score
    risk_groups[risk].append((district, score))

    # Collect provinces with high or extreme risk
    if risk == "High" or risk == "Extreme":
        alert_provinces.add(province)

# Display results
for risk, district_list in risk_groups.items():

    print(f"{risk:<9}: {district_list}")

print("Provinces to alert:", sorted(alert_provinces))