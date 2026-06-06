from db.connection import get_connection
from db.create_tables import create_main_table
from db.insert_data import seed_demo_products
from db.queries import get_all_records, find_by_filter, get_top_records
from db.reports import get_average_value, get_group_report
from db.formatters import print_table, print_filter, print_top


def menu():
    print("""
==============================
   ДЕТСКИЙ МИР (SQLite)
==============================
1 - Показать все товары
2 - Фильтр по категории
3 - Средняя цена
4 - Отчёт по категориям
5 - Топ-3 товаров
0 - Выход
""")


def main():
    connection = get_connection()

    create_main_table(connection)
    seed_demo_products(connection)

    while True:
        menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            print_table(get_all_records(connection))

        elif choice == "2":
            category = input("Введите категорию: ")
            data = find_by_filter(connection, category)

            print_filter(
                f"Фильтр: {category}",
                [f"{r[1]} — {r[3]} руб." for r in data]
            )

        elif choice == "3":
            print("\nСредняя цена:", round(get_average_value(connection), 2), "руб.")

        elif choice == "4":
            print("\nОТЧЁТ ПО КАТЕГОРИЯМ")
            print("-" * 30)
            for c, n in get_group_report(connection):
                print(f"{c:<15} | {n}")

        elif choice == "5":
            print_top(get_top_records(connection))

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор")

    connection.close()


if __name__ == "__main__":
    main()