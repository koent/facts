import json
import math
import random
import requests
import sys

from property import *

# Define parameters
λ_inv = 100_000  # Parameter for exponential distribution of q. Prob 1 / e^n that q > n * λ_inv
debug = False

# Define functions
def is_interesting(article):
    if EnLabel.has(article) and EnDescription.has(article):
        return True


# Initialize variables
q : int = 0
article = None

# Load article
if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as f:
        article = json.load(f)

# Get article
ok = not article == None
while not ok:
    q = math.floor(random.expovariate(1 / λ_inv))
    debug and print(f"Q = {q}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/Q{q}"
    response = requests.get(url)
    if not response.status_code == 200:
        continue

    article = response.json()
    ok = is_interesting(article)

# Get fact
title = EnLabel.get(article)
fact_property = EnDescription.generate_fact(article)
fact = f"{title} {fact_property}."

# Write fact
debug and print("---")
print(fact)

