from pathlib import Path

from src.load_data import load_excel_data
from src.clean_data import clean_sales_data
from src.analysis import (
    sales_by_category,
    sales_by_manager,
    sales_by_month,
    pivot_city_category,
)
from src.charts import (
    save_revenue_by_category,
    save_revenue_by_manager,
    save_revenue_by_month,
)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"


def save_report(df, filename):
    """Сохраняет DataFrame в CSV-файл."""
    path = REPORTS_DIR / filename
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path


def create_final_report(
    category_df,
    manager_df,
    month_df,
    pivot_df,
):
    """Создаёт итоговый Markdown-отчёт."""
    total_revenue = category_df["total_revenue"].sum()
    total_quantity = category_df["total_quantity"].sum()
    total_orders = category_df["orders"].sum()

    best_category = category_df.iloc[0]
    best_manager = manager_df.iloc[0]
    best_month = month_df.loc[
        month_df["total_revenue"].idxmax()
    ]

    report = f"""# Итоговый отчёт по продажам

## Общая информация

- Общая выручка: **{total_revenue:,.0f} ₽**
- Продано товаров: **{total_quantity:,.0f}**
- Количество заказов: **{total_orders}**

## Основные результаты

### Лучшая категория

**{best_category["category"]}** — {best_category["total_revenue"]:,.0f} ₽.

### Лучший менеджер

**{best_manager["manager"]}** — {best_manager["total_revenue"]:,.0f} ₽.

### Лучший месяц

**{best_month["month"]}** — {best_month["total_revenue"]:,.0f} ₽.

## Вывод

Наибольшую выручку принесла категория
**{best_category["category"]}**.

Лучший результат среди менеджеров показала
**{best_manager["manager"]}**.

Самый высокий показатель выручки за месяц был в
**{best_month["month"]}**.

## Использованные инструменты

- Excel — исходные данные;
- Python;
- pandas — очистка и анализ данных;
- matplotlib — визуализация;
- CSV — сохранение результатов анализа;
- Markdown — итоговый отчёт.
"""

    report_path = REPORTS_DIR / "final_report.md"
    report_path.write_text(report, encoding="utf-8")

    return report_path


def main():
    """Основная функция проекта."""

    REPORTS_DIR.mkdir(exist_ok=True)

    print("Загрузка данных из Excel...")
    df = load_excel_data(DATA_DIR / "sales_data.xlsx")

    print("Очистка данных...")
    cleaned_df = clean_sales_data(df)

    print("Выполнение анализа...")

    category_df = sales_by_category(cleaned_df)
    manager_df = sales_by_manager(cleaned_df)
    month_df = sales_by_month(cleaned_df)
    pivot_df = pivot_city_category(cleaned_df)

    print("Сохранение CSV-отчётов...")

    cleaned_df.to_csv(
        REPORTS_DIR / "cleaned_sales_data.csv",
        index=False,
        encoding="utf-8-sig",
    )

    save_report(category_df, "sales_by_category.csv")
    save_report(manager_df, "sales_by_manager.csv")
    save_report(month_df, "sales_by_month.csv")
    pivot_df.to_csv(
        REPORTS_DIR / "pivot_city_category.csv",
        encoding="utf-8-sig",
    )

    print("Создание графиков...")

    save_revenue_by_category(
        category_df,
        REPORTS_DIR / "revenue_by_category.png",
    )

    save_revenue_by_manager(
        manager_df,
        REPORTS_DIR / "revenue_by_manager.png",
    )

    save_revenue_by_month(
        month_df,
        REPORTS_DIR / "revenue_by_month.png",
    )

    print("Создание итогового отчёта...")

    report_path = create_final_report(
        category_df,
        manager_df,
        month_df,
        pivot_df,
    )

    print("\nПроект успешно выполнен!")
    print(f"Обработано строк: {len(cleaned_df)}")
    print(f"Итоговый отчёт: {report_path}")


if __name__ == "__main__":
    main()