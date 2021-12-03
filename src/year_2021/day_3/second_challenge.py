import math
from typing import List

from src.year_2021.day_3.first_challenge import binary_to_integer
from src.year_2021.day_3.input_values import input_list


def solve_day_3_second_challenge() -> None:
    oxygen_generator_rating = compute_oxygen_generator_rating(input_list)
    co2_scrubber_rating = compute_co2_scrubber_rating(input_list)
    life_support_rating = compute_life_support_rating(
        oxygen_generator_rating, co2_scrubber_rating
    )
    print(f"solve_day_3_first_challenge solution is {life_support_rating}")


def compute_oxygen_generator_rating(input_binary_str_list: List[str]) -> int:
    current_input_binary_str_list = input_binary_str_list
    for position_n in range(0, len(input_binary_str_list[0]) - 1):
        if len(current_input_binary_str_list) == 1:
            continue
        else:
            bit_in_position_n_list = keep_only_bit_in_position_n_of_each_binary_str(
                current_input_binary_str_list, position_n
            )
            bit_criteria = find_most_common(bit_in_position_n_list)
            current_input_binary_str_list = keep_number_matching_bit_criteria(
                current_input_binary_str_list, position_n, bit_criteria
            )
    return binary_to_integer(current_input_binary_str_list[0])


def compute_co2_scrubber_rating(input_binary_str_list: List[str]) -> int:
    current_input_binary_str_list = input_binary_str_list
    for position_n in range(0, len(input_binary_str_list[0]) - 1):
        if len(current_input_binary_str_list) == 1:
            continue
        else:
            bit_in_position_n_list = keep_only_bit_in_position_n_of_each_binary_str(
                current_input_binary_str_list, position_n
            )
            bit_criteria = find_less_common(bit_in_position_n_list)
            current_input_binary_str_list = keep_number_matching_bit_criteria(
                current_input_binary_str_list, position_n, bit_criteria
            )
    return binary_to_integer(current_input_binary_str_list[0])


def compute_life_support_rating(
    oxygen_generator_rating: int, co2_scrubber_rating: int
) -> int:
    return oxygen_generator_rating * co2_scrubber_rating


def keep_only_bit_in_position_n_of_each_binary_str(
    input_binary_str_list: List[str], position_n: int
) -> List[int]:
    return [int(binary_str[position_n]) for binary_str in input_binary_str_list]


def find_most_common(input_int_list: List[int]) -> str:
    half_value = find_half_value(input_int_list)
    number_of_ones = sum(input_int_list)
    number_of_zeros = len(input_int_list) - number_of_ones
    if number_of_ones == number_of_zeros:
        return "1"
    else:
        return "1" if (number_of_ones > half_value) else "0"


def find_less_common(input_int_list: List[int]) -> str:
    most_common = find_most_common(input_int_list)
    return "1" if (most_common == "0") else "0"


def find_half_value(input_int_list: List[int]) -> int:
    total_number_of_values = len(input_int_list)
    return math.floor(total_number_of_values / 2)


def keep_number_matching_bit_criteria(
    input_binary_str_list: List[str], position_n: int, bit_criteria: str
) -> List[str]:
    return [
        binary_str
        for binary_str in input_binary_str_list
        if binary_str[position_n] == bit_criteria
    ]
