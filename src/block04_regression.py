"""Линейная регрессия 1D."""

from __future__ import annotations

import numpy as np

from .block04_stats import (
    mean,
    variance_population
)


def cov_population(
    x_values,
    y_values
) -> float:
    """Ковариация с делением на n."""
    x_values = list(x_values)
    y_values = list(y_values)

    if len(x_values) != len(y_values):
        raise ValueError(
            "cov_population: length mismatch"
        )

    if len(x_values) == 0:
        raise ValueError(
            "cov_population: empty values"
        )

    mx = mean(x_values)
    my = mean(y_values)

    return float(
        sum(
            (x - mx) * (y - my)
            for x, y in zip(
                x_values,
                y_values
            )
        ) / len(x_values)
    )


def fit_linear_regression_1d(
    x_values,
    y_values
) -> tuple[float, float]:
    """Обучение модели y = a*x + b."""
    var_x = variance_population(x_values)

    if var_x == 0:
        raise ValueError(
            "fit_linear_regression_1d: "
            "variance of x is zero"
        )

    a = (
        cov_population(
            x_values,
            y_values
        )
        / var_x
    )

    b = (
        mean(y_values)
        - a * mean(x_values)
    )

    return float(a), float(b)


def predict_linear_1d(
    x_values,
    a: float,
    b: float
):
    """Прогноз y_hat = a*x + b."""
    x_values = np.asarray(
        x_values,
        dtype=float
    )

    return a * x_values + b


def mse(
    y_true,
    y_pred
) -> float:
    """Mean squared error."""
    y_true = np.asarray(
        y_true,
        dtype=float
    )

    y_pred = np.asarray(
        y_pred,
        dtype=float
    )

    if len(y_true) != len(y_pred):
        raise ValueError(
            "mse: length mismatch"
        )

    return float(
        np.mean(
            (y_true - y_pred) ** 2
        )
    )