from app.services.job_matcher import calculate_match


def test_perfect_match():

    resume_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Git"
    ]

    job_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Git"
    ]

    result = calculate_match(
        resume_skills,
        job_skills,
        semantic_similarity=100
    )

    assert result["match_score"] == 100
    assert result["skill_match_score"] == 100
    assert result["matched_skill_count"] == 4
    assert result["missing_skills"] == []


def test_partial_match():

    resume_skills = [
        "Python",
        "SQL"
    ]

    job_skills = [
        "Python",
        "SQL",
        "Docker",
        "AWS"
    ]

    result = calculate_match(
        resume_skills,
        job_skills,
        semantic_similarity=50
    )

    assert result["skill_match_score"] == 50
    assert result["matched_skill_count"] == 2

    assert "docker" in result["missing_skills"]
    assert "aws" in result["missing_skills"]


def test_no_job_skills():

    result = calculate_match(
        ["Python"],
        [],
        semantic_similarity=50
    )

    assert result["match_score"] == 0
    assert result["total_required_skills"] == 0
    assert result["matched_skills"] == []
    assert result["missing_skills"] == []


if __name__ == "__main__":

    test_perfect_match()
    test_partial_match()
    test_no_job_skills()

    print("All matching tests passed successfully.")