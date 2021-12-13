from typing import List, Tuple
from src.year_2021.day_13.input_values import input_values

test_fold_along = [
    ("y", 7),
    ("x", 5),
]

fold_along = [
    ("x", 655),
    ("y", 447),
    ("x", 327),
    ("y", 223),
    ("x", 163),
    ("y", 111),
    ("x", 81),
    ("y", 55),
    ("x", 40),
    ("y", 27),
    ("y", 13),
    ("y", 6),
]


def solve_day_13_second_challenge() -> None:
    input_points = input_values
    fold_along_instructions = fold_along
    initial_matrix = create_matrix(input_points)

    fold_matrix = initial_matrix
    for fold in fold_along_instructions:
        if fold[0] == "x":
            fold_matrix = fold_x(fold_matrix, fold[1])
        if fold[0] == "y":
            fold_matrix = fold_y(fold_matrix, fold[1])

    print("solve_day_13_second_challenge solution is")
    custom_print(reverse_list(fold_matrix))


def create_matrix(input_points: List[Tuple[int, int]]) -> List[List[int]]:
    max_x = 0
    max_y = 0
    for point in input_points:
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])
    matrix = []
    for i in range(max_x + 1):
        row = []
        for j in range(max_y + 1):
            row.append(0)
        matrix.append(row)
    for point in input_points:
        matrix[point[0]][point[1]] = 1
    return matrix


def fold_y(matrix: List[List[int]], y_row: int) -> List[List[int]]:
    part_1 = [sublist[:y_row] for sublist in matrix]
    part_2 = [sublist[(y_row + 1) :] for sublist in matrix]

    len_x = len(part_2)
    len_y = len(part_2[0])
    for i in range(len_x):
        for j in range(len_y):
            if part_2[i][j] == 1:
                part_1[i][len_y - j - 1] = 1
    return part_1


def fold_x(matrix: List[List[int]], x_row: int) -> List[List[int]]:
    part_1 = matrix[:x_row]
    part_2 = matrix[(x_row + 1) :]

    len_x = len(part_2)
    len_y = len(part_2[0])
    for i in range(len_x):
        for j in range(len_y):
            if part_2[i][j] == 1:
                part_1[len_x - i - 1][j] = 1
    return part_1


def count_dot(matrix: List[List[int]]) -> int:
    current_sum = 0
    for row in matrix:
        current_sum = current_sum + sum(row)
    return current_sum


def reverse_list(matrix: List[List[int]]) -> List[List[int]]:
    new_matrix = []
    len_x = len(matrix)
    len_y = len(matrix[0])
    for j in range(len_y):
        row = []
        for i in range(len_x):
            row.append(matrix[i][j])
        new_matrix.append(row)
    return new_matrix


def custom_print(matrix: List[List[int]]) -> None:
    len_x = len(matrix)
    len_y = len(matrix[0])
    for x in range(len_x):
        for y in range(len_y):
            if matrix[x][y] == 1:
                print("##", end="")
            else:
                print("..", end="")
        print()
