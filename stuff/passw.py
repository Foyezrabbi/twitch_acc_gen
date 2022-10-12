import random
import array


def pass_gen():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    locase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    upcase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = digits + upcase_characters + locase_characters + symbols

    rand_digit = random.choice(digits)
    rand_upper = random.choice(upcase_characters)
    rand_lower = random.choice(locase_characters)
    rand_symbol = random.choice(symbols)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(12 - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    return password
