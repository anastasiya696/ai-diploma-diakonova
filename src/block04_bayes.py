"""Формула Байеса для проекта по покупателям."""

from __future__ import annotations


def build_binary_counts(
    records,
    a_key: str,
    b_key: str
) -> dict:
    """Подсчёт событий A, B и A∩B."""
    n = len(records)

    if n == 0:
        raise ValueError(
            "build_binary_counts: empty records"
        )

    count_a = sum(
        1 for row in records
        if bool(row[a_key])
    )

    count_b = sum(
        1 for row in records
        if bool(row[b_key])
    )

    count_ab = sum(
        1
        for row in records
        if bool(row[a_key])
        and bool(row[b_key])
    )

    return {
        "n": n,
        "count_a": count_a,
        "count_b": count_b,
        "count_ab": count_ab,
    }


def prob_from_counts(
    count: int,
    total: int
) -> float:
    """Вероятность count / total."""
    if total <= 0:
        raise ValueError(
            "prob_from_counts: total must be positive"
        )

    return float(count / total)


def prob_conditional(
    count_ab: int,
    count_b: int
) -> float:
    """P(A|B) = P(A∩B) / P(B)."""
    if count_b <= 0:
        raise ValueError(
            "prob_conditional: condition count is zero"
        )

    return float(count_ab / count_b)


def bayes_posterior(
    p_b_given_a: float,
    p_a: float,
    p_b: float
) -> float:
    """P(A|B) = P(B|A) * P(A) / P(B)."""
    if p_b == 0:
        raise ValueError(
            "bayes_posterior: p_b is zero"
        )

    return float(
        p_b_given_a * p_a / p_b
    )


def score_buy_probability(
    clicked: bool,
    p_buy_if_click: float,
    p_buy_if_no_click: float
) -> float:
    """Скоринг вероятности покупки."""
    return float(
        p_buy_if_click
        if clicked
        else p_buy_if_no_click
    )


def laplace_smooth_prob(
    success_count: int,
    total_count: int,
    alpha: float = 1.0
) -> float:
    """Лапласовское сглаживание бинарной вероятности."""
    if total_count < 0:
        raise ValueError(
            "laplace_smooth_prob: total_count < 0"
        )

    if alpha <= 0:
        raise ValueError(
            "laplace_smooth_prob: alpha must be positive"
        )

    return float(
        (success_count + alpha)
        / (total_count + 2 * alpha)
    )