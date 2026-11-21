# Question 10: Restaurant and Cafe Review Analysis

reviews = [
    ("Momo Magic", 5, "Delicious momo and friendly staff, very clean place"),
    ("Momo Magic", 4, "Tasty food but slow service"),
    ("Thakali Kitchen", 2, "Food was cold and the place was dirty"),
    ("Thakali Kitchen", 3, "Good dal bhat but expensive and slow"),
    ("Lakeside Cafe", 5, "Amazing view, delicious coffee, friendly owner")
]

positive = {
    "delicious", "friendly", "clean",
    "tasty", "good", "amazing"
}

negative = {
    "slow", "cold", "dirty",
    "expensive", "rude"
}

# Initialize dictionaries
place_ratings = {}
place_reviews = {}

word_counts = {}

# Combine positive and negative words
opinion_words = positive | negative

# Process each review
for place, stars, text in reviews:

    # Clean the review text
    cleaned_text = text.lower().replace(",", "")

    words = cleaned_text.split()

    # Convert words into set
    review_words = set(words)

    # Count positive and negative words
    positive_words = review_words.intersection(positive)

    negative_words = review_words.intersection(negative)

    pos_count = len(positive_words)
    neg_count = len(negative_words)

    # Determine review mood
    if pos_count > neg_count:
        mood = "Positive"

    elif pos_count < neg_count:
        mood = "Negative"

    else:
        mood = "Mixed"

    print(
        f"{place:<17}{stars}* "
        f"pos={pos_count} neg={neg_count} -> {mood}"
    )

    # Store ratings
    if place not in place_ratings:
        place_ratings[place] = 0
        place_reviews[place] = 0

    place_ratings[place] += stars
    place_reviews[place] += 1

    # Count opinion words
    for word in words:

        if word in opinion_words:

            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1

# Calculate average rating per place
print("Average rating:")

for place in place_ratings:

    average = place_ratings[place] / place_reviews[place]

    print(
        f"  {place:<17}{average:.1f} "
        f"from {place_reviews[place]} reviews"
    )

# Sort opinion words by frequency
# If frequencies are equal, sort alphabetically
sorted_words = sorted(
    word_counts.items(),
    key=lambda x: (-x[1], x[0])
)

# Select top 3 words
top_three = sorted_words[:3]

print("Top opinion words:", top_three)