from typing import List, Any
from pydantic import BaseModel
from src.year_2021.day_15.input_values import input_values


class GridPosition(BaseModel):
    x: int = 0
    y: int = 0


def solve_day_15_first_challenge() -> None:
    input_grid: List[List[int]] = input_values
    rotated_180_input_grid: List[List[int]] = rotate_grid_90(rotate_grid_90(input_grid))

    best_path_list_forward: List[int] = get_best_path_to_diag(input_grid)
    best_path_list_backward: List[int] = get_best_path_to_diag(rotated_180_input_grid)

    best_path_value = merge_best_path(
        input_grid, best_path_list_forward, best_path_list_backward
    )
    print(f"solve_day_15_first_challenge solution is {best_path_value}")


def get_grid_value(input_grid: List[List[int]], grid_position: GridPosition) -> int:
    return input_grid[grid_position.x][grid_position.y]


def get_best_path_to_diag(input_grid: List[List[int]]) -> List[int]:
    grid_size = len(input_grid)
    best_path_list: List[int] = []
    for diag_number in range(grid_size):
        new_best_path_list_forward: List[int] = []
        for x in range(diag_number + 1):
            y = diag_number - x
            grid_position = GridPosition(x=x, y=y)
            if x == y == 0:
                new_best_path_list_forward.append(
                    get_grid_value(input_grid, grid_position)
                )
            elif x == 0:
                new_best_path_list_forward.append(
                    best_path_list[x] + get_grid_value(input_grid, grid_position)
                )
            elif y == 0:
                new_best_path_list_forward.append(
                    best_path_list[-1] + get_grid_value(input_grid, grid_position)
                )
            else:
                best_choice = min(best_path_list[x - 1], best_path_list[x])
                new_best_path_list_forward.append(
                    best_choice + get_grid_value(input_grid, grid_position)
                )

        best_path_list = new_best_path_list_forward
    return best_path_list


def rotate_grid_90(input_grid: List[List[int]]) -> List[List[Any]]:
    return list(map(list, zip(*input_grid)))[::-1]


def merge_best_path(
    input_grid: List[List[int]],
    best_path_list_forward: List[int],
    best_path_list_backward: List[int],
) -> int:
    best_path_list: List[int] = []
    len_diag = len(best_path_list_forward)
    for i in range(len_diag):
        y = len_diag - i - 1
        grid_position = GridPosition(x=i, y=y)
        best_path_list.append(
            best_path_list_forward[i]
            + best_path_list_backward[-(i + 1)]
            - get_grid_value(input_grid, grid_position)
        )
    return min(best_path_list) - input_grid[0][0]
