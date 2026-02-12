"""test_widget.py with tests for widget.py module functions"""
import pytest

from src import widget

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
        ("Счет 73654108430135874305", "Счет **4305")
     ]
)
def test_mask_account_card(number_to_mask, expected):
    assert widget.mask_account_card(number_to_mask) == expected


@pytest.mark.parametrize("invalid_number", ["", "12345678901234567890", "Счёт12345678901234567890"])
def test_mask_account_card_value_error(invalid_number):
    with pytest.raises(ValueError):
        widget.mask_account_card(invalid_number)

@pytest.mark.parametrize(
    "invalid_number", ["Visa Platinum 70007922896063611",
                       "Maestro 1",
                       "Maestro -1",
                       "Счет 736541084301358743051",
                       "Счет 1",
                       "Счет -1"
     ]
)
def test_mask_account_card_invalid_numbers(invalid_number):
    with pytest.raises(ValueError):
        widget.mask_account_card(invalid_number)

@pytest.mark.parametrize(
    "invalid_date", ["2024-11T02:26:16.671407",
                       "2024-03-11",
                       "2-03-11T02:26:16.671407",
     ]
)
def test_get_date_invalid_date_format(invalid_date):
    with pytest.raises(ValueError):
        widget.get_date(invalid_date)


def test_get_date_invalid_type():
    with pytest.raises(TypeError):
        widget.get_date(2026)
