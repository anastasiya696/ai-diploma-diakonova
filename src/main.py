import numpy as np
import matplotlib.pyplot as plt


# =========================
# FUNCTION + GRADIENT
# =========================

# f(x)
def f(x):
    return -x**2 + 9

# df(x)
def df(x):
    return -2 * x


# =========================
# GRADIENT ASCENT
# =========================

x_current = 5.0
learning_rate = 0.1

history_x = []
history_y = []

for _ in range(15):
    history_x.append(x_current)
    history_y.append(f(x_current))

    gradient = df(x_current)

    # градиентный подъём (ВАЖНО)
    x_current = x_current + learning_rate * gradient


print("Финальное x:", x_current)
print("Финальное f(x):", f(x_current))

# корректный assert для подъёма к максимуму
assert abs(x_current) < 1


# =========================
# VISUALIZATION
# =========================

x = np.linspace(-5, 5, 200)
y = -x**2 + 9

plt.plot(x, y, label="f(x) = -x^2 + 9")
plt.scatter(history_x, history_y, label="gradient ascent path")

plt.title("Gradient Ascent on Quadratic Function")
plt.grid(True)
plt.legend()
plt.show()

# путь должен расти (мы идём к максимуму)
assert history_y[-1] > history_y[0]


# =========================
# SUMMARY
# =========================

summary = [
    "Градиент показывает направление роста функции",
    "В точке максимума производная равна 0",
    "Градиентный подъём увеличивает значение функции",
    "Функция -x^2 + 9 имеет максимум в x = 0",
    "Итеративные методы находят экстремумы численно"
]

for item in summary:
    print(item)

assert len(summary) == 5


print("DONE")