from abc import ABC, abstractmethod
import random
from typing import List, Type

from barticle import BArticle
from property_data import LANGUAGES
from debug import DEBUG

class IProperty(ABC):
    @staticmethod
    @abstractmethod
    def id(): ...

    @staticmethod
    @abstractmethod
    def weight(): ...

    @staticmethod
    @abstractmethod
    def has(article: BArticle): ...

    @staticmethod
    @abstractmethod
    def generate_fact(article: BArticle): ...


class Description(IProperty):
    def id():
        return "C0"

    def weight():
        return 10

    def has(article: BArticle):
        return 'en' in article.descriptions

    def generate_fact(article: BArticle):
        description = article.descriptions['en']
        indef_article = "an" if description[0].lower() in "aeiou" else "a"
        return f"is {indef_article} {description}"


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
        return 100

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


ALL_PROPERTIES : List[Type[IProperty]] = [Description, Translation, Alias]
