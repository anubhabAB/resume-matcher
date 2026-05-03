# AI Resume Matcher 🤖

An AI-based web application that compares a resume with a job description and calculates how well they match using Natural Language Processing (NLP).

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge&logo=streamlit)](https://resume-matcher-7zccmht894wypotg6lgy79.streamlit.app/)

## 🚀 Features
- 📄 Upload resume (PDF or TXT)
- 🧠 Match score using TF-IDF & cosine similarity
- 📊 Visual progress bar for match percentage
- 🎯 Extract missing keywords from job description
- 🌐 Simple UI built with Streamlit

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Streamlit
- PyPDF2
- NLP (TF-IDF, Cosine Similarity)

## 📸 Screenshot

![App Screenshot](assets/screenshot.png)

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py