"""Математическая статистика для проекта по покупателям."""

from __future__ import annotations


def mean(values) -> float:
    """Среднее арифметическое."""
    values = list(values)

    if len(values) == 0:
        raise ValueError("mean: empty values")

    return float(sum(values) / len(values))


def median(values) -> float:
    """Медиана."""
    values = sorted(list(values))
    n = len(values)

    if n == 0:
        raise ValueError("median: empty values")

    middle = n // 2

    if n % 2 == 1:
        return float(values[middle])

    return float((values[middle - 1] + values[middle]) / 2)


def variance_sample(values) -> float:
    """Выборочная дисперсия с делением на n - 1."""
    values = list(values)
    n = len(values)

    if n < 2:
        raise ValueError("variance_sample: need at least 2 values")

    m = mean(values)

    return float(
        sum((x - m) ** 2 for x in values) / (n - 1)
    )


def variance_population(values) -> float:
    """Дисперсия генеральной совокупности с делением на n."""
    values = list(values)

    if len(values) == 0:
        raise ValueError("variance_population: empty values")

    m = mean(values)

    return float(
        sum((x - m) ** 2 for x in values) / len(values)
    )


def std_sample(values) -> float:
    """Выборочное стандартное отклонение."""
    return float(variance_sample(values) ** 0.5)


def sem(values) -> float:
    """Стандартная ошибка среднего."""
    values = list(values)

    if len(values) < 2:
        raise ValueError("sem: need at least 2 values")

    return float(
        std_sample(values) / (len(values) ** 0.5)
    )


def trimmed_mean(
    values,
    proportion_to_cut: float = 0.1
) -> float:
    """Усечённое среднее."""
    values = sorted(list(values))
    n = len(values)

    if n == 0:
        raise ValueError("trimmed_mean: empty values")

    if not 0 <= proportion_to_cut < 0.5:
        raise ValueError(
            "trimmed_mean: proportion must be in [0, 0.5)"
        )

    k = int(n * proportion_to_cut)

    trimmed = values[k:n - k] if k > 0 else values

    if len(trimmed) == 0:
        raise ValueError("trimmed_mean: empty result")

    return mean(trimmed)


def describe(values) -> dict:
    """Краткое описание числовой выборки."""
    values = list(values)

    if len(values) == 0:
        raise ValueError("describe: empty values")

    return {
        "n": len(values),
        "mean": mean(values),
        "median": median(values),
        "std_sample": std_sample(values),
        "min": float(min(values)),
        "max": float(max(values)),
    }


def approx(
    x: float,
    y: float,
    eps: float = 1e-6
) -> bool:
    """Проверка приблизительного равенства."""
    return abs(x - y) <= eps