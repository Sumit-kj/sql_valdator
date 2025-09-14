from common.obj.column_details import ColumnDetails


class TableDetails:
    def __init__(self, name: str, columns: list[ColumnDetails]) -> None:
        self.name = name
        self.columns = columns

    def to_dict(self) -> dict:
        """
        This function converts the object into dict
        :return: The dict of the object
        """
        return {
            "name": self.name,
            "columns": [col.to_dict() for col in self.columns]
        }