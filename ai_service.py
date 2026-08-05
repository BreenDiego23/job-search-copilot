from dotenv import load_dotenv
from openai import OpenAI

# Load private values from the ignored .env file.
load_dotenv()

# Create a connection to the OpenAI API.
client = OpenAI()

def get_ai_advice(job_description, matched_skills, missing_skills):
    """Generate one honest next step for this job opportunity."""

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=(
            "You are a careful job-search coach. "
            "Use only the information provided. "
            "Do not invent experience or qualifications. "
            "Give one practical next step in two short sentences."
        ),
        input=(
            f"Job description: {job_description}\n"
            f"Skills the user matches: {matched_skills}\n"
            f"Skills the user may need: {missing_skills}"
        ),
    )

    return response.output_text