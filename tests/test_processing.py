"""test_processing.py with tests for processing.py module functions"""
import pytest

from src import processing


def test_filter_by_state(bank_operation_list):
    assert processing.filter_by_state(bank_operation_list)== [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.mark.parametrize("targeted_state, expected", [
    ("EXECUTED", [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ("CANCELED", [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])
])
def test_filter_by_state(bank_operation_list, targeted_state, expected):
    assert processing.filter_by_state(bank_operation_list, targeted_state)== expected


def test_sort_by_date_default_desc(bank_operation_list):
    assert processing.sort_by_date(bank_operation_list) == [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_sort_by_date_asc(bank_operation_list):
    assert processing.sort_by_date(bank_operation_list, descending_sorting=False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


def test_sort_by_date_type_error(bank_operation_list):
    with pytest.raises(TypeError):
        processing.sort_by_date(bank_operation_list, False)
