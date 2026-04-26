def save_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + text)

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)