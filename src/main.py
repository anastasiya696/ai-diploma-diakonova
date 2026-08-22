"""
Сквозной проект блока 4.

Проект по анализу поведения покупателей.

Используются темы занятий 1-11:
- математическая статистика;
- теория вероятностей;
- формула Байеса;
- bootstrap;
- корреляция;
- линейная регрессия;
- A/B-тестирование;
- линейная алгебра;
- визуализация.

Данные генерируются внутри проекта.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from src.block04_stats import (
    describe,
    trimmed_mean,
)

from src.block04_probability import (
    prob_event,
    prob_conditional,
    contingency_2x2,
)

from src.block04_bayes import (
    build_binary_counts,
    prob_from_counts,
    bayes_posterior,
    score_buy_probability,
    laplace_smooth_prob,
)

from src.block04_bootstrap import (
    bootstrap_ci_mean,
)

from src.block04_correlation import (
    corr_pearson,
)

from src.block04_regression import (
    fit_linear_regression_1d,
    predict_linear_1d,
    mse,
)

from src.block04_hypothesis import (
    permutation_test_diff_means,
    p_value_two_sided,
    decision,
    cohens_d,
)

from src.block04_linear_algebra import (
    cosine_similarity,
    matvec,
)

from src.block04_visualization import (
    save_histogram,
    save_scatter,
    save_regression_plot,
    save_bar_chart,
    save_vectors_2d,
)


# ============================================================
# Пути проекта
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

DATA_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

DATA_PATH = DATA_DIR / "customer_behavior.csv"


# ============================================================
# Генерация данных покупателей
# ============================================================

def generate_data(
    n: int = 500,
    seed: int = 42,
) -> pd.DataFrame:
    """Создать демонстрационный датасет покупателей."""

    if n <= 0:
        raise ValueError("n must be positive")

    rng = np.random.default_rng(seed)

    df = pd.DataFrame(
        {
            "customer_id": np.arange(1, n + 1),

            "product_views": rng.integers(
                1,
                30,
                n,
            ),

            "clicks": rng.integers(
                0,
                10,
                n,
            ),

            "cart_additions": rng.integers(
                0,
                5,
                n,
            ),

            "discount": rng.choice(
                [0, 5, 10, 15, 20],
                size=n,
            ),

            "review_views": rng.integers(
                0,
                10,
                n,
            ),

            "group": rng.choice(
                ["A", "B"],
                size=n,
            ),
        }
    )

    # --------------------------------------------------------
    # Вероятность покупки
    # --------------------------------------------------------

    purchase_score = (
        0.02
        + df["clicks"] * 0.025
        + df["cart_additions"] * 0.08
        + df["review_views"] * 0.01
        + df["discount"] * 0.005
    )

    purchase_score = purchase_score.clip(
        0,
        0.95,
    )

    df["purchase"] = (
        rng.random(n) < purchase_score
    )

    # --------------------------------------------------------
    # Сумма покупки
    # --------------------------------------------------------

    base_amount = (
        500
        + df["product_views"] * 80
        + df["clicks"] * 150
        + df["cart_additions"] * 500
        + df["discount"] * 20
    )

    noise = rng.normal(
        0,
        500,
        n,
    )

    df["purchase_amount"] = np.where(
        df["purchase"],
        np.maximum(
            base_amount + noise,
            100,
        ),
        0,
    )

    df["purchase"] = df["purchase"].astype(bool)

    df.to_csv(
        DATA_PATH,
        index=False,
    )

    return df


# ============================================================
# 1. Математическая статистика
# ============================================================

def calculate_statistics(
    df: pd.DataFrame,
) -> dict:
    """Рассчитать статистики суммы покупок."""

    amounts = df.loc[
        df["purchase"],
        "purchase_amount",
    ].to_numpy(dtype=float)

    if len(amounts) < 2:
        raise ValueError(
            "Недостаточно покупок для статистики"
        )

    stats = describe(amounts)

    trimmed = trimmed_mean(
        amounts,
        proportion_to_cut=0.1,
    )

    ci_low, ci_high = bootstrap_ci_mean(
        amounts,
        n_boot=2000,
        alpha=0.05,
        seed=42,
    )

    return {
        "n_purchases": len(amounts),
        "mean": stats["mean"],
        "median": stats["median"],
        "std": stats["std_sample"],
        "min": stats["min"],
        "max": stats["max"],
        "trimmed_mean": trimmed,
        "ci_low": ci_low,
        "ci_high": ci_high,
    }


# ============================================================
# 2. Теория вероятностей
# ============================================================

def calculate_probability(
    df: pd.DataFrame,
) -> dict:
    """Рассчитать вероятности событий."""

    records = df.to_dict("records")

    p_purchase = prob_event(
        records,
        lambda row: bool(row["purchase"]),
    )

    p_purchase_click = prob_conditional(
        records,
        condition_func=lambda row: bool(
            row["clicks"] > 0
        ),
        event_func=lambda row: bool(
            row["purchase"]
        ),
    )

    p_purchase_no_click = prob_conditional(
        records,
        condition_func=lambda row: not bool(
            row["clicks"] > 0
        ),
        event_func=lambda row: bool(
            row["purchase"]
        ),
    )

    table = contingency_2x2(
        records,
        "purchase",
        "group",
    )

    return {
        "p_purchase": p_purchase,
        "p_purchase_click": p_purchase_click,
        "p_purchase_no_click": p_purchase_no_click,
        "contingency": table,
    }


# ============================================================
# 3. Формула Байеса
# ============================================================

def calculate_bayes(
    df: pd.DataFrame,
) -> dict:
    """Расчёт вероятности покупки по Байесу."""

    records = df.to_dict("records")

    for row in records:
        row["clicked"] = bool(row["clicks"] > 0)

    counts = build_binary_counts(
        records,
        "purchase",
        "clicked",
    )

    p_purchase = prob_from_counts(
        counts["count_a"],
        counts["n"],
    )

    p_clicked = prob_from_counts(
        counts["count_b"],
        counts["n"],
    )

    p_purchase_given_clicked = prob_from_counts(
        counts["count_ab"],
        counts["count_b"],
    )

    p_clicked_given_purchase = prob_from_counts(
        counts["count_ab"],
        counts["count_a"],
    )

    posterior = bayes_posterior(
        p_clicked_given_purchase,
        p_purchase,
        p_clicked,
    )

    smoothed = laplace_smooth_prob(
        counts["count_ab"],
        counts["count_b"],
    )

    score_clicked = score_buy_probability(
        True,
        p_purchase_given_clicked,
        probability_if_no_click := prob_conditional(
            records,
            condition_func=lambda row: not row["clicked"],
            event_func=lambda row: bool(row["purchase"]),
        ),
    )

    return {
        "p_purchase": p_purchase,
        "p_clicked": p_clicked,
        "p_purchase_given_clicked": p_purchase_given_clicked,
        "bayes_posterior": posterior,
        "laplace_probability": smoothed,
        "score_clicked": score_clicked,
    }


# ============================================================
# 4. Корреляция и линейная регрессия
# ============================================================

def calculate_regression(
    df: pd.DataFrame,
) -> dict:
    """Исследовать связь просмотров и суммы покупки."""

    purchased = df.loc[
        df["purchase"],
    ]

    if len(purchased) < 2:
        raise ValueError(
            "Недостаточно покупок для регрессии"
        )

    x = purchased[
        "product_views"
    ].to_numpy(dtype=float)

    y = purchased[
        "purchase_amount"
    ].to_numpy(dtype=float)

    correlation = corr_pearson(
        x,
        y,
    )

    a, b = fit_linear_regression_1d(
        x,
        y,
    )

    y_hat = predict_linear_1d(
        x,
        a,
        b,
    )

    error = mse(
        y,
        y_hat,
    )

    return {
        "x": x,
        "y": y,
        "y_hat": y_hat,
        "correlation": correlation,
        "a": a,
        "b": b,
        "mse": error,
    }


# ============================================================
# 5. A/B-тестирование
# ============================================================

def calculate_ab_test(
    df: pd.DataFrame,
) -> dict:
    """Сравнить сумму покупок групп A и B."""

    group_a = df.loc[
        (df["group"] == "A")
        & df["purchase"],
        "purchase_amount",
    ].to_numpy(dtype=float)

    group_b = df.loc[
        (df["group"] == "B")
        & df["purchase"],
        "purchase_amount",
    ].to_numpy(dtype=float)

    if len(group_a) < 2 or len(group_b) < 2:
        raise ValueError(
            "Недостаточно данных для A/B-теста"
        )

    mean_a = float(np.mean(group_a))
    mean_b = float(np.mean(group_b))

    diff = mean_b - mean_a

    diffs_perm = permutation_test_diff_means(
        group_a,
        group_b,
        n_perm=2000,
        seed=42,
    )

    p_value = p_value_two_sided(
        diff,
        diffs_perm,
    )

    result = decision(
        p_value,
        alpha=0.05,
    )

    effect = cohens_d(
        group_a,
        group_b,
    )

    return {
        "mean_a": mean_a,
        "mean_b": mean_b,
        "diff": diff,
        "p_value": p_value,
        "decision": result,
        "cohens_d": effect,
        "group_a": group_a,
        "group_b": group_b,
    }


# ============================================================
# 6. Линейная алгебра
# ============================================================

def calculate_linear_algebra(
    df: pd.DataFrame,
) -> dict:
    """Cosine similarity и матричное умножение."""

    features = df[
        [
            "product_views",
            "clicks",
            "cart_additions",
            "discount",
        ]
    ].to_numpy(dtype=float)

    means = features.mean(axis=0)
    stds = features.std(axis=0)

    stds[stds == 0] = 1

    normalized = (
        features - means
    ) / stds

    target_idx = 0

    target = normalized[
        target_idx
    ]

    similarities = []

    for i, vector in enumerate(normalized):
        if i == target_idx:
            similarities.append(-1.0)
        else:
            similarities.append(
                cosine_similarity(
                    target,
                    vector,
                )
            )

    best_idx = int(
        np.argmax(similarities)
    )

    matrix = np.column_stack(
        [
            df["product_views"].to_numpy(
                dtype=float
            ),
            df["clicks"].to_numpy(
                dtype=float
            ),
            df["cart_additions"].to_numpy(
                dtype=float
            ),
        ]
    )

    weights = np.array(
        [0.2, 0.3, 0.5],
        dtype=float,
    )

    scores = matvec(
        matrix,
        weights,
    )

    return {
        "target_idx": target_idx,
        "best_idx": best_idx,
        "similarity": similarities[best_idx],
        "scores": scores,
        "matrix": matrix,
        "weights": weights,
    }


# ============================================================
# 7. Визуализация
# ============================================================

def save_visualizations(
    df: pd.DataFrame,
    regression: dict,
    ab_test: dict,
    linear_algebra: dict,
) -> None:
    """Сохранить графики проекта."""

    save_histogram(
        df.loc[
            df["purchase"],
            "purchase_amount",
        ],
        title="Распределение суммы покупок",
        xlabel="Сумма покупки",
        path=REPORTS_DIR / "purchase_amount_hist.png",
    )

    save_scatter(
        regression["x"],
        regression["y"],
        title="Просмотры и сумма покупки",
        xlabel="Количество просмотров",
        ylabel="Сумма покупки",
        path=REPORTS_DIR / "views_purchase_scatter.png",
    )

    order = np.argsort(
        regression["x"]
    )

    save_regression_plot(
        regression["x"][order],
        regression["y"][order],
        regression["y_hat"][order],
        path=REPORTS_DIR / "regression.png",
    )

    save_bar_chart(
        ["A", "B"],
        [
            ab_test["mean_a"],
            ab_test["mean_b"],
        ],
        title="Средняя сумма покупки: A/B",
        xlabel="Группа",
        ylabel="Средняя сумма покупки",
        path=REPORTS_DIR / "ab_means.png",
    )

    target_idx = linear_algebra["target_idx"]
    best_idx = linear_algebra["best_idx"]

    vectors = {
        "target": linear_algebra["matrix"][target_idx][:2],
        "similar": linear_algebra["matrix"][best_idx][:2],
    }

    save_vectors_2d(
        vectors,
        REPORTS_DIR / "customer_vectors.png",
    )


# ============================================================
# 8. Отчёт
# ============================================================

def save_report(
    df: pd.DataFrame,
    statistics: dict,
    probability: dict,
    bayes: dict,
    regression: dict,
    ab_test: dict,
    linear_algebra: dict,
) -> None:
    """Сохранить итоговый Markdown-отчёт."""

    report_path = (
        REPORTS_DIR
        / "block04_customer_project_report.md"
    )

    text = f"""
# Сквозной проект блока 4 — анализ покупателей

## 1. Данные

Количество покупателей: {len(df)}.

Количество покупок: {statistics["n_purchases"]}.

## 2. Математическая статистика

Средняя сумма покупки:
{statistics["mean"]:.2f}

Медиана:
{statistics["median"]:.2f}

Стандартное отклонение:
{statistics["std"]:.2f}

Усечённое среднее:
{statistics["trimmed_mean"]:.2f}

95% bootstrap CI среднего:
[{statistics["ci_low"]:.2f}; {statistics["ci_high"]:.2f}]

## 3. Теория вероятностей

P(purchase):
{probability["p_purchase"]:.3f}

P(purchase | click):
{probability["p_purchase_click"]:.3f}

P(purchase | no click):
{probability["p_purchase_no_click"]:.3f}

## 4. Формула Байеса

P(purchase | clicked):
{bayes["p_purchase_given_clicked"]:.3f}

Bayes posterior:
{bayes["bayes_posterior"]:.3f}

Laplace-smoothed probability:
{bayes["laplace_probability"]:.3f}

## 5. Корреляция и регрессия

Корреляция просмотров и суммы покупки:
{regression["correlation"]:.3f}

Линейная модель:

purchase_amount =
{regression["a"]:.3f} * product_views
+ {regression["b"]:.3f}

MSE:
{regression["mse"]:.3f}

## 6. A/B-тестирование

Средняя сумма группы A:
{ab_test["mean_a"]:.2f}

Средняя сумма группы B:
{ab_test["mean_b"]:.2f}

Разница B - A:
{ab_test["diff"]:.2f}

p-value:
{ab_test["p_value"]:.4f}

Решение:
{ab_test["decision"]}

Cohen's d:
{ab_test["cohens_d"]:.3f}

## 7. Линейная алгебра

Целевой покупатель:
{int(df.loc[linear_algebra["target_idx"], "customer_id"])}

Самый похожий покупатель:
{int(df.loc[linear_algebra["best_idx"], "customer_id"])}

Cosine similarity:
{linear_algebra["similarity"]:.3f}

Итоговый score рассчитан через
матричное умножение матрицы признаков на вектор весов.

## 8. Вывод

Проект объединяет основные темы блока 4
на одном наборе данных покупателей.

Использованы статистика, вероятности,
формула Байеса, bootstrap, корреляция,
линейная регрессия, A/B-тестирование,
Cohen's d, cosine similarity,
матричное умножение и визуализация.

## 9. Файлы

Данные:
{DATA_PATH}

Отчёт:
{report_path}
"""

    report_path.write_text(
        text.strip(),
        encoding="utf-8",
    )

    print(
        f"Отчёт сохранён: {report_path}"
    )


# ============================================================
# Главная функция
# ============================================================

def main() -> None:
    print("=" * 60)
    print("СКВОЗНОЙ ПРОЕКТ БЛОКА 4 — ПОКУПАТЕЛИ")
    print("=" * 60)

    print("\n1. Генерация данных...")
    df = generate_data()

    print(
        f"Покупателей: {len(df)}"
    )

    print("\n2. Математическая статистика...")
    statistics = calculate_statistics(df)

    print(
        f"Средняя сумма покупки: "
        f"{statistics['mean']:.2f}"
    )

    print(
        f"Bootstrap CI: "
        f"[{statistics['ci_low']:.2f}; "
        f"{statistics['ci_high']:.2f}]"
    )

    print("\n3. Теория вероятностей...")
    probability = calculate_probability(df)

    print(
        f"P(purchase) = "
        f"{probability['p_purchase']:.3f}"
    )

    print(
        f"P(purchase | click) = "
        f"{probability['p_purchase_click']:.3f}"
    )

    print("\n4. Формула Байеса...")
    bayes = calculate_bayes(df)

    print(
        f"P(purchase | clicked) = "
        f"{bayes['p_purchase_given_clicked']:.3f}"
    )

    print("\n5. Корреляция и регрессия...")
    regression = calculate_regression(df)

    print(
        f"Correlation = "
        f"{regression['correlation']:.3f}"
    )

    print(
        f"MSE = "
        f"{regression['mse']:.3f}"
    )

    print("\n6. A/B-тестирование...")
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

    print(
        f"Решение: "
        f"{ab_test['decision']}"
    )

    print("\n7. Линейная алгебра...")
    linear_algebra = calculate_linear_algebra(df)

    print(
        "Самый похожий покупатель:",
        int(
            df.loc[
                linear_algebra["best_idx"],
                "customer_id",
            ]
        ),
    )

    print(
        "Cosine similarity:",
        f"{linear_algebra['similarity']:.3f}",
    )

    print("\n8. Визуализация...")
    save_visualizations(
        df,
        regression,
        ab_test,
        linear_algebra,
    )

    print("\n9. Отчёт...")
    save_report(
        df,
        statistics,
        probability,
        bayes,
        regression,
        ab_test,
        linear_algebra,
    )

    print("\n" + "=" * 60)
    print("ПРОЕКТ БЛОКА 4 ВЫПОЛНЕН")
    print("=" * 60)


if __name__ == "__main__":
    main()