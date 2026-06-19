import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Список чисел
# -----------------------------
numbers = [5, 12, 27, 34, 48, 63]

print("Список чисел:", numbers)
print("Длина списка:", len(numbers))

assert len(numbers) == 6


# -----------------------------
# 2. Среднее значение
# -----------------------------
average_value = sum(numbers) / len(numbers)

print("Среднее значение:", average_value)

assert average_value > 0


# -----------------------------
# 3. max / min
# -----------------------------
max_value = max(numbers)
min_value = min(numbers)

print("Максимум:", max_value)
print("Минимум:", min_value)

assert max_value == 63
assert min_value == 5


# -----------------------------
# 4. Фильтрация чисел
# -----------------------------
threshold = 30
result = []

for num in numbers:
    if num > threshold:
        result.append(num)

print("Числа > 30:", result)

assert len(result) >= 1


# -----------------------------
# 5. Словарь товара
# -----------------------------
product = {
    "name": "Детская коляска",
    "category": "Транспорт",
    "price": 15990
}

print("Товар:", product)
print("Название:", product["name"])

assert product["price"] > 0


# -----------------------------
# 6. Список словарей
# -----------------------------
products = [
    {"name": "Детская коляска", "category": "Транспорт", "price": 15990},
    {"name": "Автокресло", "category": "Безопасность", "price": 8990},
    {"name": "Детская кроватка", "category": "Мебель", "price": 12490},
    {"name": "Развивающий коврик", "category": "Игрушки", "price": 3490}
]

for p in products:
    print(p)

assert len(products) == 4


# -----------------------------
# 7. Фильтрация по категории
# -----------------------------
filtered_items = []

for p in products:
    if p["category"] == "Игрушки":
        filtered_items.append(p)

print("Игрушки:", filtered_items)

assert len(filtered_items) >= 1


# -----------------------------
# 8. Сортировка по цене
# -----------------------------
sorted_products = sorted(products, key=lambda x: x["price"])

for p in sorted_products:
    print(p)

assert sorted_products[0]["price"] <= sorted_products[-1]["price"]


# -----------------------------
# 9. SET (уникальные значения)
# -----------------------------
categories = ["Игрушки", "Мебель", "Игрушки", "Транспорт", "Мебель"]

unique_values = set(categories)

print("Уникальные категории:", unique_values)

assert len(unique_values) >= 2


# -----------------------------
# 10. Итоговое задание
# -----------------------------
products_extended = [
    {"name": "Коляска", "category": "Транспорт", "price": 15990},
    {"name": "Автокресло", "category": "Безопасность", "price": 8990},
    {"name": "Коврик", "category": "Игрушки", "price": 3490},
    {"name": "Конструктор", "category": "Игрушки", "price": 4990}
]

filtered_items = [p for p in products_extended if p["category"] == "Игрушки"]

sorted_items = sorted(filtered_items, key=lambda x: x["price"], reverse=True)

best_item = sorted_items[0]

print("Лучшая игрушка:", best_item)

assert best_item["price"] == 4990


# -----------------------------
# 11. График loss
# -----------------------------
epochs = list(range(1, 11))
loss = [10, 8.2, 6.5, 5.1, 4.0, 3.2, 2.6, 2.1, 1.7, 1.3]

plt.plot(epochs, loss, marker="o")
plt.title("Loss over epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

assert loss[-1] < loss[0]


# -----------------------------
# 12. SUMMARY
# -----------------------------
summary = [
    "Данные обработаны",
    "Фильтрация выполнена",
    "Сортировка выполнена",
    "Графики построены",
    "Анализ завершён"
]

for s in summary:
    print(s)

assert len(summary) == 5

print("\nВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО")