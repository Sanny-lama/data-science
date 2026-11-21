# Question 7: Glacier Lake Outburst Early Warning

lakes = {
    "Tsho Rolpa": (
        20.0, 24.0,
        [17.2, 17.5, 18.3, 19.0, 20.1, 22.0, 24.4, 25.0]
    ),

    "Imja": (
        15.0, 18.0,
        [12.0, 12.1, 12.3, 12.2, 12.6, 13.0, 13.1, 13.3]
    ),

    "Thulagi": (
        30.0, 33.0,
        [28.0, 28.9, 29.5, 30.2, 30.4, 30.1, 29.8, 29.6]
    )
}

# Initialize status groups
status_groups = {
    "Normal": [],
    "Watch": [],
    "Danger": []
}

# Process each lake
for lake, data in lakes.items():

    warning_level, danger_level, readings = data

    # Calculate hour-to-hour rises
    rises = []

    for i in range(1, len(readings)):
        rise = round(readings[i] - readings[i - 1], 2)
        rises.append(rise)

    maximum_level = max(readings)
    biggest_rise = max(rises)

    status = "Normal"
    warning_hour = None
    danger_hour = None

    # Find warning and danger levels
    for hour, level in enumerate(readings):

        if level >= warning_level and warning_hour is None:
            warning_hour = hour

            status = "Watch"

        if level >= danger_level:

            danger_hour = hour
            status = "Danger"

            break

    # Check for three or more consecutive rapid rises
    rapid_streak = 0
    rapid_rise = False

    for rise in rises:

        if rise > 0.5:

            rapid_streak += 1

            if rapid_streak >= 3:
                rapid_rise = True

        else:
            rapid_streak = 0

    # Create status message
    if status == "Danger":
        message = f"Danger (from hour {danger_hour})"

    elif status == "Watch":
        message = f"Watch (from hour {warning_hour})"

    else:
        message = "Normal"

    if rapid_rise:
        message += " + RAPID RISE"

    # Store lake in status dictionary
    status_groups[status].append(lake)

    print(
        f"{lake:<11} max {maximum_level:.1f} m, "
        f"biggest rise {biggest_rise:.1f} m, status {message}"
    )

# Display grouped lake status
print(status_groups)

# Print evacuation message
for lake in status_groups["Danger"]:

    print("EVACUATE downstream of:", lake)