from typing import List

from src.year_2021.day_4.input_values import input_grids, input_values


def solve_day_4_first_challenge() -> None:
    grids = input_grids
    no_winner = True
    cursor = 0
    value = -1
    winner_cursor = -1
    while no_winner and cursor < len(input_values):
        value = input_values[cursor]
        grids = visit_grids(grids, value)
        winner_cursor = check_if_there_is_a_winner(grids)
        if winner_cursor >= 0:
            no_winner = False
        else:
            cursor = cursor + 1
    score = compute_score(grids[winner_cursor], value)
    print(f"solve_day_4_first_challenge solution is {score}")


def visit_grids(grids: List[List[List[int]]], value: int) -> List[List[List[int]]]:
    new_grids = grids
    grid_number = 0
    for grid in grids:
        row_number = 0
        for row in grid:
            elem_number = 0
            for elem in row:
                if elem == value:
                    new_grids = update_grids(
                        new_grids, grid_number, row_number, elem_number
                    )
                elem_number = elem_number + 1
            row_number = row_number + 1
        grid_number = grid_number + 1
    return new_grids


def update_grids(
    grids: List[List[List[int]]], grid_number: int, row_number: int, elem_number: int
) -> List[List[List[int]]]:
    grids[grid_number][row_number][elem_number] = -1
    return grids


def check_if_there_is_a_winner(grids: List[List[List[int]]]) -> int:
    grid_number = 0
    for grid in grids:
        if is_grid_a_bingo(grid):
            return grid_number
        grid_number = grid_number + 1
    return -1


def is_grid_a_bingo(grid: List[List[int]]) -> bool:
    grid_row_a_bingo = check_grid_row(grid)
    grid_col_a_bingo = check_grid_col(grid)
    if grid_row_a_bingo or grid_col_a_bingo:
        return True
    else:
        return False


def check_grid_row(grid: List[List[int]]) -> bool:
    grid_row_a_bingo = False
    for row in grid:
        if sum(row) == -5:
            grid_row_a_bingo = True
    return grid_row_a_bingo


def check_grid_col(grid: List[List[int]]) -> bool:
    grid_col_a_bingo = False
    for col_index in range(0, len(grid[0]) - 1):
        partial_sum = 0
        for row in grid:
            partial_sum = partial_sum + row[col_index]
        if partial_sum == -5:
            grid_col_a_bingo = True
    return grid_col_a_bingo


def compute_score(grid: List[List[int]], value: int) -> int:
    sum_valid_values = 0
    for row in grid:
        for elem in row:
            if elem != -1:
                sum_valid_values = sum_valid_values + elem
    return sum_valid_values * value
