from parser import extract_text_from_pdf
from nlp_utils import extract_skills
from matcher import calculate_match, missing_skills

resume=extract_text_from_pdf("sample_resume.pdf")

job_description = input("Enter the job description: ").lower()
resume_skills = extract_skills(resume)
job_skills = extract_skills(job_description)

score = calculate_match(resume, job_description)

missing_skills_list = missing_skills(resume_skills, job_skills)

print("==== Resume Analysis Result =====")
print(f"Match Score: {score}%")
print(f"Skills in Resume: {', '.join(resume_skills)}")
print(f"Skills Required by Job: {', '.join(job_skills)}")
if score < 70:
    print(f"Missing Skills: {', '.join(missing_skills_list)}")
else:
    print("Your resume is well-aligned with the job description. No critical skills are missing.")