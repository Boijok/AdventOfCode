from typing import Dict, List

from src.year_2021.day_8.input_values import input_values


def solve_day_8_second_challenge() -> None:
    current_count = 0
    for left_list, right_list in input_values:
        decoder = decode_left_list(left_list)
        current_count = current_count + decode_right_list(right_list, decoder)
    print(f"solve_day_8_second_challenge solution is {current_count}")


def decode_left_list(input_list_values: List[str]) -> Dict[str, int]:
    decoder = decode_1478(input_list_values)
    final_decoder = decode_other(input_list_values, decoder)
    return reverse_key_value_in_dict(final_decoder)


def decode_right_list(input_list_values: List[str], decoder: Dict[str, int]) -> int:
    decoded_value = ""
    for elem in input_list_values:
        sorted_elem = sort_string_char(elem)
        decoded_value = decoded_value + str(decoder[sorted_elem])
    return int(decoded_value)


def decode_1478(input_list_values: List[str]) -> Dict[int, str]:
    decoder: Dict[int, str] = {}
    for value in input_list_values:
        sorted_value = sort_string_char(value)
        if len(sorted_value) == 2:
            decoder[1] = sorted_value
        if len(sorted_value) == 4:
            decoder[4] = sorted_value
        if len(sorted_value) == 3:
            decoder[7] = sorted_value
        if len(sorted_value) == 7:
            decoder[8] = sorted_value
    return decoder


def decode_other(
    input_list_values: List[str], decoder: Dict[int, str]
) -> Dict[int, str]:
    for value in input_list_values:
        sorted_value = sort_string_char(value)
        if len(sorted_value) == 5:
            number_of_char_in_common_with_1 = compute_number_of_char_in_common(
                decoder[1], sorted_value
            )
            number_of_char_in_common_with_4 = compute_number_of_char_in_common(
                decoder[4], sorted_value
            )
            if number_of_char_in_common_with_1 == 2:
                decoder[3] = sorted_value
            elif number_of_char_in_common_with_4 == 2:
                decoder[2] = sorted_value
            elif number_of_char_in_common_with_4 == 3:
                decoder[5] = sorted_value
            else:
                print("warning, should not come here")
        if len(sorted_value) == 6:
            number_of_char_in_common_with_1 = compute_number_of_char_in_common(
                decoder[1], sorted_value
            )
            number_of_char_in_common_with_4 = compute_number_of_char_in_common(
                decoder[4], sorted_value
            )
            if number_of_char_in_common_with_1 == 1:
                decoder[6] = sorted_value
            elif number_of_char_in_common_with_4 == 4:
                decoder[9] = sorted_value
            elif number_of_char_in_common_with_4 == 3:
                decoder[0] = sorted_value
            else:
                print("warning, should not come here")
    return decoder


def compute_number_of_char_in_common(
    char_str_to_search: str, str_to_inspect: str
) -> int:
    number_of_char_in_common = 0
    for char in char_str_to_search:
        if char in str_to_inspect:
            number_of_char_in_common = number_of_char_in_common + 1
    return number_of_char_in_common


def reverse_key_value_in_dict(input_dict: Dict[int, str]) -> Dict[str, int]:
    return {value: key for key, value in input_dict.items()}


def sort_string_char(input_string: str) -> str:
    char_list = [char for char in input_string]
    sorted_string = "".join(sorted(char_list))
    return sorted_string
