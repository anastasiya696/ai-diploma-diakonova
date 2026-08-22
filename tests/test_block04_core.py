"""Автопроверки проекта блока 4."""

import numpy as np

from src.block04_stats import (
    mean,
    median,
    std_sample,
    approx,
)

from src.block04_probability import (
    prob_event,
    prob_conditional,
)

from src.block04_bayes import (
    bayes_posterior,
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
    p_value_two_sided,
    decision,
    cohens_d,
)

from src.block04_linear_algebra import (
    dot,
    norm2,
    cosine_similarity,
    matvec,
    vector_length_2d,
    dot_2d,
    weighted_score,
)


def test_stats():
    """Проверка статистических функций."""
    values = [1, 2, 3, 4, 5]

    assert mean(values) == 3.0
    assert median(values) == 3.0

    assert approx(
        std_sample([3, 4, 5]),
        1.0
    )


def test_probability():
    """Проверка вероятностей."""
    values = [1, 2, 3, 4]

    assert (
        prob_event(
            values,
            lambda x: x > 2
        )
        == 0.5
    )

    assert (
        prob_conditional(
            values,
            lambda x: x % 2 == 0,
            lambda x: x > 2
        )
        == 0.5
    )


def test_bayes():
    """Проверка формулы Байеса."""
    result = bayes_posterior(
        p_b_given_a=0.8,
        p_a=0.1,
        p_b=0.2,
    )

    assert approx(
        result,
        0.4
    )


def test_bootstrap_ci():
    """Проверка bootstrap."""
    values = [
        10,
        11,
        12,
        13,
        14,
        15,
    ]

    low, high = bootstrap_ci_mean(
        values,
        n_boot=300,
        seed=1,
    )

    assert (
        low
        < mean(values)
        < high
    )


def test_correlation():
    """Проверка корреляции."""
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    assert approx(
        corr_pearson(x, y),
        1.0
    )


def test_regression():
    """Проверка линейной регрессии."""
    x = np.array(
        [1, 2, 3, 4],
        dtype=float
    )

    y = np.array(
        [3, 5, 7, 9],
        dtype=float
    )

    a, b = fit_linear_regression_1d(
        x,
        y
    )

    y_hat = predict_linear_1d(
        x,
        a,
        b
    )

    assert approx(a, 2.0)
    assert approx(b, 1.0)
    assert approx(
        mse(y, y_hat),
        0.0
    )


def test_hypothesis_helpers():
    """Проверка A/B-тестирования."""
    assert (
        p_value_two_sided(
            2.0,
            [-3, -1, 0, 1, 3]
        )
        == 0.4
    )

    assert (
        "значимо"
        in decision(0.01)
    )

    assert (
        cohens_d(
            [1, 2, 3],
            [3, 4, 5]
        )
        > 0
    )


def test_linear_algebra():
    """Проверка линейной алгебры."""
    assert (
        dot(
            [1, 2, 3],
            [2, 1, 0]
        )
        == 4.0
    )

    assert (
        norm2([3, 4])
        == 5.0
    )

    assert (
        cosine_similarity(
            [1, 0],
            [1, 0]
        )
        == 1.0
    )

    X = np.array(
        [
            [1, 2],
            [3, 4],
        ],
        dtype=float
    )

    w = np.array(
        [10, 1],
        dtype=float
    )

    assert np.allclose(
        matvec(X, w),
        X @ w
    )

    assert (
        vector_length_2d([3, 4])
        == 5.0
    )

    assert (
        dot_2d(
            [2, 1],
            [1, 3]
        )
        == 5.0
    )


def test_weighted_score():
    """Проверка матричного score."""
    matrix = np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
        ],
        dtype=float
    )

    weights = np.array(
        [0.5, 0.3, 0.2],
        dtype=float
    )

    result = weighted_score(
        matrix,
        weights
    )

    assert np.allclose(
        result,
        [0.5, 0.3]
    )