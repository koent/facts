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
Echinocereus triglochidiatus is a taxon.
```
```
> python3 facts.py
Miklós Szentkuthy is called Сенткути, Миклош in Russian.
```
```
> python3 facts.py
Truttikon is a municipality in Switzerland.
```
```
> python3 facts.py
Otto Haupt is a human.
```

### Developing

You can turn on debug messages by setting `DEBUG = True` in `debug.py`.


### Source

Data comes from [Wikidata](http://www.wikidata.org/).
