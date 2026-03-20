from src.utils import load_transactions_data
from src.transactions_loading import load_transactions_data_csv, load_transactions_data_xlsx
from src.processing import filter_by_state, sort_by_date, filter_by_description
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card

def main():
    print(
        "\nДобро пожаловать в программу работы с банковскими транзакциями.\n")
    user_input = None
    while user_input not in ["1", "2", "3"]:
        user_input = input("Выберите необходимый пункт меню:\n"
              "1. Получить информацию о транзакциях из JSON-файла\n"
              "2. Получить информацию о транзакциях из CSV-файла\n"
              "3. Получить информацию о транзакциях из XLSX-файла\n")

    operations_list = list()
    if user_input == "1":
        print("\nДля обработки выбран JSON-файл.\n")
        operations_list = load_transactions_data("./data/operations.json")
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        operations_list = load_transactions_data_csv("./data/transactions.csv")
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл.")
        operations_list = load_transactions_data_xlsx("./data/transactions_excel.xlsx")

    while True:
        user_input = input("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для статусы: EXECUTED, CANCELED, PENDING\n")
        targeted_status = user_input.upper()
        if targeted_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции \"{user_input}\" недоступен.")
        else:
            filtered_operations = filter_by_state(operations_list, targeted_status)
            print(f"\nОперации отфильтрованы по статусу \"{targeted_status}\"")
            break

    sorted_operations = list()
    while user_input not in ["да", "нет"]:
        user_input = input("\nОтсортировать операции по дате? Да/Нет\n").lower()
    if user_input == "да":
        while user_input not in ["по возрастанию", "по убыванию"]:
            user_input = input("\nОтсортировать по возрастанию или по убыванию?\n").lower()
        if user_input == "по возрастанию":
            sorted_operations = sort_by_date(filtered_operations, descending_sorting=False)
        elif user_input == "по убыванию":
            sorted_operations = sort_by_date(filtered_operations, descending_sorting=True)
    elif user_input == "нет":
        sorted_operations = filtered_operations

    user_input = None
    filtered_sorted_operations = list()
    while user_input not in ["да", "нет"]:
        user_input = input("\nВыводить только рублевые транзакции? Да/Нет\n").lower()
    if user_input == "да":
        filtered_sorted_operations = list(filter_by_currency(sorted_operations, "RUB"))
    elif user_input == "нет":
        filtered_sorted_operations = sorted_operations

    user_input = None
    result_list = list()
    while user_input not in ["да", "нет"]:
        user_input = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if user_input == "да":
        description  = input("\nВведите слово для поиска:\n")
        result_list = filter_by_description(filtered_sorted_operations, description)
    elif user_input == "нет":
        result_list = filtered_sorted_operations

    if len(result_list) > 0:
        print("Распечатываем итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(result_list)}\n")

        for operation in result_list:
            print(f"{get_date(operation.get("date"))} {operation.get("description")}")
            print(f"{f"{mask_account_card(operation.get("from"))} -> " if operation.get("from") else ""}{mask_account_card(operation.get("to"))}")
            operation_amount = operation.get("operationAmount", {}).get("amount", 0)
            currency_code = operation.get("operationAmount", {}).get("currency", {}).get("code", "NOT_SPECIFIED")
            print(f"Сумма: {f"{operation_amount} руб." if currency_code == "RUB" else f"{operation_amount} {currency_code}"}\n")
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
