from typing import Any, Dict

class StatementProperty:
    id: str
    dataType: str

    def __init__(self, statementProperty: Dict) -> None:
        self.id = statementProperty['id']
        self.dataType = statementProperty['data-type']

class StatementValue:
    type: str
    content: Any

    def __init__(self, statementValue, dataType: str) -> None:
        self.type = statementValue['type']
        if dataType == "wikibase-item":
            self.content = statementValue['content']
        elif dataType == "time":
            self.content = statementValue['content']['time']
            # plus precision
        elif dataType == "string":
            self.content = statementValue['content']
        elif dataType == "quantity":
            self.content = statementValue['content']['amount']
            # plus unit as wikibase-item
        else:
            # Data type not implemented yet
            pass

class Statement:
    id: str
    rank: str
    property: StatementProperty
    value: StatementValue

    def __init__(self, statement: Dict) -> None:
        self.id = statement['id']
        self.rank = statement['rank']
        self.property = StatementProperty(statement['property'])
        self.value = StatementValue(statement['value'], self.property.dataType)