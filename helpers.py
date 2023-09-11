import requests
import random
from typing import Callable, List, TypeVar
from datetime import datetime

from statement import Statement
from debug import DEBUG, MINI_DEBUG
from data import DATE_FORMATS

T = TypeVar('T')

def get_label_from_wikibase_item(q_id: str) -> str:
    DEBUG and print(f"GET {q_id}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/{q_id}"
    response = requests.get(url)
    return response.json()['labels']['en']

def verify_data_type(statement: Statement, data_type: str):
    if statement.data_type != data_type:
        raise Exception(f"Data type {data_type} expected but {statement.data_type} found")

def random_choice(statements: List[T]) -> T:
    n = random.randrange(len(statements))
    DEBUG and print(f"Statement/choice index: {n}")
    MINI_DEBUG and print(f"/{n}", end='')
    return statements[n]

def random_time_representation(dt: datetime, precision: int) -> str:
    possible_formats: List[Callable[[datetime], str]] = [f for k,fs in DATE_FORMATS.items() if k <= precision for f in fs]
    format: Callable[[datetime], str] = random.choice(possible_formats)
    return format(dt)
