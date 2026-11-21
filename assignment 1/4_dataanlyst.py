# Question 4: Data Analyst Job Shortlisting

required = {"python", "sql", "excel", "statistics"}

applicants = [
    {
        "name": "Ram",
        "age": 24,
        "cgpa": 3.4,
        "skills": {"python", "excel", "html"}
    },
    {
        "name": "Sita",
        "age": 37,
        "cgpa": 3.8,
        "skills": {"python", "sql", "excel", "statistics"}
    },
    {
        "name": "Gita",
        "age": 26,
        "cgpa": 3.6,
        "skills": {"python", "sql", "statistics", "tableau"}
    },
    {
        "name": "Hari",
        "age": 29,
        "cgpa": 2.7,
        "skills": {"sql", "excel", "statistics", "python"}
    }
]

# Initialize variables
shortlisted = []
extra_skills = set()

# Process applicants
for applicant in applicants:

    name = applicant["name"]
    age = applicant["age"]
    cgpa = applicant["cgpa"]
    skills = applicant["skills"]

    # Reject applicants outside age range
    if age < 21 or age > 35:
        print(f"{name}: rejected (age {age})")
        continue

    # Find matching skills
    matched_skills = skills.intersection(required)

    # Find missing skills
    missing_skills = required.difference(skills)

    # Calculate match percentage
    percentage = (len(matched_skills) / len(required)) * 100

    # Find extra skills
    extra_skills.update(skills.difference(required))

    # Shortlisting condition
    if percentage >= 75 and cgpa >= 2.5:

        print(
            f"{name}: {percentage:.0f}% match, "
            f"shortlisted, missing {sorted(missing_skills)}"
        )

        shortlisted.append((name, percentage, cgpa))

    else:

        print(
            f"{name}: {percentage:.0f}% match, "
            f"not shortlisted, missing {sorted(missing_skills)}"
        )

# Sort by highest match and then higher CGPA
shortlisted.sort(key=lambda x: (-x[1], -x[2]))

# Display interview order
interview_order = [applicant[0] for applicant in shortlisted]

print("Interview order:", interview_order)

print("Extra skills seen (not required):", sorted(extra_skills))