from typing import List
from pydantic import BaseModel
from app.enums.track import Track
from app.enums.code import Code
from app.models.dto import Keyword


class Competence(BaseModel):
    track: Track
    code: Code
    text: str
    topic_indices: List[int]


class Topic(BaseModel):
    index: int
    name: str
    keywords: List[Keyword]
