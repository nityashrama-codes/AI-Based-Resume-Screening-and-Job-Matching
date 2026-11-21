from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.resume import router as resume_router
from app.routes.matching import router as matching_router


app = FastAPI(
    title="AI-Based Resume Screening and Job Matching",
    description="NLP and Machine Learning based resume screening and job matching system",
    version="1.0.0"
)


# =========================
# CORS Configuration
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# API Routes
# =========================

app.include_router(resume_router)
app.include_router(matching_router)


# =========================
# Root Endpoint
# =========================

@app.get("/")
def root():
    return {
        "message": "AI Resume Screening API is running",
        "status": "success"
    }


# =========================
# Health Check
# =========================

@app.get("/api/health")
def health():
    return {
        "status": "ok"
    }