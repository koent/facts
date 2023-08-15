from abc import ABC, abstractmethod
import random
from typing import List, Type

from barticle import BArticle

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
    languages = {'en' : "English", 'fr' : "French", 'ru': "Russian", 'el': "Greek"}

    def id():
        return "C1"

    def weight():
        return 10

    def has(article: BArticle):
        return len(Translation.available_translations(article)) > 0

    def generate_fact(article: BArticle):
        translations = Translation.available_translations(article)
        language_code = random.choice(list(translations.keys()))
        language = Translation.languages[language_code]
        translation = translations[language_code]
        return f"is called {translation} in {language}"

    def available_translations(article: BArticle):
        title = article.label
        return {k:v for k,v in article.labels.items() if not v == title and k in Translation.languages}

ALL_PROPERTIES : List[Type[IProperty]] = [Description, Translation]
