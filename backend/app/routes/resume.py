import os
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.file_parser import extract_resume_text


router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


ALLOWED_EXTENSIONS = {".pdf", ".docx"}


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Please select a resume file."
        )

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    temporary_path = None

    try:

        file_content = await file.read()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temporary_file:

            temporary_file.write(file_content)
            temporary_path = temporary_file.name

        extracted_text = extract_resume_text(temporary_path)

        if not extracted_text:
            raise HTTPException(
                status_code=422,
                detail="Could not extract readable text from the resume."
            )

        return {
            "success": True,
            "filename": file.filename,
            "message": "Resume processed successfully.",
            "text": extracted_text,
            "character_count": len(extracted_text)
        }

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Resume processing failed: {str(error)}"
        )

    finally:

        if temporary_path and os.path.exists(temporary_path):
            os.remove(temporary_path)