def main():
    path = 'books/frankenstein.txt'
    # text = get_text(path)
    # count = get_word_count(text)
    # char_count = get_char_dict(text.split())
    # list_chars = [{'char': k, 'count': v} for k, v in char_count.items()]
    # sorted_chars = list_chars.sort(reverse=True, key=sort_on)
    get_report(path)

def get_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
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

def sort_on(item):
    return item['count']

def get_report(path):
    text = get_text(path)
    char_count = get_char_dict(text.split())
    list_chars = [{'char': k, 'count': v} for k, v in char_count.items()]
    list_chars.sort(reverse=True, key=sort_on)
    # print(list_chars)
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(text)} words found in the document\n")
    for item in list_chars:
        if item['char'].isalpha():
            print(f"The {item['char']} character was fount {item['count']} times")
    print(f"--- End report ---")

if __name__ == '__main__':
    main()