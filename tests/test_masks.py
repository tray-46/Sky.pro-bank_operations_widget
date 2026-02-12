"""test_masks.py with tests for masks.py module functions"""
import pytest

from src import masks

# get_mask_card_number tests
def test_get_mask_card_number():
    assert masks.get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_card_number_no_arg():
    with pytest.raises(TypeError):
        masks.get_mask_card_number()


def test_get_mask_card_number_wrong_type():
    with pytest.raises(TypeError):
        masks.get_mask_card_number("7000792289606361")

def test_get_mask_card_number_negative():
    with pytest.raises(ValueError):
        masks.get_mask_card_number(-7000792289606361)

def test_get_mask_card_number_long():
    with pytest.raises(ValueError):
        masks.get_mask_card_number(12345678901234567)


def test_get_mask_card_number_short():
    with pytest.raises(ValueError):
        masks.get_mask_card_number(1)


# get_mask_account tests
def test_get_mask_account():
    assert masks.get_mask_account(73654108430135874305) == "**4305"

def test_get_mask_account_no_arg():
    with pytest.raises(TypeError):
        masks.get_mask_account()

def test_get_mask_account_negative():
    with pytest.raises(ValueError):
        masks.get_mask_account(-73654108430135874305)

def test_get_mask_account_long():
    with pytest.raises(ValueError):
        masks.get_mask_account(123456789012345678901)


def test_get_mask_account_short():
    with pytest.raises(ValueError):
        masks.get_mask_account(1)

def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        masks.get_mask_account("73654108430135874305")
