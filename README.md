# Facts

Script that generate facts. No guarantees that the facts are interesting.

### Prerequisites

Python 3 needs to be installed, with the `abc`, `json`, `math`, `random`, `request`, `sys` and `typing` packages.

### Using

Run `python3 facts.py` to get a fact about a random article.

Run `python3 facts.py article.json` to get a fact about the article described in `article.json`.

### Examples

```
> python3 facts.py
Hans Graf von Sponeck is a German general.
```
```
> python3 facts.py
Pisonia is a genus of plants.
```
```
> python3 facts.py
Truttikon is a municipality in Switzerland.
```
```
> python3 facts.py
Wilson Kamavuaka is a Congolese footballer.
```

### Developing

You can turn on debug messages by setting `debug = True` under parameter definitions.


### Source

Data comes from [Wikidata](http://www.wikidata.org/).
