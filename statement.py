from typing import Any, Dict
from datetime import datetime

class Statement:
    id: str
    rank: str
    data_type: str
    content: Any

    def __init__(self, statement: Dict) -> None:
        self.id = statement['id']
        self.rank = statement['rank']
        self.data_type = statement['property']['data-type']
        self.set_content(statement['value'])

    def set_content(self, statementValue: Dict):
        if self.data_type == "wikibase-item":
            self.content = statementValue['content']
        elif self.data_type == "time":
            # Precision: https://www.wikidata.org/wiki/Help:Dates
            precision = int(statementValue['content']['precision'])
            if precision >= 11: # day
                self.content = datetime.fromisoformat(statementValue['content']['time'][1:-1])
            elif precision >= 6: # millenium
                year = int(statementValue['content']['time'][1:5])
                self.content = datetime(year, 1, 1)
            else:
                self.content = datetime(0, 1, 1)
        elif self.data_type == "string":
            self.content = statementValue['content']
        elif self.data_type == "quantity":
            self.content = statementValue['content']['amount']
            # plus unit as wikibase-item
        else:
            # Data type not implemented yet
            pass
