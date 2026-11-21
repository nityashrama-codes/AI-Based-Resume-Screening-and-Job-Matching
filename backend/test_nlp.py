from app.nlp.skill_extractor import extract_skills
from app.nlp.semantic_matcher import calculate_semantic_similarity


def test_skill_extraction():

    text = """
    Python developer with experience in React.js,
    FastAPI, SQL, Machine Learning, Docker and Git.
    """

    skills = extract_skills(text)

    expected_skills = [
        "Python",
        "React",
        "FastAPI",
        "SQL",
        "Machine Learning",
        "Docker",
        "Git"
    ]

    for skill in expected_skills:
        assert skill in skills


def test_semantic_similarity():

    resume = """
    Python developer experienced in machine learning,
    REST API development and SQL databases.
    """

    job = """
    Looking for a Python developer with machine learning,
    REST API and SQL experience.
    """

    result = calculate_semantic_similarity(
        resume,
        job
    )

    assert "similarity_percentage" in result
    assert result["similarity_percentage"] >= 0
    assert result["similarity_percentage"] <= 100


if __name__ == "__main__":

    test_skill_extraction()
    test_semantic_similarity()

    print("All NLP tests passed successfully.")