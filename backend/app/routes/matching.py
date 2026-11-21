from pydantic import BaseModel
from fastapi import APIRouter

from app.nlp.skill_extractor import extract_skills
from app.nlp.semantic_matcher import calculate_semantic_similarity
from app.services.job_matcher import calculate_match


router = APIRouter(
    prefix="/api/matching",
    tags=["Job Matching"]
)


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/analyze")
def analyze_job_match(request: MatchRequest):

    # Extract skills from resume
    resume_skills = extract_skills(
        request.resume_text
    )

    # Extract required skills from job description
    job_skills = extract_skills(
        request.job_description
    )

    # Calculate TF-IDF + Cosine Similarity
    semantic_result = calculate_semantic_similarity(
        resume_text=request.resume_text,
        job_description=request.job_description
    )

    semantic_score = semantic_result[
        "similarity_percentage"
    ]

    # Calculate combined matching score
    result = calculate_match(
        resume_skills=resume_skills,
        job_skills=job_skills,
        semantic_similarity=semantic_score
    )

    return {
        "success": True,
        "resume_skills": resume_skills,
        "required_skills": job_skills,
        "semantic_analysis": semantic_result,
        "match_analysis": result
    }