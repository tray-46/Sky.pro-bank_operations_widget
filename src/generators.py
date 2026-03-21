"""module with functions for working with transaction arrays"""

from typing import Generator, Iterator


def filter_by_currency(transactions_list: list[dict], targeted_currency_code: str) -> Iterator[dict]:
    """function to get iterator with transactions filtered by currency"""
    if (
        not isinstance(transactions_list, list)
        or not all(isinstance(transaction, dict) for transaction in transactions_list)
        or not isinstance(targeted_currency_code, str)
    ):
        raise TypeError("Invalid transactions list")
    if "operationAmount" in transactions_list[0]:
        return filter(
            lambda transaction: transaction.get("operationAmount", {}).get("currency", {}).get("code", "NOT_SPECIFIED")
            == targeted_currency_code,
            transactions_list,
        )
    else:
        return filter(
            lambda transaction: transaction.get("currency_code", "NOT_SPECIFIED") == targeted_currency_code,
            transactions_list,
        )


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None, None]:
    """generator function to get transactions descriptions"""
    if not isinstance(transactions_list, list) or not all(
        isinstance(transaction, dict) for transaction in transactions_list
    ):
        raise TypeError("Invalid transactions list")
    for description in (transaction.get("description", "NO_DESCRIPTION") for transaction in transactions_list):
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """generator function for generating card numbers within a given range"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Invalid range parameters")
    if start < 1 or stop < 1 or start > stop or stop > 9999999999999999:
        raise ValueError("Invalid range parameters")
    for number in range(start, stop + 1):
        card_number = f"{number:016}"
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
