import json
from typing import Tuple, List
from pathlib import Path

from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
from app.models.dto import TopicData

from app.models.models import Competence, Topic


MODEL = SentenceTransformer('distiluse-base-multilingual-cased-v1')


def load_competencies() -> Tuple[Competence]:
    return tuple(
        map(
            lambda d: Competence(**d),
            json.loads(
                Path('app', 'data', 'competencies_with_topics.json').read_text(encoding='utf-8')
            )
        )
    )


def load_topics() -> Tuple[Topic]:
    return tuple(
        map(
            lambda d: Topic(**d),
            json.loads(
                Path('app', 'data', 'keywords_with_weights.json').read_text(encoding='utf-8')
            )
        )
    )


def cut_competence_text(text: str) -> str:
    return ' '.join(text.split()[2:])


def find_closest_competence(new_competence: str, 
                            competencies: Tuple[Competence]) -> Competence:
    clean_new_competence = cut_competence_text(new_competence)
    clean_competencies = tuple(
        cut_competence_text(competence.text)
        for competence in competencies
    )

    competence_embedding = MODEL.encode([clean_new_competence])
    sentence_embeddings = MODEL.encode(clean_competencies)

    min_distance = 10
    for competence, sentence_embedding in zip(competencies, sentence_embeddings):
        dist = distance.cosine(competence_embedding, sentence_embedding)
        if dist < min_distance:
            min_distance = dist
            closest_competence = competence
    
    return closest_competence


def all_topics_keywords(indices: List[int], 
                        topics: Tuple[Topic],
                        top_n: int) -> List[TopicData]:
    indices = indices[:top_n]
    result = []
    for topic in topics:
        if topic.index in indices:
            result.append(
                TopicData(**{'topic': topic.index, 'keywords': topic.keywords})
            )
    return result