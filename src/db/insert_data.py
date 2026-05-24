import sqlite3

# подключение к базе данных
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# список данных
students_data = [
    ("Алина", 16, "10A"),
    ("Максим", 17, "11B"),
    ("София", 15, "9C")
]

# добавление данных
cursor.executemany(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    students_data
)

# сохранение изменений
connection.commit()

print("Данные успешно добавлены!")

# закрытие соединения
connection.close()