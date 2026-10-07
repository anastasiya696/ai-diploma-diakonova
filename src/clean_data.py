import pandas as pd


REQUIRED_COLUMNS = [
    "date",
    "manager",
    "city",
    "category",
    "product",
    "quantity",
    "price",
    "discount",
]


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Очищает данные о продажах и добавляет расчётные столбцы.
    """

    df = df.copy()

    # Проверяем наличие обязательных столбцов
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"В данных отсутствуют обязательные столбцы: {missing_columns}"
        )

    # Преобразуем дату
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Удаляем строки, где отсутствуют важные данные
    df = df.dropna(
        subset=["date", "manager", "category", "product"]
    )

    # Заполняем пропуски в числовых столбцах
    df["discount"] = df["discount"].fillna(0)
    df["quantity"] = df["quantity"].fillna(0)
    df["price"] = df["price"].fillna(0)

    # Удаляем дубликаты
    df = df.drop_duplicates()

    # Выручка до скидки
    df["revenue_before_discount"] = (
        df["quantity"] * df["price"]
    )

    # Размер скидки в рублях
    df["discount_amount"] = (
        df["revenue_before_discount"] * df["discount"]
    )

    # Итоговая выручка
    df["revenue"] = (
        df["revenue_before_discount"]
        - df["discount_amount"]
    )

    # Месяц продажи
    df["month"] = (
        df["date"]
        .dt.to_period("M")
        .astype(str)
    )

    return df