# Question 3: Cricket Ball-by-Ball Scorecard

balls = "1 4 . W 6 wd 2 1 . 4 nb 1 . . W 6 1 lb2"

# Convert string into list
ball_list = balls.split()

# Initialize variables
score = 0
wickets = 0
extras = 0
fours = 0
sixes = 0
dot_balls = 0
legal_balls = 0

# Process every ball
for ball in ball_list:

    # Wide
    if ball == "wd":
        score += 1
        extras += 1
        continue

    # No ball
    elif ball == "nb":
        score += 1
        extras += 1
        continue

    # Leg bye
    elif ball.startswith("lb"):
        runs = int(ball[2:])
        score += runs
        extras += runs
        legal_balls += 1
        continue

    # Wicket
    elif ball == "W":
        wickets += 1
        legal_balls += 1
        continue

    # Dot ball
    elif ball == ".":
        dot_balls += 1
        legal_balls += 1
        continue

    # Numeric runs
    else:
        runs = int(ball)

        score += runs
        legal_balls += 1

        if runs == 4:
            fours += 1

        elif runs == 6:
            sixes += 1

# Calculate overs
overs = legal_balls // 6
remaining_balls = legal_balls % 6

# Calculate run rate
run_rate = score / (legal_balls / 6)

# Calculate boundary runs
boundary_runs = (fours * 4) + (sixes * 6)

boundary_percentage = (boundary_runs / score) * 100

# Display results
print(f"Score: {score}/{wickets} in {overs}.{remaining_balls} overs")

print(
    f"Extras {extras}, Fours {fours}, "
    f"Sixes {sixes}, Dot balls {dot_balls}"
)

print(
    f"Run rate {run_rate:.2f}, "
    f"Boundary runs {boundary_runs} "
    f"({boundary_percentage:.1f}% of total)"
)