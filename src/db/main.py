import sqlite3

# Подключение к базе
connection = sqlite3.connect('kids_shop_analytics.db')
cursor = connection.cursor()

# ----------------------------
# 1. Создание таблицы
# ----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    age_group INTEGER NOT NULL
)
""")
connection.commit()

# ----------------------------
# 2. Очистка и вставка данных
# ----------------------------
cursor.execute("DELETE FROM products")

products_data = [
    ("Конструктор LEGO", "Конструкторы", 2499.99, 15, 6),
    ("Кукла Барби", "Куклы", 1299.99, 20, 3),
    ("Мягкий медведь", "Мягкие игрушки", 899.99, 30, 1),
    ("Машинка Hot Wheels", "Машинки", 399.99, 50, 4),
    ("Настольная игра Монополия", "Игры", 1999.99, 10, 8),
    ("Детский самокат", "Транспорт", 3499.99, 8, 5),
    ("Пазл 500 деталей", "Пазлы", 799.99, 25, 7),
    ("Набор фломастеров", "Творчество", 299.99, 40, 4),
    ("Радиоуправляемая машина", "Электронные игрушки", 2799.99, 12, 8),
    ("Детский рюкзак", "Аксессуары", 1499.99, 18, 6)
]

cursor.executemany("""
INSERT INTO products (product_name, category, price, stock_quantity, age_group)
VALUES (?, ?, ?, ?, ?)
""", products_data)

connection.commit()

# ----------------------------
# 3. COUNT
# ----------------------------
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print("COUNT:", count)
assert count >= 10

# ----------------------------
# 4. SUM
# ----------------------------
cursor.execute("SELECT SUM(price) FROM products")
total_price = cursor.fetchone()[0]
print("SUM price:", total_price)
assert total_price > 0

# ----------------------------
# 5. AVG / MIN / MAX
# ----------------------------
cursor.execute("""
SELECT AVG(price), MIN(price), MAX(price)
FROM products
""")
avg_price, min_price, max_price = cursor.fetchone()
print("AVG:", avg_price, "MIN:", min_price, "MAX:", max_price)
assert max_price >= min_price

# ----------------------------
# 6. GROUP BY
# ----------------------------
cursor.execute("""
SELECT category, SUM(stock_quantity)
FROM products
GROUP BY category
""")
result = cursor.fetchall()
print("GROUP BY:")
for category, total in result:
    print(category, total)
assert len(result) >= 1

# ----------------------------
# 7. ORDER BY
# ----------------------------
cursor.execute("""
SELECT category, SUM(stock_quantity) AS total
FROM products
GROUP BY category
ORDER BY total DESC
""")
result = cursor.fetchall()
print("ORDER BY:")
for category, total in result:
    print(category, total)
assert len(result) >= 1

# ----------------------------
# 8. HAVING + CLOSE
# ----------------------------
threshold = 20

cursor.execute("""
SELECT category, SUM(stock_quantity)
FROM products
GROUP BY category
HAVING SUM(stock_quantity) > ?
""", (threshold,))

result = cursor.fetchall()

print("HAVING:")
for category, total in result:
    print(category, total)

assert all(total > threshold for _, total in result)

connection.close()
print("Connection closed.")