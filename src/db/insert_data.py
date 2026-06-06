def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products")
    connection.commit()


def add_record(connection, product_name, category, price, stock_quantity, age_group):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (
            product_name,
            category,
            price,
            stock_quantity,
            age_group
        )
        VALUES (?, ?, ?, ?, ?)
    """, (product_name, category, price, stock_quantity, age_group))

    connection.commit()


def seed_demo_products(connection):
    clear_table(connection)

    add_record(connection, "LEGO City", "Конструкторы", 2499.99, 15, 6)
    add_record(connection, "Barbie", "Куклы", 1299.99, 20, 3)
    add_record(connection, "Медведь", "Мягкие игрушки", 899.99, 30, 1)
    add_record(connection, "Самокат", "Транспорт", 3499.99, 8, 5)
    add_record(connection, "Монополия", "Игры", 1999.99, 10, 8)