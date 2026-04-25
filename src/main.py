from data_utils import find_by_name, filter_by_value, count_items


tasks = [
    {"title": "Сделать отчёт", "status": "в процессе", "priority": 2},
    {"title": "Ответить на письма", "status": "новая", "priority": 3},
    {"title": "Подготовить презентацию", "status": "завершена", "priority": 1},
    {"title": "Созвон с командой", "status": "новая", "priority": 2}
]

print(tasks)

assert len(tasks) == 4
assert tasks[0]["title"] == "Сделать отчёт"