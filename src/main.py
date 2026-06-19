import numpy as np
import matplotlib.pyplot as plt


# =========================
# IMPORT (из ноутбука)
# =========================

print("Notebook: Loss + Summary")


# =========================
# LOSS EXPERIMENT
# =========================

# epochs
epochs = list(range(1, 21))

# smooth loss (плавно убывает)
smooth_loss = np.linspace(2.0, 0.5, 20)

# jump loss (скачки)
jump_loss = [
    2.0, 1.8, 2.1, 1.6, 1.9,
    1.4, 1.7, 1.2, 1.5, 1.1,
    1.3, 0.9, 1.0, 0.8, 0.95,
    0.7, 0.85, 0.6, 0.55, 0.5
]

# график
plt.figure()
plt.plot(epochs, smooth_loss, label="smooth loss")
plt.plot(epochs, jump_loss, label="jump loss")

plt.title("Smooth vs Jump Loss")
plt.grid(True)
plt.legend()
plt.show()


# assert
assert smooth_loss[-1] < smooth_loss[0]


# =========================
# SUMMARY BLOCK
# =========================

summary = [
    "Функции могут быть гладкими или с разрывами",
    "Графики помогают анализировать данные",
    "Loss может уменьшаться по-разному",
    "Алгоритмы работают пошагово",
    "Проверка результатов важна"
]

for item in summary:
    print(item)

# assert
assert len(summary) == 5


print("DONE")