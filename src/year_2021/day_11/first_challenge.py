import copy
from typing import List, Tuple

from src.year_2021.day_11.input_values import (
    input_values,
)
from src.year_2021.day_9.second_challenge import pretty_print


def solve_day_11_first_challenge() -> None:
    current_input_values = input_values
    current_count = 0
    for i in range(501):
        increased_input_values = increase_every_one(current_input_values)
        flashed_input_values = increased_input_values
        for j in range(20):
            flashed_input_values = flash(flashed_input_values)
        current_count = current_count + count_flash(flashed_input_values)
        current_input_values = reset_every_one(flashed_input_values)
    pretty_print(current_input_values)

    print(f"solve_day_11_first_challenge solution is {current_count}")


def increase_every_one(input_grid: List[List[int]]) -> List[List[int]]:
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    for x in range(max_x_value):
        for y in range(max_y_value):
            input_grid[x][y] = input_grid[x][y] + 1
    return input_grid


def flash(input_grid: List[List[int]]) -> List[List[int]]:
    new_grid = copy.deepcopy(input_grid)
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    for x in range(max_x_value):
        for y in range(max_y_value):
            if input_grid[x][y] == 10:
                new_grid[x][y] = new_grid[x][y] + 1
                new_grid = increase_neighbors(new_grid, (x, y))
    return new_grid


def increase_neighbors(
    input_grid: List[List[int]], point: Tuple[int, int]
) -> List[List[int]]:
    neighbors = get_neighbors(input_grid, point)
    for neighbor in neighbors:
        if input_grid[neighbor[0]][neighbor[1]] != 10:
            input_grid[neighbor[0]][neighbor[1]] = (
                input_grid[neighbor[0]][neighbor[1]] + 1
            )
    return input_grid


def get_neighbors(
    input_grid: List[List[int]], point: Tuple[int, int]
) -> List[Tuple[int, int]]:
    x_coord = point[0]
    y_coord = point[1]
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    neighbors: List[Tuple[int, int]] = []
    has_upper_neighbor = x_coord > 0
    has_lower_neighbor = x_coord < max_x_value - 1
    has_left_neighbor = y_coord > 0
    has_right_neighbor = y_coord < max_y_value - 1
    if has_upper_neighbor:
        upper_neighbor = (x_coord - 1, y_coord)
        neighbors.append(upper_neighbor)
        if has_left_neighbor:
            upper_left_neighbor = (x_coord - 1, y_coord - 1)
            neighbors.append(upper_left_neighbor)
        if has_right_neighbor:
            upper_right_neighbor = (x_coord - 1, y_coord + 1)
            neighbors.append(upper_right_neighbor)
    if has_lower_neighbor:
        lower_neighbor = (x_coord + 1, y_coord)
        neighbors.append(lower_neighbor)
        if has_left_neighbor:
            lower_left_neighbor = (x_coord + 1, y_coord - 1)
            neighbors.append(lower_left_neighbor)
        if has_right_neighbor:
            lower_right_neighbor = (x_coord + 1, y_coord + 1)
            neighbors.append(lower_right_neighbor)
    if has_left_neighbor:
        left_neighbor = (x_coord, y_coord - 1)
        neighbors.append(left_neighbor)
    if has_right_neighbor:
        right_neighbor = (x_coord, y_coord + 1)
        neighbors.append(right_neighbor)
    return neighbors


def count_flash(input_grid: List[List[int]]) -> int:
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    current_count = 0
    for x in range(max_x_value):
        for y in range(max_y_value):
            if input_grid[x][y] > 9:
                current_count = current_count + 1
    return current_count


def reset_every_one(input_grid: List[List[int]]) -> List[List[int]]:
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    for x in range(max_x_value):
        for y in range(max_y_value):
            if input_grid[x][y] > 9:
                input_grid[x][y] = 0
    return input_grid
