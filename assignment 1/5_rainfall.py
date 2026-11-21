# Question 5: Rainfall Stations and Flood Watch

rain = {
    "Kathmandu": [0, 12.5, 70.2, 118.0, 40.1, 0, 1.2],
    "Pokhara": [35.0, 88.4, 20.3, 95.0, 5.0, 0, 0],
    "Biratnagar": [0, 0, 2.0, 10.5, 66.0, 210.5, 130.0]
}

heavy_rain_limit = 64.5

heavy_stations = set()
station_totals = {}

# Process each station
for station, readings in rain.items():

    total = sum(readings)

    rainy_days = 0
    peak = max(readings)
    peak_day = readings.index(peak) + 1

    consecutive_heavy = 0
    flood_watch = False
    has_heavy_rain = False

    # Check daily rainfall
    for amount in readings:

        if amount > 0:
            rainy_days += 1

        if amount >= heavy_rain_limit:

            has_heavy_rain = True
            consecutive_heavy += 1

            if consecutive_heavy >= 2:
                flood_watch = True

        else:
            consecutive_heavy = 0

    if has_heavy_rain:
        heavy_stations.add(station)

    station_totals[station] = total

    if flood_watch:
        status = "FLOOD WATCH"
    else:
        status = "normal"

    print(
        f"{station:<11} total {total:6.1f} mm, "
        f"rainy days {rainy_days}, "
        f"peak {peak:.1f} mm on day {peak_day}, {status}"
    )

# Find wettest station
wettest_station = max(station_totals, key=station_totals.get)

print("Wettest station:", wettest_station)

print("Stations with heavy rain:", sorted(heavy_stations))