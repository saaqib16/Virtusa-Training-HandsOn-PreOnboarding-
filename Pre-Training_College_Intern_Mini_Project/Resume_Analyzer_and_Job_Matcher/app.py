import streamlit as st
from matcher import calculate_match, missing_skills
from nlp_utils import extract_skills
from parser import extract_text_from_pdf

st.set_page_config(page_title="Resume Analyzer and Job Matcher")
st.title("Resume Analyzer and Job Matcher")
st.write("Upload a PDF resume and paste a job description to compare the fit.")

resume = st.file_uploader("Upload Resume", type=["pdf"])

job_desc = st.text_area("Paste Job Description", height=220)

if st.button("Analyze"):
    if resume is None or not job_desc.strip():
        st.warning("Please upload a resume PDF and enter a job description.")
    else:
        resume_text = extract_text_from_pdf(resume)
        job_description = job_desc.lower()

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)
        score = calculate_match(resume_text, job_description)
        missing = missing_skills(resume_skills, job_skills)

        st.subheader("Analysis Result")
        st.metric("Match Score", f"{score}%")
        st.write("Skills in Resume:", ", ".join(resume_skills) or "No matching skills found.")
        st.write("Skills Required by Job:", ", ".join(job_skills) or "No matching skills found.")

        if missing:
            st.write("Missing Skills:", ", ".join(missing))
        else:
            st.success("Your resume is well-aligned with the job description.")
