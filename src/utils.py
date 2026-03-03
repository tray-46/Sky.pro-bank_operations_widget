"""modul with utility functions"""

import json
import pathlib

import src.external_api


def load_transactions_data(file_path_str: str) -> list[dict]:
    """
    function for loading transactions data from JSON file
    :param file_path_str: string with path to JSON file
    :return: transactions data loaded from JSON file, if file not found, empty or contain not a list return empty list
    """
    file_path = pathlib.Path(file_path_str)
    # if not file_path.is_file() or file_path.stat().st_size == 0:
    #     return []
    with open(file_path, "r", encoding="utf-8") as json_file:
        transactions_data = json.load(json_file)
        if not isinstance(transactions_data, list):
            return []
        return transactions_data


def get_transaction_amount(transaction: dict) -> float:
    """
    function to get transaction amount in rubles
    transactions in other currency will be converted at the current rate
    :param transaction: dict with transaction data
    :return: transaction amount in rubles
    """
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency_code != "RUB":
        amount = src.external_api.convert_to_rub(currency_code, amount)
    return float(amount)
