user_input = ["first", "second", "first", "third", "second"]
found_words = []
for word in user_input:
    if word not in found_words:
        print(word)
        found_words.append(word)
