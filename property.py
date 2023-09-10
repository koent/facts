from abc import ABC, abstractmethod
import random
from typing import List, Type

from barticle import BArticle
from property_data import LANGUAGES
from debug import DEBUG
import helpers
from datetime import datetime

class IProperty(ABC):
    @staticmethod
    @abstractmethod
    def id() -> str: ...

    @staticmethod
    @abstractmethod
    def weight() -> int: ...

    @staticmethod
    @abstractmethod
    def has(article: BArticle) -> bool: ...

    @staticmethod
    @abstractmethod
    def generate_fact(article: BArticle) -> str: ...


class Description(IProperty):
    def id():
        return "C0"

    def weight():
        return 10

    def has(article: BArticle):
        return 'en' in article.descriptions

    def generate_fact(article: BArticle):
        description = article.descriptions['en']
        return f"is {helpers.indef_article(description)} {description}"


class Translation(IProperty):
    def id():
        return "C1"

    def weight():
        return 30

    def has(article: BArticle):
        return len(Translation.available_translations(article)) > 0

    def generate_fact(article: BArticle):
        translations = Translation.available_translations(article)
        language_code = random.choice(list(translations.keys()))
        language = LANGUAGES[language_code]
        translation = translations[language_code]
        return f"is called {translation} in {language}"

    def available_translations(article: BArticle):
        return {k:v for k,v in article.labels.items() if not v == article.label and k in LANGUAGES}


class Alias(IProperty):
    def id():
        return "C2"

    def weight():
        return 30

    def has(article: BArticle):
        for language, aliases in article.aliases:
            for alias in aliases:
                if not alias == article.label:
                    return True

        return False

    def generate_fact(article: BArticle):
        alternative_aliases = [(language_code, alias) for language_code, aliases in article.aliases.items() for alias in aliases if not alias == article.label]
        language_code, alias = random.choice(alternative_aliases)
        language = LANGUAGES[language_code]
        return f"is also called {alias} in {language}"


class InstanceOf(IProperty):
    def id():
        return "P31"

    def weight():
        return 50

    def has(article: BArticle):
        return InstanceOf.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[InstanceOf.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = random.choice(statements)
        helpers.verify_datatype(statement, "wikibase-item")
        category = helpers.get_label_from_wikibase_item(statement.value.content)
        return f"is {helpers.indef_article(category)} {category}"


class DateOfBirth(IProperty):
    def id():
        return "P569"

    def weight():
        return 150

    def has(article: BArticle):
        return DateOfBirth.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[DateOfBirth.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = random.choice(statements)
        helpers.verify_datatype(statement, "time")
        date = datetime.fromisoformat(statement.value.content[1:-1])
        return f"was born on {date:%A, %B %-d, %Y}"


class PlaceOfBirth(IProperty):
    def id():
        return "P19"

    def weight():
        return 150

    def has(article: BArticle):
        return PlaceOfBirth.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[PlaceOfBirth.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = random.choice(statements)
        helpers.verify_datatype(statement, "wikibase-item")
        placeOfBirth = helpers.get_label_from_wikibase_item(statement.value.content)
        return f"was born in {placeOfBirth}"


class DateOfDeath(IProperty):
    def id():
        return "P570"

    def weight():
        return 200

    def has(article: BArticle):
        return DateOfDeath.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[DateOfDeath.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = random.choice(statements)
        helpers.verify_datatype(statement, "time")
        date = datetime.fromisoformat(statement.value.content[1:-1])
        return f"died on {date:%A, %B %-d, %Y}"


class PlaceOfDeath(IProperty):
    def id():
        return "P20"

    def weight():
        return 200

    def has(article: BArticle):
        return PlaceOfDeath.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[PlaceOfDeath.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = random.choice(statements)
        helpers.verify_datatype(statement, "wikibase-item")
        placeOfDeath = helpers.get_label_from_wikibase_item(statement.value.content)
        return f"died in {placeOfDeath}"


ALL_PROPERTIES : List[Type[IProperty]] = [
    Description, Translation, Alias, InstanceOf,
    DateOfBirth, PlaceOfBirth, DateOfDeath, PlaceOfDeath
]
