def get_words_count(book_content):
    words_list = book_content.split()
    words_number = len(words_list)

    return words_number


def get_char_dict(text):
    text_to_lower = text.lower()
    char_dict = {}

    for char in text_to_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def sort_on(value: tuple[str, int]):
    return value[1]


def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    holding_list = []
    for char in char_dict:
        total = char_dict[char]
        holding_list.append((char, total))
    sorted_list = sorted(holding_list, reverse=True, key=sort_on)
    return sorted_list
