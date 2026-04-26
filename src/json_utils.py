import json

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def dict_to_json_text(data):
    return json.dumps(data, ensure_ascii=False, indent=4)