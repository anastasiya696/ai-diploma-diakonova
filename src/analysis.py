import pandas as pd


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Продажи по категориям."""
    return (
        df.groupby("category")
        .agg(
            total_revenue=("revenue", "sum"),
            total_quantity=("quantity", "sum"),
            orders=("product", "count"),
        )
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )


def sales_by_manager(df: pd.DataFrame) -> pd.DataFrame:
    """Продажи по менеджерам."""
    return (
        df.groupby("manager")
        .agg(
            total_revenue=("revenue", "sum"),
            total_quantity=("quantity", "sum"),
            orders=("product", "count"),
        )
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )


def sales_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Продажи по месяцам."""
    return (
        df.groupby("month")
        .agg(
            total_revenue=("revenue", "sum"),
            total_quantity=("quantity", "sum"),
            orders=("product", "count"),
        )
        .reset_index()
        .sort_values("month")
    )


def pivot_city_category(df: pd.DataFrame) -> pd.DataFrame:
    """Сводная таблица: город × категория."""
    return pd.pivot_table(
        df,
        values="revenue",
        index="city",
        columns="category",
        aggfunc="sum",
        fill_value=0,
    )