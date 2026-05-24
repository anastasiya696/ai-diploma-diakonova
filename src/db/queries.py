CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    class_name TEXT,
    email TEXT,
    age INTEGER,
    average_grade REAL
)
"""

CREATE_GRADES_TABLE = """
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    student_name TEXT,
    score INTEGER,
    exam_type TEXT,
    weight REAL
)
"""

# вставка данных students
INSERT_STUDENT = """
INSERT INTO students (full_name, class_name, email, age, average_grade)
VALUES (?, ?, ?, ?, ?)
"""

# вставка данных grades
INSERT_GRADE = """
INSERT INTO grades (subject, student_name, score, exam_type, weight)
VALUES (?, ?, ?, ?, ?)
"""

# select
SELECT_STUDENTS = "SELECT * FROM students"
SELECT_GRADES = "SELECT * FROM grades"

# delete
DELETE_STUDENTS = "DELETE FROM students"
DELETE_GRADES = "DELETE FROM grades"

# update
UPDATE_STUDENT_AGE = """
UPDATE students
SET age = ?
WHERE full_name = ?
"""