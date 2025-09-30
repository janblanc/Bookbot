import sys
from stats import num_of_words
from stats import num_of_characters
from stats import separate_dict

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = None
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    reading = get_book_text(book_path)
    num_words = num_of_words(reading)
    num_characters = num_of_characters(reading)
    new_dict = separate_dict(num_characters)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for ch in new_dict:
        if ch["char"].isalpha():
            print(f"{ch['char']}: {ch['num']}")

    print("============= END ===============")

main()