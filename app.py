import json

def find_skills(job_description):
    
    skills = ["python", "javascript", "sql", "git", "api"]
    found_skills = []

    # Check each supported skill and save the ones mentioned in the job.
    for skill in skills:
        if skill in job_description.lower():
            found_skills.append(skill)

    return found_skills

def load_saved_job():
    """Load the most recently saved job analysis."""
    try:
        with open("saved_job.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

print("Job Search Copilot")
print("------------------")

view_saved_job = input(
    "Would you like to view your last saved analysis? (y/n): "
).strip().lower()

if view_saved_job == "y":
    saved_job = load_saved_job()

    if saved_job:
        saved_skills = ", ".join(saved_job["detected_skills"])

        print("\nLast saved analysis:")
        print(f"Detected skills: {saved_skills or 'None'}")
        print(f"Skill match: {saved_job['match_percentage']}%")
    else:
        print("\nNo saved job analysis was found.")

job_description = input("\nPaste a short job description: ")
job_skills = find_skills(job_description)

user_input = input("Enter your skills, separated by commas: ")
user_skills = []

# Clean up each skill so extra spaces and capitalization do not affect matching.
for skill in user_input.split(","):
    user_skills.append(skill.strip().lower())

matched_skills = []
missing_skills = []

# Separate the job skills into matches and possible skill gaps.
for skill in job_skills:
    if skill in user_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

# Use 0 when no job skills are detected so we do not divide by zero.
if job_skills:
    match_percentage = round(
        len(matched_skills) / len(job_skills) * 100
    )
else:
    match_percentage = 0

print(f"\nDetected skill match percentage: {match_percentage}%")
print("\nSkills you match:")

for skill in matched_skills:
    print(f"- {skill}")

print("\nSkills you may need:")

for skill in missing_skills:
    print(f"- {skill}")

# Organize the analysis into structured data that can be saved and loaded later.
job_data = {
    "job_description": job_description,
    "detected_skills": job_skills,
    "user_skills": user_skills,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "match_percentage": match_percentage,
}

# Save the analysis locally without publishing the user's information to GitHub.
with open("saved_job.json", "w") as file:
    json.dump(job_data, file, indent=4)

print("\nJob analysis saved to saved_job.json")