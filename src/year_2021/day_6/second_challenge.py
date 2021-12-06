from typing import List, Dict
from collections import Counter
from src.year_2021.day_6.input_values import input_values


def solve_day_6_second_challenge() -> None:
    input_dict = convert_to_dict(input_values)
    full_dict = complete_dict(input_dict)
    for day in range(256):
        full_dict = iterate_one_day(full_dict)
    number_fish = count_fish(full_dict)
    print(f"solve_day_6_second_challenge solution is {number_fish}")


def convert_to_dict(input_list_values: List[int]) -> Dict[int, int]:
    return Counter(input_list_values)


def complete_dict(input_dict: Dict[int, int]) -> Dict[int, int]:
    for key in range(0, 9):
        if key not in input_dict.keys():
            input_dict[key] = 0
    return input_dict


def iterate_one_day(full_dict: Dict[int, int]) -> Dict[int, int]:
    new_dict: Dict[int, int] = {}
    for key in range(0, 8):
        new_dict[key] = full_dict[key + 1]
    new_dict[8] = full_dict[0]
    new_dict[6] = new_dict[6] + full_dict[0]
    return new_dict


def count_fish(full_dict: Dict[int, int]) -> int:
    number_fish = 0
    for key in full_dict.keys():
        number_fish = number_fish + full_dict[key]
    return number_fish
