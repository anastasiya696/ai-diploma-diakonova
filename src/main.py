import numpy as np
import matplotlib.pyplot as plt

# ===== Ячейка 1 =====
print("Библиотеки импортированы")

# ===== Ячейка 2: y = x^2 =====
x = np.linspace(-5, 5, 200)
y = x ** 2

plt.figure()
plt.plot(x, y)
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 3: y = x^3 =====
x = np.linspace(-5, 5, 200)
y = x ** 3

plt.figure()
plt.plot(x, y)
plt.title("y = x³")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 4: sqrt(x) =====
x = np.linspace(0, 25, 200)
y = np.sqrt(x)

plt.figure()
plt.plot(x, y)
plt.title("y = √x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 5: 2^x =====
x = np.linspace(-2, 2, 200)
y = 2 ** x

plt.figure()
plt.plot(x, y)
plt.title("y = 2^x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 6: log(x) =====
x = np.linspace(0.1, 20, 200)
y = np.log(x)

plt.figure()
plt.plot(x, y)
plt.title("y = ln(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 7: sin(x) =====
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title("y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 8: cos(x) =====
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.cos(x)

plt.figure()
plt.plot(x, y)
plt.title("y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ===== Ячейка 9: sin vs cos =====
x = np.linspace(-2*np.pi, 2*np.pi, 200)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure()
plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.title("sin(x) и cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# ===== Ячейка 10: сравнение функций =====
x = np.linspace(0.1, 5, 200)

y_linear = x
y_square = x ** 2
y_log = np.log(x)
y_exp = 2 ** x

plt.figure()
plt.plot(x, y_linear, label="x")
plt.plot(x, y_square, label="x^2")
plt.plot(x, y_log, label="log(x)")
plt.plot(x, y_exp, label="2^x")

plt.title("Сравнение функций")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

summary = [
    "Линейная функция растёт равномерно",
    "Квадратичная растёт быстрее линейной",
    "Логарифм растёт медленно и замедляется",
    "Экспонента растёт быстрее всех"
]

print(summary)