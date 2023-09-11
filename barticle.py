from typing import Dict, List

from statement import Statement
from grammar import Tense

class BArticle:
    labels: Dict[str, str]
    descriptions: Dict[str, str]
    aliases: Dict[str, List[str]]
    id: str
    statements: Dict[str, List[Statement]]
    label: str
    capitalized_label: str
    tense: Tense
