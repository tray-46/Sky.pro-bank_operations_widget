"""test_widget.py with tests for widget.py module functions"""

import pytest

from src import widget


# mask_account_card tests
@pytest.mark.parametrize(
    "number_to_mask, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number_to_mask: str, expected: str) -> None:
    assert widget.mask_account_card(number_to_mask) == expected


def test_mask_account_card_no_arg() -> None:
    with pytest.raises(TypeError):
        widget.mask_account_card()


def test_mask_account_card_type_error() -> None:
    with pytest.raises(TypeError):
        widget.mask_account_card(123)


@pytest.mark.parametrize(
    "invalid_number",
    [
        "",
        "12345678901234567890",
        "Счёт12345678901234567890",
        "Visa Platinum 70007922896063611",
        "Maestro 1",
        "Maestro -1",
        "Счет 736541084301358743051",
        "Счет 1",
        "Счет -1",
    ],
)
def test_mask_account_card_value_error(invalid_number: str) -> None:
    with pytest.raises(ValueError):
        widget.mask_account_card(invalid_number)


# get_date tests
def test_get_date() -> None:
    assert widget.get_date("2024-03-11T02:26:16.671407") == "11.03.2024"


def test_get_date_no_arg() -> None:
    with pytest.raises(TypeError):
        widget.get_date()


def test_get_date_invalid_type() -> None:
    with pytest.raises(TypeError):
        widget.get_date(2026)


@pytest.mark.parametrize(
    "invalid_date",
    [
        "2024-11T02:26:16.671407",
        "2024-03-11",
        "2-03-11T02:26:16.671407",
    ],
)
def test_get_date_invalid_date_format(invalid_date: str) -> None:
    with pytest.raises(ValueError):
        widget.get_date(invalid_date)
