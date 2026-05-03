from text_utils import normalize_text
from data_utils import count_items
from file_utils import save_text, load_text
from json_utils import save_json, load_json


def show_menu():
    print("\n===== МОЙ ПРОЕКТ =====")
    print("1 - Обработать текст")
    print("2 - Работа со списком задач")
    print("3 - Сохранить данные в файл")
    print("4 - Сохранить JSON")
    print("0 - Выход")
    print("======================\n")


def run_choice(choice):
    if choice == "1":
        text = "   Мой учебный проект по Python   "
        result = normalize_text(text)
        print("📄 Результат:", result)

    elif choice == "2":
        tasks = [
            "изучить Python",
            "сделать проект",
            "научиться работать с Git",
            "собрать меню"
        ]
        print("📊 Количество задач:", count_items(tasks))

    elif choice == "3":
        text = "пример сохранённого текста"
        save_text("note.txt", text)
        print("💾 Текст сохранён в файл")

        loaded = load_text("note.txt")
        print("📂 Прочитано из файла:", loaded)

    elif choice == "4":
        data = {
            "project": "Python Menu App",
            "status": "in progress",
            "tasks": 4
        }
        save_json("data.json", data)
        print("💾 JSON сохранён")

        print("📂 JSON:", load_json("data.json"))

    elif choice == "0":
        print("👋 Завершение программы")

    else:
        print("❌ Неизвестная команда")