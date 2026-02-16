"""module with functions for working with transaction arrays"""
from typing import Generator, Iterator


def filter_by_currency(transactions_list: list[dict], targeted_currency_code: str) -> Iterator[dict]:
    """function to get iterator with transactions filtered by currency"""
    return filter(lambda transaction:
                  transaction.get("operationAmount", {})
                  .get("currency", {}).get("code", "NOT_SPECIFIED") == targeted_currency_code, transactions_list)


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None, None]:
    """generator function to get transactions descriptions"""
    for description in (transaction.get("description", "NO_DESCRIPTION") for transaction in transactions_list):
        yield description


def card_number_generator(start_number: int, stop_number: int) -> Generator[str, None, None]:
    """generator function for generating card numbers within a given range"""
    for number in range(start_number, stop_number + 1):
        card_number = f"{number:016}"
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


# f_trans = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(f_trans))
#
# descrs = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descrs))
#
# cards = card_number_generator(1000000,5000000)
# for _ in range(5):
#     print(next(cards))
