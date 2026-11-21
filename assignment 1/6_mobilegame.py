# Question 6: Mobile Game Match History

matches = [
    ("W", 10, 1, 5, "Layla"),
    ("W", 3, 2, 4, "Tigreal"),
    ("L", 2, 6, 3, "Layla"),
    ("W", 8, 0, 6, "Gusion"),
    ("W", 5, 2, 9, "Layla"),
    ("W", 1, 3, 12, "Tigreal"),
    ("L", 4, 5, 2, "Gusion"),
    ("W", 7, 2, 8, "Layla")
]

# Initialize variables
total_matches = len(matches)
wins = 0

current_streak = 0
longest_streak = 0

hero_kda = {}

# Process match history
for result, kills, deaths, assists, hero in matches:

    # Calculate KDA
    if deaths == 0:
        kda = kills + assists
    else:
        kda = (kills + assists) / deaths

    # Store KDA for each hero
    if hero not in hero_kda:
        hero_kda[hero] = []

    hero_kda[hero].append(kda)

    # Calculate wins and streak
    if result == "W":

        wins += 1
        current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    else:
        current_streak = 0

# Calculate win rate
win_rate = (wins / total_matches) * 100

print(
    f"Win rate: {win_rate:.1f}%  "
    f"Longest win streak: {longest_streak}"
)

# Calculate average KDA per hero
for hero, kdas in hero_kda.items():

    average_kda = sum(kdas) / len(kdas)

    print(
        f"{hero:<8} games {len(kdas)}, "
        f"avg KDA {average_kda:.2f}"
    )

# Find most played hero
most_played = max(hero_kda, key=lambda hero: len(hero_kda[hero]))

print("Most played hero:", most_played)