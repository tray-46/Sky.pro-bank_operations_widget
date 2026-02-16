"""test_processing.py with tests for processing.py module functions"""

import pytest

from src import processing


# filter_by_state tests
def test_filter_by_state_base(bank_operation_list: list[dict]) -> None:
    assert processing.filter_by_state(bank_operation_list) == [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "targeted_state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PROCESSING", []),
    ],
)
def test_filter_by_state(bank_operation_list: list[dict], targeted_state: str, expected: list[dict]) -> None:
    assert processing.filter_by_state(bank_operation_list, targeted_state) == expected


def test_filter_by_state_no_args() -> None:
    with pytest.raises(TypeError):
        processing.filter_by_state()


def test_filter_by_state_invalid_list_dict(invalid_bank_operation_list: list) -> None:
    with pytest.raises(TypeError):
        processing.filter_by_state(invalid_bank_operation_list)


def test_sort_by_date_default_desc(bank_operation_list: list[dict]) -> None:
    assert processing.sort_by_date(bank_operation_list) == [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064592, "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {
            "id": 615064593,
        },
    ]


def test_sort_by_date_asc(bank_operation_list: list[dict]) -> None:
    assert processing.sort_by_date(bank_operation_list, descending_sorting=False) == [
        {
            "id": 615064593,
        },
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064592, "date": "2018-10-14T08:21:33.419441"},
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_no_args() -> None:
    with pytest.raises(TypeError):
        processing.sort_by_date()


def test_sort_by_date_invalid_list_dict(invalid_bank_operation_list: list) -> None:
    with pytest.raises(TypeError):
        processing.sort_by_date(invalid_bank_operation_list)


def test_sort_by_date_type_error(bank_operation_list: list[dict]) -> None:
    with pytest.raises(TypeError):
        processing.sort_by_date(bank_operation_list, False)


def test_sort_by_date_date_type_error() -> None:
    with pytest.raises(TypeError):
        processing.sort_by_date([{"id": 615064591, "state": "CANCELED", "date": 123}])


@pytest.mark.parametrize(
    "invalid_date_strings",
    [
        [
            {"id": 414288290, "state": "EXECUTED", "date": "2019-15-12T18:35:29.512364"},
        ],
        [
            {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018T02:08:58.425572"},
        ],
        [
            {"id": 594226727, "state": "CANCELED", "date": "18-09-12T21:27:25.241689"},
        ],
        [
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        ],
    ],
)
def test_sort_by_date_invalid_date_strings(invalid_date_strings: list) -> None:
    with pytest.raises(ValueError):
        processing.sort_by_date(invalid_date_strings)
