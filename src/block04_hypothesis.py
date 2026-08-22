"""A/B-тестирование и permutation test."""

from __future__ import annotations

import numpy as np

from .block04_stats import (
    mean,
    std_sample
)


def permutation_test_diff_means(
    A,
    B,
    n_perm: int = 2000,
    seed: int = 0
):
    """Перестановочные разницы mean(B) - mean(A)."""
    rng = np.random.default_rng(seed)

    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)

    if len(A) == 0 or len(B) == 0:
        raise ValueError(
            "permutation_test_diff_means: "
            "empty group"
        )

    if n_perm <= 0:
        raise ValueError(
            "n_perm must be positive"
        )

    n_a = len(A)
    pool = np.concatenate([A, B])

    diffs = []

    for _ in range(n_perm):
        perm = rng.permutation(pool)

        A_perm = perm[:n_a]
        B_perm = perm[n_a:]

        diffs.append(
            mean(B_perm) - mean(A_perm)
        )

    return np.asarray(
        diffs,
        dtype=float
    )


def p_value_two_sided(
    diff_obs: float,
    diffs_perm
) -> float:
    """Двустороннее p-value."""
    diffs_perm = list(diffs_perm)

    if len(diffs_perm) == 0:
        raise ValueError(
            "p_value_two_sided: empty diffs"
        )

    count = sum(
        1
        for d in diffs_perm
        if abs(d) >= abs(diff_obs)
    )

    return float(
        count / len(diffs_perm)
    )


def decision(
    p_value: float,
    alpha: float = 0.05
) -> str:
    """Решение по p-value."""
    if not 0 <= p_value <= 1:
        raise ValueError(
            "p_value must be from 0 to 1"
        )

    if not 0 < alpha < 1:
        raise ValueError(
            "alpha must be from 0 to 1"
        )

    if p_value < alpha:
        return "значимо: отклоняем H0"

    return "не значимо: не отклоняем H0"


def cohens_d(A, B) -> float:
    """Размер эффекта Cohen's d."""
    A = list(A)
    B = list(B)

    if len(A) < 2 or len(B) < 2:
        raise ValueError(
            "cohens_d: need at least 2 values"
        )

    s_a = std_sample(A)
    s_b = std_sample(B)

    pooled = (
        (s_a ** 2 + s_b ** 2) / 2
    ) ** 0.5

    if pooled == 0:
        raise ValueError(
            "cohens_d: pooled std is 0"
        )

    return float(
        (mean(B) - mean(A))
        / pooled
    )