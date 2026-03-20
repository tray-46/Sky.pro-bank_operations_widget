"""modul with functions for data processing"""

import datetime
import logging
import pathlib
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = str(pathlib.Path(__file__).parent.parent / "logs" / "utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(operations_list: list[dict], targeted_state: str = "EXECUTED") -> list[dict]:
    """function for filtering operations list by targeted state"""
    if not isinstance(operations_list, list) or not all(isinstance(operation, dict) for operation in operations_list):
        raise TypeError("Invalid operations list")
    return [operation for operation in operations_list if operation.get("state", "NO_STATE_KEY") == targeted_state]


def filter_by_description(operations_list: list[dict], description_part: str) -> list[dict]:
    """
    function for filtering operations list by part of description
    :param operations_list: list of dict with operations data
    :param description_part: str with part of description to search
    :return: filtered list of dicts with operations that contain description_part in description
    """
    logger.debug(f"Function filter_by_description called with description_part: {description_part}")
    if not isinstance(operations_list, list) or not all(isinstance(operation, dict) for operation in operations_list):
        logger.error("Invalid operations list")
        raise TypeError("Invalid operations list")
    if not isinstance(description_part, str):
        logger.error("Invalid 'description' value type")
        raise TypeError("Invalid 'description' value type")
    description_pattern = re.compile(description_part, re.IGNORECASE)
    logger.info(f"Returning operations with \"{description_part}\" in description.")
    return [operation for operation in operations_list
            if description_pattern.search(operation.get("description", "NO_DESCRIPTION"))]


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
