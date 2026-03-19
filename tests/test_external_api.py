"""test_external_api.py with tests for external_api.py module functions"""

import json
from unittest.mock import Mock, patch

import pytest
import requests

import src.external_api


@patch("requests.get")
def test_convert_to_rub(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.5}
    assert src.external_api.convert_to_rub("USD", 1) == 75.5


@patch("requests.get")
def test_convert_to_rub_request_error(mock_get: Mock) -> None:
    mock_get.side_effect = requests.exceptions.ConnectionError("Mocked connection error")
    with pytest.raises(requests.exceptions.RequestException):
        src.external_api.convert_to_rub("USD", 1)


@patch("requests.get")
def test_convert_to_rub_no_result_key(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"res": 75.5}
    with pytest.raises(KeyError):
        src.external_api.convert_to_rub("USD", 1)


@patch("requests.get")
def test_convert_to_rub_invalid_response_json(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.side_effect = json.JSONDecodeError("Invalid JSON", "usd 1", 0)
    with pytest.raises(json.JSONDecodeError):
        src.external_api.convert_to_rub("USD", 1)


def test_convert_to_rub_negative() -> None:
    mock_response = Mock()
    mock_response.status_code = 400
    with patch("requests.get", return_value=mock_response):
        with pytest.raises(Exception, match="Conversion failed"):
            src.external_api.convert_to_rub("USD", -1)
