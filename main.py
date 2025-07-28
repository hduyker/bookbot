import sys
from stats import count_words, count_chars, sort_chars

def get_book_content(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def analyze_book(path, book_text):
    num_words = count_words(book_text)
    char_counts = count_chars(book_text)
    chars_sorted = sort_chars(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for counter in chars_sorted:
        if counter["char"].isalpha():
            print(f"{counter["char"]}: {counter["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    path = sys.argv[1]
    content = get_book_content(path)
    analyze_book(path, content)

main()
