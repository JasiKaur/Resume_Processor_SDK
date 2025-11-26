import os
import re
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


#Load environment variables
load_dotenv()
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")


#Authenticate Azure client
client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

#Load resume text from file
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()
print("\n===== RESUME LOADED =====")


#Extract Key Phrases
response = client.extract_key_phrases(documents=[resume_text])[0]


#Identify skills from predefined list
predefined_skills = [
    "Azure", "Python", "AWS", "Docker", "Kubernetes",
    "DevOps", "SQL", "Networking", "Security", "Linux"
]

matched_skills = []
for skill in predefined_skills:
    if skill.lower() in resume_text.lower():
        matched_skills.append(skill)

print("\n===== MATCHED SKILLS =====")
for s in matched_skills:
    print("-", s)


#Extract experience years using regex
experience_matches = re.findall(r"(\d+)\+?\s+years?", resume_text.lower())

if experience_matches:
    experience_years = max([int(x) for x in experience_matches])
else:
    experience_years = 0

print("\n===== EXPERIENCE YEARS =====")
print("Total years of experience:", experience_years)


#Final output summary
print("\n===== FINAL SUMMARY =====")
print("Skills Found:", matched_skills)
print("Experience (years):", experience_years)

