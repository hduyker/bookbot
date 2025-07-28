def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_item = {}
        char_item["char"] = char
        char_item["num"] = count
        char_list.append(char_item)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

