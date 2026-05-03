import re

def get_missing_keywords(resume, job_desc):
    resume_words = set(re.findall(r'\b\w+\b', resume.lower()))
    job_words = set(re.findall(r'\b\w+\b', job_desc.lower()))
    
    common_words = {"the", "and", "is", "in", "to", "of", "a", "for"}
    missing = job_words - resume_words - common_words
    
    return list(missing)[:10]