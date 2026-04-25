from csv_utils import save_csv, load_csv, count_csv_rows, sum_column

products = [
    ["title", "price", "count"],
    ["Ноутбук", 50000, 2],
    ["Мышь", 1500, 5]
]

save_csv("products.csv", products)

print(load_csv("products.csv"))
print("Количество строк:", count_csv_rows("products.csv"))
print("Сумма столбца price:", sum_column("products.csv", 1))