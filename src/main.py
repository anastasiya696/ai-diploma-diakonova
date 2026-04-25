from data_utils import find_by_name, filter_by_value, count_items

students = [
    {"name": "Анна", "city": "Казань", "age": 20},
    {"name": "Иван", "city": "Москва", "age": 21},
    {"name": "Ольга", "city": "Казань", "age": 19},
    {"name": "Павел", "city": "Уфа", "age": 22}
]

print(find_by_name(students, "Иван"))
print(filter_by_value(students, "city", "Казань"))
print(count_items(students))