"""module with functions working with external APIs"""

import logging
import os
import pathlib

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = str(pathlib.Path(__file__).parent.parent / "logs" / "external_api.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def convert_to_rub(from_currency: str, amount: float) -> float:
    """
    function to convert amount in given currency to rubles
    :param from_currency: three-letter currency code of the currency to convert from
    :param amount: amount to be converted
    :return: amount converted to rubles
    """
    logger.debug(f"Function convert_to_rub called with from_currency: {from_currency} and amount: {amount}")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": amount, "from": from_currency, "to": "RUB"}
    headers = {"apikey": API_KEY}
    try:
        logger.info("Executing request to Exchange Rates Data API")
        response = requests.get(url, params=str(payload), headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Function get_transaction_amount failed due to exception: {e}")
        raise e
    try:
        logger.info("Processing the response from Exchange Rates API")
        if response.status_code == 200:
            result: float = round(response.json()["result"], 2)
            logger.info(f"Function convert_to_rub completed successfully with result: {result}")
            return result
    except Exception as e:
        logger.error(f"Function get_transaction_amount failed due to exception: {e}")
        raise e
    logger.error("Function get_transaction_amount failed")
    raise Exception(f"Conversion failed: {from_currency} {amount}")
