"""test_main.py with tests for main.py module functions"""

from unittest.mock import Mock, patch

from pytest import CaptureFixture, MonkeyPatch

import main


@patch("main.load_transactions_data")
def test_main_json(
    mock_load_transactions_data: Mock,
    operations_list: list[dict],
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_transactions_data.return_value = operations_list
    inputs = iter(["1", "PENDING", "нет", "нет", "нет"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "\nДобро пожаловать в программу работы с банковскими транзакциями.\n\n"
        '\nДля обработки выбран JSON-файл.\n\n\nОперации отфильтрованы по статусу "PENDING"'
        "\nРаспечатываем итоговый список транзакций...\n\nВсего банковских операций в выборке: 1\n"
        "\n19.03.2026 Перевод со счета на счет\nСчет **6952 -> Счет **6702\nСумма: 9824.07 USD\n"
        "\n"
    )


@patch("main.load_transactions_data_csv")
def test_main_csv(
    mock_load_transactions_data_csv: Mock,
    operations_list: list[dict],
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_transactions_data_csv.return_value = operations_list
    inputs = iter(["q", "2", "q", "EXECUTED", "да", "q", "по возрастанию", "q", "да", "q", "да", "SOME NONSENSE"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "\nДобро пожаловать в программу работы с банковскими транзакциями.\n"
        '\nДля обработки выбран CSV-файл.\nСтатус операции "q" недоступен.\n'
        '\nОперации отфильтрованы по статусу "EXECUTED"\n'
        "\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.\n"
    )


@patch("main.load_transactions_data_xlsx")
def test_main_xlsx(
    mock_load_transactions_data_xlsx: Mock,
    operations_list: list[dict],
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_transactions_data_xlsx.return_value = operations_list
    inputs = iter(["q", "3", "q", "EXECUTED", "да", "q", "по убыванию", "q", "да", "q", "да", "SOME NONSENSE"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == (
        "\nДобро пожаловать в программу работы с банковскими транзакциями.\n"
        '\nДля обработки выбран XLSX-файл.\nСтатус операции "q" недоступен.\n'
        '\nОперации отфильтрованы по статусу "EXECUTED"\n'
        "\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.\n"
    )
