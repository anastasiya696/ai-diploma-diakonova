"""Ковариация и корреляция Пирсона."""

from __future__ import annotations

from .block04_stats import mean, std_sample


def cov_sample(
    x_values,
    y_values
) -> float:
    """Выборочная ковариация."""
    x_values = list(x_values)
    y_values = list(y_values)

    if len(x_values) != len(y_values):
        raise ValueError(
            "cov_sample: length mismatch"
        )

    if len(x_values) < 2:
        raise ValueError(
            "cov_sample: need at least 2 values"
        )

    mx = mean(x_values)
    my = mean(y_values)

    result = sum(
        (x - mx) * (y - my)
        for x, y in zip(
            x_values,
            y_values
        )
    ) / (len(x_values) - 1)

    return float(result)


def corr_pearson(
    x_values,
    y_values
) -> float:
    """Корреляция Пирсона."""
    sx = std_sample(x_values)
    sy = std_sample(y_values)

    if sx == 0 or sy == 0:
        raise ValueError(
            "corr_pearson: zero std"
        )

    return float(
        cov_sample(
            x_values,
            y_values
        ) / (sx * sy)
    )