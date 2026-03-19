"""modul with functions for data processing"""

import datetime


def filter_by_state(operations_list: list[dict], targeted_state: str = "EXECUTED") -> list[dict]:
    """function for filtering operations list by targeted state"""
    if not isinstance(operations_list, list) or not all(isinstance(operation, dict) for operation in operations_list):
        raise TypeError("Invalid operations list")
    return [operation for operation in operations_list if operation.get("state", "NO_STATE_KEY") == targeted_state]


def sort_by_date(operations_list: list[dict], *, descending_sorting: bool = True) -> list[dict]:
    """function for sorting operations list by date"""
    if not isinstance(operations_list, list) or not all(isinstance(operation, dict) for operation in operations_list):
        raise TypeError("Invalid operations list")
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
    try:
        sorted_operations_list = sorted(
            operations_list,
            key=lambda operation: datetime.datetime.strptime(
                operation.get("date", "1970-01-01T00:00:00.0"), datetime_format
            ),
            reverse=descending_sorting,
        )
    except TypeError:
        raise TypeError("Invalid 'date' value type")
    except ValueError:
        raise ValueError("Invalid 'date' value format")
    return sorted_operations_list
