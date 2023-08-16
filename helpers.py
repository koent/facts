import requests

from debug import DEBUG

def get_label(q_id: str):
    DEBUG and print(f"GET {q_id}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/{q_id}"
    response = requests.get(url)
    return response.json()['labels']['en']

def indef_article(noun: str):
    return "an" if noun[0].lower() in "aeiou" else "a"