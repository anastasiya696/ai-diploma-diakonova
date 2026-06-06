def get_average_value(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(price) FROM products")
    return cursor.fetchone()[0]


def get_group_report(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category, COUNT(*)
        FROM products
        GROUP BY category
    """)
    return cursor.fetchall()