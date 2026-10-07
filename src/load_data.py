from pathlib import Path

import pandas as pd


def load_excel_data(path: str | Path) -> pd.DataFrame:
    """
    Загружает данные из Excel-файла.

    path — путь к файлу .xlsx.
    Возвращает pandas DataFrame.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    df = pd.read_excel(path)

    return df


def load_csv_data(path: str | Path) -> pd.DataFrame:
    """
    Загружает данные из CSV-файла.

    path — путь к файлу .csv.
    Возвращает pandas DataFrame.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    df = pd.read_csv(path)

    return df