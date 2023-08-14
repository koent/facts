import json
from typing import Dict, List, Type

from barticle import BArticle
from property import *

class Article(BArticle):
    def __init__(self, labels, descriptions, aliases, statements, id, **kwargs):
        self.labels = labels
        self.descriptions = descriptions
        self.aliases = aliases
        self.statements = statements
        self.id = id

    def from_json(json_def):
        parameters : Dict = json.loads(json_def)
        return Article(**parameters)

    def is_interesting(self):
        return self.has(EnLabel) and self.has(EnDescription)

    def has(self, TProperty : Type[IProperty]):
        return TProperty.has(self)

    def get(self, TProperty : Type[IProperty]):
        return TProperty.get(self)

    def generate_fact(self, TProperty : Type[IProperty]):
        return TProperty.generate_fact(self)
