"""test_transactions_loading.py with tests for transactions_loading.py module functions"""

import pathlib
from unittest.mock import Mock, patch

import pandas as pd

import src.transactions_loading


def test_load_transactions_data_csv_bad_file() -> None:
    assert src.transactions_loading.load_transactions_data_csv("non_existing_file.csv") == []
    mock_stat_result = Mock(st_size=0)
    with patch("pathlib.Path.stat", return_value=mock_stat_result):
        assert src.transactions_loading.load_transactions_data_csv("../data/transactions.csv") == []


@patch("pandas.read_csv")
def test_load_transactions_data_csv(mock_load: Mock) -> None:
    sample_data = [
        {"id": 1, },
        {"id": 2, },
        {"id": 3, },
    ]
    mock_load.return_value = pd.DataFrame(sample_data)
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "transactions.csv")
    result = src.transactions_loading.load_transactions_data_csv(file_path)
    assert result == sample_data


@patch("pandas.read_csv")
def test_load_transactions_data_csv_error(mock_load: Mock) -> None:
    mock_load.side_effect = pd.errors.DataError
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "transactions.csv")
    result = src.transactions_loading.load_transactions_data_csv(file_path)
    assert result == []


def test_load_transactions_data_xlsx_bad_file() -> None:
    assert src.transactions_loading.load_transactions_data_csv("non_existing_file.xlsx") == []
    mock_stat_result = Mock(st_size=0)
    with patch("pathlib.Path.stat", return_value=mock_stat_result):
        assert src.transactions_loading.load_transactions_data_xlsx("../data/transactions_excel.xlsx") == []


@patch("pandas.read_excel")
def test_load_transactions_data_xlsx(mock_load: Mock) -> None:
    sample_data = [
        {"id": 1, },
        {"id": 2, },
        {"id": 3, },
    ]
    mock_load.return_value = pd.DataFrame(sample_data)
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "transactions_excel.xlsx")
    result = src.transactions_loading.load_transactions_data_xlsx(file_path)
    assert result == sample_data


@patch("pandas.read_excel")
def test_load_transactions_data_xlsx_error(mock_load: Mock) -> None:
    mock_load.side_effect = pd.errors.DataError
    file_path = str(pathlib.Path(__file__).parent.parent / "data" / "transactions_excel.xlsx")
    result = src.transactions_loading.load_transactions_data_xlsx(file_path)
    assert result == []
