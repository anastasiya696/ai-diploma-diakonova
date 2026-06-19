import numpy as np


# =========================
# 1. ANALYSIS POINTS
# =========================

points = np.linspace(-5, 5, 20)

for x in points:
    derivative = 2 * x + 3

    if derivative > 0:
        status = "растёт"
    elif derivative < 0:
        status = "убывает"
    else:
        status = "возможный экстремум"

    print(f"x = {x:.2f}, derivative = {derivative:.2f} → функция {status}")


# =========================
# 2. RULES SUMMARY
# =========================

rules = [
    "Производная показывает скорость изменения функции",
    "Если производная > 0, функция растёт",
    "Если производная < 0, функция убывает",
    "Если производная = 0, возможен экстремум",
    "Касательная показывает локальное поведение функции",
    "График помогает визуально понимать поведение функции"
]

for rule in rules:
    print(rule)

assert len(rules) == 6


print("DONE")