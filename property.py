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

class EnLabel(IProperty):
    def id():
        return None

    def weight():
        return 0

    def has(article: BArticle):
        return 'en' in article.labels

    def get(article: BArticle):
        label = article.labels['en']
        return label[0].upper() + label[1:]

    def generate_fact(article):
        raise Exception("EnLabel cannot generate fact")


class EnDescription(IProperty):
    def id():
        return None

    def weight():
        return 10

    def has(article: BArticle):
        return 'en' in article.descriptions

    def get(article: BArticle):
        return article.descriptions['en']

    def generate_fact(article: BArticle):
        description = EnDescription.get(article)
        indef_article = "an" if description[0].lower() in "aeiou" else "a"
        return f"is {indef_article} {description}"

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
        title = EnLabel.get(article)
        return {k:v for k,v in article.labels.items() if not v == title and k in Translation.languages}
