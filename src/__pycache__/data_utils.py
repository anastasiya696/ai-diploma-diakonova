def find_by_name(data, name):
    for item in data:
        if item["name"] == name:
            return item
    return None

def filter_by_value(data, key, value):
    result = []
    for item in data:
        if key in item and item[key] == value:
            result.append(item)
    return result

def count_items(data):
    return len(data)