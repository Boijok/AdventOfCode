from src.year_2021.day_10.input_values import input_values


def solve_day_10_first_challenge() -> None:
    invalid_string = [string for string in input_values if is_corrupted(string)]
    bad_chars = [get_first_bad_char(string) for string in invalid_string]
    current_count = 0
    for char in bad_chars:
        current_count = current_count + decode(char)
    print(f"solve_day_10_first_challenge solution is {current_count}")


def is_corrupted(input_string: str) -> bool:
    dict_ref = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    for character in input_string:
        if character in dict_ref.keys():
            stack.append(character)
        else:
            if not stack:
                return True
            pop_character = stack.pop()
            if character != dict_ref[pop_character]:
                return True
    return False


def get_first_bad_char(input_string: str) -> str:
    dict_ref = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    last_character = ""
    for character in input_string:
        if character in dict_ref.keys():
            stack.append(character)
        else:
            if not stack:
                return character
            pop_character = stack.pop()
            if character != dict_ref[pop_character]:
                return character
        last_character = character
    return last_character


def decode(character: str) -> int:
    dict_ref = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return dict_ref[character]
