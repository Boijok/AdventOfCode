from pandas import DataFrame
from src.year_2022.day_1.input_values import input_values


def solve_2022_day_1_second_challenge() -> None:
    input_grid: DataFrame = DataFrame(input_values)
    sorted_grid = sorted(input_grid.sum(axis=1))
    answer = sum(sorted_grid[-3:])
    print(f"solve_2022_day_1_second_challenge solution is {answer}")
