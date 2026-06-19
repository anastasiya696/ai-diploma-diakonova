import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 1. x_values около 3
# =========================

x_values = np.linspace(2.5, 3.5, 10)

# original function (x^2 - 9)/(x - 3)
original_values = (x_values**2 - 9) / (x_values - 3)

# убрать бесконечности (x=3)
original_values = np.where(np.isfinite(original_values), original_values, np.nan)

# simple function
simple_values = x_values + 3

df = pd.DataFrame({
    "x": x_values,
    "(x^2 - 9)/(x - 3)": original_values,
    "x + 3": simple_values
})

print(df)


# =========================
# 2. LIMIT GRAPH (левая и правая часть)
# =========================

x_left = np.linspace(1, 2.99, 50)
x_right = np.linspace(3.01, 5, 50)

y_left = 2 * x_left
y_right = 2 * x_right

plt.figure()
plt.plot(x_left, y_left, label="left")
plt.plot(x_right, y_right, label="right")
plt.scatter([3], [6], color="red", label="limit point (3,6)")
plt.legend()
plt.grid(True)
plt.show()


# =========================
# 3. TRAINING METRIC
# =========================

epochs = list(range(1, 21))

metric = [
    0.2, 0.35, 0.5, 0.62, 0.7,
    0.78, 0.83, 0.87, 0.9, 0.92,
    0.93, 0.935, 0.94, 0.942, 0.943,
    0.944, 0.9445, 0.9447, 0.9448, 0.945
]

plt.figure()
plt.plot(epochs, metric, label="metric")
plt.axhline(y=0.95, color="red", linestyle="--", label="limit ~0.95")
plt.legend()
plt.grid(True)
plt.show()

assert metric[-1] > metric[0]


# =========================
# 4. SUMMARY
# =========================

summary = [
    "Алгоритм — это последовательность шагов",
    "Структуры данных помогают работать с информацией",
    "Графики показывают поведение функций",
    "Пределы помогают анализировать поведение функции",
    "Метрики в AI обычно растут и стабилизируются"
]

for s in summary:
    print(s)

assert len(summary) == 5

print("ALL TASKS DONE")