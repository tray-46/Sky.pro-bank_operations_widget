"""test_external_api.py with tests for external_api.py module functions"""

from unittest.mock import Mock, patch

import pytest

import src.external_api


@patch('requests.get')
def test_convert_to_rub(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.5}
    assert src.external_api.convert_to_rub("USD", 1) == 75.5


def test_convert_to_rub_negative():
    mock_response = Mock()
    mock_response.status_code = 400
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(Exception, match="Conversion failed"):
            src.external_api.convert_to_rub("USD", -1)
