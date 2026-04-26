def normalize_text(text):
    return text.strip().lower()
 
def word_count(text):
    return len(text.split())
 
def contains_word(text, word):
    return word.lower() in text.lower()
 
text = "  Hello Python World  "
 
print(normalize_text(text))
print(word_count(text))
print(contains_word(text, "python"))