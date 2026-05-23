import sqlite3

print("Модуль sqlite3 подключен")

connection = sqlite3.connect("my_first_database.db")
print("База данных создана и подключена")

cursor = connection.cursor()
print("Cursor создан")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    price INTEGER
)
""")

print("Таблица products создана")

cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Смартфон", "Электроника", 45000)
)

cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Кроссовки", "Одежда", 8500)
)

cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Кофеварка", "Бытовая техника", 12000)
)

print("Товары добавлены")

connection.commit()
print("Изменения сохранены")

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

print(products)

assert len(products) >= 3

for id, title, category, price in products:
    print(f"ID: {id}, Товар: {title}, Категория: {category}, Цена: {price}")

cursor.execute(
    "SELECT * FROM products WHERE price > ?",
    (10000,)
)

expensive_products = cursor.fetchall()

print(expensive_products)

assert expensive_products is not None

connection.close()

print("Соединение с базой данных закрыто")