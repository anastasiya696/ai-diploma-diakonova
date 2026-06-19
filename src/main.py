# 1. Список чисел

numbers = [5, 12, 27, 34, 48, 63]

print("Список чисел:", numbers)
print("Длина списка:", len(numbers))

assert len(numbers) == 6


# 2. Среднее значение

average_value = sum(numbers) / len(numbers)

print("Среднее значение:", average_value)

assert average_value > 0


# 3. Максимум и минимум

max_value = max(numbers)
min_value = min(numbers)

print("Максимум:", max_value)
print("Минимум:", min_value)

assert max_value == 63
assert min_value == 5


# 4. Фильтрация чисел

threshold = 30
result = []

for num in numbers:
    if num > threshold:
        result.append(num)

print("Числа больше порога:", result)

assert len(result) >= 1


# 5. Словарь товара

product = {
    "name": "Детская коляска",
    "category": "Транспорт",
    "price": 15990
}

print("Товар:", product)
print("Название товара:", product["name"])

assert product["price"] > 0


# 6. Список словарей

products = [
    {"name": "Детская коляска", "category": "Транспорт", "price": 15990},
    {"name": "Автокресло", "category": "Безопасность", "price": 8990},
    {"name": "Детская кроватка", "category": "Мебель", "price": 12490},
    {"name": "Развивающий коврик", "category": "Игрушки", "price": 3490}
]

print("\nСписок товаров:")

for product in products:
    print(product)

assert len(products) == 4


# 7. Фильтрация по категории

filtered_items = []

for product in products:
    if product["category"] == "Игрушки":
        filtered_items.append(product)

print("\nОтфильтрованные товары:")
print(filtered_items)

assert len(filtered_items) >= 1


# 8. Сортировка по цене

sorted_products = sorted(products, key=lambda x: x["price"])

print("\nТовары по возрастанию цены:")

for product in sorted_products:
    print(product)

assert sorted_products[0]["price"] <= sorted_products[-1]["price"]


# 9. Множество (set)

categories = [
    "Игрушки",
    "Мебель",
    "Игрушки",
    "Транспорт",
    "Мебель",
    "Игрушки"
]

unique_values = set(categories)

print("\nУникальные категории:")
print(unique_values)

assert len(unique_values) >= 2


# 10. Итоговое задание

products_extended = [
    {"name": "Детская коляска", "category": "Транспорт", "price": 15990},
    {"name": "Автокресло", "category": "Безопасность", "price": 8990},
    {"name": "Развивающий коврик", "category": "Игрушки", "price": 3490},
    {"name": "Конструктор", "category": "Игрушки", "price": 4990}
]

filtered_items = []

for product in products_extended:
    if product["category"] == "Игрушки":
        filtered_items.append(product)

sorted_items = sorted(
    filtered_items,
    key=lambda x: x["price"],
    reverse=True
)

best_item = sorted_items[0]

print("\nЛучшая игрушка:")
print(best_item)

assert best_item["price"] == 4990

print("\nВсе задания выполнены успешно!")