# bookbot code written by Olamide Koukpoliyi via boot.dev

import sys

from stats import chars_dict_to_sorted_list, get_char_dict, get_words_count


def main():
    check_argument()
    book_path = sys.argv[1]
    book_texts = get_book_text(book_path)
    word_count = get_words_count(book_texts)
    char_stats = get_char_dict(book_texts)
    sorted_char_stats = chars_dict_to_sorted_list(char_stats)
    print_report(book_path, word_count, sorted_char_stats)


def check_argument():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def print_report(book_path, word_count, sorted_char_stats) -> None:
    print("============== BOOKBOT ==============")
    print(f"Analyzing book found at {book_path}...")
    print("------------- Word Count -------------")
    print(f"Found {word_count} total words")
    print("---------- Character Count ----------")
    for key, value in sorted_char_stats:
        if key.isalpha():
            print(f"{key}: {value}")
    print("=============== END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
