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

        if not self.is_interesting():
            raise Exception("Not interesting")

    def from_json(json_def):
        parameters : Dict = json.loads(json_def)
        return Article(**parameters)

    def is_interesting(self):
        return 'en' in self.labels and 'en'in self.descriptions

    def has(self, TProperty : Type[IProperty]):
        return TProperty.has(self)

    def get(self, TProperty : Type[IProperty]):
        return TProperty.get(self)

    def description_fact(self):
        indef_article = "an" if self.description[0].lower() in "aeiou" else "a"
        return f"is {indef_article} {self.description}"

    def generate_fact(self, TProperty : Type[IProperty]):
        return TProperty.generate_fact(self)
