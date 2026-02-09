# Sky.pro-bank_operations_widget

<details>
    <summary>Table of Content</summary>
    <ol>
        <li>
            <a href="#about-the-project">About the project</a>
        </li>
        <li>
          <a href="#getting-started">Getting started</a>
        </li>
        <li>
          <a href="#usage">Usage</a>
        </li>
    </ol>
</details>

## About the project
A training project - implementing the backend portion of a banking widget displaying a list of the most recent successfully completed transactions

### Build with
* [![Python](https://img.shields.io/badge/Python%20IDLE-3776AB?logo=python&logoColor=fff)](https://python.org/)
* [![PyCharm](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff)](https://www.jetbrains.com/pycharm/)

## Getting started
To clone the repository use the following links:

* with HTTPS:
```
    https://github.com/tray-46/Sky.pro-bank_operations_widget.git
```

* with SSH:  
```
    git@github.com:tray-46/Sky.pro-bank_operations_widget.git
```

## Usage
The following functions are implemented in the project:
1. function to get masked bank card number:  
`get_mask_card_number`

2. function to get masked bank account number:  
`get_mask_account`

3. function to get masked bank account or card number:  
`mask_account_card`

4. function to get formatted date string:  
`get_date`

5. function for filtering operations list by targeted state:  
`filter_by_state`

6. function for sorting operations list by date:  
`sort_by_date`

### Usage examples
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

3. mask_account_card(string_to_mask: str) -> str
```
number_to_mask = "Visa Platinum 7000792289606361"
mask_account_card(number_to_mask)
# output: "Visa Platinum 7000 79** **** 6361"

number_to_mask = "Счет 73654108430135874305"
mask_account_card(number_to_mask)
# output: "Счет **4305"
```

4. get_date(date_string: str) -> str
```
datetime_string = "2024-03-11T02:26:16.671407"
get_date(datetime_string)
# output: "11.03.2024"
```

5. filter_by_state(operations_list: list[dict], targeted_state: str = "EXECUTED") -> list[dict]
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
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

filter_by_state(bank_operation_list, "CANCELED")
# output:
# [
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
```

6. sort_by_date(operations_list: list[dict], *, descending_sorting: bool = True) -> list[dict]
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
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

sort_by_date(bank_operation_list, descending_sorting=False)
# output:
# [
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
# ]
```
