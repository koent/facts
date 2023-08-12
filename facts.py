import math
import random
import requests

# Define parameters
λ = 1 / 100_000  # Parameter for exponential distribution of q. Prob 1 - 1/e^n that q < n*λ


# Define functions
def is_interesting(article):
    if 'en' in article['labels'] and 'en' in article['descriptions']:
        return True


# Initialize variables
q : int = 0
article = None


# Get article
ok = False
while not ok:
    q = math.floor(random.expovariate(λ))
    print(f"Q = {q}")
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v0/entities/items/Q{q}"
    response = requests.get(url)
    if not response.status_code == 200:
        continue
    
    article = response.json()
    ok = is_interesting(article)

# Get fact
title = article['labels']['en']
title = title[0].upper() + title[1:]
description = article['descriptions']['en']
indef_article = "an" if description[0].lower() in "aeiou" else "a"

fact = f"{title} is {indef_article} {description}."

# Write fact
print()
print(fact)

