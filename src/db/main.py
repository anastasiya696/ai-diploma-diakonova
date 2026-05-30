import sqlite3

# Ячейка 1: подключение к БД
conn = sqlite3.connect("kids_shop_join.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

print("База создана")

# Ячейка 2: родительская таблица
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    city TEXT
)
""")
conn.commit()

print("clients создана")

# Ячейка 3: дочерняя таблица
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TEXT,
    client_id INTEGER,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
)
""")
conn.commit()

print("orders создана")

# Ячейка 4: очистка и родительские данные
cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM clients")

clients_data = [
    ("Анна Иванова", "+79991112233", "Москва"),
    ("Мария Петрова", "+79994445566", "Санкт-Петербург"),
    ("Елена Сидорова", "+79997778899", "Казань")
]

cursor.executemany("""
INSERT INTO clients (full_name, phone, city)
VALUES (?, ?, ?)
""", clients_data)

conn.commit()
print("Клиенты добавлены")

# Ячейка 5: получаем id и добавляем заказы
cursor.execute("SELECT * FROM clients")
clients = cursor.fetchall()

client_id_1 = clients[0][0]
client_id_2 = clients[1][0]

orders_data = [
    ("Конструктор LEGO", 1, "2025-05-01", client_id_1),
    ("Детская коляска", 1, "2025-05-03", client_id_1),
    ("Мягкая игрушка", 2, "2025-05-05", client_id_2)
]

cursor.executemany("""
INSERT INTO orders (product_name, quantity, order_date, client_id)
VALUES (?, ?, ?, ?)
""", orders_data)

conn.commit()
print("Заказы добавлены")

# Ячейка 6: вывод таблиц
cursor.execute("SELECT * FROM clients")
clients = cursor.fetchall()

cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

print("\nCLIENTS:")
for c in clients:
    print(c)

print("\nORDERS:")
for o in orders:
    print(o)

# Ячейка 7: INNER JOIN
cursor.execute("""
SELECT clients.full_name, orders.product_name
FROM clients
INNER JOIN orders
ON clients.client_id = orders.client_id
""")
print("\nINNER JOIN:", cursor.fetchall())

# Ячейка 8: INNER JOIN + WHERE
cursor.execute("""
SELECT clients.full_name, orders.product_name, clients.city
FROM clients
INNER JOIN orders
ON clients.client_id = orders.client_id
WHERE clients.city = 'Москва'
""")
print("\nWHERE JOIN:", cursor.fetchall())

# Ячейка 9: LEFT JOIN
cursor.execute("""
SELECT clients.full_name, orders.product_name
FROM clients
LEFT JOIN orders
ON clients.client_id = orders.client_id
""")
print("\nLEFT JOIN:", cursor.fetchall())

# Ячейка 10: отчёт
cursor.execute("""
SELECT
    clients.full_name,
    COUNT(orders.order_id),
    COALESCE(SUM(orders.quantity), 0)
FROM clients
LEFT JOIN orders
ON clients.client_id = orders.client_id
GROUP BY clients.client_id
""")

report = cursor.fetchall()

print("\nREPORT:")
for r in report:
    print(r)

conn.close()
print("\nГотово")