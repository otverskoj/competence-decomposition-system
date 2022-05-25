from typing import List
from pydantic import BaseModel


class CompetenceRequest(BaseModel):
    competence: str
    top_n: int


class Keyword(BaseModel):
    word: str
    weight: float


class TopicData(BaseModel):
    topic: int
    keywords: List[Keyword]


class CompetenceDecomposition(BaseModel):
    competence: str
    top_n: int
    topic_indices: List[int]
    topic_keywords: List[TopicData]
