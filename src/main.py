import sqlite3
import queries as q

# подключение к БД
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

print("БД подключена")

# ---------- СОЗДАНИЕ ТАБЛИЦ ----------
cursor.execute(q.CREATE_STUDENTS_TABLE)
cursor.execute(q.CREATE_GRADES_TABLE)
connection.commit()

print("Таблицы созданы")

# ---------- ДОБАВЛЕНИЕ ДАННЫХ ----------
students = [
    ("Алина Иванова", "10A", "alina@mail.com", 16, 4.6),
    ("Максим Петров", "11B", "maxim@mail.com", 17, 4.2)
]

grades = [
    ("Math", "Алина Иванова", 5, "exam", 1.0),
    ("Physics", "Максим Петров", 4, "test", 0.5)
]

cursor.executemany(q.INSERT_STUDENT, students)
cursor.executemany(q.INSERT_GRADE, grades)

connection.commit()

print("Данные добавлены")

# ---------- SELECT ----------
cursor.execute(q.SELECT_STUDENTS)
students_rows = cursor.fetchall()

print("Students:")
for row in students_rows:
    print(row)

cursor.execute(q.SELECT_GRADES)
grades_rows = cursor.fetchall()

print("Grades:")
for row in grades_rows:
    print(row)

# ---------- UPDATE ----------
cursor.execute(q.UPDATE_STUDENT_AGE, (18, "Алина Иванова"))
connection.commit()

print("UPDATE выполнен")

# ---------- DELETE ----------
cursor.execute("DELETE FROM grades WHERE score = 4")
connection.commit()

print("DELETE выполнен")

# ---------- ПРОВЕРКИ ----------
cursor.execute(q.SELECT_STUDENTS)
assert len(cursor.fetchall()) >= 2

cursor.execute(q.SELECT_GRADES)
assert len(cursor.fetchall()) >= 1

print("Все проверки пройдены")

# ---------- ЗАКРЫТИЕ ----------
connection.close()

print("Соединение закрыто")
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import queries as q