from typing import List

from src.year_2021.day_15.first_challenge import (
    merge_best_path,
    get_best_path_to_diag,
    rotate_grid_90,
)
from src.year_2021.day_15.input_values import input_values


def solve_day_15_second_challenge() -> None:

    input_grid = expand_grid_rows(input_values)
    rotated_180_input_grid: List[List[int]] = rotate_grid_90(rotate_grid_90(input_grid))

    best_path_list_forward: List[int] = get_best_path_to_diag(input_grid)
    best_path_list_backward: List[int] = get_best_path_to_diag(rotated_180_input_grid)

    best_path_value = merge_best_path(
        input_grid, best_path_list_forward, best_path_list_backward
    )

    print(f"solve_day_15_second_challenge solution is {best_path_value}")


def create_full_grid(input_grid: List[List[int]]) -> List[List[int]]:
    return input_grid


def create_next_grid(input_grid: List[List[int]]) -> List[List[int]]:
    next_grid: List[List[int]] = []
    for line in input_grid:
        new_row: List[int] = []
        for elem in line:
            new_elem = 1 if elem == 9 else elem + 1
            new_row.append(new_elem)
        next_grid.append(new_row)
    return next_grid


def expand_grid_rows(
    input_grid: List[List[int]], expansion_time: int = 5
) -> List[List[int]]:
    full_grid_rows: List[List[int]] = []
    current_first_grid = input_grid
    for i in range(expansion_time):
        new_grid_rows = expand_grid_line(current_first_grid)
        full_grid_rows = full_grid_rows + new_grid_rows
        current_first_grid = create_next_grid(current_first_grid)

    return full_grid_rows


def expand_grid_line(
    input_grid: List[List[int]], expansion_time: int = 5
) -> List[List[int]]:
    new_grid = input_grid
    next_grid = input_grid
    for i in range(expansion_time - 1):
        next_grid = create_next_grid(next_grid)
        new_grid = concat_grids(new_grid, next_grid)

    return new_grid


def concat_grids(
    input_grid: List[List[int]], grid_to_add: List[List[int]]
) -> List[List[int]]:
    full_grid_line: List[List[int]] = []
    for j in range(len(input_grid)):
        new_line = input_grid[j] + grid_to_add[j]
        full_grid_line.append(new_line)
    return full_grid_line
