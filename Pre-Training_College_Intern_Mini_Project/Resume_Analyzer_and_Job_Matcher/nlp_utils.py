from Skills_db import SKILLS

def extract_skills(text):
    normalized_text = text.lower()
    skills = {skill for skill in SKILLS if skill in normalized_text}
    return sorted(skills)

