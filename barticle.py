from typing import Dict, List

class BArticle:
    labels: Dict[str, str]
    descriptions: Dict[str, str]
    aliases: Dict[str, List[str]]
    id: str
    statements: Dict[str, List]

    @property
    def label(self):
        return self.labels['en']

    @property
    def description(self):
        return self.descriptions['en']