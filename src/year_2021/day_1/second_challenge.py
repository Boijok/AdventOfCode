from typing import List
from src.year_2021.day_1.first_challenge import compute_diff_list, keep_one_from_list
from src.year_2021.day_1.input_values import input_values


def solve_day_1_second_challenge() -> None:
    window_values = compute_window_values(input_values)
    window_diff_values = compute_diff_list(window_values)
    filtered_window_diff = keep_one_from_list(window_diff_values)
    print(f"solve_day_1_second_challenge solution is {len(filtered_window_diff)}")


def compute_window_values(input_int_values: List[int]) -> List[int]:
    input_values_1 = input_int_values[:-2]
    input_values_2 = input_int_values[1:-1]
    input_values_3 = input_int_values[2:]
    return [
        value_1 + value_2 + value_3
        for value_1, value_2, value_3 in zip(
            input_values_1, input_values_2, input_values_3
        )
    ]
