import sqlite3

# ---------------------------------
# Ячейка 1. Подключение sqlite3
# ---------------------------------

print("Модуль sqlite3 успешно подключён для магазина детских товаров")

# ---------------------------------
# Ячейка 2. Функция подключения
# ---------------------------------

def get_connection(db_name):
    return sqlite3.connect(db_name)

connection = get_connection("kids_store.db")

print("Подключение к базе данных магазина детских товаров выполнено успешно")

assert connection is not None

# ---------------------------------
# Ячейка 3. Создание таблицы
# ---------------------------------

def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    connection.commit()

create_table(connection)

# ---------------------------------
# Ячейка 4. Очистка таблицы
# ---------------------------------

def clear_table(connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM products")

    connection.commit()

clear_table(connection)

# ---------------------------------
# Ячейка 5. Добавление записей
# ---------------------------------

def add_record(connection, name, category, price, quantity):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    """, (name, category, price, quantity))

    connection.commit()

add_record(connection, "Конструктор LEGO", "Игрушки", 2499.99, 15)
add_record(connection, "Детская коляска", "Транспорт", 12999.99, 5)
add_record(connection, "Детский комбинезон", "Одежда", 1999.99, 20)

# ---------------------------------
# Ячейка 6. Получение всех записей
# ---------------------------------

def get_all_records(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    return cursor.fetchall()

records = get_all_records(connection)

print("\nВсе записи:")
for record in records:
    print(record)

assert len(records) >= 3

# ---------------------------------
# Ячейка 7. Фильтрация по категории
# ---------------------------------

def find_by_text_field(connection, value):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE category = ?",
        (value,)
    )

    return cursor.fetchall()

result = find_by_text_field(connection, "Игрушки")

print("\nПоиск по категории:")
for row in result:
    print(row)

assert len(result) > 0

# ---------------------------------
# Ячейка 8. Поиск одной записи
# ---------------------------------

def find_one_record(connection, value):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (value,)
    )

    return cursor.fetchone()

record = find_one_record(connection, "Конструктор LEGO")

print("\nОдна запись:")
print(record)

assert record is not None

# ---------------------------------
# Ячейка 9. UPDATE
# ---------------------------------

def update_record(connection, name, new_price):
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE products SET price = ? WHERE name = ?",
        (new_price, name)
    )

    connection.commit()

update_record(connection, "Конструктор LEGO", 2799.99)

updated_record = find_one_record(connection, "Конструктор LEGO")

print("\nПосле обновления:")
print(updated_record)

assert updated_record[3] == 2799.99

# ---------------------------------
# Ячейка 10. DELETE
# ---------------------------------

def delete_record(connection, name):
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE name = ?",
        (name,)
    )

    connection.commit()

delete_record(connection, "Детский комбинезон")

records = get_all_records(connection)

print("\nПосле удаления:")
for record in records:
    print(record)

assert len(records) == 2

connection.close()

print("\nСоединение с базой данных закрыто")