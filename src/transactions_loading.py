"""module with functions for loading transactions data from CSV and XLSX files"""

import logging
import pandas as pd
import pathlib


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = str(pathlib.Path(__file__).parent.parent / "logs" / "transactions_loading.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions_data_csv(file_path_str: str) -> list[dict]:
    """
    function for loading transactions data from CSV file
    :param file_path_str: string with path to CSV file
    :return: transactions data loaded from CSV file, if file not found or empty return empty list
    """
    logger.debug(f"Function load_transactions_data_csv called with file_path_str: {file_path_str}")
    file_path = pathlib.Path(file_path_str)
    if not file_path.is_file() or file_path.stat().st_size == 0:
        logger.info("Specified file was not found or is empty. Returning empty list")
        return []
    try:
        logger.debug(f"Reading file: {file_path_str}")
        transactions_data = pd.read_csv(file_path, delimiter=";")
        logger.info(f"Data read from {file_path_str} is successful. Returning transaction list")
        return transactions_data.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Function load_transactions_data failed due to exception: {e}. Returning empty list")
        return []


def load_transactions_data_xlsx(file_path_str: str) -> list[dict]:
    """
    function for loading transactions data from XLSX file
    :param file_path_str: string with path to XLSX file
    :return: transactions data loaded from XLSX file, if file not found or empty return empty list
    """
    logger.debug(f"Function load_transactions_data_xlsx called with file_path_str: {file_path_str}")
    file_path = pathlib.Path(file_path_str)
    if not file_path.is_file() or file_path.stat().st_size == 0:
        logger.info("Specified file was not found or is empty. Returning empty list")
        return []
    try:
        logger.debug(f"Reading file: {file_path_str}")
        transactions_data = pd.read_excel(file_path)
        logger.info(f"Data read from {file_path_str} is successful. Returning transaction list")
        return transactions_data.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Function load_transactions_data failed due to exception: {e}. Returning empty list")
        return []
