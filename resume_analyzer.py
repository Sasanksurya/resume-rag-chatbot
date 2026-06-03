import re

def analyze_resume(text):

    score = 0

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "pandas",
        "numpy",
        "power bi",
        "streamlit",
        "flask",
        "git",
        "github",
        "scikit-learn"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score += min(len(found_skills) * 5, 30)

    sections = {
        "education": 15,
        "project": 20,
        "internship": 15,
        "experience": 15,
        "certification": 10,
        "skill": 15
    }

    missing_sections = []

    for section, points in sections.items():

        if section.lower() in text.lower():
            score += points
        else:
            missing_sections.append(section)

    score = min(score, 100)

    return {
        "score": score,
        "skills": found_skills,
        "missing_sections": missing_sections
    }