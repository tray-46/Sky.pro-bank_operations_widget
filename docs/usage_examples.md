# Usage examples

## masks.py module
1. get_mask_card_number(card_number: int) -> str
```
card_number = 7000792289606361
get_mask_card_number(card_number)
# output: "7000 79** **** 6361"
```

2. get_mask_account(account_number: int) -> str
```
account_number = 73654108430135874305
get_mask_account(account_number)
# output: "**4305"
```

## widget.py module
1. mask_account_card(string_to_mask: str) -> str
```
number_to_mask = "Visa Platinum 7000792289606361"
mask_account_card(number_to_mask)
# output: "Visa Platinum 7000 79** **** 6361"

number_to_mask = "Счет 73654108430135874305"
mask_account_card(number_to_mask)
# output: "Счет **4305"
```

2. get_date(date_string: str) -> str
```
datetime_string = "2024-03-11T02:26:16.671407"
get_date(datetime_string)
# output: "11.03.2024"
```

## processing.py module
1. filter_by_state(operations_list: list[dict], targeted_state: str = "EXECUTED") -> list[dict]
```
bank_operation_list = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filter_by_state(bank_operation_list)
# output:
# [
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

filter_by_state(bank_operation_list, "CANCELED")
# output:
# [
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
```

2. sort_by_date(operations_list: list[dict], *, descending_sorting: bool = True) -> list[dict]
```
bank_operation_list = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sort_by_date(bank_operation_list)
# output:
# [
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

sort_by_date(bank_operation_list, descending_sorting=False)
# output:
# [
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
# ]
```

## generators.py module
1. filter_by_currency(transactions_list: list[dict], targeted_currency_code: str) -> Iterator[dict]:
```
transactions = [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
    {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
    {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'},
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
# output:
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
# {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
```

2. transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None, None]:
```
transactions = [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
    {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
    {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'},
]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
# output:
# "Перевод организации"
# "Перевод со счета на счет"
# "Перевод со счета на счет"
# "Перевод с карты на карту"
# "Перевод организации"
```

3. card_number_generator(start_number: int, stop_number: int) -> Generator[str, None, None]:
```
for card_number in card_number_generator(1, 5):
    print(card_number)
# output:
# "0000 0000 0000 0001"
# "0000 0000 0000 0002"
# "0000 0000 0000 0003"
# "0000 0000 0000 0004"
# "0000 0000 0000 0005"
```

## decorators.py module
1. log(filename: str | None = None) -> Callable:
```
@decorators.log()
def divide_function_console(x: int | float, y: int | float) -> float:
    """function for decorator testing"""
    return x / y


@decorators.log("log.txt")
def divide_function_file(x: int | float, y: int | float) -> float:
    """function for decorator testing"""
    return x / y
    

print(divide_function_console(1, 2))
# output:
# divide_function_console ok
# 0.5

try:
    divide_function_console(1, 0)
except ZeroDivisionError:
    pass
# output:
# divide_function_console error: division by zero. Inputs: (1, 0), {}

divide_function_file(1, 2)
try:
    divide_function_file(1, 0)
except ZeroDivisionError:
    pass
# add the same log messages to the specified file located in the 'logs' directory
```

## utils.py module
1. load_transactions_data(file_path_str: str) -> list[dict]:
```
load_transactions_data("../data/operations.json")
```

2. get_transaction_amount(file_path_str: str) -> list[dict]:  
Function uses convert_to_rub function from <a href="#external_api.py_module">external_api.py</a> module, see below
```
transaction = {"operationAmount": {"amount": "1", "currency": {"code": "RUB"}}}
print(get_transaction_amount(transaction))
# output:
# 1

transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}
print(get_transaction_amount(transaction))
# output:
# 77.6
```

## external_api.py module
1. convert_to_rub(from_currency: str, amount: float) -> float:  
Function uses [Exchange Rates Data API](https://marketplace.apilayer.com/exchangerates_data-api) from APILayer.com  
You will need to provide api key in '.env' file
```
print(convert_to_rub("USD", 1))
# output:
# 77.6
```

## transactions_loading.py module
1. load_transactions_data_csv(file_path_str: str) -> list[dict]:
```
load_transactions_data("../data/transactions.csv")
```

2. load_transactions_data_xlsx(file_path_str: str) -> list[dict]:
```
load_transactions_data("../data/transactions_excel.xlsx")
```
