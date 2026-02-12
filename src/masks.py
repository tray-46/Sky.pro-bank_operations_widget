"""modul with functions to mask bank account and card numbers"""


def get_mask_card_number(card_number: int) -> str:
    """function to get masked bank card number"""
    if not isinstance(card_number, int):
        raise TypeError("Invalid card number")
    if card_number < 0:
        raise ValueError("Invalid card number")
    str_card_number = str(card_number)
    if len(str_card_number) != 16:  # нужна проверка на 16 или реализация для номеров 12 - 19 ?
        raise ValueError("Invalid card number")
    return str_card_number[0:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]


def get_mask_account(account_number: int) -> str:
    """function to get masked bank account number"""
    if not isinstance(account_number, int):
        raise TypeError("Invalid account number")
    if account_number < 0:
        raise ValueError("Invalid account number")
    if len(str(account_number)) != 20:  # или номер может быть другой длинны?
        raise ValueError("Invalid card number")
    return "**" + str(account_number)[-4:]
