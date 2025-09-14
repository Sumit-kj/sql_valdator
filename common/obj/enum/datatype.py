from enum import Enum


class Datatype(Enum):
    """
    This is the enum for datatype of SQL
    """
    # Numeric Types
    INT = "INT"
    DECIMAL = "DECIMAL"
    NUMERIC = "NUMERIC"
    FLOAT = "FLOAT"

    # Character/String Types
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    TEXT = "TEXT"

    # Date and Time Types
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"

    # Boolean Type
    BOOLEAN = "BOOLEAN"
    BOOL = "BOOL"