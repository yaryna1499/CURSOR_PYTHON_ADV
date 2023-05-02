import re



input_text = str(input("Type the text:"))
input_word = str(input("Type the word:"))


def counter(word, text):
    words = re.findall(fr"\b{word}\b", text, flags=re.IGNORECASE)
    amount = len(words)
    new_text = re.sub(word, word.upper(), text, flags=re.IGNORECASE)

    return (amount, new_text)

print(counter(input_word, input_text))