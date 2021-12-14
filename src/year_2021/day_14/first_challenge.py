from collections import Counter
from typing import Dict, List

from src.year_2021.day_14.input_values import (
    input_values,
    input_dict,
)


def solve_day_14_first_challenge() -> None:
    first_value = input_values
    polymer_dict = input_dict

    polymerized = first_value
    for i in range(10):
        polymerized = polymerization(polymerized, polymer_dict)

    counter_dict = Counter(polymerized)
    max_value = max(counter_dict.values())
    min_value = min(counter_dict.values())

    print(f"solve_day_14_first_challenge solution is {max_value - min_value}")


def polymerization(input_string: str, polymer_dict: Dict[str, str]) -> str:
    polymer_pairs = split_string_to_pairs(input_string)
    polymer_string = ""
    for polymer_pair in polymer_pairs:
        polymer_string = polymer_string + polymer_insertion(polymer_pair, polymer_dict)
    return polymer_string + input_string[-1]


def split_string_to_pairs(input_string: str) -> List[str]:
    polymer_pairs: List[str] = []
    for i in range(0, len(input_string) - 1):
        polymer_pairs.append(input_string[i : i + 2])
    return polymer_pairs


def polymer_insertion(input_value: str, polymer_dict: Dict[str, str]) -> str:
    return input_value[0] + polymer_dict[input_value]
