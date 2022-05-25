from typing import Iterable
from pydantic import BaseModel


class CompetenceRequest(BaseModel):
    competence: str
    top_n: int


class Keyword(BaseModel):
    word: str
    weight: float


class TopicData(BaseModel):
    topic: int
    keywords: Iterable[Keyword]


class CompetenceDecomposition(BaseModel):
    competence: str
    top_n: int
    topic_indices: Iterable[int]
    topic_keywords: Iterable[TopicData]
