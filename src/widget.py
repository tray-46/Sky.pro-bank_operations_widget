"""modul with basic functions of widget"""
import datetime

from src import masks

def mask_account_card(string_to_mask: str) -> str:
    """function to get masked bank account or card number"""
    string_parts = string_to_mask.split()
    if string_parts[0] == "Счет":
        return f"{string_parts[0]} {masks.get_mask_account(int(string_parts[-1]))}"
    else:
        return f"{" ".join(string_parts[:-1])} {masks.get_mask_card_number(int(string_parts[-1]))}"


def get_date(date_string: str) -> str:
    """function to get formatted date string. required format is 'dd.mm.yyyy'"""
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
    datetime_date = datetime.datetime.strptime(date_string, datetime_format)
    return datetime_date.strftime("%d.%m.%Y")
