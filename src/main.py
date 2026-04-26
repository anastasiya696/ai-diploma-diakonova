from json_utils import save_json, load_json, dict_to_json_text

config = {
    "model": "demo",
    "temperature": 0.7,
    "max_tokens": 200
}

save_json("config.json", config)

print(load_json("config.json"))
print(dict_to_json_text(config))