"""modul with functions for data processing"""


def filter_by_state(operations_list: list[dict], targeted_state: str = "EXECUTED") -> list[dict]:
    """function for filtering operations list by targeted state"""
    return [operation for operation in operations_list if operation.get("state", "NO_STATE_KEY") == targeted_state]


def sort_by_date(operations_list: list[dict], *, descending_sorting: bool = True) -> list[dict]:
    """function for sorting operations list by date"""
    return sorted(operations_list, key=lambda operation: operation.get('date'), reverse = descending_sorting)
