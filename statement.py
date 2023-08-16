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

    def __init__(self, statementValue) -> None:
        self.type = statementValue['type']
        self.content = statementValue['content']

class Statement:
    id: str
    rank: str
    property: StatementProperty
    value: StatementValue

    def __init__(self, statement: Dict) -> None:
        self.id = statement['id']
        self.rank = statement['rank']
        self.property = StatementProperty(statement['property'])
        self.value = StatementValue(statement['value'])