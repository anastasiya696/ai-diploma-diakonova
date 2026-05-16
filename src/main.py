from text_utils import normalize_text, word_count, contains_word
from data_utils import count_items, find_by_name, filter_by_value
from file_utils import save_text, load_text
from csv_utils import save_csv, load_csv
from json_utils import save_json, load_json


def show_menu():
    print("\n===== УЧЕБНЫЙ ПРОЕКТ =====")
    print("1 - Обработать текст")
    print("2 - Работа со студентами")
    print("3 - Работа с файлами")
    print("0 - Выход")
    print("==========================\n")


def text_mode():
    text = "   Мой учебный проект по Python   "

    clean = normalize_text(text)
    words = word_count(clean)
    has_python = contains_word(clean, "python")

    print("\n📄 ТЕКСТ:")
    print("Очищенный:", clean)
    print("Слов:", words)
    print("Есть python:", has_python)


def student_mode():
    students = [
        {"name": "Анна", "city": "Москва"},
        {"name": "Иван", "city": "Казань"},
        {"name": "Ольга", "city": "Москва"}
    ]

    print("\n👩‍🎓 СТУДЕНТЫ:")

    print("Найти Иван:", find_by_name(students, "Иван"))
    print("Из Москвы:", filter_by_value(students, "city", "Москва"))
    print("Всего:", count_items(students))


def file_mode():
    text = "пример сохранения данных"

    save_text("note.txt", text)
    loaded = load_text("note.txt")

    print("\n📁 ФАЙЛ:")
    print("Сохранено и прочитано:", loaded)

    # CSV
    rows = [
        ["name", "age"],
        ["Anna", 20],
        ["Ivan", 21]
    ]

    save_csv("data.csv", rows)
    csv_data = load_csv("data.csv")

    print("\n📊 CSV:")
    print(csv_data)

    # JSON
    data = {
        "project": "lesson_project",
        "status": "done"
    }

    save_json("data.json", data)
    json_data = load_json("data.json")

    print("\n🧾 JSON:")
    print(json_data)


def main():
    while True:
        show_menu()
        choice = input("👉 Введите действие: ").strip()

        if choice == "1":
            text_mode()

        elif choice == "2":
            student_mode()

        elif choice == "3":
            file_mode()

        elif choice == "0":
            print("👋 Выход из программы")
            break

        else:
            print("❌ Неверная команда")


if __name__ == "__main__":
    main()