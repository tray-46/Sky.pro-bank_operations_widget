"""test_masks.py with tests for masks.py module functions"""
from src import masks

def test_get_mask_card_number():
    assert masks.get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_get_mask_account():
    assert masks.get_mask_account(73654108430135874305) == "**4305"
