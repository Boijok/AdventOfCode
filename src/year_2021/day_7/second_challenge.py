from typing import List, Dict, Any
from collections import Counter
from src.year_2021.day_7.input_values import input_values


def solve_day_7_second_challenge() -> None:
    input_dict = convert_to_dict(input_values)
    best_position = find_best_position_value(input_dict)
    print(f"solve_day_7_second_challenge solution is {best_position}")


def convert_to_dict(input_list_values: List[int]) -> Dict[int, int]:
    return Counter(input_list_values)


def find_best_position_value(input_dict: Dict[int, int]) -> float:
    dist_dict: Dict[int, int] = {}
    max_value = max(input_dict)
    for key1 in range(max_value + 1):
        dist_dict[key1] = 0
        for key2 in input_dict.keys():
            dist_dict[key1] = dist_dict[key1] + input_dict[key2] * sum_1_to_n(
                abs(key1 - key2)
            )
    dist_dict_getter: Any = dist_dict.get
    best_position = min(dist_dict, key=dist_dict_getter)
    return dist_dict[best_position]


def sum_1_to_n(n: int) -> int:
    return int(n * (n + 1) / 2)
