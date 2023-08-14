from typing import Dict, List

class BArticle:
    labels: Dict[str, str]
    descriptions: Dict[str, str]
    aliases: Dict[str, List[str]]
    id: str
    statements: Dict[str, List]