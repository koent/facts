from abc import ABC, abstractmethod
import random

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
    def get(article: BArticle): ...

    @staticmethod
    @abstractmethod
    def generate_fact(article: BArticle): ...


class Description(IProperty):
    def id():
        return None

    def weight():
        return 10

    def has(article: BArticle):
        return True

    def get(article: BArticle):
        return article.description

    def generate_fact(article: BArticle):
        indef_article = "an" if article.description[0].lower() in "aeiou" else "a"
        return f"is {indef_article} {article.description}"


class Translation(IProperty):
    languages = {'en' : "English", 'fr' : "French", 'ru': "Russian", 'el': "Greek"}

    def id():
        return None

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
