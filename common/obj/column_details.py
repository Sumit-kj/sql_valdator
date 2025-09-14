from common.obj.enum.datatype import Datatype


class ColumnDetails:
    def __init__(self, name: str, datatype: Datatype) -> None:
        self.name = name
        self.datatype = datatype

    def to_dict(self) -> dict:
        """
        This function creates the object into dict
        :return: Dictionary of the object
        """
        return {
            "name": self.name,
            "datatype": self.datatype
        }
