def save_report(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)