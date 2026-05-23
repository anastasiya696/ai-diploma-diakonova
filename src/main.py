import sqlite3

def main():
    # подключение к базе
    connection = sqlite3.connect("shop_lesson02.db")
    cursor = connection.cursor()

    # создание таблицы
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT,
        price REAL,
        count INTEGER
    )
    """)

    # очистка таблицы
    cursor.execute("DELETE FROM products")

    # тестовые данные
    products_data = [
        ("Apple iPhone 14", "electronics", 799.99, 10),
        ("Samsung Galaxy S23", "electronics", 699.99, 12),
        ("Nike Air Max", "shoes", 149.99, 25),
        ("Adidas Ultraboost", "shoes", 179.99, 18),
        ("Wooden Desk", "furniture", 250.00, 5),
        ("Office Chair", "furniture", 120.00, 8),
        ("Coffee Beans", "food", 12.50, 50),
        ("Green Tea", "food", 8.99, 40)
    ]

    cursor.executemany("""
    INSERT INTO products (title, category, price, count)
    VALUES (?, ?, ?, ?)
    """, products_data)

    connection.commit()

    # SELECT *
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print("Все товары:")
    for row in rows:
        print(row)

    # SELECT отдельных столбцов
    cursor.execute("SELECT title, price FROM products")
    rows = cursor.fetchall()
    print("\nНазвание и цена:")
    for row in rows:
        print(row)

    # WHERE числовое
    cursor.execute("SELECT * FROM products WHERE price > ?", (100,))
    rows = cursor.fetchall()
    print("\nЦена > 100:")
    for row in rows:
        print(row)

    # WHERE текстовое
    cursor.execute("SELECT * FROM products WHERE category = ?", ("electronics",))
    rows = cursor.fetchall()
    print("\nКатегория electronics:")
    for row in rows:
        print(row)

    # AND
    cursor.execute(
        "SELECT * FROM products WHERE category = ? AND price > ?",
        ("electronics", 700)
    )
    rows = cursor.fetchall()
    print("\nAND запрос:")
    for row in rows:
        print(row)

    # OR
    cursor.execute(
        "SELECT * FROM products WHERE category = ? OR category = ?",
        ("electronics", "food")
    )
    rows = cursor.fetchall()
    print("\nOR запрос:")
    for row in rows:
        print(row)

    # ORDER BY + LIMIT
    cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 3")
    rows = cursor.fetchall()
    print("\nTOP 3 дорогих товара:")
    for row in rows:
        print(row)

    # закрытие соединения
    connection.close()
    print("\nСоединение закрыто!")

if __name__ == "__main__":
    main()