"""test_utils.py with tests for utils.py module functions"""

import json
import pathlib
import typing
from unittest.mock import Mock, patch

import pytest

import src.utils


def test_load_transactions_data_bad_file() -> None:
    assert src.utils.load_transactions_data("non_existing_file.json") == []
    mock_stat_result = Mock(st_size=0)
    with patch("pathlib.Path.stat", return_value=mock_stat_result):
        assert src.utils.load_transactions_data("../data/operations.json") == []


@patch("json.load")
def test_load_transactions_data(mock_load: Mock) -> None:
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "operations.json")
    mock_load.return_value = 1
    assert src.utils.load_transactions_data(file_path) == []
    mock_load.return_value = []
    assert src.utils.load_transactions_data(file_path) == []
    mock_load.return_value = [
        {
            "id": 1,
        }
    ]
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "operations.json")
    result = src.utils.load_transactions_data(file_path)
    assert result == [
        {
            "id": 1,
        }
    ]


@patch("json.load")
def test_load_transactions_data_json_error(mock_load: Mock) -> None:
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "operations.json")
    mock_load.side_effect = json.JSONDecodeError("Invalid JSON", "1", 0)
    assert src.utils.load_transactions_data(file_path) == []
    mock_load.assert_called_once()


def test_get_transaction_amount() -> None:
    assert src.utils.get_transaction_amount({"operationAmount": {"amount": "1", "currency": {"code": "RUB"}}}) == 1


@patch("src.external_api.convert_to_rub")
def test_get_transaction_amount_not_rub(mock_convert_to_rub: Mock, usd_transactions: dict) -> None:
    mock_convert_to_rub.return_value = 1
    assert src.utils.get_transaction_amount(usd_transactions) == 1


@patch("src.external_api.convert_to_rub")
def test_get_transaction_amount_convert_to_rub_error(mock_convert_to_rub: Mock, usd_transactions: dict) -> None:
    mock_convert_to_rub.side_effect = Exception()
    with pytest.raises(Exception):
        src.utils.get_transaction_amount(usd_transactions)


def test_get_operations_count(operations_to_filter: list[dict]) -> None:
    expected = {
        "Перевод организации": 1,
        "Открытие вклада": 1,
        "Перевод со счета на счет": 1,
        "Перевод с карты на карту": 1,
        "Перевод с карты на счет": 1,
    }
    assert src.utils.get_operations_count(operations_to_filter) == expected


@pytest.mark.parametrize(
    "categories,expected",
    [
        (["Перевод организации"], {"Перевод организации": 1, }),
        (["Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту"],
         {"Открытие вклада": 1, "Перевод со счета на счет": 1, "Перевод с карты на карту": 1, }),
        (["Открытие вклада", "Перевод со счета на счет", "Non_existing_operation"],
         {"Открытие вклада": 1, "Перевод со счета на счет": 1, "Non_existing_operation": 0, }),
    ],
)
def test_get_operations_count_with_categories(operations_to_filter: list[dict],
                                              categories: list, expected: dict) -> None:
    assert src.utils.get_operations_count(operations_to_filter, categories) == expected


@pytest.mark.parametrize(
    "invalid_operation_list",
    [
        (
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                "{ id : 939719570,  state :  EXECUTED ,  date :  2018-06-30T02:08:58.425572}",
                594226727,
            ]
        ),
        (),
        (123,),
    ],
)
def test_get_operations_count_invalid_list_dict(invalid_operation_list: list) -> None:
    with pytest.raises(TypeError):
        src.utils.get_operations_count(invalid_operation_list)


@pytest.mark.parametrize(
    "invalid_categories",
    [
        (1,),
        ([1, []]),
    ],
)
def test_get_operations_count_invalid_categories(operations_to_filter: list, invalid_categories: typing.Any) -> None:
    with pytest.raises(TypeError):
        src.utils.get_operations_count(operations_to_filter, invalid_categories)  # type: ignore
