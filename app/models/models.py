from typing import Iterable
from pydantic import BaseModel
from app.enums.track import Track
from app.enums.code import Code
from app.models.dto import Keyword


class Competence(BaseModel):
    track: Track
    code: Code
    text: str
    topic_indices: Iterable[int]


class Topic(BaseModel):
    name: str
    keywords: Iterable[Keyword]
