from enum import Enum
from typing import Dict, List


class Verb(Enum):
    BE = "be"


class Tense(Enum):
    PAST = 0
    PRESENT = 1
    FUTURE = 2


class Count(Enum):
    SINGULAR = 0
    PLURAL = 1


class Person(Enum):
    FIRST = 0
    SECOND = 1
    THIRD = 2


# infinitive : [present tense singular, past tense singular]
VERB_CONJUGATION: Dict[Verb, List[str]] = {
    Verb.BE : [
        [["was", "were", "was"], ["were", "were", "were"]],
        [["am", "are", "is"], ["are", "are", "are"]],
        [["will be"] * 3] * 2
        ]
}


def conjugate(verb: Verb = Verb.BE, tense: Tense = Tense.PRESENT, count: Count = Count.SINGULAR, person: Person = Person.THIRD) -> str:
    return VERB_CONJUGATION[verb][tense.value][count.value][person.value]


def indef_article(noun: str):
    return "an" if noun[0].lower() in "aeiou" else "a"
