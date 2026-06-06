def print_table(products):
    print("\nID | Название | Категория | Цена | Остаток | Возраст")
    print("-" * 70)

    for p in products:
        print(f"{p[0]:<2} | {p[1]:<20} | {p[2]:<15} | {p[3]:>7} | {p[4]:>7} | {p[5]:>3}")


def print_filter(title, items):
    print(f"\n{title}")
    print("-" * len(title))

    for item in items:
        print(item)


def print_top(products):
    print("\nТОП ТОВАРОВ")
    print("-" * 40)

    for name, category, price in products:
        print(f"{name} ({category}) — {price} руб.")