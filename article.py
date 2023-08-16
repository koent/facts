import json
from typing import Dict, List, Type
import random

from barticle import BArticle
from debug import DEBUG
from property import IProperty, ALL_PROPERTIES
from statement import Statement

class Article(BArticle):
    properties: List[Type[IProperty]]

    def __init__(self, labels, descriptions, aliases, statements : Dict, id, **kwargs):
        self.labels = labels
        self.descriptions = descriptions
        self.aliases = aliases
        self.statements = {k:[Statement(s) for s in ss] for k,ss in statements.items()}
        self.id = id

        if not 'en' in self.labels:
            raise Exception("Not interesting")

        self.label = labels['en']
        self.capitalized_label = self.label[0].upper() + self.label[1:]
        self.properties = [prop for prop in ALL_PROPERTIES if self.has(prop)]
        DEBUG and print(f"Available properties: {[p.id() for p in self.properties]}")

    def from_json(json_def):
        parameters : Dict = json.loads(json_def)
        return Article(**parameters)

    def has(self, TProperty : Type[IProperty]):
        return TProperty.has(self)

    def generate_fact(self):
        if len(self.properties) == 0:
            return f"{self.capitalized_label} exists."

        property = self.random_property()
        if property == None:
            return f"{self.capitalized_label} exists."

        DEBUG and print(f"Using property {property.id()}")
        fact_property = property.generate_fact(self)
        return f"{self.capitalized_label} {fact_property}."

    def random_property(self) -> Type[IProperty]:
        total = sum([prop.weight() for prop in self.properties])
        value = random.randint(0, total)
        part = 0
        DEBUG and print(f"Random property value: {value}")
        for prop in self.properties:
            part += prop.weight()
            if value <= part:
                return prop

        return None