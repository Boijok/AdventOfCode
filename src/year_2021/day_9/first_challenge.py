from typing import List, Tuple
from src.year_2021.day_9.input_values import input_values


def solve_day_9_first_challenge() -> None:
    low_point_list = get_low_point_list(input_values)
    current_count = compute_risk_level(input_values, low_point_list)
    print(f"solve_day_9_first_challenge solution is {current_count}")


def compute_risk_level(
    input_grid: List[List[int]], low_point_list: List[Tuple[int, int]]
) -> int:
    current_count = 0
    for low_point in low_point_list:
        current_count = current_count + input_grid[low_point[0]][low_point[1]] + 1
    return current_count


def get_low_point_list(input_grid: List[List[int]]) -> List[Tuple[int, int]]:
    low_point_list: List[Tuple[int, int]] = []
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    for x in range(max_x_value):
        for y in range(max_y_value):
            if is_low_point(input_grid, x, y, max_x_value, max_y_value):
                low_point_list.append((x, y))
    return low_point_list


def is_low_point(
    input_grid: List[List[int]],
    x_coord: int,
    y_coord: int,
    max_x_value: int,
    max_y_value: int,
) -> bool:
    is_low_point_value = True
    current_value = input_grid[x_coord][y_coord]
    if x_coord > 0:
        upper_neighbor = input_grid[x_coord - 1][y_coord]
        is_low_point_value = is_low_point_value & is_lower_than(
            current_value, upper_neighbor
        )
    if x_coord < max_x_value - 1:
        lower_neighbor = input_grid[x_coord + 1][y_coord]
        is_low_point_value = is_low_point_value & is_lower_than(
            current_value, lower_neighbor
        )
    if y_coord > 0:
        left_neighbor = input_grid[x_coord][y_coord - 1]
        is_low_point_value = is_low_point_value & is_lower_than(
            current_value, left_neighbor
        )
    if y_coord < max_y_value - 1:
        right_neighbor = input_grid[x_coord][y_coord + 1]
        is_low_point_value = is_low_point_value & is_lower_than(
            current_value, right_neighbor
        )
    return is_low_point_value


def is_lower_than(value_1: int, value_2: int) -> bool:
    return value_1 < value_2
