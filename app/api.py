from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.models.dto import CompetenceDecomposition, CompetenceRequest
from app.utils import (
    find_closest_competence,
    load_competencies,
    load_topics,
    all_topics_keywords)


COMPETENCIES = load_competencies()
TOPICS = load_topics()


app = FastAPI()


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@app.post('/competence_decomposition', response_model=CompetenceDecomposition)
def competence_decomposition(data: CompetenceRequest):
    closest_competence = find_closest_competence(
        data.competence,
        COMPETENCIES
    )
    all_keywords = all_topics_keywords(
        closest_competence.topic_indices,
        TOPICS,
        data.top_n
    )
    return {
        'competence': data.competence,
        'top_n': data.top_n,
        'topic_indices': closest_competence.topic_indices,
        'topic_keywords': all_keywords
    }
