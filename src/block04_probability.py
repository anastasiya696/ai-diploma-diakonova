"""Теория вероятностей для проекта по покупателям."""

from __future__ import annotations

import numpy as np


def prob_event(values, event_func) -> float:
    """Вероятность события по данным."""
    values = list(values)

    if len(values) == 0:
        raise ValueError("prob_event: empty values")

    count = sum(
        1 for x in values
        if event_func(x)
    )

    return float(count / len(values))


def prob_conditional(
    values,
    condition_func,
    event_func
) -> float:
    """Условная вероятность P(event | condition)."""
    values = list(values)

    filtered = [
        x for x in values
        if condition_func(x)
    ]

    if len(filtered) == 0:
        raise ValueError(
            "prob_conditional: empty condition"
        )

    count = sum(
        1 for x in filtered
        if event_func(x)
    )

    return float(count / len(filtered))


def is_independent_by_counts(
    p_a: float,
    p_b: float,
    p_ab: float,
    eps: float = 1e-6
) -> bool:
    """Проверка независимости событий."""
    return abs(p_ab - p_a * p_b) <= eps


def contingency_2x2(
    records,
    a_key: str,
    b_key: str
) -> dict:
    """Таблица сопряжённости 2x2."""
    result = {
        "a1_b1": 0,
        "a1_b0": 0,
        "a0_b1": 0,
        "a0_b0": 0,
    }

    for row in records:
        a = bool(row[a_key])
        b = bool(row[b_key])

        if a and b:
            result["a1_b1"] += 1
        elif a and not b:
            result["a1_b0"] += 1
        elif not a and b:
            result["a0_b1"] += 1
        else:
            result["a0_b0"] += 1

    return result


def simulate_click_buy(
    n: int = 1000,
    seed: int = 42
):
    """Симуляция клика и покупки."""
    if n <= 0:
        raise ValueError("n must be positive")

    rng = np.random.default_rng(seed)

    records = []

    for _ in range(n):
        click = bool(
            rng.random() < 0.35
        )

        if click:
            buy = bool(
                rng.random() < 0.18
            )
        else:
            buy = bool(
                rng.random() < 0.04
            )

        records.append({
            "click": click,
            "buy": buy,
        })

    return records


def estimate_p_buy_given_click1(records) -> float:
    """Оценка P(buy | click)."""
    return prob_conditional(
        records,
        condition_func=lambda row: bool(row["click"]),
        event_func=lambda row: bool(row["buy"]),
    )