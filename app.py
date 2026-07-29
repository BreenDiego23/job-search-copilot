def find_skills(job_description):
    skills = ["python", "javascript", "sql", "git", "api"]
    found_skills = []

    for skill in skills:
        if skill in job_description.lower():
            found_skills.append(skill)

    return found_skills


print("Job Search Copilot")
print("------------------")

job_description = input("Paste a short job description: ")
job_skills = find_skills(job_description)

user_input = input("Enter your skills, separated by commas: ")
user_skills = []

for skill in user_input.split(","):
    user_skills.append(skill.strip().lower())

matched_skills = []
missing_skills = []

for skill in job_skills:
    if skill in user_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

# This calculates a detected-skill match percentage
if job_skills:
    match_percentage = round(len(matched_skills) / len(job_skills) * 100)
else:
    match_percentage = 0

print(f"\nDetected skill match percentage: {match_percentage}%")
print("\nSkills you match:")

for skill in matched_skills:
    print(f"- {skill}")

print("\nSkills you may need:")

for skill in missing_skills:
    print(f"- {skill}")