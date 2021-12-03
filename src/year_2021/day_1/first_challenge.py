from typing import List
from src.year_2021.day_1.input_values import input_values


def solve_day_1_first_challenge() -> None:
    diff_values = compute_diff_list(input_values)
    filtered_diff = keep_one_from_list(diff_values)
    print(f"solve_day_1_first_challenge solution is {len(filtered_diff)}")


def compute_diff_list(input_int_values: List[int]) -> List[int]:
    input_values_head = input_int_values[:-1]
    input_values_tail = input_int_values[1:]
    return [head - tail for head, tail in zip(input_values_head, input_values_tail)]


def keep_one_from_list(diff_values: List[int]) -> List[int]:
    return [1 for iteration in diff_values if iteration < 0]
