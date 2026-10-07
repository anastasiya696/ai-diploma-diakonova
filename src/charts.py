from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_revenue_by_category(
    df: pd.DataFrame,
    output_path: str | Path,
) -> None:
    """Сохраняет график выручки по категориям."""
    output_path = Path(output_path)

    plt.figure(figsize=(10, 6))
    plt.bar(df["category"], df["total_revenue"])
    plt.title("Выручка по категориям")
    plt.xlabel("Категория")
    plt.ylabel("Выручка, ₽")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_revenue_by_manager(
    df: pd.DataFrame,
    output_path: str | Path,
) -> None:
    """Сохраняет график выручки по менеджерам."""
    output_path = Path(output_path)

    plt.figure(figsize=(8, 5))
    plt.bar(df["manager"], df["total_revenue"])
    plt.title("Выручка по менеджерам")
    plt.xlabel("Менеджер")
    plt.ylabel("Выручка, ₽")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_revenue_by_month(
    df: pd.DataFrame,
    output_path: str | Path,
) -> None:
    """Сохраняет график динамики выручки по месяцам."""
    output_path = Path(output_path)

    plt.figure(figsize=(10, 6))
    plt.plot(
        df["month"],
        df["total_revenue"],
        marker="o",
    )
    plt.title("Динамика выручки по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Выручка, ₽")
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()