import sys
from stats import get_word_count, get_char_dict

print(len(sys.argv))

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    # text = get_text(path)
    # # count = get_word_count(text)
    # print(get_word_count(text))

    # print(get_char_dict(text.split()))
    # list_chars = [{'char': k, 'count': v} for k, v in char_count.items()]
    # sorted_chars = list_chars.sort(reverse=True, key=sort_on)
    get_report(path)

def get_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()



def sort_on(item):
    return item['count']

def get_report(path):
    text = get_text(path)
    char_count = get_char_dict(text.split())
    list_chars = [{'char': k, 'count': v} for k, v in char_count.items()]
    list_chars.sort(reverse=True, key=sort_on)
    # print(list_chars)
    print(f"--- Begin report of {path} ---")
    print(f"Found {get_word_count(text)} total words\n")
    print(f"--- Character count {path} ---")
    for item in list_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print(f"--- END ---")

if __name__ == '__main__':
    main()