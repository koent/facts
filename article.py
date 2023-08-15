import json
from typing import Dict, List, Type
import random

from barticle import BArticle
from property import IProperty, ALL_PROPERTIES

debug = True

class Article(BArticle):
    properties: List[Type[IProperty]]

    def __init__(self, labels, descriptions, aliases, statements, id, **kwargs):
        self.labels = labels
        self.descriptions = descriptions
        self.aliases = aliases
        self.statements = statements
        self.id = id

        if not 'en' in self.labels:
            raise Exception("Not interesting")
        
        self.label = labels['en']
        self.properties = [prop for prop in ALL_PROPERTIES if self.has(prop)]

    def from_json(json_def):
        parameters : Dict = json.loads(json_def)
        return Article(**parameters)

    def has(self, TProperty : Type[IProperty]):
        return TProperty.has(self)
    
    def generate_fact(self):
        if len(self.properties) == 0:
            return f"{self.label} exists."
        
        property = self.random_property()
        if property == None:
            return f"{self.label} exists."

        fact_property = property.generate_fact(self)
        return f"{self.label} {fact_property}."

    def random_property(self) -> Type[IProperty]:
        total = sum([prop.weight() for prop in self.properties])
        value = random.randint(0, total)
        part = 0
        debug and print(value, [p.id() for p in self.properties])
        for prop in self.properties:
            part += prop.weight()
            if value <= part:
                return prop

        return None