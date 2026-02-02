"""modul with functions to mask bank account and card numbers"""


def get_mask_card_number(card_number: int) -> str:
    """function to get masked bank card number"""
    str_card_number = str(card_number)
    return str_card_number[0:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]


def get_mask_account(account_number: int) -> str:
    """function to get masked bank account number"""
    return "**" + str(account_number)[-4:]
