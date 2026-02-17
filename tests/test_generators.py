"""test_generators.py with tests for generators.py module functions"""

import pytest

from src import generators


# filter_by_currency tests
@pytest.mark.parametrize(
    "targeted_currency, expected",
    [
        (
            "USD",
            [
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                 'to': 'Счет 11776614605963066702'},
                {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                 'to': 'Счет 75651667383060284188'},
                {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
                 'to': 'Visa Platinum 8990922113665229'}
            ],
        ),
        (
            "RUB",
            [
                {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
                 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
                 'to': 'Счет 74489636417521191160'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
                 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
                 'to': 'Счет 14211924144426031657'}
            ],
        ),
        ("EUR", []),
    ],
)
def test_filter_by_currency_base(transactions_list, targeted_currency, expected) -> None:
    assert list(generators.filter_by_currency(transactions_list, targeted_currency)) == expected


def test_filter_by_currency_no_args() -> None:
    with pytest.raises(TypeError):
        generators.filter_by_currency()  # type: ignore


@pytest.mark.parametrize(
    "invalid_transactions_list",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            123
        ],
        123,
    ]
)
def test_filter_by_currency_invalid_transactions_list(invalid_transactions_list) -> None:
    with pytest.raises(TypeError):
        generators.filter_by_currency(invalid_transactions_list, "USD")


def test_filter_by_currency_invalid_currency_code(transactions_list) -> None:
    with pytest.raises(TypeError):
        generators.filter_by_currency(transactions_list, 123)  # type: ignore


def test_filter_by_currency_no_keys(invalid_transactions_list) -> None:
    expected = [
        {  # no currency code
           "id": 142264268,
           "state": "EXECUTED",
           "date": "2019-04-04T23:20:05.206878",
           "operationAmount": {
               "amount": "79114.93",
               "currency": {
                   "name": "USD",
               }
           },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {  # no operation amount
           "id": 873106923,
           "state": "EXECUTED",
           "date": "2019-03-23T01:09:46.296404",
           "description": "Перевод со счета на счет",
           "from": "Счет 44812258784861134719",
           "to": "Счет 74489636417521191160"
        },
    ]
    assert list(generators.filter_by_currency(invalid_transactions_list, "NOT_SPECIFIED")) == expected


# transaction_descriptions tests
def test_transaction_descriptions_base(transactions_list):
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert list(generators.transaction_descriptions(transactions_list)) == expected


def test_transaction_descriptions_no_args() -> None:
    with pytest.raises(TypeError):
        generators.transaction_descriptions()  # type: ignore


@pytest.mark.parametrize(
    "invalid_transactions_list",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            123
        ],
        123,
    ]
)
def test_transaction_descriptions_invalid_transactions_list(invalid_transactions_list) -> None:
    transaction_descriptions = generators.transaction_descriptions(invalid_transactions_list)
    with pytest.raises(TypeError):
        next(transaction_descriptions)


def test_transaction_descriptions_no_key(invalid_transactions_list) -> None:
    transaction_descriptions = generators.transaction_descriptions(invalid_transactions_list)
    assert next(transaction_descriptions) == 'NO_DESCRIPTION'
    assert next(transaction_descriptions) == 'Перевод со счета на счет'
    assert next(transaction_descriptions) == 'Перевод со счета на счет'
    with pytest.raises(StopIteration):
        next(transaction_descriptions)


# card_number_generator tests
def test_card_number_generator_base():
    card_numbers = generators.card_number_generator(1234123412341200, 1234123412341204)
    assert next(card_numbers) == "1234 1234 1234 1200"
    assert next(card_numbers) == "1234 1234 1234 1201"
    assert next(card_numbers) == "1234 1234 1234 1202"
    assert next(card_numbers) == "1234 1234 1234 1203"
    assert next(card_numbers) == "1234 1234 1234 1204"
    with pytest.raises(StopIteration):
        next(card_numbers)


def test_card_number_generator_no_args():
    with pytest.raises(TypeError):
        generators.card_number_generator()  # type: ignore


def test_card_number_generator_invalid_args():
    with pytest.raises(TypeError):
        next(generators.card_number_generator("123", "456"))  # type: ignore


@pytest.mark.parametrize(
    "start_number, stop_number",
    [
        (-1, 1),
        (1, -1),
        (2, 1),
        (0, 1),
        (99999999999999991, 99999999999999992)
    ]
)
def test_card_number_generator_invalid_range(start_number, stop_number):
    with pytest.raises(ValueError):
        next(generators.card_number_generator(start_number, stop_number))


def test_card_number_generator_min():
    card_numbers = generators.card_number_generator(1, 1)
    assert next(card_numbers) == "0000 0000 0000 0001"
    with pytest.raises(StopIteration):
        next(card_numbers)


def test_card_number_generator_max():
    card_numbers = generators.card_number_generator(9999999999999999, 9999999999999999)
    assert next(card_numbers) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(card_numbers)
