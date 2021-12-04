from typing import List

from src.year_2021.day_4.input_values import input_grids, input_values


def solve_day_4_second_challenge() -> None:
    grids = input_grids
    cursor = 0
    value = -1
    last_grid_won = False
    while len(grids) > 0 and cursor < len(input_values) and not last_grid_won:
        value = input_values[cursor]
        grids = visit_grids(grids, value)
        winner_cursor = check_if_there_is_a_winner(grids)
        while winner_cursor >= 0 and not last_grid_won:
            if len(grids) > 1:
                del grids[winner_cursor]
                winner_cursor = check_if_there_is_a_winner(grids)
            elif len(grids) == 1:
                winner_cursor = check_if_there_is_a_winner(grids)
                last_grid_won = True
        cursor = cursor + 1
    score = compute_score(grids[0], value)
    print(f"solve_day_4_second_challenge solution is {score}")


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
    for col_index in range(0, len(grid[0])):
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
