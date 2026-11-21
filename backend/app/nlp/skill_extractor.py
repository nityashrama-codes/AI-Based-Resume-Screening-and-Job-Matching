import re
from typing import List, Dict

from app.nlp.text_cleaner import clean_text


SKILL_ALIASES: Dict[str, List[str]] = {

    "Python": [
        "python"
    ],

    "Java": [
        "java"
    ],

    "JavaScript": [
        "javascript",
        "js"
    ],

    "TypeScript": [
        "typescript",
        "ts"
    ],

    "C++": [
        "c++"
    ],

    "C#": [
        "c#",
        "c sharp"
    ],

    "HTML": [
        "html"
    ],

    "CSS": [
        "css"
    ],

    "React": [
        "react",
        "react.js",
        "reactjs"
    ],

    "Angular": [
        "angular"
    ],

    "Vue": [
        "vue",
        "vue.js"
    ],

    "Node.js": [
        "node.js",
        "nodejs",
        "node"
    ],

    "Express": [
        "express",
        "express.js"
    ],

    "Django": [
        "django"
    ],

    "Flask": [
        "flask"
    ],

    "FastAPI": [
        "fastapi",
        "fast api"
    ],

    "SQL": [
        "sql"
    ],

    "MySQL": [
        "mysql"
    ],

    "PostgreSQL": [
        "postgresql",
        "postgres"
    ],

    "MongoDB": [
        "mongodb",
        "mongo db"
    ],

    "Redis": [
        "redis"
    ],

    "Machine Learning": [
        "machine learning",
        "ml"
    ],

    "Deep Learning": [
        "deep learning",
        "dl"
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "ai"
    ],

    "Natural Language Processing": [
        "natural language processing",
        "nlp"
    ],

    "Computer Vision": [
        "computer vision"
    ],

    "Pandas": [
        "pandas"
    ],

    "NumPy": [
        "numpy",
        "num py"
    ],

    "Scikit-learn": [
        "scikit-learn",
        "sklearn",
        "scikit learn"
    ],

    "TensorFlow": [
        "tensorflow",
        "tensor flow"
    ],

    "PyTorch": [
        "pytorch",
        "py torch"
    ],

    "Git": [
        "git"
    ],

    "GitHub": [
        "github",
        "git hub"
    ],

    "Docker": [
        "docker"
    ],

    "Kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "AWS": [
        "aws",
        "amazon web services"
    ],

    "Azure": [
        "azure",
        "microsoft azure"
    ],

    "Google Cloud": [
        "google cloud",
        "gcp"
    ],

    "REST API": [
        "rest api",
        "restful api",
        "rest services"
    ],

    "API": [
        "api",
        "application programming interface"
    ],

    "Data Analysis": [
        "data analysis",
        "data analytics"
    ],

    "Data Science": [
        "data science"
    ],

    "Problem Solving": [
        "problem solving",
        "problem-solving"
    ],

    "Communication": [
        "communication",
        "communication skills"
    ],

    "Leadership": [
        "leadership",
        "leadership skills"
    ],

    "Teamwork": [
        "teamwork",
        "team work",
        "collaboration"
    ],
}


def _contains_skill(text: str, skill: str) -> bool:
    """
    Checks whether a skill exists as a complete phrase
    instead of simple substring matching.
    """

    escaped_skill = re.escape(skill.lower())

    pattern = rf"(?<![a-z0-9]){escaped_skill}(?![a-z0-9])"

    return re.search(
        pattern,
        text.lower()
    ) is not None


def extract_skills(text: str) -> List[str]:
    """
    Extracts standardized skills from resume or
    job-description text using aliases and
    boundary-aware matching.
    """

    if not text:
        return []

    cleaned_text = clean_text(text)

    if not cleaned_text:
        return []

    found_skills = []

    for standard_skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if _contains_skill(
                cleaned_text,
                alias
            ):
                found_skills.append(
                    standard_skill
                )
                break

    return sorted(
        set(found_skills),
        key=str.lower
    )