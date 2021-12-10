import math
from typing import List
from src.year_2021.day_10.first_challenge import is_corrupted
from src.year_2021.day_10.input_values import input_values


def solve_day_10_second_challenge() -> None:
    invalid_string = [string for string in input_values if not is_corrupted(string)]
    stacks_to_complete = [get_stack_to_complete(string) for string in invalid_string]
    complete_sequence = [complete_string(string) for string in stacks_to_complete]
    current_counts: List[int] = []
    for sequence in complete_sequence:
        current_counts.append(decode(sequence))
    sorted_current_counts = sorted(current_counts)
    current_count = sorted_current_counts[math.floor(len(sorted_current_counts) / 2)]
    print(f"solve_day_10_second_challenge solution is {current_count}")


def get_stack_to_complete(input_string: str) -> str:
    dict_ref = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    for character in input_string:
        if character in dict_ref.keys():
            stack.append(character)
        else:
            if not stack:
                print("Error this line is corrupter")
            pop_character = stack.pop()
            if character != dict_ref[pop_character]:
                print("Error this line is corrupter")
    return "".join(stack)


def complete_string(input_string: str) -> str:
    dict_ref = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    for character in input_string:
        stack.append(dict_ref[character])

    return "".join(reversed(stack))


def decode(sequence: str) -> int:
    dict_ref = {")": 1, "]": 2, "}": 3, ">": 4}
    current_count = 0
    for character in sequence:
        current_count = current_count * 5 + dict_ref[character]
    return current_count
