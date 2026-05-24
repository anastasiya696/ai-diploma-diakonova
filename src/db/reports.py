def get_all_categories(cursor):
    cursor.execute("SELECT * FROM categories")
    return cursor.fetchall()


def get_all_products(cursor):
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


def get_products_by_category(cursor, category_id):
    cursor.execute("""
    SELECT * FROM products
    WHERE category_id = ?
    """, (category_id,))
    return cursor.fetchall()