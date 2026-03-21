import pytest


@pytest.fixture
def bank_operation_list() -> list[dict]:
    return [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064592, "date": "2018-10-14T08:21:33.419441"},
        {
            "id": 615064593,
        },
    ]


@pytest.fixture
def invalid_bank_operation_list() -> list:
    return [
        [
            {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            "{ id : 939719570,  state :  EXECUTED ,  date :  2018-06-30T02:08:58.425572}",
            594226727,
        ],
        [],
        123,
    ]


@pytest.fixture
def transactions_list() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def invalid_transactions_list() -> list:
    return [
        {  # no description
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {  # no currency code
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                },
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {  # no operation amount
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.fixture
def usd_transactions() -> dict:
    return {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}


@pytest.fixture
def operations_to_filter() -> list:
    return [
        {
            "id": 441945886,
            "description": "Перевод организации",
        },
        {
            "id": 41428829,
            "description": "Открытие вклада",
        },
        {
            "id": 939719570,
            "description": "Перевод со счета на счет",
        },
        {
            "id": 587085106,
            "description": "Перевод с карты на карту",
        },
        {
            "id": 142264268,
            "description": "Перевод с карты на счет",
        },
    ]


@pytest.fixture
def operations_list_json() -> list:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2026-03-20T15:15:15.151515",
            "operationAmount": {"amount": "11.11", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 939719570,
            "state": "PENDING",
            "date": "2026-03-19T15:15:15.151515",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2026-03-19T14:14:14.141414",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "CANCELED",
            "date": "2026-03-18T15:15:15.151515",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2026-03-18T13:13:13.131313",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.fixture
def transactions_list_csv_xlsx_format() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "name": "USD",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "name": "USD",
            "currency_code": "USD",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2026-03-19T14:14:14.141414",
            "amount": "48223.05",
            "name": "руб.",
            "currency_code": "RUB",
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
