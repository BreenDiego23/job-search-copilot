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
found_skills = find_skills(job_description)

if found_skills:
    print("Skills found:")

    for skill in found_skills:
        print(f"- {skill}")
else:
    print("No recognized skills were found.")