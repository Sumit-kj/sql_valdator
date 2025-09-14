from common.obj.column_details import ColumnDetails


class TableDetails:
    def __init__(self, name: str, columns: list[ColumnDetails]) -> None:
        self.name = name
        self.columns = columns