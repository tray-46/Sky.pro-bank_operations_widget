"""modul with utility functions"""
import collections
import json
import logging
import pathlib

import src.external_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = str(pathlib.Path(__file__).parent.parent / "logs" / "utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions_data(file_path_str: str) -> list[dict]:
    """
    function for loading transactions data from JSON file
    :param file_path_str: string with path to JSON file
    :return: transactions data loaded from JSON file, if file not found, empty or contain not a list return empty list
    """
    logger.debug(f"Function load_transactions_data called with file_path_str: {file_path_str}")
    file_path = pathlib.Path(file_path_str)
    if not file_path.is_file() or file_path.stat().st_size == 0:
        logger.info("Specified file was not found or is empty. Returning empty list")
        return []
    try:
        logger.debug(f"Reading file: {file_path_str}")
        with open(file_path, "r", encoding="utf-8") as json_file:
            logger.debug("Loading json data")
            transactions_data = json.load(json_file)
            if not isinstance(transactions_data, list):
                logger.info(f"Data read from {file_path_str} is not a list object. Returning empty list")
                return []
            logger.info(f"Data read from {file_path_str} is successful. Returning transaction list")
            return transactions_data
    except Exception as e:
        logger.error(f"Function load_transactions_data failed due to exception: {e}. Returning empty list")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """
    function to get transaction amount in rubles
    transactions in other currency will be converted at the current rate
    :param transaction: dict with transaction data
    :return: transaction amount in rubles
    """
    logger.debug("Function get_transaction_amount called")
    try:
        logger.debug("Getting currency code from transaction data")
        currency_code = transaction["operationAmount"]["currency"]["code"]
        logger.debug("Getting amount from transaction data")
        amount = float(transaction["operationAmount"]["amount"])
        if currency_code != "RUB":
            logger.info(f"Converting amount from {currency_code} to rubles with convert_to_rub function")
            amount = src.external_api.convert_to_rub(currency_code, amount)
        logger.info(f"Getting transaction amount is successful. Returning amount: {amount}")
        return amount
    except Exception as e:
        logger.error(f"Function get_transaction_amount failed due to exception: {e}")
        raise e


def get_operations_count(operations_list: list[dict], categories: list[str] = None) -> dict:
    """
    function to get operations count for specified categories
    :param operations_list: list of dict with operations data
    :param categories: list of str with operations categories names to count, if not specified - all categories will be counted
    :return: dict with categories names as keys and number of operations in each category as values
    """
    logger.debug(f"Function get_operations_count called with categories: {categories}")
    if not isinstance(operations_list, list) or not all(isinstance(operation, dict) for operation in operations_list):
        logger.error(f"Invalid operations list")
        raise TypeError("Invalid operations list")
    if categories is not None and (not isinstance(categories, list) or all(isinstance(category, str) for category in categories)):
        logger.error(f"Invalid categories list")
        raise TypeError("Invalid 'categories' value type")
    operations_count = collections.Counter(
        [operation.get("description", "NO_DESCRIPTION") for operation in operations_list])
    if categories is None:
        logger.info(f"Categories to count not specified. Returning stats for all found categories.")
        return operations_count
    else:
        result = dict()
        for category in categories:
                result[category] = operations_count.get(category, 0)
        logger.info(f"Returning stats for specified categories.")
        return result
