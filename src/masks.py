"""modul with functions to mask bank account and card numbers"""

import logging
import pathlib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = str(pathlib.Path(__file__).parent.parent / "logs" / "masks.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """function to get masked bank card number"""
    logger.debug(f"Function get_mask_card_number called with card_number: {card_number}")
    if not isinstance(card_number, int):
        logger.error(f"Invalid card number: integer expected, got: {type(card_number)}")
        raise TypeError("Invalid card number")
    if card_number < 0:
        logger.error("Invalid card number: positive integer expected")
        raise ValueError("Invalid card number")
    str_card_number = str(card_number)
    # if len(str_card_number) != 16:  # нужна проверка на 16 или реализация для номеров 12 - 19 ?
    #     logger.error(f"Invalid card number: 16 digits number expected - {str_card_number}")
    if not 11 < len(str_card_number) < 20:
        logger.error("Invalid card number")
        raise ValueError("Invalid cad number")
    asterisk_number = len(str_card_number) - 12
    result = (
        str_card_number[0:4] + " " + str_card_number[4:6] + "** " + "*" * asterisk_number + " " + str_card_number[-4:]
    )
    logger.info(f"Function get_mask_card_number completed successfully with result: {result}")
    return result


def get_mask_account(account_number: int) -> str:
    """function to get masked bank account number"""
    logger.debug(f"Function get_mask_account called with account_number: {account_number}")
    if not isinstance(account_number, int):
        logger.error("Invalid account number: integer expected")
        raise TypeError("Invalid account number")
    if account_number < 0:
        logger.error(f"Invalid account number: positive integer expected, got: {type(account_number)}")
        raise ValueError("Invalid account number")
    # if len(str(account_number)) != 20:  # или номер может быть другой длинны?
    #     logger.error(f"Invalid account number: 20 digits number expected - {account_number}")
    if not 5 < len(str(account_number)) < 35:
        logger.error("Invalid account number")
        raise ValueError("Invalid card number")
    result = "**" + str(account_number)[-4:]
    logger.info(f"Function get_mask_account completed successfully with result: {result}")
    return result
