"""module with functions working with external APIs"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def convert_to_rub(from_currency: str, amount: float) -> float:
    """
    function to convert amount in given currency to rubles
    :param from_currency: three-letter currency code of the currency to convert from
    :param amount: amount to be converted
    :return: amount converted to rubles
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": amount, "from": from_currency, "to": "RUB"}
    headers = {"apikey": API_KEY}
    response = requests.get(url, params=str(payload), headers=headers)
    if response.status_code == 200:
        result: float = round(response.json()["result"], 2)
        return result
    raise Exception(f"Conversion failed: {from_currency} {amount}")
