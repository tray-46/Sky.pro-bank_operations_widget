"""test_decorators.py with tests for decorators.py module functions"""
import pytest
from src import decorators

@decorators.log()
def divide_function_console(x: int | float, y: int | float) -> float:
    """function for decorator testing"""
    return x / y


@decorators.log("log.txt")
def divide_function_file(x: int | float, y: int | float) -> float:
    """function for decorator testing"""
    return x / y


def test_log_decorator_base(capsys):
    assert divide_function_console(1, 2) == 0.5
    captured = capsys.readouterr()
    assert captured.out == "divide_function_console ok\n"


def test_log_decorator_exception():
    with pytest.raises(Exception):
        divide_function_console(1, 0)


def test_log_decorator_error_msg(capsys):
    try:
        divide_function_console(1, 0)
    except ZeroDivisionError:
        captured = capsys.readouterr()
        assert captured.out == "divide_function_console error: division by zero. Inputs: (1, 0), {}\n"


def test_log_decorator_base_file():
    assert divide_function_file(1, 2) == 0.5


def test_log_decorator_error_file():
    with pytest.raises(Exception):
        divide_function_file(1, 0)
