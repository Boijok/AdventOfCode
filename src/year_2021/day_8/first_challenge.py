from typing import List
from src.year_2021.day_8.input_values import input_values


def solve_day_8_first_challenge() -> None:
    current_count = 0
    for left_list, right_list in input_values:
        current_count = count_1478(right_list, current_count)
    print(f"solve_day_8_first_challenge solution is {current_count}")


def count_1478(input_list_values: List[str], current_count: int) -> int:
    for value in input_list_values:
        if len(value) in [2, 3, 4, 7]:
            current_count = current_count + 1
    return current_count
