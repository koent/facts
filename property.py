from abc import ABC, abstractmethod
from typing import List, Type

from barticle import BArticle
from data import LANGUAGES
from debug import DEBUG
import helpers
import grammar

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
        return f"{grammar.conjugate(tense=article.tense)} {grammar.indef_article(description)} {description}"


class Translation(IProperty):
    def id():
        return "C1"

    def weight():
        return 30

    def has(article: BArticle):
        return len(Translation.available_translations(article)) > 0

    def generate_fact(article: BArticle):
        translations = Translation.available_translations(article)
        language_code = helpers.random_choice(list(translations.keys()))
        language = LANGUAGES[language_code]
        translation = translations[language_code]
        return f"{grammar.conjugate(tense=article.tense)} called {translation} in {language}"

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
        language_code, alias = helpers.random_choice(alternative_aliases)
        language = LANGUAGES[language_code]
        return f"{grammar.conjugate(tense=article.tense)} also called {alias} in {language}"


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
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "wikibase-item")
        category = helpers.get_label_from_wikibase_item(statement.content)
        return f"{grammar.conjugate(tense=article.tense)} {grammar.indef_article(category)} {category}"


class DateOfBirth(IProperty):
    def id():
        return "P569"

    def weight():
        return 50

    def has(article: BArticle):
        return DateOfBirth.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[DateOfBirth.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "time")
        date = statement.content['date']
        precision = statement.content['precision']
        datestr = helpers.random_time_representation(date, precision)
        return f"was born {datestr}"


class PlaceOfBirth(IProperty):
    def id():
        return "P19"

    def weight():
        return 50

    def has(article: BArticle):
        return PlaceOfBirth.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[PlaceOfBirth.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "wikibase-item")
        placeOfBirth = helpers.get_label_from_wikibase_item(statement.content)
        return f"was born in {placeOfBirth}"


class DateOfDeath(IProperty):
    def id():
        return "P570"

    def weight():
        return 70

    def has(article: BArticle):
        return DateOfDeath.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[DateOfDeath.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "time")
        date = statement.content['date']
        precision = statement.content['precision']
        datestr = helpers.random_time_representation(date, precision)
        return f"died {datestr}"


class PlaceOfDeath(IProperty):
    def id():
        return "P20"

    def weight():
        return 70

    def has(article: BArticle):
        return PlaceOfDeath.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[PlaceOfDeath.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "wikibase-item")
        placeOfDeath = helpers.get_label_from_wikibase_item(statement.content)
        return f"died in {placeOfDeath}"


class Occupation(IProperty):
    def id():
        return "P106"

    def weight():
        return 300

    def has(article: BArticle):
        return Occupation.id() in article.statements

    def generate_fact(article: BArticle):
        statements = article.statements[Occupation.id()]
        DEBUG and print(f"Number of statements: {len(statements)}")
        statement = helpers.random_choice(statements)
        helpers.verify_data_type(statement, "wikibase-item")
        occupation = helpers.get_label_from_wikibase_item(statement.content)
        return f"{grammar.conjugate(tense = article.tense)} {grammar.indef_article(occupation)} {occupation}"


ALL_PROPERTIES : List[Type[IProperty]] = [
    Description, Translation, Alias, InstanceOf,
    DateOfBirth, PlaceOfBirth, DateOfDeath, PlaceOfDeath,
    Occupation
]
