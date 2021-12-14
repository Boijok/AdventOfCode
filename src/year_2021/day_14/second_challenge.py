from typing import Dict, List
from src.year_2021.day_14.input_values import input_values, input_dict


def solve_day_14_second_challenge() -> None:
    first_value = input_values
    polymer_dict = input_dict

    polymerized_elements = {first_value: 1}
    for i in range(41):
        polymerized_elements = polymerization(polymerized_elements, polymer_dict)

    counter_dict = compute_letter_count(polymerized_elements, first_value)
    max_value = max(counter_dict.values())
    min_value = min(counter_dict.values())

    print(f"solve_day_14_second_challenge solution is {max_value - min_value}")


def polymerization(
    input_polymer_dict: Dict[str, int], polymerization_dict: Dict[str, str]
) -> Dict[str, int]:
    polymerized_dict: Dict[str, int] = {}
    for input_polymer in input_polymer_dict.keys():
        new_polymer_keys = split_string_to_pairs(input_polymer)
        for polymer_key in new_polymer_keys:
            final_polymer_key = polymer_insertion(polymer_key, polymerization_dict)
            if final_polymer_key in polymerized_dict.keys():
                polymerized_dict[final_polymer_key] = (
                    polymerized_dict[final_polymer_key]
                    + input_polymer_dict[input_polymer]
                )
            else:
                polymerized_dict[final_polymer_key] = input_polymer_dict[input_polymer]

    return polymerized_dict


def split_string_to_pairs(input_string: str) -> List[str]:
    polymer_pairs: List[str] = []
    for i in range(0, len(input_string) - 1):
        polymer_pairs.append(input_string[i : i + 2])
    return polymer_pairs


def polymer_insertion(input_value: str, polymer_dict: Dict[str, str]) -> str:
    return input_value[0] + polymer_dict[input_value] + input_value[1]


def compute_letter_count(
    input_polymer_dict: Dict[str, int], first_value: str
) -> Dict[str, int]:
    cleaned_polymer_dict: Dict[str, int] = {}
    for key in input_polymer_dict.keys():
        if key[-1] in cleaned_polymer_dict.keys():
            cleaned_polymer_dict[key[-1]] = (
                cleaned_polymer_dict[key[-1]] + input_polymer_dict[key]
            )
        else:
            cleaned_polymer_dict[key[-1]] = input_polymer_dict[key]

    letter_count: Dict[str, int] = {}
    for letter_tuple in cleaned_polymer_dict.keys():
        for letter in letter_tuple:
            if letter in letter_count.keys():
                letter_count[letter] = (
                    letter_count[letter] + cleaned_polymer_dict[letter_tuple]
                )
            else:
                letter_count[letter] = cleaned_polymer_dict[letter_tuple]

    last_elem_letter = first_value[1]
    letter_count[last_elem_letter] = letter_count[last_elem_letter] + 1

    return letter_count
