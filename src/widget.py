"""modul with basic functions of widget"""
import datetime

from src import masks

def mask_account_card(string_to_mask: str) -> str:
    """function to get masked bank account or card number"""
    string_parts = string_to_mask.split()
    if len(string_parts) < 2:
        raise ValueError("Invalid account/card number")
    if string_parts[0] == "Счет":
        try:
            account_number = int(string_parts[-1])
            return f"{string_parts[0]} {masks.get_mask_account(account_number)}"
        except ValueError:
            raise ValueError("Invalid account number")
    else:
        try:
            card_number = int(string_parts[-1])
            return f"{" ".join(string_parts[:-1])} {masks.get_mask_card_number(card_number)}"
        except ValueError:
            raise ValueError("Invalid card number")


def get_date(date_string: str) -> str:
    """function to get formatted date string. required format is 'dd.mm.yyyy'"""
    if not isinstance(date_string, str):
        raise TypeError("Invalid date")
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
    try:
        datetime_date = datetime.datetime.strptime(date_string, datetime_format)
    except ValueError:
        raise ValueError("Invalid date format")
    return datetime_date.strftime("%d.%m.%Y")
