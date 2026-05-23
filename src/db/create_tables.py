import sqlite3

def create_tables():
    connection = sqlite3.connect("shop_lesson02.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT,
        price REAL,
        count INTEGER
    )
    """)

    connection.commit()
    connection.close()
    print("Таблицы успешно созданы!")

if __name__ == "__main__":
    create_tables()