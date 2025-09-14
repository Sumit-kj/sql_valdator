from common.obj.enum.datatype import Datatype


class ColumnDetails:
    def __init__(self, name: str, datatype: Datatype) -> None:
        self.name = name
        self.datatype = datatype
