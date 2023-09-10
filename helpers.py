import requests
import random
from typing import Any, List

from statement import Statement
from debug import DEBUG, MINI_DEBUG

def get_label_from_wikibase_item(q_id: str):
    DEBUG and print(f"GET {q_id}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/{q_id}"
    response = requests.get(url)
    return response.json()['labels']['en']


def indef_article(noun: str):
    return "an" if noun[0].lower() in "aeiou" else "a"


def verify_data_type(statement: Statement, data_type: str):
    if statement.data_type != data_type:
        raise Exception(f"Data type {data_type} expected but {statement.data_type} found")

def random_choice(statements: List[Any]):
    n = random.randrange(len(statements))
    DEBUG and print(f"Statement/choice index: {n}")
    MINI_DEBUG and print(f"/{n}", end='')
    return statements[n]
