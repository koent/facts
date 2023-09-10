import math
import random
import requests
import sys

from article import Article
from debug import DEBUG, MINI_DEBUG

# Define parameters
λ_inv = 100_000  # Parameter for exponential distribution of q. Prob 1 / e^n that q > n * λ_inv

# Initialize variables
q : int = 0
article = None

# Load article
if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as f:
        article = Article.from_json(f.read())

# Get article
ok = not article == None
while not ok:
    q = math.floor(random.expovariate(1 / λ_inv))
    DEBUG and print(f"Q = {q}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/Q{q}"
    response = requests.get(url)
    if not response.status_code == 200:
        DEBUG and print(f"Status code {response.status_code}")
        continue

    try:
        article = Article.from_json(response.text)
        ok = True
    except Exception as ex:
        DEBUG and print(f"Could not parse article: {ex}")
        continue

MINI_DEBUG and print(f"Q{q}", end='')

# Get fact
fact = article.generate_fact()

# Write fact
DEBUG and print("---")
MINI_DEBUG and print()
print(fact)
