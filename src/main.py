import sqlite3

# подключение к БД
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

print("База данных подключена!")

# создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")

connection.commit()
print("Таблица создана!")

# очистка таблицы
cursor.execute("DELETE FROM students")
connection.commit()

print("Таблица очищена!")

# просмотр данных
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Данные таблицы:")
for row in rows:
    print(row)

# UPDATE
cursor.execute("""
UPDATE students
SET age = 17
WHERE name = 'Алина'
""")

connection.commit()

print("Данные обновлены!")

# проверка UPDATE
cursor.execute("""
SELECT * FROM students
WHERE name = 'Алина'
""")

student = cursor.fetchone()

print(student)

# DELETE
cursor.execute("""
DELETE FROM students
WHERE name = 'Максим'
""")

connection.commit()

print("Запись удалена!")

# проверка DELETE
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# закрытие соединения
connection.close()

print("Соединение закрыто!")