import numpy as np
import matplotlib.pyplot as plt

print("=== START LAB: FUNCTIONS AND GRAPHS ===")


# =========================
# 1. LINEAR FUNCTION (ARRAY)
# =========================
x = np.array([2, 4, 6, 8, 10])
y = 2 * x + 1

print("\nLinear function (array):")
print("x =", x)
print("y =", y)

assert len(x) == len(y)


# =========================
# 2. LINEAR FUNCTION PLOT
# =========================
x = np.linspace(-5, 15, 100)
y = 2 * x + 1

plt.figure()
plt.plot(x, y)
plt.title("y = 2x + 1")
plt.grid(True)
plt.show()


# =========================
# 3. COMPARE LINEAR FUNCTIONS
# =========================
x = np.linspace(-8, 8, 100)

plt.figure()
plt.plot(x, x, label="y = x")
plt.plot(x, 2 * x, label="y = 2x")
plt.plot(x, -x, label="y = -x")
plt.legend()
plt.title("Linear function comparison")
plt.grid(True)
plt.show()


# =========================
# 4. SHIFT (b COEFFICIENT)
# =========================
x = np.linspace(-10, 10, 100)

plt.figure()
plt.plot(x, x, label="y = x")
plt.plot(x, x + 5, label="y = x + 5")
plt.plot(x, x - 5, label="y = x - 5")
plt.legend()
plt.title("Effect of shift (b)")
plt.grid(True)
plt.show()


# =========================
# 5. QUADRATIC FUNCTION
# =========================
x = np.linspace(-12, 12, 200)
y = x ** 2

plt.figure()
plt.plot(x, y)
plt.title("y = x^2")
plt.grid(True)
plt.show()


# =========================
# 6. QUADRATIC COMPARISON
# =========================
x = np.linspace(-12, 12, 200)

y1 = x ** 2
y2 = 2 * x ** 2
y3 = x ** 2 + 10

plt.figure()
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="2x^2")
plt.plot(x, y3, label="x^2 + 10")
plt.legend()
plt.title("Quadratic comparison")
plt.grid(True)
plt.show()


# =========================
# 7. MIN / MAX
# =========================
x = np.arange(-12, 13)
y = x ** 2

min_y = np.min(y)
max_y = np.max(y)

print("\nMin value:", min_y)
print("Max value:", max_y)

assert min_y == 0
assert max_y == 144


# =========================
# 8. TRAINING LOSS
# =========================
metrics = {
    "epoch": list(range(1, 11)),
    "loss": [0.9, 0.75, 0.6, 0.5, 0.42, 0.35, 0.3, 0.25, 0.22, 0.2]
}

plt.figure()
plt.plot(metrics["epoch"], metrics["loss"])
plt.title("Model training loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

assert len(metrics["epoch"]) == len(metrics["loss"])


# =========================
# 9. SUMMARY
# =========================
summary = [
    "Function maps x values to y values",
    "Linear functions create straight lines",
    "Graphs help visualize data relationships",
    "Quadratic functions create parabolas"
]

print("\nSUMMARY:")
for s in summary:
    print("-", s)

assert len(summary) == 4

print("\n=== END LAB ===")