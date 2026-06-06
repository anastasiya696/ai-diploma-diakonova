def get_all_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


def find_by_filter(connection, category):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
    return cursor.fetchall()


def get_top_records(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT product_name, category, price
        FROM products
        ORDER BY price DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()