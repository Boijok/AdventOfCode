import math
from typing import List, Any
from numpy import sum as np_sum
from numpy import array, ndarray
from src.year_2021.day_3.input_values import input_list


def solve_day_3_first_challenge() -> None:
    epsilon_rate = compute_epsilon_rate(input_list)
    gamma_rate = compute_gama_rate(input_list)
    power_consumption = compute_power_consumption(gamma_rate, epsilon_rate)
    print(f"solve_day_3_first_challenge solution is {power_consumption}")


def compute_gama_rate(input_list_values: List[str]) -> int:
    sum_array = compute_sum_array(input_list_values)
    half_value = find_half_value(input_list_values)
    binary_gamma_rate = compute_binary_gamma_rate(sum_array, half_value)
    return binary_to_integer(binary_gamma_rate)


def compute_epsilon_rate(input_list_values: List[str]) -> int:
    sum_array = compute_sum_array(input_list_values)
    half_value = find_half_value(input_list_values)
    binary_epsilon_rate = compute_binary_epsilon_rate(sum_array, half_value)
    return binary_to_integer(binary_epsilon_rate)


def compute_sum_array(input_list_values: List[str]) -> ndarray[Any, Any]:
    matrix_input_values = transform_input_list_to_matrix(input_list_values)
    array_matrix_input_values = transform_matrix_to_numpy_array(matrix_input_values)
    return count_number_of_ones_per_column(array_matrix_input_values)


def find_half_value(input_int_list: List[str]) -> int:
    total_number_of_values = len(input_int_list)
    return math.floor(total_number_of_values / 2)


def transform_input_list_to_matrix(input_list_values: List[str]) -> List[List[int]]:
    return [[int(char) for char in input_value] for input_value in input_list_values]


def transform_matrix_to_numpy_array(
    matrix_input_values: List[List[int]],
) -> ndarray[Any, Any]:
    return array(matrix_input_values)


def count_number_of_ones_per_column(
    array_matrix_input_values: ndarray[Any, Any]
) -> ndarray[Any, Any]:
    return np_sum(array_matrix_input_values, 0)


def compute_binary_gamma_rate(sum_array: ndarray[Any, Any], half_value: int) -> str:
    gamma_rate_list = ["1" if (sum_col > half_value) else "0" for sum_col in sum_array]
    return "".join(gamma_rate_list)


def compute_binary_epsilon_rate(sum_array: ndarray[Any, Any], half_value: int) -> str:
    epsilon_rate_list = [
        "1" if (sum_col < half_value) else "0" for sum_col in sum_array
    ]
    return "".join(epsilon_rate_list)


def binary_to_integer(binary_string: str) -> int:
    return int(binary_string, 2)


def compute_power_consumption(gamma_rate_value: int, epsilon_rate_value: int) -> int:
    return gamma_rate_value * epsilon_rate_value
