"""
Сквозной проект блока 4.

Используются темы занятий 1-11:
- математическая статистика;
- теория вероятностей;
- bootstrap;
- корреляция;
- линейная регрессия;
- A/B-тестирование;
- линейная алгебра.

Проект работает с данными студентов и рассчитывает
показатели успеваемости и риск низкого результата.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from src.block04_stats import mean, median, std_sample
from src.block04_probability import prob_event, prob_conditional
from src.block04_bootstrap import bootstrap_ci_mean
from src.block04_correlation import corr_pearson
from src.block04_regression import (
    fit_linear_regression_1d,
    predict_linear_1d,
    mse,
)
from src.block04_hypothesis import (
    permutation_test_diff_means,
    p_value_two_sided,
)
from src.block04_linear_algebra import (
    cosine_similarity,
    matvec,
)


# ============================================================
# Пути проекта
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

DATA_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)


# ============================================================
# Поиск исходного файла
# ============================================================

data_path = DATA_DIR / "student_engagement.csv"


def load_data() -> pd.DataFrame:
    """
    Загрузка данных студентов.

    Если файла student_engagement.csv нет,
    создаём небольшой демонстрационный датасет.
    """

    if data_path.exists():
        return pd.read_csv(data_path)

    rng = np.random.default_rng(42)

    n = 100

    df = pd.DataFrame(
        {
            "student_id": np.arange(1, n + 1),
            "practice_hours": rng.uniform(1, 15, n),
            "attendance": rng.uniform(50, 100, n),
            "assignments_completed": rng.integers(3, 11, n),
        }
    )

    noise = rng.normal(0, 5, n)

    df["final_score"] = (
        35
        + 2.5 * df["practice_hours"]
        + 0.25 * df["attendance"]
        + 1.5 * df["assignments_completed"]
        + noise
    )

    df["final_score"] = df["final_score"].clip(0, 100)

    df["passed"] = df["final_score"] >= 60

    df["high_attendance"] = df["attendance"] >= 80

    df["risk_score"] = (
        (100 - df["attendance"]) * 0.4
        + (10 - df["assignments_completed"]) * 4
        + (60 - df["final_score"]).clip(lower=0) * 0.6
    )

    df.to_csv(data_path, index=False)

    return df


# ============================================================
# 1. Математическая статистика
# ============================================================

def calculate_statistics(df: pd.DataFrame) -> dict:
    scores = df["final_score"].to_numpy(dtype=float)

    score_mean = mean(scores)
    score_median = median(scores)
    score_std = std_sample(scores)

    ci_low, ci_high = bootstrap_ci_mean(
        scores,
        n_boot=2000,
        alpha=0.05,
        seed=42,
    )

    return {
        "score_mean": score_mean,
        "score_median": score_median,
        "score_std": score_std,
        "ci_low": ci_low,
        "ci_high": ci_high,
    }


# ============================================================
# 2. Теория вероятностей
# ============================================================

def calculate_probability(df: pd.DataFrame) -> dict:
    records = df.to_dict("records")

    p_pass = prob_event(
        records,
        lambda row: bool(row["passed"]),
    )

    p_pass_high_att = prob_conditional(
        records,
        condition_func=lambda row: bool(row["high_attendance"]),
        event_func=lambda row: bool(row["passed"]),
    )

    low_attendance = prob_conditional(
        records,
        condition_func=lambda row: not bool(row["high_attendance"]),
        event_func=lambda row: bool(row["passed"]),
    )

    return {
        "p_pass": p_pass,
        "p_pass_high_att": p_pass_high_att,
        "p_pass_low_att": low_attendance,
    }


# ============================================================
# 3. A/B-сравнение
# ============================================================

def calculate_ab_test(df: pd.DataFrame) -> dict:
    """
    Простое A/B-сравнение.

    Группа A — студенты с practice_hours ниже медианы.
    Группа B — студенты с practice_hours выше или равным медиане.
    """

    median_practice = df["practice_hours"].median()

    scores_a = df.loc[
        df["practice_hours"] < median_practice,
        "final_score",
    ].to_numpy(dtype=float)

    scores_b = df.loc[
        df["practice_hours"] >= median_practice,
        "final_score",
    ].to_numpy(dtype=float)

    mean_a = mean(scores_a)
    mean_b = mean(scores_b)

    diff_obs = mean_b - mean_a

    diffs_perm = permutation_test_diff_means(
        scores_a,
        scores_b,
        n_perm=2000,
        seed=42,
    )

    p_value = p_value_two_sided(
        diff_obs,
        diffs_perm,
    )

    return {
        "scores_a": scores_a,
        "scores_b": scores_b,
        "mean_a": mean_a,
        "mean_b": mean_b,
        "diff_obs": diff_obs,
        "p_value": p_value,
    }


# ============================================================
# 4. Корреляция и регрессия
# ============================================================

def calculate_regression(df: pd.DataFrame) -> dict:
    x = df["practice_hours"].to_numpy(dtype=float)
    y = df["final_score"].to_numpy(dtype=float)

    corr = corr_pearson(x, y)

    a, b = fit_linear_regression_1d(x, y)

    y_hat = predict_linear_1d(
        x,
        a,
        b,
    )

    error = mse(y, y_hat)

    return {
        "corr": corr,
        "a": a,
        "b": b,
        "mse": error,
    }


# ============================================================
# 5. Линейная алгебра
# ============================================================

def calculate_linear_algebra(df: pd.DataFrame) -> dict:
    """
    Представляем студентов как векторы признаков:

    [practice_hours, attendance, assignments_completed]
    """

    features = df[
        [
            "practice_hours",
            "attendance",
            "assignments_completed",
        ]
    ].to_numpy(dtype=float)

    # Нормируем признаки, чтобы разные масштабы
    # не искажали cosine similarity.
    features_normalized = (
        features - features.mean(axis=0)
    ) / features.std(axis=0)

    target_idx = 0

    target_vector = features_normalized[target_idx]

    similarities = []

    for i, vector in enumerate(features_normalized):
        if i == target_idx:
            similarities.append(-1.0)
        else:
            similarities.append(
                cosine_similarity(
                    target_vector,
                    vector,
                )
            )

    best_idx = int(np.argmax(similarities))

    # Небольшая демонстрация матричного умножения.
    weights = np.array(
        [0.3, 0.4, 0.3],
        dtype=float,
    )

    risk_matrix = np.column_stack(
        [
            100 - df["attendance"].to_numpy(dtype=float),
            10 - df["assignments_completed"].to_numpy(dtype=float),
            np.maximum(
                60 - df["final_score"].to_numpy(dtype=float),
                0,
            ),
        ]
    )

    risk_scores = matvec(
        risk_matrix,
        weights,
    )

    return {
        "target_idx": target_idx,
        "best_idx": best_idx,
        "similarities": similarities,
        "risk_scores": risk_scores,
        "risk_matrix": risk_matrix,
        "weights": weights,
    }


# ============================================================
# 6. Сохранение результатов
# ============================================================

def save_results(
    df: pd.DataFrame,
    statistics: dict,
    probability: dict,
    ab_test: dict,
    regression: dict,
    linear_algebra: dict,
) -> None:

    # --------------------------------------------------------
    # Добавляем risk_score
    # --------------------------------------------------------

    df = df.copy()

    df["risk_score"] = linear_algebra["risk_scores"]

    df["risk_level"] = pd.cut(
        df["risk_score"],
        bins=[
            -np.inf,
            10,
            20,
            np.inf,
        ],
        labels=[
            "low",
            "medium",
            "high",
        ],
    )

    # --------------------------------------------------------
    # Основной файл
    # --------------------------------------------------------

    final_data_path = (
        DATA_DIR
        / "student_engagement_block04_with_risk.csv"
    )

    df.to_csv(
        final_data_path,
        index=False,
    )

    # --------------------------------------------------------
    # Таблица вероятностей
    # --------------------------------------------------------

    prob_table = pd.DataFrame(
        {
            "metric": [
                "P(pass)",
                "P(pass | high attendance)",
                "P(pass | low attendance)",
            ],
            "value": [
                probability["p_pass"],
                probability["p_pass_high_att"],
                probability["p_pass_low_att"],
            ],
        }
    )

    prob_table_path = (
        REPORTS_DIR
        / "probability_table.csv"
    )

    prob_table.to_csv(
        prob_table_path,
        index=False,
    )

    # --------------------------------------------------------
    # TOP-10 студентов по риску
    # --------------------------------------------------------

    risk_top10 = df.sort_values(
        "risk_score",
        ascending=False,
    ).head(10)

    risk_top10_path = (
        REPORTS_DIR
        / "risk_top10.csv"
    )

    risk_top10.to_csv(
        risk_top10_path,
        index=False,
    )

    # --------------------------------------------------------
    # Текстовый отчёт
    # --------------------------------------------------------

    target_idx = linear_algebra["target_idx"]
    best_idx = linear_algebra["best_idx"]

    report_text = f"""
# Сквозной проект блока 4

## 1. Данные

Количество студентов: {len(df)}.
Файл данных: {data_path}.

## 2. Математическая статистика

Средний итоговый балл: {statistics["score_mean"]:.2f}.
Медианный итоговый балл: {statistics["score_median"]:.2f}.
Стандартное отклонение: {statistics["score_std"]:.2f}.

95% bootstrap CI среднего итогового балла:
[{statistics["ci_low"]:.2f}; {statistics["ci_high"]:.2f}].

## 3. Теория вероятностей

P(pass): {probability["p_pass"]:.3f}.
P(pass | high attendance): {probability["p_pass_high_att"]:.3f}.
P(pass | low attendance): {probability["p_pass_low_att"]:.3f}.

## 4. A/B сравнение

mean(A): {ab_test["mean_a"]:.2f}.
mean(B): {ab_test["mean_b"]:.2f}.
diff B - A: {ab_test["diff_obs"]:.2f}.
p-value: {ab_test["p_value"]:.4f}.

## 5. Корреляция и регрессия

Корреляция practice_hours и final_score:
{regression["corr"]:.3f}.

Линейная модель:

final_score = {regression["a"]:.3f} * practice_hours + {regression["b"]:.3f}.

MSE: {regression["mse"]:.3f}.

## 6. Линейная алгебра

Матрица признаков содержит:
{len(df)} студентов и 3 признака.

Целевой студент:
{df.loc[target_idx, "student_id"]}.

Самый похожий студент:
{df.loc[best_idx, "student_id"]}.

Cosine similarity:
{linear_algebra["similarities"][best_idx]:.3f}.

Risk score рассчитан через
risk_matrix @ weights.

## 7. Вывод

Проект показывает, как темы блока 4 работают вместе.

Теория вероятностей используется для оценки вероятности успешной сдачи.

Математическая статистика используется для описания итоговых баллов
и оценки неопределённости среднего значения.

A/B-сравнение позволяет сравнить результаты двух групп студентов.

Корреляция и линейная регрессия позволяют исследовать связь
между временем практики и итоговым баллом.

Линейная алгебра позволяет представить студентов как векторы признаков,
сравнить их через cosine similarity и рассчитать риск через
матричное умножение.

## 8. Файлы результата

Основные данные:
{final_data_path}

Таблица вероятностей:
{prob_table_path}

TOP-10 студентов по риску:
{risk_top10_path}

Отчёт:
{REPORTS_DIR / "block04_cross_project_report.md"}
"""

    report_path = (
        REPORTS_DIR
        / "block04_cross_project_report.md"
    )

    report_path.write_text(
        report_text,
        encoding="utf-8",
    )

    print(report_text)

    print("\nФайлы сохранены:")
    print("-", final_data_path)
    print("-", prob_table_path)
    print("-", risk_top10_path)
    print("-", report_path)


# ============================================================
# Главная функция
# ============================================================

def main() -> None:

    print("=" * 60)
    print("СКВОЗНОЙ ПРОЕКТ БЛОКА 4")
    print("=" * 60)

    print("\n1. Загрузка данных...")

    df = load_data()

    print(
        f"Загружено студентов: {len(df)}"
    )

    print("\n2. Математическая статистика...")

    statistics = calculate_statistics(df)

    print(
        f"Средний балл: "
        f"{statistics['score_mean']:.2f}"
    )

    print(
        f"Медианный балл: "
        f"{statistics['score_median']:.2f}"
    )

    print("\n3. Теория вероятностей...")

    probability = calculate_probability(df)

    print(
        f"P(pass) = "
        f"{probability['p_pass']:.3f}"
    )

    print("\n4. A/B-сравнение...")

    ab_test = calculate_ab_test(df)

    print(
        f"mean(A) = "
        f"{ab_test['mean_a']:.2f}"
    )

    print(
        f"mean(B) = "
        f"{ab_test['mean_b']:.2f}"
    )

    print(
        f"p-value = "
        f"{ab_test['p_value']:.4f}"
    )

    print("\n5. Корреляция и регрессия...")

    regression = calculate_regression(df)

    print(
        f"Correlation = "
        f"{regression['corr']:.3f}"
    )

    print(
        f"MSE = "
        f"{regression['mse']:.3f}"
    )

    print("\n6. Линейная алгебра...")

    linear_algebra = calculate_linear_algebra(df)

    best_idx = linear_algebra["best_idx"]

    print(
        "Самый похожий студент:",
        df.loc[best_idx, "student_id"],
    )

    print(
        "Cosine similarity:",
        f"{linear_algebra['similarities'][best_idx]:.3f}",
    )

    print("\n7. Сохранение результатов...")

    save_results(
        df,
        statistics,
        probability,
        ab_test,
        regression,
        linear_algebra,
    )

    print("\n" + "=" * 60)
    print("Сквозной проект блока 4 выполнен успешно.")
    print("=" * 60)


if __name__ == "__main__":
    main()