from text_utils import normalize_text
from data_utils import count_items
from file_utils import save_text, load_text
from json_utils import save_json, load_json
 
text = "   Мой первый проект на Python   "
tasks = ["изучить строки", "изучить файлы", "изучить json"]
 
clean_text = normalize_text(text)
task_count = count_items(tasks)
 
save_text("project_note.txt", clean_text)
loaded_text = load_text("project_note.txt")
 
config = {
    "project_name": "my_first_project",
    "task_count": task_count
}
 
save_json("project_config.json", config)
loaded_config = load_json("project_config.json")
 
print("Очищенный текст:", clean_text)
print("Прочитанный текст из файла:", loaded_text)
print("Количество задач:", task_count)
print("Загруженный JSON:", loaded_config)
