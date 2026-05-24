import sqlite3
from reports import (
    get_all_categories,
    get_all_products,
    get_products_by_category
)

# подключение к базе
connection = sqlite3.connect("kids_products.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# ===== СОЗДАНИЕ ТАБЛИЦ (ВАЖНО!) =====
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    name TEXT NOT NULL,
    price REAL,
    age_group TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

connection.commit()

# ===== ЕСЛИ ТАБЛИЦЫ ПУСТЫЕ — МОЖНО ДОБАВИТЬ ДАННЫЕ =====

cursor.execute("SELECT COUNT(*) FROM categories")
if cursor.fetchone()[0] == 0:

    cursor.executemany("""
    INSERT INTO categories (name)
    VALUES (?)
    """, [
        ("Игрушки",),
        ("Одежда",),
        ("Питание",)
    ])

    connection.commit()

# ===== ПОЛУЧАЕМ ДАННЫЕ =====

cursor.execute("SELECT * FROM categories")
categories = cursor.fetchall()

category_id_1 = categories[0][0]

# добавим товары, если их нет
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:

    cursor.executemany("""
    INSERT INTO products (category_id, name, price, age_group)
    VALUES (?, ?, ?, ?)
    """, [
        (category_id_1, "Конструктор LEGO", 1500.0, "3+"),
        (category_id_1, "Мягкая игрушка", 800.0, "0+"),
    ])

    connection.commit()

# ===== ВЫВОД ЧЕРЕЗ reports.py =====

print("Категории:")
print(get_all_categories(cursor))

print("\nВсе товары:")
print(get_all_products(cursor))

print("\nТовары категории 1:")
print(get_products_by_category(cursor, category_id_1))

# закрытие
connection.close()