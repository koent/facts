from abc import ABC, abstractmethod

class Property(ABC):
    @staticmethod
    @abstractmethod
    def id(): ...

    @staticmethod
    @abstractmethod
    def weight(): ...

    @staticmethod
    @abstractmethod
    def has(article): ...

    @staticmethod
    @abstractmethod
    def get(article): ...

    @staticmethod
    @abstractmethod
    def generate_fact(article): ...

class EnLabel(Property):
    def id():
        return None
    
    def weight():
        return 0
    
    def has(article):
        return 'en' in article['labels']
    
    def get(article):
        label = article['labels']['en']
        return label[0].upper() + label[1:]
    
    def generate_fact(article):
        raise Exception("EnLabel cannot generate fact")


class EnDescription(Property):
    def id():
        return None
    
    def weight():
        return 10
    
    def has(article):
        return 'en' in article['descriptions']
    
    def get(article):
        return article['descriptions']['en']
    
    def generate_fact(article):
        description = EnDescription.get(article)
        indef_article = "an" if description[0].lower() in "aeiou" else "a"
        return f"is {indef_article} {description}"
    