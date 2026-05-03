import streamlit as st
from ml_model import match_score
from utils import get_missing_keywords
import PyPDF2

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("AI Resume Matcher 🤖")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

# Job Description Input
job_desc = st.text_area("Paste Job Description")

# Extract text from file
def extract_text(file):
    text = ""
    
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
    
    elif file.type == "text/plain":
        text = file.read().decode("utf-8")
    
    return text

# Analyze Button
if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume = extract_text(uploaded_file)

        score = match_score(resume, job_desc)
        missing = get_missing_keywords(resume, job_desc)

        st.subheader(f"Match Score: {score}%")
        st.progress(int(score))

        st.subheader("Missing Keywords:")
        st.write(missing)
    else:
        st.warning("Please upload resume and enter job description")