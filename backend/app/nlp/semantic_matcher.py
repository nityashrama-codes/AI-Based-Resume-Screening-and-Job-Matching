from typing import Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.nlp.text_cleaner import clean_text


def calculate_semantic_similarity(
    resume_text: str,
    job_description: str
) -> Dict[str, Any]:

    if not resume_text or not job_description:
        return {
            "similarity_score": 0.0,
            "similarity_percentage": 0.0,
            "method": "TF-IDF + Cosine Similarity"
        }

    resume_cleaned = clean_text(resume_text)
    job_cleaned = clean_text(job_description)

    if not resume_cleaned or not job_cleaned:
        return {
            "similarity_score": 0.0,
            "similarity_percentage": 0.0,
            "method": "TF-IDF + Cosine Similarity"
        }

    try:
        documents = [
            resume_cleaned,
            job_cleaned
        ]

        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            stop_words="english"
        )

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        similarity_percentage = round(
            float(similarity) * 100,
            2
        )

        return {
            "similarity_score": round(
                float(similarity),
                4
            ),
            "similarity_percentage": similarity_percentage,
            "method": "TF-IDF + Cosine Similarity"
        }

    except ValueError:

        return {
            "similarity_score": 0.0,
            "similarity_percentage": 0.0,
            "method": "TF-IDF + Cosine Similarity"
        }

    except Exception as error:

        return {
            "similarity_score": 0.0,
            "similarity_percentage": 0.0,
            "method": "TF-IDF + Cosine Similarity",
            "error": str(error)
        }