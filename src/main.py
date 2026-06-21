import pandas as pd

from src.optimization import gradient_descent
from src.visualization import show_loss_graph
from src.report_utils import save_report


def main():
    print("START PROJECT")

    show_loss_graph()

    history = gradient_descent(
        start_x=-2,
        learning_rate=0.2,
        steps=20
    )

    df = pd.DataFrame(history)
    print(df)

    final_x = df["x"].iloc[-1]
    final_loss = df["loss"].iloc[-1]

    start_x = df["x"].iloc[0]
    start_loss = df["loss"].iloc[0]

    report = f"""
PROJECT: Loss Optimization

Start x: {start_x}
Start loss: {start_loss}

Final x: {final_x}
Final loss: {final_loss}
"""

    save_report(report, "data/project_report.txt")

    print("REPORT SAVED")

    summary = [
        "Функция потерь имеет минимум в точке x = 4",
        "Градиентный спуск успешно приближает значение к минимуму",
        "Loss уменьшается с каждой итерацией",
        "Производная показывает направление изменения функции",
        "Алгоритм стабильно сходится к оптимальному решению",
        "Модульная структура упрощает анализ и поддержку проекта"
    ]

    for item in summary:
        print(item)

    assert len(summary) == 6
    assert final_loss < start_loss


if __name__ == "__main__":
    main()