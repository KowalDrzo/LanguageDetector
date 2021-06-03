import numpy as np

def parse_file(file_name: str) -> np.array:

    file = open(file_name, "r")
    temp_string = file.read()

    return parse_string(temp_string)

def parse_string(string_to_parse: str) -> np.array:

    char_counter = 0
    tab_lang = []

    for i in range(65, 91):

        letter_counter = 0
        for char in string_to_parse:

            if ord(char) == i or ord(char) == i + 32:
                char_counter += 1
                letter_counter += 1
        
        tab_lang.append(letter_counter)

    final_list = []

    for element in tab_lang:
        final_list.append(element/char_counter)

    return np.array(final_list)