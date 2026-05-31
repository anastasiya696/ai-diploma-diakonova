import sqlite3

# =========================
# 1. Подключение
# =========================

def get_connection(db_name):
    return sqlite3.connect(db_name)

connection = get_connection("my_kids_world_project.db")

print("Подключение к базе данных 'Детский мир' выполнено успешно")
assert connection is not None


# =========================
# 2. Создание таблицы
# =========================

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


# =========================
# 3. Очистка таблицы
# =========================

def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products")
    connection.commit()

clear_table(connection)


# =========================
# 4. Добавление записей
# =========================

def add_record(connection, name, category, price, quantity):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    """, (name, category, price, quantity))

    connection.commit()


add_record(connection, "Конструктор LEGO", "Игрушки", 2499.99, 15)
add_record(connection, "Кукла LOL", "Куклы", 1599.99, 20)
add_record(connection, "Мягкий медведь", "Мягкие игрушки", 899.99, 30)
add_record(connection, "Детский самокат", "Транспорт", 3499.99, 10)
add_record(connection, "Набор фломастеров", "Творчество", 299.99, 50)


# =========================
# 5. Получение всех записей
# =========================

def get_all_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

records = get_all_records(connection)

print("\nВСЕ ТОВАРЫ:")
for r in records:
    print(r)

assert len(records) >= 5


# =========================
# 6. Фильтр по категории
# =========================

def find_by_field(connection, value):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE category = ?", (value,))
    return cursor.fetchall()

filtered_records = find_by_field(connection, "Игрушки")

print("\nФИЛЬТР (Игрушки):")
for r in filtered_records:
    print(r)

assert len(filtered_records) > 0


# =========================
# 7. Поиск одной записи
# =========================

def find_one_record(connection, value):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE name = ?", (value,))
    return cursor.fetchone()

record = find_one_record(connection, "Конструктор LEGO")

print("\nОДНА ЗАПИСЬ:")
print(record)

assert record is not None


# =========================
# 8. UPDATE
# =========================

def update_record(connection, name, new_price):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE products
        SET price = ?
        WHERE name = ?
    """, (new_price, name))
    connection.commit()

update_record(connection, "Конструктор LEGO", 2799.99)

updated_record = find_one_record(connection, "Конструктор LEGO")
print("\nПОСЛЕ UPDATE:")
print(updated_record)

assert updated_record[3] == 2799.99


# =========================
# 9. GROUP BY (аналитика)
# =========================

def get_group_report(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category, COUNT(*)
        FROM products
        GROUP BY category
    """)
    return cursor.fetchall()

report = get_group_report(connection)

print("\nОТЧЁТ ПО КАТЕГОРИЯМ:")
for r in report:
    print(r)

assert len(report) >= 1


# =========================
# 10. TOP-3
# =========================

def get_top_records(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name, category, price, quantity
        FROM products
        ORDER BY price DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()

top_records = get_top_records(connection, 3)

print("\nТОП-3 ТОВАРА:")
for r in top_records:
    print(r)

assert len(top_records) == 3


# =========================
# ФИНАЛ
# =========================

print("\n" + "="*50)
print("ФИНАЛЬНЫЙ ОТЧЁТ ПРОЕКТА 'ДЕТСКИЙ МИР'")
print("="*50)

print("\nВСЕ ТОВАРЫ:")
for r in get_all_records(connection):
    print(r)

print("\nФИЛЬТР (Игрушки):")
for r in find_by_field(connection, "Игрушки"):
    print(r)

print("\nОТЧЁТ ПО КАТЕГОРИЯМ:")
for r in get_group_report(connection):
    print(r)

print("\nТОП-3:")
for r in get_top_records(connection, 3):
    print(r)

connection.close()

print("\nСоединение с базой закрыто. Проект завершён.")