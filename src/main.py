import numpy as np
import matplotlib.pyplot as plt


# =========================
# LOSS + GRADIENT
# =========================

# создаём x
x = np.linspace(-5, 5, 200)

# loss = x^2
loss = x ** 2

# gradient = 2x
gradient = 2 * x

# график
plt.figure()

plt.plot(x, loss, label="loss = x^2")
plt.plot(x, gradient, label="gradient = 2x")

# минимум
plt.scatter([0], [0], color="red", label="minimum (0,0)")

plt.title("Loss and Gradient")
plt.grid(True)
plt.legend()

plt.show()

# FIXED ASSERT (важно!)
assert np.isclose(loss.min(), 0)


# =========================
# SUMMARY
# =========================

summary = [
    "Loss показывает ошибку модели",
    "Градиент показывает направление изменения функции",
    "Минимум функции находится в точке x = 0",
    "Квадратичная функция всегда неотрицательна",
    "Производная помогает находить экстремумы"
]

for item in summary:
    print(item)

assert len(summary) == 5


print("DONE")