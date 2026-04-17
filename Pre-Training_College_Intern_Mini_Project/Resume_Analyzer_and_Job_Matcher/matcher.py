from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description):
    documents = [resume_text, job_description]
    cv = CountVectorizer()
    matrix = cv.fit_transform(documents)

    similarity_score = cosine_similarity(matrix[0], matrix[1])
    return round(similarity_score[0][0] * 100, 2)


def missing_skills(resume_skills, job_skills):
    missing = set(job_skills) - set(resume_skills)
    return list(missing)
