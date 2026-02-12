"""test_masks.py with tests for masks.py module functions"""

import pytest

from src import masks


# get_mask_card_number tests
def test_get_mask_card_number() -> None:
    assert masks.get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_card_number_no_arg() -> None:
    with pytest.raises(TypeError):
        masks.get_mask_card_number()


def test_get_mask_card_number_wrong_type() -> None:
    with pytest.raises(TypeError):
        masks.get_mask_card_number("7000792289606361")


@pytest.mark.parametrize("invalid_number", [-7000792289606361, 12345678901234567, 1])
def test_get_mask_card_number_negative(invalid_number: int) -> None:
    with pytest.raises(ValueError):
        masks.get_mask_card_number(invalid_number)


# get_mask_account tests
def test_get_mask_account() -> None:
    assert masks.get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_account_no_arg() -> None:
    with pytest.raises(TypeError):
        masks.get_mask_account()


def test_get_mask_account_wrong_type() -> None:
    with pytest.raises(TypeError):
        masks.get_mask_account("73654108430135874305")


@pytest.mark.parametrize("invalid_number", [-73654108430135874305, 123456789012345678901, 1])
def test_get_mask_account_negative(invalid_number: int) -> None:
    with pytest.raises(ValueError):
        masks.get_mask_account(invalid_number)
