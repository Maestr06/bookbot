def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(words):
    characters = {}

    for word in words:
        for c in word.lower():
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1         
    return characters