import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "scikit-learn",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "power bi",
    "excel"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(found_skills)


def analyze_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    if len(job_skills) > 0:
        score = round(
            (len(matched_skills) / len(job_skills)) * 100
        )
    else:
        score = 0

    suggestions = []

    if missing_skills:
        suggestions.append(
            "Consider adding projects or experience related "
            "to the missing skills."
        )

    if score < 50:
        suggestions.append(
            "Your resume has a low match with the job description. "
            "Try highlighting more relevant technical skills."
        )

    elif score < 75:
        suggestions.append(
            "Your resume has a moderate match. "
            "Add more job-specific skills and project experience."
        )

    else:
        suggestions.append(
            "Your resume has a strong skill match with the job description."
        )

    return {
        "score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }