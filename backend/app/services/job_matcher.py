from typing import List, Dict, Any


def calculate_match(
    resume_skills: List[str],
    job_skills: List[str],
    semantic_similarity: float = 0.0
) -> Dict[str, Any]:

    resume_set = {
        skill.strip().lower()
        for skill in resume_skills
        if skill and skill.strip()
    }

    job_set = {
        skill.strip().lower()
        for skill in job_skills
        if skill and skill.strip()
    }

    if not job_set:
        return {
            "match_score": 0,
            "skill_match_score": 0,
            "semantic_similarity": round(
                semantic_similarity, 2
            ),
            "matched_skills": [],
            "missing_skills": [],
            "total_required_skills": 0,
            "matched_skill_count": 0,
            "recommendation": "No job skills were provided."
        }

    matched = sorted(
        resume_set.intersection(job_set)
    )

    missing = sorted(
        job_set.difference(resume_set)
    )

    # Skill matching score
    skill_score = (
        len(matched) / len(job_set)
    ) * 100

    skill_score = round(
        skill_score, 2
    )

    # Semantic similarity score
    semantic_score = max(
        0.0,
        min(float(semantic_similarity), 100.0)
    )

    # Final score
    final_score = (
        (skill_score * 0.60)
        +
        (semantic_score * 0.40)
    )

    final_score = round(
        final_score, 2
    )

    if final_score >= 80:
        recommendation = (
            "Strong match. Your profile covers most "
            "of the important requirements for this role."
        )
    elif final_score >= 60:
        recommendation = (
            "Good match. Your profile has a solid "
            "alignment with the job requirements."
        )
    elif final_score >= 40:
        recommendation = (
            "Moderate match. Some relevant skills are "
            "present, but additional skills are recommended."
        )
    else:
        recommendation = (
            "Low match. The resume has limited "
            "alignment with the current job requirements."
        )

    return {
        "match_score": final_score,
        "skill_match_score": skill_score,
        "semantic_similarity": round(
            semantic_score, 2
        ),
        "matched_skills": matched,
        "missing_skills": missing,
        "total_required_skills": len(job_set),
        "matched_skill_count": len(matched),
        "recommendation": recommendation
    }