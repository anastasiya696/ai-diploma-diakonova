"""Bootstrap и доверительные интервалы."""

from __future__ import annotations

import numpy as np

from .block04_stats import mean, sem


def ci_mean_normal_approx(
    values,
    z: float = 1.96
) -> tuple[float, float]:
    """Нормальный доверительный интервал среднего."""
    m = mean(values)
    margin = z * sem(values)

    return (
        float(m - margin),
        float(m + margin)
    )


def bootstrap_means(
    values,
    n_boot: int = 2000,
    seed: int = 42
) -> np.ndarray:
    """Получение bootstrap-выборки средних."""
    rng = np.random.default_rng(seed)

    values = np.asarray(
        values,
        dtype=float
    )

    if len(values) == 0:
        raise ValueError(
            "bootstrap_means: empty values"
        )

    if n_boot <= 0:
        raise ValueError(
            "bootstrap_means: n_boot must be positive"
        )

    result = []

    for _ in range(n_boot):
        sample = rng.choice(
            values,
            size=len(values),
            replace=True
        )

        result.append(
            mean(sample)
        )

    return np.array(
        result,
        dtype=float
    )


def bootstrap_ci_mean(
    values,
    n_boot: int = 2000,
    alpha: float = 0.05,
    seed: int = 42
) -> tuple[float, float]:
    """Bootstrap confidence interval для среднего."""
    if not 0 < alpha < 1:
        raise ValueError(
            "alpha must be between 0 and 1"
        )

    means = bootstrap_means(
        values,
        n_boot=n_boot,
        seed=seed
    )

    low = float(
        np.quantile(
            means,
            alpha / 2
        )
    )

    high = float(
        np.quantile(
            means,
            1 - alpha / 2
        )
    )

    return low, high