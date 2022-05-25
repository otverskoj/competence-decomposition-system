import json
from pathlib import Path
from app.models.models import Competence


data = json.loads(Path('app', 'data', 'competencies_with_topics.json').read_text(encoding='utf-8'))
competences = list(map(lambda d: Competence(**d), data))
print(competences[0].code.value)
